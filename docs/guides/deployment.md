# ATLAS Deployment and Operations Guide

This guide covers running ATLAS in production, operational procedures, and the safety model.

## Prerequisites

- Python 3.13+
- SQLite 3 (bundled with Python; no separate server required for single-process use)
- Optional: RabbitMQ (AMQP 0-9-1) for distributed event publishing
- Optional: `aio-pika` (`pip install atlas-pipeline[rabbitmq]`)

## Installation

### From PyPI

```bash
pip install atlas-pipeline
```

### With RabbitMQ support

```bash
pip install atlas-pipeline[rabbitmq]
```

### Local development (editable)

```bash
git clone https://github.com/Runndownn/ATLAS.git
cd ATLAS
pip install -e ".[dev]"
```

### Verifying the install

```bash
atlas run --help
atlas jobs list --help
```

## Deployment Models

### Single-Process (Default)

ATLAS runs as a single Python process using `InMemoryEventBus` and an on-disk or in-memory SQLite database. This is the default mode for CLI usage and small workloads.

```bash
atlas run examples/ctfd_pipeline.yaml my_jobs.db
```

Job state and events persist to `my_jobs.db`.

### With RabbitMQ Event Bus

Configure the event bus URL via environment variable or pass it programmatically:

```python
from atlas.core.event_bus import RabbitMQEventBus
from atlas.core.runtime import AtlasRuntime

rabbit_url = os.environ.get("ATLAS_RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
event_bus = RabbitMQEventBus(url=rabbit_url, exchange="atlas.events", fallback=True)
runtime = AtlasRuntime(db_path="jobs.db", event_bus=event_bus)
```

### Container / Process Manager

ATLAS does not ship a Dockerfile. For production, run under a process manager (systemd, supervisord, or container orchestrator). Key configuration:

| Setting | Env Var | Default | Notes |
|---------|---------|---------|-------|
| SQLite DB path | `ATLAS_DB_PATH` | `atlas_jobs.db` | Use a persistent volume for durability |
| RabbitMQ URL | `ATLAS_RABBITMQ_URL` | — | Required only when using `RabbitMQEventBus` |
| Exchange name | `ATLAS_RABBITMQ_EXCHANGE` | `atlas.events` | |

## Operational Procedures

### Running a Pipeline

```bash
atlas run <pipeline.yaml> [db_path]
```

- If `db_path` is omitted, defaults to `atlas_jobs.db` in the current directory.
- The pipeline runs in the foreground. The CLI polls job status every 0.5s and exits when the job reaches `completed`, `error`, or `cancelled`.
- Use `Ctrl+C` to interrupt the polling loop (the pipeline task continues in the background until the async task is cancelled or the process exits).

### Listing Jobs

```bash
atlas jobs list [db_path]
```

Prints a table: `Job ID`, `Status`, `Phase`, `Progress`, `Source`.

### Job Control

```bash
atlas job <job_id> status [db_path]   # show detailed job + phase info
atlas job <job_id> pause  [db_path]   # pause a running job
atlas job <job_id> resume [db_path]   # resume a paused job
atlas job <job_id> cancel [db_path]   # cancel a running or paused job
```

**Important:** Pause, resume, and cancel are **process-local**. They only affect jobs running in the same process that started them. For cross-process control, a long-running daemon that consumes from a control table is recommended (see assessment note in `atlas/core/orchestrator.py`).

### Checking Job Status via SQL

```bash
sqlite3 jobs.db "SELECT job_id, status, phase, progress_percent, started_at, completed_at FROM atlas_jobs WHERE job_id = '<id>';"
```

### Event Log

```bash
sqlite3 jobs.db "SELECT routing_key, created_at, payload FROM atlas_events WHERE job_id = '<id>' ORDER BY created_at;"
```

## Safety Model

ATLAS enforces safety on filesystem and archive artifacts. These checks live in `atlas/safety/`:

| Module | Protection |
|--------|-----------|
| `archive_safety.py` | Archive bomb detection (max uncompressed size, max member count, decompression ratio) |
| `path_safety.py` | Path traversal detection (`../`, absolute paths, symlink resolution) |
| `filesystem_discovery.py` | Filesystem discovery with depth and size limits |

### Safety Limits Configuration

```python
from atlas.core.runtime import AtlasRuntime

runtime = AtlasRuntime(
    max_uncompressed_bytes=1_073_741_824,  # 1 GB
    max_members=10_000,
)
```

Defaults (if unset): enforced via each phase handler's constructor defaults in `atlas/safety/archive_safety.py`. Check the source for current defaults.

## Backup

The SQLite database at `db_path` contains all job state, phase records, and event logs. Back it up using standard SQLite tools:

```bash
# Live backup (snapshot)
sqlite3 jobs.db ".backup backup-$(date +%Y%m%d).db"

# Or copy the file when no pipeline is running
cp jobs.db jobs.db.bak
```

## Monitoring

- **Job status**: `atlas jobs list` or query `atlas_jobs` table.
- **Error detection**: `atlas job <id> status` shows `last_error`; query `SELECT job_id, last_error FROM atlas_jobs WHERE status = 'error'`.
- **Event stream**: Query `atlas_events` table or consume from RabbitMQ exchange.
- **Progress**: `progress_percent` on both `atlas_jobs` and `atlas_phases` tables.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `FileNotFoundError` on `atlas run` | Pipeline YAML path is wrong or file does not exist | Verify path; use `atlas run --help` for usage |
| `No handler registered for phase` | Running without `AtlasRuntime` or handler not registered | Use `AtlasRuntime` or call `register_phase_handler` |
| `aio-pika not installed` | RabbitMQ support not installed | `pip install atlas-pipeline[rabbitmq]` |
| `RabbitMQ connection failed` | Broker unreachable or wrong URL | Verify `ATLAS_RABBITMQ_URL`; `fallback=True` uses in-memory |
| `Job not found` after restart | In-memory job lost (process-local controls) | Use `:memory:` only for testing; use a file DB for persistence |

## See Also

- `atlas/core/runtime.py` — `AtlasRuntime` composition root
- `atlas/core/orchestrator.py` — orchestration logic, pause/resume/cancel semantics
- `atlas/core/job_store.py` — SQLite schema and persistence
- `atlas/core/event_bus.py` — event bus backends
- `atlas/safety/` — safety services
- `atlas/docs/guides/extending-phases.md` — custom phase development
- `atlas/docs/guides/event-bus-integration.md` — consuming events
