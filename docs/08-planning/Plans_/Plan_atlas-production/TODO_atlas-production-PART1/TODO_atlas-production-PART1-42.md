@BinReaper Production TODOs

## TODO

* [ ] TODO 124: Prove CAS, deterministic reuse, and derivation correctness under contention

  1.2 source task(s): `T30.1.4`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T12.1.4, T16.1.3, T29.1.5`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/proofs/test_content_store_reuse.py (create); tests/proofs/test_derivation_contention.py (create); benchmarks/reuse/ (create); docs/verification/content-reuse-proof.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Demonstrate that managed content and reusable deterministic results remain exact, immutable, and fully traceable under concurrency and corruption.
  * Restore or protect this invariant: Canonical SHA-256 identity, no-replace storage, exact reuse keys, and derivation lineage cannot be altered by concurrent or stale writers.
  * Source lineage: Advanced proof refinement of T12.1.1-T12.1.4, T13.1.4, and T16.1.3; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/proofs/test_content_store_reuse.py` (create: Verify staged no-replace content commits and exact-key result reuse.); `tests/proofs/test_derivation_contention.py` (create: Exercise concurrent writers, derivations, references, and cleanup.); `benchmarks/reuse/` (create: Measure deduplication, reuse, contention, storage, and invalidation.); `docs/verification/content-reuse-proof.md` (create: Document guarantees, invalidation keys, benchmarks, and limits.)
  * Epic boundary: E30 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/proofs/test_content_store_reuse.py` (create: Verify staged no-replace content commits and exact-key result reuse.); `tests/proofs/test_derivation_contention.py` (create: Exercise concurrent writers, derivations, references, and cleanup.); `benchmarks/reuse/` (create: Measure deduplication, reuse, contention, storage, and invalidation.); `docs/verification/content-reuse-proof.md` (create: Document guarantees, invalidation keys, benchmarks, and limits.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Keep SHA-256 canonical even when BLAKE3 or other hashes accelerate detection; always verify committed bytes.
  * Stage, fsync/verify as required, and atomically no-replace commit content; concurrent identical writers converge on one verified object.
  * Define reuse keys from operation/version, input content identities, normalized config, policy, tool/plugin/model versions, and relevant context.
  * Treat storage deduplication, computation reuse, and provenance linking as separate mechanisms with separate evidence.

  Implementation requirements

  * Create concurrent identical/different write, partial stage, corrupt stage, pre-existing corrupt blob, interrupted rename, quota, reference, orphan, and retention-race scenarios.
  * Use a test-only fake digest provider to force collision-handling paths while still requiring canonical SHA-256 verification for real commits.
  * Exercise reuse hits/misses and invalidation when any key component changes, including source-dependent context and policy/model/tool versions.
  * Assert immutable content metadata, occurrence/content links, derivation edges, result provenance, reference counts/holds, and replayability status.
  * Benchmark duplicate-heavy runs, writer contention, open/hash/copy I/O, storage saved, analysis work avoided, database pressure, and cleanup cost.

  Security and safety requirements

  * Never trust provider ETag/path/size or accelerated digest as canonical identity.
  * Reject corrupt existing objects, mismatched lengths/digests, stale reuse records, and unauthorized retention/hold changes.
  * Run all storage tests in disposable roots with quotas and synthetic bytes.
  * Prevent GC/retention from deleting referenced, held, staged, unknown, or evidence-bearing objects.
  * Scan manifests and diagnostics for raw content or secret leakage.

  Edge cases and outliers to handle

  * Two writers commit identical content while one crashes after staging.
  * A blob exists at the expected path but bytes or metadata are corrupt.
  * Reuse keys collide due to omitted configuration, policy, plugin, or model context.
  * Reference/hold changes race with garbage collection.
  * Cross-device storage prevents atomic rename.

  Acceptance criteria (“done” definition)

  * Concurrent identical writers converge on one verified immutable object; corrupt or partial objects never become trusted.
  * Reuse occurs only for exact compatible keys and misses on every semantically relevant version/config/policy/context change.
  * All reused and derived results retain exact source/content/operation/attempt lineage and replayability state.
  * Benchmarks report semantic-equivalence checks, storage/work savings, contention, and failure cost without arbitrary scale claims.

  Testing plan

  * Concurrent staged/no-replace write tests.
  * Partial/corrupt/pre-existing object and collision-path tests.
  * Reuse-key hit/miss/invalidation property tests.
  * Derivation/reference/hold/retention race tests.
  * Crash/quota/cross-device reconciliation tests.
  * Semantic-equivalence tests for reused versus recomputed results.
  * Duplicate-heavy performance/resource benchmarks.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until ContentStore/reuse implementations and proof runner exist`; run in approved storage lanes.
  * Expected evidence: content integrity, contention, invalidation, lineage, retention, crash, semantic-equivalence, and benchmark gates pass.
  * Completion record: store/schema/key versions, lane/config/fixture digests, commands, object/lineage evidence, measurements, reconciliation/cleanup, hashes.

  Debugging checklist

  * Verify canonical digest and bytes before interpreting path or metadata.
  * Compare full reuse-key components and versions for unexpected hits/misses.
  * Trace stage, commit, reference, derivation, hold, and cleanup transactions.
  * Reproduce with two writers, one object, and one controlled failure.

* [ ] TODO 125: Prove idempotent publication and unknown-outcome reconciliation

  1.2 source task(s): `T30.1.5`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T17.1.4, T18.1.4, T21.1.4, T29.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/proofs/test_publication_exactly_once_visible.py (create); tests/doubles/publication_destinations.py (create); scripts/run_publication_reconciliation.py (create); docs/verification/publication-proof.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Demonstrate that approved publication produces one idempotent observable effect or a deterministically reconciled blocked state despite retries and ambiguous outcomes.
  * Restore or protect this invariant: No publication executes without a current approved decision and idempotency identity; unknown outcomes are reconciled rather than blindly repeated.
  * Source lineage: Advanced proof refinement of T17.1.3-T17.1.4, T18.1.1-T18.1.4, and T21.1.4; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/proofs/test_publication_exactly_once_visible.py` (create: Verify idempotent observable publication effects and decision binding.); `tests/doubles/publication_destinations.py` (create: Model queryable, non-queryable, slow, duplicate, conflicting, and ambiguous destinations.); `scripts/run_publication_reconciliation.py` (create: Execute commit/timeout/retry/reconcile matrices.); `docs/verification/publication-proof.md` (create: Document guarantees, destination classes, recovery, and limits.)
  * Epic boundary: E30 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/proofs/test_publication_exactly_once_visible.py` (create: Verify idempotent observable publication effects and decision binding.); `tests/doubles/publication_destinations.py` (create: Model queryable, non-queryable, slow, duplicate, conflicting, and ambiguous destinations.); `scripts/run_publication_reconciliation.py` (create: Execute commit/timeout/retry/reconcile matrices.); `docs/verification/publication-proof.md` (create: Document guarantees, destination classes, recovery, and limits.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Promise idempotent observable effects under adapter contracts, not impossible literal exactly-once transport.
  * Use request, decision/evidence digest, destination identity, operation version, idempotency key, attempt, verification, and reconciliation records.
  * Classify destinations by queryability, atomic staging/commit, conditional create/no-replace, and compensation support.
  * Keep review/policy authority separate from destination execution and verification.

  Implementation requirements

  * Create doubles for local atomic destination, conditional-create service, queryable remote service, non-queryable side effect, slow/timeout, duplicate callback, conflict, partial response, and unavailable destination.
  * Inject faults before/after stage, external mutation, response, verify, publication record, event/outbox, and decision revocation.
  * Assert current decision/evidence/content binding, idempotency reservation/finalization, staged output identity, external effect query, verification manifest, lineage, and final disposition.
  * Define retry versus reconcile versus HOLD/manual-resolution behavior for each destination/operation semantics class.
  * Verify duplicate commands, webhook replays, stale attempts, conflicting prior effects, interrupted rollback/compensation, and operator diagnostics.

  Security and safety requirements

  * Use synthetic destinations and credentials; no production publication target.
  * Require authorization/policy and current evidence decision before each consequential attempt.
  * Reject stale/replayed commands, mismatched destination/content/decision IDs, forged callbacks, and unauthorized overwrite.
  * Redact destination credentials and sensitive payloads from events/diagnostics.
  * Preserve evidence and require explicit operator resolution when non-queryable effects remain ambiguous.

  Edge cases and outliers to handle

  * Destination mutates successfully but client times out before response.
  * Verification sees conflicting pre-existing content.
  * Approval is revoked between staging and commit.
  * Destination is non-queryable and cannot provide idempotency support.
  * Compensation fails after partial external mutation.

  Acceptance criteria (“done” definition)

  * Every destination class has explicit idempotency, verification, retry/reconcile, conflict, and unknown-outcome semantics.
  * Duplicate commands/retries never create a second observable effect under supported adapter contracts.
  * Ambiguous non-queryable outcomes become HOLD/manual-resolution with retained evidence, not success or blind retry.
  * Every successful publication links exact content, evidence/decision, destination effect, attempt, verification, and event history.

  Testing plan

  * Decision/evidence/content binding tests.
  * Duplicate command/idempotency reservation tests.
  * Timeout-after-mutation and unknown-outcome reconciliation tests.
  * Conflict/no-replace/stale-decision tests.
  * Queryable versus non-queryable destination tests.
  * Callback/webhook replay and forged-identity tests.
  * Compensation/rollback failure and diagnostic-evidence tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until publication adapters, doubles, and proof runner exist`; execute only against synthetic destinations.
  * Expected evidence: binding, idempotency, ambiguous outcome, conflict, replay, reconciliation, lineage, and security gates pass.
  * Completion record: adapter/operation versions, destination class, scenario/lane digests, commands, external effect logs, decision/publication records, recovery result, hashes.

  Debugging checklist

  * Start with idempotency key, decision/evidence/content digest, destination identity, attempt, and operation semantics.
  * Determine whether mutation occurred by destination query or retained external evidence before retrying.
  * Compare stage, execute, verify, record, and event boundaries.
  * Reproduce with one destination double and one fault point.

* [ ] TODO 126: Run the production-qualification upgrade, rollback, disaster, and soak program

  1.2 source task(s): `T30.1.6`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T30.1.1, T30.1.2, T30.1.3, T30.1.4, T30.1.5, T24.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/qualification/ (create); scripts/run_production_qualification.py (create); .github/workflows/production-qualification.yml (create); docs/operations/production-qualification.md (create); docs/operations/disaster-recovery.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Exercise the complete release candidate through clean install, compatibility migration, sustained workload, failures, backup/restore, rollback, and operational recovery.
  * Restore or protect this invariant: A release is not described as production-qualified until mandatory native lanes, migrations, failure recovery, security, performance, diagnostics, and rollback evidence all pass.
  * Source lineage: Final qualification refinement of T24.1.1-T24.1.4 and all preceding P0/P1 work; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/qualification/` (create: Host release-candidate install, migration, failure, soak, and rollback scenarios.); `scripts/run_production_qualification.py` (create: Orchestrate approved qualification lanes and assemble evidence.); `.github/workflows/production-qualification.yml` (create: Run gated scheduled/release-candidate qualification jobs.); `docs/operations/production-qualification.md` (create: Define entry/exit gates, workload profiles, evidence, and approval.); `docs/operations/disaster-recovery.md` (create: Define backup, restore, corruption, failback, and evidence procedures.)
  * Epic boundary: E30 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/qualification/` (create: Host release-candidate install, migration, failure, soak, and rollback scenarios.); `scripts/run_production_qualification.py` (create: Orchestrate approved qualification lanes and assemble evidence.); `.github/workflows/production-qualification.yml` (create: Run gated scheduled/release-candidate qualification jobs.); `docs/operations/production-qualification.md` (create: Define entry/exit gates, workload profiles, evidence, and approval.); `docs/operations/disaster-recovery.md` (create: Define backup, restore, corruption, failback, and evidence procedures.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Use the approved support matrix and representative workload catalog; do not invent universal durations or throughput targets.
  * Test a packaged release candidate against a predecessor database/config/plugin/checkpoint/event population and a clean installation.
  * Inject service, process, host, disk, source, plugin, event, and publication failures during sustained operation.
  * Make rollback depend on stored-data compatibility and explicit restore/failback procedures rather than only reinstalling code.
  * Assemble one immutable release evidence bundle with pass/fail/skip, limitations, hashes, and reviewer sign-off.

  Implementation requirements

  * Install built wheel/sdist in clean native lanes; verify CLI, Python API, configuration, migrations, daemon/status, lifecycle, safety, plugins, events, review, publication, diagnostics, and shutdown.
  * Create predecessor-state fixtures and perform upgrade, mixed-version rejection, forward migration, backup, restore, application rollback, schema/data rollback or forward-fix, and failback drills.
  * Run approved bounded soak profiles with concurrent jobs, duplicate-heavy inputs, large/deep generated workloads, expensive analyzers, event backlog, content reuse, retention, and cleanup.
  * Inject process/host restart, SQLite contention/corruption, disk/inode pressure, service outages, plugin failures, source mutation, event failure, and interrupted publication while measuring recovery time and operator intervention.
  * Verify SBOM/provenance/package hashes, secret scans, health/readiness/status/diagnostic quality, benchmark regressions, support claims, release notes, runbooks, and rollback artifacts.

  Security and safety requirements

  * Use isolated release-candidate environments, synthetic data/identities/destinations, and no production credentials.
  * Run dependency, license, secret, artifact-integrity, hostile input, plugin isolation, and authorization-policy gates.
  * Protect and sanitize retained databases, diagnostics, traces, content samples, and crash evidence.
  * Block release on unapproved skips, cleanup leaks, missing rollback evidence, unsupported platform claims, or unresolved high-risk defects.
  * Require two-person review for release evidence and any exception to a mandatory security/recovery gate.

  Edge cases and outliers to handle

  * Upgrade succeeds but old code cannot read the new schema for rollback.
  * Restore works only to a different filesystem or host capability set.
  * Soak reveals backlog/leak only after ordinary CI timeout.
  * A release candidate changes plugin/config/event/checkpoint compatibility unexpectedly.
  * Failure injection corrupts the qualification environment before evidence is collected.

  Acceptance criteria (“done” definition)

  * All mandatory native support lanes complete clean-install, upgrade, workload, failure, recovery, diagnostics, and teardown gates with no unapproved skip.
  * Backup/restore and approved rollback or forward-fix procedures are executed from retained artifacts and meet measured recovery objectives.
  * Soak/benchmark results name workload/environment/raw metrics and show no unaccepted semantic, resource, backlog, or cleanup regression.
  * The release evidence bundle contains package/SBOM/provenance hashes, test/fault/security/compatibility/performance results, limitations, approvals, and rollback artifacts.

  Testing plan

  * Clean package install and entry-point smoke tests.
  * Predecessor upgrade/migration/mixed-version/rollback tests.
  * Backup/restore/corruption/failback disaster drills.
  * Sustained concurrent workload and leak/backlog soak tests.
  * Process/host/disk/service/source/plugin/event/publication fault tests.
  * Security, secret, dependency, license, artifact-integrity, and hostile-input gates.
  * Health/status/diagnostic/operator-procedure tests.
  * Release evidence manifest and independent revalidation.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T24.1.1/T24.1.4 approve support lanes, workload profiles, and repository-native qualification commands`; retain every resolved command.
  * Expected evidence: all mandatory install, migration, compatibility, soak, fault, security, recovery, diagnostics, rollback, and manifest gates pass with no unapproved skip.
  * Completion record: release candidate hashes, environment/lane/workload versions, commands/results, raw metrics, migrations/backups/restores, fault/recovery evidence, exceptions, approvals, and rollback package.

  Debugging checklist

  * Identify the first failed entry/exit gate and retain the entire environment/evidence manifest.
  * Separate product, packaging, migration, environment, workload, dependency, and harness failures.
  * Reproduce with the smallest predecessor state and workload that preserves the issue.
  * Do not clean failed qualification environments until sanitized evidence and rollback implications are captured.
