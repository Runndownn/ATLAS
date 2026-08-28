@BinReaper Production TODOs

## TODO

* [ ] TODO 121: Model-check lifecycle, lease, fencing, and recovery invariants

  1.2 source task(s): `T30.1.1`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T5.1.4, T9.1.4, T18.1.4, T29.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `specs/atlas-lifecycle/ (create); tests/model/test_model_trace_replay.py (create); scripts/check_lifecycle_model.py (create); docs/architecture/formal-invariants.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Attempt to falsify lifecycle, control, lease, fencing, retry, and crash-recovery invariants before production qualification.
  * Restore or protect this invariant: No modeled interleaving permits two active authorities, an illegal transition, a stale commit, or an unrecoverable ambiguous state.
  * Source lineage: Advanced proof refinement of T5.1.4, T9.1.4, T18.1.4, and the machine-logic evaluation rule; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `specs/atlas-lifecycle/` (create: Store a bounded formal or executable model selected by evidence.); `tests/model/test_model_trace_replay.py` (create: Replay counterexamples against the executable state-machine implementation.); `scripts/check_lifecycle_model.py` (create: Run bounded checks and emit machine-readable traces.); `docs/architecture/formal-invariants.md` (create: Document modeled invariants, abstractions, limits, and maintenance.)
  * Epic boundary: E30 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `specs/atlas-lifecycle/` (create: Store a bounded formal or executable model selected by evidence.); `tests/model/test_model_trace_replay.py` (create: Replay counterexamples against the executable state-machine implementation.); `scripts/check_lifecycle_model.py` (create: Run bounded checks and emit machine-readable traces.); `docs/architecture/formal-invariants.md` (create: Document modeled invariants, abstractions, limits, and maintenance.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Compare a small formal model such as TLA+/PlusCal with a Python executable model and select the simplest approach that finds additional defects and remains maintainable.
  * Model only authoritative states, commands, leases/fences, attempts, crashes, checkpoints, retries, reconciliation, and events; abstract payload processing.
  * Generate counterexample traces that can be converted into executable scenario fixtures.
  * Treat model checking as supplementary evidence, never a replacement for implementation, integration, and crash tests.

  Implementation requirements

  * Define job, phase, attempt, control, lease, fence, checkpoint, event, and recovery variables plus legal transition actions.
  * Encode invariants for single authority, monotonic fencing, terminal-state immutability, control acknowledgement, event/state pairing, bounded retry, idempotency, and deterministic recovery.
  * Explore bounded interleavings with process crash, message duplication/reorder, stale result, lease expiry/renewal, pause/cancel, and checkpoint mismatch.
  * Export minimized counterexample traces and replay them through T29.1.4 scenarios and the implementation.
  * Measure model state-space, runtime, defects found, maintenance cost, and false abstraction gaps; retire unnecessary formal tooling if it adds no measurable value.

  Security and safety requirements

  * Use no production data, credentials, or network access in the model.
  * Do not weaken an invariant merely to reduce state space; document abstractions and coverage boundaries.
  * Treat stale authority, replay, forged identity, and duplicate command actions as explicit adversarial transitions.
  * Hash model inputs/results and require review before accepting changed invariants.
  * Do not claim proof beyond the bounded model and stated assumptions.

  Edge cases and outliers to handle

  * State-space explosion hides important interleavings.
  * The model omits a real implementation side effect or transaction boundary.
  * A counterexample cannot be reproduced because of abstraction mismatch.
  * Model and implementation drift after schema/state changes.
  * The chosen tool is unavailable on a supported developer platform.

  Acceptance criteria (“done” definition)

  * The chosen model and alternatives are evaluated against complexity, defects found, execution cost, and maintainability.
  * All documented invariants hold within declared bounds or produce replayable counterexamples and correction tasks.
  * Every counterexample is minimized and replayed against executable scenarios where the abstraction permits.
  * Model/version drift is detected by CI and no bounded result is described as universal proof.

  Testing plan

  * Model syntax/type and invariant self-tests.
  * Deliberately broken model tests that must produce counterexamples.
  * State-space bound and timeout tests.
  * Counterexample export/minimization tests.
  * Executable trace-replay tests.
  * Schema/state-version drift tests.
  * Deterministic result-manifest tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until the modeling approach is selected and checked into the active repository`; retain exact tool/version/bounds.
  * Expected evidence: deliberate defects are detected, declared invariants hold or yield replayable traces, and model/implementation drift gates pass.
  * Completion record: model/tool versions, assumptions/bounds, commands, state counts, counterexamples, replay results, measured value/maintenance decision, hashes.

  Debugging checklist

  * Confirm the failing trace uses modeled actions that correspond to real implementation boundaries.
  * Reduce variable domains and trace length without changing the violated invariant.
  * Replay the trace in the deterministic scenario harness before changing implementation.
  * Inspect model/version drift whenever state, event, lease, or checkpoint schemas change.

* [ ] TODO 122: Prove immutable intake and race-resistant source access under mutation

  1.2 source task(s): `T30.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T6.1.4, T7.1.4, T10.1.4, T29.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/proofs/test_intake_source_races.py (create); tests/helpers/source_mutator.py (create); benchmarks/source_access/ (create); docs/verification/source-snapshot-proof.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Demonstrate that accepted occurrences and exact-byte identities survive or detect source mutation without downstream raw-path rediscovery.
  * Restore or protect this invariant: Downstream phases consume verified accepted occurrences; changed or unresolvable bytes block rather than silently changing identity.
  * Source lineage: Advanced proof refinement of T6.1.1-T6.1.4, T7.1.1-T7.1.4, and T10.1.1-T10.1.4; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/proofs/test_intake_source_races.py` (create: Execute deterministic source mutation barriers and assert exact outcomes.); `tests/helpers/source_mutator.py` (create: Apply bounded path/content/link/root/mount mutations at named barriers.); `benchmarks/source_access/` (create: Measure safe handle access versus path reopen under representative workloads.); `docs/verification/source-snapshot-proof.md` (create: Document invariants, platform evidence, failures, and limits.)
  * Epic boundary: E30 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/proofs/test_intake_source_races.py` (create: Execute deterministic source mutation barriers and assert exact outcomes.); `tests/helpers/source_mutator.py` (create: Apply bounded path/content/link/root/mount mutations at named barriers.); `benchmarks/source_access/` (create: Measure safe handle access versus path reopen under representative workloads.); `docs/verification/source-snapshot-proof.md` (create: Document invariants, platform evidence, failures, and limits.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Use barrier-controlled mutation across discovery, open, hash, checkpoint, structural inspection, and materialization.
  * Compare descriptor/handle-relative access with legacy path reopening under identical workloads and platform lanes.
  * Assert occurrence identity, native object identity, content digest, mutation evidence, and lifecycle decision separately.
  * Require native Linux, Windows, and macOS evidence for any cross-platform claim.

  Implementation requirements

  * Create scenarios for path replacement, truncate/append, rename/delete, chmod, symlink/junction swap, hard-link alias, root/mount swap, inode/file-ID reuse, and concurrent writers.
  * Capture accepted manifest fields, pre/open/post identity facts, content digest, bytes read, timestamps, file size, and mutation reason.
  * Verify downstream phases use occurrence/handle references and reject raw paths or stale generation/checkpoint data.
  * Exercise resume/retry after source mutation and define when a new intake generation is required.
  * Benchmark safe access overhead, descriptors/handles, open counts, I/O, and failure detection relative to legacy behavior.

  Security and safety requirements

  * Use only synthetic sources under disposable roots and native platform capabilities.
  * Never follow unverified links or mounts during the mutator setup or cleanup.
  * Treat ambiguous native identity or unsupported no-follow behavior as blocked/reduced assurance.
  * Bound writer rates, file sizes, handles, and test duration.
  * Sanitize native paths and system identifiers in shared evidence.

  Edge cases and outliers to handle

  * Mutation occurs after a verified open but before the final read.
  * Object identity is reused after delete/recreate.
  * Network/FUSE filesystems provide weak or unstable identity guarantees.
  * Hashing detects size/time change only after reading substantial bytes.
  * Resume references a valid checkpoint whose source generation is superseded.

  Acceptance criteria (“done” definition)

  * Every mutation scenario yields the exact original content identity, a verified new generation requirement, or a stable blocked/stale result—never silent byte substitution.
  * No downstream built-in phase reopens an untrusted raw path outside canonical SourceAccess.
  * Native platform evidence identifies supported, reduced-assurance, and blocked source semantics.
  * Measured safety overhead and detection cost are reported without weakening invariants.

  Testing plan

  * Barrier and source-mutator determinism tests.
  * Content/path/link/root/mount/inode mutation tests.
  * Cross-platform handle/object-identity tests.
  * Checkpoint/resume and generation-supersession tests.
  * Downstream raw-path rejection tests.
  * Legacy-versus-safe differential tests.
  * Performance/resource and cleanup tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until source-access proof runner and native lane IDs exist`; execute through T28/T29 facilities.
  * Expected evidence: all mutation, generation, identity, downstream-access, resume, cross-platform, and benchmark gates pass.
  * Completion record: platform/lane facts, fixture/mutator digests, commands, accepted manifests, identity traces, outcomes, measurements, cleanup, hashes.

  Debugging checklist

  * Compare accepted occurrence, native object identity, open handle, bytes read, and post-read identity.
  * Locate the exact barrier at which mutation became visible.
  * Reproduce with one file and one mutation on a native filesystem.
  * Trace downstream access calls to ensure no path reopen bypassed SourceAccess.

* [ ] TODO 123: Prove transaction, durable-event, and outbox crash atomicity

  1.2 source task(s): `T30.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T4.1.4, T8.1.4, T18.1.4, T28.1.6`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/proofs/test_state_event_atomicity.py (create); tests/proofs/test_outbox_crash_matrix.py (create); scripts/run_atomicity_proof.py (create); docs/verification/state-event-atomicity.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Demonstrate atomic state/event/outbox behavior across every transition and crash boundary.
  * Restore or protect this invariant: No committed authoritative transition lacks its durable event/outbox intent, and no durable event claims an uncommitted transition.
  * Source lineage: Advanced proof refinement of T4.1.1-T4.1.4, T8.1.1-T8.1.4, and T18.1.4; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/proofs/test_state_event_atomicity.py` (create: Assert state transition and durable event commit together.); `tests/proofs/test_outbox_crash_matrix.py` (create: Exercise dispatch leases, duplicate delivery, ack ambiguity, and recovery.); `scripts/run_atomicity_proof.py` (create: Run repeated external-kill fault points and summarize invariants.); `docs/verification/state-event-atomicity.md` (create: Document transaction boundaries, guarantees, and evidence.)
  * Epic boundary: E30 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/proofs/test_state_event_atomicity.py` (create: Assert state transition and durable event commit together.); `tests/proofs/test_outbox_crash_matrix.py` (create: Exercise dispatch leases, duplicate delivery, ack ambiguity, and recovery.); `scripts/run_atomicity_proof.py` (create: Run repeated external-kill fault points and summarize invariants.); `docs/verification/state-event-atomicity.md` (create: Document transaction boundaries, guarantees, and evidence.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Test before/after each SQL statement, transaction commit, fsync-relevant boundary, dispatcher lease, publish, acknowledgement, and delivery-state update.
  * Use external process kills and database inspection rather than trusting rollback callbacks.
  * Separate authoritative event history from at-least-once transport delivery and consumer idempotency.
  * Run identical invariant checks for SQLite and any later conforming StateStore.

  Implementation requirements

  * Instrument named fault points around guarded transition, event insert, outbox insert, commit, dispatcher claim/lease, publish, confirm/ack, retry, and dead-letter.
  * For every fault, assert exact authoritative state, event sequence, outbox status, delivery attempts, lease/fence state, and startup recovery action.
  * Inject duplicate delivery, consumer crash, publisher timeout after broker receipt, broker restart, poison payload, stale dispatcher, and clock skew.
  * Verify per-job sequence monotonicity, event IDs, correlation/causation, schema version, idempotency keys, and backpressure/dead-letter diagnostics.
  * Repeat scenarios and run integrity/backup/restore checks after hard kills.

  Security and safety requirements

  * Use synthetic brokers/consumers and isolated databases; no production event endpoints.
  * Reject forged event, correlation, job, attempt, and schema identities before dispatch or consumption.
  * Bound queue depth, retries, payload size, logs, and retained database copies.
  * Ensure diagnostic evidence does not include raw artifact bytes or secrets.
  * Treat missing event/state evidence as release-blocking corruption.

  Edge cases and outliers to handle

  * Process dies after database commit but before caller observes success.
  * Broker accepts publish while client times out before confirmation.
  * Dispatcher lease expires during a long publish.
  * Consumer applies effect then crashes before acknowledgement.
  * Disk-full or corruption occurs during transaction or recovery.

  Acceptance criteria (“done” definition)

  * Every tested transition commits state, durable event, and outbox intent atomically or commits none.
  * At-least-once delivery may duplicate transport attempts but never duplicates authoritative state or idempotent consumer effects.
  * Startup reconciliation deterministically resolves every injected crash point with complete evidence.
  * Integrity, backup/restore, sequence, schema, and dead-letter checks pass after repeated hard kills.

  Testing plan

  * Transactional rollback/commit boundary tests.
  * External SIGKILL crash matrix.
  * Outbox lease/fence and stale-dispatcher tests.
  * Duplicate/ack-ambiguity/consumer-crash tests.
  * Broker outage/restart/poison/backpressure tests.
  * Event identity/sequence/schema injection tests.
  * Database integrity/backup/restore post-crash tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until proof runner and transactional schema exist`; execute repeated scenarios through T28.1.6 and service lanes.
  * Expected evidence: state/event/outbox pairing, delivery idempotency, crash recovery, sequence/schema security, and integrity gates pass.
  * Completion record: schema/migration versions, fault catalog, DB/broker/lane versions, commands, rows/events/outbox traces, recovery results, integrity reports, hashes.

  Debugging checklist

  * Inspect committed transaction rows before logs or broker state.
  * Identify the exact fault point, transaction ID, event sequence, outbox ID, lease/fence, and delivery attempt.
  * Reproduce with one transition and one subscriber.
  * Compare startup recovery decision to the operation-semantics registry and retained evidence.
