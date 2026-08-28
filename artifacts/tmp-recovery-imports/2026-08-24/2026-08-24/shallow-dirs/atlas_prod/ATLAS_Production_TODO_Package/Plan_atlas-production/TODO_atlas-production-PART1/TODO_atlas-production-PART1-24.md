@BinReaper Production TODOs

## TODO

* [ ] TODO 70: Implement retry, deadline, timeout, and idempotency policy

  1.2 source task(s): `T18.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T18.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/recovery/policy.py::RetryPolicyResolver (create); atlas/recovery/idempotency.py::IdempotencyService (create); atlas/core/coordinator.py (extend); atlas/schema/migrations/*_recovery_policy.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create bounded retry decisions that derive from operation semantics, attempt history, verified checkpoints, deadlines, and idempotency identity rather than ad hoc exception handling.
  * Restore or protect this invariant: Retry decisions are deterministic for the same durable state and policy version.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27.

  Where this applies

  * Primary affected components: `atlas/recovery/policy.py::RetryPolicyResolver` (create: Compute retry/block/fail/reconcile decisions and bounded schedules.); `atlas/recovery/idempotency.py::IdempotencyService` (create: Reserve, look up, and finalize operation-level idempotency records.); `atlas/core/coordinator.py` (extend: Create successor attempts and enforce deadlines without mutating predecessor history.); `atlas/schema/migrations/*_recovery_policy.sql` (create: Persist idempotency, retry schedule, deadline, and recovery reason.)
  * Epic boundary: Retry, timeout, idempotency, reconciliation, and crash recovery — Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.
  * Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-016 requires: Replay is unsafe unless each operation declares duplicate effects, checkpoints, and unknown-outcome handling.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create bounded retry decisions that derive from operation semantics, attempt history, verified checkpoints, deadlines, and idempotency identity rather than ad hoc exception handling.
  * Component dispositions: `atlas/recovery/policy.py::RetryPolicyResolver` (create: Compute retry/block/fail/reconcile decisions and bounded schedules.); `atlas/recovery/idempotency.py::IdempotencyService` (create: Reserve, look up, and finalize operation-level idempotency records.); `atlas/core/coordinator.py` (extend: Create successor attempts and enforce deadlines without mutating predecessor history.); `atlas/schema/migrations/*_recovery_policy.sql` (create: Persist idempotency, retry schedule, deadline, and recovery reason.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define maximum attempts, bounded exponential backoff/jitter, total deadline, per-attempt timeout, retry budget, and dependency-specific circuit behavior.
  * Generate or validate idempotency keys from stable operation identity and immutable inputs before side effects.
  * Create a new attempt for every retry and link predecessor, reason, checkpoint, policy version, and next eligible time.
  * Ensure cancellation and pause requests take precedence at defined safe points and cannot be lost inside retry sleep.

  Security and safety requirements

  * Bound retries and jitter to prevent retry storms and deliberate resource amplification.
  * Do not expose idempotency keys as authorization credentials; scope them to job/operation/version.
  * Reject replay across tenant/deployment/source scope where optional deployment identity applies.
  * Timeout handling must revoke/fence the attempt and verify child/external operation state before successor execution.

  Edge cases and outliers to handle

  * Host restarts during backoff.
  * Clock moves backward/forward or differs from remote dependency.
  * Timeout fires while operation actually committed.
  * Multiple coordinators schedule the same retry.

  Acceptance criteria (“done” definition)

  * Retry decisions are deterministic for the same durable state and policy version.
  * No unsafe or unknown-outcome operation is automatically retried.
  * Duplicate idempotency identity returns the prior canonical result or conflict rather than repeating an effect.
  * Attempt/deadline/backoff state survives process restart.

  Testing plan

  * Retry policy truth-table tests.
  * Backoff/jitter bounded property tests.
  * Concurrent idempotency reservation tests.
  * Timeout-versus-commit race tests.
  * Restart-during-backoff tests.
  * Cancellation/pause precedence tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Retry policy truth-table tests., Backoff/jitter bounded property tests., Concurrent idempotency reservation tests., Timeout-versus-commit race tests., Restart-during-backoff tests., Cancellation/pause precedence tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T18.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/recovery/policy.py::RetryPolicyResolver, atlas/recovery/idempotency.py::IdempotencyService, atlas/core/coordinator.py, atlas/schema/migrations/*_recovery_policy.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 71: Implement startup reconciliation and deterministic recovery decisions

  1.2 source task(s): `T18.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T18.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/recovery/service.py::RecoveryService (create); atlas/recovery/reconcilers.py (create); atlas/core/runtime.py (extend); atlas/status/projection.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Scan nonterminal jobs, phase runs, attempts, controls, work items, checkpoints, workspaces, and publications after restart and choose exactly one safe action from durable evidence.
  * Restore or protect this invariant: Each nonterminal attempt maps to one persisted recovery disposition.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27.

  Where this applies

  * Primary affected components: `atlas/recovery/service.py::RecoveryService` (create: Inspect durable state and emit resume/retry/reconcile/block/fail decisions.); `atlas/recovery/reconcilers.py` (create: Host operation-specific and external-effect reconciliation adapters.); `atlas/core/runtime.py` (extend: Invoke recovery before claiming new work and expose a recovery summary.); `atlas/status/projection.py` (extend: Show recovery requirement, reason, evidence, and operator action.)
  * Epic boundary: Retry, timeout, idempotency, reconciliation, and crash recovery — Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.
  * Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-016 requires: Replay is unsafe unless each operation declares duplicate effects, checkpoints, and unknown-outcome handling.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Scan nonterminal jobs, phase runs, attempts, controls, work items, checkpoints, workspaces, and publications after restart and choose exactly one safe action from durable evidence.
  * Component dispositions: `atlas/recovery/service.py::RecoveryService` (create: Inspect durable state and emit resume/retry/reconcile/block/fail decisions.); `atlas/recovery/reconcilers.py` (create: Host operation-specific and external-effect reconciliation adapters.); `atlas/core/runtime.py` (extend: Invoke recovery before claiming new work and expose a recovery summary.); `atlas/status/projection.py` (extend: Show recovery requirement, reason, evidence, and operator action.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define startup scan order and snapshot/transaction boundaries so recovery does not race normal claims.
  * Validate checkpoint schema/config/input/content/attempt lineage before resuming.
  * Reconcile staged workspaces, orphan child processes where observable, outbox state, idempotency records, and external publication attempts.
  * Persist one `RecoveryDecision` with reason, evidence, policy/semantics version, and successor action before execution.
  * Conservatively block legacy nonterminal jobs whose safe continuation cannot be established.

  Security and safety requirements

  * Recovery cannot trust stale in-memory maps, unverified files, model output, or transport events.
  * Use least-privilege external reconciliation and exact destination/idempotency identities.
  * Fence stale owners before accepting results or deleting resources.
  * Preserve failed/unknown evidence; cleanup cannot erase information needed to determine duplicate effects.

  Edge cases and outliers to handle

  * Database is partially corrupted or migration incomplete.
  * Checkpoint exists but source/content/config/plugin changed.
  * External service is unavailable during reconciliation.
  * Repeated restart occurs while a recovery action is in progress.

  Acceptance criteria (“done” definition)

  * Each nonterminal attempt maps to one persisted recovery disposition.
  * Unsafe or insufficient evidence becomes `BLOCKED/RECONCILIATION_REQUIRED`, never guessed success.
  * Repeated startup converges without duplicating the selected action.
  * Recovery summary identifies exact job/phase/attempt/checkpoint/effect boundary and next operator action.

  Testing plan

  * Recovery decision table tests.
  * Repeated-start idempotency tests.
  * Stale checkpoint/source/plugin tests.
  * External outage/unknown publication tests.
  * Legacy job conservative migration tests.
  * Corrupt-state and partial-migration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Recovery decision table tests., Repeated-start idempotency tests., Stale checkpoint/source/plugin tests., External outage/unknown publication tests., Legacy job conservative migration tests., Corrupt-state and partial-migration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T18.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/recovery/service.py::RecoveryService, atlas/recovery/reconcilers.py, atlas/core/runtime.py, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 72: Build the phase-by-phase crash and replay verification matrix

  1.2 source task(s): `T18.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T18.1.2, T18.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/faults/crash_matrix/ (create); tests/integration/test_recovery_matrix.py (create); scripts/run_recovery_matrix.py (create); docs/operations/recovery-matrix.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prove recovery behavior at transaction, checkpoint, materialization, plugin, event, control, and publication boundaries for every built-in phase and operation class.
  * Restore or protect this invariant: The matrix covers all built-in phases and every declared operation-semantics class.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27.

  Where this applies

  * Primary affected components: `tests/faults/crash_matrix/` (create: Store deterministic fault points, fixtures, expected recovery decisions, and evidence.); `tests/integration/test_recovery_matrix.py` (create: Run multi-process kill/restart and replay scenarios.); `scripts/run_recovery_matrix.py` (create: Execute and summarize the matrix in CI/operator environments.); `docs/operations/recovery-matrix.md` (create: Document supported outcomes, gaps, and manual recovery.)
  * Epic boundary: Retry, timeout, idempotency, reconciliation, and crash recovery — Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.
  * Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-016 requires: Replay is unsafe unless each operation declares duplicate effects, checkpoints, and unknown-outcome handling.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prove recovery behavior at transaction, checkpoint, materialization, plugin, event, control, and publication boundaries for every built-in phase and operation class.
  * Component dispositions: `tests/faults/crash_matrix/` (create: Store deterministic fault points, fixtures, expected recovery decisions, and evidence.); `tests/integration/test_recovery_matrix.py` (create: Run multi-process kill/restart and replay scenarios.); `scripts/run_recovery_matrix.py` (create: Execute and summarize the matrix in CI/operator environments.); `docs/operations/recovery-matrix.md` (create: Document supported outcomes, gaps, and manual recovery.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Enumerate fault points immediately before and after each authoritative transaction, filesystem commit, checkpoint, plugin launch/result, outbox write, and external publication boundary.
  * For each fault point define expected durable rows/files, allowed duplicate effects, recovery decision, cleanup, and retained evidence.
  * Run repeated restart and duplicate-delivery scenarios, not only one crash.
  * Produce machine-readable results tied to schema, code, fixture, platform, and operation-semantics versions.

  Security and safety requirements

  * Use isolated temporary roots and fake/replayable external adapters; never point fault tests at production destinations.
  * Include malicious/stale checkpoint, forged result, stale fencing, and event-injection scenarios.
  * Secret and payload fixtures must be synthetic and scanned before retention.
  * A skipped platform control must be explicit, owned, and cannot count as proof.

  Edge cases and outliers to handle

  * Kill occurs while SQLite lock or fsync is pending.
  * Disk-full or permission error masks the intended crash point.
  * Flaky timing makes a result nondeterministic.
  * Cleanup removes evidence before assertions.

  Acceptance criteria (“done” definition)

  * The matrix covers all built-in phases and every declared operation-semantics class.
  * Each fault point produces exactly the documented recovery disposition across repeated clean runs.
  * No unsafe side effect is repeated and no unknown outcome is reported as success.
  * CI publishes machine-readable crash/replay evidence and blocks regressions for mandatory platforms.

  Testing plan

  * Fault-injection unit tests.
  * Multi-process crash/restart integration tests.
  * Replay/idempotency property tests.
  * Disk/lock/dependency fault tests.
  * Stale fencing/forged result security tests.
  * Evidence determinism and secret-scan tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Fault-injection unit tests., Multi-process crash/restart integration tests., Replay/idempotency property tests., Disk/lock/dependency fault tests., Stale fencing/forged result security tests., Evidence determinism and secret-scan tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T18.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/faults/crash_matrix/, tests/integration/test_recovery_matrix.py, scripts/run_recovery_matrix.py, docs/operations/recovery-matrix.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
