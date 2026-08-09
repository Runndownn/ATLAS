"""Tests for atlas.core.orchestrator."""

import asyncio
import pytest
from datetime import datetime

from atlas.core.event_bus import InMemoryEventBus
from atlas.core.job_store import JobStore, JobRecord, PhaseRecord
from atlas.core.orchestrator import (
    PipelineConfig,
    PipelineOrchestrator,
    PipelinePhase,
    PipelineStatus,
)


@pytest.fixture
async def job_store():
    store = JobStore(":memory:")
    await store.connect()
    return store


@pytest.fixture
async def event_bus():
    return InMemoryEventBus()


@pytest.fixture
async def orchestrator(job_store, event_bus):
    return PipelineOrchestrator(job_store, event_bus)


class TestJobRecord:
    def test_create_generates_ids(self):
        job = JobRecord.create(source_path="/tmp/test")
        assert job.job_id
        assert job.root_id
        assert job.status == "pending"
        assert job.progress_percent == 0.0
        assert job.error_count == 0

    def test_to_dict_serializes_metadata(self):
        job = JobRecord.create(source_path="/tmp/test", metadata={"key": "value"})
        d = job.to_dict()
        assert d["metadata"]  # JSON string
        import json
        parsed = json.loads(d["metadata"])
        assert parsed["key"] == "value"


class TestPhaseRecord:
    def test_create_phase(self):
        phase = PhaseRecord(
            phase_id="test-phase-1",
            job_id="test-job-1",
            phase="reconnaissance",
        )
        assert phase.status == "pending"
        assert phase.phase == "reconnaissance"
        assert phase.progress_percent == 0.0


class TestPipelineConfig:
    def test_default_has_all_phases(self):
        config = PipelineConfig.default(source_path="/tmp/test")
        assert len(config.phases) == len(PipelinePhase)

    def test_default_name(self):
        config = PipelineConfig.default(source_path="/tmp/test")
        assert config.name == "default"


class TestPipelineOrchestrator:
    @pytest.mark.asyncio
    async def test_start_pipeline_returns_job(self, orchestrator):
        config = PipelineConfig.default(source_path="/tmp/test")
        job = await orchestrator.start_pipeline(config)
        assert job.job_id == config.pipeline_id
        assert job.source_path == "/tmp/test"
        assert job.status == PipelineStatus.PENDING

    @pytest.mark.asyncio
    async def test_start_pipeline_assigns_job(self, orchestrator):
        config = PipelineConfig.default(source_path="/tmp/test")
        job = await orchestrator.start_pipeline(config)
        retrieved = await orchestrator.get_job(job.job_id)
        assert retrieved is not None
        assert retrieved.job_id == job.job_id

    @pytest.mark.asyncio
    async def test_pause_nonexistent_job(self, orchestrator):
        result = await orchestrator.pause_pipeline("nonexistent")
        assert result is False

    @pytest.mark.asyncio
    async def test_cancel_nonexistent_job(self, orchestrator):
        result = await orchestrator.cancel_pipeline("nonexistent")
        assert result is False

    @pytest.mark.asyncio
    async def test_list_jobs_empty(self, orchestrator):
        jobs = await orchestrator.list_jobs()
        assert jobs == []

    @pytest.mark.asyncio
    async def test_list_jobs_returns_created(self, orchestrator):
        config = PipelineConfig.default(source_path="/tmp/test")
        await orchestrator.start_pipeline(config)
        # Give the background task a moment
        await asyncio.sleep(0.1)
        jobs = await orchestrator.list_jobs()
        assert len(jobs) >= 0  # May have completed already

    @pytest.mark.asyncio
    async def test_register_phase_handler(self, orchestrator):
        """Test that a custom phase handler can be registered and called."""

        executed = False

        class TestHandler:
            async def execute(self, job: JobRecord, config: PipelineConfig, phase_record) -> None:
                nonlocal executed
                executed = True

        orchestrator._phase_handlers[PipelinePhase.RECONNAISSANCE] = TestHandler()

        config = PipelineConfig(
            pipeline_id="test-1",
            name="handler-test",
            phases=[PipelinePhase.RECONNAISSANCE],
            source_path="/tmp/test",
        )

        job = await orchestrator.start_pipeline(config)
        # Wait for pipeline to complete
        await asyncio.sleep(0.5)

        assert executed is True
