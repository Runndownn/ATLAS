"""ATLAS CLI — Adaptive Task Lifecycle Engine for Staged Artifact Processing.

Usage:
    atlas run <pipeline.yaml>          Run a pipeline
    atlas jobs list                    List all jobs
    atlas job <id> status              Show job status
    atlas job <id> pause               Pause a running job
    atlas job <id> resume              Resume a paused job
    atlas job <id> cancel              Cancel a job
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from typing import Any

from atlas.core.event_bus import EventBus, InMemoryEventBus, RabbitMQEventBus
from atlas.core.job_store import JobStore
from atlas.core.orchestrator import (
    PipelineConfig,
    PipelineOrchestrator,
    PipelinePhase,
    PipelineStatus,
)


def _load_pipeline(path: str) -> dict[str, Any]:
    """Load a pipeline YAML/JSON definition."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Pipeline file not found: {path}")

    if file_path.suffix in {".yaml", ".yml"}:
        import yaml  # type: ignore
        with open(file_path) as f:
            return yaml.safe_load(f)
    elif file_path.suffix == ".json":
        with open(file_path) as f:
            return json.load(f)
    else:
        raise ValueError(f"Unsupported pipeline file format: {file_path.suffix}")


def _build_pipeline_config(pipeline_def: dict[str, Any]) -> PipelineConfig:
    """Build a PipelineConfig from a pipeline definition."""
    source_path = pipeline_def.get("source_path", "")
    phases = pipeline_def.get("phases", [p.value for p in PipelinePhase])

    return PipelineConfig(
        pipeline_id=pipeline_def.get("pipeline_id", str(__import__("uuid").uuid4())),
        name=pipeline_def.get("name", "default"),
        phases=[PipelinePhase(p) for p in phases],
        source_path=source_path,
        metadata={
            "pipeline_name": pipeline_def.get("name", "default"),
            "abort_on_error": pipeline_def.get("abort_on_error", True),
        },
    )


async def _run_pipeline(args: list[str]) -> int:
    """Execute the 'atlas run' command."""
    if not args:
        print("Usage: atlas run <pipeline.yaml>")
        return 1

    pipeline_path = args[0]
    db_path = args[1] if len(args) > 1 else "atlas_jobs.db"

    pipeline_def = _load_pipeline(pipeline_path)
    config = _build_pipeline_config(pipeline_def)

    job_store = JobStore(db_path)
    await job_store.connect()
    event_bus: EventBus = InMemoryEventBus()
    orchestrator = PipelineOrchestrator(job_store, event_bus)

    job = await orchestrator.start_pipeline(config)
    print(f"Started pipeline '{config.name}' with job_id={job.job_id}")

    # Wait for completion (or poll)
    while True:
        job = await orchestrator.get_job(job.job_id)
        if job is None:
            print("Job not found")
            return 1
        if job.status in ("completed", "error", "cancelled"):
            print(f"Pipeline {job.status}: job_id={job.job_id}")
            if job.status == "error" and job.last_error:
                print(f"Error: {job.last_error}")
            return 0 if job.status == "completed" else 1
        await asyncio.sleep(0.5)

    return 0


async def _list_jobs(args: list[str]) -> int:
    """Execute the 'atlas jobs list' command."""
    db_path = args[0] if args else "atlas_jobs.db"
    job_store = JobStore(db_path)
    await job_store.connect()
    jobs = await job_store.list_jobs()

    if not jobs:
        print("No jobs found.")
        return 0

    print(f"{'Job ID':<36} {'Status':<12} {'Phase':<24} {'Progress':>8}  Source")
    print("-" * 100)
    for job in jobs:
        progress = f"{job.progress_percent:.0f}%"
        print(f"{job.job_id:<36} {job.status:<12} {job.phase:<24} {progress:>8}  {job.source_path}")

    return 0


async def _job_action(action: str, args: list[str]) -> int:
    """Execute a job action (status/pause/resume/cancel)."""
    if not args:
        print(f"Usage: atlas job <id> {action}")
        return 1

    job_id = args[0]
    db_path = args[1] if len(args) > 1 else "atlas_jobs.db"

    job_store = JobStore(db_path)
    await job_store.connect()
    event_bus: EventBus = InMemoryEventBus()
    orchestrator = PipelineOrchestrator(job_store, event_bus)

    if action == "status":
        job = await orchestrator.get_job(job_id)
        if job is None:
            print(f"Job {job_id} not found")
            return 1
        print(f"Job ID:    {job.job_id}")
        print(f"Status:    {job.status}")
        print(f"Phase:     {job.phase}")
        print(f"Progress:  {job.progress_percent:.1f}%")
        print(f"Source:    {job.source_path}")
        print(f"Started:   {job.started_at}")
        print(f"Completed: {job.completed_at}")
        if job.last_error:
            print(f"Error:     {job.last_error}")

        phases = await job_store.list_phases(job_id)
        if phases:
            print(f"\nPhases:")
            for p in phases:
                print(f"  {p.phase:<24} {p.status:<12} {p.progress_percent:.0f}%")
        return 0

    if action == "pause":
        success = await orchestrator.pause_pipeline(job_id)
        if success:
            print(f"Paused job {job_id}")
            return 0
        print(f"Could not pause job {job_id} (not running)")
        return 1

    if action == "resume":
        success = await orchestrator.resume_pipeline(job_id)
        if success:
            print(f"Resumed job {job_id}")
            return 0
        print(f"Could not resume job {job_id} (not paused)")
        return 1

    if action == "cancel":
        success = await orchestrator.cancel_pipeline(job_id)
        if success:
            print(f"Cancelled job {job_id}")
            return 0
        print(f"Could not cancel job {job_id}")
        return 1

    return 1


async def _amain() -> int:
    """Main async entry point."""
    args = sys.argv[1:]

    if not args:
        print("ATLAS — Adaptive Task Lifecycle Engine")
        print("Usage: atlas <command> [args...]")
        print("")
        print("Commands:")
        print("  run <pipeline.yaml> [db_path]    Run a pipeline")
        print("  jobs list [db_path]              List all jobs")
        print("  job <id> status [db_path]        Show job status")
        print("  job <id> pause [db_path]         Pause a running job")
        print("  job <id> resume [db_path]        Resume a paused job")
        print("  job <id> cancel [db_path]        Cancel a job")
        return 0

    command = args[0]
    rest = args[1:]

    if command == "run":
        return await _run_pipeline(rest)
    elif command == "jobs":
        if len(rest) >= 1 and rest[0] == "list":
            return await _list_jobs(rest[1:])
        print("Usage: atlas jobs list [db_path]")
        return 1
    elif command == "job":
        if len(rest) < 2:
            print("Usage: atlas job <id> <status|pause|resume|cancel> [db_path]")
            return 1
        job_id, action = rest[0], rest[1]
        return await _job_action(action, rest[2:] if len(rest) > 2 else [job_id])
    else:
        print(f"Unknown command: {command}")
        return 1


def app() -> None:
    """CLI entry point (sync wrapper)."""
    exit_code = asyncio.run(_amain())
    sys.exit(exit_code)
