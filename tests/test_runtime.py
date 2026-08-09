"""Tests for AtlasRuntime composition root and fail-closed behavior."""

import asyncio
import json
import os
import tempfile

import pytest

from atlas.core.event_bus import InMemoryEventBus
from atlas.core.job_store import JobStore
from atlas.core.orchestrator import (
    PipelineConfig,
    PipelineOrchestrator,
    PipelinePhase,
    PipelineStatus,
)
from atlas.core.runtime import AtlasRuntime


class TestAtlasRuntime:
    """Test the canonical composition root."""

    @pytest.mark.asyncio
    async def test_runtime_wires_all_handlers(self):
        """AtlasRuntime must register all 6 phase handlers."""
        runtime = AtlasRuntime(db_path=":memory:")
        await runtime.connect()

        handlers = runtime.phase_handlers
        assert PipelinePhase.RECONNAISSANCE in handlers
        assert PipelinePhase.FINGERPRINTING in handlers
        assert PipelinePhase.STRUCTURAL_DISCOVERY in handlers
        assert PipelinePhase.CONTROLLED_EXTRACTION in handlers
        assert PipelinePhase.DEEP_UNDERSTANDING in handlers
        assert PipelinePhase.REVIEW_PROMOTION in handlers

        await runtime.close()

    @pytest.mark.asyncio
    async def test_runtime_executes_full_pipeline(self, tmp_path):
        """The runtime must execute all phases when used by the CLI."""
        (tmp_path / "test.txt").write_text("hello world")
        (tmp_path / "config.env").write_text("SECRET=value")

        runtime = AtlasRuntime(db_path=":memory:")
        await runtime.connect()
        orch = runtime.orchestrator

        config = PipelineConfig(
            pipeline_id="runtime-test",
            name="test",
            phases=list(PipelinePhase),
            source_path=str(tmp_path),
        )

        job = await orch.start_pipeline(config)

        # Poll for completion
        deadline = asyncio.get_event_loop().time() + 10.0
        while True:
            await asyncio.sleep(0.2)
            job = await orch.get_job(job.job_id)
            if job.status in ("completed", "error", "cancelled"):
                break
            if asyncio.get_event_loop().time() > deadline:
                pytest.fail("Pipeline timed out")

        assert job.status == PipelineStatus.COMPLETED.value

        phases = await runtime.job_store.list_phases(job.job_id)
        assert len(phases) == 6
        for p in phases:
            assert p.status == PipelineStatus.COMPLETED.value

        await runtime.close()

    @pytest.mark.asyncio
    async def test_runtime_events_persisted(self, tmp_path):
        """Events should be persisted in the SQLite events table."""
        (tmp_path / "test.txt").write_text("hello")

        runtime = AtlasRuntime(db_path=":memory:")
        await runtime.connect()

        config = PipelineConfig(
            pipeline_id="event-test",
            name="test",
            phases=list(PipelinePhase),
            source_path=str(tmp_path),
        )

        job = await runtime.orchestrator.start_pipeline(config)

        deadline = asyncio.get_event_loop().time() + 10.0
        while True:
            await asyncio.sleep(0.2)
            job = await runtime.orchestrator.get_job(job.job_id)
            if job.status in ("completed", "error", "cancelled"):
                break
            if asyncio.get_event_loop().time() > deadline:
                pytest.fail("Pipeline timed out")

        events = await runtime.job_store.list_events(job.job_id)
        assert len(events) > 0
        # Should have at least: pipeline.started, phase.started (x6), phase.completed (x6), pipeline.completed
        assert len(events) >= 10

        await runtime.close()


class TestFailClosed:
    """Test that missing handlers cause pipeline failure (not silent success)."""

    @pytest.mark.asyncio
    async def test_no_handlers_fails_pipeline(self, tmp_path):
        """A bare orchestrator without handlers must fail, not silently complete."""
        (tmp_path / "test.txt").write_text("hello")

        job_store = JobStore(":memory:")
        await job_store.connect()
        event_bus = InMemoryEventBus()
        orch = PipelineOrchestrator(job_store, event_bus)

        config = PipelineConfig(
            pipeline_id="failclosed-test",
            name="test",
            phases=list(PipelinePhase),
            source_path=str(tmp_path),
        )

        job = await orch.start_pipeline(config)

        deadline = asyncio.get_event_loop().time() + 10.0
        while True:
            await asyncio.sleep(0.2)
            job = await orch.get_job(job.job_id)
            if job.status in ("completed", "error", "cancelled"):
                break
            if asyncio.get_event_loop().time() > deadline:
                pytest.fail("Pipeline timed out")

        assert job.status == PipelineStatus.ERROR.value
        assert "No handler registered" in (job.last_error or "")

        await job_store.close()
        await event_bus.close()
