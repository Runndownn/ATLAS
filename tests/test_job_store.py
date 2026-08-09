"""Tests for atlas.core.job_store."""

import pytest
from datetime import datetime

from atlas.core.job_store import JobStore, JobRecord, PhaseRecord


@pytest.fixture
async def job_store():
    store = JobStore(":memory:")
    await store.connect()
    return store


class TestJobStore:
    @pytest.mark.asyncio
    async def test_create_and_retrieve_job(self, job_store):
        job = JobRecord.create(source_path="/tmp/test")
        await job_store.create_job(job)

        retrieved = await job_store.get_job(job.job_id)
        assert retrieved is not None
        assert retrieved.job_id == job.job_id
        assert retrieved.source_path == "/tmp/test"

    @pytest.mark.asyncio
    async def test_update_job(self, job_store):
        job = JobRecord.create(source_path="/tmp/test")
        await job_store.create_job(job)

        job.status = "running"
        job.progress_percent = 25.0
        await job_store.update_job(job)

        retrieved = await job_store.get_job(job.job_id)
        assert retrieved.status == "running"
        assert retrieved.progress_percent == 25.0

    @pytest.mark.asyncio
    async def test_list_jobs_empty(self, job_store):
        jobs = await job_store.list_jobs()
        assert jobs == []

    @pytest.mark.asyncio
    async def test_list_jobs_multiple(self, job_store):
        job1 = JobRecord.create(source_path="/tmp/test1")
        job2 = JobRecord.create(source_path="/tmp/test2")
        await job_store.create_job(job1)
        await job_store.create_job(job2)

        jobs = await job_store.list_jobs()
        assert len(jobs) == 2

    @pytest.mark.asyncio
    async def test_add_phase_record(self, job_store):
        job = JobRecord.create(source_path="/tmp/test")
        await job_store.create_job(job)

        phase = PhaseRecord(
            phase_id="phase-1",
            job_id=job.job_id,
            phase="reconnaissance",
        )
        await job_store.add_phase_record(phase)

        phases = await job_store.list_phases(job.job_id)
        assert len(phases) == 1
        assert phases[0].phase == "reconnaissance"

    @pytest.mark.asyncio
    async def test_update_phase_record(self, job_store):
        job = JobRecord.create(source_path="/tmp/test")
        await job_store.create_job(job)

        phase = PhaseRecord(
            phase_id="phase-1",
            job_id=job.job_id,
            phase="reconnaissance",
        )
        await job_store.add_phase_record(phase)

        phase.status = "completed"
        phase.progress_percent = 100.0
        await job_store.update_phase_record(phase)

        phases = await job_store.list_phases(job.job_id)
        assert phases[0].status == "completed"
        assert phases[0].progress_percent == 100.0

    @pytest.mark.asyncio
    async def test_get_nonexistent_job(self, job_store):
        result = await job_store.get_job("does-not-exist")
        assert result is None

    @pytest.mark.asyncio
    async def test_job_metadata_round_trips(self, job_store):
        job = JobRecord.create(
            source_path="/tmp/test",
            metadata={"pipeline_name": "test", "abort_on_error": False},
        )
        await job_store.create_job(job)

        retrieved = await job_store.get_job(job.job_id)
        assert retrieved.metadata["pipeline_name"] == "test"
        assert retrieved.metadata["abort_on_error"] is False
