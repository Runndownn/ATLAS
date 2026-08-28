@BinReaper Production TODOs

## TODO

* [ ] TODO 34: Persist live progress and deterministic job-level projections

  1.2 source task(s): `T9.1.2`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T9.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/repositories/progress.py (create); atlas/phases/base.py::report_progress (refactor); atlas/status/projection.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Write bounded intermediate phase progress to authoritative state and derive job-level progress so independent status clients see real work rather than post-return snapshots.
  * Restore or protect this invariant: A second process observes progress within the documented staleness bound.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28.

  Where this applies

  * Primary affected components: `atlas/persistence/repositories/progress.py` (create: Own current progress and update sequence.); `atlas/phases/base.py::report_progress` (refactor: Delegate through PhaseContext.); `atlas/status/projection.py` (create: Aggregate phase/work-item progress deterministically.)
  * Epic boundary: Durable progress, controls, safe points, and checkpoints — Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.
  * Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-008 requires: Current progress and pause/resume/cancel are process-local; restart repeats phases without verified recovery state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Write bounded intermediate phase progress to authoritative state and derive job-level progress so independent status clients see real work rather than post-return snapshots.
  * Component dispositions: `atlas/persistence/repositories/progress.py` (create: Own current progress and update sequence.); `atlas/phases/base.py::report_progress` (refactor: Delegate through PhaseContext.); `atlas/status/projection.py` (create: Aggregate phase/work-item progress deterministically.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Persist current phase progress with sequence/version, units completed/total/unknown, message code, resource counters, and update time.
  * Define aggregation weights or phase-state-based semantics without presenting false precision.
  * Coalesce writes by time/work threshold while guaranteeing bounded status staleness.
  * Link sampled progress events to authoritative current progress sequence.

  Security and safety requirements

  * Untrusted labels and paths are bounded/redacted before status or logs.
  * A plugin cannot set another phase or job's progress.
  * Progress write failure is classified and cannot silently report success.
  * High-frequency updates are rate-limited without blocking cancellation checks.

  Edge cases and outliers to handle

  * Total work becomes known only after traversal.
  * Retry restarts or resumes from checkpoint.
  * Parallel work items complete out of order.
  * Database contention delays progress writes.

  Acceptance criteria (“done” definition)

  * A second process observes progress within the documented staleness bound.
  * Job-level progress is deterministic and never decreases except by a documented retry-generation reset.
  * Progress write volume remains bounded under million-entry workloads.
  * Terminal state and final progress are mutually consistent.

  Testing plan

  * Progress repository unit tests.
  * Aggregation property tests.
  * Second-process status integration tests.
  * High-frequency load tests.
  * Retry/resume progress tests.
  * Contention and write-failure tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Progress repository unit tests., Aggregation property tests., Second-process status integration tests., High-frequency load tests., Retry/resume progress tests., Contention and write-failure tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T9.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/repositories/progress.py, atlas/phases/base.py::report_progress, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 35: Implement durable control requests and safe-point acknowledgement

  1.2 source task(s): `T9.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T9.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/control_service.py::ControlRequestService (create); atlas/phases/base.py::control_point (extend); atlas/cli.py::pause/resume/cancel (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Turn pause, resume, and cancel into idempotent commands that the active attempt polls and either applies at a declared safe point or rejects with a durable reason.
  * Restore or protect this invariant: A second process can request and observe applied/rejected control state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28.

  Where this applies

  * Primary affected components: `atlas/core/control_service.py::ControlRequestService` (create: Validate and persist control commands.); `atlas/phases/base.py::control_point` (extend: Poll and acknowledge controls through PhaseContext.); `atlas/cli.py::pause/resume/cancel` (refactor: Submit commands instead of mutating process-local maps.)
  * Epic boundary: Durable progress, controls, safe points, and checkpoints — Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.
  * Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-008 requires: Current progress and pause/resume/cancel are process-local; restart repeats phases without verified recovery state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Turn pause, resume, and cancel into idempotent commands that the active attempt polls and either applies at a declared safe point or rejects with a durable reason.
  * Component dispositions: `atlas/core/control_service.py::ControlRequestService` (create: Validate and persist control commands.); `atlas/phases/base.py::control_point` (extend: Poll and acknowledge controls through PhaseContext.); `atlas/cli.py::pause/resume/cancel` (refactor: Submit commands instead of mutating process-local maps.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Persist idempotent control requests with actor, target, expected state/version, requested time, and correlation.
  * Define phase-specific safe-point classes and maximum polling latency.
  * At a safe point, atomically checkpoint if required, acknowledge applied/rejected state, and transition attempt/phase/job according to policy.
  * Define cancellation cleanup ownership and resume preconditions.

  Security and safety requirements

  * Authorization and expected-state checks occur before control persistence or application.
  * Late or replayed commands cannot reopen terminal jobs.
  * Cancel does not delete evidence or unverified side effects.
  * Control reasons and actor identifiers are auditable and redacted.

  Edge cases and outliers to handle

  * Pause arrives while no attempt is running.
  * Cancel and success race at the same safe point.
  * Resume references stale checkpoint or superseded job.
  * Duplicate command is delivered from CLI and REST.

  Acceptance criteria (“done” definition)

  * A second process can request and observe applied/rejected control state.
  * `PAUSED` is reached only after durable safe-point acknowledgement.
  * Duplicate control requests are idempotent and conflicting payloads are rejected.
  * Built-in phases document and test maximum control latency.

  Testing plan

  * Control service unit tests.
  * Second-process integration tests.
  * Cancel-versus-success race tests.
  * Duplicate/idempotency tests.
  * Phase safe-point latency tests.
  * Cleanup/evidence preservation tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Control service unit tests., Second-process integration tests., Cancel-versus-success race tests., Duplicate/idempotency tests., Phase safe-point latency tests., Cleanup/evidence preservation tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T9.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/control_service.py::ControlRequestService, atlas/phases/base.py::control_point, atlas/cli.py::pause/resume/cancel.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 36: Implement checkpoint validation, resume decisions, and stale-checkpoint rejection

  1.2 source task(s): `T9.1.4`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T9.1.2, T9.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/checkpoint_service.py::CheckpointService (create); atlas/phases/* checkpoint adapters (extend); atlas/persistence/repositories/checkpoints.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Resume expensive work only from durable checkpoints whose phase, operation, input, config, policy, code, and output references still match current authority.
  * Restore or protect this invariant: Stale or incompatible checkpoints never resume execution.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28.

  Where this applies

  * Primary affected components: `atlas/core/checkpoint_service.py::CheckpointService` (create: Create, validate, supersede, and query checkpoints.); `atlas/phases/* checkpoint adapters` (extend: Implement phase-specific cursor and reconciliation logic.); `atlas/persistence/repositories/checkpoints.py` (create: Persist versioned checkpoint records.)
  * Epic boundary: Durable progress, controls, safe points, and checkpoints — Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.
  * Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-008 requires: Current progress and pause/resume/cancel are process-local; restart repeats phases without verified recovery state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Resume expensive work only from durable checkpoints whose phase, operation, input, config, policy, code, and output references still match current authority.
  * Component dispositions: `atlas/core/checkpoint_service.py::CheckpointService` (create: Create, validate, supersede, and query checkpoints.); `atlas/phases/* checkpoint adapters` (extend: Implement phase-specific cursor and reconciliation logic.); `atlas/persistence/repositories/checkpoints.py` (create: Persist versioned checkpoint records.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define checkpoint creation transactions, immutable digest, predecessor chain, and latest-compatible lookup.
  * Validate job/phase/attempt, input identity, config/policy digest, plugin/backend version, schema, cursor, referenced outputs, and fencing epoch before resume.
  * Define per-phase resume-from-checkpoint versus restart-from-beginning behavior and cleanup of incompatible partial state.
  * Record rejection reason and deterministic recovery decision.

  Security and safety requirements

  * Do not deserialize arbitrary objects or execute data from checkpoints.
  * Referenced files/blobs are revalidated by identity and containment before use.
  * Stale fencing or superseded input invalidates the checkpoint.
  * Checkpoint deletion/retention cannot erase required recovery evidence prematurely.

  Edge cases and outliers to handle

  * Checkpoint record exists but referenced workspace/output is missing.
  * Code/plugin/config version changed incompatibly.
  * Crash during checkpoint creation leaves partial data.
  * Multiple checkpoints compete as latest after retry.

  Acceptance criteria (“done” definition)

  * Stale or incompatible checkpoints never resume execution.
  * Every built-in phase declares checkpoint granularity and validation inputs.
  * Crash tests resume or restart according to one deterministic rule.
  * Checkpoint rejection remains visible in status and diagnostics.

  Testing plan

  * Checkpoint service unit tests.
  * Per-phase resume integration tests.
  * Version/config/input mismatch negative tests.
  * Missing/corrupt referenced-output tests.
  * Crash-at-checkpoint fault injection.
  * Fencing and concurrent-checkpoint tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Checkpoint service unit tests., Per-phase resume integration tests., Version/config/input mismatch negative tests., Missing/corrupt referenced-output tests., Crash-at-checkpoint fault injection., Fencing and concurrent-checkpoint tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T9.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/checkpoint_service.py::CheckpointService, atlas/phases/* checkpoint adapters, atlas/persistence/repositories/checkpoints.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
