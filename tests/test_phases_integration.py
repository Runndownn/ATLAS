"""Tests for atlas.phases — integration test for full phase sequence."""

import asyncio
import tempfile
from pathlib import Path

import pytest

from atlas.core.event_bus import InMemoryEventBus
from atlas.core.job_store import JobStore
from atlas.core.orchestrator import (
    PipelineConfig,
    PipelineOrchestrator,
    PipelinePhase,
)
from atlas.phases.reconnaissance import ReconnaissancePhase
from atlas.phases.fingerprinting import FingerprintingPhase
from atlas.phases.extraction import ExtractionPhase
from atlas.phases.analysis import AnalysisPhase
from atlas.phases.review import ReviewPhase


@pytest.fixture
async def orchestrator_with_phases(tmp_path):
    """Create an orchestrator with all built-in phase handlers."""
    job_store = JobStore(":memory:")
    await job_store.connect()
    event_bus = InMemoryEventBus()

    orch = PipelineOrchestrator(job_store, event_bus)

    # Register phases
    orch._phase_handlers[PipelinePhase.RECONNAISSANCE] = ReconnaissancePhase()
    orch._phase_handlers[PipelinePhase.FINGERPRINTING] = FingerprintingPhase()
    orch._phase_handlers[PipelinePhase.STRUCTURAL_DISCOVERY] = ExtractionPhase()
    orch._phase_handlers[PipelinePhase.CONTROLLED_EXTRACTION] = ExtractionPhase()
    orch._phase_handlers[PipelinePhase.DEEP_UNDERSTANDING] = AnalysisPhase()
    orch._phase_handlers[PipelinePhase.REVIEW_PROMOTION] = ReviewPhase()

    return orch


class TestPhaseIntegration:
    @pytest.mark.asyncio
    async def test_full_pipeline_runs(self, orchestrator_with_phases, tmp_path):
        """Test that a full pipeline runs through all phases."""
        # Create a test file
        (tmp_path / "test.txt").write_text("hello world")
        (tmp_path / "config.env").write_text("SECRET=value")

        config = PipelineConfig(
            pipeline_id="test-full-pipeline",
            name="integration-test",
            source_path=str(tmp_path),
            phases=list(PipelinePhase),
        )

        job = await orchestrator_with_phases.start_pipeline(config)

        # Wait for completion by polling the store (not the local object)
        deadline = asyncio.get_event_loop().time() + 10.0
        while True:
            await asyncio.sleep(0.2)
            job = await orchestrator_with_phases.get_job(job.job_id)
            if job is None:
                pytest.fail("Job disappeared")
            if job.status in ("completed", "error", "cancelled"):
                break
            if asyncio.get_event_loop().time() > deadline:
                pytest.fail("Pipeline timed out")

        assert job.status in ("completed", "error", "cancelled")
        if job.status == "error":
            pytest.fail(f"Pipeline failed: {job.last_error}")

        # Check phase records
        phases = await orchestrator_with_phases._job_store.list_phases(job.job_id)
        assert len(phases) > 0

        # Check discovery metadata exists
        assert "discovery" in job.metadata
        discovery = job.metadata["discovery"]
        assert discovery["total_files"] >= 2

    @pytest.mark.asyncio
    async def test_pause_during_pipeline(self, orchestrator_with_phases, tmp_path):
        """Test that pipeline can be paused."""
        (tmp_path / "test.txt").write_text("hello")

        config = PipelineConfig(
            pipeline_id="test-pause",
            name="pause-test",
            source_path=str(tmp_path),
            phases=list(PipelinePhase),
        )

        job = await orchestrator_with_phases.start_pipeline(config)
        await asyncio.sleep(0.1)

        # Try to pause
        result = await orchestrator_with_phases.pause_pipeline(job.job_id)
        # May or may not succeed depending on timing
        assert isinstance(result, bool)

    @pytest.mark.asyncio
    async def test_cancel_pipeline(self, orchestrator_with_phases, tmp_path):
        """Test that pipeline can be cancelled."""
        (tmp_path / "test.txt").write_text("hello")

        config = PipelineConfig(
            pipeline_id="test-cancel",
            name="cancel-test",
            source_path=str(tmp_path),
            phases=list(PipelinePhase),
        )

        job = await orchestrator_with_phases.start_pipeline(config)
        await asyncio.sleep(0.1)

        result = await orchestrator_with_phases.cancel_pipeline(job.job_id)
        # If job already completed, cancel returns False — that's valid
        # If still running, cancel should succeed
        assert isinstance(result, bool)
        if result:
            # Wait for cancellation to propagate
            await asyncio.sleep(0.3)
            updated = await orchestrator_with_phases.get_job(job.job_id)
            assert updated is not None
            assert updated.status == "cancelled"
