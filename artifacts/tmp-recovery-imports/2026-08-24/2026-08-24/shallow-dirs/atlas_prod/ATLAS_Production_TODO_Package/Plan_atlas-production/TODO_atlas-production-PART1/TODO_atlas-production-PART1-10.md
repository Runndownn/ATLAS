@BinReaper Production TODOs

## TODO

* [ ] TODO 28: Preserve `HashStore` compatibility while removing process-local authority

  1.2 source task(s): `T7.1.4`
  Priority: `P0`
  Estimated effort: `10 hours`
  Dependencies: `T7.1.2, T7.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/storage/hash_store.py::HashStore (refactor); atlas/storage/__init__.py (extend); tests/compatibility/test_hash_store_v0_1.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Keep existing imports and expected `has_content` behavior as a facade over persistent identity without allowing the legacy in-memory manifest to remain authoritative.
  * Restore or protect this invariant: Supported legacy calls return documented equivalent results from persistent state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/storage/hash_store.py::HashStore` (refactor: Delegate to ContentIdentityService and StateStore.); `atlas/storage/__init__.py` (extend: Preserve supported public imports and deprecations.); `tests/compatibility/test_hash_store_v0_1.py` (create: Pin legacy behavior and migration.)
  * Epic boundary: Persistent content identity and occurrence linkage — Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]
  * Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-006 requires: Current hashes are process-local and disconnected from accepted occurrences, preventing cross-run deduplication and exact-byte lineage.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Keep existing imports and expected `has_content` behavior as a facade over persistent identity without allowing the legacy in-memory manifest to remain authoritative.
  * Component dispositions: `atlas/storage/hash_store.py::HashStore` (refactor: Delegate to ContentIdentityService and StateStore.); `atlas/storage/__init__.py` (extend: Preserve supported public imports and deprecations.); `tests/compatibility/test_hash_store_v0_1.py` (create: Pin legacy behavior and migration.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Inventory public methods, constructors, return types, examples, and tests that depend on HashStore.
  * Implement facade calls using persistent identity repositories and explicit async/runtime ownership.
  * Emit deprecation guidance for storage semantics that were previously overstated.
  * Remove or constrain process-local caches to non-authoritative performance hints with invalidation.

  Security and safety requirements

  * A cache miss cannot be interpreted as identity absence without consulting the store.
  * Do not expose raw database or source access through the facade.
  * Compatibility logs avoid paths/content and are rate-limited.
  * Old behavior that falsely implied CAS is corrected in docs and telemetry.

  Edge cases and outliers to handle

  * HashStore used before runtime connection.
  * Multiple runtimes share the same database.
  * Legacy caller expects synchronous access.
  * Cache contains stale result after migration or process fork.

  Acceptance criteria (“done” definition)

  * Supported legacy calls return documented equivalent results from persistent state.
  * No in-memory manifest is authoritative after migration.
  * Deprecated semantics produce actionable warnings and migration docs.
  * Compatibility tests cover restart and multiple-runtime cases.

  Testing plan

  * Public import/API compatibility tests.
  * Restart and multi-runtime tests.
  * Cache invalidation tests.
  * Pre-connect and lifecycle error tests.
  * Documentation example tests.
  * Deprecation telemetry/redaction tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Public import/API compatibility tests., Restart and multi-runtime tests., Cache invalidation tests., Pre-connect and lifecycle error tests., Documentation example tests., Deprecation telemetry/redaction tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T7.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/storage/hash_store.py::HashStore, atlas/storage/__init__.py, tests/compatibility/test_hash_store_v0_1.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 29: Define versioned durable event and outbox schemas

  1.2 source task(s): `T8.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T4.1.4, T5.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/models.py::DurableEvent (create); atlas/events/models.py::OutboxRecord (create); events and outbox migrations (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify immutable event identity, ordering, correlation, causation, entity references, payload versions, and transport intent separately from authoritative state.
  * Restore or protect this invariant: Every required transition event has a stable typed schema and entity references.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23.

  Where this applies

  * Primary affected components: `atlas/events/models.py::DurableEvent` (create: Own event envelope and typed payload references.); `atlas/events/models.py::OutboxRecord` (create: Represent delivery intent and status.); `events and outbox migrations` (create: Persist immutable history and dispatch state.)
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

  * Specify immutable event identity, ordering, correlation, causation, entity references, payload versions, and transport intent separately from authoritative state.
  * Component dispositions: `atlas/events/models.py::DurableEvent` (create: Own event envelope and typed payload references.); `atlas/events/models.py::OutboxRecord` (create: Represent delivery intent and status.); `events and outbox migrations` (create: Persist immutable history and dispatch state.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define event ID, local sequence, schema version, class, occurred/recorded times, correlation/causation IDs, actor, job/phase/attempt/work/content IDs, and typed payload.
  * Define which transitions require durable events and which high-volume observations remain current-state-only or sampled history.
  * Define outbox destination, delivery key, status, attempts, next attempt, and terminal/dead-letter fields.
  * Publish compatibility and evolution rules for event envelopes and payload schemas.

  Security and safety requirements

  * Event payloads contain references and bounded summaries, not artifact bytes, secrets, or arbitrary untrusted text.
  * Event IDs and sequence are generated by the core, not external callers.
  * Unknown payload versions remain queryable but cannot be interpreted as commands.
  * Transport routing metadata cannot alter lifecycle authority.

  Edge cases and outliers to handle

  * Clock moves backward or events are recorded after occurrence time.
  * One transaction emits several ordered events.
  * Payload schema is newer than a consumer.
  * High-volume progress would exceed storage/backlog budgets.

  Acceptance criteria (“done” definition)

  * Every required transition event has a stable typed schema and entity references.
  * Local sequence establishes deterministic within-store ordering.
  * Outbox state is distinct from event history and transport-specific payload.
  * Event evolution rules preserve old history and reject unsafe downgrade.

  Testing plan

  * Schema and serialization tests.
  * Sequence/ordering tests.
  * Unknown-version compatibility tests.
  * Payload size/redaction tests.
  * Correlation/causation integrity tests.
  * Migration round-trip tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Schema and serialization tests., Sequence/ordering tests., Unknown-version compatibility tests., Payload size/redaction tests., Correlation/causation integrity tests., Migration round-trip tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T8.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/models.py::DurableEvent, atlas/events/models.py::OutboxRecord, events and outbox migrations.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 30: Record state transitions, durable events, and outbox rows atomically

  1.2 source task(s): `T8.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T8.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/recorder.py::DurableEventRecorder (create); atlas/core/lifecycle.py (extend); atlas/core/job_store.py::store_event (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make one StateStore transaction commit the authoritative mutation, required history event, and transport intent or commit none of them.
  * Restore or protect this invariant: Fault injection at every transaction step yields all-or-nothing state/history/outbox.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23.

  Where this applies

  * Primary affected components: `atlas/events/recorder.py::DurableEventRecorder` (create: Build and append required events inside caller transactions.); `atlas/core/lifecycle.py` (extend: Invoke recorder within transition commands.); `atlas/core/job_store.py::store_event` (refactor: Delegate to canonical event repository.)
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

  * Make one StateStore transaction commit the authoritative mutation, required history event, and transport intent or commit none of them.
  * Component dispositions: `atlas/events/recorder.py::DurableEventRecorder` (create: Build and append required events inside caller transactions.); `atlas/core/lifecycle.py` (extend: Invoke recorder within transition commands.); `atlas/core/job_store.py::store_event` (refactor: Delegate to canonical event repository.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Add recorder APIs that require an active StateStore transaction and validated transition context.
  * Allocate local sequence and append event/outbox records before commit.
  * Refactor orchestrator and built-in phases so required detailed events use the recorder rather than transport-only emission.
  * Define behavior when payload construction, event insert, outbox insert, or commit fails.

  Security and safety requirements

  * No state transition commits without its required event.
  * No event claims a transition that rolled back.
  * Event data is validated and bounded before persistence.
  * Transport availability is never checked inside the authoritative transaction except bounded outbox capacity policy.

  Edge cases and outliers to handle

  * Event serialization fails after state row update.
  * Outbox insert violates capacity or constraint.
  * Process dies before/after commit acknowledgement.
  * Duplicate transition command re-enters recorder.

  Acceptance criteria (“done” definition)

  * Fault injection at every transaction step yields all-or-nothing state/history/outbox.
  * Every required transition query returns its durable event.
  * Duplicate commands do not create duplicate lifecycle effects.
  * Transport outage cannot corrupt or roll back already-valid state.

  Testing plan

  * Transaction unit tests.
  * Kill/fault injection at state/event/outbox/commit boundaries.
  * Duplicate command/idempotency tests.
  * Detailed phase-event persistence integration tests.
  * Outbox capacity policy tests.
  * Recovery query reconstruction tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Transaction unit tests., Kill/fault injection at state/event/outbox/commit boundaries., Duplicate command/idempotency tests., Detailed phase-event persistence integration tests., Outbox capacity policy tests., Recovery query reconstruction tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T8.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/recorder.py::DurableEventRecorder, atlas/core/lifecycle.py, atlas/core/job_store.py::store_event.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
