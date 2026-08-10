"""SQLite-backed job store for ATLAS pipeline state.

Extracted from the Yggdrasil orchestrator + event bus patterns and
generalized for any pipeline with job/phase lifecycle tracking.
"""

from __future__ import annotations

import asyncio
import json
import logging
import sqlite3
from dataclasses import dataclass, asdict, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

logger = logging.getLogger("atlas.job_store")

_DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS atlas_jobs (
    job_id          TEXT PRIMARY KEY,
    root_id         TEXT NOT NULL,
    source_path     TEXT,
    phase           TEXT,
    status          TEXT NOT NULL,
    progress_percent REAL DEFAULT 0.0,
    error_count     INTEGER DEFAULT 0,
    last_error      TEXT,
    started_at      TIMESTAMP,
    paused_at       TIMESTAMP,
    completed_at    TIMESTAMP,
    cancelled_at    TIMESTAMP,
    resumed_at      TIMESTAMP,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata        TEXT
);

CREATE TABLE IF NOT EXISTS atlas_phases (
    phase_id          TEXT PRIMARY KEY,
    job_id            TEXT NOT NULL REFERENCES atlas_jobs(job_id) ON DELETE CASCADE,
    phase             TEXT NOT NULL,
    status            TEXT NOT NULL,
    progress_percent  REAL DEFAULT 0.0,
    started_at        TIMESTAMP,
    completed_at      TIMESTAMP,
    error             TEXT,
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS atlas_events (
    event_id       TEXT PRIMARY KEY,
    job_id         TEXT,
    routing_key    TEXT NOT NULL,
    payload        TEXT NOT NULL,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_atlas_phases_job ON atlas_phases(job_id);
CREATE INDEX IF NOT EXISTS idx_atlas_events_job ON atlas_events(job_id);
CREATE INDEX IF NOT EXISTS idx_atlas_events_created ON atlas_events(created_at);
"""


@dataclass
class JobRecord:
    """A pipeline job record."""

    job_id: str
    root_id: str
    source_path: str
    phase: str = "reconnaissance"
    status: str = "pending"
    progress_percent: float = 0.0
    error_count: int = 0
    last_error: str | None = None
    started_at: datetime | None = None
    paused_at: datetime | None = None
    completed_at: datetime | None = None
    cancelled_at: datetime | None = None
    resumed_at: datetime | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        source_path: str,
        metadata: dict[str, Any] | None = None,
    ) -> "JobRecord":
        """Create a new job record with generated IDs."""
        now = datetime.now(UTC)
        return cls(
            job_id=str(uuid4()),
            root_id=str(uuid4()),
            source_path=source_path,
            metadata=metadata or {},
            created_at=now,
            updated_at=now,
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize to dictionary for storage."""
        d = asdict(self)
        # Convert datetimes to ISO strings for storage
        for key in ("started_at", "paused_at", "completed_at", "cancelled_at", "resumed_at", "created_at", "updated_at"):
            if d[key] is not None:
                d[key] = d[key].isoformat()
        # Serialize metadata as JSON, handling non-serializable values
        def _json_safe(obj: Any) -> Any:
            """Convert non-JSON-serializable objects to safe equivalents."""
            if isinstance(obj, datetime):
                return obj.isoformat()
            if isinstance(obj, Path):
                return str(obj)
            if isinstance(obj, dict):
                return {k: _json_safe(v) for k, v in obj.items()}
            if isinstance(obj, (list, tuple)):
                return [_json_safe(v) for v in obj]
            # Handle dataclass instances (e.g., EvidenceRecord, PromotionRecord)
            if hasattr(obj, "__dataclass_fields__"):
                return _json_safe(asdict(obj))
            # Handle enums
            if hasattr(obj, "value") and not isinstance(obj, (str, int, float, bool, dict, list, tuple)):
                return str(obj)
            return obj

        d["metadata"] = json.dumps(_json_safe(d["metadata"]))
        return d


@dataclass
class PhaseRecord:
    """A phase execution record within a job."""

    phase_id: str
    job_id: str
    phase: str
    status: str = "pending"
    progress_percent: float = 0.0
    started_at: datetime | None = None
    completed_at: datetime | None = None
    error: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def to_dict(self) -> dict[str, Any]:
        """Serialize to dictionary."""
        d = asdict(self)
        for key in ("started_at", "completed_at", "created_at", "updated_at"):
            if d[key] is not None:
                d[key] = d[key].isoformat()
        # Ensure status is a plain string (may be PipelineStatus enum)
        if d.get("status") is not None:
            d["status"] = str(d["status"])
        return d


class JobStore:
    """SQLite-backed persistent job store."""

    def __init__(self, db_path: str = ":memory:"):
        self._db_path = db_path
        self._lock = asyncio.Lock()
        self._conn: sqlite3.Connection | None = None
        self._initialized = False

    def _get_conn(self) -> sqlite3.Connection:
        """Get or create the shared SQLite connection."""
        if self._conn is not None:
            return self._conn
        conn = sqlite3.connect(self._db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.executescript(
            _DB_SCHEMA.replace(
                "updated_at TRIGGER_DEFAULT",
                "DEFAULT CURRENT_TIMESTAMP",
            )
        )
        self._conn = conn
        return conn

    async def connect(self) -> None:
        """Initialize the database schema."""
        if self._initialized:
            return
        self._get_conn()  # Creates + initializes the shared connection
        self._initialized = True
        logger.info("JobStore initialized with db_path=%s", self._db_path)

    async def close(self) -> None:
        """Close the database connection."""
        if self._conn is not None:
            self._conn.close()
            self._conn = None
            self._initialized = False

    async def create_job(self, job: JobRecord) -> None:
        """Insert a new job record."""
        async with self._lock:
            conn = self._get_conn()
            conn.execute(
                """
                INSERT INTO atlas_jobs
                    (job_id, root_id, source_path,
                     phase, status, progress_percent, metadata, created_at, updated_at)
                VALUES (:job_id, :root_id, :source_path,
                        :phase, :status, :progress_percent, :metadata, :created_at, :updated_at)
                """,
                job.to_dict(),
            )
            conn.commit()

    async def update_job(self, job: JobRecord) -> None:
        """Update an existing job record."""
        async with self._lock:
            conn = self._get_conn()
            conn.execute(
                """
                UPDATE atlas_jobs SET
                    root_id = :root_id,
                    source_path = :source_path,
                    phase = :phase,
                    status = :status,
                    progress_percent = :progress_percent,
                    error_count = :error_count,
                    last_error = :last_error,
                    started_at = :started_at,
                    paused_at = :paused_at,
                    completed_at = :completed_at,
                    cancelled_at = :cancelled_at,
                    resumed_at = :resumed_at,
                    metadata = :metadata,
                    updated_at = :updated_at
                WHERE job_id = :job_id
                """,
                job.to_dict(),
            )
            conn.commit()

    async def add_phase_record(self, phase: PhaseRecord) -> None:
        """Insert a phase execution record."""
        async with self._lock:
            conn = self._get_conn()
            conn.execute(
                """
                INSERT INTO atlas_phases
                    (phase_id, job_id, phase, status, progress_percent,
                     started_at, completed_at, error, created_at, updated_at)
                VALUES (:phase_id, :job_id, :phase, :status, :progress_percent,
                        :started_at, :completed_at, :error, :created_at, :updated_at)
                """,
                phase.to_dict(),
            )
            conn.commit()

    async def update_phase_record(self, phase: PhaseRecord) -> None:
        """Update an existing phase record."""
        async with self._lock:
            conn = self._get_conn()
            conn.execute(
                """
                UPDATE atlas_phases SET
                    status = :status,
                    progress_percent = :progress_percent,
                    completed_at = :completed_at,
                    error = :error,
                    updated_at = :updated_at
                WHERE phase_id = :phase_id
                """,
                phase.to_dict(),
            )
            conn.commit()

    async def get_job(self, job_id: str) -> JobRecord | None:
        """Fetch a job by ID."""
        conn = self._get_conn()
        row = conn.execute(
            "SELECT * FROM atlas_jobs WHERE job_id = ?",
            (job_id,),
        ).fetchone()
        if row is None:
            return None
        return self._row_to_job(row)

    async def list_jobs(self) -> list[JobRecord]:
        """List all jobs."""
        conn = self._get_conn()
        rows = conn.execute(
            "SELECT * FROM atlas_jobs ORDER BY created_at DESC"
        ).fetchall()
        return [self._row_to_job(row) for row in rows]

    async def list_phases(self, job_id: str) -> list[PhaseRecord]:
        """List all phase records for a job."""
        conn = self._get_conn()
        rows = conn.execute(
            "SELECT * FROM atlas_phases WHERE job_id = ? ORDER BY created_at",
            (job_id,),
        ).fetchall()
        return [self._row_to_phase(row) for row in rows]

    async def store_event(
        self,
        job_id: str,
        routing_key: str,
        payload: dict[str, Any],
        queue: str = "atlas.events",
    ) -> str:
        """Persist a lifecycle event to the events table."""
        event_id = str(uuid4())
        now = datetime.now(UTC)
        conn = self._get_conn()
        def _json_safe(obj: Any) -> Any:
            if isinstance(obj, datetime):
                return obj.isoformat()
            if isinstance(obj, Path):
                return str(obj)
            if isinstance(obj, dict):
                return {k: _json_safe(v) for k, v in obj.items()}
            if isinstance(obj, (list, tuple)):
                return [_json_safe(v) for v in obj]
            if hasattr(obj, "__dataclass_fields__"):
                return _json_safe(asdict(obj))
            return obj

        conn.execute(
            """
            INSERT INTO atlas_events
                (event_id, job_id, routing_key, payload, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (event_id, job_id, routing_key, json.dumps(_json_safe(payload)), now.isoformat()),
        )
        conn.commit()
        return event_id

    async def list_events(self, job_id: str | None = None, limit: int = 1000) -> list[dict[str, Any]]:
        """List persisted events, optionally filtered by job_id."""
        conn = self._get_conn()
        if job_id:
            rows = conn.execute(
                "SELECT event_id, job_id, routing_key, payload, created_at "
                "FROM atlas_events WHERE job_id = ? ORDER BY created_at DESC LIMIT ?",
                (job_id, limit),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT event_id, job_id, routing_key, payload, created_at "
                "FROM atlas_events ORDER BY created_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [
            {
                "event_id": row["event_id"],
                "job_id": row["job_id"],
                "routing_key": row["routing_key"],
                "payload": json.loads(row["payload"]),
                "created_at": row["created_at"],
            }
            for row in rows
        ]

    def _row_to_job(self, row: sqlite3.Row) -> JobRecord:
        """Convert a database row to a JobRecord."""
        d = dict(row)
        for key in ("started_at", "paused_at", "completed_at", "cancelled_at", "resumed_at", "created_at", "updated_at"):
            if d[key]:
                d[key] = datetime.fromisoformat(d[key])
        if d.get("metadata"):
            d["metadata"] = json.loads(d["metadata"])
        else:
            d["metadata"] = {}
        return JobRecord(**d)

    def _row_to_phase(self, row: sqlite3.Row) -> PhaseRecord:
        """Convert a database row to a PhaseRecord."""
        d = dict(row)
        for key in ("started_at", "completed_at", "created_at", "updated_at"):
            if d[key]:
                d[key] = datetime.fromisoformat(d[key])
        return PhaseRecord(**d)
