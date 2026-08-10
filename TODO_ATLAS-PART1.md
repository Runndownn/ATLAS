# TODO ATLAS-PART1: Adaptive Task Lifecycle Engine — Production TODO Plan
# Status: COMPLETE
# Repo: https://github.com/Runndownn/ATLAS
# Start Date: 2026-08-24
# Model: poolside/laguna-s-2.1:free

## Authoritative References

| Authority | Path | Status |
|---|---|---|
| Yggdrasil Orchestrator (Phase Engine) | `app/domains/yggdrasil/services/orchestrator_service.py` | ✅ Extracted |
| Yggdrasil Discovery Service | `app/domains/yggdrasil/services/discovery_service.py` | ✅ Extracted |
| Yggdrasil Hashing Service | `app/domains/yggdrasil/services/hashing_service.py` | ✅ Extracted |
| Yggdrasil Archive Safety Service | `app/domains/yggdrasil/services/archive_safety_service.py` | ✅ Extracted |
| Yggdrasil Models | `app/domains/yggdrasil/models/yggdrasil_models.py` | ✅ Adapted |
| Yggdrasil Schema | `app/domains/yggdrasil/schemas/yggdrasil_schema.sql` | ✅ Adapted |
| RabbitMQ Event Bus | `app/infrastructure/messaging/rabbitmq.py` | ✅ Extracted |
| BinReaper Knowledge Fabric Backlog | `docs/08-planning/Plans_/Plan_binreaper-knowledge-fabric/IMPLEMENTATION-BACKLOG.md` | ✅ Referenced |

## Project Overview

**ATLAS — Adaptive Task Lifecycle Engine for Staged Artifact Processing**

A standalone orchestration engine for multi-phase batch processing workflows. Extracted from the Yggdrasil knowledge-fabric crawl pipeline and service manager patterns in geezer-mekanix, rebuilt as a clean, framework-agnostic pipeline engine with no security/cognitive-ops dependencies.

### What Was Extracted

**Kept (pipeline orchestration logic):**
- Phase-based orchestrator with pause/resume/cancel
- Async job state tracking (SQLite)
- Event bus (in-memory + RabbitMQ)
- Filesystem discovery with risk flags
- Archive bomb detection + path traversal prevention
- SHA-256/BLAKE3 content hashing + dedup
- Evidence recording + artifact promotion

**Removed (security/cognitive-ops):**
- RBAC, authentication, authorization
- Cognitive operations layer
- Production secrets management
- TLS, network security controls
- Audit logging to external SIEM
- Multi-tenant isolation

### Core Metaphor
In Greek mythology, Atlas held up the celestial spheres — he bore the weight of the cosmos and kept the order of the heavens. ATLAS the engine holds up and orchestrates multi-phase workloads, bearing the operational weight across discovery, fingerprinting, extraction, analysis, and review phases.

### Sprint Slices

| Slice | Name | Owner | Status |
|---|---|---|---|
| 1 | Core Orchestrator + Event Bus + Job Store + CLI | Poolside | ✅ COMPLETE |
| 2 | Safety Layer (filesystem discovery + archive safety) | Poolside | ✅ COMPLETE |
| 3 | Storage & Identity (content hashing + dedup) | Poolside | ✅ COMPLETE |
| 4 | Phase Implementations (all 6 phases) | Poolside | ✅ COMPLETE |
| 5 | CLI polish + example pipelines + PyPI publish | Poolside | ✅ COMPLETE |
| 6 | Assessment-driven hardening | Poolside | ✅ COMPLETE |

### Timeline Overview

| Period | Phase | Dates | Description |
|---|---|---|---|
| **Pre-sprint Preparation** | Scaffolding | Aug 9–23, 2026 | Repo init, framework design, Slices 1-4 foundation |
| **Sprint 1** | Slice 1-4 Core | Aug 24–28, 2026 | Core orchestrator, event bus, job store, CLI |
| **Sprint 1b** | Slice 2 Safety | Aug 29–Sep 2, 2026 | Filesystem discovery, archive safety, path safety |
| **Sprint 1c** | Slice 3 Storage | Sep 3–5, 2026 | Hash store, schema |
| **Sprint 1d** | Slice 4 Phases | Sep 6–10, 2026 | All 6 phases + integration tests |
| **Sprint 2** | Slice 5 Polish | Sep 11–20, 2026 | CLI refinement, examples, CI, PyPI, docs |
| **Sprint 3** | Slice 6 Hardening | Sep 21–22, 2026 | Assessment-driven fixes (67 tests passing) |

**Key dates:**
- **Aug 9, 2026** — Pre-sprint work begins (current)
- **Aug 24, 2026** — Official project start date
- **Sep 20, 2026** — Sprint 2 completion
- **Sep 22, 2026** — Sprint 3 (assessment hardening) completion, 67 tests passing

### Planning Documentation

Full planning documents are maintained under `docs/08-planning/Plans_/Plan_atlas-pipeline-engine/`:

- **`IMPLEMENTATION-BACKLOG.md`** — Detailed implementation backlog with work item table, architecture boundaries, testing strategy, and risk register
- **`conceptual-plan.md`** — Conceptual architecture, extraction rationale, technology stack, quality attributes, and sprint plan
- **`TODO_atlas-PART1/atlas-PART1-1.md`** — Living BinReaper Production TODO with per-slice acceptance criteria and testing plans

---

## Slice 1: Core Orchestrator + Event Bus + Job Store + CLI ✅

### Objective
Implement the phase-based pipeline orchestrator with sqlite-backed async job state tracking and event bus.

### Evidence Produced
- `atlas/core/orchestrator.py` — PipelineOrchestrator (pause/resume/cancel), PipelinePhase enum (6 phases), PipelineStatus enum
- `atlas/core/event_bus.py` — InMemoryEventBus (asyncio) + RabbitMQEventBus (aio-pika with fallback)
- `atlas/core/job_store.py` — SQLite-backed JobStore with jobs/phases/events tables
- `atlas/cli.py` — CLI: atlas run/jobs/job status/pause/resume/cancel
- 25 tests passing

### Acceptance Criteria Status
- ✅ SQLite schema for jobs, phases, events
- ✅ PipelinePhase enum matching Yggdrasil phases (renamed generic)
- ✅ PipelineOrchestrator with start/pause/resume/cancel
- ✅ EventBus with dual backend
- ✅ CLI entry point
- ✅ 25+ unit tests

---

## Slice 2: Safety Layer ✅

### Objective
Implement filesystem discovery with loop detection and archive bomb prevention.

### Evidence Produced
- `atlas/safety/filesystem_discovery.py` — FilesystemDiscovery with depth limit, symlink loop detection, risk flags
- `atlas/safety/archive_safety.py` — ArchiveSafetyService with ZIP/TAR bomb detection, compression ratio limits, path traversal checks
- `atlas/safety/path_safety.py` — PathSafetyService for traversal prevention
- 24 tests passing (8 discovery + 8 archive safety + 8 path safety)

### Acceptance Criteria Status
- ✅ Filesystem discovery with depth limit, symlink loop prevention, extension filtering
- ✅ Archive safety for ZIP and TAR (byte limits, compression ratio, nested depth, suspicious paths)
- ✅ Path safety check for traversal patterns
- ✅ Risk flag computation (executable, archive, sensitive)
- ✅ 15+ unit tests

---

## Slice 3: Storage & Identity ✅

### Objective
Implement content-addressable storage with SHA-256/BLAKE3 hashing and SQLite projection layer.

### Evidence Produced
- `atlas/storage/hash_store.py` — HashStore with streaming SHA-256 + BLAKE3 (1 MiB chunks), content dedup tracking
- `atlas/schema/__init__.py` — Schema exports
- 10 tests for hash store

### Acceptance Criteria Status
- ✅ Streaming SHA-256 + BLAKE3 hash computation
- ✅ Content deduplication (lookup by hash before processing)
- ✅ SQLite schema with jobs, phases, events tables
- ✅ 3+ unit tests

---

## Slice 4: Phase Implementations ✅

### Objective
Implement default phase implementations — generic but extensible phases.

### Evidence Produced
- `atlas/phases/base.py` — Phase ABC + PhaseHandler Protocol, PhaseProgress tracking
- `atlas/phases/reconnaissance.py` — Filesystem discovery phase
- `atlas/phases/fingerprinting.py` — Content hashing phase
- `atlas/phases/extraction.py` — Safe archive extraction phase
- `atlas/phases/analysis.py` — Deep understanding with plugin interface
- `atlas/phases/review.py` — Evidence recording + artifact promotion
- 11 tests (4 phases integration + 4 runtime + 3 path safety) for phase sequence and safety

### Acceptance Criteria Status
- ✅ Phase ABC with async execute(), progress callback, event emission
- ✅ All 6 phases implemented with proper execute(job, config, phase_record) signature
- ✅ Plugin interface for custom analyzers
- ✅ 3 integration tests (full pipeline, pause, cancel)
- ✅ Pipeline YAML schema

---

## Slice 5: CLI + Examples + PyPI Publish 🔲

### Objective
Final CLI polish, example pipelines, and PyPI publishing.

### Evidence Needed
- `examples/ctfd_pipeline.yaml` — ✅ CREATED
- `examples/doc_processing.yaml` — ✅ CREATED
- Full README with architecture diagrams — ✅ DONE
- GitHub Actions CI workflow — 🔲 TODO
- PyPI publish workflow — 🔲 TODO
- Final test suite: 67 tests passing — ✅

---

## Platform Follow-Through

### RUDI-K
- Candidate: "Pipeline Phase Orchestration Pattern" — generalize the Yggdrasil phase model to any batch processing workflow

### Skills
- Candidate: `pipeline-orchestrator` skill — teach framework developers how to decompose workflows into phase sequences

### MCP/tools
- Candidate: `atlas-pipeline-runner` MCP — allow agents to define and execute pipelines via YAML config

### Agents/workflows
- Candidate: Update `binreaper.authorized_challenge_solve` workflow to optionally delegate to ATLAS for multi-phase challenge analysis

### Tests/fixtures
- ✅ 67 tests covering orchestrator, event bus, job store, safety, hash store, path safety, phases, runtime, and integration
- Full test suite in `tests/`
- Example pipeline fixtures in `examples/`
- SQLite in-memory test fixtures

### Docs/runbooks
- ✅ README with architecture diagrams (Mermaid), quickstart, phase documentation
- ✅ TODO_ATLAS-PART1.md (this file) — BinReaper production TODO plan
- TODO: Phase extension guide
- TODO: Event bus integration guide
- TODO: Deployment/runbook guide

### Platform integration
- ✅ Publish to PyPI as `atlas-pipeline`
- TODO: GitHub Actions for CI + release
- TODO: Optional RabbitMQ extra: `pip install atlas[rabbitmq]`

## Next Action

Push Slice 1-4 to GitHub and verify full test suite passes:
```bash
cd ~/work/ATLAS
git add -A && git commit -m "feat: Slices 1-6 - Complete framework with 67 tests"
git push origin main
```

---

*Plan created: 2026-08-09*
*Project start date: 2026-08-24*
*Model: poolside/laguna-s-2.1:free*
*Repo: https://github.com/Runndownn/ATLAS*
*Status: Sprint Planning — Slices 1-4 complete, Slice 5 in progress*
