@BinReaper Production TODOs

## TODO

* [ ] TODO 13: Define the narrow `StateStore` transaction and repository contracts

  1.2 source task(s): `T4.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T2.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/base.py::StateStore (create); atlas/core/job_store.py::JobStore (refactor); atlas/persistence/errors.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Separate lifecycle semantics from aiosqlite details while assigning explicit transaction ownership and error taxonomy to one persistence boundary.
  * Restore or protect this invariant: No authoritative repository method commits outside a `StateStore` transaction.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15.

  Where this applies

  * Primary affected components: `atlas/persistence/base.py::StateStore` (create: Define transaction, repository, and capability protocols.); `atlas/core/job_store.py::JobStore` (refactor: Retain as compatibility facade over the new repositories.); `atlas/persistence/errors.py` (create: Normalize contention, integrity, schema, and I/O failures.)
  * Epic boundary: StateStore and SQLite migration foundation — Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]
  * Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-003 requires: Inline schema creation, independent commits, and absent schema versioning prevent safe evolution of authoritative records.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Separate lifecycle semantics from aiosqlite details while assigning explicit transaction ownership and error taxonomy to one persistence boundary.
  * Component dispositions: `atlas/persistence/base.py::StateStore` (create: Define transaction, repository, and capability protocols.); `atlas/core/job_store.py::JobStore` (refactor: Retain as compatibility facade over the new repositories.); `atlas/persistence/errors.py` (create: Normalize contention, integrity, schema, and I/O failures.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define async transaction context, read/write repository interfaces, isolation expectations, commit/rollback ownership, and nested-transaction prohibition or savepoint rules.
  * Separate repositories for jobs, phase runs, attempts, events, controls, checkpoints, artifacts, and later records without exposing raw connections.
  * Define stable persistence error codes and retryability hints without making retry decisions inside the store.
  * Create a backend conformance contract that SQLite and future PostgreSQL must satisfy.

  Security and safety requirements

  * Use parameterized SQL only and never expose raw SQL execution to plugins, adapters, or model-controlled input.
  * Database paths must be canonical, outside source roots, and created with restrictive permissions.
  * Transaction APIs must not allow partial authoritative writes after an exception.
  * Unknown integrity or schema errors fail closed and retain diagnostics.

  Edge cases and outliers to handle

  * Nested service calls attempt independent commits.
  * Cancellation occurs during commit or rollback.
  * Connection is lost or closed while a transaction is active.
  * A future backend cannot provide identical locking semantics.

  Acceptance criteria (“done” definition)

  * No authoritative repository method commits outside a `StateStore` transaction.
  * `JobStore` compatibility calls delegate without changing public results.
  * The error taxonomy distinguishes contention, corruption, schema mismatch, constraint, cancellation, and storage exhaustion.
  * A backend conformance test skeleton covers transaction atomicity and rollback.

  Testing plan

  * Protocol/type-check tests.
  * Transaction commit/rollback unit tests.
  * Nested-call and cancellation tests.
  * Parameterized-query/static checks.
  * Compatibility facade tests.
  * Backend conformance contract tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Protocol/type-check tests., Transaction commit/rollback unit tests., Nested-call and cancellation tests., Parameterized-query/static checks., Compatibility facade tests., Backend conformance contract tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T4.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/base.py::StateStore, atlas/core/job_store.py::JobStore, atlas/persistence/errors.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 14: Implement the SQLite backend with explicit connection and locking policy

  1.2 source task(s): `T4.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T4.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/sqlite.py::SQLiteStateStore (create); atlas/persistence/sqlite_repositories.py (create); atlas/core/job_store.py (migrate)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide the reference backend with foreign keys, WAL/rollback policy, busy timeout, connection lifecycle, contention behavior, and health diagnostics defined rather than implicit.
  * Restore or protect this invariant: Foreign keys and uniqueness constraints are enabled and demonstrated.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15.

  Where this applies

  * Primary affected components: `atlas/persistence/sqlite.py::SQLiteStateStore` (create: Own SQLite connections and transactions.); `atlas/persistence/sqlite_repositories.py` (create: Implement repository contracts.); `atlas/core/job_store.py` (migrate: Route all writes through SQLiteStateStore.)
  * Epic boundary: StateStore and SQLite migration foundation — Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]
  * Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-003 requires: Inline schema creation, independent commits, and absent schema versioning prevent safe evolution of authoritative records.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Provide the reference backend with foreign keys, WAL/rollback policy, busy timeout, connection lifecycle, contention behavior, and health diagnostics defined rather than implicit.
  * Component dispositions: `atlas/persistence/sqlite.py::SQLiteStateStore` (create: Own SQLite connections and transactions.); `atlas/persistence/sqlite_repositories.py` (create: Implement repository contracts.); `atlas/core/job_store.py` (migrate: Route all writes through SQLiteStateStore.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Configure and verify foreign keys, journal mode, synchronous level, busy timeout, row factory, and connection ownership at startup.
  * Use explicit transaction modes for read and write paths and document lock acquisition order.
  * Implement bounded contention retry signaling without hidden infinite loops.
  * Expose integrity, schema, lock-wait, file-permission, and capacity health information.

  Security and safety requirements

  * Reject database files or parent directories under untrusted source roots.
  * Avoid permissive file modes and unsafe temporary database locations.
  * Do not log SQL parameter values that may contain source paths, secrets, or payload text.
  * Corruption and unsupported pragmas fail readiness rather than degrade silently.

  Edge cases and outliers to handle

  * Two writers contend while a long reader is active.
  * Filesystem does not support requested journal behavior.
  * Disk fills during journal or commit.
  * Process is terminated while WAL contains committed but uncheckpointed data.

  Acceptance criteria (“done” definition)

  * Foreign keys and uniqueness constraints are enabled and demonstrated.
  * Contention yields bounded, classified behavior with lock-wait metrics.
  * All existing job/phase persistence tests pass through the new backend.
  * Startup reports actual SQLite capabilities and refuses unsafe/unsupported state.

  Testing plan

  * SQLite conformance tests.
  * Concurrent reader/writer contention tests.
  * Foreign-key and constraint negative tests.
  * Disk-full and permission fault tests.
  * WAL recovery tests.
  * Connection-leak and shutdown tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: SQLite conformance tests., Concurrent reader/writer contention tests., Foreign-key and constraint negative tests., Disk-full and permission fault tests., WAL recovery tests., Connection-leak and shutdown tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T4.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/sqlite.py::SQLiteStateStore, atlas/persistence/sqlite_repositories.py, atlas/core/job_store.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 15: Create immutable numbered migrations and the v0.1 upgrade path

  1.2 source task(s): `T4.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T4.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/migrations/ (create); atlas/schema/__init__.py (refactor); schema_migrations table (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace inline schema creation with checksummed, forward-applied migrations and deterministic schema fingerprints for fresh and upgraded databases.
  * Restore or protect this invariant: Fresh and upgraded databases have identical schema fingerprints and invariants.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15.

  Where this applies

  * Primary affected components: `atlas/persistence/migrations/` (create: Store immutable numbered migration modules or SQL.); `atlas/schema/__init__.py` (refactor: Export schema version and migration APIs.); `schema_migrations table` (create: Record version, checksum, tool version, and application result.)
  * Epic boundary: StateStore and SQLite migration foundation — Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]
  * Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-003 requires: Inline schema creation, independent commits, and absent schema versioning prevent safe evolution of authoritative records.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace inline schema creation with checksummed, forward-applied migrations and deterministic schema fingerprints for fresh and upgraded databases.
  * Component dispositions: `atlas/persistence/migrations/` (create: Store immutable numbered migration modules or SQL.); `atlas/schema/__init__.py` (refactor: Export schema version and migration APIs.); `schema_migrations table` (create: Record version, checksum, tool version, and application result.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define migration discovery, ordering, checksums, schema metadata, supported version range, and no-edit rule for applied migrations.
  * Write the initial baseline and v0.1-to-target migrations for existing jobs, phases, selected events, and required constraints.
  * Compute a canonical schema fingerprint and verify fresh versus upgraded convergence.
  * Record migration events only after successful schema/data verification.

  Security and safety requirements

  * Never auto-downgrade or run against a newer unknown schema.
  * Checksum drift, missing migration, or duplicate version fails startup.
  * Migrations use bounded data transforms and parameterized operations.
  * Sensitive row values are not written to migration logs.

  Edge cases and outliers to handle

  * Empty database, current v0.1 database, partially initialized database.
  * Migration file edited after prior application.
  * Process termination between DDL and data transform.
  * Large legacy tables exceed memory if transformed eagerly.

  Acceptance criteria (“done” definition)

  * Fresh and upgraded databases have identical schema fingerprints and invariants.
  * Migration checksums are immutable and verified on every startup.
  * Newer unsupported schema and checksum drift fail with stable diagnostics.
  * Every migration has forward test fixtures and a documented restore-based rollback.

  Testing plan

  * Fresh-install migration tests.
  * Every-version upgrade tests.
  * Schema fingerprint comparison.
  * Checksum-drift and missing-version negative tests.
  * Large-row streaming migration tests.
  * Process-kill fault injection at each migration boundary.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Fresh-install migration tests., Every-version upgrade tests., Schema fingerprint comparison., Checksum-drift and missing-version negative tests., Large-row streaming migration tests., Process-kill fault injection at each migration boundary..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T4.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/migrations/, atlas/schema/__init__.py, schema_migrations table.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
