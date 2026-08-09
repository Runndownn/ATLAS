# ATLAS — Adaptive Task Lifecycle Engine

> In Greek mythology, Atlas held up the celestial spheres. In your pipelines, ATLAS holds up and orchestrates multi-phase workloads.

ATLAS is a standalone orchestration engine for multi-phase batch processing workflows. It sequences pipeline phases (discovery → fingerprinting → extraction → analysis → review), tracks async job state, emits events for observability, and enforces safety checks on filesystem artifacts.

![ATLAS Logo](static/ATLAS-LOGO.png)

## Installation

```bash
pip install atlas-pipeline
```

## Quick Start

```bash
# Run a pipeline
atlas run examples/ctfd_pipeline.yaml

# List jobs
atlas jobs list

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
    P1["1. Recon\n(Filesystem Discovery)"]
    P2["2. Fingerprint\n(SHA-256 + BLAKE3)"]
    P3["3. Extract\n(Safe Archive Unpacking)"]
    P4["4. Analyze\n(Deep Understanding)"]
    P5["5. Review\n(Evidence + Promotion)"]

    P1 -->|"file list"| P2
    P2 -->|"content hashes"| P3
    P3 -->|"extracted artifacts"| P4
    P4 -->|"analysis results"| P5

    style P1 fill:#e1f5fe
    style P2 fill:#f3e5f5
    style P3 fill:#e8f5e9
    style P4 fill:#fff3e0
    style P5 fill:#fce4ec
```

## License

MIT
