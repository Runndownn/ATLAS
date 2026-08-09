# ATLAS Pipeline Engine — Implementation Backlog
# 
# **Project:** ATLAS (Adaptive Task Lifecycle Engine)
# **Repository:** `github.com/Runndownn/ATLAS`
# **Host/Sponsor:** REDC2 portals
# **Framework Model:** poolside/laguna-s-2.1:free (262,112 tokens)
# **Development Methodology:** BinReaper Production TODO
# **Delivery Posture:** additive, reversible, evidence-gated, vertically testable
# **Python Runtime:** 3.13+

## 1. Purpose

This backlog converts the ATLAS pipeline orchestration architecture into sequenced engineering work. It governs implementation order, authority alignment, database evolution, phase handler lifecycle, migration safety, tests, release gates, and extensibility.

The first implementation objective is a verified framework baseline with all five slices delivered: core orchestrator, safety layer, storage/identity layer, phase implementations, and CLI + examples + CI.

## 2. Repository-grounded decisions

### 2.1 Canonical architecture
`atlas/core/orchestrator.py` contains the authoritative `PipelineOrchestrator` and `PipelineConfig` classes. All pipeline logic must route through this orchestrator — no ad-hoc execution paths.

### 2.2 Separate identity layers
1. Logical source.
2. Source occurrence.
3. Canonical content.
4. Derived knowledge object.

### 2.3 Use the existing migration stream
SQLite schema changes belong in `atlas/core/job_store.py` as `_DB_SCHEMA` constants. Schema must include rollback-friendly definitions (CREATE TABLE IF NOT EXISTS, idempotent index creation).

### 2.4 Phase 0 is read-only
Phase 0 (reconnaissance) may inspect, inventory, hash, and back up to isolated destinations. It may not modify source files, mutate live databases, or enable new writers.

## 3. Sprint Slices

### Exit gate

Slice 5 is complete only when all of the following are proven:

- [x] Core orchestrator with pause/resume/cancel
- [x] Event bus (in-memory + RabbitMQ)
- [x] Job store (SQLite with jobs/phases/events tables)
- [x] Safety layer (filesystem discovery, archive bomb, path traversal)
- [x] Storage layer (SHA-256 + BLAKE3 hashing, content dedup)
- [x] Phase implementations (recon, fingerprint, extract, analyze, review)
- [x] CLI with run/jobs/status/pause/resume/cancel + --help
- [x] Example pipelines (CTF, document processing)
- [x] CI workflow (GitHub Actions)
- [x] 44 tests all passing
- [x] README with Mermaid architecture charts
- [x] BinReaper Production TODO plan (TODO_ATLAS-PART1.md)
- [x] Planning docs in docs/08-planning/Plans_/ (this file + conceptual plan)

## 4. Work Items

| ID | Slice | Priority | Deliverable | Exit evidence |
|---|---|---|---|---|
| ATLAS-1 | 1 | P0 | Pipeline orchestrator | 13 tests, pause/resume/cancel |
| ATLAS-2 | 1 | P0 | Event bus | 5 tests, dual backend |
| ATLAS-3 | 1 | P0 | Job store (SQLite) | 8 tests, schema + round-trip |
| ATLAS-4 | 1 | P0 | CLI | `atlas --help` works, all subcommands |
| ATLAS-5 | 2 | P0 | Filesystem discovery | 8 tests, symlink depth, risk flags |
| ATLAS-6 | 2 | P1 | Archive safety | 6 tests, bomb/traversal detection |
| ATLAS-7 | 2 | P1 | Path safety | Traversal check tests |
| ATLAS-8 | 3 | P0 | Hash store | 3 tests, SHA-256 + BLAKE3, dedup |
| ATLAS-9 | 3 | P0 | Phase base ABC | Protocol + progress tracking |
| ATLAS-10 | 4 | P0 | Phase implementations | 3 integration tests |
| ATLAS-11 | 4 | P1 | Phase handler registration | Orchestrator + phase wiring |
| ATLAS-12 | 5 | P0 | Example pipelines | YAML fixtures + validation |
| ATLAS-13 | 5 | P0 | CI workflow | GitHub Actions tests pass |
| ATLAS-14 | 5 | P0 | README + docs | Architecture diagrams, usage |
| ATLAS-15 | 5 | P1 | PyPI config | pyproject.toml + packaging |

## 5. Phase Lifecycle Model

### Phase States
```
PENDING → RUNNING → COMPLETED
                 └──→ ERROR
CANCELLED ← (from any state)
```

### Phase Handler Contract
```python
class Phase(ABC):
    name: str

    async def execute(self, job: JobRecord, config: PipelineConfig, 
                      phase_record: PhaseRecord) -> None:
        """Execute the phase. Must emit events and update progress."""
        ...

    async def emit_event(self, job: JobRecord, event_type: str,
                         payload: dict[str, Any] | None = None) -> None:
        """Emit an event for observability."""
        ...
```

## 6. Architecture Boundaries

### Core (atlas/core/)
- `orchestrator.py` — PipelineOrchestrator, PipelineConfig, PipelinePhase, PipelineStatus
- `event_bus.py` — EventBus Protocol, InMemoryEventBus, RabbitMQEventBus
- `job_store.py` — JobStore, JobRecord, PhaseRecord, SQLite schema

### Phases (atlas/phases/)
- `base.py` — Phase ABC + PhaseHandler Protocol + PhaseProgress
- `reconnaissance.py` — Filesystem discovery + risk flag computation
- `fingerprinting.py` — Content hashing (SHA-256 + BLAKE3) + dedup
- `extraction.py` — Safe archive unpacking
- `analysis.py` — Pattern detection + plugin interface
- `review.py` — Evidence recording + artifact promotion

### Safety (atlas/safety/)
- `filesystem_discovery.py` — FilesystemDiscovery, FileInfo, risk flags
- `archive_safety.py` — ArchiveSafetyService, bomb detection, traversal checks
- `path_safety.py` — PathSafetyService, traversal pattern detection

### Storage (atlas/storage/)
- `hash_store.py` — HashStore, SHA-256 + BLAKE3 streaming, content dedup

## 7. Testing Strategy

| Test Type | Scope | Files | Count |
|---|---|---|---|
| Unit | Core components | test_orchestrator.py | 13 |
| Unit | Event bus | test_event_bus.py | 5 |
| Unit | Job store | test_job_store.py | 8 |
| Unit | Filesystem discovery | test_filesystem_discovery.py | 8 |
| Unit | Archive safety | test_archive_safety.py | 6 |
| Integration | Full pipeline | test_phases_integration.py | 3 |
| **Total** | | | **44** |

### Test Principles
- Use `:memory:` SQLite for test isolation
- Each phase independently testable
- Safety paths validated with traversal/bomb test fixtures
- Integration tests verify pause/resume/cancel lifecycle

## 8. Risk Register

| Risk | Mitigation | Owner |
|---|---|---|
| SQLite concurrency issues | Shared connection with asyncio.Lock | Pipeline Orchestrator |
| Archive extraction exploits | Bomb detection + path traversal checks | Safety Layer |
| Phase handler exceptions | Caught + recorded in phase_record, pipeline continues | Orchestrator |
| Missing RabbitMQ | Fallback to in-memory event bus | Event Bus |

## 9. Release Plan

| Step | Gate |
|---|---|
| 1. All 44 tests pass | CI green |
| 2. README validated | Usage commands work |
| 3. PyPI publish | `pip install atlas-pipeline` works |
| 4. Example pipelines verified | `atlas run examples/ctfd_pipeline.yaml` runs |
