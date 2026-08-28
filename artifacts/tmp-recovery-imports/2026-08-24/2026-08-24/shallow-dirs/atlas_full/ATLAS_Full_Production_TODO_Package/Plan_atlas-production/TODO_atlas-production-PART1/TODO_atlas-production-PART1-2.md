@BinReaper Production TODOs

## TODO

* [ ] TODO 4: Publish the canonical component-ownership and scope boundary matrix

  1.2 source task(s): `T1.1.4`
  Priority: `P0`
  Estimated effort: `10 hours`
  Dependencies: `T1.1.1, T1.1.2, T1.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `ATLAS_Evidence_Driven_Architecture_Blueprint.md sections 8-17 (reuse); Pasted markdown (2).md Stages 1-5 (reuse); docs/architecture/component-responsibility-matrix.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Reconcile the latest architecture with the earlier deep-review helper candidates, assigning one owner to each authoritative state and rejecting unnecessary micro-components or generic workflow expansion.
  * Restore or protect this invariant: Every authoritative record and transition has exactly one named owner.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze.

  Where this applies

  * Primary affected components: `ATLAS_Evidence_Driven_Architecture_Blueprint.md sections 8-17` (reuse: Use the latest target architecture as the decision authority.); `Pasted markdown (2).md Stages 1-5` (reuse: Use helper candidates as questions, not as implementation facts.); `docs/architecture/component-responsibility-matrix.md` (create: Record final component classifications, state ownership, and prohibited authority crossings.)
  * Epic boundary: Evidence, baseline, and authority reconciliation — Replace the prior assessment limitations with a reproducible implementation baseline while preserving the supplied ZIP as the canonical planning truth.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Evidence, baseline, and authority reconciliation.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Reconcile the latest architecture with the earlier deep-review helper candidates, assigning one owner to each authoritative state and rejecting unnecessary micro-components or generic workflow expansion.
  * Component dispositions: `ATLAS_Evidence_Driven_Architecture_Blueprint.md sections 8-17` (reuse: Use the latest target architecture as the decision authority.); `Pasted markdown (2).md Stages 1-5` (reuse: Use helper candidates as questions, not as implementation facts.); `docs/architecture/component-responsibility-matrix.md` (create: Record final component classifications, state ownership, and prohibited authority crossings.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Classify every candidate helper as REQUIRED CORE, USEFUL CORE, ADAPTER, PLUGIN, LATER, or UNNECESSARY.
  * Map one authoritative owner for job, phase, attempt, intake, occurrence, content, structure, extraction, finding, evidence, decision, publication, checkpoint, event history, transport, budget, and configuration state.
  * Combine cohesive responsibilities such as quarantine into WorkspaceManager and fencing into StateStore/LifecycleCoordinator rather than creating micro-services.
  * Record explicit non-goals: no generic DAG, no alternate lifecycle authority, no mandatory distributed infrastructure, and no model-owned trust transition.

  Security and safety requirements

  * Prevent adapters, workers, plugins, AI, event consumers, and UIs from acquiring direct StateStore mutation authority.
  * Keep source-provider and deployment IAM abstractions deferred until a proven use case exists.
  * Document capability boundaries for all components that touch files, processes, networks, secrets, or publications.
  * Require one canonical write path for every authoritative record.

  Edge cases and outliers to handle

  * Two components both appear to own checkpoint or progress state.
  * A convenience adapter bypasses CommandService or event-outbox semantics.
  * A helper candidate is merely a renamed method with no independent invariant.
  * Future source providers or tenants require a new boundary not supported by current evidence.

  Acceptance criteria (“done” definition)

  * Every authoritative record and transition has exactly one named owner.
  * All helper candidates are classified with rationale and mapped to a task or explicit rejection.
  * The matrix preserves fixed A-F barriers and separates mechanism from deployment policy.
  * The matrix is reviewed before module creation begins.

  Testing plan

  * Responsibility-overlap lint over the matrix.
  * Architecture dependency-cycle review.
  * Trust-boundary walkthrough from source registration to publication.
  * Negative design review for direct StateStore access from plugins/adapters.
  * Traceability check from every proposed module to a requirement or verified gap.
  * Review for unnecessary abstractions and generic scheduler drift.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Responsibility-overlap lint over the matrix., Architecture dependency-cycle review., Trust-boundary walkthrough from source registration to publication., Negative design review for direct StateStore access from plugins/adapters., Traceability check from every proposed module to a requirement or verified gap., Review for unnecessary abstractions and generic scheduler drift..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T1.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: ATLAS_Evidence_Driven_Architecture_Blueprint.md sections 8-17, Pasted markdown (2).md Stages 1-5, docs/architecture/component-responsibility-matrix.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 5: Define the versioned characterization fixture manifest

  1.2 source task(s): `T2.1.1`
  Priority: `P0`
  Estimated effort: `8 hours`
  Dependencies: `T1.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/characterization/manifest.schema.json (create); tests/fixtures/v0_1/ (create); tests/characterization/conftest.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create the canonical machine-readable fixture schema that separates current observed behavior from target behavior and ties each case to gaps, requirements, setup, cleanup, and evidence artifacts.
  * Restore or protect this invariant: The manifest schema validates all baseline fixtures and rejects missing GAP/REQ lineage.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14.

  Where this applies

  * Primary affected components: `tests/characterization/manifest.schema.json` (create: Define deterministic fixture records and evidence fields.); `tests/fixtures/v0_1/` (create: Store sanitized baseline inputs by version.); `tests/characterization/conftest.py` (create: Provide bounded setup, normalization, and cleanup helpers.)
  * Epic boundary: Deterministic current-behavior characterization — Create executable evidence for every consequential current defect and compatibility surface before production behavior changes.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]
  * Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-001 requires: Pin the observable defects and compatibility surfaces before refactoring so corrections do not erase evidence or silently change unrelated behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create the canonical machine-readable fixture schema that separates current observed behavior from target behavior and ties each case to gaps, requirements, setup, cleanup, and evidence artifacts.
  * Component dispositions: `tests/characterization/manifest.schema.json` (create: Define deterministic fixture records and evidence fields.); `tests/fixtures/v0_1/` (create: Store sanitized baseline inputs by version.); `tests/characterization/conftest.py` (create: Provide bounded setup, normalization, and cleanup helpers.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define fixture fields for source setup, invocation surface, expected current result, expected target result, database assertions, event assertions, filesystem manifest, cleanup, platform capabilities, and related GAP/REQ IDs.
  * Normalize timestamps, temporary roots, UUIDs, and platform-specific metadata without erasing behaviorally significant differences.
  * Create initial fixture metadata for every GAP-001 through GAP-015, marking unresolved runtime evidence explicitly.
  * Document fixture provenance and rules for changing a characterization expectation.

  Security and safety requirements

  * Use synthetic non-secret inputs only; no production artifacts or credentials.
  * Fixture extraction and cleanup must remain under a test-owned temporary root.
  * Do not normalize away path escapes, permission failures, event loss, or other security-significant evidence.
  * A known-bad expectation must be labeled `CURRENT_DEFECT`, never `DESIRED`.

  Edge cases and outliers to handle

  * Unsupported permission semantics on Windows or containerized CI.
  * Tests requiring symlink, mount, or file-descriptor capabilities unavailable on a runner.
  * Expected output contains nondeterministic ordering or platform-specific error text.
  * A fixture partially creates state before setup fails.

  Acceptance criteria (“done” definition)

  * The manifest schema validates all baseline fixtures and rejects missing GAP/REQ lineage.
  * Every GAP-001 through GAP-015 has a fixture or an explicit investigation record.
  * All fixture inputs are sanitized, bounded, and self-contained.
  * Expectation-change policy requires linked correction task and reviewer approval.

  Testing plan

  * JSON schema validation tests.
  * Property tests for normalization idempotency.
  * Negative tests for path escape and unsafe cleanup declarations.
  * Cross-platform fixture capability tests.
  * Fixture provenance and secret-scan tests.
  * Snapshot tests for manifest canonical ordering.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: JSON schema validation tests., Property tests for normalization idempotency., Negative tests for path escape and unsafe cleanup declarations., Cross-platform fixture capability tests., Fixture provenance and secret-scan tests., Snapshot tests for manifest canonical ordering..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T2.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/characterization/manifest.schema.json, tests/fixtures/v0_1/, tests/characterization/conftest.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 6: Characterize CLI, API, persistence, event, and filesystem outcomes

  1.2 source task(s): `T2.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T2.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/characterization/test_cli_api_state.py (create); tests/characterization/evidence_capture.py (create); atlas public CLI/Python API (reuse)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Execute the highest-consequence baseline scenarios through real public entry points and capture exit status, terminal states, rows, event sequences, exceptions, and side effects as machine-readable evidence.
  * Restore or protect this invariant: Every selected scenario records a complete, canonical evidence bundle.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14.

  Where this applies

  * Primary affected components: `tests/characterization/test_cli_api_state.py` (create: Exercise public invocation surfaces and persisted outcomes.); `tests/characterization/evidence_capture.py` (create: Capture normalized database, event, and filesystem evidence.); `atlas public CLI/Python API` (reuse: Characterize without changing production behavior.)
  * Epic boundary: Deterministic current-behavior characterization — Create executable evidence for every consequential current defect and compatibility surface before production behavior changes.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-001: Establish deterministic current-behavior characterization; evidence: GAP-001, GAP-002, GAP-003, GAP-004, GAP-006, GAP-007, GAP-009; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_runtime.py:L18-L144]; [ATLAS-TEST:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:tests/test_orchestrator.py:L103-L111]
  * Canonical proposed files/interfaces: Existing `tests/`; create `tests/characterization/`, versioned fixtures under `tests/fixtures/v0_1/`; no production-file behavior changes in this task. / Versioned fixture manifest: `{fixture_id, requirement_ids, gap_ids, setup, command_or_api, expected_current, expected_target, cleanup}`. No public runtime API change.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-001 requires: Pin the observable defects and compatibility surfaces before refactoring so corrections do not erase evidence or silently change unrelated behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Execute the highest-consequence baseline scenarios through real public entry points and capture exit status, terminal states, rows, event sequences, exceptions, and side effects as machine-readable evidence.
  * Component dispositions: `tests/characterization/test_cli_api_state.py` (create: Exercise public invocation surfaces and persisted outcomes.); `tests/characterization/evidence_capture.py` (create: Capture normalized database, event, and filesystem evidence.); `atlas public CLI/Python API` (reuse: Characterize without changing production behavior.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Exercise missing, non-directory, unreadable, and empty sources through CLI and Python API.
  * Exercise invalid phase permutations, contradictory error flags, missing handlers, and failed phases under non-abort behavior.
  * Capture job/phase state, database rows, emitted events, exception classes, CLI status, and filesystem side effects for each case.
  * Run each case three times and compare normalized evidence hashes.

  Security and safety requirements

  * Run in disposable temporary roots and a disposable SQLite database.
  * Do not invoke network transports or active-content analyzers during baseline characterization.
  * Preserve false-success and partial-write evidence rather than treating it as test-harness failure.
  * Retain logs and DB copies only after redaction and size bounds.

  Edge cases and outliers to handle

  * CLI returns zero while a phase row is failed.
  * A missing source is recorded as an empty successful intake.
  * Event persistence fails after state mutation.
  * Cleanup fails because a test intentionally leaves read-only or locked files.

  Acceptance criteria (“done” definition)

  * Every selected scenario records a complete, canonical evidence bundle.
  * CLI and Python invocation paths are compared for equivalent authoritative outcomes.
  * Three clean runs yield identical normalized evidence hashes.
  * No production source behavior changes are included.

  Testing plan

  * Subprocess CLI integration tests.
  * Public Python API integration tests.
  * SQLite row and transition assertions.
  * Event-sequence assertions.
  * Filesystem manifest and cleanup tests.
  * Determinism comparison across three clean runs.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Subprocess CLI integration tests., Public Python API integration tests., SQLite row and transition assertions., Event-sequence assertions., Filesystem manifest and cleanup tests., Determinism comparison across three clean runs..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T2.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/characterization/test_cli_api_state.py, tests/characterization/evidence_capture.py, atlas public CLI/Python API.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
