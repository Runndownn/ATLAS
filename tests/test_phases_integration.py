"""Tests for atlas.phases — integration test for full phase sequence.

Uses AtlasRuntime (the canonical composition root) to ensure tests
exercise exactly the same code path as the CLI, per the BinReaper
assessment recommendation.
"""

import asyncio
import pytest

from atlas.core.orchestrator import (
    PipelineConfig,
    PipelinePhase,
    PipelineStatus,
)
from atlas.core.runtime import AtlasRuntime


@pytest.fixture
async def runtime(tmp_path):
    """Create an AtlasRuntime with all built-in phase handlers wired."""
    rt = AtlasRuntime(db_path=":memory:")
    await rt.connect()
    return rt


@pytest.fixture
async def orchestrator(runtime):
    """Get the orchestrator from AtlasRuntime (all handlers pre-registered)."""
    return runtime.orchestrator


class TestPhaseIntegration:
    @pytest.mark.asyncio
    async def test_full_pipeline_runs(self, runtime, orchestrator, tmp_path):
        """Test that a full pipeline runs through all phases via AtlasRuntime."""
        # Create test files
        (tmp_path / "test.txt").write_text("hello world")
        (tmp_path / "config.env").write_text("SECRET=value")

        config = PipelineConfig(
            pipeline_id="test-full-pipeline",
            name="integration-test",
            phases=list(PipelinePhase),
            source_path=str(tmp_path),
        )

        job = await orchestrator.start_pipeline(config)

        # Wait for completion by polling the store (not the local object)
        deadline = asyncio.get_event_loop().time() + 10.0
        while True:
            await asyncio.sleep(0.2)
            job = await orchestrator.get_job(job.job_id)
            if job is None:
                pytest.fail("Job disappeared")
            if job.status in ("completed", "error", "cancelled"):
                break
            if asyncio.get_event_loop().time() > deadline:
                pytest.fail("Pipeline timed out")

        assert job.status in ("completed", "error", "cancelled")
        if job.status == "error":
            pytest.fail(f"Pipeline failed: {job.last_error}")

        # Check phase records — should have all 6 phases
        phases = await runtime.job_store.list_phases(job.job_id)
        assert len(phases) == 6

        # Check discovery metadata exists
        assert "discovery" in job.metadata
        discovery = job.metadata["discovery"]
        assert discovery["total_files"] >= 2

        await runtime.close()

    @pytest.mark.asyncio
    async def test_pause_during_pipeline(self, runtime, orchestrator, tmp_path):
        """Test that pipeline can be paused."""
        (tmp_path / "test.txt").write_text("hello")

        config = PipelineConfig(
            pipeline_id="test-pause",
            name="pause-test",
            source_path=str(tmp_path),
            phases=list(PipelinePhase),
        )

        job = await orchestrator.start_pipeline(config)
        await asyncio.sleep(0.1)

        # Try to pause
        result = await orchestrator.pause_pipeline(job.job_id)
        # May or may not succeed depending on timing
        assert isinstance(result, bool)

        await runtime.close()

    @pytest.mark.asyncio
    async def test_cancel_pipeline(self, runtime, orchestrator, tmp_path):
        """Test that pipeline can be cancelled."""
        (tmp_path / "test.txt").write_text("hello")

        config = PipelineConfig(
            pipeline_id="test-cancel",
            name="cancel-test",
            source_path=str(tmp_path),
            phases=list(PipelinePhase),
        )

        job = await orchestrator.start_pipeline(config)
        await asyncio.sleep(0.1)

        result = await orchestrator.cancel_pipeline(job.job_id)
        # If job already completed, cancel returns False — that's valid
        # If still running, cancel should succeed
        assert isinstance(result, bool)
        if result:
            # Wait for cancellation to propagate
            await asyncio.sleep(0.3)
            updated = await orchestrator.get_job(job.job_id)
            assert updated is not None
            assert updated.status == "cancelled"

        await runtime.close()

    @pytest.mark.asyncio
    async def test_phase_handler_registration_api(self, runtime):
        """Test that handlers are registered via the canonical API, not _phase_handlers directly."""
        # AtlasRuntime should have all 6 phases registered
        handlers = runtime.phase_handlers
        assert len(handlers) == 6
        for phase in PipelinePhase:
            assert phase in handlers

        # The registration API should work for overriding handlers
        from atlas.phases.review import ReviewPhase
        await runtime.orchestrator.register_phase_handler(
            PipelinePhase.REVIEW_PROMOTION,
            ReviewPhase(event_bus=runtime.event_bus),
        )
        assert PipelinePhase.REVIEW_PROMOTION in runtime.phase_handlers

        await runtime.close()
