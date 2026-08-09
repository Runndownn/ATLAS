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
import uuid
from pathlib import Path
from typing import Any

from atlas.core.event_bus import EventBus
from atlas.core.job_store import JobStore
from atlas.core.orchestrator import (
    PipelineConfig,
    PipelinePhase,
    PipelineStatus,
)
from atlas.core.runtime import AtlasRuntime


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
    """Build a PipelineConfig from a pipeline definition.

    Handles:
    - pipeline_id: "auto" generates a UUID; otherwise uses literal value
    - phase_config: passed through to metadata per-phase settings
    - continue_on_phase_error: honored for per-phase error tolerance
    - metadata: all top-level keys preserved in job metadata
    """
    # Handle "auto" pipeline_id — generate UUID instead of using literal "auto"
    pipeline_id = pipeline_def.get("pipeline_id", "auto")
    if pipeline_id == "auto" or not pipeline_id:
        pipeline_id = str(uuid.uuid4())

    source_path = pipeline_def.get("source_path", "")
    phases_raw = pipeline_def.get("phases")
    if phases_raw:
        phases = [PipelinePhase(p) for p in phases_raw]
    else:
        phases = list(PipelinePhase)

    # Extract phase_config and error semantics
    phase_config = pipeline_def.get("phase_config", {})
    continue_on_error = pipeline_def.get("continue_on_phase_error", False)
    abort_on_error = pipeline_def.get("abort_on_error", True)

    # Build metadata — preserve all top-level keys from the YAML
    metadata = {
        "pipeline_name": pipeline_def.get("name", "default"),
        "phase_config": phase_config,
        "continue_on_phase_error": continue_on_error,
        "abort_on_error": abort_on_error,
    }

    # Merge any additional metadata from the YAML
    extra_meta = pipeline_def.get("metadata", {})
    metadata.update(extra_meta)

    return PipelineConfig(
        pipeline_id=pipeline_id,
        name=pipeline_def.get("name", "default"),
        phases=phases,
        source_path=source_path,
        metadata=metadata,
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

    # Use AtlasRuntime to ensure all phase handlers are wired
    runtime = AtlasRuntime(db_path=db_path)
    await runtime.connect()
    orchestrator = runtime.orchestrator

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
            await runtime.close()
            return 0 if job.status == "completed" else 1
        await asyncio.sleep(0.5)

    await runtime.close()
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
    """Execute a job action (status/pause/resume/cancel).

    For status queries, reads directly from the JobStore. For control
    actions (pause/resume/cancel), hydrates the job into an orchestrator
    instance and applies the state change.

    Note: control actions currently work within the same process. For
    cross-process control, a runtime daemon consuming a control table
    is recommended (see assessment note on process-local controls).
    """
    if not args:
        print(f"Usage: atlas job <id> {action}")
        return 1

    job_id = args[0]
    db_path = args[1] if len(args) > 1 else "atlas_jobs.db"

    # --- Status: read directly from store ---
    if action == "status":
        job_store = JobStore(db_path)
        await job_store.connect()
        job = await job_store.get_job(job_id)
        if job is None:
            print(f"Job {job_id} not found")
            await job_store.close()
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
        await job_store.close()
        return 0

    # --- Control actions: pause/resume/cancel ---
    # Use AtlasRuntime to ensure handlers are wired (needed for resume)
    runtime = AtlasRuntime(db_path=db_path)
    await runtime.connect()
    orchestrator = runtime.orchestrator
    job = await job_store if False else await runtime.job_store.get_job(job_id)

    if job is None:
        print(f"Job {job_id} not found")
        await runtime.close()
        return 1

    # Load job into orchestrator's in-memory dict for process-local control
    orchestrator._jobs[job.job_id] = job

    try:
        if action == "pause":
            success = await orchestrator.pause_pipeline(job_id)
            msg = f"Paused job {job_id}" if success else f"Could not pause job {job_id} (not running)"
        elif action == "resume":
            success = await orchestrator.resume_pipeline(job_id)
            msg = f"Resumed job {job_id}" if success else f"Could not resume job {job_id} (not paused)"
        elif action == "cancel":
            success = await orchestrator.cancel_pipeline(job_id)
            msg = f"Cancelled job {job_id}" if success else f"Could not cancel job {job_id}"
        else:
            msg = f"Unknown action: {action}"
            success = False
        print(msg)
        return 0 if success else 1
    finally:
        await runtime.close()


async def _amain() -> int:
    """Main async entry point."""
    args = sys.argv[1:]

    # Handle --help and -h
    if not args or args[0] in ("--help", "-h"):
        print("ATLAS — Adaptive Task Lifecycle Engine")
        print("")
        print("Usage: atlas <command> [args...]")
        print("")
        print("Commands:")
        print("  run <pipeline.yaml> [db_path]    Run a pipeline")
        print("  jobs list [db_path]              List all jobs")
        print("  job <id> status [db_path]        Show job status")
        print("  job <id> pause [db_path]         Pause a running job")
        print("  job <id> resume [db_path]        Resume a paused job")
        print("  job <id> cancel [db_path]        Cancel a job")
        print("")
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
