# Flagship Production Engineering TODO Plan — ATLAS Production Engineering TODO Program

Evidence and assumption note: evidence mode is `ATTACHED-SNAPSHOT`. The latest ZIP is authoritative for architecture and macro tasks. Repository behavior is limited to frozen cited evidence; unsupported conclusions use stable assumption IDs and exactly one validation task.

| Epic name | P0 | P1 | P2 | P3 | Total estimated hours | Three highest-risk tasks |
|---|---:|---:|---:|---:|---:|---|
| E1 — Evidence, baseline, and authority reconciliation | 4 | 0 | 0 | 0 | 42 | T1.1.1: Implementing against a stale or mislocated repository surface could invalidate every downstream TODO.; T1.1.2: A transcription or diagram-reading error could drive the production backlog away from the intended product.; T1.1.3: Unverified donor transplantation could import hidden dependencies, governance coupling, platform races, or license obligations. |
| E2 — Deterministic current-behavior characterization | 4 | 0 | 0 | 0 | 50 | T2.1.1: A weak fixture contract could preserve accidental nondeterminism or hide the exact defect later corrections must prove.; T2.1.2: Characterizing only unit seams could miss false success and drift at public interfaces.; T2.1.3: Timing-only or unbounded adversarial tests can be flaky, unsafe, or misleading. |
| E3 — Versioned pipeline semantics and configuration | 4 | 0 | 0 | 0 | 56 | T3.1.1: A permissive model could continue to allow caller-controlled lifecycle order under a new name.; T3.1.2: Configuration merge or hashing drift could make replay, compatibility, and policy enforcement non-reproducible.; T3.1.3: Hidden dictionary contracts could survive inside handlers and continue to drift from schema and documentation. |
| E4 — StateStore and SQLite migration foundation | 4 | 0 | 0 | 0 | 60 | T4.1.1: An overly broad abstraction or hidden direct commits would preserve inconsistent transaction ownership.; T4.1.2: Incorrect locking or pragma assumptions can produce stalls, lost updates, or false readiness.; T4.1.3: A migration defect could irreversibly damage the only authoritative job database. |
| E5 — Explicit lifecycle state machines, attempts, and fencing | 4 | 0 | 0 | 0 | 58 | T5.1.1: Ambiguous states would make retries, controls, and recovery nondeterministic even with durable persistence.; T5.1.2: Mutable or duplicate attempt records could conceal repeated execution and side effects.; T5.1.3: A stale owner or duplicate request could commit a second side effect or overwrite terminal truth. |
| E6 — Registered sources and immutable intake generations | 4 | 0 | 0 | 0 | 58 | T6.1.1: Conflating source roots, observations, and paths would make provenance and mutation detection impossible to reason about.; T6.1.2: A partial or nondeterministic traversal could become a falsely authoritative intake manifest.; T6.1.3: Acceptance without a deterministic completeness barrier would make downstream identity and safety claims untrustworthy. |
| E7 — Persistent content identity and occurrence linkage | 4 | 0 | 0 | 0 | 50 | T7.1.1: Treating identity and storage as the same concept would create false replayability and break provenance.; T7.1.2: A path-based or single-stat hash read can bind new bytes to an old occurrence after source mutation.; T7.1.3: Naive deduplication could skip required work or lose occurrence provenance. |
| E8 — Durable events and transactional outbox | 4 | 0 | 0 | 0 | 56 | T8.1.1: An ambiguous event model could be mistaken for authoritative state or lose causal reconstruction.; T8.1.2: Independent commits can leave state without evidence or evidence without truth.; T8.1.3: Unbounded or authority-confused delivery can cause memory/storage exhaustion or duplicate effects. |
| E9 — Durable progress, controls, safe points, and checkpoints | 4 | 0 | 0 | 0 | 60 | T9.1.1: An overpowered context or opaque checkpoint would recreate hidden authority and unsafe replay.; T9.1.2: Unbounded progress writes can create contention, while stale phase-local updates mislead operators.; T9.1.3: Persisting a request without safe-point semantics can report a pause or cancel that never safely took effect. |
| E10 — Canonical race-resistant source access | 4 | 0 | 0 | 0 | 56 | T10.1.1: Cross-platform path semantics can make a syntactically clean path escape its intended root.; T10.1.2: Check-then-open path validation can be bypassed by concurrent filesystem mutation.; T10.1.3: Mixing read and write path helpers can give untrusted inputs an unintended mutation path. |
| E11 — Quarantine, recursive archive budgets, and controlled materialization | 4 | 0 | 0 | 0 | 62 | T11.1.1: Source-adjacent or weakly owned extraction can overwrite evidence, collide on replay, or escape cleanup.; T11.1.2: Counting nested files without recursively enforcing cumulative limits leaves decompression and parser exhaustion paths.; T11.1.3: Extraction driven from live paths or library defaults can bypass structural decisions and create uncontrolled files. |
| E12 — Optional immutable local content store | 0 | 4 | 0 | 0 | 56 | T12.1.1: An implicit default could create unexpected disk growth or false reproducibility claims.; T12.1.2: A non-atomic or overwrite-capable CAS can corrupt canonical bytes while preserving a trusted digest label.; T12.1.3: Filesystem and database state can diverge around blob commits, producing false presence or leaked capacity. |
| E13 — Structural and extraction lineage contracts | 0 | 4 | 0 | 0 | 56 | T13.1.1: A structure report not bound to exact bytes/policy can authorize extraction of different content.; T13.1.2: Without attempt-level records, partial writes and retries cannot be reconciled or attributed.; T13.1.3: Convenience fallback can bypass the structural safety barrier and reintroduce live-source ambiguity. |
| E14 — Typed plugin contracts, registry, and trust policy | 0 | 4 | 0 | 0 | 58 | T14.1.1: Weak contracts let plugins smuggle authority, lose attribution, or create unbounded/ambiguous outputs.; T14.1.2: Nondeterministic or unsafe discovery can execute the wrong plugin version or import hostile code at startup.; T14.1.3: Treating declarations as grants or trusting all plugins in-process gives third-party code host and lifecycle influence. |
| E15 — ExecutionBackend contracts and trusted in-process execution | 0 | 4 | 0 | 0 | 62 | T15.1.1: A weak execution contract can leak authority or force lifecycle semantics into each backend.; T15.1.2: An in-process backend can accidentally retain direct runtime authority or block the event loop.; T15.1.3: Accepting backend claims directly would let crashes, stale workers, or malicious plugins corrupt lifecycle truth. |
| E16 — Phase-internal work items, deterministic reuse, and unified budgets | 0 | 4 | 0 | 0 | 62 | T16.1.1: A generic work graph could quietly turn ATLAS into a scheduler and weaken lifecycle semantics.; T16.1.2: Unbounded fan-out or weak claims can exhaust memory and duplicate work.; T16.1.3: An incomplete cache key can return stale or policy-incompatible conclusions with convincing provenance. |
| E17 — Durable findings, evidence, review, and publication | 0 | 4 | 0 | 0 | 64 | T17.1.1: A loose finding schema could recreate hidden metadata contracts and allow analytical assertions to masquerade as trusted evidence.; T17.1.2: Evidence may become a vague label that hides source quality or lets a plugin self-certify its claims.; T17.1.3: Unresolved review classes could either burden harmless work with unnecessary approval or allow consequential publication without accountable authority. |
| E18 — Retry, timeout, idempotency, reconciliation, and crash recovery | 0 | 4 | 0 | 0 | 62 | T18.1.1: A generic retry flag can repeat unsafe side effects or hide the distinction between validation, exhaustion, and unknown external state.; T18.1.2: Retries can create duplicate effects, storms, or irreproducible behavior if timing and identity are process-local.; T18.1.3: A restart path can become a second orchestrator that advances state from stale or incomplete evidence. |
| E19 — Long-running local runtime ownership | 0 | 4 | 0 | 0 | 58 | T19.1.1: A daemon can create a second execution authority or make foreground mode behavior diverge.; T19.1.2: Lease loss without commit fencing permits duplicate or stale processes to advance authoritative state.; T19.1.3: Multiple client paths can recreate alternate state mutation logic or silently change CLI behavior. |
| E20 — Canonical status, telemetry, health, and diagnostics | 0 | 4 | 0 | 0 | 56 | T20.1.1: Observability can become a data-exfiltration path or a second inconsistent account of lifecycle truth.; T20.1.2: Unbounded telemetry labels can exhaust memory/storage and leak artifact identity.; T20.1.3: A convenience status cache can become an alternate authority or hide missing provenance behind optimistic defaults. |
| E21 — Versioned external command and event adapters | 0 | 0 | 4 | 0 | 60 | T21.1.1: Transport-specific schemas can smuggle alternate state mutation or drift from CLI/Python semantics.; T21.1.2: A network API can accidentally become a second coordinator or expose unsafe local assumptions.; T21.1.3: Treating the broker as authoritative can lose transitions, block local execution, or let event consumers mutate state. |
| E22 — Subprocess plugin isolation and enforceable resource controls | 0 | 0 | 4 | 0 | 62 | T22.1.1: A loose IPC contract can expose internal authority or permit malformed plugin output to mutate state.; T22.1.2: A timed-out parent may leave descendants running or a restart may kill an unrelated reused PID.; T22.1.3: Cross-platform resource controls are uneven, creating false isolation claims or escape through tools/network/secrets. |
| E23 — Retention, compatibility, plugin SDK, and source-provider evolution | 0 | 0 | 4 | 0 | 58 | T23.1.1: Cleanup can irreversibly destroy provenance, recovery data, or published-content lineage.; T23.1.2: Scattered version checks create ambiguous behavior, silent data loss, and unsafe downgrade paths.; T23.1.3: A difficult SDK encourages plugins to depend on private internals, weakening compatibility and authority boundaries. |
| E24 — Continuous quality, packaging, benchmarks, and release evidence | 0 | 4 | 0 | 0 | 62 | T24.1.1: An undefined support matrix can turn skipped platform controls into misleading release claims.; T24.1.2: Passing unit tests can mask transition, recovery, parser, concurrency, and migration failures that only appear under faults.; T24.1.3: A green source test suite does not prove that the shipped wheel is complete, reproducible, untampered, or license-compliant. |
| E25 — Measured optional PostgreSQL and object-storage adapters | 0 | 0 | 0 | 4 | 58 | T25.1.1: Premature infrastructure can increase failure surface and operations without solving the measured bottleneck.; T25.1.2: Adapter abstractions can hide weaker consistency or enable simultaneous writable backends.; T25.1.3: Database semantics, failover, and connection behavior can subtly change transition atomicity and recovery. |
| E26 — Optional remote worker execution | 0 | 0 | 0 | 4 | 64 | T26.1.1: A remote protocol can accidentally make workers authorities or accept stale/forged results across versions.; T26.1.2: Workers may accumulate broad credentials, stale authority, or unverifiable cached/content outputs.; T26.1.3: Reassignment or fallback after worker uncertainty can duplicate effects or downgrade isolation. |
| E27 — Bounded MCP and operator interfaces | 0 | 0 | 0 | 4 | 60 | T27.1.1: Agent interfaces are vulnerable to prompt injection and excessive agency if artifact content can drive tools or mutations.; T27.1.2: Adding mutation tools can make the model an implicit authority or confused deputy.; T27.1.3: A UI can mislead operators by presenting inferred or pending information as trusted success and can render untrusted content. |

## Domain Registry

* `{EVIDENCE}` — Evidence and authority: Baselines, repository facts, document requirements, assumptions, conflicts, and completion evidence.
* `{ARCHITECTURE}` — Architecture: Component ownership, semantic boundaries, composition, and deliberately rejected complexity.
* `{CONFIGURATION}` — Configuration: Typed versioned configuration, deterministic loading, migration, and safe defaults.
* `{PERSISTENCE}` — Persistence: StateStore contracts, transactions, schemas, migrations, integrity, backup, and recovery.
* `{LIFECYCLE}` — Lifecycle: Jobs, phases, attempts, work items, controls, transitions, fencing, and phase barriers.
* `{INTAKE}` — Intake and sources: Source registration, immutable generations, occurrences, mutation detection, and source providers.
* `{IDENTITY}` — Content identity: Canonical byte identity, hashing, occurrence linkage, deduplication, and verification.
* `{EVENTS}` — Events: Durable history, transactional outbox, transport adapters, replay, sequencing, and notifications.
* `{SAFETY}` — Filesystem and archive safety: Path policy, quarantine, structural inspection, materialization, archive limits, and containment.
* `{STORAGE}` — Artifact storage: Managed content, workspaces, blobs, references, integrity, quotas, and retention.
* `{PROVENANCE}` — Provenance and lineage: Source-to-byte-to-derived-to-evidence-to-publication traceability and immutable records.
* `{PLUGINS}` — Plugins and capabilities: Typed extension contracts, registries, descriptors, trust policy, and compatibility.
* `{EXECUTION}` — Execution: In-process, subprocess, work-item, resource, and optional remote execution contracts.
* `{REVIEW}` — Evidence, review, and publication: Findings, evidence, decisions, policy, publication, verification, and authority.
* `{RECOVERY}` — Failure and recovery: Retries, timeouts, checkpoints, idempotency, reconciliation, crash/restart, and rollback.
* `{OBSERVABILITY}` — Observability: Structured logs, metrics, traces, status, health, readiness, and diagnostics.
* `{API}` — Interfaces: CLI, Python, REST, RabbitMQ, webhooks, MCP, UI, contracts, and adapters.
* `{SECURITY}` — Security and governance: Trust boundaries, authorization, capability restriction, hostile input, auditing, and fail-closed behavior.
* `{PERFORMANCE}` — Performance and scale evidence: Workloads, resource accounting, benchmarks, contention, reuse, and trigger evidence.
* `{COMPATIBILITY}` — Versioning and compatibility: Schema/API/plugin/config/checkpoint compatibility, translators, deprecation, and migration.
* `{RELEASE}` — Testing and release: CI gates, test architecture, packaging, SBOM, provenance, release evidence, and rollback.
* `{OPERATIONS}` — Operations: Daemon/worker lifecycle, runbooks, backup, health, cleanup, incidents, and operator workflows.
* `{DX}` — Developer experience: SDKs, examples, documentation, diagnostics, accessibility, and supported public surfaces.
* `{SCALE}` — Optional scale adapters: PostgreSQL, object storage, remote workers, tenant/deployment scale, and evidence-based adoption.

## E1. Evidence, baseline, and authority reconciliation

Replace the prior assessment limitations with a reproducible implementation baseline while preserving the supplied ZIP as the canonical planning truth.

* [ ] - T1.1.1 Freeze the active ATLAS ref and repository authority map
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVIDENCE} {ARCHITECTURE} {RELEASE}
  * Dependencies: None
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4; PDF:p.1-34
  * Acceptance Criteria: 1) The baseline record contains the exact current SHA, branch, dirty-state summary, repository inventory hash, and source-package hash.; 2) Every ZIP-cited ATLAS path/symbol is classified as present, moved, replaced, removed, or unverified.; 3) A command matrix identifies the exact repository-native validation commands, working directory, prerequisites, and expected result class.; 4) No production source file is modified.
  * Steps / Subtasks:
    * Record default branch, exact commit SHA, dirty state, submodules, generated/vendor boundaries, package/toolchain versions, and supported targets.
    * Run a deterministic secret-safe repository inventory and map every path/symbol cited by the latest ZIP to present or missing state.
    * Extract authoritative build, lint, type, test, migration, packaging, and release commands from manifests and CI.
    * Publish an evidence delta showing unchanged, moved, replaced, newly implemented, and unresolved surfaces relative to `efa547cafc64b58d60d19dcc1e5ba32c6b046bc5`.
  * Risks & Mitigations: Implementing against a stale or mislocated repository surface could invalidate every downstream TODO. / Block product implementation until the baseline and command matrix are reviewed and hashed..
  * Tags: [baseline] [authority] [read-only] [p0]

* [ ] - T1.1.2 Revalidate all product-direction requirements against the attached PDF
  * Priority: `P0`
  * Est. Effort: `8h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVIDENCE} {ARCHITECTURE} {PROVENANCE}
  * Dependencies: None
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4; PDF:p.1-34
  * Acceptance Criteria: 1) All 30 requirements have a verified page range, status, mapped production task IDs, and an ambiguity field.; 2) The end-state and lifecycle diagrams are summarized without contradicting the attached visuals.; 3) The previous `PDF not independently accessible` limitation is explicitly closed for this planning run.; 4) No PDF statement is promoted to current implementation fact.
  * Steps / Subtasks:
    * Verify the document page count, metadata availability, repository baseline, and the six-stage lifecycle wording.
    * Recheck REQ-001 through REQ-030 against the cited pages and record explicit versus inferred status without strengthening ambiguous language.
    * Inspect the lifecycle, end-state, and lineage visuals on pages 21, 29, and 31 and reconcile them with the prose on pages 16, 22, 27, and 28.
    * Update the production task crosswalk so every requirement maps to at least one implementation or explicit defer/reject task.
  * Risks & Mitigations: A transcription or diagram-reading error could drive the production backlog away from the intended product. / Retain page-specific evidence, rendered screenshots, and ambiguity notes; require reviewer sign-off..
  * Tags: [pdf] [requirements] [evidence] [p0]

* [ ] - T1.1.3 Restore and revalidate the Yggdrasil donor baseline and license provenance
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVIDENCE} {ARCHITECTURE} {SECURITY} {COMPATIBILITY}
  * Dependencies: None
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4; PDF:p.1-34
  * Acceptance Criteria: 1) Every donor integration row has a verified path/symbol, commit, dependency set, license note, and final disposition.; 2) Tests worth porting are named with the ATLAS invariant they prove.; 3) No donor mechanism is designated `REUSE` without an exact source and compatibility assessment.; 4) Unavailable evidence remains `UNRESOLVED` and blocks code transplantation.
  * Steps / Subtasks:
    * Obtain an archive or checkout of the exact frozen donor commit and verify its tree hash and default branch history.
    * Read every donor path/symbol cited by the ZIP, including registry, store, content models, release filesystem, staging, and executor code.
    * Map transitive dependencies, platform assumptions, data contracts, migrations, test fixtures, and license obligations.
    * Revise donor dispositions only where primary source changes the latest package's conclusion; never copy wholesale.
  * Risks & Mitigations: Unverified donor transplantation could import hidden dependencies, governance coupling, platform races, or license obligations. / Default to REIMPLEMENT from documented invariants until exact source and tests are restored..
  * Tags: [donor] [license] [provenance] [p0]

* [ ] - T1.1.4 Publish the canonical component-ownership and scope boundary matrix
  * Priority: `P0`
  * Est. Effort: `10h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {ARCHITECTURE} {EVIDENCE} {SECURITY} {COMPATIBILITY}
  * Dependencies: T1.1.1, T1.1.2, T1.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4; PDF:p.1-34
  * Acceptance Criteria: 1) Every authoritative record and transition has exactly one named owner.; 2) All helper candidates are classified with rationale and mapped to a task or explicit rejection.; 3) The matrix preserves fixed A-F barriers and separates mechanism from deployment policy.; 4) The matrix is reviewed before module creation begins.
  * Steps / Subtasks:
    * Classify every candidate helper as REQUIRED CORE, USEFUL CORE, ADAPTER, PLUGIN, LATER, or UNNECESSARY.
    * Map one authoritative owner for job, phase, attempt, intake, occurrence, content, structure, extraction, finding, evidence, decision, publication, checkpoint, event history, transport, budget, and configuration state.
    * Combine cohesive responsibilities such as quarantine into WorkspaceManager and fencing into StateStore/LifecycleCoordinator rather than creating micro-services.
    * Record explicit non-goals: no generic DAG, no alternate lifecycle authority, no mandatory distributed infrastructure, and no model-owned trust transition.
  * Risks & Mitigations: Adding every suggested helper as a separate service would increase coupling and obscure authority rather than improve it. / Require an invariant and independent failure boundary for every component; merge or reject the rest..
  * Tags: [architecture] [ownership] [scope] [p0]

## E2. Deterministic current-behavior characterization

Create executable evidence for every consequential current defect and compatibility surface before production behavior changes.

* [ ] - T2.1.1 Define the versioned characterization fixture manifest
  * Priority: `P0`
  * Est. Effort: `8h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVIDENCE} {RELEASE} {SECURITY}
  * Dependencies: T1.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]; Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14
  * Acceptance Criteria: 1) The manifest schema validates all baseline fixtures and rejects missing GAP/REQ lineage.; 2) Every GAP-001 through GAP-015 has a fixture or an explicit investigation record.; 3) All fixture inputs are sanitized, bounded, and self-contained.; 4) Expectation-change policy requires linked correction task and reviewer approval.
  * Steps / Subtasks:
    * Define fixture fields for source setup, invocation surface, expected current result, expected target result, database assertions, event assertions, filesystem manifest, cleanup, platform capabilities, and related GAP/REQ IDs.
    * Normalize timestamps, temporary roots, UUIDs, and platform-specific metadata without erasing behaviorally significant differences.
    * Create initial fixture metadata for every GAP-001 through GAP-015, marking unresolved runtime evidence explicitly.
    * Document fixture provenance and rules for changing a characterization expectation.
  * Risks & Mitigations: A weak fixture contract could preserve accidental nondeterminism or hide the exact defect later corrections must prove. / Version the schema, retain raw evidence, and require explicit defect/target labels..
  * Tags: [tests] [fixtures] [characterization] [p0]

* [ ] - T2.1.2 Characterize CLI, API, persistence, event, and filesystem outcomes
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVIDENCE} {LIFECYCLE} {PERSISTENCE} {EVENTS}
  * Dependencies: T2.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]; Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14
  * Acceptance Criteria: 1) Every selected scenario records a complete, canonical evidence bundle.; 2) CLI and Python invocation paths are compared for equivalent authoritative outcomes.; 3) Three clean runs yield identical normalized evidence hashes.; 4) No production source behavior changes are included.
  * Steps / Subtasks:
    * Exercise missing, non-directory, unreadable, and empty sources through CLI and Python API.
    * Exercise invalid phase permutations, contradictory error flags, missing handlers, and failed phases under non-abort behavior.
    * Capture job/phase state, database rows, emitted events, exception classes, CLI status, and filesystem side effects for each case.
    * Run each case three times and compare normalized evidence hashes.
  * Risks & Mitigations: Characterizing only unit seams could miss false success and drift at public interfaces. / Drive scenarios through CLI/Python boundaries and retain all authoritative outputs..
  * Tags: [cli] [api] [state] [characterization] [p0]

* [ ] - T2.1.3 Add adversarial source, archive, analyzer, and control baselines
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SECURITY} {SAFETY} {INTAKE} {PLUGINS} {RECOVERY}
  * Dependencies: T2.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]; Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14
  * Acceptance Criteria: 1) Every high-risk path has a reproducible current-state outcome or explicit capability-limited investigation.; 2) The >50 finding case proves whether authoritative data is truncated or only summarized.; 3) Source mutation and second-process control behavior are recorded with exact state/effect boundaries.; 4) All adversarial fixtures stay within declared byte, time, and file-count limits.
  * Steps / Subtasks:
    * Create source-mutation cases between Reconnaissance and Fingerprinting, including replacement, rename, truncation, and symlink swap where supported.
    * Create archive fixtures for traversal, absolute names, links, devices, nested depth, compression ratio, declared/actual byte mismatch, and partial extraction.
    * Create analyzer fixtures emitting 0, 1, 50, 51, conflicting, malformed, and oversized findings.
    * Characterize pause/resume/cancel from the owning process and from a second process, plus event-store full/failure behavior.
  * Risks & Mitigations: Timing-only or unbounded adversarial tests can be flaky, unsafe, or misleading. / Use deterministic barriers, inert fixtures, explicit budgets, and capability-gated skips..
  * Tags: [adversarial] [archive] [toctou] [controls] [p0]

* [ ] - T2.1.4 Integrate characterization evidence into CI and correction gates
  * Priority: `P0`
  * Est. Effort: `10h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RELEASE} {EVIDENCE} {COMPATIBILITY}
  * Dependencies: T2.1.2, T2.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]; Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14
  * Acceptance Criteria: 1) Characterization jobs are mandatory for P0 changes and fail on unapproved skips.; 2) Failure artifacts include all required evidence without secrets or unbounded payloads.; 3) Every expectation change links to its implementation task and reviewer decision.; 4) Three-run determinism is checked in CI or an equivalent reproducible gate.
  * Steps / Subtasks:
    * Add CI jobs for characterization, deterministic reruns, artifact retention, and platform capability reporting.
    * Require each P0 implementation PR to reference the failing/current fixture and update only its target expectation after the correction lands.
    * Publish JUnit/JSON reports, normalized event traces, database snapshots, and filesystem manifests on failure.
    * Add a gate that rejects vacuous assertions, unapproved skips, or fixtures lacking cleanup/provenance metadata.
  * Risks & Mitigations: A passive characterization suite could drift or be bypassed during refactoring. / Make it a mandatory CI gate with change lineage and retained evidence..
  * Tags: [ci] [quality-gate] [evidence] [p0]

## E3. Versioned pipeline semantics and configuration

Make the six lifecycle slots, failure policy, typed phase configuration, and canonical configuration digest one deterministic contract across CLI, Python, tests, and future services.

* [ ] - T3.1.1 Define `PipelineDefinitionV1`, canonical phase slots, and one failure policy
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {CONFIGURATION} {LIFECYCLE} {COMPATIBILITY}
  * Dependencies: T2.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]; Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34; ADR-001,ADR-007
  * Acceptance Criteria: 1) Every accepted definition contains A-F exactly once in canonical order.; 2) Contradictory legacy failure flags are rejected before job creation.; 3) Disabled phases produce an explicit policy and eventual durable `SKIPPED` reason.; 4) The JSON schema and Python model agree on all required fields and enums.
  * Steps / Subtasks:
    * Model schema version, pipeline name, source reference, metadata, six named phase policies, and one `FailurePolicy`.
    * Represent disabled or inapplicable work as validated phase policy that yields durable `SKIPPED`, never by deleting or reordering a slot.
    * Define required/optional semantics and legal failure propagation for each phase slot.
    * Publish canonical JSON schema and examples for valid, invalid, skipped, and optional-phase pipelines.
  * Risks & Mitigations: A permissive model could continue to allow caller-controlled lifecycle order under a new name. / Encode A-F as named slots and exhaustively test invalid permutations..
  * Tags: [configuration] [lifecycle] [schema] [p0]

* [ ] - T3.1.2 Implement deterministic safe loading, merge order, and canonical digests
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {CONFIGURATION} {SECURITY} {COMPATIBILITY}
  * Dependencies: T3.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]; Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34; ADR-001,ADR-007
  * Acceptance Criteria: 1) Equivalent normalized configurations produce identical digests across runs.; 2) Every accepted phase key is consumed by a typed model.; 3) Invalid configuration creates no job row, workspace, or outbox event.; 4) Diagnostics identify source path, key, expected type, and stable error code without exposing secrets.
  * Steps / Subtasks:
    * Use a safe loader with duplicate-key rejection, bounded aliases, and source-location diagnostics.
    * Define merge precedence for defaults, file, environment, and explicit CLI values; reject ambiguous or wrong-typed overrides.
    * Validate every phase-specific field against a consumer-owned typed model and reject accepted-but-unused keys.
    * Canonicalize normalized data, redact/resolve secret references, and compute a stable digest persisted with the job.
  * Risks & Mitigations: Configuration merge or hashing drift could make replay, compatibility, and policy enforcement non-reproducible. / Centralize resolution and canonicalization, then test equivalent inputs and secret handling..
  * Tags: [loader] [digest] [yaml] [p0]

* [ ] - T3.1.3 Create typed configuration contracts for all six built-in phases
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {CONFIGURATION} {PLUGINS} {SAFETY}
  * Dependencies: T3.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]; Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34; ADR-001,ADR-007
  * Acceptance Criteria: 1) Every built-in phase receives only its typed configuration object.; 2) No production phase reads raw `phase_config` dictionaries after migration.; 3) Unsupported capability or platform combinations fail before attempt creation.; 4) Config schema round-trips preserve semantics and digest.
  * Steps / Subtasks:
    * Define Recon traversal depth/exclusions/budgets; Fingerprint algorithms/chunk/capture mode; Structure inspectors/budgets; Extraction policy/workspace limits; Analysis plugin selection/resources; Review/publication policy references.
    * Assign one owner and default rationale to every field and mark deployment-policy fields separately from mechanism fields.
    * Reject fields unsupported by the selected platform, plugin, or backend before execution.
    * Expose versioned serialization and upgrade hooks for each phase config.
  * Risks & Mitigations: Hidden dictionary contracts could survive inside handlers and continue to drift from schema and documentation. / Require typed context injection and consumer-coverage tests..
  * Tags: [typed-config] [phases] [contracts] [p0]

* [ ] - T3.1.4 Add legacy pipeline migration, dual support, and deprecation telemetry
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {COMPATIBILITY} {CONFIGURATION} {OBSERVABILITY}
  * Dependencies: T3.1.2, T3.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]; Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34; ADR-001,ADR-007
  * Acceptance Criteria: 1) All existing examples either migrate to an approved digest or fail with a documented reason.; 2) Legacy and migrated definitions produce equivalent intended lifecycle behavior for supported cases.; 3) Deprecation telemetry reports use without logging sensitive configuration.; 4) Removal criteria and compatibility window are documented and testable.
  * Steps / Subtasks:
    * Inventory legacy keys, examples, CLI arguments, public imports, and conflicting error-policy combinations.
    * Implement read-old/write-new normalization with warnings and a deterministic converted definition.
    * Provide a dry-run migration command that emits a diff, target digest, unsupported keys, and rollback instructions.
    * Add deprecation counters/events and a version-detection matrix; do not remove legacy support until usage and tests permit.
  * Risks & Mitigations: A flag-day configuration rewrite could break users or silently alter failure semantics. / Use introduce-dual-support-migrate-verify-deprecate-remove with explicit unsupported cases..
  * Tags: [migration] [legacy] [deprecation] [p0]

## E4. StateStore and SQLite migration foundation

Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.

* [ ] - T4.1.1 Define the narrow `StateStore` transaction and repository contracts
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PERSISTENCE} {ARCHITECTURE} {SECURITY}
  * Dependencies: T2.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]; Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15; ADR-002,ADR-003; R-02
  * Acceptance Criteria: 1) No authoritative repository method commits outside a `StateStore` transaction.; 2) `JobStore` compatibility calls delegate without changing public results.; 3) The error taxonomy distinguishes contention, corruption, schema mismatch, constraint, cancellation, and storage exhaustion.; 4) A backend conformance test skeleton covers transaction atomicity and rollback.
  * Steps / Subtasks:
    * Define async transaction context, read/write repository interfaces, isolation expectations, commit/rollback ownership, and nested-transaction prohibition or savepoint rules.
    * Separate repositories for jobs, phase runs, attempts, events, controls, checkpoints, artifacts, and later records without exposing raw connections.
    * Define stable persistence error codes and retryability hints without making retry decisions inside the store.
    * Create a backend conformance contract that SQLite and future PostgreSQL must satisfy.
  * Risks & Mitigations: An overly broad abstraction or hidden direct commits would preserve inconsistent transaction ownership. / Keep the protocol narrow, ban raw connection access outside persistence, and enforce conformance tests..
  * Tags: [persistence] [transactions] [state-store] [p0]

* [ ] - T4.1.2 Implement the SQLite backend with explicit connection and locking policy
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PERSISTENCE} {RECOVERY} {OBSERVABILITY}
  * Dependencies: T4.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]; Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15; ADR-002,ADR-003; R-02
  * Acceptance Criteria: 1) Foreign keys and uniqueness constraints are enabled and demonstrated.; 2) Contention yields bounded, classified behavior with lock-wait metrics.; 3) All existing job/phase persistence tests pass through the new backend.; 4) Startup reports actual SQLite capabilities and refuses unsafe/unsupported state.
  * Steps / Subtasks:
    * Configure and verify foreign keys, journal mode, synchronous level, busy timeout, row factory, and connection ownership at startup.
    * Use explicit transaction modes for read and write paths and document lock acquisition order.
    * Implement bounded contention retry signaling without hidden infinite loops.
    * Expose integrity, schema, lock-wait, file-permission, and capacity health information.
  * Risks & Mitigations: Incorrect locking or pragma assumptions can produce stalls, lost updates, or false readiness. / Verify actual pragmas, bound contention, and test process/disk faults..
  * Tags: [sqlite] [locking] [persistence] [p0]

* [ ] - T4.1.3 Create immutable numbered migrations and the v0.1 upgrade path
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PERSISTENCE} {COMPATIBILITY} {RECOVERY}
  * Dependencies: T4.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]; Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15; ADR-002,ADR-003; R-02
  * Acceptance Criteria: 1) Fresh and upgraded databases have identical schema fingerprints and invariants.; 2) Migration checksums are immutable and verified on every startup.; 3) Newer unsupported schema and checksum drift fail with stable diagnostics.; 4) Every migration has forward test fixtures and a documented restore-based rollback.
  * Steps / Subtasks:
    * Define migration discovery, ordering, checksums, schema metadata, supported version range, and no-edit rule for applied migrations.
    * Write the initial baseline and v0.1-to-target migrations for existing jobs, phases, selected events, and required constraints.
    * Compute a canonical schema fingerprint and verify fresh versus upgraded convergence.
    * Record migration events only after successful schema/data verification.
  * Risks & Mitigations: A migration defect could irreversibly damage the only authoritative job database. / Use verified backup, immutable migrations, transactional transforms, and restore-based rollback..
  * Tags: [migrations] [schema] [upgrade] [p0]

* [ ] - T4.1.4 Implement verified backup, restore, integrity, and migration recovery
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PERSISTENCE} {RECOVERY} {OPERATIONS}
  * Dependencies: T4.1.2, T4.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]; Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15; ADR-002,ADR-003; R-02
  * Acceptance Criteria: 1) A verified pre-migration backup exists before any schema change.; 2) Restore drills reproduce schema and row fingerprints in a separate location.; 3) Migration failure leaves the original database and backup usable.; 4) Operator diagnostics identify exact failure stage, artifact hashes, and safe next action.
  * Steps / Subtasks:
    * Before migration, run integrity/foreign-key checks, capture schema/row fingerprints, create a verified backup, and confirm free-space requirements.
    * After migration, verify schema fingerprint, row counts, referential invariants, and representative deserialization.
    * Implement restore verification into a separate path before any destructive replacement.
    * Detect partial migration markers, stale backups, orphan temporary files, and incompatible binary/schema combinations.
  * Risks & Mitigations: A migration can be technically correct but operationally unrecoverable if backup and restore are unverified. / Require independent restore verification and deterministic fault drills before release..
  * Tags: [backup] [restore] [integrity] [p0]

## E5. Explicit lifecycle state machines, attempts, and fencing

Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.

* [ ] - T5.1.1 Specify exhaustive job, phase, attempt, and control state tables
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {LIFECYCLE} {ARCHITECTURE} {RECOVERY}
  * Dependencies: T3.1.4, T4.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.; Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15; ADR-011; R-11
  * Acceptance Criteria: 1) Transition tables are exhaustive and machine-readable.; 2) Every state has one owner, legal predecessors/successors, and terminal semantics.; 3) Invalid legacy combinations have an explicit migration or blocked-state rule.; 4) The tables map to PDF lifecycle semantics without creating DAG behavior.
  * Steps / Subtasks:
    * Define job, phase-run, attempt, and control-request states with one meaning per state.
    * Enumerate every legal transition with actor, preconditions, required evidence, emitted event, and terminal behavior.
    * Define propagation from attempt outcome to phase and job, including optional/skipped/blocked/degraded distinctions.
    * Define restart and replay decisions without implying side-effect safety not yet proven.
  * Risks & Mitigations: Ambiguous states would make retries, controls, and recovery nondeterministic even with durable persistence. / Specify the complete transition system and review it before mutation code..
  * Tags: [state-machine] [attempts] [controls] [p0]

* [ ] - T5.1.2 Persist immutable phase runs and execution attempts
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {LIFECYCLE} {PERSISTENCE} {PROVENANCE}
  * Dependencies: T5.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.; Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15; ADR-011; R-11
  * Acceptance Criteria: 1) Every execution is represented by exactly one immutable attempt record.; 2) Duplicate concurrent attempt creation is rejected by transaction and uniqueness guards.; 3) Legacy phase status remains available as a derived compatibility projection.; 4) Attempt rows link to exact input/config/policy and later result/checkpoint evidence.
  * Steps / Subtasks:
    * Add phase-run and attempt identifiers, ordinal, backend/plugin identity, fencing token, start/end, outcome, error class, checkpoint, work/result digest, and predecessor/successor links.
    * Create an attempt only after transition guards and required inputs are durably verified.
    * Append outcomes and evidence without mutating completed attempt identity.
    * Project legacy phase fields from canonical records during the compatibility window.
  * Risks & Mitigations: Mutable or duplicate attempt records could conceal repeated execution and side effects. / Use append-oriented attempt records, guarded creation, and unique ordinals/fencing..
  * Tags: [attempts] [persistence] [lineage] [p0]

* [ ] - T5.1.3 Implement guarded atomic transitions and fencing tokens
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {LIFECYCLE} {PERSISTENCE} {SECURITY}
  * Dependencies: T5.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.; Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15; ADR-011; R-11
  * Acceptance Criteria: 1) Every transition requires the expected current state/version and fails deterministically when stale.; 2) Stale fencing tokens cannot commit result or terminal state.; 3) Concurrent transition tests produce one winner and auditable losers.; 4) No production code mutates lifecycle status fields outside the coordinator/repository path.
  * Steps / Subtasks:
    * Implement transition commands with expected state/version, actor, reason, correlation, and required evidence references.
    * Issue monotonically changing fencing tokens or equivalent lease epochs when execution authority changes.
    * Atomically update canonical state and transition sequence; event atomicity is completed in E8.
    * Reject stale, duplicate, out-of-order, or unauthorized transition requests with stable reason codes.
  * Risks & Mitigations: A stale owner or duplicate request could commit a second side effect or overwrite terminal truth. / Use compare-and-set transitions and fencing on every authoritative result..
  * Tags: [guards] [fencing] [atomicity] [p0]

* [ ] - T5.1.4 Add model-based state-machine and invalid-transition verification
  * Priority: `P0`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {LIFECYCLE} {RELEASE} {RECOVERY}
  * Dependencies: T5.1.2, T5.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.; Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15; ADR-011; R-11
  * Acceptance Criteria: 1) Model and implementation agree across the declared generated sequence budget.; 2) Every illegal transition class has a stable error code and zero authoritative mutation.; 3) Counterexamples are reproducible and retained.; 4) State-machine tests run in mandatory CI without unapproved skips.
  * Steps / Subtasks:
    * Build a reference model for job, phase, attempt, and control transitions.
    * Generate valid and invalid command sequences, compare implementation state to the model, and minimize failures.
    * Inject cancellation, process loss, duplicate commands, stale results, and storage faults at transition boundaries.
    * Retain counterexample sequences and transition histories as regression fixtures.
  * Risks & Mitigations: Hand-authored tests can miss transition combinations that later cause irrecoverable state divergence. / Use a reference model, generated sequences, and retained minimized failures..
  * Tags: [property-testing] [state-machine] [verification] [p0]

## E6. Registered sources and immutable intake generations

Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.

* [ ] - T6.1.1 Define `SourceRoot`, `IntakeGeneration`, and `ArtifactOccurrence` schemas
  * Priority: `P0`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {INTAKE} {PROVENANCE} {PERSISTENCE}
  * Dependencies: T4.1.4, T5.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]; Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31; ADR-013; GAP-001,GAP-004
  * Acceptance Criteria: 1) Occurrence and content concepts remain structurally distinct.; 2) Every occurrence belongs to exactly one generation and one source root.; 3) Accepted generation records are immutable and supersession is explicit.; 4) Schema supports local filesystem now without claiming unsupported provider semantics.
  * Steps / Subtasks:
    * Define stable IDs, provider type, normalized locator, allowed-root policy, generation state, manifest digest, traversal policy digest, and timestamps.
    * Define occurrence relative path, entry type, size, mode, timestamps, device/inode where available, link/special status, exclusion/error reason, and observation sequence.
    * Define uniqueness, foreign keys, immutability, and supersession relationships.
    * Publish serialization/schema versions and authority classification for each field.
  * Risks & Mitigations: Conflating source roots, observations, and paths would make provenance and mutation detection impossible to reason about. / Use separate records and explicit provider/capability fields..
  * Tags: [intake] [models] [occurrence] [p0]

* [ ] - T6.1.2 Implement bounded deterministic intake traversal
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {INTAKE} {SAFETY} {PERFORMANCE}
  * Dependencies: T6.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]; Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31; ADR-013; GAP-001,GAP-004
  * Acceptance Criteria: 1) Traversal order and accepted manifest input are deterministic for a stable source.; 2) Every skipped/error entry has a persisted reason and no silent omission.; 3) Budget exhaustion yields BLOCKED or FAILED, not ACCEPTED.; 4) Memory use is bounded independently of total entry count.
  * Steps / Subtasks:
    * Resolve a registered root, snapshot policy/capabilities, create a BUILDING generation, and enumerate entries in deterministic relative-path order.
    * Persist occurrence candidates incrementally with traversal sequence, exclusion/error reason, and resource counters.
    * Enforce entry, depth, byte-metadata, elapsed-time, and error-policy budgets without unbounded memory.
    * Checkpoint traversal position only where deterministic resume can be proven.
  * Risks & Mitigations: A partial or nondeterministic traversal could become a falsely authoritative intake manifest. / Persist explicit outcomes, enforce budgets, and accept only after completeness checks..
  * Tags: [traversal] [determinism] [budgets] [p0]

* [ ] - T6.1.3 Implement generation acceptance, manifest digests, and supersession
  * Priority: `P0`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {INTAKE} {PROVENANCE} {EVENTS}
  * Dependencies: T6.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]; Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31; ADR-013; GAP-001,GAP-004
  * Acceptance Criteria: 1) Only complete generations reach ACCEPTED.; 2) Equivalent stable observations yield the same manifest digest.; 3) Duplicate acceptance is idempotent and conflicting acceptance fails.; 4) Supersession preserves both generations and lineage.
  * Steps / Subtasks:
    * Compute a canonical manifest over ordered occurrence records and policy/config versions.
    * Validate traversal completeness, unresolved errors, budgets, source guard, and required entry classes before acceptance.
    * Atomically transition BUILDING to ACCEPTED/FAILED/BLOCKED with reason and durable event hook.
    * Create explicit superseding generation relationships when a new observation is requested.
  * Risks & Mitigations: Acceptance without a deterministic completeness barrier would make downstream identity and safety claims untrustworthy. / Use atomic guarded acceptance and immutable manifests..
  * Tags: [manifest] [acceptance] [provenance] [p0]

* [ ] - T6.1.4 Make all downstream phases consume accepted occurrence IDs only
  * Priority: `P0`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {INTAKE} {LIFECYCLE} {SECURITY}
  * Dependencies: T6.1.2, T6.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]; Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31; ADR-013; GAP-001,GAP-004
  * Acceptance Criteria: 1) Static/runtime guards find no unauthorized downstream source enumeration.; 2) Fingerprinting consumes exactly the accepted occurrence set.; 3) Deleted/mutated occurrences produce deterministic stale/missing outcomes.; 4) Compatibility behavior is documented and time-bounded.
  * Steps / Subtasks:
    * Change phase inputs to `intake_generation_id` and occurrence/content references.
    * Add guards that reject non-ACCEPTED generations, foreign-job occurrences, stale/superseded generations, and arbitrary absolute paths.
    * Remove or isolate legacy re-traversal behavior behind a temporary compatibility test-only adapter.
    * Add source-mutation tests proving downstream phases do not silently substitute a new occurrence set.
  * Risks & Mitigations: Leaving one phase on live rediscovery would preserve the central TOCTOU and provenance defect. / Make occurrence IDs mandatory and guard direct traversal..
  * Tags: [phase-inputs] [immutable-intake] [toctou] [p0]

## E7. Persistent content identity and occurrence linkage

Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.

* [ ] - T7.1.1 Define `ContentIdentity` and occurrence-to-content link contracts
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {IDENTITY} {PROVENANCE} {PERSISTENCE}
  * Dependencies: T6.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]; Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31; ADR-005,ADR-006; GAP-004,GAP-005
  * Acceptance Criteria: 1) Identical bytes converge on one persistent SHA-256 identity across processes.; 2) All occurrences remain independently traceable to the shared identity.; 3) Identity records do not falsely claim retained bytes.; 4) Malformed or conflicting digest records fail integrity checks.
  * Steps / Subtasks:
    * Define canonical `sha256:<hex>` identity, byte count, optional secondary hash, first/last verification, and integrity status.
    * Define occurrence link fields for read start/end metadata, mutation result, capture status, config/algorithm version, and attempt.
    * Enforce many occurrences to one identity, one successful identity per occurrence/read attempt, and immutable digest values.
    * Separate identity existence from blob retention and replayability.
  * Risks & Mitigations: Treating identity and storage as the same concept would create false replayability and break provenance. / Persist independent identity and retention fields with strict invariants..
  * Tags: [sha256] [identity] [provenance] [p0]

* [ ] - T7.1.2 Implement race-aware streaming hashing from accepted occurrences
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {IDENTITY} {SECURITY} {PERFORMANCE}
  * Dependencies: T7.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]; Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31; ADR-005,ADR-006; GAP-004,GAP-005
  * Acceptance Criteria: 1) Stable inputs produce the expected SHA-256 and link evidence.; 2) Mutation cannot attach the wrong identity to an occurrence.; 3) Partial or indeterminate reads never appear successful.; 4) Progress remains bounded and durable through the PhaseContext contract.
  * Steps / Subtasks:
    * Resolve occurrence through SourceAccess, open no-follow/handle-relative where available, and compare pre-read handle metadata to the occurrence record.
    * Stream SHA-256 in bounded chunks while recording bytes read, progress, and optional capture sink.
    * Recheck handle/path-relevant metadata after read and classify stable, stale, disappeared, or indeterminate.
    * Persist identity and occurrence link atomically only when read evidence satisfies policy.
  * Risks & Mitigations: A path-based or single-stat hash read can bind new bytes to an old occurrence after source mutation. / Verify the opened handle before and after streaming and fail closed on drift..
  * Tags: [hashing] [toctou] [streaming] [p0]

* [ ] - T7.1.3 Add persistent cross-run duplicate lookup and processing-reuse eligibility
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {IDENTITY} {PROVENANCE} {PERFORMANCE}
  * Dependencies: T7.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]; Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31; ADR-005,ADR-006; GAP-004,GAP-005
  * Acceptance Criteria: 1) A restart recognizes previously seen content without recomputing downstream identity state.; 2) Every duplicate occurrence is persisted and queryable.; 3) Reuse eligibility is false unless exact downstream keys and integrity requirements are satisfied.; 4) High-occurrence queries remain bounded and indexed.
  * Steps / Subtasks:
    * Create indexed lookup by canonical digest and size with integrity verification.
    * Return prior occurrence count, retention/replayability state, and compatible downstream result candidates without auto-reusing them.
    * Record every new occurrence even when content is already known.
    * Expose a deterministic eligibility signal consumed later by the result-reuse service.
  * Risks & Mitigations: Naive deduplication could skip required work or lose occurrence provenance. / Separate duplicate recognition from exact-key result reuse and persist every occurrence..
  * Tags: [dedup] [reuse] [queries] [p0]

* [ ] - T7.1.4 Preserve `HashStore` compatibility while removing process-local authority
  * Priority: `P0`
  * Est. Effort: `10h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {COMPATIBILITY} {IDENTITY} {OBSERVABILITY}
  * Dependencies: T7.1.2, T7.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]; Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31; ADR-005,ADR-006; GAP-004,GAP-005
  * Acceptance Criteria: 1) Supported legacy calls return documented equivalent results from persistent state.; 2) No in-memory manifest is authoritative after migration.; 3) Deprecated semantics produce actionable warnings and migration docs.; 4) Compatibility tests cover restart and multiple-runtime cases.
  * Steps / Subtasks:
    * Inventory public methods, constructors, return types, examples, and tests that depend on HashStore.
    * Implement facade calls using persistent identity repositories and explicit async/runtime ownership.
    * Emit deprecation guidance for storage semantics that were previously overstated.
    * Remove or constrain process-local caches to non-authoritative performance hints with invalidation.
  * Risks & Mitigations: A compatibility facade could accidentally preserve a second, stale identity authority. / Route every authoritative answer to StateStore and treat caches as expendable hints..
  * Tags: [compatibility] [hash-store] [migration] [p0]

## E8. Durable events and transactional outbox

Persist required lifecycle history atomically with authoritative state and project it to transports without making messaging a second authority.

* [ ] - T8.1.1 Define versioned durable event and outbox schemas
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVENTS} {PERSISTENCE} {COMPATIBILITY}
  * Dependencies: T4.1.4, T5.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]; Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23; ADR-004,ADR-012; R-08,R-14
  * Acceptance Criteria: 1) Every required transition event has a stable typed schema and entity references.; 2) Local sequence establishes deterministic within-store ordering.; 3) Outbox state is distinct from event history and transport-specific payload.; 4) Event evolution rules preserve old history and reject unsafe downgrade.
  * Steps / Subtasks:
    * Define event ID, local sequence, schema version, class, occurred/recorded times, correlation/causation IDs, actor, job/phase/attempt/work/content IDs, and typed payload.
    * Define which transitions require durable events and which high-volume observations remain current-state-only or sampled history.
    * Define outbox destination, delivery key, status, attempts, next attempt, and terminal/dead-letter fields.
    * Publish compatibility and evolution rules for event envelopes and payload schemas.
  * Risks & Mitigations: An ambiguous event model could be mistaken for authoritative state or lose causal reconstruction. / Define immutable typed history with explicit state and transport separation..
  * Tags: [events] [outbox] [schemas] [p0]

* [ ] - T8.1.2 Record state transitions, durable events, and outbox rows atomically
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVENTS} {PERSISTENCE} {LIFECYCLE}
  * Dependencies: T8.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]; Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23; ADR-004,ADR-012; R-08,R-14
  * Acceptance Criteria: 1) Fault injection at every transaction step yields all-or-nothing state/history/outbox.; 2) Every required transition query returns its durable event.; 3) Duplicate commands do not create duplicate lifecycle effects.; 4) Transport outage cannot corrupt or roll back already-valid state.
  * Steps / Subtasks:
    * Add recorder APIs that require an active StateStore transaction and validated transition context.
    * Allocate local sequence and append event/outbox records before commit.
    * Refactor orchestrator and built-in phases so required detailed events use the recorder rather than transport-only emission.
    * Define behavior when payload construction, event insert, outbox insert, or commit fails.
  * Risks & Mitigations: Independent commits can leave state without evidence or evidence without truth. / Share one transaction and require recorder participation for guarded mutations..
  * Tags: [atomicity] [events] [transactions] [p0]

* [ ] - T8.1.3 Implement the idempotent outbox dispatcher and delivery backpressure
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVENTS} {RECOVERY} {PERFORMANCE}
  * Dependencies: T8.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]; Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23; ADR-004,ADR-012; R-08,R-14
  * Acceptance Criteria: 1) Redelivery creates no duplicate lifecycle effect.; 2) A poison event is isolated and does not starve later records.; 3) Backlog limits produce documented block/degrade behavior and diagnostics.; 4) Disabling all transports leaves core execution correct.
  * Steps / Subtasks:
    * Lease pending outbox records with fencing, batch limits, delivery keys, and bounded concurrency.
    * Define exponential backoff/jitter, maximum attempts, dead-letter/blocked status, retention, and operator retry controls.
    * Require adapters to report delivered, retryable failure, permanent failure, or unknown outcome.
    * Expose backlog age/size and explicit degraded behavior when limits are reached.
  * Risks & Mitigations: Unbounded or authority-confused delivery can cause memory/storage exhaustion or duplicate effects. / Fence leases, bound retries/backlog, and keep transports projection-only..
  * Tags: [dispatcher] [backpressure] [idempotency] [p0]

* [ ] - T8.1.4 Define progress-event sampling, retention, replay, and event diagnostics
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVENTS} {OBSERVABILITY} {PERFORMANCE}
  * Dependencies: T8.1.2, T8.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]; Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23; ADR-004,ADR-012; R-08,R-14
  * Acceptance Criteria: 1) Current progress remains exact within defined update semantics even when history is sampled.; 2) Required event classes are never sampled or pruned outside policy.; 3) Replay/export detects gaps and schema incompatibility.; 4) Event diagnostics identify backlog, dead letters, retention watermark, and sequence gaps.
  * Steps / Subtasks:
    * Classify events as required transition, evidentiary, operational, sampled progress, or transport-only.
    * Define coalescing/sampling keyed by entity and interval while persisting current progress separately.
    * Define retention/export rules that never delete authoritative state and preserve audit-critical history.
    * Add replay/export cursors for consumers without replaying events as lifecycle commands.
  * Risks & Mitigations: Persisting every progress signal could make the outbox and database the bottleneck; over-sampling could erase evidence. / Separate current progress from sampled history and classify non-droppable events..
  * Tags: [sampling] [retention] [replay] [events] [p0]

## E9. Durable progress, controls, safe points, and checkpoints

Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.

* [ ] - T9.1.1 Define `PhaseContext`, progress, control-request, and checkpoint contracts
  * Priority: `P0`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {LIFECYCLE} {RECOVERY} {SECURITY}
  * Dependencies: T5.1.4, T8.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.; Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28; ADR-011; GAP-006,GAP-007
  * Acceptance Criteria: 1) Contracts distinguish current progress, sampled history, controls, and checkpoints.; 2) All serialized records are versioned and digestible.; 3) PhaseContext grants no direct lifecycle authority.; 4) Safe-point and maximum-control-latency requirements are expressible per phase.
  * Steps / Subtasks:
    * Define current progress fields, monotonicity/aggregation rules, update sequence, and history sampling references.
    * Define control request type, requested/applied/rejected states, actor, correlation, idempotency key, reason, and target scope.
    * Define checkpoint phase/operation/input/config/policy/schema versions, cursor, output references, integrity digest, and safe-point class.
    * Specify which PhaseContext methods are transactional, cancellable, and available to built-ins versus plugins.
  * Risks & Mitigations: An overpowered context or opaque checkpoint would recreate hidden authority and unsafe replay. / Expose narrow typed services and reference-based versioned checkpoints..
  * Tags: [phase-context] [progress] [controls] [checkpoints] [p0]

* [ ] - T9.1.2 Persist live progress and deterministic job-level projections
  * Priority: `P0`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {OBSERVABILITY} {PERSISTENCE} {PERFORMANCE}
  * Dependencies: T9.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.; Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28; ADR-011; GAP-006,GAP-007
  * Acceptance Criteria: 1) A second process observes progress within the documented staleness bound.; 2) Job-level progress is deterministic and never decreases except by a documented retry-generation reset.; 3) Progress write volume remains bounded under million-entry workloads.; 4) Terminal state and final progress are mutually consistent.
  * Steps / Subtasks:
    * Persist current phase progress with sequence/version, units completed/total/unknown, message code, resource counters, and update time.
    * Define aggregation weights or phase-state-based semantics without presenting false precision.
    * Coalesce writes by time/work threshold while guaranteeing bounded status staleness.
    * Link sampled progress events to authoritative current progress sequence.
  * Risks & Mitigations: Unbounded progress writes can create contention, while stale phase-local updates mislead operators. / Persist a bounded current projection with deterministic aggregation and coalescing..
  * Tags: [progress] [status] [durability] [p0]

* [ ] - T9.1.3 Implement durable control requests and safe-point acknowledgement
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {LIFECYCLE} {RECOVERY} {SECURITY}
  * Dependencies: T9.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.; Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28; ADR-011; GAP-006,GAP-007
  * Acceptance Criteria: 1) A second process can request and observe applied/rejected control state.; 2) `PAUSED` is reached only after durable safe-point acknowledgement.; 3) Duplicate control requests are idempotent and conflicting payloads are rejected.; 4) Built-in phases document and test maximum control latency.
  * Steps / Subtasks:
    * Persist idempotent control requests with actor, target, expected state/version, requested time, and correlation.
    * Define phase-specific safe-point classes and maximum polling latency.
    * At a safe point, atomically checkpoint if required, acknowledge applied/rejected state, and transition attempt/phase/job according to policy.
    * Define cancellation cleanup ownership and resume preconditions.
  * Risks & Mitigations: Persisting a request without safe-point semantics can report a pause or cancel that never safely took effect. / Acknowledge only at defined safe points with state/version guards and checkpoint evidence..
  * Tags: [controls] [pause] [cancel] [p0]

* [ ] - T9.1.4 Implement checkpoint validation, resume decisions, and stale-checkpoint rejection
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RECOVERY} {LIFECYCLE} {PROVENANCE}
  * Dependencies: T9.1.2, T9.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.; Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28; ADR-011; GAP-006,GAP-007
  * Acceptance Criteria: 1) Stale or incompatible checkpoints never resume execution.; 2) Every built-in phase declares checkpoint granularity and validation inputs.; 3) Crash tests resume or restart according to one deterministic rule.; 4) Checkpoint rejection remains visible in status and diagnostics.
  * Steps / Subtasks:
    * Define checkpoint creation transactions, immutable digest, predecessor chain, and latest-compatible lookup.
    * Validate job/phase/attempt, input identity, config/policy digest, plugin/backend version, schema, cursor, referenced outputs, and fencing epoch before resume.
    * Define per-phase resume-from-checkpoint versus restart-from-beginning behavior and cleanup of incompatible partial state.
    * Record rejection reason and deterministic recovery decision.
  * Risks & Mitigations: Blind checkpoint reuse can combine stale inputs or side effects with a new attempt. / Bind checkpoints to exact authority fields and fail closed on any mismatch..
  * Tags: [resume] [checkpoint] [validation] [p0]

## E10. Canonical race-resistant source access

Route every source read through one registered-root, source-relative, capability-aware service that detects symlink, mount, case, Unicode, and TOCTOU hazards.

* [ ] - T10.1.1 Specify source-access policy and platform capability contracts
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SAFETY} {SECURITY} {COMPATIBILITY}
  * Dependencies: T6.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].; Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23; R-03,R-04; E-ATL-016
  * Acceptance Criteria: 1) Policy documents exact guarantees by supported platform.; 2) Unsafe or unsupported capability combinations fail before intake/job execution.; 3) Source and destination path authorities remain separate.; 4) Every normalization and policy decision has a stable error/status code.
  * Steps / Subtasks:
    * Define canonical root and relative-path representations, allowed entry classes, symlink policy, mount boundary, path length, case/Unicode strategy, and expected occurrence metadata.
    * Define platform capability probes for handle-relative open, no-follow, directory descriptors, stable file IDs, mount IDs, and no-replace operations.
    * Define strong, reduced-assurance, and unsupported modes with explicit startup/config behavior.
    * Separate source reads from workspace/destination path construction and temporary-file APIs.
  * Risks & Mitigations: Cross-platform path semantics can make a syntactically clean path escape its intended root. / Probe capabilities, define guarantees explicitly, and fail closed when strong containment is unavailable..
  * Tags: [path-safety] [platform] [policy] [p0]

* [ ] - T10.1.2 Implement handle-relative no-follow opens and occurrence verification
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SAFETY} {SECURITY} {PERFORMANCE}
  * Dependencies: T10.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].; Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23; R-03,R-04; E-ATL-016
  * Acceptance Criteria: 1) Symlink/reparse swap fixtures cannot escape the registered root.; 2) Opened object identity is compared to the occurrence before bytes are trusted.; 3) Unsupported strong primitives are reported, never silently emulated as equivalent.; 4) All descriptors close on success, cancellation, and failure.
  * Steps / Subtasks:
    * Open and retain a trusted root handle/identity, resolve path components without following unapproved links, and reject root escape.
    * Open the final object with required flags, validate type and available device/inode/file-ID/size metadata against the occurrence, and return a mediated handle.
    * Revalidate relevant metadata after read and close all descriptors deterministically.
    * Surface platform capability and reduced-assurance reason with every access result.
  * Risks & Mitigations: Check-then-open path validation can be bypassed by concurrent filesystem mutation. / Use handle-relative operations and verify the opened object, not just the pathname..
  * Tags: [source-access] [toctou] [handles] [p0]

* [ ] - T10.1.3 Create separate safe temporary and destination path services
  * Priority: `P0`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SAFETY} {STORAGE} {SECURITY}
  * Dependencies: T10.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].; Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23; R-03,R-04; E-ATL-016
  * Acceptance Criteria: 1) All temp/workspace files are attempt-owned, permission-restricted, and contained.; 2) No-replace behavior is capability-tested and collision-safe.; 3) Cleanup is idempotent and cannot escape its root.; 4) Source and destination APIs cannot be substituted for one another by type/interface.
  * Steps / Subtasks:
    * Define APIs for attempt workspace children, staged output names, unique temp files, destination-relative targets, and no-replace/expected-replace commits.
    * Use restrictive permissions, unpredictable names, same-filesystem staging where atomic commit is required, and explicit cleanup ownership.
    * Reject untrusted member/plugin-provided names before path construction.
    * Return mediated handles/objects rather than raw unrestricted paths where practical.
  * Risks & Mitigations: Mixing read and write path helpers can give untrusted inputs an unintended mutation path. / Use distinct typed services and attempt-owned roots with no-replace commits..
  * Tags: [tempfiles] [destinations] [workspace] [p0]

* [ ] - T10.1.4 Route every built-in filesystem operation through canonical access services
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SAFETY} {ARCHITECTURE} {SECURITY}
  * Dependencies: T10.1.2, T10.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].; Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23; R-03,R-04; E-ATL-016
  * Acceptance Criteria: 1) Static analysis finds no unapproved direct filesystem authority in built-in phases.; 2) Every source read is attributable to SourceRoot/Generation/Occurrence.; 3) Every write is attributable to job/phase/attempt/workspace or publication attempt.; 4) Bypass attempts fail deterministic security tests.
  * Steps / Subtasks:
    * Inventory every `open`, `stat`, `walk`, `glob`, archive extract, temp, subprocess file, and destination write call.
    * Refactor each call to the appropriate source, workspace, content-store, or destination service with occurrence/attempt attribution.
    * Add a static allowlist or architecture test for unavoidable low-level implementation calls.
    * Emit access decisions and stable errors without logging sensitive paths or content.
  * Risks & Mitigations: One direct open or extraction path can invalidate the entire source-safety model. / Inventory all calls, route through canonical services, and add enforceable architecture tests..
  * Tags: [integration] [guardrails] [filesystem] [p0]

## E11. Quarantine, recursive archive budgets, and controlled materialization

Inspect containers before extraction, contain every side effect in attempt-owned workspaces, and enforce cumulative recursive resource limits.

* [ ] - T11.1.1 Implement attempt-owned quarantine workspace lifecycle
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SAFETY} {STORAGE} {RECOVERY}
  * Dependencies: T7.1.4, T10.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].; Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25; R-05; GAP-010,GAP-013
  * Acceptance Criteria: 1) No Phase-D or analyzer write occurs under any registered source root.; 2) Every workspace is attributable to one attempt and has deterministic status/recovery.; 3) Quotas and actual usage are persisted and enforced.; 4) Cleanup is idempotent, contained, and preserves evidence when ownership is uncertain.
  * Steps / Subtasks:
    * Allocate canonical workspace roots outside source roots using job/phase/attempt identity and unpredictable staging names.
    * Persist status CREATED/ACTIVE/SEALED/CLEANUP_PENDING/CLEANED/ORPHANED/BLOCKED, quota, permissions, provider, and manifest digest.
    * Provide mediated child creation, byte/file accounting, seal/no-more-writes, and idempotent cleanup.
    * Reconcile orphan or partial workspaces at startup without deleting unknown operator data.
  * Risks & Mitigations: Source-adjacent or weakly owned extraction can overwrite evidence, collide on replay, or escape cleanup. / Use unique attempt-owned quarantines with persisted lifecycle and strict containment..
  * Tags: [quarantine] [workspace] [isolation] [p0]

* [ ] - T11.1.2 Implement recursive structural inspection under cumulative archive budgets
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SAFETY} {PERFORMANCE} {PROVENANCE}
  * Dependencies: T11.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].; Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25; R-05; GAP-010,GAP-013
  * Acceptance Criteria: 1) All adversarial containers terminate within configured CPU/time/byte/member/depth bounds.; 2) Nested limits are cumulative and recursively enforced.; 3) Every member decision is recorded with stable reason and parent linkage.; 4) Unknown or partial inspection cannot authorize extraction.
  * Steps / Subtasks:
    * Define canonical member paths and reject absolute, drive, UNC, NUL, parent traversal, reserved/device, link, and special entries by default.
    * Inspect supported nested formats through a bounded queue while carrying cumulative depth, member, declared/actual expanded bytes, ratio, temp, and elapsed budgets.
    * Record accepted/skipped/rejected/unknown member decisions with reason and parent content/member identity.
    * Stop deterministically at limits and mark partial/unknown structure non-success.
  * Risks & Mitigations: Counting nested files without recursively enforcing cumulative limits leaves decompression and parser exhaustion paths. / Use a bounded structural work queue and account both declared and actual resources..
  * Tags: [archives] [recursive] [budgets] [p0]

* [ ] - T11.1.3 Implement exact-report-bound `MaterializationService`
  * Priority: `P0`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SAFETY} {STORAGE} {LIFECYCLE}
  * Dependencies: T11.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].; Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25; R-05; GAP-010,GAP-013
  * Acceptance Criteria: 1) Phase D rejects every report/content/config/policy mismatch before writing.; 2) No output escapes the attempt workspace or overwrites an existing file.; 3) Actual written bytes and file counts remain within cumulative budgets.; 4) Partial/cancelled attempts retain deterministic status, evidence, and cleanup ownership.
  * Steps / Subtasks:
    * Validate report state, parent content identity, inspector/config/policy digests, approved member plan, workspace ownership, and current budgets before any write.
    * Stream each member to a unique staged file with no-follow/no-replace semantics, actual byte accounting, hash calculation, fsync policy, and final seal.
    * Reject links/devices/specials and canonicalize destination names independently of archive library output.
    * Persist partial results and cleanup state; never present partial extraction as complete.
  * Risks & Mitigations: Extraction driven from live paths or library defaults can bypass structural decisions and create uncontrolled files. / Bind to exact reports, stream through mediated writers, and fail closed on mismatch..
  * Tags: [materialization] [extraction] [no-overwrite] [p0]

* [ ] - T11.1.4 Persist derivation edges and adversarial materialization evidence
  * Priority: `P0`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PROVENANCE} {SAFETY} {RELEASE}
  * Dependencies: T11.1.2, T11.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].; Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25; R-05; GAP-010,GAP-013
  * Acceptance Criteria: 1) Every downstream extracted identity has at least one valid derivation edge.; 2) No derivation is committed before child hash verification.; 3) Bidirectional lineage queries detect and reject orphan records.; 4) Adversarial corpus tests complete within declared resource ceilings on supported platforms.
  * Steps / Subtasks:
    * Persist parent content identity, structural report, member identity/path, extraction attempt, workspace output, child content identity, bytes, and disposition.
    * Create derivation only after the child hash is verified; keep failed/partial member attempts separately.
    * Build bidirectional lineage queries and invariant checks for orphan children or duplicate commits.
    * Version the adversarial corpus with generated provenance, expected policy decision, and resource ceiling.
  * Risks & Mitigations: Materialized files without durable derivation make downstream findings irreproducible and untrustworthy. / Hash before commit and persist immutable parent/member/report/attempt lineage..
  * Tags: [derivation] [lineage] [archive-tests] [p0]

## E12. Optional immutable local content store

Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.

* [ ] - T12.1.1 Define `ContentStore` contracts and retention-mode semantics
  * Priority: `P1`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {STORAGE} {IDENTITY} {CONFIGURATION}
  * Dependencies: T7.1.4, T10.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.; Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28; ADR-005; R-06,R-07
  * Acceptance Criteria: 1) Retention mode has one documented effect on job state and replayability.; 2) Provider contract distinguishes absent, corrupt, unknown, and verified blobs.; 3) Default mode and compatibility policy are approved and recorded.; 4) No API equates `ContentIdentity` existence with managed-byte availability.
  * Steps / Subtasks:
    * Define staged put, verified open, stat, integrity check, lease/reference, retention class, delete/tombstone, and orphan reconciliation contracts.
    * Define retention modes and exactly how each affects job success, replayability, diagnostics, and later result reuse.
    * Define blob states STAGING/COMMITTED/ORPHANED/CORRUPT/MISSING/DELETING/DELETED with authority rules.
    * Resolve the default retention mode through an operator/product decision and record migration behavior.
  * Risks & Mitigations: An implicit default could create unexpected disk growth or false reproducibility claims. / Make retention mode explicit, measured, and visible in status/provenance..
  * Tags: [cas] [retention-mode] [contracts] [p1]

* [ ] - T12.1.2 Implement staged, verified, no-replace local CAS writes
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {STORAGE} {SECURITY} {RECOVERY}
  * Dependencies: T12.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.; Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28; ADR-005; R-06,R-07
  * Acceptance Criteria: 1) Repeated identical bytes consume one verified blob payload.; 2) Concurrent writes yield one commit and safe verified reuse.; 3) Existing mismatch is blocked and surfaced as integrity incident.; 4) Crash points leave valid blob, detectable orphan, or no blob—never false commit.
  * Steps / Subtasks:
    * Derive provider-relative paths from canonical SHA-256 with bounded directory fan-out.
    * Write to an exclusive attempt-owned staging file while hashing and accounting bytes; verify digest/size before commit.
    * Fsync file and parent directory where supported, then perform no-replace commit or verified platform-safe equivalent.
    * If target exists, verify its digest/size before reuse; mismatch becomes an integrity incident.
  * Risks & Mitigations: A non-atomic or overwrite-capable CAS can corrupt canonical bytes while preserving a trusted digest label. / Use exclusive staging, verify before commit, and never replace an existing digest path..
  * Tags: [local-cas] [atomic-write] [integrity] [p1]

* [ ] - T12.1.3 Persist blob provenance, references, quotas, and replayability status
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {STORAGE} {PROVENANCE} {OBSERVABILITY}
  * Dependencies: T12.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.; Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28; ADR-005; R-06,R-07
  * Acceptance Criteria: 1) Every committed blob has verifiable identity, provider, provenance, and retention status.; 2) Replayability is accurate after restart and missing/corrupt file detection.; 3) Quota use and reservations reconcile deterministically.; 4) Identity-only and captured modes remain distinguishable in APIs/events.
  * Steps / Subtasks:
    * Persist provider key, canonical identity, size, status, capture attempt/occurrence, verification time, retention class, and reference counts/leases.
    * Make identity hashing and capture one pass where configured, with separate success/failure outcomes.
    * Enforce provider/job/global quotas before and during writes and report capacity decisions.
    * Expose `replayable_from_managed_bytes` and exact reason.
  * Risks & Mitigations: Filesystem and database state can diverge around blob commits, producing false presence or leaked capacity. / Persist explicit states, verify on use, and reconcile reservations/orphans..
  * Tags: [blob-records] [quota] [replayability] [p1]

* [ ] - T12.1.4 Implement CAS integrity scans and orphan reconciliation hooks
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {STORAGE} {RECOVERY} {OPERATIONS}
  * Dependencies: T12.1.2, T12.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.; Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28; ADR-005; R-06,R-07
  * Acceptance Criteria: 1) Reconciliation classifies every observed divergence with deterministic next action.; 2) Safe repairs are idempotent and uncertain objects remain preserved/quarantined.; 3) Scans are resumable/bounded and expose progress.; 4) Integrity incidents disable replay/reuse until resolved.
  * Steps / Subtasks:
    * Compare committed records to provider objects and digest/size metadata under bounded scan budgets.
    * Classify missing, corrupt, orphaned, abandoned staging, unreferenced, and unknown objects.
    * Provide dry-run plans and idempotent repairs for safe cases; quarantine or block uncertain cases.
    * Emit integrity events/metrics and retain reconciliation manifests.
  * Risks & Mitigations: Aggressive cleanup can destroy the only retained bytes; absent cleanup can exhaust disk. / Classify before action, default preserve, and require policy for deletion..
  * Tags: [reconciliation] [integrity] [cas] [p1]

## E13. Structural and extraction lineage contracts

Persist exact-byte structural reports and extraction records whose bindings are verified before materialization and reusable only under exact deterministic keys.

* [ ] - T13.1.1 Define and persist versioned `StructuralReport` records
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PROVENANCE} {SAFETY} {PERSISTENCE}
  * Dependencies: T11.1.4, T12.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.; Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31; ADR-013
  * Acceptance Criteria: 1) Every report binds to exact parent bytes, inspector, config, policy, and schema versions.; 2) Partial and unknown outcomes are visibly non-success.; 3) Member manifests are deterministic and queryable without unbounded loads.; 4) Reports are immutable and supersession preserves history.
  * Steps / Subtasks:
    * Define report ID, parent ContentIdentity, inspector/plugin/version, operation/config/policy digest, schema version, member manifest digest, budget summary, warnings, confidence/unknown state, and acceptance decision.
    * Persist normalized member records and nested parent relationships without embedding unbounded raw metadata.
    * Make reports immutable and allow supersession only by a new report.
    * Define deterministic report reuse key and non-cacheable/partial semantics.
  * Risks & Mitigations: A structure report not bound to exact bytes/policy can authorize extraction of different content. / Persist immutable exact-key bindings and reject partial/unknown acceptance..
  * Tags: [structure] [reports] [lineage] [p1]

* [ ] - T13.1.2 Define and persist `ExtractionRecord` and output manifests
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PROVENANCE} {STORAGE} {RECOVERY}
  * Dependencies: T13.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.; Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31; ADR-013
  * Acceptance Criteria: 1) Every extraction attempt has one immutable record and output manifest.; 2) Successful records reference only verified child identities and derivations.; 3) Partial/failure cleanup state remains explicit.; 4) Output manifest supports deterministic bidirectional lineage queries.
  * Steps / Subtasks:
    * Define report binding, attempt/workspace IDs, planned members, actual outputs, child identities, budget start/end, status, error, cleanup, and output manifest digest.
    * Persist per-member attempt outcome and derivation reference incrementally under one attempt.
    * Seal a successful record only after all approved outputs are hashed and workspace state is consistent.
    * Retain failed/cancelled/partial records for recovery and audit.
  * Risks & Mitigations: Without attempt-level records, partial writes and retries cannot be reconciled or attributed. / Persist plans and actual effects incrementally, then seal only after verification..
  * Tags: [extraction-record] [outputs] [lineage] [p1]

* [ ] - T13.1.3 Enforce exact content, configuration, policy, and report binding before extraction
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SAFETY} {LIFECYCLE} {SECURITY}
  * Dependencies: T13.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.; Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31; ADR-013
  * Acceptance Criteria: 1) All mismatches are detected before workspace creation or output writes.; 2) Exact-key equality is based on canonical normalized values.; 3) A valid report/material pair proceeds through one controlled path.; 4) Blocked reasons are visible in state, event history, and status.
  * Steps / Subtasks:
    * Load report and verify ACCEPTED state, parent content identity, inspector/schema, config/policy digest, selected member plan, and job/intake ownership.
    * Verify current material source is the same retained/validated ContentIdentity.
    * Create extraction attempt/workspace only after binding validation succeeds.
    * Return stable blocked/error reasons and durable event without side effects on mismatch.
  * Risks & Mitigations: Convenience fallback can bypass the structural safety barrier and reintroduce live-source ambiguity. / Require exact report identity and fail before any materialization..
  * Tags: [binding] [phase-d] [fail-closed] [p1]

* [ ] - T13.1.4 Add deterministic structure reuse and end-to-end lineage invariants
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PROVENANCE} {PERFORMANCE} {COMPATIBILITY}
  * Dependencies: T13.1.2, T13.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.; Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31; ADR-013
  * Acceptance Criteria: 1) Reuse occurs only on exact key equality and records current use provenance.; 2) Every derived content identity traces to at least one valid parent/report/extraction/attempt.; 3) Every publication-ready lineage can traverse back to SourceRoot and exact bytes.; 4) Graph invariant checks detect all injected orphan/cross-job/cycle cases.
  * Steps / Subtasks:
    * Define reuse key from content identity, inspector/version, config/policy/schema digest, deterministic flag, and relevant capability version.
    * On reuse, append a reuse record tied to the current job/phase attempt rather than copying or mutating the report.
    * Implement lineage queries including SourceRoot, IntakeGeneration, Occurrence, ContentIdentity, StructuralReport, ExtractionRecord, Derivation, and child identity.
    * Add invariant checks for orphan, cyclic, cross-job, missing, or inconsistent edges.
  * Risks & Mitigations: Loose reuse keys or incomplete graphs can produce stale results that appear correctly attributed. / Require exact deterministic keys and validate graph invariants continuously..
  * Tags: [reuse] [lineage] [invariants] [p1]

## E14. Typed plugin contracts, registry, and trust policy

Turn Deep Understanding into a deterministic, versioned capability platform whose plugins emit normalized findings without receiving lifecycle or host authority.

* [ ] - T14.1.1 Define `PluginDescriptor`, `AnalysisContext`, and `AnalysisFinding` schemas
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PLUGINS} {SECURITY} {PROVENANCE}
  * Dependencies: T3.1.4, T7.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].; Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23; ADR-007,ADR-010; R-09,R-17,R-18
  * Acceptance Criteria: 1) No arbitrary dictionary reaches durable findings.; 2) Descriptors express every required capability/resource and fail validation when incomplete.; 3) AnalysisContext exposes no lifecycle or raw persistence authority.; 4) Finding schema preserves complete attributed result sets beyond prior 50-item summaries.
  * Steps / Subtasks:
    * Define stable plugin ID/version/API range, input content/artifact types, output schema versions, deterministic/cacheable flags, provenance, and supported backends.
    * Declare filesystem read/write, network, subprocess/tool, active-content, CPU, memory, temp, process, and timeout expectations.
    * Define finding category/severity, observation, source/content references, confidence, evidence type, relationships, tool/model version, timestamps, and bounded structured data.
    * Define context methods that cannot access StateStore, source roots, lifecycle transitions, decisions, or publication.
  * Risks & Mitigations: Weak contracts let plugins smuggle authority, lose attribution, or create unbounded/ambiguous outputs. / Use strict descriptors, mediated context, normalized findings, and bounded schemas..
  * Tags: [plugins] [contracts] [findings] [p1]

* [ ] - T14.1.2 Implement deterministic plugin discovery and registry snapshots
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PLUGINS} {ARCHITECTURE} {COMPATIBILITY}
  * Dependencies: T14.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].; Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23; ADR-007,ADR-010; R-09,R-17,R-18
  * Acceptance Criteria: 1) Two clean registry builds produce identical order and digest.; 2) Duplicate/incompatible plugins fail before job creation.; 3) Jobs retain the exact registry snapshot/version used.; 4) Unavailable plugin states are distinct from disabled policy.
  * Steps / Subtasks:
    * Define approved discovery sources, deterministic ordering, duplicate/conflict rules, enabled/deployed status, and runtime freeze semantics.
    * Validate descriptor, import/factory, API range, output schemas, backend availability, external tools, and policy grants.
    * Compute a canonical registry snapshot/digest persisted with jobs and findings.
    * Provide explicit unavailable/disabled/incompatible diagnostics instead of silent omission.
  * Risks & Mitigations: Nondeterministic or unsafe discovery can execute the wrong plugin version or import hostile code at startup. / Restrict discovery, validate/freeze descriptors, and fail on ambiguity..
  * Tags: [registry] [discovery] [determinism] [p1]

* [ ] - T14.1.3 Implement plugin capability and trust-tier policy
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PLUGINS} {SECURITY} {EXECUTION}
  * Dependencies: T14.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].; Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23; ADR-007,ADR-010; R-09,R-17,R-18
  * Acceptance Criteria: 1) Every enabled plugin has one effective capability set and required backend.; 2) Untrusted/high-risk plugins cannot run in process.; 3) Policy/config/version changes invalidate stale WorkSpecs and reuse keys.; 4) Denied capability attempts are observable and tested.
  * Steps / Subtasks:
    * Define trust inputs: bundled/signed/approved provenance, active-content risk, filesystem/network/tool needs, deterministic claim, and deployment policy.
    * Return effective capabilities, required backend, limits, denied reasons, and policy digest.
    * Require in-process execution only for explicitly trusted bundled plugins; route risky/external-tool work to isolation or block.
    * Persist policy decision/version with WorkSpec and findings.
  * Risks & Mitigations: Treating declarations as grants or trusting all plugins in-process gives third-party code host and lifecycle influence. / Evaluate capabilities through deterministic policy and require isolation or deny..
  * Tags: [trust-policy] [capabilities] [isolation] [p1]

* [ ] - T14.1.4 Add the legacy `AnalyzerPlugin` adapter and lossless finding migration
  * Priority: `P1`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {COMPATIBILITY} {PLUGINS} {PROVENANCE}
  * Dependencies: T14.1.2, T14.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].; Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23; ADR-007,ADR-010; R-09,R-17,R-18
  * Acceptance Criteria: 1) Supported legacy plugins produce equivalent normalized findings through the adapter.; 2) All findings persist losslessly within declared limits.; 3) Unsupported authority assumptions fail with migration guidance.; 4) Metadata summary is explicitly derived and never authoritative.
  * Steps / Subtasks:
    * Inventory existing analyzer protocol, registration, result dictionaries, metadata summaries, and example plugins.
    * Wrap legacy plugins with explicit synthetic descriptor defaults only where behavior is provable; otherwise require migration.
    * Normalize every result into typed findings and persist all findings; keep metadata as bounded derived summary.
    * Emit deprecation diagnostics and a migration guide for plugin authors.
  * Risks & Mitigations: A compatibility adapter can silently preserve untyped output and unrestricted authority. / Normalize strictly, deny undeclared capabilities, and time-bound the adapter..
  * Tags: [legacy-plugin] [migration] [findings] [p1]

## E15. ExecutionBackend contracts and trusted in-process execution

Separate lifecycle authority from execution location using immutable WorkSpec/WorkResult contracts and a conformance-tested trusted backend.

* [ ] - T15.1.1 Define immutable `WorkSpec`, `WorkResult`, and backend protocols
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {LIFECYCLE} {SECURITY}
  * Dependencies: T5.1.4, T14.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.; Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21; ADR-008,ADR-010
  * Acceptance Criteria: 1) Contracts are versioned, deterministic, and backend-neutral.; 2) Backend code cannot obtain StateStore or transition authority through the interface.; 3) Malformed/stale/foreign results are representable as validation failures.; 4) Contract supports in-process, subprocess, and later remote backends without changing lifecycle semantics.
  * Steps / Subtasks:
    * Define operation ID/version, plugin/handler, input identity references, config/policy/registry digests, resource budget, deadline, idempotency key, attempt/work IDs, and fencing token.
    * Define result status, echoed authority fields, output references/manifest digest, findings, diagnostics, usage, start/end, and backend identity.
    * Define cancellation/deadline protocol, health/capabilities, and serialization/version negotiation.
    * Make specs/results content-addressable or digestible for audit and duplicate detection.
  * Risks & Mitigations: A weak execution contract can leak authority or force lifecycle semantics into each backend. / Make immutable authority fields explicit and validate all results centrally..
  * Tags: [work-spec] [backend] [contracts] [p1]

* [ ] - T15.1.2 Implement the trusted `InProcessBackend`
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {PLUGINS} {RECOVERY}
  * Dependencies: T15.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.; Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21; ADR-008,ADR-010
  * Acceptance Criteria: 1) A bundled analyzer produces identical normalized findings through WorkSpec/WorkResult.; 2) Backend has no direct persistence/lifecycle mutation capability.; 3) Timeout/cancel outcomes are explicit and later recovery-classifiable.; 4) Registry and policy versions used are echoed and validated.
  * Steps / Subtasks:
    * Resolve approved operation/plugin factory from frozen registries and create mediated context from WorkSpec.
    * Execute asynchronously with deadline/cancellation propagation and capture normalized result/usage/diagnostics.
    * Prevent handler access to runtime globals, raw StateStore, source roots, or unrestricted workspace paths through provided interfaces.
    * Return WorkResult without committing lifecycle state.
  * Risks & Mitigations: An in-process backend can accidentally retain direct runtime authority or block the event loop. / Limit it to trusted code, mediated contexts, frozen registries, and explicit deadline behavior..
  * Tags: [in-process] [trusted] [backend] [p1]

* [ ] - T15.1.3 Implement coordinator-side result validation and commit
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {LIFECYCLE} {SECURITY}
  * Dependencies: T15.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.; Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21; ADR-008,ADR-010
  * Acceptance Criteria: 1) Only fully validated current results can change attempt/phase state.; 2) Duplicate identical results have one authoritative effect.; 3) Stale/malformed/conflicting results are retained and rejected with stable codes.; 4) Output integrity and budgets are verified before downstream use.
  * Steps / Subtasks:
    * Load expected attempt/work/spec digest and compare all echoed authority fields and fencing token.
    * Validate result schema, status, deadlines, usage, finding limits, output manifest, content identities, and workspace ownership.
    * Persist accepted or rejected result evidence, then invoke guarded attempt/phase transition in one transaction/event path.
    * Make duplicate identical results idempotent and conflicting duplicates/stale results explicit.
  * Risks & Mitigations: Accepting backend claims directly would let crashes, stale workers, or malicious plugins corrupt lifecycle truth. / Revalidate every authority and output field in the coordinator before commit..
  * Tags: [result-validation] [fencing] [commit] [p1]

* [ ] - T15.1.4 Create the reusable backend conformance and fault suite
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {RELEASE} {COMPATIBILITY}
  * Dependencies: T15.1.2, T15.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.; Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21; ADR-008,ADR-010
  * Acceptance Criteria: 1) InProcessBackend passes every applicable mandatory case.; 2) The suite can be reused unchanged by subprocess and remote backends.; 3) Unsupported controls are reported and block claims that they are enforced.; 4) Fault cases produce deterministic coordinator outcomes.
  * Steps / Subtasks:
    * Test spec acceptance, result echo/schema, cancellation, deadline, progress, resource reporting, duplicate submission, stale fencing, output mediation, and health.
    * Inject backend crash/loss, malformed result, delayed result, partial output, cancellation race, and unavailable capability.
    * Compare normalized result semantics across backends for the same deterministic fixture.
    * Publish required versus platform-optional conformance cases and unsupported-control evidence.
  * Risks & Mitigations: Each backend could otherwise implement subtly different lifecycle, cancellation, and failure semantics. / Make a shared conformance suite a registration and release gate..
  * Tags: [conformance] [fault-injection] [backends] [p1]

## E16. Phase-internal work items, deterministic reuse, and unified budgets

Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.

* [ ] - T16.1.1 Define durable `WorkItem` and phase-barrier semantics
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {LIFECYCLE} {ARCHITECTURE}
  * Dependencies: T8.1.4, T9.1.4, T12.1.4, T13.1.4, T15.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance; PROMPT:Pasted markdown (2).md:Stage 5; ADR-001,ADR-008; R-17
  * Acceptance Criteria: 1) The model supports bounded parallelism while A-F order remains immutable.; 2) Work-item IDs/order are deterministic for identical phase inputs.; 3) Cross-phase dependencies and cycles are structurally impossible or rejected.; 4) Barrier closure requires all declared invariants and aggregate validation.
  * Steps / Subtasks:
    * Define work item identity, phase run, operation/plugin, input references, parent/partition key, deterministic ordinal, state, attempt, dependencies limited to same phase, and result reference.
    * Define phase barrier completion: all required work items terminal and valid aggregation before next semantic phase.
    * Define bounded dynamic expansion only from verified work results with deterministic IDs and depth/count limits.
    * Define optional/skipped/failed item propagation without allowing work items to transition job/phase state directly.
  * Risks & Mitigations: A generic work graph could quietly turn ATLAS into a scheduler and weaken lifecycle semantics. / Scope dependencies and expansion to one phase and keep barrier authority in the coordinator..
  * Tags: [work-items] [parallelism] [phase-barrier] [p1]

* [ ] - T16.1.2 Implement the bounded local work-item scheduler and aggregation path
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {PERFORMANCE} {RECOVERY}
  * Dependencies: T16.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance; PROMPT:Pasted markdown (2).md:Stage 5; ADR-001,ADR-008; R-17
  * Acceptance Criteria: 1) Concurrency never exceeds configured/effective budgets.; 2) Ready sets and aggregation remain bounded under large worksets.; 3) Crash/restart does not duplicate accepted work effects.; 4) Phase barrier closes only after deterministic aggregate validation.
  * Steps / Subtasks:
    * Persist deterministic work plans and ready/running/terminal item states with claims/fencing.
    * Schedule only within current phase using configured per-job/per-phase/per-plugin concurrency and fair queueing.
    * Integrate control polling, cancellation, deadlines, retries, and checkpointable planner cursors.
    * Aggregate accepted results into phase outputs and close the barrier through LifecycleCoordinator.
  * Risks & Mitigations: Unbounded fan-out or weak claims can exhaust memory and duplicate work. / Persist plans, stream readiness, enforce concurrency/fencing, and bound expansion..
  * Tags: [scheduler] [bounded-concurrency] [aggregation] [p1]

* [ ] - T16.1.3 Implement exact-key deterministic result reuse
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PERFORMANCE} {PROVENANCE} {SECURITY}
  * Dependencies: T16.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance; PROMPT:Pasted markdown (2).md:Stage 5; ADR-001,ADR-008; R-17
  * Acceptance Criteria: 1) Reuse occurs only under exact canonical key and verified outputs.; 2) Every reuse is attributable to original result and current decision.; 3) Stale/missing/corrupt/non-deterministic results are not reused.; 4) Metrics quantify hit rate and avoided work without losing occurrence provenance.
  * Steps / Subtasks:
    * Define canonical operation key from operation/version, input identities, plugin/tool/model version, config/policy/registry/schema digests, deterministic flag, and declared environment inputs.
    * Persist result digest, output references, findings/report IDs, integrity status, and invalidation reason.
    * Before reuse, verify current policy, output existence/integrity, schema compatibility, and no prior incident.
    * Record a reuse decision/attempt tied to the current job rather than pretending the prior execution reran.
  * Risks & Mitigations: An incomplete cache key can return stale or policy-incompatible conclusions with convincing provenance. / Use exact typed keys, verify outputs, and default uncertain operations non-cacheable..
  * Tags: [memoization] [reuse] [determinism] [p1]

* [ ] - T16.1.4 Implement a unified hierarchical `ResourceBudgetManager`
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PERFORMANCE} {SECURITY} {OBSERVABILITY}
  * Dependencies: T16.1.2, T16.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance; PROMPT:Pasted markdown (2).md:Stage 5; ADR-001,ADR-008; R-17
  * Acceptance Criteria: 1) All core resource-consuming operations use scoped budget handles.; 2) Concurrent reservations cannot exceed hard shared limits.; 3) Restart reconciliation clears or transfers abandoned reservations deterministically.; 4) Status and diagnostics distinguish requested, reserved, used, exceeded, and unenforceable.
  * Steps / Subtasks:
    * Define budget dimensions, hierarchy/inheritance, reservation/commit/release, soft versus hard limits, and platform-enforceability metadata.
    * Integrate archive, workspace, hashing, event, scheduler, plugin, and backend accounting with one scoped API.
    * Persist authoritative counters/reservations needed for restart and reconcile abandoned reservations.
    * Define deterministic behavior on soft warning, hard exceed, unknown usage, and unsupported enforcement.
  * Risks & Mitigations: Independent subsystem limits can double-count, conflict, or allow aggregate exhaustion. / Use one hierarchical accounting authority with persisted reservations and explicit enforcement capability..
  * Tags: [resource-governance] [quotas] [budgets] [p1]

## E17. Durable findings, evidence, review, and publication

Separate analytical output from evidence, trust decisions, and externally verified publications while preserving exact-byte lineage and fail-closed authority.

* [ ] - T17.1.1 Persist normalized analysis findings and typed relationships
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {REVIEW} {PROVENANCE} {PLUGINS} {PERSISTENCE}
  * Dependencies: T7.1.4, T8.1.4, T13.1.4, T14.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].; Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31; ADR-009; GAP-011,GAP-015
  * Acceptance Criteria: 1) Every persisted finding identifies exact input content, analyzer/plugin version, configuration digest, phase attempt, and schema version.; 2) Finding persistence cannot create evidence, a promotion decision, or a publication.; 3) Duplicate policy and supersession behavior are deterministic and documented.; 4) Legacy findings remain readable without being misrepresented as approved knowledge.
  * Steps / Subtasks:
    * Define stable finding IDs, finding schema version, content/derived-artifact subject, analyzer and plugin-version identity, attempt/work-item origin, confidence/uncertainty, observed time, and supersession state.
    * Define a closed initial relationship vocabulary plus an extension namespace; reject unknown unversioned relationship semantics.
    * Persist findings transactionally with the phase result and durable event; expose deterministic ordering and pagination.
    * Keep legacy metadata output as a derived compatibility view and mark unmappable legacy records as `authority=none`.
  * Risks & Mitigations: A loose finding schema could recreate hidden metadata contracts and allow analytical assertions to masquerade as trusted evidence. / Use typed, versioned records with explicit non-authoritative status and a separate evidence/review path..
  * Tags: [findings] [analysis] [provenance] [p1]

* [ ] - T17.1.2 Define and persist evidence records with explicit provenance and confidence
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {REVIEW} {PROVENANCE} {SECURITY} {PERSISTENCE}
  * Dependencies: T17.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].; Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31; ADR-009; GAP-011,GAP-015
  * Acceptance Criteria: 1) Evidence-set digests are stable under deterministic canonical ordering and change when any cited record changes.; 2) Every evidence record resolves to immutable source observations or explicitly labeled external authority.; 3) Unverified findings cannot silently become deterministic evidence.; 4) Superseded evidence remains queryable and cannot satisfy a current-decision policy unless allowed explicitly.
  * Steps / Subtasks:
    * Define evidence classes for deterministic observation, structural validation, extraction verification, analyzer corroboration, policy evaluation, and external verification.
    * Require every evidence record to cite one or more immutable source records and an exact subject identity.
    * Compute a canonical evidence-record digest and an ordered evidence-set digest for review binding.
    * Define validity, expiry where applicable, revocation/supersession, and provenance-completeness rules without rewriting history.
  * Risks & Mitigations: Evidence may become a vague label that hides source quality or lets a plugin self-certify its claims. / Require typed evidence classes, immutable citations, explicit verifier identity, and policy-visible confidence/validity..
  * Tags: [evidence] [confidence] [lineage] [p1]

* [ ] - T17.1.3 Implement evidence-bound promotion decisions and review policy
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {REVIEW} {SECURITY} {LIFECYCLE} {COMPATIBILITY}
  * Dependencies: T17.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].; Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31; ADR-009; GAP-011,GAP-015
  * Acceptance Criteria: 1) Only one current decision is authoritative for a subject/policy scope.; 2) `REJECT` and `HOLD` structurally block publication.; 3) A stale or replayed review command cannot overwrite a newer decision.; 4) The deployment-specific rule for interactive versus automatic review is resolved and documented before publication is enabled.
  * Steps / Subtasks:
    * Define which harmless local outcomes may receive deterministic policy decisions and which publication classes require an attributed human or external authority.
    * Bind every decision to subject identity, evidence-set digest, policy ID/version/digest, actor type/ID, reason code/text, time, and predecessor when superseding.
    * Reject stale decision attempts if the evidence set, subject version, policy, or lifecycle version changed.
    * Expose a versioned review command through canonical `CommandService`; no plugin, model, event consumer, or destination adapter may write decisions directly.
  * Risks & Mitigations: Unresolved review classes could either burden harmless work with unnecessary approval or allow consequential publication without accountable authority. / Separate core decision mechanics from deployment policy and require A6 validation before enabling destinations..
  * Tags: [review] [decision] [policy] [authority] [p1]

* [ ] - T17.1.4 Implement staged idempotent publication and bidirectional lineage
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {REVIEW} {RECOVERY} {PROVENANCE} {SECURITY}
  * Dependencies: T17.1.2, T17.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].; Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31; ADR-009; GAP-011,GAP-015
  * Acceptance Criteria: 1) No publication begins without a current authorized `APPROVE` decision bound to the exact evidence set.; 2) Duplicate requests converge on one verified destination effect or a deterministic conflict.; 3) Unknown outcome is reconciled rather than blindly repeated.; 4) Every verified publication resolves bidirectionally to source root, intake generation, occurrence, exact content, derivations, findings, evidence, decision, actor, policy, and attempt.
  * Steps / Subtasks:
    * Validate a current `APPROVE` decision, exact evidence-set digest, subject content identity, destination policy, and adapter capability before creating an attempt.
    * Derive a stable idempotency key from publication request identity and persist it before any external side effect.
    * Stage destination content/metadata, commit with no-replace or explicit expected-replace semantics, then independently verify bytes and destination identity.
    * Record `SUCCEEDED`, `FAILED`, or `UNKNOWN/RECONCILIATION_REQUIRED`; never infer destination success from a request or transport acknowledgement.
    * Expose forward and reverse lineage queries from source occurrence/content through derived records to every verified publication.
  * Risks & Mitigations: External side effects can be duplicated or falsely reported as successful when timeout and destination state disagree. / Persist intent/idempotency first, stage and verify effects, and route unknown outcomes through deterministic reconciliation..
  * Tags: [publication] [idempotency] [review] [lineage] [p1]

## E18. Retry, timeout, idempotency, reconciliation, and crash recovery

Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.

* [ ] - T18.1.1 Define the error taxonomy and operation-semantics registry
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RECOVERY} {LIFECYCLE} {PLUGINS} {SECURITY}
  * Dependencies: T9.1.4, T15.1.4, T17.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.; Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27; ADR-011; R-08,R-09,R-11
  * Acceptance Criteria: 1) Every built-in operation has exactly one current, versioned semantics classification.; 2) Unknown/unregistered semantics block automatic retry.; 3) Error codes are stable, serializable, and safe for API/event/log projection.; 4) Policy can prove why an outcome is retryable, blocked, terminal, or requires reconciliation.
  * Steps / Subtasks:
    * Define error categories for validation, policy, input mutation, resource limit, timeout, cancellation, dependency, persistence, protocol, plugin, invariant, and unknown external outcome.
    * Classify each built-in operation as pure/restartable, checkpoint-resumable, idempotent side effect, externally reconcilable side effect, or non-retriable/manual.
    * Require operation semantics ID/version/digest in phase/plugin descriptors and persisted attempts.
    * Map legacy exceptions conservatively and preserve original causes without exposing secrets or raw payloads.
  * Risks & Mitigations: A generic retry flag can repeat unsafe side effects or hide the distinction between validation, exhaustion, and unknown external state. / Make error type and operation semantics explicit, versioned, policy-validated, and persisted with each attempt..
  * Tags: [errors] [operation-semantics] [recovery] [p1]

* [ ] - T18.1.2 Implement retry, deadline, timeout, and idempotency policy
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RECOVERY} {PERSISTENCE} {SECURITY} {OBSERVABILITY}
  * Dependencies: T18.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.; Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27; ADR-011; R-08,R-09,R-11
  * Acceptance Criteria: 1) Retry decisions are deterministic for the same durable state and policy version.; 2) No unsafe or unknown-outcome operation is automatically retried.; 3) Duplicate idempotency identity returns the prior canonical result or conflict rather than repeating an effect.; 4) Attempt/deadline/backoff state survives process restart.
  * Steps / Subtasks:
    * Define maximum attempts, bounded exponential backoff/jitter, total deadline, per-attempt timeout, retry budget, and dependency-specific circuit behavior.
    * Generate or validate idempotency keys from stable operation identity and immutable inputs before side effects.
    * Create a new attempt for every retry and link predecessor, reason, checkpoint, policy version, and next eligible time.
    * Ensure cancellation and pause requests take precedence at defined safe points and cannot be lost inside retry sleep.
  * Risks & Mitigations: Retries can create duplicate effects, storms, or irreproducible behavior if timing and identity are process-local. / Persist policy inputs and schedules, reserve idempotency before effects, and require reconciliation for ambiguous outcomes..
  * Tags: [retry] [timeout] [idempotency] [deadline] [p1]

* [ ] - T18.1.3 Implement startup reconciliation and deterministic recovery decisions
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RECOVERY} {LIFECYCLE} {PERSISTENCE} {OPERATIONS}
  * Dependencies: T18.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.; Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27; ADR-011; R-08,R-09,R-11
  * Acceptance Criteria: 1) Each nonterminal attempt maps to one persisted recovery disposition.; 2) Unsafe or insufficient evidence becomes `BLOCKED/RECONCILIATION_REQUIRED`, never guessed success.; 3) Repeated startup converges without duplicating the selected action.; 4) Recovery summary identifies exact job/phase/attempt/checkpoint/effect boundary and next operator action.
  * Steps / Subtasks:
    * Define startup scan order and snapshot/transaction boundaries so recovery does not race normal claims.
    * Validate checkpoint schema/config/input/content/attempt lineage before resuming.
    * Reconcile staged workspaces, orphan child processes where observable, outbox state, idempotency records, and external publication attempts.
    * Persist one `RecoveryDecision` with reason, evidence, policy/semantics version, and successor action before execution.
    * Conservatively block legacy nonterminal jobs whose safe continuation cannot be established.
  * Risks & Mitigations: A restart path can become a second orchestrator that advances state from stale or incomplete evidence. / Centralize recovery decisions, persist them before action, and keep coordinator/state guards authoritative..
  * Tags: [startup] [reconciliation] [recovery] [p1]

* [ ] - T18.1.4 Build the phase-by-phase crash and replay verification matrix
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RECOVERY} {RELEASE} {SECURITY} {EVIDENCE}
  * Dependencies: T18.1.2, T18.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.; Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27; ADR-011; R-08,R-09,R-11
  * Acceptance Criteria: 1) The matrix covers all built-in phases and every declared operation-semantics class.; 2) Each fault point produces exactly the documented recovery disposition across repeated clean runs.; 3) No unsafe side effect is repeated and no unknown outcome is reported as success.; 4) CI publishes machine-readable crash/replay evidence and blocks regressions for mandatory platforms.
  * Steps / Subtasks:
    * Enumerate fault points immediately before and after each authoritative transaction, filesystem commit, checkpoint, plugin launch/result, outbox write, and external publication boundary.
    * For each fault point define expected durable rows/files, allowed duplicate effects, recovery decision, cleanup, and retained evidence.
    * Run repeated restart and duplicate-delivery scenarios, not only one crash.
    * Produce machine-readable results tied to schema, code, fixture, platform, and operation-semantics versions.
  * Risks & Mitigations: Happy-path recovery tests may miss the exact before/after boundaries where duplicate effects and false success occur. / Enumerate durable fault points and require repeated, machine-readable, phase-specific crash/replay evidence..
  * Tags: [crash] [replay] [fault-injection] [recovery] [p1]

## E19. Long-running local runtime ownership

Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.

* [ ] - T19.1.1 Define the daemon lifecycle, configuration, and ownership contract
  * Priority: `P1`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {OPERATIONS} {LIFECYCLE} {SECURITY} {CONFIGURATION}
  * Dependencies: T5.1.4, T9.1.4, T18.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.; Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27; GAP-007; ADR-008
  * Acceptance Criteria: 1) Readiness is false until store, migration, recovery, and ownership checks succeed.; 2) Only one valid local owner can advance an attempt.; 3) Drain stops new claims while allowing documented safe completion/cancellation behavior.; 4) Embedded and daemon modes use identical lifecycle/state/policy services.
  * Steps / Subtasks:
    * Define states `STARTING`, `RECOVERING`, `READY`, `DRAINING`, `STOPPING`, `STOPPED`, and `FAILED` with deterministic readiness semantics.
    * Define one authoritative owner of job advancement per deployment and an explicit embedded-mode ownership contract for tests/library use.
    * Run migration/integrity/recovery checks before readiness and stop claiming work during drain.
    * Define local IPC or database-mediated command access without opening a network listener by default.
  * Risks & Mitigations: A daemon can create a second execution authority or make foreground mode behavior diverge. / Define one ownership contract and reuse the same coordinator, state guards, command service, and recovery path..
  * Tags: [daemon] [runtime-owner] [service] [p1]

* [ ] - T19.1.2 Implement durable claims, leases, heartbeats, and fenced execution
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {LIFECYCLE} {PERSISTENCE} {SECURITY} {RECOVERY}
  * Dependencies: T19.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.; Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27; GAP-007; ADR-008
  * Acceptance Criteria: 1) Two daemons cannot validly own or commit the same attempt.; 2) A lost lease immediately removes authority at the next guarded boundary.; 3) Stale results are rejected and retained as diagnostic evidence.; 4) Claim recovery follows operation semantics and never blindly re-executes an unknown effect.
  * Steps / Subtasks:
    * Select runnable jobs with deterministic ordering and transactionally acquire one claim with monotonic fencing generation.
    * Renew before expiry, stop authority on failed renewal, and persist release/expiry reasons.
    * Require claim and attempt fencing tokens at every authoritative transition and side-effect result commit.
    * Recover expired claims only after operation-specific reconciliation; never steal an active unknown effect.
  * Risks & Mitigations: Lease loss without commit fencing permits duplicate or stale processes to advance authoritative state. / Use monotonic fencing generations on every state/effect boundary and reconcile expired work before succession..
  * Tags: [claims] [leases] [fencing] [daemon] [p1]

* [ ] - T19.1.3 Route CLI and Python controls through canonical command and status services
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {API} {COMPATIBILITY} {LIFECYCLE} {SECURITY}
  * Dependencies: T19.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.; Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27; GAP-007; ADR-008
  * Acceptance Criteria: 1) A separate CLI process can control a daemon-owned job without private runtime mutation.; 2) Equivalent CLI/Python commands produce identical persisted command and lifecycle results.; 3) Replayed or stale commands return deterministic prior result/conflict.; 4) Compatibility behavior and deprecation window are documented and tested.
  * Steps / Subtasks:
    * Define versioned commands with actor, idempotency key, expected state/version, reason, and request/correlation IDs.
    * Persist command acceptance/rejection and let the daemon/coordinator apply controls at valid state/safe-point boundaries.
    * Preserve existing CLI verbs through a compatibility window; add explicit foreground/daemon connection behavior.
    * Remove access to private `_jobs` or orchestrator handler maps from CLI and public Python surfaces.
  * Risks & Mitigations: Multiple client paths can recreate alternate state mutation logic or silently change CLI behavior. / Make clients thin adapters over one validated command/status boundary and retain dual-support tests..
  * Tags: [command-service] [status-service] [cli] [python-api] [p1]

* [ ] - T19.1.4 Verify graceful shutdown, forced restart, and orphan containment
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {OPERATIONS} {RECOVERY} {SECURITY} {RELEASE}
  * Dependencies: T19.1.2, T19.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.; Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27; GAP-007; ADR-008
  * Acceptance Criteria: 1) Graceful stop leaves no new claims and records deterministic terminal/suspended/checkpoint state.; 2) Forced restart fences the old owner and produces one recovery decision per nonterminal attempt.; 3) Orphan handling cannot terminate an unrelated process.; 4) Runbook and tests cover foreground rollback for new jobs without stealing existing daemon-owned work.
  * Steps / Subtasks:
    * Define graceful shutdown phases, deadlines, safe-point behavior, subprocess termination, checkpoint flush, and claim release.
    * On forced restart, run fencing and recovery before accepting new commands/work.
    * Detect or reconcile orphan subprocesses/workspaces using attempt ownership and platform-supported process identity.
    * Produce a startup/shutdown recovery report with blocked items and operator actions.
  * Risks & Mitigations: Shutdown cleanup can lose evidence, release authority too early, or kill unrelated processes. / Use staged drain/fencing/recovery and bind process cleanup to durable attempt identity..
  * Tags: [shutdown] [restart] [orphan] [runbook] [p1]

## E20. Canonical status, telemetry, health, and diagnostics

Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.

* [ ] - T20.1.1 Define structured logging, correlation, error catalog, and redaction
  * Priority: `P1`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {OBSERVABILITY} {SECURITY} {LIFECYCLE} {COMPATIBILITY}
  * Dependencies: T8.1.4, T9.1.4, T18.1.4, T19.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.; Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27; R-15
  * Acceptance Criteria: 1) Every major lifecycle, control, recovery, policy, and publication action has a stable code and correlation chain.; 2) Redaction occurs before every configured sink and diagnostic export.; 3) Telemetry sink failure cannot change job state or result.; 4) Golden log schema is versioned and compatibility-tested.
  * Steps / Subtasks:
    * Define a versioned log envelope with time, severity, code, message template, correlation/job/phase/attempt/work/control/event/request IDs, component, and bounded attributes.
    * Propagate context explicitly across async tasks, subprocess boundaries, outbox dispatch, and command requests.
    * Classify fields as safe, hashed/minimized, secret, content-derived, or prohibited; redact before serialization.
    * Define sink failure/backpressure behavior and ensure logging cannot fail authoritative transitions.
  * Risks & Mitigations: Observability can become a data-exfiltration path or a second inconsistent account of lifecycle truth. / Use typed bounded records, redact before sinks, and derive status from authoritative state instead of logs..
  * Tags: [logging] [errors] [redaction] [correlation] [p1]

* [ ] - T20.1.2 Implement bounded metrics and optional distributed tracing
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {OBSERVABILITY} {PERFORMANCE} {SECURITY} {OPERATIONS}
  * Dependencies: T20.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.; Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27; R-15
  * Acceptance Criteria: 1) Metric names, units, label sets, and bounds are documented and schema-tested.; 2) No mandatory lifecycle path depends on exporter success.; 3) Load tests demonstrate bounded cardinality and memory use for representative workloads.; 4) Trace removal/no-op mode leaves persisted semantics identical.
  * Steps / Subtasks:
    * Define a stable metric catalog for lifecycle states, phase/operation duration, throughput, bytes/entries, budgets, retries, checkpoints, claims, outbox, publications, and failures.
    * Allow only bounded labels such as phase, operation class, backend, result, and stable error code; never raw artifact IDs or paths by default.
    * Create optional traces linking command, coordinator, work item, backend, event, and publication spans through correlation IDs.
    * Document sampling, aggregation, clock, and retention limitations and keep durable evidence independent.
  * Risks & Mitigations: Unbounded telemetry labels can exhaust memory/storage and leak artifact identity. / Use a closed bounded catalog and keep high-cardinality detail in authorized status/evidence queries..
  * Tags: [metrics] [tracing] [cardinality] [p1]

* [ ] - T20.1.3 Build the canonical versioned job status projection
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {OBSERVABILITY} {PERSISTENCE} {API} {COMPATIBILITY}
  * Dependencies: T20.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.; Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27; R-15
  * Acceptance Criteria: 1) An operator can identify exact current phase, attempt, checkpoint, control, blocker, retry/recovery action, and provenance completeness without raw DB access.; 2) Status is rebuildable from authoritative state and events are supplemental only.; 3) Legacy/partial/corrupt fields are explicit and never mistaken for complete.; 4) Query performance and pagination are measured on representative large jobs.
  * Steps / Subtasks:
    * Define status fields and authority source for job/phase/attempt/work, progress numerator/denominator, pending control, checkpoint age, claim/lease, retry, blocker, budget, outbox backlog, provenance completeness, and publication state.
    * Read from a consistent StateStore transaction/snapshot and mark unavailable/corrupt/legacy fields explicitly.
    * Define stable pagination, filtering, ordering, and optional incremental sequence cursor.
    * Keep projection rebuildable; never write lifecycle state from status code.
  * Risks & Mitigations: A convenience status cache can become an alternate authority or hide missing provenance behind optimistic defaults. / Make the projection read-only, versioned, source-attributed, rebuildable, and explicit about degradation..
  * Tags: [status] [projection] [progress] [p1]

* [ ] - T20.1.4 Implement health, readiness, and sanitized diagnostic bundles
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {OBSERVABILITY} {OPERATIONS} {SECURITY} {EVIDENCE}
  * Dependencies: T20.1.2, T20.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.; Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27; R-15
  * Acceptance Criteria: 1) Health/readiness results are deterministic and identify each failed dependency/control.; 2) Diagnostic bundle verifies against its manifest and records all omissions/degraded collectors.; 3) Synthetic secret/raw-content tests find no prohibited data.; 4) Bundle failure cannot mutate lifecycle state or overwrite an existing file.
  * Steps / Subtasks:
    * Separate liveness from readiness and dependency degradation; define exact reason codes and recovery guidance.
    * Include schema/config/runtime/plugin versions, sanitized status, recent stable error codes, migration/integrity state, resource summary, and selected evidence references.
    * Create a bundle manifest with file sizes, schema versions, SHA-256 hashes, omissions, and redaction policy version.
    * Bound time, size, rows, and path samples; permit partial bundle with explicit missing-component records.
  * Risks & Mitigations: Diagnostic collection can leak sensitive artifacts or make a degraded service appear ready. / Use explicit health semantics, allowlisted bounded collectors, pre-write redaction, secure no-replace output, and an integrity manifest..
  * Tags: [health] [readiness] [diagnostics] [redaction] [p1]

## E21. Versioned external command and event adapters

Expose REST, RabbitMQ, and webhook surfaces only as adapters over canonical command, status, and durable event contracts.

* [ ] - T21.1.1 Define versioned external command, status, and error schemas
  * Priority: `P2`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {API} {COMPATIBILITY} {SECURITY} {LIFECYCLE}
  * Dependencies: T8.1.4, T19.1.4, T20.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.; Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27; GAP-006; ADR-004
  * Acceptance Criteria: 1) Equivalent local and external contracts produce identical authoritative command outcomes.; 2) No request field can directly set job/phase/attempt state, fencing, policy result, or publication success.; 3) Replay/stale/version conflicts are deterministic and machine-readable.; 4) Schemas and examples are generated or CI-checked against implementation.
  * Steps / Subtasks:
    * Define submit, pause, resume, cancel, retry, reconcile, review, and publication command bodies with request ID, idempotency key, actor, expected state/version, reason, and typed payload.
    * Define stable success, accepted/pending, conflict, validation, policy, unavailable, and internal error responses.
    * Define schema/version negotiation and additive/deprecation rules; reject unknown major versions and ambiguous duplicate fields.
    * Map every contract to the same `CommandService`/`StatusService` used by local clients.
  * Risks & Mitigations: Transport-specific schemas can smuggle alternate state mutation or drift from CLI/Python semantics. / Define transport-neutral contracts and map all clients through the same canonical services and guards..
  * Tags: [contracts] [commands] [status] [api-v1] [p2]

* [ ] - T21.1.2 Implement REST v1 and generate the OpenAPI contract
  * Priority: `P2`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {API} {SECURITY} {OBSERVABILITY} {COMPATIBILITY}
  * Dependencies: T21.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.; Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27; GAP-006; ADR-004
  * Acceptance Criteria: 1) REST and CLI/Python commands converge on the same persisted result for equivalent requests.; 2) OpenAPI is versioned, complete for implemented endpoints, and fails CI on drift.; 3) Client disconnect/retry cannot duplicate authoritative effects.; 4) Disabling/removing REST leaves core job execution and status semantics unchanged.
  * Steps / Subtasks:
    * Expose bounded endpoints for command submission/results, job list/status, events/evidence/lineage reads, health/readiness, and API schema.
    * Use canonical error objects, request/correlation IDs, idempotency, conditional expected-version/ETag semantics, pagination, and content negotiation.
    * Keep server startup/configuration optional and disabled by default for local library/CLI use.
    * Generate OpenAPI from contracts or verify it bidirectionally in CI, including examples and error cases.
  * Risks & Mitigations: A network API can accidentally become a second coordinator or expose unsafe local assumptions. / Keep it an optional thin adapter, require deployment controls for exposure, and test semantic equivalence and retries..
  * Tags: [rest] [openapi] [adapter] [p2]

* [ ] - T21.1.3 Implement outbox-backed RabbitMQ event delivery
  * Priority: `P2`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVENTS} {API} {RECOVERY} {SECURITY}
  * Dependencies: T21.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.; Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27; GAP-006; ADR-004
  * Acceptance Criteria: 1) Broker outage cannot roll back or falsely fail an already committed lifecycle transition.; 2) Delivery retries are bounded and duplicate event IDs/sequences support idempotent consumers.; 3) No replayed event can mutate lifecycle state.; 4) Legacy routing and new envelopes have a tested compatibility/deprecation path.
  * Steps / Subtasks:
    * Read committed outbox rows in sequence, publish canonical event envelope and headers, wait for publisher confirm, then persist delivery state.
    * Define bounded retry/dead-letter terminal status, broker topology declarations, message TTL/size, and consumer offset/replay guidance.
    * Preserve legacy routing keys through a versioned compatibility adapter and publish deprecation telemetry.
    * Keep lifecycle state and event history authoritative in StateStore even when broker is unavailable.
  * Risks & Mitigations: Treating the broker as authoritative can lose transitions, block local execution, or let event consumers mutate state. / Drive transport only from committed outbox rows and require all commands to re-enter canonical validation..
  * Tags: [rabbitmq] [outbox] [events] [p2]

* [ ] - T21.1.4 Implement signed idempotent webhook notifications
  * Priority: `P2`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EVENTS} {SECURITY} {API} {RECOVERY}
  * Dependencies: T21.1.2, T21.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.; Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27; GAP-006; ADR-004
  * Acceptance Criteria: 1) Receivers can verify authenticity, schema version, event identity, and replay window.; 2) Duplicate delivery is expected and safely identifiable.; 3) Webhook failure never changes lifecycle state or loses durable event history.; 4) SSRF/redirect/rebinding tests demonstrate deployment-policy enforcement.
  * Steps / Subtasks:
    * Define explicit event subscriptions, endpoint policy, schema version, signing key reference, timeout, retry/dead-letter, and disable controls.
    * Sign canonical body plus event ID/sequence/time/version and expose a stable delivery ID for receiver idempotency.
    * Persist attempt before request and store bounded response metadata; never store arbitrary response bodies.
    * Treat 2xx as transport acknowledgement only; it cannot alter ATLAS lifecycle state.
  * Risks & Mitigations: Outbound webhooks can become an SSRF and secret-leak path or be mistaken for authoritative acknowledgements. / Use strict endpoint policy, signed idempotent notifications, bounded transport, and explicit non-authoritative semantics..
  * Tags: [webhooks] [signatures] [notifications] [p2]

## E22. Subprocess plugin isolation and enforceable resource controls

Run untrusted or high-risk plugins outside the core process with mediated inputs, explicit capabilities, bounded resources, deterministic termination, and visible platform limitations.

* [ ] - T22.1.1 Define the subprocess protocol and mediated artifact contract
  * Priority: `P2`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {PLUGINS} {SECURITY} {COMPATIBILITY}
  * Dependencies: T14.1.4, T15.1.4, T16.1.4, T18.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.; Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27; ADR-010; GAP-014
  * Acceptance Criteria: 1) Subprocess cannot receive StateStore credentials or undeclared source/workspace paths through the protocol/environment.; 2) Malformed or forged protocol messages fail the attempt without lifecycle mutation.; 3) Equivalent trusted plugin results normalize identically in in-process and subprocess backends.; 4) Protocol compatibility and capability negotiation are versioned and tested.
  * Steps / Subtasks:
    * Define protocol major/minor version, plugin identity/digest, operation, inputs, grants, budgets, deadline, attempt/fencing context, progress, result, evidence, and errors.
    * Use length-delimited or equivalent framing with strict size/encoding/order rules; reject extra/ambiguous/duplicate fields according to version policy.
    * Provide read-only mediated content handles/copies and an attempt-owned output workspace; never expose StateStore credentials or unrestricted source paths.
    * Validate all output through the same typed analyzer/phase contracts before persistence.
  * Risks & Mitigations: A loose IPC contract can expose internal authority or permit malformed plugin output to mutate state. / Use a minimal typed protocol, mediated immutable inputs, strict validation, and coordinator-owned persistence..
  * Tags: [subprocess] [protocol] [mediated-artifacts] [p2]

* [ ] - T22.1.2 Implement deterministic process lifecycle, timeout, and tree termination
  * Priority: `P2`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {RECOVERY} {SECURITY} {OPERATIONS}
  * Dependencies: T22.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.; Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27; ADR-010; GAP-014
  * Acceptance Criteria: 1) Timeout/cancel kills and reaps the entire controlled process tree on supported platforms.; 2) Late or stale results cannot commit after fencing/cancellation.; 3) Unsupported containment controls are explicit in status and release evidence.; 4) No zombie, leaked handle, or unbounded output remains after hostile fixtures.
  * Steps / Subtasks:
    * Launch in a dedicated process group/session or platform job object and record robust process identity with attempt.
    * Enforce handshake/start/idle/total deadlines, cancellation, graceful termination grace, forced tree kill, wait/reap, and deterministic outcome mapping.
    * Bound stdout, stderr, protocol, child count, open handles, and retained diagnostics; truncate with explicit evidence.
    * On restart, never kill by PID alone; reconcile platform process identity and fenced attempt ownership.
  * Risks & Mitigations: A timed-out parent may leave descendants running or a restart may kill an unrelated reused PID. / Use platform process containers, robust identity, fenced attempts, bounded termination escalation, and explicit reduced-assurance reporting..
  * Tags: [process-supervisor] [timeout] [tree-kill] [p2]

* [ ] - T22.1.3 Enforce subprocess resource, network, tool, and secret policy
  * Priority: `P2`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {EXECUTION} {SECURITY} {PERFORMANCE} {PLUGINS}
  * Dependencies: T22.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.; Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27; ADR-010; GAP-014
  * Acceptance Criteria: 1) Each subprocess attempt records requested, enforced, unavailable, and exceeded controls plus measured usage.; 2) Network/tools/secrets are absent unless explicitly granted by deterministic policy.; 3) Required unavailable controls block untrusted execution rather than silently weakening policy.; 4) Tool and command-injection tests show no shell interpretation of plugin-controlled values.
  * Steps / Subtasks:
    * Enforce or monitor wall time, CPU, memory, process/thread count, file descriptors, output bytes, workspace/temp bytes, and opened files.
    * Deny network and external tools by default; grant allowlisted endpoints/tools with resolved immutable executable identity and arguments contract.
    * Provide secrets only through explicit short-lived references/channels and never general environment inheritance.
    * Record each control as enforced, monitored-only, unavailable, or not requested and feed actual usage to `ResourceBudgetManager`.
  * Risks & Mitigations: Cross-platform resource controls are uneven, creating false isolation claims or escape through tools/network/secrets. / Track enforcement state per control, default deny capabilities, and block untrusted execution when mandatory controls are unavailable..
  * Tags: [resource-limits] [capabilities] [network] [secrets] [p2]

* [ ] - T22.1.4 Establish hostile-plugin and backend conformance gates
  * Priority: `P2`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RELEASE} {SECURITY} {EXECUTION} {EVIDENCE}
  * Dependencies: T22.1.2, T22.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.; Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27; ADR-010; GAP-014
  * Acceptance Criteria: 1) Every supported platform has a current pass/fail/reduced-assurance enforcement matrix.; 2) Hostile fixtures cannot commit lifecycle state or escape mediated inputs under claimed controls.; 3) Cleanup and resource-accounting assertions pass after every failure class.; 4) No unsupported control is marketed as enforced and no mandatory isolation test is silently skipped.
  * Steps / Subtasks:
    * Define benign reference plugins and one synthetic fixture for every declared threat/failure mode.
    * Run in-process only for trusted fixtures and subprocess for hostile/untrusted cases; compare normalized valid results.
    * Verify workspace containment, process cleanup, budget metrics, denied grants, error taxonomy, checkpoint/recovery, and status evidence.
    * Publish a versioned enforcement report tied to OS/kernel/runtime, plugin digest, and test suite.
  * Risks & Mitigations: Isolation can be declared complete from architecture alone while platform-specific escapes and cleanup failures remain untested. / Require an adversarial, versioned, per-platform conformance report and fail closed on unverified mandatory controls..
  * Tags: [hostile-plugin] [conformance] [ci-gate] [p2]

## E23. Retention, compatibility, plugin SDK, and source-provider evolution

Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.

* [ ] - T23.1.1 Define retention classes and implement reference-safe cleanup
  * Priority: `P2`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {OPERATIONS} {STORAGE} {PROVENANCE} {SECURITY}
  * Dependencies: T12.1.4, T17.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28; REQ-021,REQ-023,REQ-029; ADR-012
  * Acceptance Criteria: 1) Retention periods and required preserved classes are explicitly resolved and versioned before deletion is enabled.; 2) Dry-run and execution use the same immutable plan or fail on changed preconditions.; 3) No referenced, held, active, or unknown-ownership object is deleted.; 4) Interrupted cleanup is idempotently reconciled with durable per-object evidence.
  * Steps / Subtasks:
    * Classify lifecycle records, events/outbox, content blobs, quarantine/workspaces, checkpoints, plugin outputs, diagnostics, and telemetry by minimum retention and replay/lineage dependency.
    * Compute deletion eligibility from reference graph, current/nonterminal state, holds, publication lineage, backup policy, and configured retention version.
    * Require dry-run plan with counts/bytes/reasons, explicit confirmation/policy for consequential deletion, then no-follow/no-replace safe execution and post-delete verification.
    * Persist tombstone and cleanup evidence without retaining prohibited content; support interrupted-run reconciliation.
  * Risks & Mitigations: Cleanup can irreversibly destroy provenance, recovery data, or published-content lineage. / Resolve policy first, plan immutably, recheck references/holds, use managed identities, and persist verifiable deletion evidence..
  * Tags: [retention] [garbage-collection] [cleanup] [p2]

* [ ] - T23.1.2 Implement the compatibility catalog and deprecation telemetry
  * Priority: `P2`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {COMPATIBILITY} {ARCHITECTURE} {OBSERVABILITY} {RELEASE}
  * Dependencies: T3.1.4, T4.1.4, T8.1.4, T14.1.4, T18.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28; REQ-021,REQ-023,REQ-029; ADR-012
  * Acceptance Criteria: 1) Every persisted/public contract has one catalog entry and explicit read/write/deprecation policy.; 2) Unsupported or lossy authority-bearing conversions fail closed with actionable status.; 3) Compatibility reports identify affected records/plugins/configurations before upgrade.; 4) Deprecation removal requires evidence that migration and rollback gates passed.
  * Steps / Subtasks:
    * Register database, config, pipeline, event, plugin, finding/evidence, checkpoint, protocol, API, and manifest schemas with current/read/write ranges.
    * Require an explicit translator or hard incompatibility; never best-effort unknown-field guessing for authority-bearing records.
    * Record original version/digest, translator chain, output version/digest, warnings, and lossiness.
    * Emit bounded deprecation telemetry and operator reports before write support is removed.
  * Risks & Mitigations: Scattered version checks create ambiguous behavior, silent data loss, and unsafe downgrade paths. / Use one catalog with explicit translators, lossiness policy, provenance, and release-gated deprecation..
  * Tags: [compatibility] [schema] [deprecation] [p2]

* [ ] - T23.1.3 Deliver the plugin SDK, fixtures, and contract-validation CLI
  * Priority: `P2`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {DX} {PLUGINS} {COMPATIBILITY} {SECURITY}
  * Dependencies: T14.1.4, T15.1.4, T22.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28; REQ-021,REQ-023,REQ-029; ADR-012
  * Acceptance Criteria: 1) A third party can implement and validate a plugin without importing private runtime/persistence APIs.; 2) Contract CLI reports exact failed section, capability, compatibility, and remediation guidance.; 3) Examples pass the same registry/backend conformance tests as built-ins.; 4) Untrusted validation cannot mutate lifecycle state or access undeclared resources.
  * Steps / Subtasks:
    * Package only public contracts needed by plugin authors; keep StateStore/coordinator/internal repositories inaccessible.
    * Provide fixture builders for content identities, structural reports, extracted artifacts, findings, budgets, cancellation, checkpoints, and errors.
    * Validate descriptor/schema/version/capabilities/tools/network/resources/timeout/risk and run deterministic contract tests.
    * Generate a machine-readable compatibility and capability report suitable for CI and registry admission.
  * Risks & Mitigations: A difficult SDK encourages plugins to depend on private internals, weakening compatibility and authority boundaries. / Expose a narrow tested public SDK and make contract/capability validation easy and deterministic..
  * Tags: [plugin-sdk] [developer-experience] [contracts] [p2]

* [ ] - T23.1.4 Define the source-provider extension contract and defer unsupported providers
  * Priority: `P2`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {INTAKE} {PLUGINS} {SECURITY} {COMPATIBILITY}
  * Dependencies: T6.1.4, T10.1.4, T14.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.; This is a planning decomposition/new support capability, not a claim that the current repository implements it.; source mapping: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28; REQ-021,REQ-023,REQ-029; ADR-012
  * Acceptance Criteria: 1) Local provider passes the contract without changing accepted local semantics.; 2) Any provider lacking stable observation/mutation semantics is rejected or explicitly reduced-assurance, not silently accepted.; 3) Deferred providers are named as non-implemented and have measurable admission criteria.; 4) Provider removal leaves persisted source/intake/occurrence/content records readable.
  * Steps / Subtasks:
    * Define provider-neutral `SourceRoot` locator/config digest, observation cursor/snapshot token, occurrence locator, metadata, safe open, mutation detection, and unavailable/changed behavior.
    * Require providers to produce immutable accepted `IntakeGeneration` manifests and exact bytes for content identity; providers cannot skip A–F phases.
    * Separate provider credentials/auth from artifact identity and store only secret references.
    * Document object storage, HTTP, repository, stream, and removable-media providers as deferred until a concrete requirement and consistency model exist.
  * Risks & Mitigations: Premature remote-provider implementation can redefine snapshot and identity semantics or add network trust to the core. / Specify the semantic contract, prove it with local sources, and require concrete evidence before implementing additional providers..
  * Tags: [source-provider] [registry] [defer] [p2]

## E24. Continuous quality, packaging, benchmarks, and release evidence

Make every release claim traceable to clean builds, mandatory test families, security and compatibility evidence, representative benchmarks, and a practiced rollback.

* [ ] - T24.1.1 Define the supported-platform matrix and mandatory CI policy
  * Priority: `P1`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RELEASE} {COMPATIBILITY} {SECURITY} {EVIDENCE}
  * Dependencies: T2.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.; Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28; R-16; ATLAS:.github/workflows/tests.yml:L1-L34 (frozen assessment citation)
  * Acceptance Criteria: 1) Supported and reduced-assurance platforms are explicitly resolved and versioned.; 2) Every mandatory job blocks release and unapproved skips fail policy.; 3) CI reports what is not covered and does not use blanket production-ready claims.; 4) Clean reruns preserve deterministic configuration and evidence metadata.
  * Steps / Subtasks:
    * Resolve and document supported Python versions, Linux/macOS/Windows scope, filesystems, architectures, and subprocess/resource-control assurance.
    * Define mandatory formatter, linter, type checker, unit, integration, schema/migration, docs/link, packaging, and security baseline jobs.
    * Require any skip/allowed failure to include owner, reason, issue, expiry, and release-impact marker.
    * Retain machine-readable job status, tool versions, commit, fixture/catalog versions, and coverage boundaries.
  * Risks & Mitigations: An undefined support matrix can turn skipped platform controls into misleading release claims. / Resolve support explicitly, make gates mandatory by policy, and publish reduced-assurance limitations..
  * Tags: [ci] [platform-matrix] [quality-gates] [p1]

* [ ] - T24.1.2 Add state-machine, migration, crash, adversarial, compatibility, and fuzz gates
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RELEASE} {RECOVERY} {SECURITY} {COMPATIBILITY}
  * Dependencies: T5.1.4, T11.1.4, T18.1.4, T22.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.; Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28; R-16; ATLAS:.github/workflows/tests.yml:L1-L34 (frozen assessment citation)
  * Acceptance Criteria: 1) Each major lifecycle/safety/recovery contract has an assigned mandatory test family and CI job.; 2) Regression fixtures are deterministic, licensed/provenanced, bounded, and sanitized.; 3) No unapproved skip or flaky quarantine permits release.; 4) Failures produce actionable minimized evidence without leaking sensitive input.
  * Steps / Subtasks:
    * Run state-machine/model, property, migration forward/rollback, crash/restart, replay/idempotency, concurrency, malformed input, archive, plugin isolation, compatibility, and security regression tests.
    * Define fixture schema, origin/license/sensitivity, expected oracle, bounds, deterministic seed, and minimization/retention.
    * Use time/resource limits and quarantine for fuzz/crash jobs; retain minimized regressions.
    * Map every P0/P1 capability to required test jobs and completion evidence.
  * Risks & Mitigations: Passing unit tests can mask transition, recovery, parser, concurrency, and migration failures that only appear under faults. / Make risk-mapped non-happy-path suites first-class mandatory release gates..
  * Tags: [property-tests] [fuzz] [adversarial] [migration] [p1]

* [ ] - T24.1.3 Produce reproducible packages, SBOMs, provenance, and integrity manifests
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {RELEASE} {SECURITY} {PROVENANCE} {COMPATIBILITY}
  * Dependencies: T24.1.1, T4.1.4, T23.1.2
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.; Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28; R-16; ATLAS:.github/workflows/tests.yml:L1-L34 (frozen assessment citation)
  * Acceptance Criteria: 1) Clean wheel/sdist install and smoke tests pass with recorded tool/dependency versions.; 2) Release bundle includes hashes, SBOM, license, provenance, security/dependency report, and coverage limitations.; 3) Reproducibility comparison is automated and any variance is documented and bounded.; 4) Publishing cannot proceed if integrity/provenance or mandatory tests fail.
  * Steps / Subtasks:
    * Define lock/pin strategy for runtime, build, dev, and optional extras and verify dependency resolution from a clean environment.
    * Build sdist/wheel at least twice in isolated clean environments and compare normalized outputs/hashes; explain unavoidable variance.
    * Generate SBOM, license inventory, package/source provenance, dependency/advisory report, checksums, and optional signatures/attestations under explicit policy.
    * Install wheel into a clean environment and run CLI/Python/schema/migration/smoke end-to-end checks.
  * Risks & Mitigations: A green source test suite does not prove that the shipped wheel is complete, reproducible, untampered, or license-compliant. / Build clean artifacts, verify installed behavior, and bind release evidence and hashes to the exact source/toolchain..
  * Tags: [packaging] [sbom] [provenance] [reproducible-build] [p1]

* [ ] - T24.1.4 Build representative benchmarks, soak tests, and release rollback evidence
  * Priority: `P1`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {PERFORMANCE} {RELEASE} {RECOVERY} {OPERATIONS}
  * Dependencies: T24.1.2, T24.1.3, T23.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.; Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28; R-16; ATLAS:.github/workflows/tests.yml:L1-L34 (frozen assessment citation)
  * Acceptance Criteria: 1) Every performance claim names workload, environment, metric, raw evidence, and confidence/limitation.; 2) Semantic and integrity tests run alongside benchmark optimizations.; 3) Release bundle contains mandatory test reports, benchmark raw data, migration/restore/rollback evidence, hashes, and operator notes.; 4) A failed mandatory gate or rollback drill blocks release.
  * Steps / Subtasks:
    * Benchmark thousands of small files, millions of entries, multi-gigabyte files, large/deep archives, duplicate-heavy reruns, concurrent jobs, expensive analyzers, subprocesses, and later adapters.
    * Record hardware/OS/filesystem/Python/config/schema/plugin/fixture versions, warm/cold cache, repetitions, raw samples, confidence/noise, and failures.
    * Measure throughput, latency, CPU, memory, I/O, database lock time, temp/storage, event volume/backlog, recovery time, dedup/reuse, and operator interventions.
    * Define regression comparison and scale-adapter trigger reports without inventing arbitrary universal thresholds.
    * Practice application/schema/content backup and rollback on a release candidate and retain the signed-off evidence bundle.
  * Risks & Mitigations: Unqualified performance claims and unpracticed rollback can drive premature scale architecture or unsafe releases. / Use reproducible workload-specific evidence, preserve raw results, and make rollback a tested release gate..
  * Tags: [benchmarks] [soak] [rollback] [release-evidence] [p1]

## E25. Measured optional PostgreSQL and object-storage adapters

Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.

* [ ] - T25.1.1 Define and approve quantitative scale-adapter trigger evidence
  * Priority: `P3`
  * Est. Effort: `12h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SCALE} {PERFORMANCE} {EVIDENCE} {ARCHITECTURE}
  * Dependencies: T4.1.4, T12.1.4, T18.1.4, T24.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.; Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27; ADR-003; OQ-007
  * Acceptance Criteria: 1) Trigger criteria, measurement procedure, and decision authority are resolved and versioned.; 2) Raw evidence demonstrates a specific local limitation and the proposed adapter addresses it.; 3) Simpler local optimizations are tested or explicitly rejected with evidence.; 4) A no-go result keeps adapter tasks deferred without being treated as failure.
  * Steps / Subtasks:
    * Define candidate triggers: write/read contention, dataset/row/blob size, recovery objective, multi-host coordination, storage durability/availability, operational backup, and lifecycle cost.
    * Benchmark/soak the local backends under the actual target workload and identify the bottleneck with raw evidence.
    * Compare logic/index/batching/checkpoint/retention improvements before infrastructure replacement.
    * Record selected/no-go decision, expected measurable benefit, complexity/operational cost, compatibility, migration, rollback, and disproof criteria.
  * Risks & Mitigations: Premature infrastructure can increase failure surface and operations without solving the measured bottleneck. / Make implementation contingent on reproducible trigger evidence and a falsifiable decision record..
  * Tags: [scale-trigger] [benchmark] [decision] [p3]

* [ ] - T25.1.2 Finalize backend conformance and one-authority migration contracts
  * Priority: `P3`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SCALE} {PERSISTENCE} {STORAGE} {RECOVERY}
  * Dependencies: T25.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.; Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27; ADR-003; OQ-007
  * Acceptance Criteria: 1) Conformance suites are backend-neutral and pass for SQLite/local content before alternate implementation.; 2) Migration protocol makes writable authority explicit and prevents dual writers.; 3) Verification manifest covers all authority-bearing rows/blobs and lineage.; 4) Rollback feasibility and cutoff are explicit before cutover.
  * Steps / Subtasks:
    * Define exact StateStore isolation/transaction/constraint/sequence/locking/time semantics and ContentStore integrity/read-after-write/list/delete semantics.
    * Define source and target schema/provider version compatibility, snapshot/copy strategy, verification manifest, maintenance/read-only window, and authority marker.
    * Require one writable authoritative backend at a time; shadow copies remain non-authoritative until verified cutover.
    * Define rollback preconditions after new writes and how copied/unknown objects are retained/reconciled.
  * Risks & Mitigations: Adapter abstractions can hide weaker consistency or enable simultaneous writable backends. / Define observable conformance and a fail-closed one-authority migration protocol before coding adapters..
  * Tags: [conformance] [migration] [single-authority] [p3]

* [ ] - T25.1.3 Implement and validate the optional PostgreSQL StateStore
  * Priority: `P3`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SCALE} {PERSISTENCE} {RECOVERY} {SECURITY}
  * Dependencies: T25.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.; Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27; ADR-003; OQ-007
  * Acceptance Criteria: 1) PostgreSQL passes the same StateStore, state-machine, crash, event, claim, idempotency, migration, and status tests as SQLite.; 2) Cutover/rollback drill preserves counts, identities, constraints, sequence, event order, and hashes.; 3) One writable backend authority is enforced at startup and during migration.; 4) Measured workload shows the approved benefit without changing lifecycle semantics.
  * Steps / Subtasks:
    * Implement transactions, guarded transitions, sequence allocation, outbox, claims/leases/fencing, idempotency, checkpoints, lineage queries, and migration locks under documented isolation.
    * Use bounded connection pool/lifecycle, timeouts, cancellation, retryable transaction handling, and health/readiness.
    * Implement SQLite-to-PostgreSQL snapshot/copy/verify/cutover tooling using the one-authority contract.
    * Document backup/restore, maintenance, upgrades, operational dependencies, and rollback cutoff.
  * Risks & Mitigations: Database semantics, failover, and connection behavior can subtly change transition atomicity and recovery. / Run unchanged conformance/differential suites and perform verified one-authority cutover/rollback drills..
  * Tags: [postgresql] [state-store] [migration] [p3]

* [ ] - T25.1.4 Implement and validate the optional object-backed ContentStore
  * Priority: `P3`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SCALE} {STORAGE} {IDENTITY} {SECURITY}
  * Dependencies: T25.1.2, T25.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.; Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27; ADR-003; OQ-007
  * Acceptance Criteria: 1) Object backend passes immutable ContentStore, integrity, reference, retention, recovery, and replay tests.; 2) No-replace commit and byte verification prevent canonical-key corruption.; 3) Migration/cutover/rollback preserves all referenced content hashes and one writable authority.; 4) Approved workload demonstrates benefit and provider consistency limitations are explicit.
  * Steps / Subtasks:
    * Stage uploads under attempt identity, stream/hash/size verify, commit immutable canonical key, verify visibility/metadata/bytes, and record provider object version/etag as supplemental.
    * Handle provider consistency by explicit read/verify/retry rules without treating ETag/path as canonical content identity.
    * Implement resumable copy manifest, reference validation, retention/holds, orphan reconciliation, and local-to-object cutover.
    * Document durability/availability, backup/replication, lifecycle policies, cost, health, and rollback.
  * Risks & Mitigations: Object-store consistency and provider identities can be confused with canonical byte identity or create silent missing content. / Keep SHA-256 authoritative, stage/no-replace/verify every write, and use a manifest-driven one-authority migration..
  * Tags: [object-storage] [content-store] [migration] [p3]

## E26. Optional remote worker execution

Scale execution location without changing phase barriers, coordinator authority, work semantics, exact-byte identity, or durable recovery.

* [ ] - T26.1.1 Define the authenticated remote worker protocol and compatibility handshake
  * Priority: `P3`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SCALE} {EXECUTION} {SECURITY} {COMPATIBILITY}
  * Dependencies: T15.1.4, T18.1.4, T21.1.4, T25.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.; Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29; R-11,R-17; Option C deferred
  * Acceptance Criteria: 1) Protocol is versioned and compatibility failure is explicit before work starts.; 2) Worker cannot mutate lifecycle state or access undeclared artifacts.; 3) Stale/duplicate/forged results are rejected deterministically and retained as evidence.; 4) Local and remote backends share WorkSpec/result conformance semantics.
  * Steps / Subtasks:
    * Define service/worker identity, protocol version, runtime/plugin/backend capability digest, WorkSpec digest, immutable input references, budgets, deadline, lease/fencing token, idempotency key, and result/evidence digest.
    * Negotiate compatible versions/capabilities before assignment and reject semantic/plugin/config mismatches.
    * Define heartbeat/lease renewal, cancellation acknowledgement, drain, progress/checkpoint reference, result upload/verification, stale rejection, and replay.
    * Keep phase/work planning and authoritative attempt transitions in coordinator/StateStore.
  * Risks & Mitigations: A remote protocol can accidentally make workers authorities or accept stale/forged results across versions. / Bind authenticated messages to immutable WorkSpec, lease, fencing, and compatibility digests while keeping all transitions central..
  * Tags: [remote-worker] [protocol] [identity] [p3]

* [ ] - T26.1.2 Implement the least-privileged remote worker service
  * Priority: `P3`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SCALE} {EXECUTION} {SECURITY} {STORAGE}
  * Dependencies: T26.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.; Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29; R-11,R-17; Option C deferred
  * Acceptance Criteria: 1) Worker completes only authenticated assigned WorkSpecs and cannot write lifecycle authority.; 2) All input/output bytes are hash-verified and scoped to the attempt.; 3) Lease loss/cancel/drain leads to deterministic backend stop/result handling.; 4) Compromise/revocation can fence the worker and preserve investigation evidence.
  * Steps / Subtasks:
    * Advertise only locally verified backend/plugin/tool/resource capabilities and apply server-approved grants per assignment.
    * Fetch immutable inputs through scoped single-use/expiring references, verify content hashes, and isolate per-attempt workspace/cache.
    * Execute using in-process only for explicitly trusted plugins or subprocess for untrusted/high-risk work under the same policy.
    * Heartbeat/renew, honor cancel/drain, upload staged results/evidence, and discard/fence after lease loss.
  * Risks & Mitigations: Workers may accumulate broad credentials, stale authority, or unverifiable cached/content outputs. / Use scoped identity/artifact grants, verify exact bytes, fence on lease loss, and keep persistence central..
  * Tags: [worker-service] [least-privilege] [artifacts] [p3]

* [ ] - T26.1.3 Implement remote scheduling, result verification, cancellation, and fallback policy
  * Priority: `P3`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SCALE} {EXECUTION} {RECOVERY} {LIFECYCLE}
  * Dependencies: T26.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.; Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29; R-11,R-17; Option C deferred
  * Acceptance Criteria: 1) One valid fenced result can commit for each work attempt.; 2) Worker loss maps to deterministic wait/retry/reconcile/block behavior from operation semantics.; 3) Fallback/reassignment is disabled for unsafe/unknown side effects and never weakens policy.; 4) Remote execution preserves the same phase barriers, persistence, events, lineage, and status as local execution.
  * Steps / Subtasks:
    * Filter workers by protocol/runtime/plugin/capability/resource/data-locality compatibility and apply deterministic or explainable tie-breaking.
    * Persist assignment/lease before dispatch; verify authenticated result envelope, fencing, WorkSpec digest, output content hashes, schema, and budget evidence before commit.
    * Define cancellation/drain and local fallback/reassignment only for operations whose semantics and idempotency allow it.
    * Preserve work-item phase barrier and coordinator-owned aggregation/transition.
  * Risks & Mitigations: Reassignment or fallback after worker uncertainty can duplicate effects or downgrade isolation. / Persist/fence assignments, verify results, and consult operation semantics before any successor or backend change..
  * Tags: [remote-scheduler] [result-verification] [fallback] [p3]

* [ ] - T26.1.4 Gate distributed execution with chaos, security, load, and operational evidence
  * Priority: `P3`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SCALE} {RELEASE} {SECURITY} {PERFORMANCE}
  * Dependencies: T26.1.2, T26.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.; Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29; R-11,R-17; Option C deferred
  * Acceptance Criteria: 1) Remote backend passes all local backend/state/recovery/lineage conformance suites.; 2) Chaos matrix demonstrates stale fencing and no duplicate authoritative effects.; 3) Benchmark and operations evidence justify distributed complexity for a defined workload.; 4) Drain/rollback/revocation drill handles in-flight work without alternate authority.
  * Steps / Subtasks:
    * Test partitions at dispatch/heartbeat/result/ack, worker kill/restart, duplicate delivery, stale result, clock skew, protocol/plugin mismatch, artifact corruption, and control-plane outage.
    * Run malicious-worker scenarios for forged identities/results, capability overclaim, data access, resource reporting, and replay.
    * Benchmark against local execution including transfer overhead, utilization, throughput, recovery time, event/database pressure, and operator burden.
    * Progressively roll out by operation/plugin with canary, drain, fallback rules, and a local rollback path where safe.
  * Risks & Mitigations: Distributed execution can widen failure and security surfaces while delivering no workload benefit. / Require local-semantic conformance, adversarial chaos evidence, measurable benefit, and practiced drain/rollback..
  * Tags: [chaos] [distributed] [load] [rollout] [p3]

## E27. Bounded MCP and operator interfaces

Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.

* [ ] - T27.1.1 Expose read-only and proposal-only MCP resources and tools
  * Priority: `P3`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {API} {SECURITY} {REVIEW} {PLUGINS}
  * Dependencies: T17.1.4, T19.1.4, T20.1.4, T21.1.4
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.; Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27; R-18
  * Acceptance Criteria: 1) MCP read/proposal tools cannot mutate lifecycle state, safety records, evidence authority, decisions, or publications.; 2) Every proposal is visibly non-authoritative and provenance-versioned.; 3) Hostile artifact text cannot create an unrequested tool call or expand capabilities.; 4) Removing/disabling MCP leaves core semantics and data readable.
  * Steps / Subtasks:
    * Expose read-only job/status, artifact lineage, structural/evidence summaries, capability catalog, and proposal submission with strict schemas and pagination.
    * Label all model/agent output as proposed/inferred, record model/provider/prompt/tool/config/input evidence versions, and keep it separate from findings/evidence/decisions unless deterministic services accept it.
    * Use canonical service calls and return stable IDs/references rather than raw unrestricted files/content.
    * Make MCP an optional package/process that can be removed without core behavior changes.
  * Risks & Mitigations: Agent interfaces are vulnerable to prompt injection and excessive agency if artifact content can drive tools or mutations. / Start read/proposal-only, use strict deterministic services and least-privilege grants, and preserve explicit authority labels..
  * Tags: [mcp] [ai] [proposal] [read-only] [p3]

* [ ] - T27.1.2 Route consequential MCP actions through deterministic command and review gates
  * Priority: `P3`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {API} {SECURITY} {LIFECYCLE} {REVIEW}
  * Dependencies: T27.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.; Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27; R-18
  * Acceptance Criteria: 1) No MCP command bypasses CommandService, lifecycle guards, review policy, publication checks, or expected-version/idempotency.; 2) Prompt-injected artifact text cannot authorize or alter a tool action.; 3) AI-only output cannot create an approved PromotionDecision.; 4) Replay, stale state, revoked session, and changed confirmation return deterministic non-success outcomes.
  * Steps / Subtasks:
    * Classify MCP tools by read, proposal, reversible control, review request, and external side effect; disable consequential classes by default.
    * Require deployment authorization, exact subject/state version, idempotency key, reason, policy evaluation, and explicit confirmation/approval for configured side effects.
    * Record requested versus accepted command and final authoritative outcome separately.
    * Never allow an AI actor to be the sole final promotion authority; it may submit a proposal/request for deterministic or human review.
  * Risks & Mitigations: Adding mutation tools can make the model an implicit authority or confused deputy. / Keep deterministic command/policy/review gates authoritative and require explicit scoped deployment enablement and confirmation..
  * Tags: [mcp] [commands] [prompt-injection] [governance] [p3]

* [ ] - T27.1.3 Build an operator UI that preserves authority and uncertainty distinctions
  * Priority: `P3`
  * Est. Effort: `16h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {DX} {API} {SECURITY} {OBSERVABILITY}
  * Dependencies: T27.1.1
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.; Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27; R-18
  * Acceptance Criteria: 1) UI never labels a finding/proposal as evidence, a request as decision, or an attempt as verified publication.; 2) All commands traverse canonical APIs and reject stale/replayed input.; 3) Hostile rendered content cannot execute or create unauthorized navigation/actions.; 4) Accessibility, large-job performance, partial outage, and compatibility behavior are tested.
  * Steps / Subtasks:
    * Design views for job/phase/attempt/work progress, controls, blockers/recovery, artifact/provenance graph, findings/evidence, review, publications, events, health, and diagnostics.
    * Use generated versioned API contracts and expected-version/idempotency for all commands; refresh and surface stale data before confirmation.
    * Label observed, derived, inferred, proposed, evidence, approved/rejected/held, attempted, verified published, unknown, and degraded states distinctly.
    * Provide accessible keyboard/navigation/status/error behavior and bounded pagination for large jobs.
  * Risks & Mitigations: A UI can mislead operators by presenting inferred or pending information as trusted success and can render untrusted content. / Make authority categories first-class, use generated contracts, encode all content, and require stale/version checks..
  * Tags: [operator-ui] [authority-labels] [accessibility] [p3]

* [ ] - T27.1.4 Resolve tenant, authentication, authorization, and deployment-governance scope
  * Priority: `P3`
  * Est. Effort: `14h`
  * Owner: `@unassigned` | R: implementation owner | A: ATLAS maintainer | C: security, reliability, data-model, and operator reviewers | I: plugin authors, integrators, and downstream operators
  * Domains: {SECURITY} {ARCHITECTURE} {COMPATIBILITY} {SCALE}
  * Dependencies: T27.1.2, T27.1.3
  * Evidence: Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.; Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.; Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.; Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.; source mapping: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27; R-18
  * Acceptance Criteria: 1) Deployment identity/tenancy requirements, non-goals, and decision authority are evidenced and approved.; 2) Selected adapters preserve core semantics and local mode remains safe and documented.; 3) If multi-tenancy is required, isolation is modeled across state, content, events, caches, workers, diagnostics, and publications before implementation.; 4) Auth/policy outage, revocation, and rollback behavior are deterministic and tested.
  * Steps / Subtasks:
    * Inventory deployment actors, service boundaries, data sensitivity, source/destination ownership, concurrent users, audit obligations, and tenant separation needs.
    * Classify actions: local harmless analysis, controls, plugin grants, review, publication, retention deletion, configuration, and administration.
    * Compare local OS identity, API gateway/IdP, RBAC/ABAC, tenant-scoped stores/content, and service identity adapters against requirements and cost.
    * Keep deterministic lifecycle/state/source/safety enforcement in core and define deployment auth/policy adapters only where justified.
  * Risks & Mitigations: Premature IAM can overengineer the core, while network/tenant deployment without explicit identity creates severe confused-deputy and data-boundary risks. / Resolve actual deployment scope first and isolate optional auth/policy adapters from deterministic core enforcement..
  * Tags: [identity] [authorization] [tenancy] [governance] [p3]

Implementation notes: execute evidence and authority resolution before path-dependent changes; preserve the six phase barriers, one authoritative state owner, exact-byte lineage, fail-closed safety, replay/idempotency semantics, observability, migration, rollout, rollback, documentation, and completion evidence. P2/P3 adapters must not bypass unresolved P0/P1 foundations.

## Machine-Readable Task Index

```json
[
  {
    "task_id": "T1.1.1",
    "title": "Freeze the active ATLAS ref and repository authority map",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "The baseline record contains the exact current SHA, branch, dirty-state summary, repository inventory hash, and source-package hash.",
      "Every ZIP-cited ATLAS path/symbol is classified as present, moved, replaced, removed, or unverified.",
      "A command matrix identifies the exact repository-native validation commands, working directory, prerequisites, and expected result class.",
      "No production source file is modified."
    ],
    "tags": [
      "baseline",
      "authority",
      "read-only",
      "p0"
    ]
  },
  {
    "task_id": "T1.1.2",
    "title": "Revalidate all product-direction requirements against the attached PDF",
    "priority": "P0",
    "estimated_hours": "8h",
    "owner": "@unassigned",
    "dependencies": [],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "All 30 requirements have a verified page range, status, mapped production task IDs, and an ambiguity field.",
      "The end-state and lifecycle diagrams are summarized without contradicting the attached visuals.",
      "The previous `PDF not independently accessible` limitation is explicitly closed for this planning run.",
      "No PDF statement is promoted to current implementation fact."
    ],
    "tags": [
      "pdf",
      "requirements",
      "evidence",
      "p0"
    ]
  },
  {
    "task_id": "T1.1.3",
    "title": "Restore and revalidate the Yggdrasil donor baseline and license provenance",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "Every donor integration row has a verified path/symbol, commit, dependency set, license note, and final disposition.",
      "Tests worth porting are named with the ATLAS invariant they prove.",
      "No donor mechanism is designated `REUSE` without an exact source and compatibility assessment.",
      "Unavailable evidence remains `UNRESOLVED` and blocks code transplantation."
    ],
    "tags": [
      "donor",
      "license",
      "provenance",
      "p0"
    ]
  },
  {
    "task_id": "T1.1.4",
    "title": "Publish the canonical component-ownership and scope boundary matrix",
    "priority": "P0",
    "estimated_hours": "10h",
    "owner": "@unassigned",
    "dependencies": [
      "T1.1.1",
      "T1.1.2",
      "T1.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "Every authoritative record and transition has exactly one named owner.",
      "All helper candidates are classified with rationale and mapped to a task or explicit rejection.",
      "The matrix preserves fixed A-F barriers and separates mechanism from deployment policy.",
      "The matrix is reviewed before module creation begins."
    ],
    "tags": [
      "architecture",
      "ownership",
      "scope",
      "p0"
    ]
  },
  {
    "task_id": "T2.1.1",
    "title": "Define the versioned characterization fixture manifest",
    "priority": "P0",
    "estimated_hours": "8h",
    "owner": "@unassigned",
    "dependencies": [
      "T1.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]",
      "Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change."
    ],
    "acceptance_criteria": [
      "The manifest schema validates all baseline fixtures and rejects missing GAP/REQ lineage.",
      "Every GAP-001 through GAP-015 has a fixture or an explicit investigation record.",
      "All fixture inputs are sanitized, bounded, and self-contained.",
      "Expectation-change policy requires linked correction task and reviewer approval."
    ],
    "tags": [
      "tests",
      "fixtures",
      "characterization",
      "p0"
    ]
  },
  {
    "task_id": "T2.1.2",
    "title": "Characterize CLI, API, persistence, event, and filesystem outcomes",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T2.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]",
      "Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change."
    ],
    "acceptance_criteria": [
      "Every selected scenario records a complete, canonical evidence bundle.",
      "CLI and Python invocation paths are compared for equivalent authoritative outcomes.",
      "Three clean runs yield identical normalized evidence hashes.",
      "No production source behavior changes are included."
    ],
    "tags": [
      "cli",
      "api",
      "state",
      "characterization",
      "p0"
    ]
  },
  {
    "task_id": "T2.1.3",
    "title": "Add adversarial source, archive, analyzer, and control baselines",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T2.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]",
      "Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change."
    ],
    "acceptance_criteria": [
      "Every high-risk path has a reproducible current-state outcome or explicit capability-limited investigation.",
      "The >50 finding case proves whether authoritative data is truncated or only summarized.",
      "Source mutation and second-process control behavior are recorded with exact state/effect boundaries.",
      "All adversarial fixtures stay within declared byte, time, and file-count limits."
    ],
    "tags": [
      "adversarial",
      "archive",
      "toctou",
      "controls",
      "p0"
    ]
  },
  {
    "task_id": "T2.1.4",
    "title": "Integrate characterization evidence into CI and correction gates",
    "priority": "P0",
    "estimated_hours": "10h",
    "owner": "@unassigned",
    "dependencies": [
      "T2.1.2",
      "T2.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]",
      "Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change."
    ],
    "acceptance_criteria": [
      "Characterization jobs are mandatory for P0 changes and fail on unapproved skips.",
      "Failure artifacts include all required evidence without secrets or unbounded payloads.",
      "Every expectation change links to its implementation task and reviewer decision.",
      "Three-run determinism is checked in CI or an equivalent reproducible gate."
    ],
    "tags": [
      "ci",
      "quality-gate",
      "evidence",
      "p0"
    ]
  },
  {
    "task_id": "T3.1.1",
    "title": "Define `PipelineDefinitionV1`, canonical phase slots, and one failure policy",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T2.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]",
      "Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax."
    ],
    "acceptance_criteria": [
      "Every accepted definition contains A-F exactly once in canonical order.",
      "Contradictory legacy failure flags are rejected before job creation.",
      "Disabled phases produce an explicit policy and eventual durable `SKIPPED` reason.",
      "The JSON schema and Python model agree on all required fields and enums."
    ],
    "tags": [
      "configuration",
      "lifecycle",
      "schema",
      "p0"
    ]
  },
  {
    "task_id": "T3.1.2",
    "title": "Implement deterministic safe loading, merge order, and canonical digests",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T3.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]",
      "Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax."
    ],
    "acceptance_criteria": [
      "Equivalent normalized configurations produce identical digests across runs.",
      "Every accepted phase key is consumed by a typed model.",
      "Invalid configuration creates no job row, workspace, or outbox event.",
      "Diagnostics identify source path, key, expected type, and stable error code without exposing secrets."
    ],
    "tags": [
      "loader",
      "digest",
      "yaml",
      "p0"
    ]
  },
  {
    "task_id": "T3.1.3",
    "title": "Create typed configuration contracts for all six built-in phases",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T3.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]",
      "Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax."
    ],
    "acceptance_criteria": [
      "Every built-in phase receives only its typed configuration object.",
      "No production phase reads raw `phase_config` dictionaries after migration.",
      "Unsupported capability or platform combinations fail before attempt creation.",
      "Config schema round-trips preserve semantics and digest."
    ],
    "tags": [
      "typed-config",
      "phases",
      "contracts",
      "p0"
    ]
  },
  {
    "task_id": "T3.1.4",
    "title": "Add legacy pipeline migration, dual support, and deprecation telemetry",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T3.1.2",
      "T3.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]",
      "Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax."
    ],
    "acceptance_criteria": [
      "All existing examples either migrate to an approved digest or fail with a documented reason.",
      "Legacy and migrated definitions produce equivalent intended lifecycle behavior for supported cases.",
      "Deprecation telemetry reports use without logging sensitive configuration.",
      "Removal criteria and compatibility window are documented and testable."
    ],
    "tags": [
      "migration",
      "legacy",
      "deprecation",
      "p0"
    ]
  },
  {
    "task_id": "T4.1.1",
    "title": "Define the narrow `StateStore` transaction and repository contracts",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T2.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]",
      "Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`."
    ],
    "acceptance_criteria": [
      "No authoritative repository method commits outside a `StateStore` transaction.",
      "`JobStore` compatibility calls delegate without changing public results.",
      "The error taxonomy distinguishes contention, corruption, schema mismatch, constraint, cancellation, and storage exhaustion.",
      "A backend conformance test skeleton covers transaction atomicity and rollback."
    ],
    "tags": [
      "persistence",
      "transactions",
      "state-store",
      "p0"
    ]
  },
  {
    "task_id": "T4.1.2",
    "title": "Implement the SQLite backend with explicit connection and locking policy",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T4.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]",
      "Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`."
    ],
    "acceptance_criteria": [
      "Foreign keys and uniqueness constraints are enabled and demonstrated.",
      "Contention yields bounded, classified behavior with lock-wait metrics.",
      "All existing job/phase persistence tests pass through the new backend.",
      "Startup reports actual SQLite capabilities and refuses unsafe/unsupported state."
    ],
    "tags": [
      "sqlite",
      "locking",
      "persistence",
      "p0"
    ]
  },
  {
    "task_id": "T4.1.3",
    "title": "Create immutable numbered migrations and the v0.1 upgrade path",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T4.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]",
      "Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`."
    ],
    "acceptance_criteria": [
      "Fresh and upgraded databases have identical schema fingerprints and invariants.",
      "Migration checksums are immutable and verified on every startup.",
      "Newer unsupported schema and checksum drift fail with stable diagnostics.",
      "Every migration has forward test fixtures and a documented restore-based rollback."
    ],
    "tags": [
      "migrations",
      "schema",
      "upgrade",
      "p0"
    ]
  },
  {
    "task_id": "T4.1.4",
    "title": "Implement verified backup, restore, integrity, and migration recovery",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T4.1.2",
      "T4.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]",
      "Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`."
    ],
    "acceptance_criteria": [
      "A verified pre-migration backup exists before any schema change.",
      "Restore drills reproduce schema and row fingerprints in a separate location.",
      "Migration failure leaves the original database and backup usable.",
      "Operator diagnostics identify exact failure stage, artifact hashes, and safe next action."
    ],
    "tags": [
      "backup",
      "restore",
      "integrity",
      "p0"
    ]
  },
  {
    "task_id": "T5.1.1",
    "title": "Specify exhaustive job, phase, attempt, and control state tables",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T3.1.4",
      "T4.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.",
      "Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`."
    ],
    "acceptance_criteria": [
      "Transition tables are exhaustive and machine-readable.",
      "Every state has one owner, legal predecessors/successors, and terminal semantics.",
      "Invalid legacy combinations have an explicit migration or blocked-state rule.",
      "The tables map to PDF lifecycle semantics without creating DAG behavior."
    ],
    "tags": [
      "state-machine",
      "attempts",
      "controls",
      "p0"
    ]
  },
  {
    "task_id": "T5.1.2",
    "title": "Persist immutable phase runs and execution attempts",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T5.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.",
      "Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`."
    ],
    "acceptance_criteria": [
      "Every execution is represented by exactly one immutable attempt record.",
      "Duplicate concurrent attempt creation is rejected by transaction and uniqueness guards.",
      "Legacy phase status remains available as a derived compatibility projection.",
      "Attempt rows link to exact input/config/policy and later result/checkpoint evidence."
    ],
    "tags": [
      "attempts",
      "persistence",
      "lineage",
      "p0"
    ]
  },
  {
    "task_id": "T5.1.3",
    "title": "Implement guarded atomic transitions and fencing tokens",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T5.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.",
      "Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`."
    ],
    "acceptance_criteria": [
      "Every transition requires the expected current state/version and fails deterministically when stale.",
      "Stale fencing tokens cannot commit result or terminal state.",
      "Concurrent transition tests produce one winner and auditable losers.",
      "No production code mutates lifecycle status fields outside the coordinator/repository path."
    ],
    "tags": [
      "guards",
      "fencing",
      "atomicity",
      "p0"
    ]
  },
  {
    "task_id": "T5.1.4",
    "title": "Add model-based state-machine and invalid-transition verification",
    "priority": "P0",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T5.1.2",
      "T5.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.",
      "Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`."
    ],
    "acceptance_criteria": [
      "Model and implementation agree across the declared generated sequence budget.",
      "Every illegal transition class has a stable error code and zero authoritative mutation.",
      "Counterexamples are reproducible and retained.",
      "State-machine tests run in mandatory CI without unapproved skips."
    ],
    "tags": [
      "property-testing",
      "state-machine",
      "verification",
      "p0"
    ]
  },
  {
    "task_id": "T6.1.1",
    "title": "Define `SourceRoot`, `IntakeGeneration`, and `ArtifactOccurrence` schemas",
    "priority": "P0",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T4.1.4",
      "T5.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]",
      "Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`."
    ],
    "acceptance_criteria": [
      "Occurrence and content concepts remain structurally distinct.",
      "Every occurrence belongs to exactly one generation and one source root.",
      "Accepted generation records are immutable and supersession is explicit.",
      "Schema supports local filesystem now without claiming unsupported provider semantics."
    ],
    "tags": [
      "intake",
      "models",
      "occurrence",
      "p0"
    ]
  },
  {
    "task_id": "T6.1.2",
    "title": "Implement bounded deterministic intake traversal",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T6.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]",
      "Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`."
    ],
    "acceptance_criteria": [
      "Traversal order and accepted manifest input are deterministic for a stable source.",
      "Every skipped/error entry has a persisted reason and no silent omission.",
      "Budget exhaustion yields BLOCKED or FAILED, not ACCEPTED.",
      "Memory use is bounded independently of total entry count."
    ],
    "tags": [
      "traversal",
      "determinism",
      "budgets",
      "p0"
    ]
  },
  {
    "task_id": "T6.1.3",
    "title": "Implement generation acceptance, manifest digests, and supersession",
    "priority": "P0",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T6.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]",
      "Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`."
    ],
    "acceptance_criteria": [
      "Only complete generations reach ACCEPTED.",
      "Equivalent stable observations yield the same manifest digest.",
      "Duplicate acceptance is idempotent and conflicting acceptance fails.",
      "Supersession preserves both generations and lineage."
    ],
    "tags": [
      "manifest",
      "acceptance",
      "provenance",
      "p0"
    ]
  },
  {
    "task_id": "T6.1.4",
    "title": "Make all downstream phases consume accepted occurrence IDs only",
    "priority": "P0",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T6.1.2",
      "T6.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]",
      "Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`."
    ],
    "acceptance_criteria": [
      "Static/runtime guards find no unauthorized downstream source enumeration.",
      "Fingerprinting consumes exactly the accepted occurrence set.",
      "Deleted/mutated occurrences produce deterministic stale/missing outcomes.",
      "Compatibility behavior is documented and time-bounded."
    ],
    "tags": [
      "phase-inputs",
      "immutable-intake",
      "toctou",
      "p0"
    ]
  },
  {
    "task_id": "T7.1.1",
    "title": "Define `ContentIdentity` and occurrence-to-content link contracts",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T6.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]",
      "Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade."
    ],
    "acceptance_criteria": [
      "Identical bytes converge on one persistent SHA-256 identity across processes.",
      "All occurrences remain independently traceable to the shared identity.",
      "Identity records do not falsely claim retained bytes.",
      "Malformed or conflicting digest records fail integrity checks."
    ],
    "tags": [
      "sha256",
      "identity",
      "provenance",
      "p0"
    ]
  },
  {
    "task_id": "T7.1.2",
    "title": "Implement race-aware streaming hashing from accepted occurrences",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T7.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]",
      "Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade."
    ],
    "acceptance_criteria": [
      "Stable inputs produce the expected SHA-256 and link evidence.",
      "Mutation cannot attach the wrong identity to an occurrence.",
      "Partial or indeterminate reads never appear successful.",
      "Progress remains bounded and durable through the PhaseContext contract."
    ],
    "tags": [
      "hashing",
      "toctou",
      "streaming",
      "p0"
    ]
  },
  {
    "task_id": "T7.1.3",
    "title": "Add persistent cross-run duplicate lookup and processing-reuse eligibility",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T7.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]",
      "Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade."
    ],
    "acceptance_criteria": [
      "A restart recognizes previously seen content without recomputing downstream identity state.",
      "Every duplicate occurrence is persisted and queryable.",
      "Reuse eligibility is false unless exact downstream keys and integrity requirements are satisfied.",
      "High-occurrence queries remain bounded and indexed."
    ],
    "tags": [
      "dedup",
      "reuse",
      "queries",
      "p0"
    ]
  },
  {
    "task_id": "T7.1.4",
    "title": "Preserve `HashStore` compatibility while removing process-local authority",
    "priority": "P0",
    "estimated_hours": "10h",
    "owner": "@unassigned",
    "dependencies": [
      "T7.1.2",
      "T7.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]",
      "Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade."
    ],
    "acceptance_criteria": [
      "Supported legacy calls return documented equivalent results from persistent state.",
      "No in-memory manifest is authoritative after migration.",
      "Deprecated semantics produce actionable warnings and migration docs.",
      "Compatibility tests cover restart and multiple-runtime cases."
    ],
    "tags": [
      "compatibility",
      "hash-store",
      "migration",
      "p0"
    ]
  },
  {
    "task_id": "T8.1.1",
    "title": "Define versioned durable event and outbox schemas",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T4.1.4",
      "T5.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]",
      "Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`."
    ],
    "acceptance_criteria": [
      "Every required transition event has a stable typed schema and entity references.",
      "Local sequence establishes deterministic within-store ordering.",
      "Outbox state is distinct from event history and transport-specific payload.",
      "Event evolution rules preserve old history and reject unsafe downgrade."
    ],
    "tags": [
      "events",
      "outbox",
      "schemas",
      "p0"
    ]
  },
  {
    "task_id": "T8.1.2",
    "title": "Record state transitions, durable events, and outbox rows atomically",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T8.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]",
      "Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`."
    ],
    "acceptance_criteria": [
      "Fault injection at every transaction step yields all-or-nothing state/history/outbox.",
      "Every required transition query returns its durable event.",
      "Duplicate commands do not create duplicate lifecycle effects.",
      "Transport outage cannot corrupt or roll back already-valid state."
    ],
    "tags": [
      "atomicity",
      "events",
      "transactions",
      "p0"
    ]
  },
  {
    "task_id": "T8.1.3",
    "title": "Implement the idempotent outbox dispatcher and delivery backpressure",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T8.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]",
      "Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`."
    ],
    "acceptance_criteria": [
      "Redelivery creates no duplicate lifecycle effect.",
      "A poison event is isolated and does not starve later records.",
      "Backlog limits produce documented block/degrade behavior and diagnostics.",
      "Disabling all transports leaves core execution correct."
    ],
    "tags": [
      "dispatcher",
      "backpressure",
      "idempotency",
      "p0"
    ]
  },
  {
    "task_id": "T8.1.4",
    "title": "Define progress-event sampling, retention, replay, and event diagnostics",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T8.1.2",
      "T8.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]",
      "Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`."
    ],
    "acceptance_criteria": [
      "Current progress remains exact within defined update semantics even when history is sampled.",
      "Required event classes are never sampled or pruned outside policy.",
      "Replay/export detects gaps and schema incompatibility.",
      "Event diagnostics identify backlog, dead letters, retention watermark, and sequence gaps."
    ],
    "tags": [
      "sampling",
      "retention",
      "replay",
      "events",
      "p0"
    ]
  },
  {
    "task_id": "T9.1.1",
    "title": "Define `PhaseContext`, progress, control-request, and checkpoint contracts",
    "priority": "P0",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T5.1.4",
      "T8.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.",
      "Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`."
    ],
    "acceptance_criteria": [
      "Contracts distinguish current progress, sampled history, controls, and checkpoints.",
      "All serialized records are versioned and digestible.",
      "PhaseContext grants no direct lifecycle authority.",
      "Safe-point and maximum-control-latency requirements are expressible per phase."
    ],
    "tags": [
      "phase-context",
      "progress",
      "controls",
      "checkpoints",
      "p0"
    ]
  },
  {
    "task_id": "T9.1.2",
    "title": "Persist live progress and deterministic job-level projections",
    "priority": "P0",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T9.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.",
      "Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`."
    ],
    "acceptance_criteria": [
      "A second process observes progress within the documented staleness bound.",
      "Job-level progress is deterministic and never decreases except by a documented retry-generation reset.",
      "Progress write volume remains bounded under million-entry workloads.",
      "Terminal state and final progress are mutually consistent."
    ],
    "tags": [
      "progress",
      "status",
      "durability",
      "p0"
    ]
  },
  {
    "task_id": "T9.1.3",
    "title": "Implement durable control requests and safe-point acknowledgement",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T9.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.",
      "Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`."
    ],
    "acceptance_criteria": [
      "A second process can request and observe applied/rejected control state.",
      "`PAUSED` is reached only after durable safe-point acknowledgement.",
      "Duplicate control requests are idempotent and conflicting payloads are rejected.",
      "Built-in phases document and test maximum control latency."
    ],
    "tags": [
      "controls",
      "pause",
      "cancel",
      "p0"
    ]
  },
  {
    "task_id": "T9.1.4",
    "title": "Implement checkpoint validation, resume decisions, and stale-checkpoint rejection",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T9.1.2",
      "T9.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.",
      "Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`."
    ],
    "acceptance_criteria": [
      "Stale or incompatible checkpoints never resume execution.",
      "Every built-in phase declares checkpoint granularity and validation inputs.",
      "Crash tests resume or restart according to one deterministic rule.",
      "Checkpoint rejection remains visible in status and diagnostics."
    ],
    "tags": [
      "resume",
      "checkpoint",
      "validation",
      "p0"
    ]
  },
  {
    "task_id": "T10.1.1",
    "title": "Specify source-access policy and platform capability contracts",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T6.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].",
      "Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report."
    ],
    "acceptance_criteria": [
      "Policy documents exact guarantees by supported platform.",
      "Unsafe or unsupported capability combinations fail before intake/job execution.",
      "Source and destination path authorities remain separate.",
      "Every normalization and policy decision has a stable error/status code."
    ],
    "tags": [
      "path-safety",
      "platform",
      "policy",
      "p0"
    ]
  },
  {
    "task_id": "T10.1.2",
    "title": "Implement handle-relative no-follow opens and occurrence verification",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T10.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].",
      "Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report."
    ],
    "acceptance_criteria": [
      "Symlink/reparse swap fixtures cannot escape the registered root.",
      "Opened object identity is compared to the occurrence before bytes are trusted.",
      "Unsupported strong primitives are reported, never silently emulated as equivalent.",
      "All descriptors close on success, cancellation, and failure."
    ],
    "tags": [
      "source-access",
      "toctou",
      "handles",
      "p0"
    ]
  },
  {
    "task_id": "T10.1.3",
    "title": "Create separate safe temporary and destination path services",
    "priority": "P0",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T10.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].",
      "Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report."
    ],
    "acceptance_criteria": [
      "All temp/workspace files are attempt-owned, permission-restricted, and contained.",
      "No-replace behavior is capability-tested and collision-safe.",
      "Cleanup is idempotent and cannot escape its root.",
      "Source and destination APIs cannot be substituted for one another by type/interface."
    ],
    "tags": [
      "tempfiles",
      "destinations",
      "workspace",
      "p0"
    ]
  },
  {
    "task_id": "T10.1.4",
    "title": "Route every built-in filesystem operation through canonical access services",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T10.1.2",
      "T10.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].",
      "Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report."
    ],
    "acceptance_criteria": [
      "Static analysis finds no unapproved direct filesystem authority in built-in phases.",
      "Every source read is attributable to SourceRoot/Generation/Occurrence.",
      "Every write is attributable to job/phase/attempt/workspace or publication attempt.",
      "Bypass attempts fail deterministic security tests."
    ],
    "tags": [
      "integration",
      "guardrails",
      "filesystem",
      "p0"
    ]
  },
  {
    "task_id": "T11.1.1",
    "title": "Implement attempt-owned quarantine workspace lifecycle",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T7.1.4",
      "T10.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].",
      "Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`."
    ],
    "acceptance_criteria": [
      "No Phase-D or analyzer write occurs under any registered source root.",
      "Every workspace is attributable to one attempt and has deterministic status/recovery.",
      "Quotas and actual usage are persisted and enforced.",
      "Cleanup is idempotent, contained, and preserves evidence when ownership is uncertain."
    ],
    "tags": [
      "quarantine",
      "workspace",
      "isolation",
      "p0"
    ]
  },
  {
    "task_id": "T11.1.2",
    "title": "Implement recursive structural inspection under cumulative archive budgets",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T11.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].",
      "Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`."
    ],
    "acceptance_criteria": [
      "All adversarial containers terminate within configured CPU/time/byte/member/depth bounds.",
      "Nested limits are cumulative and recursively enforced.",
      "Every member decision is recorded with stable reason and parent linkage.",
      "Unknown or partial inspection cannot authorize extraction."
    ],
    "tags": [
      "archives",
      "recursive",
      "budgets",
      "p0"
    ]
  },
  {
    "task_id": "T11.1.3",
    "title": "Implement exact-report-bound `MaterializationService`",
    "priority": "P0",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T11.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].",
      "Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`."
    ],
    "acceptance_criteria": [
      "Phase D rejects every report/content/config/policy mismatch before writing.",
      "No output escapes the attempt workspace or overwrites an existing file.",
      "Actual written bytes and file counts remain within cumulative budgets.",
      "Partial/cancelled attempts retain deterministic status, evidence, and cleanup ownership."
    ],
    "tags": [
      "materialization",
      "extraction",
      "no-overwrite",
      "p0"
    ]
  },
  {
    "task_id": "T11.1.4",
    "title": "Persist derivation edges and adversarial materialization evidence",
    "priority": "P0",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T11.1.2",
      "T11.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].",
      "Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`."
    ],
    "acceptance_criteria": [
      "Every downstream extracted identity has at least one valid derivation edge.",
      "No derivation is committed before child hash verification.",
      "Bidirectional lineage queries detect and reject orphan records.",
      "Adversarial corpus tests complete within declared resource ceilings on supported platforms."
    ],
    "tags": [
      "derivation",
      "lineage",
      "archive-tests",
      "p0"
    ]
  },
  {
    "task_id": "T12.1.1",
    "title": "Define `ContentStore` contracts and retention-mode semantics",
    "priority": "P1",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T7.1.4",
      "T10.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.",
      "Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor."
    ],
    "acceptance_criteria": [
      "Retention mode has one documented effect on job state and replayability.",
      "Provider contract distinguishes absent, corrupt, unknown, and verified blobs.",
      "Default mode and compatibility policy are approved and recorded.",
      "No API equates `ContentIdentity` existence with managed-byte availability."
    ],
    "tags": [
      "cas",
      "retention-mode",
      "contracts",
      "p1"
    ]
  },
  {
    "task_id": "T12.1.2",
    "title": "Implement staged, verified, no-replace local CAS writes",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T12.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.",
      "Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor."
    ],
    "acceptance_criteria": [
      "Repeated identical bytes consume one verified blob payload.",
      "Concurrent writes yield one commit and safe verified reuse.",
      "Existing mismatch is blocked and surfaced as integrity incident.",
      "Crash points leave valid blob, detectable orphan, or no blob—never false commit."
    ],
    "tags": [
      "local-cas",
      "atomic-write",
      "integrity",
      "p1"
    ]
  },
  {
    "task_id": "T12.1.3",
    "title": "Persist blob provenance, references, quotas, and replayability status",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T12.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.",
      "Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor."
    ],
    "acceptance_criteria": [
      "Every committed blob has verifiable identity, provider, provenance, and retention status.",
      "Replayability is accurate after restart and missing/corrupt file detection.",
      "Quota use and reservations reconcile deterministically.",
      "Identity-only and captured modes remain distinguishable in APIs/events."
    ],
    "tags": [
      "blob-records",
      "quota",
      "replayability",
      "p1"
    ]
  },
  {
    "task_id": "T12.1.4",
    "title": "Implement CAS integrity scans and orphan reconciliation hooks",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T12.1.2",
      "T12.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.",
      "Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor."
    ],
    "acceptance_criteria": [
      "Reconciliation classifies every observed divergence with deterministic next action.",
      "Safe repairs are idempotent and uncertain objects remain preserved/quarantined.",
      "Scans are resumable/bounded and expose progress.",
      "Integrity incidents disable replay/reuse until resolved."
    ],
    "tags": [
      "reconciliation",
      "integrity",
      "cas",
      "p1"
    ]
  },
  {
    "task_id": "T13.1.1",
    "title": "Define and persist versioned `StructuralReport` records",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T11.1.4",
      "T12.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.",
      "Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`."
    ],
    "acceptance_criteria": [
      "Every report binds to exact parent bytes, inspector, config, policy, and schema versions.",
      "Partial and unknown outcomes are visibly non-success.",
      "Member manifests are deterministic and queryable without unbounded loads.",
      "Reports are immutable and supersession preserves history."
    ],
    "tags": [
      "structure",
      "reports",
      "lineage",
      "p1"
    ]
  },
  {
    "task_id": "T13.1.2",
    "title": "Define and persist `ExtractionRecord` and output manifests",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T13.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.",
      "Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`."
    ],
    "acceptance_criteria": [
      "Every extraction attempt has one immutable record and output manifest.",
      "Successful records reference only verified child identities and derivations.",
      "Partial/failure cleanup state remains explicit.",
      "Output manifest supports deterministic bidirectional lineage queries."
    ],
    "tags": [
      "extraction-record",
      "outputs",
      "lineage",
      "p1"
    ]
  },
  {
    "task_id": "T13.1.3",
    "title": "Enforce exact content, configuration, policy, and report binding before extraction",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T13.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.",
      "Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`."
    ],
    "acceptance_criteria": [
      "All mismatches are detected before workspace creation or output writes.",
      "Exact-key equality is based on canonical normalized values.",
      "A valid report/material pair proceeds through one controlled path.",
      "Blocked reasons are visible in state, event history, and status."
    ],
    "tags": [
      "binding",
      "phase-d",
      "fail-closed",
      "p1"
    ]
  },
  {
    "task_id": "T13.1.4",
    "title": "Add deterministic structure reuse and end-to-end lineage invariants",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T13.1.2",
      "T13.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.",
      "Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`."
    ],
    "acceptance_criteria": [
      "Reuse occurs only on exact key equality and records current use provenance.",
      "Every derived content identity traces to at least one valid parent/report/extraction/attempt.",
      "Every publication-ready lineage can traverse back to SourceRoot and exact bytes.",
      "Graph invariant checks detect all injected orphan/cross-job/cycle cases."
    ],
    "tags": [
      "reuse",
      "lineage",
      "invariants",
      "p1"
    ]
  },
  {
    "task_id": "T14.1.1",
    "title": "Define `PluginDescriptor`, `AnalysisContext`, and `AnalysisFinding` schemas",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T3.1.4",
      "T7.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].",
      "Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`."
    ],
    "acceptance_criteria": [
      "No arbitrary dictionary reaches durable findings.",
      "Descriptors express every required capability/resource and fail validation when incomplete.",
      "AnalysisContext exposes no lifecycle or raw persistence authority.",
      "Finding schema preserves complete attributed result sets beyond prior 50-item summaries."
    ],
    "tags": [
      "plugins",
      "contracts",
      "findings",
      "p1"
    ]
  },
  {
    "task_id": "T14.1.2",
    "title": "Implement deterministic plugin discovery and registry snapshots",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T14.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].",
      "Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`."
    ],
    "acceptance_criteria": [
      "Two clean registry builds produce identical order and digest.",
      "Duplicate/incompatible plugins fail before job creation.",
      "Jobs retain the exact registry snapshot/version used.",
      "Unavailable plugin states are distinct from disabled policy."
    ],
    "tags": [
      "registry",
      "discovery",
      "determinism",
      "p1"
    ]
  },
  {
    "task_id": "T14.1.3",
    "title": "Implement plugin capability and trust-tier policy",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T14.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].",
      "Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`."
    ],
    "acceptance_criteria": [
      "Every enabled plugin has one effective capability set and required backend.",
      "Untrusted/high-risk plugins cannot run in process.",
      "Policy/config/version changes invalidate stale WorkSpecs and reuse keys.",
      "Denied capability attempts are observable and tested."
    ],
    "tags": [
      "trust-policy",
      "capabilities",
      "isolation",
      "p1"
    ]
  },
  {
    "task_id": "T14.1.4",
    "title": "Add the legacy `AnalyzerPlugin` adapter and lossless finding migration",
    "priority": "P1",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T14.1.2",
      "T14.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].",
      "Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`."
    ],
    "acceptance_criteria": [
      "Supported legacy plugins produce equivalent normalized findings through the adapter.",
      "All findings persist losslessly within declared limits.",
      "Unsupported authority assumptions fail with migration guidance.",
      "Metadata summary is explicitly derived and never authoritative."
    ],
    "tags": [
      "legacy-plugin",
      "migration",
      "findings",
      "p1"
    ]
  },
  {
    "task_id": "T15.1.1",
    "title": "Define immutable `WorkSpec`, `WorkResult`, and backend protocols",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T5.1.4",
      "T14.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.",
      "Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`."
    ],
    "acceptance_criteria": [
      "Contracts are versioned, deterministic, and backend-neutral.",
      "Backend code cannot obtain StateStore or transition authority through the interface.",
      "Malformed/stale/foreign results are representable as validation failures.",
      "Contract supports in-process, subprocess, and later remote backends without changing lifecycle semantics."
    ],
    "tags": [
      "work-spec",
      "backend",
      "contracts",
      "p1"
    ]
  },
  {
    "task_id": "T15.1.2",
    "title": "Implement the trusted `InProcessBackend`",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T15.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.",
      "Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`."
    ],
    "acceptance_criteria": [
      "A bundled analyzer produces identical normalized findings through WorkSpec/WorkResult.",
      "Backend has no direct persistence/lifecycle mutation capability.",
      "Timeout/cancel outcomes are explicit and later recovery-classifiable.",
      "Registry and policy versions used are echoed and validated."
    ],
    "tags": [
      "in-process",
      "trusted",
      "backend",
      "p1"
    ]
  },
  {
    "task_id": "T15.1.3",
    "title": "Implement coordinator-side result validation and commit",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T15.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.",
      "Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`."
    ],
    "acceptance_criteria": [
      "Only fully validated current results can change attempt/phase state.",
      "Duplicate identical results have one authoritative effect.",
      "Stale/malformed/conflicting results are retained and rejected with stable codes.",
      "Output integrity and budgets are verified before downstream use."
    ],
    "tags": [
      "result-validation",
      "fencing",
      "commit",
      "p1"
    ]
  },
  {
    "task_id": "T15.1.4",
    "title": "Create the reusable backend conformance and fault suite",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T15.1.2",
      "T15.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.",
      "Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`."
    ],
    "acceptance_criteria": [
      "InProcessBackend passes every applicable mandatory case.",
      "The suite can be reused unchanged by subprocess and remote backends.",
      "Unsupported controls are reported and block claims that they are enforced.",
      "Fault cases produce deterministic coordinator outcomes."
    ],
    "tags": [
      "conformance",
      "fault-injection",
      "backends",
      "p1"
    ]
  },
  {
    "task_id": "T16.1.1",
    "title": "Define durable `WorkItem` and phase-barrier semantics",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T8.1.4",
      "T9.1.4",
      "T12.1.4",
      "T13.1.4",
      "T15.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "The model supports bounded parallelism while A-F order remains immutable.",
      "Work-item IDs/order are deterministic for identical phase inputs.",
      "Cross-phase dependencies and cycles are structurally impossible or rejected.",
      "Barrier closure requires all declared invariants and aggregate validation."
    ],
    "tags": [
      "work-items",
      "parallelism",
      "phase-barrier",
      "p1"
    ]
  },
  {
    "task_id": "T16.1.2",
    "title": "Implement the bounded local work-item scheduler and aggregation path",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T16.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "Concurrency never exceeds configured/effective budgets.",
      "Ready sets and aggregation remain bounded under large worksets.",
      "Crash/restart does not duplicate accepted work effects.",
      "Phase barrier closes only after deterministic aggregate validation."
    ],
    "tags": [
      "scheduler",
      "bounded-concurrency",
      "aggregation",
      "p1"
    ]
  },
  {
    "task_id": "T16.1.3",
    "title": "Implement exact-key deterministic result reuse",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T16.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "Reuse occurs only under exact canonical key and verified outputs.",
      "Every reuse is attributable to original result and current decision.",
      "Stale/missing/corrupt/non-deterministic results are not reused.",
      "Metrics quantify hit rate and avoided work without losing occurrence provenance."
    ],
    "tags": [
      "memoization",
      "reuse",
      "determinism",
      "p1"
    ]
  },
  {
    "task_id": "T16.1.4",
    "title": "Implement a unified hierarchical `ResourceBudgetManager`",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T16.1.2",
      "T16.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "All core resource-consuming operations use scoped budget handles.",
      "Concurrent reservations cannot exceed hard shared limits.",
      "Restart reconciliation clears or transfers abandoned reservations deterministically.",
      "Status and diagnostics distinguish requested, reserved, used, exceeded, and unenforceable."
    ],
    "tags": [
      "resource-governance",
      "quotas",
      "budgets",
      "p1"
    ]
  },
  {
    "task_id": "T17.1.1",
    "title": "Persist normalized analysis findings and typed relationships",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T7.1.4",
      "T8.1.4",
      "T13.1.4",
      "T14.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].",
      "Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`."
    ],
    "acceptance_criteria": [
      "Every persisted finding identifies exact input content, analyzer/plugin version, configuration digest, phase attempt, and schema version.",
      "Finding persistence cannot create evidence, a promotion decision, or a publication.",
      "Duplicate policy and supersession behavior are deterministic and documented.",
      "Legacy findings remain readable without being misrepresented as approved knowledge."
    ],
    "tags": [
      "findings",
      "analysis",
      "provenance",
      "p1"
    ]
  },
  {
    "task_id": "T17.1.2",
    "title": "Define and persist evidence records with explicit provenance and confidence",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T17.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].",
      "Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`."
    ],
    "acceptance_criteria": [
      "Evidence-set digests are stable under deterministic canonical ordering and change when any cited record changes.",
      "Every evidence record resolves to immutable source observations or explicitly labeled external authority.",
      "Unverified findings cannot silently become deterministic evidence.",
      "Superseded evidence remains queryable and cannot satisfy a current-decision policy unless allowed explicitly."
    ],
    "tags": [
      "evidence",
      "confidence",
      "lineage",
      "p1"
    ]
  },
  {
    "task_id": "T17.1.3",
    "title": "Implement evidence-bound promotion decisions and review policy",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T17.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].",
      "Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`."
    ],
    "acceptance_criteria": [
      "Only one current decision is authoritative for a subject/policy scope.",
      "`REJECT` and `HOLD` structurally block publication.",
      "A stale or replayed review command cannot overwrite a newer decision.",
      "The deployment-specific rule for interactive versus automatic review is resolved and documented before publication is enabled."
    ],
    "tags": [
      "review",
      "decision",
      "policy",
      "authority",
      "p1"
    ]
  },
  {
    "task_id": "T17.1.4",
    "title": "Implement staged idempotent publication and bidirectional lineage",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T17.1.2",
      "T17.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].",
      "Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`."
    ],
    "acceptance_criteria": [
      "No publication begins without a current authorized `APPROVE` decision bound to the exact evidence set.",
      "Duplicate requests converge on one verified destination effect or a deterministic conflict.",
      "Unknown outcome is reconciled rather than blindly repeated.",
      "Every verified publication resolves bidirectionally to source root, intake generation, occurrence, exact content, derivations, findings, evidence, decision, actor, policy, and attempt."
    ],
    "tags": [
      "publication",
      "idempotency",
      "review",
      "lineage",
      "p1"
    ]
  },
  {
    "task_id": "T18.1.1",
    "title": "Define the error taxonomy and operation-semantics registry",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T9.1.4",
      "T15.1.4",
      "T17.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.",
      "Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy."
    ],
    "acceptance_criteria": [
      "Every built-in operation has exactly one current, versioned semantics classification.",
      "Unknown/unregistered semantics block automatic retry.",
      "Error codes are stable, serializable, and safe for API/event/log projection.",
      "Policy can prove why an outcome is retryable, blocked, terminal, or requires reconciliation."
    ],
    "tags": [
      "errors",
      "operation-semantics",
      "recovery",
      "p1"
    ]
  },
  {
    "task_id": "T18.1.2",
    "title": "Implement retry, deadline, timeout, and idempotency policy",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T18.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.",
      "Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy."
    ],
    "acceptance_criteria": [
      "Retry decisions are deterministic for the same durable state and policy version.",
      "No unsafe or unknown-outcome operation is automatically retried.",
      "Duplicate idempotency identity returns the prior canonical result or conflict rather than repeating an effect.",
      "Attempt/deadline/backoff state survives process restart."
    ],
    "tags": [
      "retry",
      "timeout",
      "idempotency",
      "deadline",
      "p1"
    ]
  },
  {
    "task_id": "T18.1.3",
    "title": "Implement startup reconciliation and deterministic recovery decisions",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T18.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.",
      "Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy."
    ],
    "acceptance_criteria": [
      "Each nonterminal attempt maps to one persisted recovery disposition.",
      "Unsafe or insufficient evidence becomes `BLOCKED/RECONCILIATION_REQUIRED`, never guessed success.",
      "Repeated startup converges without duplicating the selected action.",
      "Recovery summary identifies exact job/phase/attempt/checkpoint/effect boundary and next operator action."
    ],
    "tags": [
      "startup",
      "reconciliation",
      "recovery",
      "p1"
    ]
  },
  {
    "task_id": "T18.1.4",
    "title": "Build the phase-by-phase crash and replay verification matrix",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T18.1.2",
      "T18.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.",
      "Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy."
    ],
    "acceptance_criteria": [
      "The matrix covers all built-in phases and every declared operation-semantics class.",
      "Each fault point produces exactly the documented recovery disposition across repeated clean runs.",
      "No unsafe side effect is repeated and no unknown outcome is reported as success.",
      "CI publishes machine-readable crash/replay evidence and blocks regressions for mandatory platforms."
    ],
    "tags": [
      "crash",
      "replay",
      "fault-injection",
      "recovery",
      "p1"
    ]
  },
  {
    "task_id": "T19.1.1",
    "title": "Define the daemon lifecycle, configuration, and ownership contract",
    "priority": "P1",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T5.1.4",
      "T9.1.4",
      "T18.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.",
      "Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs."
    ],
    "acceptance_criteria": [
      "Readiness is false until store, migration, recovery, and ownership checks succeed.",
      "Only one valid local owner can advance an attempt.",
      "Drain stops new claims while allowing documented safe completion/cancellation behavior.",
      "Embedded and daemon modes use identical lifecycle/state/policy services."
    ],
    "tags": [
      "daemon",
      "runtime-owner",
      "service",
      "p1"
    ]
  },
  {
    "task_id": "T19.1.2",
    "title": "Implement durable claims, leases, heartbeats, and fenced execution",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T19.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.",
      "Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs."
    ],
    "acceptance_criteria": [
      "Two daemons cannot validly own or commit the same attempt.",
      "A lost lease immediately removes authority at the next guarded boundary.",
      "Stale results are rejected and retained as diagnostic evidence.",
      "Claim recovery follows operation semantics and never blindly re-executes an unknown effect."
    ],
    "tags": [
      "claims",
      "leases",
      "fencing",
      "daemon",
      "p1"
    ]
  },
  {
    "task_id": "T19.1.3",
    "title": "Route CLI and Python controls through canonical command and status services",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T19.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.",
      "Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs."
    ],
    "acceptance_criteria": [
      "A separate CLI process can control a daemon-owned job without private runtime mutation.",
      "Equivalent CLI/Python commands produce identical persisted command and lifecycle results.",
      "Replayed or stale commands return deterministic prior result/conflict.",
      "Compatibility behavior and deprecation window are documented and tested."
    ],
    "tags": [
      "command-service",
      "status-service",
      "cli",
      "python-api",
      "p1"
    ]
  },
  {
    "task_id": "T19.1.4",
    "title": "Verify graceful shutdown, forced restart, and orphan containment",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T19.1.2",
      "T19.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.",
      "Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs."
    ],
    "acceptance_criteria": [
      "Graceful stop leaves no new claims and records deterministic terminal/suspended/checkpoint state.",
      "Forced restart fences the old owner and produces one recovery decision per nonterminal attempt.",
      "Orphan handling cannot terminate an unrelated process.",
      "Runbook and tests cover foreground rollback for new jobs without stealing existing daemon-owned work."
    ],
    "tags": [
      "shutdown",
      "restart",
      "orphan",
      "runbook",
      "p1"
    ]
  },
  {
    "task_id": "T20.1.1",
    "title": "Define structured logging, correlation, error catalog, and redaction",
    "priority": "P1",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T8.1.4",
      "T9.1.4",
      "T18.1.4",
      "T19.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.",
      "Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result."
    ],
    "acceptance_criteria": [
      "Every major lifecycle, control, recovery, policy, and publication action has a stable code and correlation chain.",
      "Redaction occurs before every configured sink and diagnostic export.",
      "Telemetry sink failure cannot change job state or result.",
      "Golden log schema is versioned and compatibility-tested."
    ],
    "tags": [
      "logging",
      "errors",
      "redaction",
      "correlation",
      "p1"
    ]
  },
  {
    "task_id": "T20.1.2",
    "title": "Implement bounded metrics and optional distributed tracing",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T20.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.",
      "Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result."
    ],
    "acceptance_criteria": [
      "Metric names, units, label sets, and bounds are documented and schema-tested.",
      "No mandatory lifecycle path depends on exporter success.",
      "Load tests demonstrate bounded cardinality and memory use for representative workloads.",
      "Trace removal/no-op mode leaves persisted semantics identical."
    ],
    "tags": [
      "metrics",
      "tracing",
      "cardinality",
      "p1"
    ]
  },
  {
    "task_id": "T20.1.3",
    "title": "Build the canonical versioned job status projection",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T20.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.",
      "Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result."
    ],
    "acceptance_criteria": [
      "An operator can identify exact current phase, attempt, checkpoint, control, blocker, retry/recovery action, and provenance completeness without raw DB access.",
      "Status is rebuildable from authoritative state and events are supplemental only.",
      "Legacy/partial/corrupt fields are explicit and never mistaken for complete.",
      "Query performance and pagination are measured on representative large jobs."
    ],
    "tags": [
      "status",
      "projection",
      "progress",
      "p1"
    ]
  },
  {
    "task_id": "T20.1.4",
    "title": "Implement health, readiness, and sanitized diagnostic bundles",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T20.1.2",
      "T20.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.",
      "Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result."
    ],
    "acceptance_criteria": [
      "Health/readiness results are deterministic and identify each failed dependency/control.",
      "Diagnostic bundle verifies against its manifest and records all omissions/degraded collectors.",
      "Synthetic secret/raw-content tests find no prohibited data.",
      "Bundle failure cannot mutate lifecycle state or overwrite an existing file."
    ],
    "tags": [
      "health",
      "readiness",
      "diagnostics",
      "redaction",
      "p1"
    ]
  },
  {
    "task_id": "T21.1.1",
    "title": "Define versioned external command, status, and error schemas",
    "priority": "P2",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T8.1.4",
      "T19.1.4",
      "T20.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.",
      "Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics."
    ],
    "acceptance_criteria": [
      "Equivalent local and external contracts produce identical authoritative command outcomes.",
      "No request field can directly set job/phase/attempt state, fencing, policy result, or publication success.",
      "Replay/stale/version conflicts are deterministic and machine-readable.",
      "Schemas and examples are generated or CI-checked against implementation."
    ],
    "tags": [
      "contracts",
      "commands",
      "status",
      "api-v1",
      "p2"
    ]
  },
  {
    "task_id": "T21.1.2",
    "title": "Implement REST v1 and generate the OpenAPI contract",
    "priority": "P2",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T21.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.",
      "Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics."
    ],
    "acceptance_criteria": [
      "REST and CLI/Python commands converge on the same persisted result for equivalent requests.",
      "OpenAPI is versioned, complete for implemented endpoints, and fails CI on drift.",
      "Client disconnect/retry cannot duplicate authoritative effects.",
      "Disabling/removing REST leaves core job execution and status semantics unchanged."
    ],
    "tags": [
      "rest",
      "openapi",
      "adapter",
      "p2"
    ]
  },
  {
    "task_id": "T21.1.3",
    "title": "Implement outbox-backed RabbitMQ event delivery",
    "priority": "P2",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T21.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.",
      "Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics."
    ],
    "acceptance_criteria": [
      "Broker outage cannot roll back or falsely fail an already committed lifecycle transition.",
      "Delivery retries are bounded and duplicate event IDs/sequences support idempotent consumers.",
      "No replayed event can mutate lifecycle state.",
      "Legacy routing and new envelopes have a tested compatibility/deprecation path."
    ],
    "tags": [
      "rabbitmq",
      "outbox",
      "events",
      "p2"
    ]
  },
  {
    "task_id": "T21.1.4",
    "title": "Implement signed idempotent webhook notifications",
    "priority": "P2",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T21.1.2",
      "T21.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.",
      "Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics."
    ],
    "acceptance_criteria": [
      "Receivers can verify authenticity, schema version, event identity, and replay window.",
      "Duplicate delivery is expected and safely identifiable.",
      "Webhook failure never changes lifecycle state or loses durable event history.",
      "SSRF/redirect/rebinding tests demonstrate deployment-policy enforcement."
    ],
    "tags": [
      "webhooks",
      "signatures",
      "notifications",
      "p2"
    ]
  },
  {
    "task_id": "T22.1.1",
    "title": "Define the subprocess protocol and mediated artifact contract",
    "priority": "P2",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T14.1.4",
      "T15.1.4",
      "T16.1.4",
      "T18.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.",
      "Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator."
    ],
    "acceptance_criteria": [
      "Subprocess cannot receive StateStore credentials or undeclared source/workspace paths through the protocol/environment.",
      "Malformed or forged protocol messages fail the attempt without lifecycle mutation.",
      "Equivalent trusted plugin results normalize identically in in-process and subprocess backends.",
      "Protocol compatibility and capability negotiation are versioned and tested."
    ],
    "tags": [
      "subprocess",
      "protocol",
      "mediated-artifacts",
      "p2"
    ]
  },
  {
    "task_id": "T22.1.2",
    "title": "Implement deterministic process lifecycle, timeout, and tree termination",
    "priority": "P2",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T22.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.",
      "Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator."
    ],
    "acceptance_criteria": [
      "Timeout/cancel kills and reaps the entire controlled process tree on supported platforms.",
      "Late or stale results cannot commit after fencing/cancellation.",
      "Unsupported containment controls are explicit in status and release evidence.",
      "No zombie, leaked handle, or unbounded output remains after hostile fixtures."
    ],
    "tags": [
      "process-supervisor",
      "timeout",
      "tree-kill",
      "p2"
    ]
  },
  {
    "task_id": "T22.1.3",
    "title": "Enforce subprocess resource, network, tool, and secret policy",
    "priority": "P2",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T22.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.",
      "Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator."
    ],
    "acceptance_criteria": [
      "Each subprocess attempt records requested, enforced, unavailable, and exceeded controls plus measured usage.",
      "Network/tools/secrets are absent unless explicitly granted by deterministic policy.",
      "Required unavailable controls block untrusted execution rather than silently weakening policy.",
      "Tool and command-injection tests show no shell interpretation of plugin-controlled values."
    ],
    "tags": [
      "resource-limits",
      "capabilities",
      "network",
      "secrets",
      "p2"
    ]
  },
  {
    "task_id": "T22.1.4",
    "title": "Establish hostile-plugin and backend conformance gates",
    "priority": "P2",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T22.1.2",
      "T22.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.",
      "Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator."
    ],
    "acceptance_criteria": [
      "Every supported platform has a current pass/fail/reduced-assurance enforcement matrix.",
      "Hostile fixtures cannot commit lifecycle state or escape mediated inputs under claimed controls.",
      "Cleanup and resource-accounting assertions pass after every failure class.",
      "No unsupported control is marketed as enforced and no mandatory isolation test is silently skipped."
    ],
    "tags": [
      "hostile-plugin",
      "conformance",
      "ci-gate",
      "p2"
    ]
  },
  {
    "task_id": "T23.1.1",
    "title": "Define retention classes and implement reference-safe cleanup",
    "priority": "P2",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T12.1.4",
      "T17.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "Retention periods and required preserved classes are explicitly resolved and versioned before deletion is enabled.",
      "Dry-run and execution use the same immutable plan or fail on changed preconditions.",
      "No referenced, held, active, or unknown-ownership object is deleted.",
      "Interrupted cleanup is idempotently reconciled with durable per-object evidence."
    ],
    "tags": [
      "retention",
      "garbage-collection",
      "cleanup",
      "p2"
    ]
  },
  {
    "task_id": "T23.1.2",
    "title": "Implement the compatibility catalog and deprecation telemetry",
    "priority": "P2",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T3.1.4",
      "T4.1.4",
      "T8.1.4",
      "T14.1.4",
      "T18.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "Every persisted/public contract has one catalog entry and explicit read/write/deprecation policy.",
      "Unsupported or lossy authority-bearing conversions fail closed with actionable status.",
      "Compatibility reports identify affected records/plugins/configurations before upgrade.",
      "Deprecation removal requires evidence that migration and rollback gates passed."
    ],
    "tags": [
      "compatibility",
      "schema",
      "deprecation",
      "p2"
    ]
  },
  {
    "task_id": "T23.1.3",
    "title": "Deliver the plugin SDK, fixtures, and contract-validation CLI",
    "priority": "P2",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T14.1.4",
      "T15.1.4",
      "T22.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "A third party can implement and validate a plugin without importing private runtime/persistence APIs.",
      "Contract CLI reports exact failed section, capability, compatibility, and remediation guidance.",
      "Examples pass the same registry/backend conformance tests as built-ins.",
      "Untrusted validation cannot mutate lifecycle state or access undeclared resources."
    ],
    "tags": [
      "plugin-sdk",
      "developer-experience",
      "contracts",
      "p2"
    ]
  },
  {
    "task_id": "T23.1.4",
    "title": "Define the source-provider extension contract and defer unsupported providers",
    "priority": "P2",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T6.1.4",
      "T10.1.4",
      "T14.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.",
      "This is a planning decomposition/new support capability, not a claim that the current repository implements it."
    ],
    "acceptance_criteria": [
      "Local provider passes the contract without changing accepted local semantics.",
      "Any provider lacking stable observation/mutation semantics is rejected or explicitly reduced-assurance, not silently accepted.",
      "Deferred providers are named as non-implemented and have measurable admission criteria.",
      "Provider removal leaves persisted source/intake/occurrence/content records readable."
    ],
    "tags": [
      "source-provider",
      "registry",
      "defer",
      "p2"
    ]
  },
  {
    "task_id": "T24.1.1",
    "title": "Define the supported-platform matrix and mandatory CI policy",
    "priority": "P1",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T2.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.",
      "Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts."
    ],
    "acceptance_criteria": [
      "Supported and reduced-assurance platforms are explicitly resolved and versioned.",
      "Every mandatory job blocks release and unapproved skips fail policy.",
      "CI reports what is not covered and does not use blanket production-ready claims.",
      "Clean reruns preserve deterministic configuration and evidence metadata."
    ],
    "tags": [
      "ci",
      "platform-matrix",
      "quality-gates",
      "p1"
    ]
  },
  {
    "task_id": "T24.1.2",
    "title": "Add state-machine, migration, crash, adversarial, compatibility, and fuzz gates",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T5.1.4",
      "T11.1.4",
      "T18.1.4",
      "T22.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.",
      "Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts."
    ],
    "acceptance_criteria": [
      "Each major lifecycle/safety/recovery contract has an assigned mandatory test family and CI job.",
      "Regression fixtures are deterministic, licensed/provenanced, bounded, and sanitized.",
      "No unapproved skip or flaky quarantine permits release.",
      "Failures produce actionable minimized evidence without leaking sensitive input."
    ],
    "tags": [
      "property-tests",
      "fuzz",
      "adversarial",
      "migration",
      "p1"
    ]
  },
  {
    "task_id": "T24.1.3",
    "title": "Produce reproducible packages, SBOMs, provenance, and integrity manifests",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T24.1.1",
      "T4.1.4",
      "T23.1.2"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.",
      "Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts."
    ],
    "acceptance_criteria": [
      "Clean wheel/sdist install and smoke tests pass with recorded tool/dependency versions.",
      "Release bundle includes hashes, SBOM, license, provenance, security/dependency report, and coverage limitations.",
      "Reproducibility comparison is automated and any variance is documented and bounded.",
      "Publishing cannot proceed if integrity/provenance or mandatory tests fail."
    ],
    "tags": [
      "packaging",
      "sbom",
      "provenance",
      "reproducible-build",
      "p1"
    ]
  },
  {
    "task_id": "T24.1.4",
    "title": "Build representative benchmarks, soak tests, and release rollback evidence",
    "priority": "P1",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T24.1.2",
      "T24.1.3",
      "T23.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.",
      "Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts."
    ],
    "acceptance_criteria": [
      "Every performance claim names workload, environment, metric, raw evidence, and confidence/limitation.",
      "Semantic and integrity tests run alongside benchmark optimizations.",
      "Release bundle contains mandatory test reports, benchmark raw data, migration/restore/rollback evidence, hashes, and operator notes.",
      "A failed mandatory gate or rollback drill blocks release."
    ],
    "tags": [
      "benchmarks",
      "soak",
      "rollback",
      "release-evidence",
      "p1"
    ]
  },
  {
    "task_id": "T25.1.1",
    "title": "Define and approve quantitative scale-adapter trigger evidence",
    "priority": "P3",
    "estimated_hours": "12h",
    "owner": "@unassigned",
    "dependencies": [
      "T4.1.4",
      "T12.1.4",
      "T18.1.4",
      "T24.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.",
      "Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version."
    ],
    "acceptance_criteria": [
      "Trigger criteria, measurement procedure, and decision authority are resolved and versioned.",
      "Raw evidence demonstrates a specific local limitation and the proposed adapter addresses it.",
      "Simpler local optimizations are tested or explicitly rejected with evidence.",
      "A no-go result keeps adapter tasks deferred without being treated as failure."
    ],
    "tags": [
      "scale-trigger",
      "benchmark",
      "decision",
      "p3"
    ]
  },
  {
    "task_id": "T25.1.2",
    "title": "Finalize backend conformance and one-authority migration contracts",
    "priority": "P3",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T25.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.",
      "Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version."
    ],
    "acceptance_criteria": [
      "Conformance suites are backend-neutral and pass for SQLite/local content before alternate implementation.",
      "Migration protocol makes writable authority explicit and prevents dual writers.",
      "Verification manifest covers all authority-bearing rows/blobs and lineage.",
      "Rollback feasibility and cutoff are explicit before cutover."
    ],
    "tags": [
      "conformance",
      "migration",
      "single-authority",
      "p3"
    ]
  },
  {
    "task_id": "T25.1.3",
    "title": "Implement and validate the optional PostgreSQL StateStore",
    "priority": "P3",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T25.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.",
      "Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version."
    ],
    "acceptance_criteria": [
      "PostgreSQL passes the same StateStore, state-machine, crash, event, claim, idempotency, migration, and status tests as SQLite.",
      "Cutover/rollback drill preserves counts, identities, constraints, sequence, event order, and hashes.",
      "One writable backend authority is enforced at startup and during migration.",
      "Measured workload shows the approved benefit without changing lifecycle semantics."
    ],
    "tags": [
      "postgresql",
      "state-store",
      "migration",
      "p3"
    ]
  },
  {
    "task_id": "T25.1.4",
    "title": "Implement and validate the optional object-backed ContentStore",
    "priority": "P3",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T25.1.2",
      "T25.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.",
      "Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version."
    ],
    "acceptance_criteria": [
      "Object backend passes immutable ContentStore, integrity, reference, retention, recovery, and replay tests.",
      "No-replace commit and byte verification prevent canonical-key corruption.",
      "Migration/cutover/rollback preserves all referenced content hashes and one writable authority.",
      "Approved workload demonstrates benefit and provider consistency limitations are explicit."
    ],
    "tags": [
      "object-storage",
      "content-store",
      "migration",
      "p3"
    ]
  },
  {
    "task_id": "T26.1.1",
    "title": "Define the authenticated remote worker protocol and compatibility handshake",
    "priority": "P3",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T15.1.4",
      "T18.1.4",
      "T21.1.4",
      "T25.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.",
      "Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens."
    ],
    "acceptance_criteria": [
      "Protocol is versioned and compatibility failure is explicit before work starts.",
      "Worker cannot mutate lifecycle state or access undeclared artifacts.",
      "Stale/duplicate/forged results are rejected deterministically and retained as evidence.",
      "Local and remote backends share WorkSpec/result conformance semantics."
    ],
    "tags": [
      "remote-worker",
      "protocol",
      "identity",
      "p3"
    ]
  },
  {
    "task_id": "T26.1.2",
    "title": "Implement the least-privileged remote worker service",
    "priority": "P3",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T26.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.",
      "Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens."
    ],
    "acceptance_criteria": [
      "Worker completes only authenticated assigned WorkSpecs and cannot write lifecycle authority.",
      "All input/output bytes are hash-verified and scoped to the attempt.",
      "Lease loss/cancel/drain leads to deterministic backend stop/result handling.",
      "Compromise/revocation can fence the worker and preserve investigation evidence."
    ],
    "tags": [
      "worker-service",
      "least-privilege",
      "artifacts",
      "p3"
    ]
  },
  {
    "task_id": "T26.1.3",
    "title": "Implement remote scheduling, result verification, cancellation, and fallback policy",
    "priority": "P3",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T26.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.",
      "Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens."
    ],
    "acceptance_criteria": [
      "One valid fenced result can commit for each work attempt.",
      "Worker loss maps to deterministic wait/retry/reconcile/block behavior from operation semantics.",
      "Fallback/reassignment is disabled for unsafe/unknown side effects and never weakens policy.",
      "Remote execution preserves the same phase barriers, persistence, events, lineage, and status as local execution."
    ],
    "tags": [
      "remote-scheduler",
      "result-verification",
      "fallback",
      "p3"
    ]
  },
  {
    "task_id": "T26.1.4",
    "title": "Gate distributed execution with chaos, security, load, and operational evidence",
    "priority": "P3",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T26.1.2",
      "T26.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.",
      "Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens."
    ],
    "acceptance_criteria": [
      "Remote backend passes all local backend/state/recovery/lineage conformance suites.",
      "Chaos matrix demonstrates stale fencing and no duplicate authoritative effects.",
      "Benchmark and operations evidence justify distributed complexity for a defined workload.",
      "Drain/rollback/revocation drill handles in-flight work without alternate authority."
    ],
    "tags": [
      "chaos",
      "distributed",
      "load",
      "rollout",
      "p3"
    ]
  },
  {
    "task_id": "T27.1.1",
    "title": "Expose read-only and proposal-only MCP resources and tools",
    "priority": "P3",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T17.1.4",
      "T19.1.4",
      "T20.1.4",
      "T21.1.4"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.",
      "Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records."
    ],
    "acceptance_criteria": [
      "MCP read/proposal tools cannot mutate lifecycle state, safety records, evidence authority, decisions, or publications.",
      "Every proposal is visibly non-authoritative and provenance-versioned.",
      "Hostile artifact text cannot create an unrequested tool call or expand capabilities.",
      "Removing/disabling MCP leaves core semantics and data readable."
    ],
    "tags": [
      "mcp",
      "ai",
      "proposal",
      "read-only",
      "p3"
    ]
  },
  {
    "task_id": "T27.1.2",
    "title": "Route consequential MCP actions through deterministic command and review gates",
    "priority": "P3",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T27.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.",
      "Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records."
    ],
    "acceptance_criteria": [
      "No MCP command bypasses CommandService, lifecycle guards, review policy, publication checks, or expected-version/idempotency.",
      "Prompt-injected artifact text cannot authorize or alter a tool action.",
      "AI-only output cannot create an approved PromotionDecision.",
      "Replay, stale state, revoked session, and changed confirmation return deterministic non-success outcomes."
    ],
    "tags": [
      "mcp",
      "commands",
      "prompt-injection",
      "governance",
      "p3"
    ]
  },
  {
    "task_id": "T27.1.3",
    "title": "Build an operator UI that preserves authority and uncertainty distinctions",
    "priority": "P3",
    "estimated_hours": "16h",
    "owner": "@unassigned",
    "dependencies": [
      "T27.1.1"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.",
      "Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records."
    ],
    "acceptance_criteria": [
      "UI never labels a finding/proposal as evidence, a request as decision, or an attempt as verified publication.",
      "All commands traverse canonical APIs and reject stale/replayed input.",
      "Hostile rendered content cannot execute or create unauthorized navigation/actions.",
      "Accessibility, large-job performance, partial outage, and compatibility behavior are tested."
    ],
    "tags": [
      "operator-ui",
      "authority-labels",
      "accessibility",
      "p3"
    ]
  },
  {
    "task_id": "T27.1.4",
    "title": "Resolve tenant, authentication, authorization, and deployment-governance scope",
    "priority": "P3",
    "estimated_hours": "14h",
    "owner": "@unassigned",
    "dependencies": [
      "T27.1.2",
      "T27.1.3"
    ],
    "evidence": [
      "Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.",
      "Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.",
      "Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.",
      "Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records."
    ],
    "acceptance_criteria": [
      "Deployment identity/tenancy requirements, non-goals, and decision authority are evidenced and approved.",
      "Selected adapters preserve core semantics and local mode remains safe and documented.",
      "If multi-tenancy is required, isolation is modeled across state, content, events, caches, workers, diagnostics, and publications before implementation.",
      "Auth/policy outage, revocation, and rollback behavior are deterministic and tested."
    ],
    "tags": [
      "identity",
      "authorization",
      "tenancy",
      "governance",
      "p3"
    ]
  }
]
```
