"""Event bus for ATLAS — dual backend (in-memory + RabbitMQ).

Extracted from geezer-mekanix's InMemoryBroker / RabbitMQFanoutPublisher pattern,
generalized for standalone use with graceful fallback.
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

logger = logging.getLogger("atlas.event_bus")

# Try optional RabbitMQ support
try:
    import aio_pika  # type: ignore
    _AIO_PIKA_AVAILABLE = True
except ImportError:
    _AIO_PIKA_AVAILABLE = False
    aio_pika = None  # type: ignore


@dataclass
class EventEnvelope:
    """Envelope wrapping an event for bus transport."""

    routing_key: str
    queue: str
    payload: dict[str, Any]
    headers: dict[str, Any] = field(default_factory=dict)
    attempt: int = 1
    published_at: datetime = field(default_factory=lambda: datetime.now(UTC))


class EventBus:
    """Abstract event bus interface."""

    async def publish(self, envelope: EventEnvelope) -> None:
        """Publish an event envelope."""
        raise NotImplementedError

    async def close(self) -> None:
        """Clean up resources."""
        pass


class InMemoryEventBus(EventBus):
    """asyncio-backed in-memory event bus.

    Mirrors the InMemoryBroker pattern from geezer-mekanix for scenarios
    where RabbitMQ is unavailable or not configured.
    """

    def __init__(
        self,
        *,
        queue_maxsize: int = 0,
        overflow_policy: str = "drop_oldest",
    ) -> None:
        self._queues: dict[str, asyncio.Queue[EventEnvelope]] = {}
        self._queue_maxsize = max(0, int(queue_maxsize))
        self._overflow_policy = (overflow_policy or "").strip().lower() or None
        self._consumers: list[asyncio.Queue[EventEnvelope]] = []
        self._closed = False

    def _queue(self, name: str) -> asyncio.Queue[EventEnvelope]:
        queue = self._queues.get(name)
        if queue is None:
            if self._queue_maxsize > 0:
                queue = asyncio.Queue(maxsize=self._queue_maxsize)
            else:
                queue = asyncio.Queue()
            self._queues[name] = queue
        return queue

    async def publish(self, envelope: EventEnvelope) -> None:
        """Publish an event to the in-memory bus."""
        if self._closed:
            logger.warning("publish on closed EventBus")
            return

        queue = self._queue(envelope.queue)
        dropped = False
        queued = False

        try:
            queue.put_nowait(envelope)
            queued = True
        except asyncio.QueueFull:
            if self._overflow_policy == "drop_oldest":
                try:
                    queue.get_nowait()
                except asyncio.QueueEmpty:
                    pass
                try:
                    queue.put_nowait(envelope)
                    queued = True
                    dropped = True
                except asyncio.QueueFull:
                    dropped = True
                    queued = False
            elif self._overflow_policy == "drop_newest":
                dropped = True
                queued = False
            else:
                # Preserve legacy semantics: await
                await queue.put(envelope)
                queued = True

        if dropped:
            logger.warning(
                "event_bus_queue_overflow",
                extra={
                    "queue": envelope.queue,
                    "routing_key": envelope.routing_key,
                    "policy": self._overflow_policy or "unknown",
                },
            )

        # Notify any consumers
        for consumer_queue in self._consumers:
            try:
                if consumer_queue.full():
                    # Drop oldest if full
                    try:
                        consumer_queue.get_nowait()
                    except asyncio.QueueEmpty:
                        pass
                consumer_queue.put_nowait(envelope)
            except asyncio.QueueFull:
                pass

    def subscribe(self) -> asyncio.Queue[EventEnvelope]:
        """Subscribe to all events (returns a consumer queue)."""
        queue: asyncio.Queue[EventEnvelope] = asyncio.Queue(maxsize=1000)
        self._consumers.append(queue)
        return queue

    async def close(self) -> None:
        """Close the event bus."""
        self._closed = True
        self._consumers.clear()


class RabbitMQEventBus(EventBus):
    """RabbitMQ-backed event bus with in-memory fallback.

    Uses aio-pika for async RabbitMQ access. Falls back to
    InMemoryEventBus behavior when the broker is unreachable.
    """

    def __init__(
        self,
        url: str = "amqp://guest:guest@localhost:5672/",
        *,
        exchange: str = "atlas.events",
        fallback: bool = True,
    ) -> None:
        self._url = url
        self._exchange_name = exchange
        self._fallback = fallback
        self._connection: aio_pika.AbstractRobustConnection | None = None
        self._channel: aio_pika.AbstractChannel | None = None
        self._exchange: aio_pika.AbstractExchange | None = None
        self._in_memory_fallback: InMemoryEventBus | None = None

    async def connect(self) -> None:
        """Establish connection to RabbitMQ (or fall back to memory)."""
        if not _AIO_PIKA_AVAILABLE:
            logger.warning("aio-pika not installed; using in-memory fallback")
            self._in_memory_fallback = InMemoryEventBus()
            return

        try:
            self._connection = await aio_pika.connect_robust(self._url)
            self._channel = await self._connection.channel()
            self._exchange = await self._channel.declare_exchange(
                self._exchange_name,
                aio_pika.ExchangeType.FANOUT,
            )
            logger.info("Connected to RabbitMQ at %s", self._url)
        except Exception as exc:
            logger.warning("RabbitMQ connection failed (%s); using fallback", exc)
            if self._fallback:
                self._in_memory_fallback = InMemoryEventBus()

    async def publish(self, envelope: EventEnvelope) -> None:
        """Publish an event to RabbitMQ or fallback."""
        if self._exchange and self._connection:
            try:
                message = aio_pika.Message(
                    body=__import__("json").dumps(envelope.payload).encode(),
                    headers={**envelope.headers, "routing_key": envelope.routing_key},
                    timestamp=int(envelope.published_at.timestamp()),
                )
                await self._exchange.publish(message, routing_key=envelope.routing_key)
                return
            except Exception as exc:
                logger.warning("RabbitMQ publish failed (%s); falling back", exc)

        if self._in_memory_fallback:
            await self._in_memory_fallback.publish(envelope)
        else:
            logger.debug("Event bus not connected; dropping: %s", envelope.routing_key)

    async def close(self) -> None:
        """Close connections."""
        if self._connection:
            await self._connection.close()
        if self._in_memory_fallback:
            await self._in_memory_fallback.close()
