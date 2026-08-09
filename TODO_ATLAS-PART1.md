# TODO ATLAS-PART1: Adaptive Task Lifecycle Engine — Production TODO Plan
# Status: ACTIVE (Sprint Planning)
# Repo Target: New standalone GitHub repo — `atlas`

## Authoritative References

| Authority | Path | Status |
|---|---|---|
| Yggdrasil Orchestrator (Phase Engine) | `app/domains/yggdrasil/services/orchestrator_service.py` | ✅ FOUND |
| Yggdrasil Discovery Service | `app/domains/yggdrasil/services/discovery_service.py` | ✅ FOUND |
| Yggdrasil Hashing Service | `app/domains/yggdrasil/services/hashing_service.py` | ✅ FOUND |
| Yggdrasil Archive Safety Service | `app/domains/yggdrasil/services/archive_safety_service.py` | ✅ FOUND |
| Yggdrasil Models | `app/domains/yggdrasil/models/yggdrasil_models.py` | ✅ FOUND |
| Yggdrasil Schema | `app/domains/yggdrasil/schemas/yggdrasil_schema.sql` | ✅ FOUND |
| Yggdrasil API Routes | `app/domains/yggdrasil/api/yggdrasil_routes.py` | ✅ FOUND |
| RabbitMQ Event Bus | `app/infrastructure/messaging/rabbitmq.py` | ✅ FOUND |
| BinReaper Knowledge Fabric Backlog | `docs/08-planning/Plans_/Plan_binreaper-knowledge-fabric/IMPLEMENTATION-BACKLOG.md` | ✅ FOUND |

## Project Overview

**ATLAS — Adaptive Task Lifecycle Engine for Staged Artifact Processing**

A standalone orchestration engine for multi-phase batch processing workflows. Extracted from the Yggdrasil knowledge-fabric crawl pipeline and service manager patterns in geezer-mekanix, rebuilt as a clean, framework-agnostic pipeline engine with no security/cognitive-ops dependencies.

### Core Metaphor
In Greek mythology, Atlas held up the celestial spheres — he bore the weight of the cosmos and kept the order of the heavens. ATLAS the engine holds up and orchestrates multi-phase workloads, bearing the operational weight across discovery, fingerprinting, extraction, analysis, and review phases.

### Sprint Slices

| Slice | Name | Owner | Status |
|---|---|---|---|
| 1 | Core Orchestrator + Event Bus | Build/Scaffold | OPEN |
| 2 | Safety Layer | Build/Scaffold | OPEN |
| 3 | Storage & Identity | Build/Scaffold | OPEN |
| 4 | Phase Implementations | Build/Scaffold | OPEN |
| 5 | CLI + Examples + Publish | Build/Scaffold | OPEN |

---

## Slice 1: Core Orchestrator + Event Bus

### Objective
Implement the phase-based pipeline orchestrator with async job tracking, event bus, and CLI entry point. This is the backbone extracted from `yggdrasil/services/orchestrator_service.py` and the RabbitMQ event bus from `app/infrastructure/messaging/rabbitmq.py`.

### Why It Matters
The orchestrator is the engine's heart — it sequences phases, tracks job state, and emits events for observability. Without this, nothing runs.

### Evidence Needed
- `atlas/core/orchestrator.py` — Phase sequence engine with pause/resume/cancel
- `atlas/core/event_bus.py` — Dual-backend event bus (in-memory + RabbitMQ)
- `atlas/core/job_store.py` — SQLite-backed async job state tracking
- `atlas/cli.py` — CLI entry point with `atlas run` and `atlas jobs` commands
- Unit tests: `tests/test_orchestrator.py`, `tests/test_event_bus.py`
- Integration test: full phase sequence run

### Knowledge Basis
- `app/domains/yggdrasil/services/orchestrator_service.py` — CrawlPhase enum (reconnaissance, fingerprinting, structural_discovery, controlled_extraction, deep_understanding, review_promotion)
- `app/domains/yggdrasil/models/yggdrasil_models.py` — SourceRoot, CanonicalContent, FileOccurrence models (generalize to PhaseArtifact)
- `app/infrastructure/messaging/rabbitmq.py` — RabbitMQFanoutPublisher + InMemoryBroker pattern

### Acceptance Criteria
- [ ] Create repo scaffold with pyproject.toml (dependencies: sqlite3 stdlib, typing_extensions, rabbitmq optional)
- [ ] Implement `CrawlPhase` → `PipelinePhase` (generic phases: discover, fingerprint, extract, analyze, review, complete)
- [ ] Implement `PipelineOrchestrator` class with start/pause/resume/cancel
- [ ] Implement `EventBus` with in-memory + optional RabbitMQ backends
- [ ] Implement `JobStore` with SQLite persistence for job state + progress
- [ ] CLI: `atlas run <pipeline.yaml>`, `atlas jobs list`, `atlas job <id> status`
- [ ] 10+ unit tests passing
- [ ] Integration test: 3-phase pipeline runs end-to-end

---

## Slice 2: Safety Layer

### Objective
Implement the safety and filesystem discovery layer — archive bomb detection, symlink loop prevention, path traversal checking, and risk-flagged file discovery. Extracted from `yggdrasil/services/discovery_service.py` and `yggdrasil/services/archive_safety_service.py`.

### Why It Matters
Any pipeline that processes external artifacts must do so safely. This prevents archive bombs, infinite symlink loops, and path traversal attacks during batch processing.

### Evidence Needed
- `atlas/safety/filesystem_discovery.py` — Safe traversal with symlink loop detection
- `atlas/safety/archive_safety.py` — ZIP/TAR archive bomb detection
- `atlas/safety/path_safety.py` — Path traversal prevention + risk flag computation
- Tests for all safety checks with edge cases
- Integration with orchestrator phases

### Knowledge Basis
- `app/domains/yggdrasil/services/discovery_service.py` — FileDiscoveryRecord, DiscoveryStats, SUSPICIOUS_EXTENSIONS, SUSPICIOUS_NAMES
- `app/domains/yggdrasil/services/archive_safety_service.py` — ArchiveSafetyReport, ArchiveMember, MAX_TOTAL_UNCOMPRESSED_BYTES, MAX_NESTED_DEPTH

### Acceptance Criteria
- [ ] Filesystem discovery with depth limit, symlink loop prevention, extension filtering
- [ ] Archive safety assessment for ZIP and TAR (compressed/uncompressed byte limits, compression ratio, nested depth, suspicious paths)
- [ ] Path safety check for traversal patterns (.., /etc/, .ssh/, \windows\)
- [ ] Risk flag computation (executable extensions, suspicious names, large archives)
- [ ] 15+ unit tests covering edge cases
- [ ] Safety checks integrated into discover phase

---

## Slice 3: Storage & Identity

### Objective
Implement content-addressable storage with SHA-256/BLAKE3 hashing, SQLite schema with rollback capabilities, and deterministic projection builder. Extracted from `yggdrasil/services/hashing_service.py` and the BinReaper Knowledge Fabric backlog (PR E/F patterns).

### Why It Matters
Content addressing prevents duplicate processing, provides integrity verification, and enables deterministic pipeline snapshots with atomic rollback.

### Evidence Needed
- `atlas/storage/hash_store.py` — SHA-256 + BLAKE3 streaming hash computation
- `atlas/storage/projection_builder.py` — Deterministic SQLite projection with atomic swap
- `atlas/schema/migrations.sql` — SQLite schema with version tracking + rollback functions
- `atlas/schema/__init__.py` — Schema migration runner
- Tests for hash uniqueness, content dedup, rollback behavior

### Knowledge Basis
- `app/domains/yggdrasil/services/hashing_service.py` — HashingService, HashResult, CHUNK_SIZE, streaming hasher
- `app/domains/yggdrasil/schemas/yggdrasil_schema.sql` — SQL patterns, triggers, rollback function
- `docs/08-planning/Plans_/Plan_binreaper-knowledge-fabric/IMPLEMENTATION-BACKLOG.md` — SQLite projection builds, integrity/smoke tests, versioned snapshots, host-side atomic activation

### Acceptance Criteria
- [ ] Streaming SHA-256 + BLAKE3 hash computation (1 MiB chunks)
- [ ] Content deduplication (lookup by hash before processing)
- [ ] SQLite schema with: jobs, phases, artifacts, content, events tables
- [ ] Projection builder: writes to temp DB, verifies integrity, atomic swap
- [ ] Rollback function for full schema teardown
- [ ] 12+ unit tests for hash uniqueness, dedup, projection integrity

---

## Slice 4: Phase Implementations

### Objective
Implement the default phase implementations — generic but extensible phases for discover, fingerprint, extract, analyze, and review. Each phase is a plugin that can be overridden in a pipeline YAML definition.

### Why It Matters
Phases are what make ATLAS a pipeline engine rather than just a state machine. Generic phases cover 80% of use cases; custom phases handle the rest.

### Evidence Needed
- `atlas/phases/base.py` — Phase ABC with execute() and validate()
- `atlas/phases/discover.py` — Filesystem discovery phase (uses Safety Layer)
- `atlas/phases/fingerprint.py` — Content hashing phase (uses Storage & Identity)
- `atlas/phases/extract.py` — Safe archive extraction phase
- `atlas/phases/analyze.py` — Plugin hook for deep analysis
- `atlas/phases/review.py` — Promotion/evidence recording phase
- Example phase plugins in `examples/`

### Knowledge Basis
- `app/domains/yggdrasil/services/orchestrator_service.py` — _execute_phase dispatch, phase methods (_run_reconnaissance, etc.)
- `app/domains/yggdrasil/services/discovery_service.py` — Phase A: reconnaissance logic
- `app/domains/yggdrasil/services/hashing_service.py` — Phase B: fingerprinting logic
- BinReaper Knowledge Fabric backlog PR D/E: fingerprints, equivalence, extraction

### Acceptance Criteria
- [ ] Phase ABC with async execute(), progress callback, event emission
- [ ] Discover phase: traverses path, applies safety checks, emits discovery events
- [ ] Fingerprint phase: hashes all discovered artifacts, stores in content table
- [ ] Extract phase: safe archive extraction with bomb prevention
- [ ] Analyze phase: plugin interface for custom analysis
- [ ] Review phase: evidence recording, artifact promotion
- [ ] 8+ unit tests for phase behavior
- [ ] Pipeline YAML schema with phase config

---

## Slice 5: CLI + Examples + Publish

### Objective
Final CLI polish, example pipelines, documentation, and publish to PyPI/npm.

### Why It Matters
Shipping a framework without examples and docs is just a library. This slice makes ATLAS usable and shareable.

### Evidence Needed
- `atlas/cli.py` — Full CLI: run, jobs, job, phases, info
- `atlas/__init__.py` — Package exports
- `examples/ctfd_pipeline.yaml` — CTF challenge analysis pipeline
- `examples/doc_processing.yaml` — Document indexing pipeline
- `examples/code_indexing.yaml` — Code repository indexing pipeline
- `README.md` — Installation, quickstart, architecture overview
- `LICENSE` — MIT
- `pyproject.toml` — Build config + publish metadata
- GitHub Actions CI workflow

### Acceptance Criteria
- [ ] `atlas run <pipeline.yaml>` executes full pipeline with progress display
- [ ] `atlas jobs list` shows all jobs with status
- [ ] `atlas job <id> [pause|resume|cancel]` controls running jobs
- [ ] Three example pipelines with README instructions
- [ ] Full test suite passes (50+ tests total)
- [ ] `pip install atlas` works from PyPI test
- [ ] GitHub Actions CI green badge

---

## Platform Follow-Through

### RUDI-K
- Candidate: "Pipeline Phase Orchestration Pattern" — generalize the Yggdrasil phase model to any batch processing workflow

### Skills
- Candidate: `pipeline-orchestrator` skill — teach challenge planners how to decompose workflows into phase sequences

### MCP/tools
- Candidate: `atlas-pipeline-runner` MCP — allow agents to define and execute pipelines via YAML config

### Agents/workflows
- Candidate: Update `binreaper.authorized_challenge_solve` workflow to optionally delegate to ATLAS for multi-phase challenge analysis

### Tests/fixtures
- Full unit + integration test suite in `tests/`
- Example pipeline fixtures in `examples/`
- Schema migration test fixtures

### Docs/runbooks
- README with architecture diagram (Mermaid)
- Phase extension guide
- Event bus integration guide
- Safety layer usage guide

### Platform integration
- Publish to PyPI as `atlas-pipeline`
- GitHub Actions for CI + release
- Optional RabbitMQ extra: `pip install atlas[rabbitmq]`

## Next Action
Create the repo scaffold:
```bash
mkdir /mnt/geezer-venvs/work/geezer-mekanix/atlas
cd atlas
git init  # will be pushed to new GitHub repo
```
Then start Slice 1: Core Orchestrator + Event Bus.

---

*Plan created: 2026-08-24*
*Project start date: 2026-08-24*
*Model: poolside/laguna-s-2.1:free*
*Status: Sprint Planning — ready for execution*
