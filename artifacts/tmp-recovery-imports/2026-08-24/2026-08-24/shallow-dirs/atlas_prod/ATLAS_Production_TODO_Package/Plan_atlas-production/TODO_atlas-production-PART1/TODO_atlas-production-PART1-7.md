@BinReaper Production TODOs

## TODO

* [ ] TODO 19: Implement guarded atomic transitions and fencing tokens

  1.2 source task(s): `T5.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T5.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/lifecycle.py::LifecycleCoordinator (create); atlas/persistence/repositories/transitions.py (create); atlas/core/orchestrator.py::PipelineOrchestrator (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Apply state changes through one coordinator path that compares expected state/version, advances fencing authority, and records the transition atomically.
  * Restore or protect this invariant: Every transition requires the expected current state/version and fails deterministically when stale.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15.

  Where this applies

  * Primary affected components: `atlas/core/lifecycle.py::LifecycleCoordinator` (create: Own authoritative transition commands.); `atlas/persistence/repositories/transitions.py` (create: Perform compare-and-set mutations.); `atlas/core/orchestrator.py::PipelineOrchestrator` (refactor: Become a compatibility facade over the coordinator.)
  * Epic boundary: Explicit lifecycle state machines, attempts, and fencing — Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.
  * Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-004 requires: Current mutable status fields do not define legal transitions, attempts, fencing, immutable terminal truth, or stale-result behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Apply state changes through one coordinator path that compares expected state/version, advances fencing authority, and records the transition atomically.
  * Component dispositions: `atlas/core/lifecycle.py::LifecycleCoordinator` (create: Own authoritative transition commands.); `atlas/persistence/repositories/transitions.py` (create: Perform compare-and-set mutations.); `atlas/core/orchestrator.py::PipelineOrchestrator` (refactor: Become a compatibility facade over the coordinator.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Implement transition commands with expected state/version, actor, reason, correlation, and required evidence references.
  * Issue monotonically changing fencing tokens or equivalent lease epochs when execution authority changes.
  * Atomically update canonical state and transition sequence; event atomicity is completed in E8.
  * Reject stale, duplicate, out-of-order, or unauthorized transition requests with stable reason codes.

  Security and safety requirements

  * Only coordinator/service identities authorized by the core can call mutation repositories.
  * Treat all adapter, worker, plugin, and user-supplied state values as requests, never direct mutations.
  * Fencing values are unpredictable or integrity-protected where remote trust will later matter.
  * Rejected transitions are auditable without exposing secrets.

  Edge cases and outliers to handle

  * Two processes attempt the same transition.
  * Lease expires while a result is in flight.
  * Cancellation races with success commit.
  * Database retry replays a transition command.

  Acceptance criteria (“done” definition)

  * Every transition requires the expected current state/version and fails deterministically when stale.
  * Stale fencing tokens cannot commit result or terminal state.
  * Concurrent transition tests produce one winner and auditable losers.
  * No production code mutates lifecycle status fields outside the coordinator/repository path.

  Testing plan

  * Compare-and-set unit tests.
  * Concurrent process race tests.
  * Stale fencing-result tests.
  * Cancellation-versus-success race tests.
  * Idempotent command replay tests.
  * Static direct-mutation guard.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Compare-and-set unit tests., Concurrent process race tests., Stale fencing-result tests., Cancellation-versus-success race tests., Idempotent command replay tests., Static direct-mutation guard..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T5.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/lifecycle.py::LifecycleCoordinator, atlas/persistence/repositories/transitions.py, atlas/core/orchestrator.py::PipelineOrchestrator.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 20: Add model-based state-machine and invalid-transition verification

  1.2 source task(s): `T5.1.4`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T5.1.2, T5.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/state_machine/ (create); tests/fixtures/state_sequences/ (create); atlas diagnostics transition errors (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prove the transition system under generated sequences, concurrency, restart, and malformed input rather than relying only on hand-picked happy paths.
  * Restore or protect this invariant: Model and implementation agree across the declared generated sequence budget.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15.

  Where this applies

  * Primary affected components: `tests/state_machine/` (create: Host model-based and property tests.); `tests/fixtures/state_sequences/` (create: Store minimized regression sequences.); `atlas diagnostics transition errors` (extend: Expose stable state/version/fencing context.)
  * Epic boundary: Explicit lifecycle state machines, attempts, and fencing — Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.
  * Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-004 requires: Current mutable status fields do not define legal transitions, attempts, fencing, immutable terminal truth, or stale-result behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prove the transition system under generated sequences, concurrency, restart, and malformed input rather than relying only on hand-picked happy paths.
  * Component dispositions: `tests/state_machine/` (create: Host model-based and property tests.); `tests/fixtures/state_sequences/` (create: Store minimized regression sequences.); `atlas diagnostics transition errors` (extend: Expose stable state/version/fencing context.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Build a reference model for job, phase, attempt, and control transitions.
  * Generate valid and invalid command sequences, compare implementation state to the model, and minimize failures.
  * Inject cancellation, process loss, duplicate commands, stale results, and storage faults at transition boundaries.
  * Retain counterexample sequences and transition histories as regression fixtures.

  Security and safety requirements

  * Generated tests must remain bounded in steps, state size, and runtime.
  * Do not include raw source payloads in counterexample artifacts.
  * Malformed actor/correlation/state data is rejected before mutation.
  * A diagnostics failure cannot change transition outcome.

  Edge cases and outliers to handle

  * Long valid sequence with repeated pause/resume/retry.
  * Invalid transition from every terminal state.
  * Crash between attempt result and phase/job propagation.
  * Version skew in serialized state or command.

  Acceptance criteria (“done” definition)

  * Model and implementation agree across the declared generated sequence budget.
  * Every illegal transition class has a stable error code and zero authoritative mutation.
  * Counterexamples are reproducible and retained.
  * State-machine tests run in mandatory CI without unapproved skips.

  Testing plan

  * Property-based transition sequence tests.
  * Concurrency and compare-and-set tests.
  * Crash/restart fault injection.
  * Malformed command fuzz tests.
  * Version-skew serialization tests.
  * Regression replay of minimized counterexamples.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Property-based transition sequence tests., Concurrency and compare-and-set tests., Crash/restart fault injection., Malformed command fuzz tests., Version-skew serialization tests., Regression replay of minimized counterexamples..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T5.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/state_machine/, tests/fixtures/state_sequences/, atlas diagnostics transition errors.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 21: Define `SourceRoot`, `IntakeGeneration`, and `ArtifactOccurrence` schemas

  1.2 source task(s): `T6.1.1`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T4.1.4, T5.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/models.py::SourceRoot (create); atlas/artifacts/models.py::IntakeGeneration (create); atlas/artifacts/models.py::ArtifactOccurrence (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create typed, versioned records that separate registered source authority, one observation generation, and each location/type observed under that generation.
  * Restore or protect this invariant: Occurrence and content concepts remain structurally distinct.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/models.py::SourceRoot` (create: Represent stable source identity and provider locator.); `atlas/artifacts/models.py::IntakeGeneration` (create: Represent BUILDING/ACCEPTED/FAILED/BLOCKED observations.); `atlas/artifacts/models.py::ArtifactOccurrence` (create: Represent source-relative observed entries and decisions.)
  * Epic boundary: Registered sources and immutable intake generations — Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]
  * Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-005 requires: Downstream phases currently rediscover mutable sources, so a job has no immutable occurrence set or completeness decision.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create typed, versioned records that separate registered source authority, one observation generation, and each location/type observed under that generation.
  * Component dispositions: `atlas/artifacts/models.py::SourceRoot` (create: Represent stable source identity and provider locator.); `atlas/artifacts/models.py::IntakeGeneration` (create: Represent BUILDING/ACCEPTED/FAILED/BLOCKED observations.); `atlas/artifacts/models.py::ArtifactOccurrence` (create: Represent source-relative observed entries and decisions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define stable IDs, provider type, normalized locator, allowed-root policy, generation state, manifest digest, traversal policy digest, and timestamps.
  * Define occurrence relative path, entry type, size, mode, timestamps, device/inode where available, link/special status, exclusion/error reason, and observation sequence.
  * Define uniqueness, foreign keys, immutability, and supersession relationships.
  * Publish serialization/schema versions and authority classification for each field.

  Security and safety requirements

  * Do not store arbitrary absolute paths as downstream artifact identity.
  * Canonical locators and relative paths are validated separately from byte identity.
  * Sensitive source names can be redacted in telemetry while canonical records remain protected.
  * Provider-specific metadata cannot grant filesystem authority.

  Edge cases and outliers to handle

  * Case-insensitive path collisions and Unicode normalization variants.
  * Dangling links, sockets, devices, FIFOs, inaccessible entries.
  * Source root is renamed, remounted, or points to a different object.
  * Provider lacks inode/device semantics.

  Acceptance criteria (“done” definition)

  * Occurrence and content concepts remain structurally distinct.
  * Every occurrence belongs to exactly one generation and one source root.
  * Accepted generation records are immutable and supersession is explicit.
  * Schema supports local filesystem now without claiming unsupported provider semantics.

  Testing plan

  * Schema and serialization unit tests.
  * Uniqueness/FK negative tests.
  * Case/Unicode collision fixtures.
  * Provider-capability compatibility tests.
  * Immutability/supersession tests.
  * Migration round-trip tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Schema and serialization unit tests., Uniqueness/FK negative tests., Case/Unicode collision fixtures., Provider-capability compatibility tests., Immutability/supersession tests., Migration round-trip tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T6.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/models.py::SourceRoot, atlas/artifacts/models.py::IntakeGeneration, atlas/artifacts/models.py::ArtifactOccurrence.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
