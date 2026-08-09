"""AtlasRuntime — canonical composition root for ATLAS.

Ensures every phase handler is registered at startup. Eliminates the
fail-open behavior where missing handlers cause phases to be silently
marked COMPLETED.

Extracted from the BinReaper assessment finding: "atlas run creates a
new orchestrator but never registers the built-in phase handlers."
"""

from __future__ import annotations

import logging
from pathlib import Path

from atlas.core.event_bus import EventBus, InMemoryEventBus
from atlas.core.job_store import JobStore
from atlas.core.orchestrator import (
    PipelineOrchestrator,
    PipelinePhase,
    PhaseHandler,
)
from atlas.phases.analysis import AnalysisPhase
from atlas.phases.extraction import ExtractionPhase
from atlas.phases.fingerprinting import FingerprintingPhase
from atlas.phases.reconnaissance import ReconnaissancePhase
from atlas.phases.review import ReviewPhase
from atlas.safety.archive_safety import ArchiveSafetyService
from atlas.safety.filesystem_discovery import FilesystemDiscovery
from atlas.storage.hash_store import HashStore

logger = logging.getLogger("atlas.runtime")


class AtlasRuntime:
    """Canonical composition root.

    Creates and wires all shared services and phase handlers in one
    place. This is the single path through which the CLI, tests, and
    any future API layer should construct an orchestrator.

    Usage:
        runtime = AtlasRuntime(db_path=":memory:")
        orchestrator = runtime.orchestrator
        await orchestrator.start_pipeline(config)
    """

    def __init__(
        self,
        db_path: str = ":memory:",
        event_bus: EventBus | None = None,
        *,
        max_uncompressed_bytes: int | None = None,
        max_members: int | None = None,
    ):
        self._db_path = db_path
        self._event_bus = event_bus or InMemoryEventBus()
        self._job_store = JobStore(db_path)

        # Shared safety/storage services
        archive_kwargs: dict = {}
        if max_uncompressed_bytes is not None:
            archive_kwargs["max_uncompressed_bytes"] = max_uncompressed_bytes
        if max_members is not None:
            archive_kwargs["max_members"] = max_members

        self._filesystem_discovery = FilesystemDiscovery()
        self._archive_safety = ArchiveSafetyService(**archive_kwargs)
        self._path_safety = None  # Lazy: requires root_path; created on demand
        self._hash_store = HashStore()

        self._phase_handlers: dict[PipelinePhase, PhaseHandler] = {}
        self._build_default_handlers()

        self._orchestrator: PipelineOrchestrator | None = None
        self._connected = False

    def _build_default_handlers(self) -> None:
        """Register all built-in phase handlers."""
        # Phase A — Reconnaissance
        self._phase_handlers[PipelinePhase.RECONNAISSANCE] = ReconnaissancePhase(
            discovery=self._filesystem_discovery,
            archive_safety=self._archive_safety,
        )

        # Phase B — Fingerprinting
        self._phase_handlers[PipelinePhase.FINGERPRINTING] = FingerprintingPhase(
            hash_store=self._hash_store,
        )

        # Phase C — Structural Discovery
        self._phase_handlers[PipelinePhase.STRUCTURAL_DISCOVERY] = ExtractionPhase(
            archive_safety=self._archive_safety,
        )

        # Phase D — Controlled Extraction
        self._phase_handlers[PipelinePhase.CONTROLLED_EXTRACTION] = ExtractionPhase(
            archive_safety=self._archive_safety,
        )

        # Phase E — Deep Understanding
        self._phase_handlers[PipelinePhase.DEEP_UNDERSTANDING] = AnalysisPhase()

        # Phase F — Review / Promotion
        self._phase_handlers[PipelinePhase.REVIEW_PROMOTION] = ReviewPhase()

    @property
    def orchestrator(self) -> PipelineOrchestrator:
        """Get the orchestrator with all handlers registered."""
        if self._orchestrator is not None:
            return self._orchestrator

        self._orchestrator = PipelineOrchestrator(
            job_store=self._job_store,
            event_bus=self._event_bus,
            phase_handlers=dict(self._phase_handlers),
        )
        return self._orchestrator

    @property
    def job_store(self) -> JobStore:
        return self._job_store

    @property
    def event_bus(self) -> EventBus:
        return self._event_bus

    @property
    def hash_store(self) -> HashStore:
        return self._hash_store

    @property
    def filesystem_discovery(self) -> FilesystemDiscovery:
        return self._filesystem_discovery

    @property
    def archive_safety(self) -> ArchiveSafetyService:
        return self._archive_safety

    @property
    def phase_handlers(self) -> dict[PipelinePhase, PhaseHandler]:
        """Return a copy of the registered phase handlers."""
        return dict(self._phase_handlers)

    async def connect(self) -> None:
        """Initialize the job store and event bus."""
        if self._connected:
            return
        await self._job_store.connect()
        # InMemoryEventBus doesn't need explicit connect;
        # RabbitMQEventBus would be initialized here.
        self._connected = True
        logger.info("AtlasRuntime connected (db=%s)", self._db_path)

    async def close(self) -> None:
        """Clean up connections."""
        await self._job_store.close()
        await self._event_bus.close()
        self._connected = False
        logger.info("AtlasRuntime closed")

    async def __aenter__(self) -> "AtlasRuntime":
        await self.connect()
        return self

    async def __aexit__(self, *exc) -> None:
        await self.close()

    def get_phase_handler(self, phase: PipelinePhase) -> PhaseHandler | None:
        """Retrieve a registered phase handler."""
        return self._phase_handlers.get(phase)

    def register_phase_handler(
        self, phase: PipelinePhase, handler: PhaseHandler
    ) -> None:
        """Override or add a phase handler."""
        self._phase_handlers[phase] = handler
        if self._orchestrator is not None:
            # Update orchestrator's handlers too
            import asyncio

            async def _update():
                await self._orchestrator.register_phase_handler(phase, handler)

            try:
                asyncio.get_running_loop().create_task(_update())
            except RuntimeError:
                # No running loop; sync update
                self._orchestrator._phase_handlers[phase] = handler


def default_runtime(db_path: str = "atlas_jobs.db") -> AtlasRuntime:
    """Create a runtime with default services and all handlers wired.

    This is the function the CLI should use instead of manually
    constructing an orchestrator without handlers.
    """
    return AtlasRuntime(db_path=db_path)
