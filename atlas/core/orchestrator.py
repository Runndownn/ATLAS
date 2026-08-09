"""Adaptive Task Lifecycle Engine for Staged Artifact Processing.

This module provides the core orchestration layer — a phase-based pipeline
engine that sequences work stages, tracks async job state, and emits
events for observability.

Extracted from the Yggdrasil knowledge-fabric orchestrator and generalized
for any multi-phase batch processing workflow.
"""

from __future__ import annotations

import asyncio
import logging
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from typing import Any, Protocol

from atlas.core.event_bus import EventBus, EventEnvelope
from atlas.core.job_store import JobRecord, JobStore, PhaseRecord

logger = logging.getLogger("atlas.orchestrator")


class PipelinePhase(str, Enum):
    """Pipeline phase enumeration (generic, orderable)."""

    RECONNAISSANCE = "reconnaissance"      # Phase A — discover + assess
    FINGERPRINTING = "fingerprinting"       # Phase B — hash + identity
    STRUCTURAL_DISCOVERY = "structural_discovery"  # Phase C — context + structure
    CONTROLLED_EXTRACTION = "controlled_extraction"  # Phase D — safe content
    DEEP_UNDERSTANDING = "deep_understanding"   # Phase E — analysis
    REVIEW_PROMOTION = "review_promotion"   # Phase F — promote to knowledge


class PipelineStatus(str, Enum):
    """Pipeline run status."""

    PENDING = "pending"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    ERROR = "error"
    CANCELLED = "cancelled"


@dataclass
class PipelineConfig:
    """Configuration for a pipeline run."""

    pipeline_id: str
    name: str
    phases: list[PipelinePhase] = field(default_factory=list)
    source_path: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def default(cls, source_path: str, name: str = "default") -> "PipelineConfig":
        """Create a default config with all phases."""
        return cls(
            pipeline_id=str(uuid.uuid4()),
            name=name,
            phases=list(PipelinePhase),
            source_path=source_path,
        )


class PhaseHandler(Protocol):
    """Protocol for phase handlers (plugin interface)."""

    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
    ) -> None:
        """Execute a phase for the given job."""
        ...


class PipelineOrchestrator:
    """Orchestrates multi-phase pipeline execution.

    Extracted from Yggdrasil's CrawlJob/CrawlPhase/CrawlStatus pattern,
    generalized to support any pipeline with pause/resume/cancel semantics.
    """

    def __init__(
        self,
        job_store: JobStore,
        event_bus: EventBus,
        phase_handlers: dict[PipelinePhase, PhaseHandler] | None = None,
    ):
        self._job_store = job_store
        self._event_bus = event_bus
        self._phase_handlers = phase_handlers or {}
        self._jobs: dict[str, JobRecord] = {}
        self._lock = asyncio.Lock()

    async def start_pipeline(
        self,
        config: PipelineConfig,
        phases: list[PipelinePhase] | None = None,
    ) -> JobRecord:
        """Start a new pipeline run."""
        job = JobRecord(
            job_id=config.pipeline_id,
            root_id=str(uuid.uuid4()),
            source_path=config.source_path,
            phase=PipelinePhase.RECONNAISSANCE,
            status=PipelineStatus.PENDING,
            metadata=config.metadata,
        )

        async with self._lock:
            self._jobs[job.job_id] = job
            await self._job_store.create_job(job)

        # Start execution in background
        asyncio.create_task(self._run_pipeline(job, phases or config.phases))

        return job

    async def _run_pipeline(
        self,
        job: JobRecord,
        phases: list[PipelinePhase],
    ) -> None:
        """Execute pipeline phases sequentially."""
        job.status = PipelineStatus.RUNNING
        job.started_at = datetime.now(UTC)

        await self._job_store.update_job(job)
        await self._emit_job_event(job, "pipeline.started")

        for phase in phases:
            if job.status in (PipelineStatus.CANCELLED, PipelineStatus.PAUSED):
                break

            job.phase = phase
            phase_record = PhaseRecord(
                phase_id=str(uuid.uuid4()),
                job_id=job.job_id,
                phase=phase.value,
                status=PipelineStatus.RUNNING,
                started_at=datetime.now(UTC),
            )
            await self._job_store.add_phase_record(phase_record)
            await self._emit_job_event(job, f"phase.{phase.value}.started")

            try:
                handler = self._phase_handlers.get(phase)
                if handler:
                    config = PipelineConfig(
                        pipeline_id=job.job_id,
                        name=job.metadata.get("pipeline_name", "default"),
                        phases=phases,
                        source_path=job.source_path,
                        metadata=job.metadata,
                    )
                    await handler.execute(job, config)
                else:
                    logger.warning("No handler registered for phase %s", phase.value)

                phase_record.status = PipelineStatus.COMPLETED
                phase_record.completed_at = datetime.now(UTC)
                phase_record.progress_percent = 100.0
                await self._job_store.update_phase_record(phase_record)
                await self._emit_job_event(job, f"phase.{phase.value}.completed", {
                    "phase_id": phase_record.phase_id,
                })
            except Exception as exc:
                logger.error("Phase %s failed: %s", phase.value, exc, exc_info=True)
                job.error_count += 1
                job.last_error = str(exc)
                phase_record.status = PipelineStatus.ERROR
                phase_record.completed_at = datetime.now(UTC)
                phase_record.error = str(exc)
                await self._job_store.update_phase_record(phase_record)
                await self._job_store.update_job(job)

                # Error handling: continue or abort
                abort = job.metadata.get("abort_on_error", True)
                if abort:
                    job.status = PipelineStatus.ERROR
                    await self._emit_job_event(job, "pipeline.errored", {"error": str(exc)})
                    break

        if job.status not in (PipelineStatus.CANCELLED, PipelineStatus.PAUSED, PipelineStatus.ERROR):
            job.status = PipelineStatus.COMPLETED
            job.completed_at = datetime.now(UTC)

        await self._job_store.update_job(job)
        await self._emit_job_event(job, f"pipeline.{job.status.value}")

    async def pause_pipeline(self, job_id: str) -> bool:
        """Pause a running pipeline."""
        async with self._lock:
            job = self._jobs.get(job_id)
            if job is None:
                return False
            if job.status == PipelineStatus.RUNNING:
                job.status = PipelineStatus.PAUSED
                job.paused_at = datetime.now(UTC)
                await self._job_store.update_job(job)
                await self._emit_job_event(job, "pipeline.paused")
                return True
            return False

    async def resume_pipeline(self, job_id: str) -> bool:
        """Resume a paused pipeline."""
        async with self._lock:
            job = self._jobs.get(job_id)
            if job is None:
                return False
            if job.status == PipelineStatus.PAUSED:
                job.status = PipelineStatus.RUNNING
                job.resumed_at = datetime.now(UTC)
                await self._job_store.update_job(job)
                await self._emit_job_event(job, "pipeline.resumed")

                # Restart from current phase
                phases_from_current = list(PipelinePhase)[
                    list(PipelinePhase).index(job.phase):
                ] if job.phase in [p.value for p in PipelinePhase] else [PipelinePhase.RECONNAISSANCE]
                # Convert string back to enum
                phase_enum = PipelinePhase(job.phase)
                start_index = list(PipelinePhase).index(phase_enum)
                phases_from_current = list(PipelinePhase)[start_index:]
                asyncio.create_task(self._run_pipeline(job, phases_from_current))
                return True
            return False

    async def cancel_pipeline(self, job_id: str) -> bool:
        """Cancel a running or paused pipeline."""
        async with self._lock:
            job = self._jobs.get(job_id)
            if job is None:
                return False
            if job.status in (PipelineStatus.RUNNING, PipelineStatus.PAUSED):
                job.status = PipelineStatus.CANCELLED
                job.cancelled_at = datetime.now(UTC)
                await self._job_store.update_job(job)
                await self._emit_job_event(job, "pipeline.cancelled")
                return True
            return False

    async def get_job(self, job_id: str) -> JobRecord | None:
        """Get job by ID."""
        return self._jobs.get(job_id) or await self._job_store.get_job(job_id)

    async def list_jobs(self) -> list[JobRecord]:
        """List all tracked jobs."""
        return await self._job_store.list_jobs()

    async def register_phase_handler(self, phase: PipelinePhase, handler: PhaseHandler) -> None:
        """Register a handler for a pipeline phase."""
        self._phase_handlers[phase] = handler

    async def _emit_job_event(
        self,
        job: JobRecord,
        event_type: str,
        extra: dict[str, Any] | None = None,
    ) -> None:
        """Emit a job lifecycle event."""
        payload = {
            "event_type": event_type,
            "category": "atlas",
            "job_id": job.job_id,
            "pipeline_id": job.job_id,
            "phase": job.phase,
            "status": job.status.value,
            "progress_percent": job.progress_percent,
            "source_path": job.source_path,
        }
        if extra:
            payload.update(extra)

        envelope = EventEnvelope(
            routing_key=f"atlas.pipeline.{event_type}",
            queue="atlas.pipeline",
            payload=payload,
        )
        await self._event_bus.publish(envelope)

    def set_progress(self, job_id: str, percent: float) -> None:
        """Update progress for a job (callable from phase handlers)."""
        # This is not async-safe for direct mutation; use update_progress instead
        # Kept for interface compatibility
        job = self._jobs.get(job_id)
        if job:
            job.progress_percent = percent
