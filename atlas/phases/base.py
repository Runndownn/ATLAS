"""Base phase implementation for ATLAS pipeline phases.

Extracted from Yggdrasil's _execute_phase dispatch pattern and generalized
for any pipeline phase. Phases are plugin-implementable.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Protocol

from atlas.core.event_bus import EventBus, EventEnvelope
from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig

logger = logging.getLogger("atlas.phases.base")


@dataclass
class PhaseProgress:
    """Progress state for a phase."""

    percent: float = 0.0
    processed: int = 0
    total: int = 0
    message: str = ""


class Phase(ABC):
    """Abstract base class for pipeline phases.

    Each phase processes artifacts from the discovery phase and emits
    events for observability. Phases are designed to be independently
    runnable and pausable.

    To implement a custom phase, subclass Phase and implement execute().
    """

    #: The phase name (must match PipelinePhase or a custom phase ID)
    name: str = "base"

    #: Whether this phase can be safely retried after failure
    retryable: bool = True

    def __init__(self, event_bus: EventBus | None = None):
        self._event_bus = event_bus
        self._progress = PhaseProgress()

    @abstractmethod
    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        """Execute the phase logic.

        Args:
            job: The current pipeline job record.
            config: Pipeline configuration (source path, phases, metadata).
            phase_record: The phase record to update with progress.

        Raises:
            Exception: Any error during execution. The orchestrator will
                       record the error and handle retry/abort.
        """
        ...

    @property
    def progress(self) -> PhaseProgress:
        """Current progress of this phase."""
        return self._progress

    def update_progress(
        self,
        percent: float,
        processed: int | None = None,
        total: int | None = None,
        message: str | None = None,
    ) -> None:
        """Update phase progress (call from within execute)."""
        self._progress.percent = percent
        if processed is not None:
            self._progress.processed = processed
        if total is not None:
            self._progress.total = total
        if message is not None:
            self._progress.message = message

    async def emit_event(
        self,
        job: JobRecord,
        event_type: str,
        payload: dict[str, Any] | None = None,
    ) -> None:
        """Emit a phase lifecycle event."""
        if self._event_bus is None:
            return

        full_payload = {
            "event_type": event_type,
            "category": "atlas.phase",
            "job_id": job.job_id,
            "phase": self.name,
            "progress": self._progress.percent,
        }
        if payload:
            full_payload.update(payload)

        envelope = EventEnvelope(
            routing_key=f"atlas.phase.{self.name}.{event_type}",
            queue="atlas.phase",
            payload=full_payload,
        )
        await self._event_bus.publish(envelope)


class PhaseHandler(Protocol):
    """Protocol for phase handlers compatible with PipelineOrchestrator."""

    async def execute(self, job: JobRecord, config: PipelineConfig) -> None:
        """Execute the phase."""
        ...
