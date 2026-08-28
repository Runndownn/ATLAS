@BinReaper Production TODOs

## TODO

* [ ] TODO 94: Add state-machine, migration, crash, adversarial, compatibility, and fuzz gates

  1.2 source task(s): `T24.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T5.1.4, T11.1.4, T18.1.4, T22.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `.github/workflows/verification.yml (create); tests/property/ (create); tests/fuzz/ (create); tests/fixtures/adversarial/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Integrate the non-happy-path test families required to prove lifecycle truth, recovery, hostile-input handling, and stored/public contract evolution.
  * Restore or protect this invariant: Each major lifecycle/safety/recovery contract has an assigned mandatory test family and CI job.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28.

  Where this applies

  * Primary affected components: `.github/workflows/verification.yml` (create: Run advanced deterministic, fault, adversarial, and compatibility suites.); `tests/property/` (create: Host state, identity, archive, event, and idempotency property tests.); `tests/fuzz/` (create: Host parsers/protocol/archive/config/event/API fuzz harnesses.); `tests/fixtures/adversarial/` (create: Version synthetic malformed and resource-exhaustion fixtures with provenance.)
  * Epic boundary: Continuous quality, packaging, benchmarks, and release evidence — Make every release claim traceable to clean builds, mandatory test families, security and compatibility evidence, representative benchmarks, and a practiced rollback.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.
  * Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-024 requires: Current CI is test-only on Ubuntu/Python 3.13 and does not prove migration, packaging, security, compatibility, recovery, or performance.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Integrate the non-happy-path test families required to prove lifecycle truth, recovery, hostile-input handling, and stored/public contract evolution.
  * Component dispositions: `.github/workflows/verification.yml` (create: Run advanced deterministic, fault, adversarial, and compatibility suites.); `tests/property/` (create: Host state, identity, archive, event, and idempotency property tests.); `tests/fuzz/` (create: Host parsers/protocol/archive/config/event/API fuzz harnesses.); `tests/fixtures/adversarial/` (create: Version synthetic malformed and resource-exhaustion fixtures with provenance.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Run state-machine/model, property, migration forward/rollback, crash/restart, replay/idempotency, concurrency, malformed input, archive, plugin isolation, compatibility, and security regression tests.
  * Define fixture schema, origin/license/sensitivity, expected oracle, bounds, deterministic seed, and minimization/retention.
  * Use time/resource limits and quarantine for fuzz/crash jobs; retain minimized regressions.
  * Map every P0/P1 capability to required test jobs and completion evidence.

  Security and safety requirements

  * Use synthetic/sanitized fixtures; exclude real credentials, challenge answers, personal data, and destructive payloads.
  * Treat parser crashes, hangs, resource overruns, invariant violations, and unexpected side effects as findings.
  * Prevent untrusted fuzz corpus from reaching network, host paths, or release credentials.
  * Require approval/expiry for quarantined flaky tests; do not silently skip.

  Edge cases and outliers to handle

  * Nondeterministic race test.
  * Fuzzer finds platform-only issue.
  * Migration rollback is impossible after new writes.
  * Adversarial archive consumes runner storage.

  Acceptance criteria (“done” definition)

  * Each major lifecycle/safety/recovery contract has an assigned mandatory test family and CI job.
  * Regression fixtures are deterministic, licensed/provenanced, bounded, and sanitized.
  * No unapproved skip or flaky quarantine permits release.
  * Failures produce actionable minimized evidence without leaking sensitive input.

  Testing plan

  * CI self-tests and marker selection tests.
  * Fault/crash/replay suite integration.
  * Fuzz harness smoke and corpus regression tests.
  * Fixture provenance/secret scans.
  * Resource-bound/quarantine tests.
  * Coverage mapping validation.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: CI self-tests and marker selection tests., Fault/crash/replay suite integration., Fuzz harness smoke and corpus regression tests., Fixture provenance/secret scans., Resource-bound/quarantine tests., Coverage mapping validation..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T24.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: .github/workflows/verification.yml, tests/property/, tests/fuzz/, tests/fixtures/adversarial/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 95: Produce reproducible packages, SBOMs, provenance, and integrity manifests

  1.2 source task(s): `T24.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T24.1.1, T4.1.4, T23.1.2`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `pyproject.toml (extend); scripts/build_release.py (create); .github/workflows/release.yml (create); SECURITY.md (create); CONTRIBUTING.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Build and verify ATLAS from a clean pinned environment and publish artifacts with dependency/license inventory, provenance, checksums, and smoke evidence.
  * Restore or protect this invariant: Clean wheel/sdist install and smoke tests pass with recorded tool/dependency versions.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28.

  Where this applies

  * Primary affected components: `pyproject.toml` (extend: Finalize package metadata, dependencies/extras, build backend, included data, and entry points.); `scripts/build_release.py` (create: Build clean artifacts, normalize/compare, hash, and assemble evidence.); `.github/workflows/release.yml` (create: Run protected build, attest, sign if policy chooses, and stage artifacts.); `SECURITY.md` (create: Document supported versions, reporting, dependency response, and artifact verification.); `CONTRIBUTING.md` (create: Document deterministic development, testing, and change evidence.)
  * Epic boundary: Continuous quality, packaging, benchmarks, and release evidence — Make every release claim traceable to clean builds, mandatory test families, security and compatibility evidence, representative benchmarks, and a practiced rollback.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.
  * Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-024 requires: Current CI is test-only on Ubuntu/Python 3.13 and does not prove migration, packaging, security, compatibility, recovery, or performance.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Build and verify ATLAS from a clean pinned environment and publish artifacts with dependency/license inventory, provenance, checksums, and smoke evidence.
  * Component dispositions: `pyproject.toml` (extend: Finalize package metadata, dependencies/extras, build backend, included data, and entry points.); `scripts/build_release.py` (create: Build clean artifacts, normalize/compare, hash, and assemble evidence.); `.github/workflows/release.yml` (create: Run protected build, attest, sign if policy chooses, and stage artifacts.); `SECURITY.md` (create: Document supported versions, reporting, dependency response, and artifact verification.); `CONTRIBUTING.md` (create: Document deterministic development, testing, and change evidence.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define lock/pin strategy for runtime, build, dev, and optional extras and verify dependency resolution from a clean environment.
  * Build sdist/wheel at least twice in isolated clean environments and compare normalized outputs/hashes; explain unavoidable variance.
  * Generate SBOM, license inventory, package/source provenance, dependency/advisory report, checksums, and optional signatures/attestations under explicit policy.
  * Install wheel into a clean environment and run CLI/Python/schema/migration/smoke end-to-end checks.

  Security and safety requirements

  * Use protected least-privilege publishing credentials with environment approval and never expose them to pull-request code.
  * Pin/review build actions/tools and verify downloaded build dependencies where practical.
  * Scan source, artifacts, metadata, examples, fixtures, and diagnostic outputs for secrets.
  * Fail on unexpected files, executable content, license conflict, hash mismatch, or provenance gap.

  Edge cases and outliers to handle

  * Build timestamp/path causes nondeterminism.
  * Optional extra has vulnerable/incompatible dependency.
  * Artifact upload succeeds but provenance/signature fails.
  * Rollback requires an older schema/runtime pair.

  Acceptance criteria (“done” definition)

  * Clean wheel/sdist install and smoke tests pass with recorded tool/dependency versions.
  * Release bundle includes hashes, SBOM, license, provenance, security/dependency report, and coverage limitations.
  * Reproducibility comparison is automated and any variance is documented and bounded.
  * Publishing cannot proceed if integrity/provenance or mandatory tests fail.

  Testing plan

  * Build twice/hash comparison tests.
  * Clean install/entry-point smoke tests.
  * Package-content allowlist tests.
  * SBOM/license/advisory validation.
  * Secret scan tests.
  * Protected release dry-run and rollback artifact tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Build twice/hash comparison tests., Clean install/entry-point smoke tests., Package-content allowlist tests., SBOM/license/advisory validation., Secret scan tests., Protected release dry-run and rollback artifact tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T24.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: pyproject.toml, scripts/build_release.py, .github/workflows/release.yml, SECURITY.md, CONTRIBUTING.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 96: Build representative benchmarks, soak tests, and release rollback evidence

  1.2 source task(s): `T24.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T24.1.2, T24.1.3, T23.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `benchmarks/ (create); tests/soak/ (create); scripts/release_evidence.py (create); docs/operations/release-and-rollback.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Measure defined workloads and retain raw environment-aware evidence for performance, resource, contention, recovery-time, and rollout/rollback decisions.
  * Restore or protect this invariant: Every performance claim names workload, environment, metric, raw evidence, and confidence/limitation.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28.

  Where this applies

  * Primary affected components: `benchmarks/` (create: Provide versioned workload generators, runners, schemas, and baselines.); `tests/soak/` (create: Exercise long-running concurrent jobs, retries, events, storage, and cleanup.); `scripts/release_evidence.py` (create: Assemble test/benchmark/migration/security/rollback reports and hashes.); `docs/operations/release-and-rollback.md` (create: Define progressive rollout, schema backup, compatibility, rollback, and evidence.)
  * Epic boundary: Continuous quality, packaging, benchmarks, and release evidence — Make every release claim traceable to clean builds, mandatory test families, security and compatibility evidence, representative benchmarks, and a practiced rollback.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.
  * Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-024 requires: Current CI is test-only on Ubuntu/Python 3.13 and does not prove migration, packaging, security, compatibility, recovery, or performance.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Measure defined workloads and retain raw environment-aware evidence for performance, resource, contention, recovery-time, and rollout/rollback decisions.
  * Component dispositions: `benchmarks/` (create: Provide versioned workload generators, runners, schemas, and baselines.); `tests/soak/` (create: Exercise long-running concurrent jobs, retries, events, storage, and cleanup.); `scripts/release_evidence.py` (create: Assemble test/benchmark/migration/security/rollback reports and hashes.); `docs/operations/release-and-rollback.md` (create: Define progressive rollout, schema backup, compatibility, rollback, and evidence.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Benchmark thousands of small files, millions of entries, multi-gigabyte files, large/deep archives, duplicate-heavy reruns, concurrent jobs, expensive analyzers, subprocesses, and later adapters.
  * Record hardware/OS/filesystem/Python/config/schema/plugin/fixture versions, warm/cold cache, repetitions, raw samples, confidence/noise, and failures.
  * Measure throughput, latency, CPU, memory, I/O, database lock time, temp/storage, event volume/backlog, recovery time, dedup/reuse, and operator interventions.
  * Define regression comparison and scale-adapter trigger reports without inventing arbitrary universal thresholds.
  * Practice application/schema/content backup and rollback on a release candidate and retain the signed-off evidence bundle.

  Security and safety requirements

  * Use synthetic data and isolated roots; do not benchmark against untrusted production sources or destinations.
  * Bound archive/subprocess/remote fixtures so a benchmark cannot exhaust shared infrastructure.
  * Protect benchmark integrity from result cherry-picking by retaining raw data and failed runs.
  * Rollback drill must not weaken unknown-outcome, provenance, or migration safeguards.

  Edge cases and outliers to handle

  * Noisy shared runner.
  * Benchmark optimization changes semantics.
  * Long soak exposes disk growth/outbox backlog.
  * Rollback binary cannot read post-migration data.

  Acceptance criteria (“done” definition)

  * Every performance claim names workload, environment, metric, raw evidence, and confidence/limitation.
  * Semantic and integrity tests run alongside benchmark optimizations.
  * Release bundle contains mandatory test reports, benchmark raw data, migration/restore/rollback evidence, hashes, and operator notes.
  * A failed mandatory gate or rollback drill blocks release.

  Testing plan

  * Benchmark determinism/schema tests.
  * Representative workload smoke/regression tests.
  * Soak/leak/backlog tests.
  * Semantic equivalence during optimization tests.
  * Backup/restore/rollback drill tests.
  * Release evidence manifest/hash verification.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Benchmark determinism/schema tests., Representative workload smoke/regression tests., Soak/leak/backlog tests., Semantic equivalence during optimization tests., Backup/restore/rollback drill tests., Release evidence manifest/hash verification..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T24.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: benchmarks/, tests/soak/, scripts/release_evidence.py, docs/operations/release-and-rollback.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
