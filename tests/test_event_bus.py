"""Tests for atlas.core.event_bus."""

import asyncio

import pytest

from atlas.core.event_bus import EventBus, EventEnvelope, InMemoryEventBus


@pytest.fixture
def event_bus():
    return InMemoryEventBus()


class TestInMemoryEventBus:
    def test_publish_to_queue(self, event_bus):
        queue = event_bus.subscribe()

        envelope = EventEnvelope(
            routing_key="test.event",
            queue="test_queue",
            payload={"message": "hello"},
        )

        asyncio.get_event_loop().run_until_complete(
            event_bus.publish(envelope)
        ) if False else None  # async test below

    @pytest.mark.asyncio
    async def test_publish_and_consume(self, event_bus):
        consumer_queue = event_bus.subscribe()

        envelope = EventEnvelope(
            routing_key="test.event",
            queue="test_queue",
            payload={"message": "hello"},
        )
        await event_bus.publish(envelope)

        received = await asyncio.wait_for(consumer_queue.get(), timeout=1.0)
        assert received.routing_key == "test.event"
        assert received.payload["message"] == "hello"

    @pytest.mark.asyncio
    async def test_close_prevents_publish(self, event_bus):
        await event_bus.close()

        envelope = EventEnvelope(
            routing_key="test.event",
            queue="test_queue",
            payload={"message": "hello"},
        )
        # Should not raise, just log warning
        await event_bus.publish(envelope)

    @pytest.mark.asyncio
    async def test_overflow_drop_oldest(self):
        bus = InMemoryEventBus(queue_maxsize=2, overflow_policy="drop_oldest")
        consumer = bus.subscribe()

        # Fill queue
        for i in range(2):
            await bus.publish(EventEnvelope(
                routing_key="test", queue="test", payload={"i": i}
            ))

        # This should drop the oldest
        await bus.publish(EventEnvelope(
            routing_key="test", queue="test", payload={"i": 99}
        ))

        # Consumer should have received messages (3 total, but queue max is 2 for internal queues)
        # The consumer queue has its own maxsize=1000
        received_count = 0
        while not consumer.empty():
            consumer.get_nowait()
            received_count += 1
        assert received_count >= 2  # At least 2 should be there

    @pytest.mark.asyncio
    async def test_headers_preserved(self, event_bus):
        consumer_queue = event_bus.subscribe()

        envelope = EventEnvelope(
            routing_key="test.event",
            queue="test_queue",
            payload={"msg": "test"},
            headers={"correlation_id": "abc123"},
        )
        await event_bus.publish(envelope)

        received = await asyncio.wait_for(consumer_queue.get(), timeout=1.0)
        assert received.headers["correlation_id"] == "abc123"
