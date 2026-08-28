@BinReaper Production TODOs

## TODO

* [ ] TODO 10: Implement deterministic safe loading, merge order, and canonical digests

  1.2 source task(s): `T3.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T3.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/config/loader.py::ConfigurationResolver (create); examples/*.yaml (migrate); atlas/cli.py::pipeline preflight (extend)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create one resolver that safely parses pipeline YAML/JSON, applies deterministic overrides, validates typed values, and computes a stable secret-free configuration digest.
  * Restore or protect this invariant: Equivalent normalized configurations produce identical digests across runs.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34.

  Where this applies

  * Primary affected components: `atlas/config/loader.py::ConfigurationResolver` (create: Own parsing, merging, validation, and canonicalization.); `examples/*.yaml` (migrate: Add schema version and typed phase sections.); `atlas/cli.py::pipeline preflight` (extend: Validate before job creation.)
  * Epic boundary: Versioned pipeline semantics and configuration — Make the six lifecycle slots, failure policy, typed phase configuration, and canonical configuration digest one deterministic contract across CLI, Python, tests, and future services.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]
  * Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-002 requires: The current caller-controlled phase list and overlapping failure flags permit extraction-before-structure and ambiguous terminal truth.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create one resolver that safely parses pipeline YAML/JSON, applies deterministic overrides, validates typed values, and computes a stable secret-free configuration digest.
  * Component dispositions: `atlas/config/loader.py::ConfigurationResolver` (create: Own parsing, merging, validation, and canonicalization.); `examples/*.yaml` (migrate: Add schema version and typed phase sections.); `atlas/cli.py::pipeline preflight` (extend: Validate before job creation.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Use a safe loader with duplicate-key rejection, bounded aliases, and source-location diagnostics.
  * Define merge precedence for defaults, file, environment, and explicit CLI values; reject ambiguous or wrong-typed overrides.
  * Validate every phase-specific field against a consumer-owned typed model and reject accepted-but-unused keys.
  * Canonicalize normalized data, redact/resolve secret references, and compute a stable digest persisted with the job.

  Security and safety requirements

  * Never embed secret values in the digest input, logs, events, or migration output.
  * Reject YAML tags, object construction, alias bombs, duplicate keys, and oversized documents.
  * Configuration cannot loosen registered source roots or platform safety controls beyond policy-authorized bounds.
  * Environment override names and values are treated as untrusted input.

  Edge cases and outliers to handle

  * Equivalent YAML formatting produces the same digest.
  * Environment value is empty, malformed, duplicated, or conflicts with CLI value.
  * Deprecated keys coexist with new keys.
  * Secret reference cannot resolve during preflight.

  Acceptance criteria (“done” definition)

  * Equivalent normalized configurations produce identical digests across runs.
  * Every accepted phase key is consumed by a typed model.
  * Invalid configuration creates no job row, workspace, or outbox event.
  * Diagnostics identify source path, key, expected type, and stable error code without exposing secrets.

  Testing plan

  * Parser unit and fuzz tests.
  * Duplicate-key, alias-bomb, and unsafe-tag negative tests.
  * Merge-precedence table tests.
  * Digest determinism/property tests.
  * Secret-redaction tests.
  * CLI preflight integration tests over every example file.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Parser unit and fuzz tests., Duplicate-key, alias-bomb, and unsafe-tag negative tests., Merge-precedence table tests., Digest determinism/property tests., Secret-redaction tests., CLI preflight integration tests over every example file..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T3.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/config/loader.py::ConfigurationResolver, examples/*.yaml, atlas/cli.py::pipeline preflight.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 11: Create typed configuration contracts for all six built-in phases

  1.2 source task(s): `T3.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T3.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/config/phases.py (create); atlas/phases/base.py::PhaseContext (extend); atlas/phases/* (refactor)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace opaque metadata dictionaries with phase-owned configuration models that define defaults, limits, capability requirements, and validation for each A-F stage.
  * Restore or protect this invariant: Every built-in phase receives only its typed configuration object.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34.

  Where this applies

  * Primary affected components: `atlas/config/phases.py` (create: Own Recon through Review typed configuration models.); `atlas/phases/base.py::PhaseContext` (extend: Expose validated phase configuration only.); `atlas/phases/*` (refactor: Consume typed settings instead of unstructured metadata.)
  * Epic boundary: Versioned pipeline semantics and configuration — Make the six lifecycle slots, failure policy, typed phase configuration, and canonical configuration digest one deterministic contract across CLI, Python, tests, and future services.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]
  * Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-002 requires: The current caller-controlled phase list and overlapping failure flags permit extraction-before-structure and ambiguous terminal truth.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace opaque metadata dictionaries with phase-owned configuration models that define defaults, limits, capability requirements, and validation for each A-F stage.
  * Component dispositions: `atlas/config/phases.py` (create: Own Recon through Review typed configuration models.); `atlas/phases/base.py::PhaseContext` (extend: Expose validated phase configuration only.); `atlas/phases/*` (refactor: Consume typed settings instead of unstructured metadata.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define Recon traversal depth/exclusions/budgets; Fingerprint algorithms/chunk/capture mode; Structure inspectors/budgets; Extraction policy/workspace limits; Analysis plugin selection/resources; Review/publication policy references.
  * Assign one owner and default rationale to every field and mark deployment-policy fields separately from mechanism fields.
  * Reject fields unsupported by the selected platform, plugin, or backend before execution.
  * Expose versioned serialization and upgrade hooks for each phase config.

  Security and safety requirements

  * Safety ceilings have conservative defaults and cannot be silently disabled by omission.
  * Plugin and execution capability requests are validated against policy, not trusted because they appear in configuration.
  * Paths remain source-relative or registered destination references; no arbitrary path injection.
  * Active-content execution flags are explicit and default denied.

  Edge cases and outliers to handle

  * Plugin requests a resource or network capability absent from the phase config.
  * Phase config version is newer than runtime.
  * Legacy free-form keys collide with typed fields.
  * Platform cannot enforce a requested limit.

  Acceptance criteria (“done” definition)

  * Every built-in phase receives only its typed configuration object.
  * No production phase reads raw `phase_config` dictionaries after migration.
  * Unsupported capability or platform combinations fail before attempt creation.
  * Config schema round-trips preserve semantics and digest.

  Testing plan

  * Per-phase model unit tests.
  * Unknown/missing/wrong-type property tests.
  * Consumer coverage test proving every field is read or intentionally reserved.
  * Platform capability validation tests.
  * Round-trip and version-upgrade tests.
  * Phase integration tests using typed contexts.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Per-phase model unit tests., Unknown/missing/wrong-type property tests., Consumer coverage test proving every field is read or intentionally reserved., Platform capability validation tests., Round-trip and version-upgrade tests., Phase integration tests using typed contexts..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T3.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/config/phases.py, atlas/phases/base.py::PhaseContext, atlas/phases/*.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 12: Add legacy pipeline migration, dual support, and deprecation telemetry

  1.2 source task(s): `T3.1.4`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T3.1.2, T3.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/config/legacy.py::LegacyPipelineLoader (create); atlas/cli.py::pipeline migrate (extend); docs/migrations/pipeline-v1.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Preserve current YAML, CLI syntax, and imports through an explicit compatibility window while making new definitions canonical and observable.
  * Restore or protect this invariant: All existing examples either migrate to an approved digest or fail with a documented reason.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34.

  Where this applies

  * Primary affected components: `atlas/config/legacy.py::LegacyPipelineLoader` (create: Normalize supported v0.1 inputs without guessing.); `atlas/cli.py::pipeline migrate` (extend: Provide dry-run conversion and diagnostics.); `docs/migrations/pipeline-v1.md` (create: Document compatibility window, rollback, and deprecation.)
  * Epic boundary: Versioned pipeline semantics and configuration — Make the six lifecycle slots, failure policy, typed phase configuration, and canonical configuration digest one deterministic contract across CLI, Python, tests, and future services.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-002: Introduce a versioned PipelineDefinition and enforce canonical A–F semantics; evidence: GAP-002, GAP-003, REQ-001, REQ-002, REQ-006, REQ-007; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L25-L68,L128-L220]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/cli.py:L42-L91]
  * Canonical proposed files/interfaces: Create `atlas/config/models.py`, `atlas/config/loader.py`; refactor `atlas/cli.py`, `atlas/core/orchestrator.py`; update `examples/*.yaml`; compatibility shim for `PipelineConfig`. / `PipelineDefinitionV1`; `FailurePolicy={FAIL_REQUIRED_PHASE, CONTINUE_OPTIONAL_PHASE, COLLECT_FAILURES}` or an equivalent minimal enum; `LegacyPipelineLoader` normalizes unversioned YAML without changing public CLI syntax.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-002 requires: The current caller-controlled phase list and overlapping failure flags permit extraction-before-structure and ambiguous terminal truth.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Preserve current YAML, CLI syntax, and imports through an explicit compatibility window while making new definitions canonical and observable.
  * Component dispositions: `atlas/config/legacy.py::LegacyPipelineLoader` (create: Normalize supported v0.1 inputs without guessing.); `atlas/cli.py::pipeline migrate` (extend: Provide dry-run conversion and diagnostics.); `docs/migrations/pipeline-v1.md` (create: Document compatibility window, rollback, and deprecation.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Inventory legacy keys, examples, CLI arguments, public imports, and conflicting error-policy combinations.
  * Implement read-old/write-new normalization with warnings and a deterministic converted definition.
  * Provide a dry-run migration command that emits a diff, target digest, unsupported keys, and rollback instructions.
  * Add deprecation counters/events and a version-detection matrix; do not remove legacy support until usage and tests permit.

  Security and safety requirements

  * Never silently choose between contradictory `continue_on_phase_error` and `abort_on_error` settings.
  * Migration output excludes secret values and preserves comments only when safe and deterministic.
  * Unsupported legacy semantics block migration with actionable errors.
  * Deprecated input cannot bypass new capability or phase-order validation.

  Edge cases and outliers to handle

  * Unversioned file with only defaults.
  * Both legacy failure flags set in inconsistent combinations.
  * Unknown phase name or obsolete plugin configuration.
  * Rollback reads a new stored definition with an older binary.

  Acceptance criteria (“done” definition)

  * All existing examples either migrate to an approved digest or fail with a documented reason.
  * Legacy and migrated definitions produce equivalent intended lifecycle behavior for supported cases.
  * Deprecation telemetry reports use without logging sensitive configuration.
  * Removal criteria and compatibility window are documented and testable.

  Testing plan

  * Golden migration fixtures for every legacy example.
  * Behavior-equivalence integration tests.
  * Contradictory-flag negative tests.
  * CLI dry-run and exit-code tests.
  * Deprecation telemetry/redaction tests.
  * Rollback/version-skew compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Golden migration fixtures for every legacy example., Behavior-equivalence integration tests., Contradictory-flag negative tests., CLI dry-run and exit-code tests., Deprecation telemetry/redaction tests., Rollback/version-skew compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T3.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/config/legacy.py::LegacyPipelineLoader, atlas/cli.py::pipeline migrate, docs/migrations/pipeline-v1.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
