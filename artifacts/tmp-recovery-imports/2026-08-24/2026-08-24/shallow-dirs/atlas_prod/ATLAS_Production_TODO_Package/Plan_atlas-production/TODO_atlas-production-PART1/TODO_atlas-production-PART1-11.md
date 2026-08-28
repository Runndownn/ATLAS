@BinReaper Production TODOs

## TODO

* [ ] TODO 31: Implement the idempotent outbox dispatcher and delivery backpressure

  1.2 source task(s): `T8.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T8.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/dispatcher.py::OutboxDispatcher (create); atlas/core/event_bus.py (refactor); atlas/events/transports/base.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Project committed events to zero or more transports with at-least-once delivery, stable delivery keys, bounded retry, explicit dead-letter state, and no authority over lifecycle.
  * Restore or protect this invariant: Redelivery creates no duplicate lifecycle effect.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23.

  Where this applies

  * Primary affected components: `atlas/events/dispatcher.py::OutboxDispatcher` (create: Own leasing, delivery, retry, and acknowledgement.); `atlas/core/event_bus.py` (refactor: Retain observer/transport facade only.); `atlas/events/transports/base.py` (create: Define delivery adapter contract.)
  * Epic boundary: Durable events and transactional outbox — Persist required lifecycle history atomically with authoritative state and project it to transports without making messaging a second authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]
  * Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-007 requires: Current publish-then-persist behavior can commit authoritative state without durable evidence and treats RabbitMQ as an ambiguous side channel.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Project committed events to zero or more transports with at-least-once delivery, stable delivery keys, bounded retry, explicit dead-letter state, and no authority over lifecycle.
  * Component dispositions: `atlas/events/dispatcher.py::OutboxDispatcher` (create: Own leasing, delivery, retry, and acknowledgement.); `atlas/core/event_bus.py` (refactor: Retain observer/transport facade only.); `atlas/events/transports/base.py` (create: Define delivery adapter contract.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Lease pending outbox records with fencing, batch limits, delivery keys, and bounded concurrency.
  * Define exponential backoff/jitter, maximum attempts, dead-letter/blocked status, retention, and operator retry controls.
  * Require adapters to report delivered, retryable failure, permanent failure, or unknown outcome.
  * Expose backlog age/size and explicit degraded behavior when limits are reached.

  Security and safety requirements

  * Dispatcher cannot mutate job/phase/attempt state or interpret payloads as commands.
  * Delivery keys and signatures prevent accidental duplicate consumer effects where supported.
  * Untrusted broker errors and acknowledgements are validated and bounded.
  * Dead-letter records retain provenance without leaking payload secrets.

  Edge cases and outliers to handle

  * Broker accepts message but acknowledgement is lost.
  * Dispatcher crashes after send before marking delivered.
  * One poison event blocks a batch.
  * Backlog exceeds count, bytes, or age thresholds.

  Acceptance criteria (“done” definition)

  * Redelivery creates no duplicate lifecycle effect.
  * A poison event is isolated and does not starve later records.
  * Backlog limits produce documented block/degrade behavior and diagnostics.
  * Disabling all transports leaves core execution correct.

  Testing plan

  * Dispatcher lease/fencing tests.
  * Lost-ack and duplicate-delivery tests.
  * Poison/dead-letter tests.
  * Backoff/jitter deterministic tests.
  * Backlog saturation/load tests.
  * Transport-disabled integration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Dispatcher lease/fencing tests., Lost-ack and duplicate-delivery tests., Poison/dead-letter tests., Backoff/jitter deterministic tests., Backlog saturation/load tests., Transport-disabled integration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T8.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/dispatcher.py::OutboxDispatcher, atlas/core/event_bus.py, atlas/events/transports/base.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 32: Define progress-event sampling, retention, replay, and event diagnostics

  1.2 source task(s): `T8.1.4`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T8.1.2, T8.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/policy.py (create); atlas/events/queries.py (create); atlas diagnostics events (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prevent progress and analyzer chatter from overwhelming durable history while preserving current progress authority and enough evidence for reconstruction.
  * Restore or protect this invariant: Current progress remains exact within defined update semantics even when history is sampled.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23.

  Where this applies

  * Primary affected components: `atlas/events/policy.py` (create: Own event class durability, sampling, coalescing, and retention policy.); `atlas/events/queries.py` (create: Provide ordered history and replay/export queries.); `atlas diagnostics events` (extend: Expose gaps, backlog, dead letters, and schema versions.)
  * Epic boundary: Durable events and transactional outbox — Persist required lifecycle history atomically with authoritative state and project it to transports without making messaging a second authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]
  * Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-007 requires: Current publish-then-persist behavior can commit authoritative state without durable evidence and treats RabbitMQ as an ambiguous side channel.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prevent progress and analyzer chatter from overwhelming durable history while preserving current progress authority and enough evidence for reconstruction.
  * Component dispositions: `atlas/events/policy.py` (create: Own event class durability, sampling, coalescing, and retention policy.); `atlas/events/queries.py` (create: Provide ordered history and replay/export queries.); `atlas diagnostics events` (extend: Expose gaps, backlog, dead letters, and schema versions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Classify events as required transition, evidentiary, operational, sampled progress, or transport-only.
  * Define coalescing/sampling keyed by entity and interval while persisting current progress separately.
  * Define retention/export rules that never delete authoritative state and preserve audit-critical history.
  * Add replay/export cursors for consumers without replaying events as lifecycle commands.

  Security and safety requirements

  * Sampling cannot drop terminal, rejection, safety, decision, publication, or integrity events.
  * Exports redact secrets and bound payload text.
  * Retention deletion is transactional, auditable, and policy-controlled.
  * Replay offsets are consumer state, not lifecycle state.

  Edge cases and outliers to handle

  * Millions of progress updates for one large job.
  * Consumer offset points to pruned history.
  * Event payload fails schema validation during export.
  * Retention runs while dispatcher is delivering.

  Acceptance criteria (“done” definition)

  * Current progress remains exact within defined update semantics even when history is sampled.
  * Required event classes are never sampled or pruned outside policy.
  * Replay/export detects gaps and schema incompatibility.
  * Event diagnostics identify backlog, dead letters, retention watermark, and sequence gaps.

  Testing plan

  * Sampling/coalescing property tests.
  * Required-event non-drop tests.
  * High-volume progress load tests.
  * Retention/dispatcher concurrency tests.
  * Replay gap and offset tests.
  * Redacted export tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Sampling/coalescing property tests., Required-event non-drop tests., High-volume progress load tests., Retention/dispatcher concurrency tests., Replay gap and offset tests., Redacted export tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T8.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/policy.py, atlas/events/queries.py, atlas diagnostics events.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 33: Define `PhaseContext`, progress, control-request, and checkpoint contracts

  1.2 source task(s): `T9.1.1`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T5.1.4, T8.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/context.py::PhaseContext (create); atlas/models/controls.py (create); atlas/models/checkpoints.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace mutable phase-local state with typed services for durable progress, control polling, checkpoint creation, result writes, and telemetry.
  * Restore or protect this invariant: Contracts distinguish current progress, sampled history, controls, and checkpoints.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28.

  Where this applies

  * Primary affected components: `atlas/core/context.py::PhaseContext` (create: Expose bounded phase services without StateStore authority.); `atlas/models/controls.py` (create: Define ControlRequest and acknowledgement states.); `atlas/models/checkpoints.py` (create: Define versioned checkpoint identity and compatibility fields.)
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

  * Replace mutable phase-local state with typed services for durable progress, control polling, checkpoint creation, result writes, and telemetry.
  * Component dispositions: `atlas/core/context.py::PhaseContext` (create: Expose bounded phase services without StateStore authority.); `atlas/models/controls.py` (create: Define ControlRequest and acknowledgement states.); `atlas/models/checkpoints.py` (create: Define versioned checkpoint identity and compatibility fields.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define current progress fields, monotonicity/aggregation rules, update sequence, and history sampling references.
  * Define control request type, requested/applied/rejected states, actor, correlation, idempotency key, reason, and target scope.
  * Define checkpoint phase/operation/input/config/policy/schema versions, cursor, output references, integrity digest, and safe-point class.
  * Specify which PhaseContext methods are transactional, cancellable, and available to built-ins versus plugins.

  Security and safety requirements

  * PhaseContext does not expose raw StateStore, arbitrary filesystem, or lifecycle transition methods.
  * Control actor and scope are validated by CommandService/policy before persistence.
  * Checkpoint payloads contain references and validated cursors, not arbitrary pickled Python objects.
  * Progress and diagnostics are bounded and redact payload-derived text.

  Edge cases and outliers to handle

  * Progress moves backward after retry or phase fan-out.
  * Duplicate control request with same idempotency key but different payload.
  * Checkpoint schema/plugin/config version mismatch.
  * Control targets a terminal or foreign job.

  Acceptance criteria (“done” definition)

  * Contracts distinguish current progress, sampled history, controls, and checkpoints.
  * All serialized records are versioned and digestible.
  * PhaseContext grants no direct lifecycle authority.
  * Safe-point and maximum-control-latency requirements are expressible per phase.

  Testing plan

  * Model/schema unit tests.
  * Progress monotonicity/property tests.
  * Control idempotency and scope tests.
  * Checkpoint serialization/integrity tests.
  * Context capability negative tests.
  * Version-skew compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Model/schema unit tests., Progress monotonicity/property tests., Control idempotency and scope tests., Checkpoint serialization/integrity tests., Context capability negative tests., Version-skew compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T9.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/context.py::PhaseContext, atlas/models/controls.py, atlas/models/checkpoints.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
