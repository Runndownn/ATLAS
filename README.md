# ATLAS — Adaptive Task Lifecycle Engine

> In Greek mythology, Atlas held up the celestial spheres. In your pipelines, ATLAS holds up and orchestrates multi-phase batch processing workflows.

[![PyPI](https://img.shields.io/pypi/v/atlas-pipeline)](https://pypi.org/project/atlas-pipeline/)
[![Tests](https://github.com/Runndownn/ATLAS/actions/workflows/tests.yml/badge.svg)](https://github.com/Runndownn/ATLAS/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

![ATLAS Logo](static/ATLAS-LOGO.png)

## Overview

ATLAS is a standalone orchestration engine for multi-phase batch processing workflows. It sequences pipeline phases (discovery → fingerprinting → extraction → analysis → review), tracks async job state, emits events for observability, and enforces safety checks on filesystem artifacts.

Built for reliability, observability, and extensibility — whether you're processing CTF challenges, document archives, or code repositories.

## Key Features

- **Phase-based orchestration** — Sequential phase execution with pause/resume/cancel
- **Event-driven** — Dual backend: in-memory (default) or RabbitMQ
- **SQLite persistence** — Job state, phase records, and events stored durably
- **Safety-first** — Archive bomb detection, symlink loop prevention, path traversal checks
- **Content-addressable** — SHA-256 + BLAKE3 hashing with automatic deduplication
- **Plugin phases** — Register custom phase handlers via Python Protocol
- **Observable** — Event bus emits structured events at every lifecycle point

## Installation

```bash
pip install atlas-pipeline
```

### With RabbitMQ support

```bash
pip install atlas-pipeline[rabbitmq]
```

### Development setup

```bash
pip install -e ".[dev]"
```

## Quick Start

```bash
# Run a pipeline
atlas run examples/ctfd_pipeline.yaml

# List all jobs
atlas jobs list

# Show job status
atlas job <job-id> status

# Control a running job
atlas job <job-id> pause
atlas job <job-id> resume
atlas job <job-id> cancel
```

## Architecture

### System Overview

```mermaid
graph LR
    subgraph "User / Operator"
        CLI["atlas CLI"]
    end

    subgraph "ATLAS Engine"
        ORCH["Orchestrator"]
        EB["Event Bus"]
        JS["Job Store"]

        ORCH <-->|"phase events"| EB
        ORCH <-->|"job state"| JS
    end

    subgraph "Phase Pipeline"
        P1["1. Recon"]
        P2["2. Fingerprint"]
        P3["3. Extract"]
        P4["4. Analyze"]
        P5["5. Review"]

        P1 --> P2 --> P3 --> P4 --> P5
    end

    subgraph "External Backends"
        RABBIT["RabbitMQ (optional)"]
        SQLITE["SQLite"]
    end

    CLI -->|"run/pause/cancel"| ORCH
    EB <--> RABBIT
    JS <--> SQLITE
    ORCH -->|"dispatch"| P1
    P1 -.->|"handlers"| P2
    P2 -.->|"handlers"| P3
    P3 -.->|"handlers"| P4
    P4 -.->|"handlers"| P5
```

### Data Flow

```mermaid
graph TB
    subgraph "External"
        YAML["Pipeline YAML"]
        FS["Filesystem"]
    end

    subgraph "ATLAS Core"
        O["Orchestrator"]
        EB["Event Bus"]
        JS["Job Store"]
    end

    subgraph "Safety Layer"
        FD["Filesystem Discovery"]
        AS["Archive Safety"]
    end

    subgraph "Storage Layer"
        HS["Hash Store"]
        DB["SQLite DB"]
    end

    YAML -->|"config"| O
    FS -->|"scan"| FD
    FD -->|"risk flags"| AS
    AS -->|"safe members"| HS
    HS -->|"content_id"| DB

    O -->|"phase dispatch"| FD
    O -->|"phase dispatch"| HS
    FD -->|"events"| EB
    HS -->|"events"| EB
    O -->|"job state"| JS
    JS -->|"persist"| DB
```

### Phase Pipeline Sequence

```mermaid
graph LR
    P1["1. Recon<br/>Filesystem Discovery"] --> P2["2. Fingerprint<br/>SHA-256 + BLAKE3"]
    P2 --> P3["3. Extract<br/>Safe Archive Unpacking"]
    P3 --> P4["4. Analyze<br/>Pattern Detection"]
    P4 --> P5["5. Review<br/>Evidence + Promotion"]

    style P1 fill:#e1f5fe
    style P2 fill:#f3e5f5
    style P3 fill:#e8f5e9
    style P4 fill:#fff3e0
    style P5 fill:#fce4ec
```

## Pipeline Phases

| Phase | Name | Description | Source |
|-------|------|-------------|--------|
| 1 | **Reconnaissance** | Filesystem discovery + risk flag computation | Yggdrasil Phase A |
| 2 | **Fingerprinting** | Content hashing (SHA-256 + BLAKE3) + dedup detection | Yggdrasil Phase B |
| 3 | **Structural Discovery** | Archive structure analysis + safe extraction | Yggdrasil Phase C |
| 4 | **Controlled Extraction** | Safe archive unpacking with bomb/path-traversal prevention | Yggdrasil Phase D |
| 5 | **Deep Understanding** | Analysis plugins + pattern detection | Yggdrasil Phase E |
| 6 | **Review/Promotion** | Evidence recording + artifact promotion | Yggdrasil Phase F |

## Process & Development

### Building Blocks

ATLAS is built with a clear separation of concerns:

```
atlas/
├── core/           # Orchestrator, Event Bus, Job Store
├── phases/         # Pipeline phase implementations
├── safety/         # Archive safety + filesystem discovery
├── storage/        # Content hashing + dedup store
├── schema/         # SQLite migrations
├── cli.py          # CLI entry point
└── __init__.py     # Package exports
```

### Development Process

This project follows the **BinReaper Mekanix** challenge-solving methodology, adapted for framework development:

1. **Evidence-based design** — Every phase is extracted from proven patterns in the geezer-mekanix workspace
2. **Phase isolation** — Each phase is independently testable
3. **Safety-first** — All filesystem operations go through the safety layer
4. **Observability** — Event bus emits structured events for every lifecycle action
5. **Reversible** — SQLite projections support atomic rollback

### Development Workflow

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v

# Run a test pipeline
atlas run examples/ctfd_pipeline.yaml

# Check job status
atlas jobs list
atlas job <job-id> status
```

### Creating Custom Phases

```python
from atlas.core.orchestrator import PipelinePhase, PipelineOrchestrator
from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.phases.base import Phase

class MyCustomPhase(Phase):
    name = "my_custom_phase"
    
    async def execute(self, job, config, phase_record):
        await self.emit_event(job, "custom_started")
        # ... your logic here ...
        self.update_progress(percent=100.0, message="Done")

# Register with orchestrator
orchestrator.register_phase_handler(
    PipelinePhase.REVIEW_PROMOTION,  # or a custom phase
    MyCustomPhase()
)
```

## Testing

```bash
# Run full test suite
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=atlas --cov-report=html

# Run specific test file
python -m pytest tests/test_orchestrator.py -v
```

### Test Structure

| File | Tests | Coverage |
|------|-------|----------|
| `test_orchestrator.py` | 13 | Orchestrator + JobRecord + PhaseRecord |
| `test_event_bus.py` | 5 | InMemoryEventBus (publish/consume/close) |
| `test_job_store.py` | 8 | SQLite persistence + metadata round-trip |
| `test_filesystem_discovery.py` | 8 | Risk flags, symlink detection, depth limits |
| `test_archive_safety.py` | 6 | ZIP assessment, traversal detection, limits |
| `test_phases_integration.py` | 3 | Full pipeline end-to-end |

## Project Origin & Philosophy

ATLAS was born from the **BinReaperMekanix** challenge-solving ecosystem. The orchestration patterns, phase sequencing, event bus, and safety checks were extracted from the [geezer-mekanix](https://github.com/Runndownn/geezer-mekanix) workspace's Yggdrasil knowledge-fabric domain and generalized into a standalone, open-source framework.

**What was removed (security/cognitive-ops):**
- RBAC / authentication / authorization
- Cognitive operations layer
- Production secrets management
- TLS / network security controls
- Audit logging to external SIEM
- Multi-tenant isolation

**What remains:** The pure orchestration, discovery, hashing, safety, and phase-engine logic — rebuilt as a clean, framework-agnostic package.

## BinReaper Production TODO Plan

This project is developed using the **BinReaper Production TODO** methodology. The living plan is in [`TODO_ATLAS-PART1.md`](TODO_ATLAS-PART1.md).

### Sprint Slices

| Slice | Status | Description |
|-------|--------|-------------|
| **Slice 1** | ✅ Complete | Core Orchestrator + Event Bus + Job Store + CLI + Tests |
| **Slice 2** | ✅ Complete | Safety Layer (filesystem discovery + archive safety) |
| **Slice 3** | ✅ Complete | Storage & Identity (content hashing + dedup) |
| **Slice 4** | ✅ Complete | Phase Implementations (recon → fingerprint → extract → analyze → review) |
| **Slice 5** | 🔲 In Progress | CLI polish + example pipelines + PyPI publish |

### Development Log

- **2026-08-09** — Project initialized. Slice 1: Core orchestrator, event bus, job store, CLI. 25 tests passing.
- **2026-08-09** — Slices 2-4: Safety layer, storage layer, phase implementations. 44 tests passing, full integration test passing.
- **2026-08-09** — README updated with Mermaid architecture charts and process documentation.

## Hosting & Platform

ATLAS is hosted and sponsored by **REDC2 portals**, providing the infrastructure backbone for pipeline orchestration workloads.

The AI model powering framework development and planning decisions is the **Poolside Laguna S 2.1 (free)** — a 262,112-token model used through the Kilo Gateway for code generation, architectural reasoning, and sprint planning.

## License

MIT — See [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please follow the BinReaper methodology:
1. Review the TODO plan before implementing
2. Write tests for new features
3. Ensure all tests pass before merging
4. Document new phases/plugins in README
