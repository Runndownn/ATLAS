# Extending ATLAS Pipeline Phases

This guide explains how to create, register, and package custom pipeline phases.

## Phase Model

ATLAS pipelines are sequences of phases executed in order by `PipelineOrchestrator`. Each phase is a callable conforming to the `PhaseHandler` protocol. The canonical `Phase` ABC (`atlas.phases.base.Phase`) provides a convenient base class with progress reporting and event emission.

The six built-in phases are defined by `PipelinePhase`:

| Member | Value | Role |
|--------|-------|------|
| `RECONNAISSANCE` | reconnaissance | Discover + assess input artifacts |
| `FINGERPRINTING` | fingerprinting | Hash + identity artifacts |
| `STRUCTURAL_DISCOVERY` | structural_discovery | Inspect archive structure without extracting |
| `CONTROLLED_EXTRACTION` | controlled_extraction | Safe content extraction within safety limits |
| `DEEP_UNDERSTANDING` | deep_understanding | Analysis of extracted content |
| `REVIEW_PROMOTION` | review_promotion | Promote results to knowledge stores |

## Implementing a Phase

Subclass `Phase` (or implement `PhaseHandler` directly) and implement `execute`.

```python
import logging
from atlas.core.event_bus import EventBus
from atlas.phases.base import Phase, PhaseProgress
from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig

logger = logging.getLogger("atlas.phases.custom")

class CustomPhase(Phase):
    name = "custom_phase"
    retryable = True  # set False if the phase has side effects that make retries unsafe

    def __init__(self, event_bus: EventBus | None = None):
        super().__init__(event_bus)

    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        # Bind job + progress tracking
        self._bind(job, phase_record)

        total = 100
        for i in range(total):
            # Check for pause/cancel is handled by the orchestrator loop;
            # for long loops, you may poll job status via the job_store if needed.
            self.update_progress(
                percent=round((i + 1) / total * 100, 1),
                processed=i + 1,
                total=total,
                message=f"processing item {i + 1}",
            )
            # ... your phase logic ...

            # Emit a domain event
            await self.emit_event(
                job,
                "item_processed",
                {"index": i, "result": "ok"},
            )
```

### PhaseHandler Protocol (Minimal)

If you prefer not to subclass `Phase`, implement the protocol directly:

```python
from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig, PhaseHandler

class MyPhase:
    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        ...
```

## Registering a Phase

### Via AtlasRuntime (Recommended)

`AtlasRuntime` is the canonical composition root. Register handlers before `start_pipeline`:

```python
import asyncio
from atlas.core.runtime import AtlasRuntime
from atlas.core.orchestrator import PipelinePhase
from my_phases import CustomPhase

async def main():
    runtime = AtlasRuntime(db_path="jobs.db")
    await runtime.connect()

    # Register a custom phase for an existing PipelinePhase member
    runtime.register_phase_handler(PipelinePhase.REVIEW_PROMOTION, CustomPhase(
        event_bus=runtime.event_bus,
    ))

    config = PipelineConfig(
        pipeline_id="my-run",
        name="custom-pipeline",
        phases=[PipelinePhase.REVIEW_PROMOTION],
        source_path="/path/to/input",
    )
    # Ensure config.metadata includes abort_on_error / continue_on_phase_error if needed
    job = await runtime.orchestrator.start_pipeline(config)
    await runtime.close()

asyncio.run(main())
```

### Via PipelineOrchestrator Directly

```python
from atlas.core.orchestrator import PipelineOrchestrator, PipelinePhase

orchestrator = PipelineOrchestrator(
    job_store=job_store,
    event_bus=event_bus,
    phase_handlers={PipelinePhase.REVIEW_PROMOTION: MyPhase()},
)
```

## Custom Phase Identifiers

To register a phase that is not one of the six `PipelinePhase` members, you must extend the enum or use a standalone phase outside the standard ordering. ATLAS does not currently support arbitrary string phase IDs in the ordered enum; the recommended approach is to map custom logic into the `REVIEW_PROMOTION` slot or create a wrapper that runs additional work as part of a standard phase.

## Error Handling and Retry

- An exception raised from `execute` is caught by the orchestrator, recorded on the `PhaseRecord` (`status=error`, `error` set), and increments `job.error_count`.
- If `metadata.abort_on_error` is `True` (default), the pipeline stops and the job records status `error`.
- If `metadata.abort_on_error` is `False` (or `continue_on_phase_error` is `True`), the orchestrator proceeds to the next phase.
- Set `retryable = False` on phases with non-idempotent side effects to signal that automatic retry should not be attempted.

## Progress Reporting

Call `self.update_progress(...)` from within `execute` to update both the in-memory `PhaseProgress` and the persisted `PhaseRecord`. The orchestrator flushes `phase_record` to SQLite after `execute` returns.

## Event Emission

Use `self.emit_event(job, event_type, payload)` to publish structured events. Events are routed to:

- The event bus (in-memory or RabbitMQ) under routing key `atlas.phase.<name>.<event_type>`.
- The SQLite `atlas_events` table via the job store's event log.

## Packaging Custom Phases

1. Place phase modules under a package (e.g., `my_atlas_phases/`).
2. Register during application startup (e.g., in a factory function or main module).
3. For PyPI distribution, add an entry point if you want discoverability:

```toml
[project.entry-points."atlas.phases"]
custom_phase = "my_atlas_phases:CustomPhase"
```

ATLAS does not yet auto-discover entry points; registration must be done programmatically via `AtlasRuntime.register_phase_handler`.

## See Also

- `atlas/phases/base.py` — `Phase` ABC and `PhaseProgress`
- `atlas/core/orchestrator.py` — `PhaseHandler` protocol, `_run_pipeline` dispatch
- `atlas/core/runtime.py` — `AtlasRuntime` composition root
- `atlas/docs/guides/event-bus-integration.md` — consuming phase events
