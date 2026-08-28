@BinReaper Production TODOs

## TODO

* [ ] TODO 97: Define and approve quantitative scale-adapter trigger evidence

  1.2 source task(s): `T25.1.1`
  Priority: `P3`
  Estimated effort: `12 hours`
  Dependencies: `T4.1.4, T12.1.4, T18.1.4, T24.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `docs/decisions/scale-adapter-trigger.md (create); benchmarks/scale_triggers/ (create); atlas/config/scale.py (create); ATLAS_Production_Task_Crosswalk.csv (extend)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Require a workload-specific decision record showing why SQLite or local content storage fails measured contention, capacity, durability, recovery, availability, or multi-host requirements before adapter implementation begins.
  * Restore or protect this invariant: Trigger criteria, measurement procedure, and decision authority are resolved and versioned.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `docs/decisions/scale-adapter-trigger.md` (create: Record workload, environment, measurements, alternatives, cost, risks, and decision.); `benchmarks/scale_triggers/` (create: Retain repeatable local-backend workloads and raw results.); `atlas/config/scale.py` (create: Represent selected backend only after an approved compatibility decision.); `ATLAS_Production_Task_Crosswalk.csv` (extend: Link trigger evidence to deferred adapter tasks and original AT-021.)
  * Epic boundary: Measured optional PostgreSQL and object-storage adapters — Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.
  * Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-021 requires: Additional stores are justified only when SQLite/local CAS fail defined workloads while semantics are already stable.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Require a workload-specific decision record showing why SQLite or local content storage fails measured contention, capacity, durability, recovery, availability, or multi-host requirements before adapter implementation begins.
  * Component dispositions: `docs/decisions/scale-adapter-trigger.md` (create: Record workload, environment, measurements, alternatives, cost, risks, and decision.); `benchmarks/scale_triggers/` (create: Retain repeatable local-backend workloads and raw results.); `atlas/config/scale.py` (create: Represent selected backend only after an approved compatibility decision.); `ATLAS_Production_Task_Crosswalk.csv` (extend: Link trigger evidence to deferred adapter tasks and original AT-021.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define candidate triggers: write/read contention, dataset/row/blob size, recovery objective, multi-host coordination, storage durability/availability, operational backup, and lifecycle cost.
  * Benchmark/soak the local backends under the actual target workload and identify the bottleneck with raw evidence.
  * Compare logic/index/batching/checkpoint/retention improvements before infrastructure replacement.
  * Record selected/no-go decision, expected measurable benefit, complexity/operational cost, compatibility, migration, rollback, and disproof criteria.

  Security and safety requirements

  * Do not put production data/secrets into benchmark artifacts.
  * A vendor/backend choice cannot override lifecycle, provenance, event, or safety invariants.
  * Record deployment IAM/TLS/secret requirements separately from core semantics.
  * Reject pressure to implement scale adapters from terminology, fashion, or an arbitrary task completion target.

  Edge cases and outliers to handle

  * No local workload reproduces the claimed bottleneck.
  * Benchmark bottleneck is filesystem/analyzer rather than database/store.
  * Multi-host requirement appears before remote-worker semantics are ready.
  * Measurements vary by hardware or cache.

  Acceptance criteria (“done” definition)

  * Trigger criteria, measurement procedure, and decision authority are resolved and versioned.
  * Raw evidence demonstrates a specific local limitation and the proposed adapter addresses it.
  * Simpler local optimizations are tested or explicitly rejected with evidence.
  * A no-go result keeps adapter tasks deferred without being treated as failure.

  Testing plan

  * Benchmark repeatability tests.
  * Bottleneck attribution experiments.
  * Semantic equivalence checks under local optimizations.
  * Decision-record completeness validation.
  * Secret/provenance scans.
  * Independent review/reproduction.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Benchmark repeatability tests., Bottleneck attribution experiments., Semantic equivalence checks under local optimizations., Decision-record completeness validation., Secret/provenance scans., Independent review/reproduction..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T25.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: docs/decisions/scale-adapter-trigger.md, benchmarks/scale_triggers/, atlas/config/scale.py, ATLAS_Production_Task_Crosswalk.csv.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 98: Finalize backend conformance and one-authority migration contracts

  1.2 source task(s): `T25.1.2`
  Priority: `P3`
  Estimated effort: `14 hours`
  Dependencies: `T25.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/conformance.py (extend); atlas/storage/conformance.py (extend); atlas/migration/backend.py (create); docs/architecture/backend-conformance.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify the exact semantic, transactional, consistency, backup, cutover, and rollback obligations that any alternate StateStore or ContentStore must pass unchanged.
  * Restore or protect this invariant: Conformance suites are backend-neutral and pass for SQLite/local content before alternate implementation.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/persistence/conformance.py` (extend: Cover transactions, locks, migrations, events, claims, idempotency, recovery, and queries.); `atlas/storage/conformance.py` (extend: Cover immutable writes, hash verification, references, reconciliation, and retention.); `atlas/migration/backend.py` (create: Define copy, verify, freeze/cutover, authority marker, and rollback protocols.); `docs/architecture/backend-conformance.md` (create: Document consistency model and no-dual-writer invariant.)
  * Epic boundary: Measured optional PostgreSQL and object-storage adapters — Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.
  * Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-021 requires: Additional stores are justified only when SQLite/local CAS fail defined workloads while semantics are already stable.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify the exact semantic, transactional, consistency, backup, cutover, and rollback obligations that any alternate StateStore or ContentStore must pass unchanged.
  * Component dispositions: `atlas/persistence/conformance.py` (extend: Cover transactions, locks, migrations, events, claims, idempotency, recovery, and queries.); `atlas/storage/conformance.py` (extend: Cover immutable writes, hash verification, references, reconciliation, and retention.); `atlas/migration/backend.py` (create: Define copy, verify, freeze/cutover, authority marker, and rollback protocols.); `docs/architecture/backend-conformance.md` (create: Document consistency model and no-dual-writer invariant.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define exact StateStore isolation/transaction/constraint/sequence/locking/time semantics and ContentStore integrity/read-after-write/list/delete semantics.
  * Define source and target schema/provider version compatibility, snapshot/copy strategy, verification manifest, maintenance/read-only window, and authority marker.
  * Require one writable authoritative backend at a time; shadow copies remain non-authoritative until verified cutover.
  * Define rollback preconditions after new writes and how copied/unknown objects are retained/reconciled.

  Security and safety requirements

  * Prevent split-brain through a deployment authority token/config digest and startup refusal on conflicting writable backends.
  * Use least-privilege migration credentials, encrypted transport where external, and secret references.
  * Verify row/blob counts, identities, hashes, constraints, lineage, decisions, events, and checkpoints before cutover.
  * Do not accept eventual consistency where a core invariant requires read-after-write without an explicit adapter mechanism.

  Edge cases and outliers to handle

  * Partial snapshot/copy.
  * Writes occur during verification.
  * Source and target clocks/order semantics differ.
  * Rollback target cannot represent new schema records.

  Acceptance criteria (“done” definition)

  * Conformance suites are backend-neutral and pass for SQLite/local content before alternate implementation.
  * Migration protocol makes writable authority explicit and prevents dual writers.
  * Verification manifest covers all authority-bearing rows/blobs and lineage.
  * Rollback feasibility and cutoff are explicit before cutover.

  Testing plan

  * Reference-backend conformance tests.
  * Authority-marker/split-brain negative tests.
  * Partial copy/write-race fault tests.
  * Consistency/order/transaction tests.
  * Verification manifest tests.
  * Rollback cutoff compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Reference-backend conformance tests., Authority-marker/split-brain negative tests., Partial copy/write-race fault tests., Consistency/order/transaction tests., Verification manifest tests., Rollback cutoff compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T25.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/conformance.py, atlas/storage/conformance.py, atlas/migration/backend.py, docs/architecture/backend-conformance.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 99: Implement and validate the optional PostgreSQL StateStore

  1.2 source task(s): `T25.1.3`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T25.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/postgres.py::PostgresStateStore (create); atlas/schema/postgres/ (create); atlas/config/persistence.py (extend); tests/persistence/test_postgres_conformance.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Add PostgreSQL only behind the proven StateStore contract with equivalent transitions, transactions, events, claims, recovery, migrations, and diagnostics.
  * Restore or protect this invariant: PostgreSQL passes the same StateStore, state-machine, crash, event, claim, idempotency, migration, and status tests as SQLite.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/persistence/postgres.py::PostgresStateStore` (create: Implement StateStore with explicit transaction and connection ownership.); `atlas/schema/postgres/` (create: Provide versioned PostgreSQL migrations with parity mapping.); `atlas/config/persistence.py` (extend: Select one backend with typed DSN secret reference and pool settings.); `tests/persistence/test_postgres_conformance.py` (create: Run full conformance, fault, migration, and load suites.)
  * Epic boundary: Measured optional PostgreSQL and object-storage adapters — Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.
  * Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-021 requires: Additional stores are justified only when SQLite/local CAS fail defined workloads while semantics are already stable.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Add PostgreSQL only behind the proven StateStore contract with equivalent transitions, transactions, events, claims, recovery, migrations, and diagnostics.
  * Component dispositions: `atlas/persistence/postgres.py::PostgresStateStore` (create: Implement StateStore with explicit transaction and connection ownership.); `atlas/schema/postgres/` (create: Provide versioned PostgreSQL migrations with parity mapping.); `atlas/config/persistence.py` (extend: Select one backend with typed DSN secret reference and pool settings.); `tests/persistence/test_postgres_conformance.py` (create: Run full conformance, fault, migration, and load suites.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Implement transactions, guarded transitions, sequence allocation, outbox, claims/leases/fencing, idempotency, checkpoints, lineage queries, and migration locks under documented isolation.
  * Use bounded connection pool/lifecycle, timeouts, cancellation, retryable transaction handling, and health/readiness.
  * Implement SQLite-to-PostgreSQL snapshot/copy/verify/cutover tooling using the one-authority contract.
  * Document backup/restore, maintenance, upgrades, operational dependencies, and rollback cutoff.

  Security and safety requirements

  * Require TLS/credential/role/schema isolation as deployment controls and secret references rather than config plaintext.
  * Use parameterized SQL and bounded queries; test injection and denial-of-service inputs.
  * Fence duplicate coordinators and handle serializable/deadlock retries only when operation transaction semantics permit.
  * Do not expose database credentials to plugins, workers, events, or diagnostics.

  Edge cases and outliers to handle

  * Network partition or failover during commit.
  * Deadlock/serialization failure.
  * Pool exhaustion or long transaction.
  * Migration partially applies or old runtime reconnects.

  Acceptance criteria (“done” definition)

  * PostgreSQL passes the same StateStore, state-machine, crash, event, claim, idempotency, migration, and status tests as SQLite.
  * Cutover/rollback drill preserves counts, identities, constraints, sequence, event order, and hashes.
  * One writable backend authority is enforced at startup and during migration.
  * Measured workload shows the approved benefit without changing lifecycle semantics.

  Testing plan

  * StateStore conformance suite.
  * Network/failover/deadlock fault tests.
  * Pool/contention/load tests.
  * Migration/cutover/rollback tests.
  * SQL injection/credential-redaction tests.
  * SQLite/PostgreSQL semantic differential tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: StateStore conformance suite., Network/failover/deadlock fault tests., Pool/contention/load tests., Migration/cutover/rollback tests., SQL injection/credential-redaction tests., SQLite/PostgreSQL semantic differential tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T25.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/postgres.py::PostgresStateStore, atlas/schema/postgres/, atlas/config/persistence.py, tests/persistence/test_postgres_conformance.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
