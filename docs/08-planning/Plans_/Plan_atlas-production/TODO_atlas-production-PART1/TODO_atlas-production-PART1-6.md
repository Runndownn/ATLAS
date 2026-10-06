@BinReaper Production TODOs

## TODO

* [ ] TODO 16: Implement verified backup, restore, integrity, and migration recovery

  1.2 source task(s): `T4.1.4`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T4.1.2, T4.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/backup.py (create); atlas/cli.py::database commands (extend); docs/operations/database-recovery.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make database evolution and corruption handling operationally recoverable with preflight integrity checks, verified backups, post-migration invariants, and deterministic operator diagnostics.
  * Restore or protect this invariant: A verified pre-migration backup exists before any schema change.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15.

  Where this applies

  * Primary affected components: `atlas/persistence/backup.py` (create: Own safe backup, hash, restore, and verification workflows.); `atlas/cli.py::database commands` (extend: Expose inspect, backup, verify, migrate, and restore dry runs.); `docs/operations/database-recovery.md` (create: Document failure and rollback procedures.)
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

  * Make database evolution and corruption handling operationally recoverable with preflight integrity checks, verified backups, post-migration invariants, and deterministic operator diagnostics.
  * Component dispositions: `atlas/persistence/backup.py` (create: Own safe backup, hash, restore, and verification workflows.); `atlas/cli.py::database commands` (extend: Expose inspect, backup, verify, migrate, and restore dry runs.); `docs/operations/database-recovery.md` (create: Document failure and rollback procedures.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Before migration, run integrity/foreign-key checks, capture schema/row fingerprints, create a verified backup, and confirm free-space requirements.
  * After migration, verify schema fingerprint, row counts, referential invariants, and representative deserialization.
  * Implement restore verification into a separate path before any destructive replacement.
  * Detect partial migration markers, stale backups, orphan temporary files, and incompatible binary/schema combinations.

  Security and safety requirements

  * Backup and restore paths are canonical, permission-restricted, and outside source roots.
  * Never overwrite the only valid database without a separately verified copy.
  * Integrity failure blocks normal startup and exposes read-only diagnostics.
  * Backup manifests contain hashes and versions but no sensitive row content.

  Edge cases and outliers to handle

  * Corrupt source DB, corrupt backup, insufficient disk, permission loss.
  * Operator selects the wrong backup or a backup from a newer schema.
  * Restore succeeds but application binary cannot read the schema.
  * Crash occurs during final database swap.

  Acceptance criteria (“done” definition)

  * A verified pre-migration backup exists before any schema change.
  * Restore drills reproduce schema and row fingerprints in a separate location.
  * Migration failure leaves the original database and backup usable.
  * Operator diagnostics identify exact failure stage, artifact hashes, and safe next action.

  Testing plan

  * Integrity and FK check tests.
  * Backup hash and restore verification tests.
  * Corruption and truncated-backup negative tests.
  * Disk-full and permission fault tests.
  * Crash-at-swap tests.
  * End-to-end v0.1 migration and rollback drill.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Integrity and FK check tests., Backup hash and restore verification tests., Corruption and truncated-backup negative tests., Disk-full and permission fault tests., Crash-at-swap tests., End-to-end v0.1 migration and rollback drill..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T4.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/backup.py, atlas/cli.py::database commands, docs/operations/database-recovery.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 17: Specify exhaustive job, phase, attempt, and control state tables

  1.2 source task(s): `T5.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T3.1.4, T4.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/states.py (create); docs/architecture/state-machines.md (create); atlas/core/lifecycle.py::TransitionPolicy (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Define states, terminal conditions, transition guards, failure propagation, skip reasons, suspension, cancellation, retry scheduling, restart, and replay before implementing mutations.
  * Restore or protect this invariant: Transition tables are exhaustive and machine-readable.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15.

  Where this applies

  * Primary affected components: `atlas/models/states.py` (create: Own enums, terminal sets, and typed transition reasons.); `docs/architecture/state-machines.md` (create: Publish transition tables and invariants.); `atlas/core/lifecycle.py::TransitionPolicy` (create: Represent legal transitions as data and guards.)
  * Epic boundary: Explicit lifecycle state machines, attempts, and fencing — Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.
  * Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-004 requires: Current mutable status fields do not define legal transitions, attempts, fencing, immutable terminal truth, or stale-result behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Define states, terminal conditions, transition guards, failure propagation, skip reasons, suspension, cancellation, retry scheduling, restart, and replay before implementing mutations.
  * Component dispositions: `atlas/models/states.py` (create: Own enums, terminal sets, and typed transition reasons.); `docs/architecture/state-machines.md` (create: Publish transition tables and invariants.); `atlas/core/lifecycle.py::TransitionPolicy` (create: Represent legal transitions as data and guards.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define job, phase-run, attempt, and control-request states with one meaning per state.
  * Enumerate every legal transition with actor, preconditions, required evidence, emitted event, and terminal behavior.
  * Define propagation from attempt outcome to phase and job, including optional/skipped/blocked/degraded distinctions.
  * Define restart and replay decisions without implying side-effect safety not yet proven.

  Security and safety requirements

  * No plugin, worker, adapter, event consumer, or AI output can author a state transition.
  * Terminal truth is immutable except through explicit reconciliation/supersession records.
  * Unknown or malformed state/version fails closed.
  * Cancellation and suspension never erase prior evidence.

  Edge cases and outliers to handle

  * Cancel requested before first attempt, during checkpoint, or after terminal completion.
  * Optional phase fails while required phases succeed.
  * Process restarts with job RUNNING but no live owner.
  * Legacy database contains a status combination not representable in the new tables.

  Acceptance criteria (“done” definition)

  * Transition tables are exhaustive and machine-readable.
  * Every state has one owner, legal predecessors/successors, and terminal semantics.
  * Invalid legacy combinations have an explicit migration or blocked-state rule.
  * The tables map to PDF lifecycle semantics without creating DAG behavior.

  Testing plan

  * Transition-table completeness tests.
  * State enum serialization/version tests.
  * Truth-table tests for failure propagation.
  * Legacy-state mapping tests.
  * Terminal immutability negative tests.
  * Model-based review against sequence diagrams.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Transition-table completeness tests., State enum serialization/version tests., Truth-table tests for failure propagation., Legacy-state mapping tests., Terminal immutability negative tests., Model-based review against sequence diagrams..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T5.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/states.py, docs/architecture/state-machines.md, atlas/core/lifecycle.py::TransitionPolicy.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 18: Persist immutable phase runs and execution attempts

  1.2 source task(s): `T5.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T5.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `phase_runs and attempts migrations (create); atlas/persistence/repositories/attempts.py (create); atlas/core/orchestrator.py (refactor)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Represent each phase execution as a durable phase run with one or more immutable attempts, linked errors, checkpoints, backend identity, and result digests.
  * Restore or protect this invariant: Every execution is represented by exactly one immutable attempt record.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15.

  Where this applies

  * Primary affected components: `phase_runs and attempts migrations` (create: Persist phase/attempt identity and relationships.); `atlas/persistence/repositories/attempts.py` (create: Own attempt reads and writes.); `atlas/core/orchestrator.py` (refactor: Delegate attempt lifecycle to the coordinator.)
  * Epic boundary: Explicit lifecycle state machines, attempts, and fencing — Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.
  * Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-004 requires: Current mutable status fields do not define legal transitions, attempts, fencing, immutable terminal truth, or stale-result behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Represent each phase execution as a durable phase run with one or more immutable attempts, linked errors, checkpoints, backend identity, and result digests.
  * Component dispositions: `phase_runs and attempts migrations` (create: Persist phase/attempt identity and relationships.); `atlas/persistence/repositories/attempts.py` (create: Own attempt reads and writes.); `atlas/core/orchestrator.py` (refactor: Delegate attempt lifecycle to the coordinator.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Add phase-run and attempt identifiers, ordinal, backend/plugin identity, fencing token, start/end, outcome, error class, checkpoint, work/result digest, and predecessor/successor links.
  * Create an attempt only after transition guards and required inputs are durably verified.
  * Append outcomes and evidence without mutating completed attempt identity.
  * Project legacy phase fields from canonical records during the compatibility window.

  Security and safety requirements

  * Prevent caller-supplied IDs from colliding or crossing jobs.
  * Do not persist unbounded error payloads or artifact content in attempt rows.
  * Foreign keys and uniqueness prevent duplicate attempt numbers and cross-phase checkpoint links.
  * Backend credentials or secrets never enter attempt metadata.

  Edge cases and outliers to handle

  * Attempt creation succeeds but execution never starts.
  * Two owners race to create the next attempt.
  * Result arrives after a successor attempt exists.
  * Legacy phase row has no attempt record.

  Acceptance criteria (“done” definition)

  * Every execution is represented by exactly one immutable attempt record.
  * Duplicate concurrent attempt creation is rejected by transaction and uniqueness guards.
  * Legacy phase status remains available as a derived compatibility projection.
  * Attempt rows link to exact input/config/policy and later result/checkpoint evidence.

  Testing plan

  * Repository unit tests.
  * Concurrent attempt-creation tests.
  * Foreign-key/uniqueness negative tests.
  * Legacy projection tests.
  * Crash after attempt creation tests.
  * Serialization and schema migration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Repository unit tests., Concurrent attempt-creation tests., Foreign-key/uniqueness negative tests., Legacy projection tests., Crash after attempt creation tests., Serialization and schema migration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T5.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: phase_runs and attempts migrations, atlas/persistence/repositories/attempts.py, atlas/core/orchestrator.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
