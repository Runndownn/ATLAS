@BinReaper Production TODOs

## TODO

* [ ] TODO 55: Implement plugin capability and trust-tier policy

  1.2 source task(s): `T14.1.3`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T14.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/plugins/policy.py::PluginTrustPolicy (create); atlas/plugins/registry.py (extend); atlas/config/phases.py::AnalysisConfig (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Map declared capabilities and provenance to trusted in-process, isolated subprocess, later sandbox, or denied execution without allowing configuration to self-grant authority.
  * Restore or protect this invariant: Every enabled plugin has one effective capability set and required backend.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23.

  Where this applies

  * Primary affected components: `atlas/plugins/policy.py::PluginTrustPolicy` (create: Evaluate descriptor, provenance, capabilities, and backend.); `atlas/plugins/registry.py` (extend: Attach policy decision and effective capabilities.); `atlas/config/phases.py::AnalysisConfig` (extend: Select plugins without granting privileges.)
  * Epic boundary: Typed plugin contracts, registry, and trust policy — Turn Deep Understanding into a deterministic, versioned capability platform whose plugins emit normalized findings without receiving lifecycle or host authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].
  * Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-013 requires: Arbitrary in-process plugin dictionaries lack schema, version, capability, resource, determinism, and authority boundaries.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Map declared capabilities and provenance to trusted in-process, isolated subprocess, later sandbox, or denied execution without allowing configuration to self-grant authority.
  * Component dispositions: `atlas/plugins/policy.py::PluginTrustPolicy` (create: Evaluate descriptor, provenance, capabilities, and backend.); `atlas/plugins/registry.py` (extend: Attach policy decision and effective capabilities.); `atlas/config/phases.py::AnalysisConfig` (extend: Select plugins without granting privileges.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define trust inputs: bundled/signed/approved provenance, active-content risk, filesystem/network/tool needs, deterministic claim, and deployment policy.
  * Return effective capabilities, required backend, limits, denied reasons, and policy digest.
  * Require in-process execution only for explicitly trusted bundled plugins; route risky/external-tool work to isolation or block.
  * Persist policy decision/version with WorkSpec and findings.

  Security and safety requirements

  * Plugin descriptor requests are untrusted declarations, not grants.
  * Network, process, secret, and source-root access default denied.
  * Policy downgrade requires explicit deployment authority and produces durable audit evidence.
  * AI plugins remain finding/proposal producers only.

  Edge cases and outliers to handle

  * Trusted plugin later changes package hash/version.
  * Required isolation backend unavailable.
  * Plugin declares no network but attempts connection.
  * Policy version changes while job is queued.

  Acceptance criteria (“done” definition)

  * Every enabled plugin has one effective capability set and required backend.
  * Untrusted/high-risk plugins cannot run in process.
  * Policy/config/version changes invalidate stale WorkSpecs and reuse keys.
  * Denied capability attempts are observable and tested.

  Testing plan

  * Policy truth-table tests.
  * Package provenance/version change tests.
  * Backend availability tests.
  * Denied network/process/filesystem abuse tests.
  * Queued-job policy drift tests.
  * AI authority negative tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Policy truth-table tests., Package provenance/version change tests., Backend availability tests., Denied network/process/filesystem abuse tests., Queued-job policy drift tests., AI authority negative tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T14.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/plugins/policy.py::PluginTrustPolicy, atlas/plugins/registry.py, atlas/config/phases.py::AnalysisConfig.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 56: Add the legacy `AnalyzerPlugin` adapter and lossless finding migration

  1.2 source task(s): `T14.1.4`
  Priority: `P1`
  Estimated effort: `12 hours`
  Dependencies: `T14.1.2, T14.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/phases/analysis.py::AnalyzerPlugin (refactor); atlas/plugins/legacy.py::LegacyAnalyzerAdapter (create); tests/compatibility/analyzers_v0_1/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Preserve existing analyzer plugins during a compatibility window while normalizing outputs, recording limitations, and eliminating metadata truncation as authoritative storage.
  * Restore or protect this invariant: Supported legacy plugins produce equivalent normalized findings through the adapter.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23.

  Where this applies

  * Primary affected components: `atlas/phases/analysis.py::AnalyzerPlugin` (refactor: Retain compatibility protocol and adapter.); `atlas/plugins/legacy.py::LegacyAnalyzerAdapter` (create: Translate supported descriptors/results safely.); `tests/compatibility/analyzers_v0_1/` (create: Pin supported legacy behavior.)
  * Epic boundary: Typed plugin contracts, registry, and trust policy — Turn Deep Understanding into a deterministic, versioned capability platform whose plugins emit normalized findings without receiving lifecycle or host authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-013: Define versioned typed plugin descriptors and a deterministic registry; evidence: GAP-014, GAP-015, REQ-021, REQ-022, REQ-023; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/analysis.py:L18-L134].
  * Canonical proposed files/interfaces: Create `atlas/plugins/contracts.py`, `atlas/plugins/registry.py`; refactor `atlas/phases/analysis.py`; compatibility adapter for `AnalyzerPlugin`. / `PluginDescriptor`, `Analyzer`, `AnalyzerInput`, `AnalyzerResult`, `AnalysisFinding`, `RegistrySnapshot`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-013 requires: Arbitrary in-process plugin dictionaries lack schema, version, capability, resource, determinism, and authority boundaries.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Preserve existing analyzer plugins during a compatibility window while normalizing outputs, recording limitations, and eliminating metadata truncation as authoritative storage.
  * Component dispositions: `atlas/phases/analysis.py::AnalyzerPlugin` (refactor: Retain compatibility protocol and adapter.); `atlas/plugins/legacy.py::LegacyAnalyzerAdapter` (create: Translate supported descriptors/results safely.); `tests/compatibility/analyzers_v0_1/` (create: Pin supported legacy behavior.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Inventory existing analyzer protocol, registration, result dictionaries, metadata summaries, and example plugins.
  * Wrap legacy plugins with explicit synthetic descriptor defaults only where behavior is provable; otherwise require migration.
  * Normalize every result into typed findings and persist all findings; keep metadata as bounded derived summary.
  * Emit deprecation diagnostics and a migration guide for plugin authors.

  Security and safety requirements

  * Legacy arbitrary fields are preserved only in bounded namespaced structured data after validation.
  * Adapter does not grant filesystem/network/process authority absent from approved policy.
  * Malformed or excessive output fails/blocks according to analysis policy rather than truncating silently.
  * Legacy plugins cannot create evidence approval or lifecycle transitions.

  Edge cases and outliers to handle

  * Legacy plugin returns non-serializable object.
  * More than 50 findings or nested huge metadata.
  * Plugin assumes direct source path access.
  * Plugin ID/version is missing.

  Acceptance criteria (“done” definition)

  * Supported legacy plugins produce equivalent normalized findings through the adapter.
  * All findings persist losslessly within declared limits.
  * Unsupported authority assumptions fail with migration guidance.
  * Metadata summary is explicitly derived and never authoritative.

  Testing plan

  * Legacy plugin golden tests.
  * Large-result/no-truncation tests.
  * Malformed/non-serializable output tests.
  * Direct path/network authority negative tests.
  * Deprecation telemetry tests.
  * Plugin author migration example tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Legacy plugin golden tests., Large-result/no-truncation tests., Malformed/non-serializable output tests., Direct path/network authority negative tests., Deprecation telemetry tests., Plugin author migration example tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T14.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/phases/analysis.py::AnalyzerPlugin, atlas/plugins/legacy.py::LegacyAnalyzerAdapter, tests/compatibility/analyzers_v0_1/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 57: Define immutable `WorkSpec`, `WorkResult`, and backend protocols

  1.2 source task(s): `T15.1.1`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T5.1.4, T14.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/base.py::WorkSpec (create); atlas/execution/base.py::WorkResult (create); atlas/execution/base.py::ExecutionBackend (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify exact operation inputs, identity/config/policy/resource authority, deadline, idempotency, fencing, outputs, diagnostics, and usage without exposing StateStore to execution code.
  * Restore or protect this invariant: Contracts are versioned, deterministic, and backend-neutral.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21.

  Where this applies

  * Primary affected components: `atlas/execution/base.py::WorkSpec` (create: Represent immutable authorized work.); `atlas/execution/base.py::WorkResult` (create: Represent untrusted execution outcome for validation.); `atlas/execution/base.py::ExecutionBackend` (create: Define submit/cancel/health/conformance contract.)
  * Epic boundary: ExecutionBackend contracts and trusted in-process execution — Separate lifecycle authority from execution location using immutable WorkSpec/WorkResult contracts and a conformance-tested trusted backend.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.
  * Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-014 requires: A stable work/result contract is required before isolation or remote execution; the backend must never own lifecycle state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify exact operation inputs, identity/config/policy/resource authority, deadline, idempotency, fencing, outputs, diagnostics, and usage without exposing StateStore to execution code.
  * Component dispositions: `atlas/execution/base.py::WorkSpec` (create: Represent immutable authorized work.); `atlas/execution/base.py::WorkResult` (create: Represent untrusted execution outcome for validation.); `atlas/execution/base.py::ExecutionBackend` (create: Define submit/cancel/health/conformance contract.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define operation ID/version, plugin/handler, input identity references, config/policy/registry digests, resource budget, deadline, idempotency key, attempt/work IDs, and fencing token.
  * Define result status, echoed authority fields, output references/manifest digest, findings, diagnostics, usage, start/end, and backend identity.
  * Define cancellation/deadline protocol, health/capabilities, and serialization/version negotiation.
  * Make specs/results content-addressable or digestible for audit and duplicate detection.

  Security and safety requirements

  * WorkSpec contains scoped references, not unrestricted source paths, database credentials, or secret values.
  * WorkResult is untrusted until coordinator validates identity, version, fencing, schema, quotas, and output integrity.
  * Backend has no lifecycle mutation interface.
  * Idempotency and fencing are core-authored and integrity-protected.

  Edge cases and outliers to handle

  * Result omits or changes echoed fields.
  * Result arrives after deadline/cancel/fencing change.
  * Spec schema newer than backend.
  * Output manifest references missing or foreign artifacts.

  Acceptance criteria (“done” definition)

  * Contracts are versioned, deterministic, and backend-neutral.
  * Backend code cannot obtain StateStore or transition authority through the interface.
  * Malformed/stale/foreign results are representable as validation failures.
  * Contract supports in-process, subprocess, and later remote backends without changing lifecycle semantics.

  Testing plan

  * Schema/serialization tests.
  * Digest determinism tests.
  * Malformed result fuzz tests.
  * Capability/version negotiation tests.
  * No-StateStore architecture tests.
  * Idempotency/fencing field integrity tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Schema/serialization tests., Digest determinism tests., Malformed result fuzz tests., Capability/version negotiation tests., No-StateStore architecture tests., Idempotency/fencing field integrity tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T15.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/base.py::WorkSpec, atlas/execution/base.py::WorkResult, atlas/execution/base.py::ExecutionBackend.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
