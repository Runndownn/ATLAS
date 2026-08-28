@BinReaper Production TODOs

## TODO

* [ ] TODO 7: Add adversarial source, archive, analyzer, and control baselines

  1.2 source task(s): `T2.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T2.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/characterization/test_adversarial_baseline.py (create); tests/fixtures/v0_1/adversarial/ (create); tests/characterization/faults.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Capture current behavior for source mutation, symlink/path cases, nested archives, event-store faults, process-local controls, and finding truncation before hardening changes.
  * Restore or protect this invariant: Every high-risk path has a reproducible current-state outcome or explicit capability-limited investigation.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14.

  Where this applies

  * Primary affected components: `tests/characterization/test_adversarial_baseline.py` (create: Exercise hostile and faulted inputs deterministically.); `tests/fixtures/v0_1/adversarial/` (create: Store bounded path, archive, mutation, and analyzer fixtures.); `tests/characterization/faults.py` (create: Inject persistence, event, and process interruption faults.)
  * Epic boundary: Deterministic current-behavior characterization — Create executable evidence for every consequential current defect and compatibility surface before production behavior changes.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]
  * Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-001 requires: Pin the observable defects and compatibility surfaces before refactoring so corrections do not erase evidence or silently change unrelated behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Capture current behavior for source mutation, symlink/path cases, nested archives, event-store faults, process-local controls, and finding truncation before hardening changes.
  * Component dispositions: `tests/characterization/test_adversarial_baseline.py` (create: Exercise hostile and faulted inputs deterministically.); `tests/fixtures/v0_1/adversarial/` (create: Store bounded path, archive, mutation, and analyzer fixtures.); `tests/characterization/faults.py` (create: Inject persistence, event, and process interruption faults.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Create source-mutation cases between Reconnaissance and Fingerprinting, including replacement, rename, truncation, and symlink swap where supported.
  * Create archive fixtures for traversal, absolute names, links, devices, nested depth, compression ratio, declared/actual byte mismatch, and partial extraction.
  * Create analyzer fixtures emitting 0, 1, 50, 51, conflicting, malformed, and oversized findings.
  * Characterize pause/resume/cancel from the owning process and from a second process, plus event-store full/failure behavior.

  Security and safety requirements

  * Archive and analyzer fixtures must be inert and bounded; do not include executable malware or destructive payloads.
  * Race cases use controlled barriers rather than timing-only loops whenever possible.
  * Platform-specific skips require a capability probe and retained reason.
  * Fault injection must not target operator files or shared databases.

  Edge cases and outliers to handle

  * A race cannot be deterministically triggered on a runner.
  * Archive libraries normalize malformed names differently by platform.
  * Analyzer output ordering changes across runs.
  * A process interruption leaves locked test files or an unclosed database.

  Acceptance criteria (“done” definition)

  * Every high-risk path has a reproducible current-state outcome or explicit capability-limited investigation.
  * The >50 finding case proves whether authoritative data is truncated or only summarized.
  * Source mutation and second-process control behavior are recorded with exact state/effect boundaries.
  * All adversarial fixtures stay within declared byte, time, and file-count limits.

  Testing plan

  * Barrier-controlled TOCTOU tests.
  * Adversarial archive corpus tests.
  * Malformed analyzer-output tests.
  * Second-process control integration tests.
  * Event-store and disk-fault injection tests.
  * Resource-bound and cleanup verification.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Barrier-controlled TOCTOU tests., Adversarial archive corpus tests., Malformed analyzer-output tests., Second-process control integration tests., Event-store and disk-fault injection tests., Resource-bound and cleanup verification..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T2.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/characterization/test_adversarial_baseline.py, tests/fixtures/v0_1/adversarial/, tests/characterization/faults.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 8: Integrate characterization evidence into CI and correction gates

  1.2 source task(s): `T2.1.4`
  Priority: `P0`
  Estimated effort: `10 hours`
  Dependencies: `T2.1.2, T2.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `.github/workflows/tests.yml (extend); tests/characterization/README.md (create); planning/characterization-baseline.json (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make the baseline an enforceable precondition for every P0 correction, with retained evidence and explicit updates when target behavior changes.
  * Restore or protect this invariant: Characterization jobs are mandatory for P0 changes and fail on unapproved skips.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14.

  Where this applies

  * Primary affected components: `.github/workflows/tests.yml` (extend: Run characterization and retain failure artifacts.); `tests/characterization/README.md` (create: Document fixture lifecycle and correction workflow.); `planning/characterization-baseline.json` (create: Record baseline hashes and correction ownership.)
  * Epic boundary: Deterministic current-behavior characterization — Create executable evidence for every consequential current defect and compatibility surface before production behavior changes.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]
  * Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-001 requires: Pin the observable defects and compatibility surfaces before refactoring so corrections do not erase evidence or silently change unrelated behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Make the baseline an enforceable precondition for every P0 correction, with retained evidence and explicit updates when target behavior changes.
  * Component dispositions: `.github/workflows/tests.yml` (extend: Run characterization and retain failure artifacts.); `tests/characterization/README.md` (create: Document fixture lifecycle and correction workflow.); `planning/characterization-baseline.json` (create: Record baseline hashes and correction ownership.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Add CI jobs for characterization, deterministic reruns, artifact retention, and platform capability reporting.
  * Require each P0 implementation PR to reference the failing/current fixture and update only its target expectation after the correction lands.
  * Publish JUnit/JSON reports, normalized event traces, database snapshots, and filesystem manifests on failure.
  * Add a gate that rejects vacuous assertions, unapproved skips, or fixtures lacking cleanup/provenance metadata.

  Security and safety requirements

  * Retention artifacts must be redacted and size-limited.
  * CI permissions remain read-only except required artifact upload.
  * A failed evidence upload cannot convert a failing test into success.
  * Unapproved platform skips block release rather than silently reducing coverage.

  Edge cases and outliers to handle

  * Artifact storage outage.
  * A baseline test is flaky only on one supported OS.
  * A correction intentionally changes multiple related expectations.
  * A known defect remains unresolved for a compatibility window.

  Acceptance criteria (“done” definition)

  * Characterization jobs are mandatory for P0 changes and fail on unapproved skips.
  * Failure artifacts include all required evidence without secrets or unbounded payloads.
  * Every expectation change links to its implementation task and reviewer decision.
  * Three-run determinism is checked in CI or an equivalent reproducible gate.

  Testing plan

  * CI workflow syntax and least-privilege tests.
  * Artifact-retention integration test.
  * Skip-policy negative tests.
  * Vacuous-assertion lint or review gate.
  * Baseline hash comparison test.
  * Manual dry-run of one known-defect-to-correction transition.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: CI workflow syntax and least-privilege tests., Artifact-retention integration test., Skip-policy negative tests., Vacuous-assertion lint or review gate., Baseline hash comparison test., Manual dry-run of one known-defect-to-correction transition..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T2.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: .github/workflows/tests.yml, tests/characterization/README.md, planning/characterization-baseline.json.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 9: Define `PipelineDefinitionV1`, canonical phase slots, and one failure policy

  1.2 source task(s): `T3.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T2.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/config/models.py::PipelineDefinitionV1 (create); atlas/core/orchestrator.py::PipelineConfig (refactor); atlas/models/states.py::FailurePolicy (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace arbitrary phase lists and overlapping continue/abort flags with a versioned definition whose six semantic slots always remain ordered and whose terminal behavior is predictable.
  * Restore or protect this invariant: Every accepted definition contains A-F exactly once in canonical order.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34.

  Where this applies

  * Primary affected components: `atlas/config/models.py::PipelineDefinitionV1` (create: Own the versioned pipeline contract.); `atlas/core/orchestrator.py::PipelineConfig` (refactor: Retain only as a compatibility facade.); `atlas/models/states.py::FailurePolicy` (create: Provide one authoritative error-policy enum.)
  * Epic boundary: Versioned pipeline semantics and configuration — Make the six lifecycle slots, failure policy, typed phase configuration, and canonical configuration digest one deterministic contract across CLI, Python, tests, and future services.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]
  * Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-002 requires: The current caller-controlled phase list and overlapping failure flags permit extraction-before-structure and ambiguous terminal truth.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace arbitrary phase lists and overlapping continue/abort flags with a versioned definition whose six semantic slots always remain ordered and whose terminal behavior is predictable.
  * Component dispositions: `atlas/config/models.py::PipelineDefinitionV1` (create: Own the versioned pipeline contract.); `atlas/core/orchestrator.py::PipelineConfig` (refactor: Retain only as a compatibility facade.); `atlas/models/states.py::FailurePolicy` (create: Provide one authoritative error-policy enum.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Model schema version, pipeline name, source reference, metadata, six named phase policies, and one `FailurePolicy`.
  * Represent disabled or inapplicable work as validated phase policy that yields durable `SKIPPED`, never by deleting or reordering a slot.
  * Define required/optional semantics and legal failure propagation for each phase slot.
  * Publish canonical JSON schema and examples for valid, invalid, skipped, and optional-phase pipelines.

  Security and safety requirements

  * Reject configurations that attempt extraction before structural discovery or promotion before analysis/evidence.
  * Do not allow configuration to grant undeclared filesystem, network, subprocess, or publication authority.
  * Keep unknown schema versions and contradictory failure settings fail-closed.
  * Record normalized configuration without secrets.

  Edge cases and outliers to handle

  * Duplicate phase declarations, omitted required phase, duplicate YAML keys, unknown schema version.
  * All phases disabled, optional phase failure, required phase failure under collect policy.
  * Legacy names with case or Unicode variants.
  * Future phase extensions that must not alter A-F meaning.

  Acceptance criteria (“done” definition)

  * Every accepted definition contains A-F exactly once in canonical order.
  * Contradictory legacy failure flags are rejected before job creation.
  * Disabled phases produce an explicit policy and eventual durable `SKIPPED` reason.
  * The JSON schema and Python model agree on all required fields and enums.

  Testing plan

  * Model unit tests for every valid state.
  * Permutation/property tests rejecting reordering and duplicates.
  * Failure-policy truth-table tests.
  * Schema/Python differential tests.
  * Unknown-version and duplicate-key negative tests.
  * Public import compatibility tests for `PipelineConfig`.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Model unit tests for every valid state., Permutation/property tests rejecting reordering and duplicates., Failure-policy truth-table tests., Schema/Python differential tests., Unknown-version and duplicate-key negative tests., Public import compatibility tests for `PipelineConfig`..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T3.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/config/models.py::PipelineDefinitionV1, atlas/core/orchestrator.py::PipelineConfig, atlas/models/states.py::FailurePolicy.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
