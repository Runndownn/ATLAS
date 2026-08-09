# ATLAS Pipeline Engine — Conceptual Architecture Plan

**Project:** ATLAS (Adaptive Task Lifecycle Engine)  
**Repository:** `github.com/Runndownn/ATLAS`  
**Host/Sponsor:** REDC2 Portal (built on the Geezer Mekanix Agentic Engineering Platform)  
**Framework Model:** poolside/laguna-s-2.1:free (262,112 tokens)  
**Development Methodology:** BinReaper Production TODO  
**Status:** ACTIVE — All 5 slices complete  

## 1. Problem Statement

Modern pipeline orchestration engines are either overly complex (Kubernetes operators) or too simplistic (script runners). There is a gap for a lightweight, standalone engine that provides:

1. **Phase-based sequencing** — Ordered, pausable, resumable pipeline phases
2. **Durable state** — SQLite-backed job tracking with full lifecycle
3. **Safety guarantees** — Archive bomb detection, symlink loop prevention, path traversal checks
4. **Content identity** — SHA-256 + BLAKE3 hashing with automatic deduplication
5. **Observable execution** — Event bus with structured emission at every lifecycle point

## 2. Solution Overview

ATLAS fills this gap with a minimal, dependency-light Python engine:

```
┌─────────────────────────────────────────────────┐
│                    CLI Layer                     │
│              (atlas run/jobs/job)                │
└──────────────┬──────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────┐
│               Orchestrator Layer                │
│  • PipelineOrchestrator (pause/resume/cancel)   │
│  • Event Bus (InMemory + RabbitMQ)              │
│  • Job Store (SQLite: jobs/phases/events)       │
├─────────────────────────────────────────────────┤
│               Safety Layer                      │
│  • Filesystem Discovery (depth, symlinks, risk) │
│  • Archive Safety (bomb, traversal, limits)    │
│  • Path Safety (traversal pattern detection)   │
└─────────────────────────────────────────────────┘
```

## 3. Core Concepts

### Pipeline
A pipeline is a named sequence of phases, each executing in order. Defined via YAML:

```yaml
name: "my-pipeline"
phases:
  - reconnaissance
  - fingerprinting
  - extraction
  - analysis
  - review
```

### Phase
A phase is a unit of work in a pipeline. Phases are:
- **Ordered** — Executed sequentially
- **Observable** — Emit structured events
- **Trackable** — Progress stored in SQLite
- **Pausable** — Can be paused/resumed at any point
- **Extensible** — Custom phases via Python Protocol

### Job
A job is an execution instance of a pipeline. Jobs maintain:
- Status (pending/running/paused/completed/error/cancelled)
- Progress percentage
- Metadata (discovery results, fingerprinting data, etc.)
- Phase history (PhaseRecord per phase)

### Safety Model
All filesystem operations pass through safety checks:

1. **Filesystem Discovery** — Enumerates files with depth limits, symlink loop detection, and risk flag computation (executable, archive, sensitive)
2. **Archive Safety** — For ZIP/TAR archives: checks compression ratio (bomb detection), entry count limits, path traversal patterns, and nested archive depth
3. **Path Safety** — Detects path traversal patterns (`../`, absolute paths, null bytes) in all user-provided paths

### Content Identity
- **Hashing** — Files are hashed with both SHA-256 and BLAKE3 (streaming, 1 MiB chunks)
- **Deduplication** — If a hash is already known, the file is skipped
- **Content Store** — HashStore tracks content_id → processing metadata

## 4. Architecture Decisions

| Decision | Outcome | Rationale |
|---|---|---|
| SQLite as primary store | In-memory by default, file path for persistence | Lightweight, no external dependencies required |
| asyncio for concurrency | Pipeline runs asynchronously, phases can await | Prevents blocking on I/O, enables pause/resume |
| Event Bus pattern | InMemoryEventBus + RabbitMQEventBus | Observability decoupled from core logic |
| Phase ABC + Protocol | Phase base class + PhaseHandler Protocol | Extensibility without framework lock-in |
| Safety as layers | Separate safety/ module with clear boundaries | Defense in depth, each check independently testable |

## 5. Data Model

```
jobs ──┐
       │
phases │ (1:N)
       │
events ┘ (1:N, optional)

Job: (job_id, root_id, source_path, phase, status, progress, metadata)
Phase: (phase_id, job_id, phase, status, progress, error, timestamps)
Event: (event_id, job_id, routing_key, payload, created_at)
```

## 6. Extraction Rationale

The Geezer Mekanix Agentic Engineering Platform transforms human intent into **Bounded. Observable. Evidence-Aware. Governed.** execution, providing the infrastructure backbone for ATLAS pipeline orchestration workloads.

- **Security infrastructure** — RBAC, authentication, TLS, audit logging to SIEM
- **Cognitive operations** — Knowledge fabric ingestion, source registry, retrieval synchronization
- **Production ops** — Secrets management, multi-tenant isolation, deployment manifests

What remains is pure orchestration logic: phase sequencing, event emission, job state tracking, and safety checks — generalized for any multi-phase pipeline workload.

## 7. Technology Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.13+ |
| **Build** | Hatchling (pyproject.toml) |
| **Testing** | pytest + asyncio-mode |
| **Database** | SQLite (stdlib) |
| **Hashing** | hashlib (SHA-256) + blake3 (BLAKE3) |
| **Messaging** | asyncio (in-memory) + aio-pika (RabbitMQ, optional extra) |
| **CLI** | argparse + asyncio.run |
| **CI** | GitHub Actions |
| **Development Model** | poolside/laguna-s-2.1:free (262,112 tokens) via Kilo Gateway |

## 8. Quality Attributes

| Attribute | Target | Verification |
|---|---|---|
| **Reliability** | 99.9% job completion | 44 passing tests, integration tests |
| **Observability** | Structured events for all lifecycle | EventBus emits on phase start/complete/error |
| **Safety** | Zero path traversal exploits | PathSafetyService + ArchiveSafetyService |
| **Extensibility** | Custom phases via Protocol | Phase ABC + register_phase_handler |
| **Performance** | Streaming, 1MiB chunks | HashStore streaming hash |
| **Testability** | 80%+ coverage | pytest --cov report |

## 9. Risk & Mitigation

| Risk | Mitigation |
|---|---|
| SQLite concurrency limits | asyncio.Lock serializes writes; shared connection |
| Archive extraction exploits | Pre-extraction safety checks (bomb ratio, traversal, limits) |
| Phase handler crashes | Try/except in orchestrator, recorded as phase error |
| RabbitMQ unavailable | Graceful fallback to InMemoryEventBus |
| Large file memory | Streaming 1 MiB chunks for hashing |
| Symlink loops | Depth limit + visited path tracking |

## 10. Sprint Plan

| Sprint | Slice | Scope | Tests | Status |
|---|---|---|---|---|
| Sprint 1 | Slice 1 | Core orchestrator, event bus, job store, CLI | 25 | ✅ Complete |
| Sprint 1b | Slice 2 | Filesystem discovery, archive safety, path safety | 22 | ✅ Complete |
| Sprint 1c | Slice 3 | Hash store, schema | 3 | ✅ Complete |
| Sprint 1d | Slice 4 | All 6 phases + integration tests | 3 | ✅ Complete |
| Sprint 2 | Slice 5 | CLI polish, examples, CI, PyPI, docs | 44 total | ✅ Complete |
