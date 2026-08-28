@BinReaper Production TODOs

## TODO

* [ ] TODO 118: Create the persistence, event, control, and concurrency scenario corpus

  1.2 source task(s): `T29.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.5, T28.1.6, T5.1.4, T8.1.4, T9.1.4, T19.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/fixtures/scenarios/ (create); tests/model/scenario.schema.json (create); tests/integration/test_concurrency_scenarios.py (create); docs/testing/state-event-scenario-corpus.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create deterministic multi-actor scenarios for transition races, controls, leases, events, checkpoints, retries, and persistence contention.
  * Restore or protect this invariant: Concurrent or repeated operations resolve to one legal authoritative state with explicit losers, no stale authority, and complete durable evidence.
  * Source lineage: Expansion of T5.1.1-T5.1.4, T8.1.1-T8.1.4, T9.1.1-T9.1.4, T18, and T19; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/fixtures/scenarios/` (create: Store declarative state, event, control, lease, checkpoint, and concurrency scenarios.); `tests/model/scenario.schema.json` (create: Version initial state, actors, barriers, commands, faults, and expected durable outcomes.); `tests/integration/test_concurrency_scenarios.py` (create: Execute multi-process scenarios against StateStore and runtime services.); `docs/testing/state-event-scenario-corpus.md` (create: Document scenario semantics, scheduling, and oracles.)
  * Epic boundary: E29 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/fixtures/scenarios/` (create: Store declarative state, event, control, lease, checkpoint, and concurrency scenarios.); `tests/model/scenario.schema.json` (create: Version initial state, actors, barriers, commands, faults, and expected durable outcomes.); `tests/integration/test_concurrency_scenarios.py` (create: Execute multi-process scenarios against StateStore and runtime services.); `docs/testing/state-event-scenario-corpus.md` (create: Document scenario semantics, scheduling, and oracles.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Describe initial durable state, actors, barriers, commands, injected faults, permitted interleavings, and exact terminal invariants.
  * Use deterministic barriers and model-generated schedules rather than sleep-based races.
  * Separate authoritative state/event history from transport delivery and telemetry.
  * Run the same scenarios against local and later conforming StateStore/event adapters.

  Implementation requirements

  * Create cases for duplicate start/control/review/publication commands, simultaneous transitions, pause/cancel/resume races, stale checkpoints, retry successors, lease renewal/loss, fencing, and stale worker results.
  * Create outbox duplicate/reorder/poison/backpressure/consumer failure and event-schema/version mismatch cases.
  * Create SQLite busy/lock, process crash, migration skew, clock skew, restart, and unknown-outcome reconciliation cases.
  * Define exact rows, transition/event sequence, command status, idempotency outcome, lease/fence generation, checkpoint disposition, and diagnostics for each scenario.
  * Execute schedules repeatedly and store normalized traces/counterexamples without relying on wall-clock timing.

  Security and safety requirements

  * Actors use synthetic identities and scoped commands; no test has direct table mutation except explicit corruption fixtures.
  * Reject replayed commands, stale fencing, forged event/attempt IDs, schema downgrade, and cross-job control.
  * Bound actor count, trace size, retries, events, and retained database copies.
  * Sanitize diagnostic bundles and prevent raw fixture content from entering logs.
  * Require crash cleanup and database integrity checks before reusing a lane.

  Edge cases and outliers to handle

  * Two legal transitions contend and one loses after side effects were prepared.
  * Clock skew changes lease observation but not monotonic fencing.
  * Event transport duplicates while state/event history remains singular.
  * Migration/schema mismatch appears during a restart scenario.
  * SQLite busy timeout or disk-full masks the intended concurrency outcome.

  Acceptance criteria (“done” definition)

  * Every scenario validates against the schema and names legal outcomes, forbidden states, and exact durable evidence.
  * Repeated schedules never produce invalid transition, stale authority commit, missing state event, or duplicate authoritative effect.
  * Transport duplicates/reordering do not alter authoritative state and are visible through delivery evidence.
  * Failures yield deterministic reconciliation or blocked operator action rather than guessed success.

  Testing plan

  * Scenario-schema and schedule-determinism tests.
  * Transition/control race and idempotency tests.
  * Lease/fence/stale-result tests.
  * Checkpoint/retry/restart tests.
  * Outbox duplicate/reorder/poison/backpressure tests.
  * SQLite contention/migration/clock-skew tests.
  * Trace normalization, minimization, and diagnostic-sanitization tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until scenario runner and authoritative stores exist`; execute under T28.1.5/T28.1.6 lanes.
  * Expected evidence: all scenario oracles, repeatability, stale-authority, event-delivery, contention, recovery, and security gates pass.
  * Completion record: scenario schema/catalog digests, seeds/schedules, backend/lane manifests, commands, normalized traces, minimized failures, integrity checks, hashes.

  Debugging checklist

  * Compare initial state, actor commands, barrier order, transaction result, fence generation, event sequence, and final projection.
  * Identify whether failure is an illegal transition, duplicate effect, missing evidence, or harness schedule drift.
  * Replay the minimized schedule with one actor pair and one fault.
  * Inspect authoritative database rows before transport/log output.

* [ ] TODO 119: Build cross-platform contract, differential, and semantic-equivalence runners

  1.2 source task(s): `T29.1.5`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T29.1.1, T29.1.2, T29.1.3, T29.1.4, T15.1.4, T23.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/contracts/ (create); tests/differential/ (create); scripts/run_contract_matrix.py (create); docs/testing/contract-matrix.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prove that adapters, platforms, and versions preserve the same authoritative semantics while allowing explicitly documented operational differences.
  * Restore or protect this invariant: Any implementation advertised as conforming passes the same observable state, lineage, error, replay, and safety contracts.
  * Source lineage: Expansion of T4, T10, T12, T14, T15, T23, and T24.1.2; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/contracts/` (create: Host reusable conformance suites for state, storage, source, execution, plugins, events, and configuration.); `tests/differential/` (create: Normalize and compare platform/backend/version outcomes.); `scripts/run_contract_matrix.py` (create: Execute contracts across selected lanes and emit compatibility evidence.); `docs/testing/contract-matrix.md` (create: Publish mandatory contracts, normalization, exceptions, and supported implementations.)
  * Epic boundary: E29 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/contracts/` (create: Host reusable conformance suites for state, storage, source, execution, plugins, events, and configuration.); `tests/differential/` (create: Normalize and compare platform/backend/version outcomes.); `scripts/run_contract_matrix.py` (create: Execute contracts across selected lanes and emit compatibility evidence.); `docs/testing/contract-matrix.md` (create: Publish mandatory contracts, normalization, exceptions, and supported implementations.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Define contracts by observable inputs, authoritative outputs, side effects, errors, idempotency, recovery, and evidence—not internal implementation.
  * Normalize volatile platform fields while preserving identity, ordering, policy, and failure semantics.
  * Compare one trusted reference implementation against each adapter/backend/platform/version candidate.
  * Require exceptions to be versioned, owned, time-bounded, and unable to weaken safety or authority.

  Implementation requirements

  * Create conformance suites for StateStore, ContentStore, SourceAccess, ExecutionBackend, Plugin SDK, configuration loader, durable events/outbox, status, and destination adapters.
  * Define normalized result schemas and explicit fields that may differ by platform or backend.
  * Run same fixtures, faults, and commands against reference and candidate implementations and produce field-level semantic diffs.
  * Include forward/backward compatibility, migration, mixed-version, replay, cancellation, timeout, and resource-accounting cases.
  * Publish machine-readable pass/fail/reduced-assurance results tied to implementation/version/environment/fixture digests.

  Security and safety requirements

  * A normalization rule cannot discard authorization, identity, provenance, error, or policy differences.
  * Run candidates with least privilege and synthetic data; do not share writable authority stores between comparison lanes.
  * Reject unknown schema fields/versions at authority boundaries unless an explicit translator exists.
  * Scan differential artifacts for secrets, raw content, and platform path leakage.
  * Treat skipped mandatory contracts as non-conformance.

  Edge cases and outliers to handle

  * Reference behavior itself is later found incorrect.
  * Equivalent outcomes differ in ordering where ordering is or is not authoritative.
  * Platform error codes differ but map to one stable taxonomy.
  * A candidate passes normal operations but diverges under crash/replay.
  * Version translators lose fields or confidence/provenance.

  Acceptance criteria (“done” definition)

  * Every advertised adapter/backend/plugin/platform implementation has a versioned contract result and exact environment/fixture binding.
  * Normalization preserves all authoritative fields and flags every unapproved semantic difference.
  * Normal, fault, replay, migration, cancellation, and resource cases pass before conformance is claimed.
  * Unsupported implementations are blocked or labeled reduced-assurance and cannot enter stronger release matrices.

  Testing plan

  * Contract-suite self-tests and negative reference implementations.
  * Normalization schema and forbidden-field-drop tests.
  * Reference/candidate normal-operation differentials.
  * Fault/replay/cancellation/migration differentials.
  * Cross-platform error-taxonomy tests.
  * Version/translator compatibility tests.
  * Evidence-manifest and skip/exception policy tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until contract runner and implementations exist`; execute selected matrices through T28.1.1.
  * Expected evidence: self-tests, normal/fault/version/platform differentials, normalization guards, and evidence/exception policy pass.
  * Completion record: contract versions, reference/candidate versions, lane/fixture digests, commands, field-level diffs, exceptions, hashes, and approval.

  Debugging checklist

  * Determine whether the difference is authoritative, operational, volatile, or a normalization bug.
  * Compare raw outputs before normalized projections.
  * Reproduce one contract case with one reference and one candidate.
  * Trace identity, transition, side effect, error taxonomy, and evidence fields end to end.

* [ ] TODO 120: Add mutation, property, fuzz, metamorphic, and corpus-triage automation

  1.2 source task(s): `T29.1.6`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T29.1.1, T29.1.2, T29.1.3, T29.1.4, T24.1.2`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/property/ (create); tests/fuzz/ (create); tests/metamorphic/ (create); scripts/triage_test_failure.py (create); docs/testing/fuzzing-and-triage.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Continuously search beyond enumerated examples and turn every reproducible failure into a bounded versioned regression case.
  * Restore or protect this invariant: Generated and mutated inputs cannot crash, escape, silently corrupt authority, or produce non-reproducible failures without retained evidence.
  * Source lineage: Expansion of T24.1.2 and deep-review Testing Architecture Upgrade; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/property/` (create: Host state, identity, budget, replay, and configuration property tests.); `tests/fuzz/` (create: Host bounded fuzz harnesses for parsers, protocols, config, events, archives, and APIs.); `tests/metamorphic/` (create: Assert transformations that must preserve or predictably change results.); `scripts/triage_test_failure.py` (create: Minimize, sanitize, classify, and retain reproducible failures.); `docs/testing/fuzzing-and-triage.md` (create: Document seeds, limits, corpora, oracles, and promotion to regressions.)
  * Epic boundary: E29 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/property/` (create: Host state, identity, budget, replay, and configuration property tests.); `tests/fuzz/` (create: Host bounded fuzz harnesses for parsers, protocols, config, events, archives, and APIs.); `tests/metamorphic/` (create: Assert transformations that must preserve or predictably change results.); `scripts/triage_test_failure.py` (create: Minimize, sanitize, classify, and retain reproducible failures.); `docs/testing/fuzzing-and-triage.md` (create: Document seeds, limits, corpora, oracles, and promotion to regressions.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Use properties and metamorphic relations where exact outputs are too large, while preserving exact authority/state oracles.
  * Fuzz only bounded pure parsers or isolated service boundaries; run side-effecting fuzz cases in disposable lanes.
  * Seed from governed corpora and retain minimized sanitized regressions with provenance.
  * Separate product defect, harness defect, environment defect, and flaky/non-reproducible outcomes.

  Implementation requirements

  * Create property/state-machine tests for lifecycle transitions, idempotency, occurrence/content identity, manifests, resource budgets, events, checkpoints, and compatibility.
  * Create fuzz harnesses for pipeline config, event/API schemas, subprocess protocol, archive metadata, identifiers, status pagination, migrations, and plugin results.
  * Add metamorphic checks: traversal order does not change canonical manifest; rename changes occurrence not content identity; duplicate delivery does not duplicate state; tighter budgets cannot increase accepted work; equivalent config normalization yields one digest.
  * Enforce per-example/process/total time, memory, disk, output, recursion, and corpus limits.
  * Implement automated minimization, secret/path sanitization, deduplication, classification, issue metadata, and regression promotion.

  Security and safety requirements

  * Never fuzz production services, destinations, or real data.
  * Run native parser fuzzing with sanitizers where supported and side-effecting harnesses in isolated disposable lanes.
  * Block corpora containing credentials, personal data, exploit secrets, or unbounded decompression behavior.
  * Treat hangs, excessive allocation, log flooding, path escape, and cleanup failure as security-relevant failures.
  * Hash and review retained minimized inputs before committing.

  Edge cases and outliers to handle

  * Minimization removes the timing or platform condition needed to reproduce.
  * Coverage guidance drives pathological resource use.
  * A property encodes current defective behavior.
  * Different Python/library versions produce distinct parser behavior.
  * A crash prevents writing the failing seed.

  Acceptance criteria (“done” definition)

  * Each critical parser/state boundary has a bounded property, fuzz, or metamorphic harness with explicit oracle and limits.
  * All failures retain seed/input/environment/command and minimize to a reproducible sanitized regression or are labeled non-reproducible with evidence.
  * No fuzz lane can reach production resources or exceed outer quotas.
  * Regression corpora remain licensed/provenanced, secret-free, deduplicated, and versioned.

  Testing plan

  * Property-oracle and deliberate-mutant tests.
  * Fuzz harness smoke and seed-replay tests.
  * Limit/timeout/OOM/output containment tests.
  * Metamorphic relation positive/negative tests.
  * Minimization and cross-environment reproduction tests.
  * Secret/path/license/provenance scans.
  * Corpus deduplication and regression-promotion tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until harness targets and repository-native runners exist`; record exact seeds, limits, and commands.
  * Expected evidence: deliberate mutants are found, seeds replay, limits contain failures, minimization/sanitization works, and corpora pass governance checks.
  * Completion record: harness/tool versions, corpus/seed digests, lane manifests, commands, coverage boundaries, minimized failures, retained regressions, hashes.

  Debugging checklist

  * Reproduce the exact seed in the recorded environment before minimizing.
  * Determine whether failure is oracle, harness, environment, or product behavior.
  * Disable coverage guidance and isolate one parser/state boundary if resource use dominates.
  * Retain the smallest sanitized input plus authoritative state/trace evidence.
