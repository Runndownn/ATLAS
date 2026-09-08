# ATLAS Event Bus Integration Guide

ATLAS emits structured lifecycle events at every stage of pipeline execution. This guide covers the event bus backends, event schema, and how to consume events.

## Backends

ATLAS ships two event bus implementations in `atlas/core/event_bus.py`:

| Class | Backend | Default | Description |
|-------|---------|---------|-------------|
| `InMemoryEventBus` | asyncio queues | Yes | Zero-dependency, in-process event delivery. Suitable for single-process deployments and testing. |
| `RabbitMQEventBus` | AMQP (via `aio-pika`) | No | Distributed, durable pub/sub. Falls back to `InMemoryEventBus` when RabbitMQ is unreachable or `aio-pika` is not installed. |

### Selecting a Backend

By default, `AtlasRuntime` constructs an `InMemoryEventBus`. To use RabbitMQ:

```python
from atlas.core.event_bus import RabbitMQEventBus
from atlas.core.runtime import AtlasRuntime

event_bus = RabbitMQEventBus(
    url="amqp://guest:guest@localhost:5672/",
    exchange="atlas.events",
    fallback=True,  # fall back to in-memory if broker unreachable
)

runtime = AtlasRuntime(db_path="jobs.db", event_bus=event_bus)
await runtime.connect()

# RabbitMQEventBus.connect() is called automatically by the orchestrator
# on first publish if not yet connected. To connect eagerly:
if hasattr(event_bus, "connect"):
    await event_bus.connect()
```

RabbitMQ support is optional. Install it with:

```bash
pip install atlas-pipeline[rabbitmq]
```

If `aio-pika` is missing, `RabbitMQEventBus` logs a warning and uses the in-memory fallback transparently.

## Event Envelope

All events use the `EventEnvelope` dataclass:

```python
@dataclass
class EventEnvelope:
    routing_key: str      # e.g. "atlas.pipeline.started"
    queue: str            # logical queue group, e.g. "atlas.pipeline" or "atlas.phase"
    payload: dict[str, Any] # event body
    headers: dict[str, Any] = {}
    attempt: int = 1
    published_at: datetime
```

### Event Categories

Events fall into two categories based on their `queue` field:

- **`atlas.pipeline`** — job-level lifecycle events emitted by the orchestrator.
- **`atlas.phase`** — phase-level events emitted by phase handlers via `Phase.emit_event`.

## Event Types

### Pipeline-Level Events (routing key: `atlas.pipeline.*`)

| Event | Trigger | Payload extras |
|-------|---------|----------------|
| `pipeline.started` | Pipeline begins execution | none |
| `phase.<name>.started` | Each phase begins | `phase_id` |
| `phase.<name>.completed` | Each phase completes | `phase_id` |
| `pipeline.errored` | Pipeline aborts on error | `error` |
| `pipeline.paused` | `pause_pipeline` called | none |
| `pipeline.resumed` | `resume_pipeline` called | none |
| `pipeline.cancelled` | `cancel_pipeline` called | none |
| `pipeline.<status>` | Final status (completed/error/cancelled) | none |

### Phase-Level Events (routing key: `atlas.phase.<phase>.<event_type>`)

Phase handlers may emit arbitrary events via `self.emit_event(job, event_type, payload)`. The envelope payload always includes:

```python
{
    "event_type": ...,
    "category": "atlas.phase",
    "job_id": ...,
    "phase": <phase name>,
    "progress": <percent>,
    # ... plus any extra keys from the payload argument
}
```

## Consuming Events

### In-Memory Subscription

```python
from atlas.core.event_bus import InMemoryEventBus

bus = InMemoryEventBus()
consumer_queue = bus.subscribe()

import asyncio
async for envelope in consumer_queue:
    print(envelope.routing_key, envelope.payload)
```

> `InMemoryEventBus.subscribe()` returns a separate consumer queue per subscriber. Each subscriber receives every published event.

### RabbitMQ Subscription

For RabbitMQ, use standard `aio-pika` consumers on the `atlas.events` exchange:

```python
import aio_pika

async def consume():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost:5672/")
    channel = await connection.channel()
    exchange = await channel.declare_exchange("atlas.events", aio_pika.ExchangeType.FANOUT)
    queue = await channel.declare_queue("atlas_consumer", auto_delete=True)
    await queue.bind(exchange, routing_key="#")

    async with queue.iterator() as iterator:
        async for message in iterator:
            async with message.process():
                print(message.routing_key, message.body.decode())
```

## Event Persistence

Regardless of the event bus backend, the orchestrator also persists every job-level and phase-level event to the SQLite `atlas_events` table via `JobStore.store_event`. This provides a durable event log even when using the in-memory bus:

```sql
SELECT routing_key, payload, created_at
FROM atlas_events
WHERE job_id = ?
ORDER BY created_at;
```

Phase-level events emitted by custom handlers are **not** persisted to SQLite automatically — only orchestrator-emitted events are. To persist phase events, insert them directly via the job store or emit them through the orchestrator.

## Failover Behavior

When `RabbitMQEventBus` cannot connect to the broker:

1. If `aio_pika` is not installed → uses in-memory fallback immediately.
2. If the broker is unreachable → logs a warning and uses in-memory fallback (when `fallback=True`, the default).
3. Events are never lost from the in-memory queue for the lifetime of the process.

For production deployments requiring event durability across process restarts, ensure `db_path` points to a persistent SQLite file. Job records and events persist there; subscriber queues (in-memory or RabbitMQ) do not.

## See Also

- `atlas/core/event_bus.py` — `EventBus`, `InMemoryEventBus`, `RabbitMQEventBus`, `EventEnvelope`
- `atlas/core/orchestrator.py` — `_emit_job_event`, event persistence via `JobStore`
- `atlas/core/runtime.py` — `AtlasRuntime` event bus injection
- `atlas/docs/guides/extending-phases.md` — emitting events from custom phases
- `atlas/docs/guides/deployment.md` — RabbitMQ deployment configuration
