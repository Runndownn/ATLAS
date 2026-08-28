@BinReaper Production TODOs

## TODO

* [ ] TODO 52: Add deterministic structure reuse and end-to-end lineage invariants

  1.2 source task(s): `T13.1.4`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T13.1.2, T13.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/reuse.py::StructuralReusePolicy (create); atlas/artifacts/lineage.py (create); tests/lineage/ (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Reuse only declared deterministic structural results under exact operation keys and prove complete source-to-derived lineage, including the full model omitted by simplified diagrams.
  * Restore or protect this invariant: Reuse occurs only on exact key equality and records current use provenance.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/reuse.py::StructuralReusePolicy` (create: Evaluate exact-key report reuse.); `atlas/artifacts/lineage.py` (create: Query SourceRoot through extraction outputs bidirectionally.); `tests/lineage/` (create: Enforce graph invariants and PDF model completeness.)
  * Epic boundary: Structural and extraction lineage contracts — Persist exact-byte structural reports and extraction records whose bindings are verified before materialization and reusable only under exact deterministic keys.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.
  * Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-012 requires: Current structural and extraction phases exchange summaries/live paths rather than durable records bound to exact content.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Reuse only declared deterministic structural results under exact operation keys and prove complete source-to-derived lineage, including the full model omitted by simplified diagrams.
  * Component dispositions: `atlas/artifacts/reuse.py::StructuralReusePolicy` (create: Evaluate exact-key report reuse.); `atlas/artifacts/lineage.py` (create: Query SourceRoot through extraction outputs bidirectionally.); `tests/lineage/` (create: Enforce graph invariants and PDF model completeness.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define reuse key from content identity, inspector/version, config/policy/schema digest, deterministic flag, and relevant capability version.
  * On reuse, append a reuse record tied to the current job/phase attempt rather than copying or mutating the report.
  * Implement lineage queries including SourceRoot, IntakeGeneration, Occurrence, ContentIdentity, StructuralReport, ExtractionRecord, Derivation, and child identity.
  * Add invariant checks for orphan, cyclic, cross-job, missing, or inconsistent edges.

  Security and safety requirements

  * Non-deterministic, partial, unknown, or integrity-incident reports are never reused.
  * Reuse cannot bypass current policy compatibility or source/content validation.
  * Lineage API authorization/redaction is deployment-specific but core records remain immutable.
  * Graph traversal is bounded and paginated.

  Edge cases and outliers to handle

  * Same report reused by many jobs.
  * Inspector version string reused for changed code.
  * Lineage includes identical child content from multiple parents.
  * Simplified external view omits structure/extraction nodes.

  Acceptance criteria (“done” definition)

  * Reuse occurs only on exact key equality and records current use provenance.
  * Every derived content identity traces to at least one valid parent/report/extraction/attempt.
  * Every publication-ready lineage can traverse back to SourceRoot and exact bytes.
  * Graph invariant checks detect all injected orphan/cross-job/cycle cases.

  Testing plan

  * Reuse-key unit/property tests.
  * Deterministic/non-deterministic inspector tests.
  * Bidirectional lineage integration tests.
  * Graph corruption negative tests.
  * High-fanout pagination tests.
  * Version-attribution regression tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Reuse-key unit/property tests., Deterministic/non-deterministic inspector tests., Bidirectional lineage integration tests., Graph corruption negative tests., High-fanout pagination tests., Version-attribution regression tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T13.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/reuse.py::StructuralReusePolicy, atlas/artifacts/lineage.py, tests/lineage/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 53: Define `PluginDescriptor`, `AnalysisContext`, and `AnalysisFinding` schemas

  1.2 source task(s): `T14.1.1`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T3.1.4, T7.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/plugins/contracts.py::PluginDescriptor (create); atlas/plugins/contracts.py::AnalysisContext (create); atlas/plugins/contracts.py::AnalysisFinding (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace arbitrary analyzer dictionaries with versioned descriptors, mediated contexts, normalized finding envelopes, and explicit resource/capability declarations.
  * Restore or protect this invariant: No arbitrary dictionary reaches durable findings.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23.

  Where this applies

  * Primary affected components: `atlas/plugins/contracts.py::PluginDescriptor` (create: Declare identity, compatibility, inputs, outputs, capabilities, and resources.); `atlas/plugins/contracts.py::AnalysisContext` (create: Expose mediated reads, derived outputs, progress, and diagnostics.); `atlas/plugins/contracts.py::AnalysisFinding` (create: Normalize attributed analyzer output.)
  * Epic boundary: Typed plugin contracts, registry, and trust policy — Turn Deep Understanding into a deterministic, versioned capability platform whose plugins emit normalized findings without receiving lifecycle or host authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].
  * Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-013 requires: Arbitrary in-process plugin dictionaries lack schema, version, capability, resource, determinism, and authority boundaries.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace arbitrary analyzer dictionaries with versioned descriptors, mediated contexts, normalized finding envelopes, and explicit resource/capability declarations.
  * Component dispositions: `atlas/plugins/contracts.py::PluginDescriptor` (create: Declare identity, compatibility, inputs, outputs, capabilities, and resources.); `atlas/plugins/contracts.py::AnalysisContext` (create: Expose mediated reads, derived outputs, progress, and diagnostics.); `atlas/plugins/contracts.py::AnalysisFinding` (create: Normalize attributed analyzer output.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define stable plugin ID/version/API range, input content/artifact types, output schema versions, deterministic/cacheable flags, provenance, and supported backends.
  * Declare filesystem read/write, network, subprocess/tool, active-content, CPU, memory, temp, process, and timeout expectations.
  * Define finding category/severity, observation, source/content references, confidence, evidence type, relationships, tool/model version, timestamps, and bounded structured data.
  * Define context methods that cannot access StateStore, source roots, lifecycle transitions, decisions, or publication.

  Security and safety requirements

  * All model/AI text is untrusted data and cannot become a command or approved decision.
  * Finding fields are validated, bounded, and escaped for logs/UI/export.
  * Capabilities default denied and cannot be inferred from plugin code comments.
  * Context-mediated writes create derived artifacts through workspace/content APIs only.

  Edge cases and outliers to handle

  * Plugin returns zero, thousands, conflicting, cyclic, malformed, or oversized findings.
  * Plugin version compatible with API but output schema is not.
  * Active-content parser claims deterministic behavior.
  * Model/provider version or prompt/config attribution is missing.

  Acceptance criteria (“done” definition)

  * No arbitrary dictionary reaches durable findings.
  * Descriptors express every required capability/resource and fail validation when incomplete.
  * AnalysisContext exposes no lifecycle or raw persistence authority.
  * Finding schema preserves complete attributed result sets beyond prior 50-item summaries.

  Testing plan

  * Schema/model unit tests.
  * Malformed/oversized finding fuzz tests.
  * Context capability negative tests.
  * Large-result persistence tests.
  * Version/API compatibility tests.
  * AI attribution and untrusted-text tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Schema/model unit tests., Malformed/oversized finding fuzz tests., Context capability negative tests., Large-result persistence tests., Version/API compatibility tests., AI attribution and untrusted-text tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T14.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/plugins/contracts.py::PluginDescriptor, atlas/plugins/contracts.py::AnalysisContext, atlas/plugins/contracts.py::AnalysisFinding.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 54: Implement deterministic plugin discovery and registry snapshots

  1.2 source task(s): `T14.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T14.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/plugins/registry.py::PluginRegistry (create); atlas/core/runtime.py (extend); atlas/plugins/discovery.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create one ordered registry that rejects duplicate IDs, incompatible API ranges, conflicting providers, and source-declared capabilities that are not actually deployed.
  * Restore or protect this invariant: Two clean registry builds produce identical order and digest.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23.

  Where this applies

  * Primary affected components: `atlas/plugins/registry.py::PluginRegistry` (create: Own discovery, validation, enablement, and snapshot digest.); `atlas/core/runtime.py` (extend: Construct and freeze registries during composition.); `atlas/plugins/discovery.py` (create: Load approved built-ins/entry points deterministically.)
  * Epic boundary: Typed plugin contracts, registry, and trust policy — Turn Deep Understanding into a deterministic, versioned capability platform whose plugins emit normalized findings without receiving lifecycle or host authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].
  * Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-013 requires: Arbitrary in-process plugin dictionaries lack schema, version, capability, resource, determinism, and authority boundaries.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create one ordered registry that rejects duplicate IDs, incompatible API ranges, conflicting providers, and source-declared capabilities that are not actually deployed.
  * Component dispositions: `atlas/plugins/registry.py::PluginRegistry` (create: Own discovery, validation, enablement, and snapshot digest.); `atlas/core/runtime.py` (extend: Construct and freeze registries during composition.); `atlas/plugins/discovery.py` (create: Load approved built-ins/entry points deterministically.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define approved discovery sources, deterministic ordering, duplicate/conflict rules, enabled/deployed status, and runtime freeze semantics.
  * Validate descriptor, import/factory, API range, output schemas, backend availability, external tools, and policy grants.
  * Compute a canonical registry snapshot/digest persisted with jobs and findings.
  * Provide explicit unavailable/disabled/incompatible diagnostics instead of silent omission.

  Security and safety requirements

  * Do not import arbitrary modules from untrusted pipeline definitions.
  * Entry points are loaded only from installed/approved distributions and validated before activation.
  * Duplicate IDs and version ambiguity fail runtime construction.
  * Registry diagnostics avoid leaking environment secrets or full PATH.

  Edge cases and outliers to handle

  * Two distributions claim same plugin ID.
  * Plugin import has side effects or hangs.
  * External tool missing or wrong version.
  * Registry changes between job submission and execution.

  Acceptance criteria (“done” definition)

  * Two clean registry builds produce identical order and digest.
  * Duplicate/incompatible plugins fail before job creation.
  * Jobs retain the exact registry snapshot/version used.
  * Unavailable plugin states are distinct from disabled policy.

  Testing plan

  * Deterministic snapshot tests.
  * Duplicate/conflict negative tests.
  * Import timeout/side-effect isolation tests.
  * Missing tool/backend tests.
  * Registry change/version-skew tests.
  * Packaging entry-point integration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Deterministic snapshot tests., Duplicate/conflict negative tests., Import timeout/side-effect isolation tests., Missing tool/backend tests., Registry change/version-skew tests., Packaging entry-point integration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T14.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/plugins/registry.py::PluginRegistry, atlas/core/runtime.py, atlas/plugins/discovery.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
