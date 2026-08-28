@BinReaper Production TODOs

## TODO

* [ ] TODO 91: Deliver the plugin SDK, fixtures, and contract-validation CLI

  1.2 source task(s): `T23.1.3`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T14.1.4, T15.1.4, T22.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/plugin_sdk/ (create); atlas/cli.py (extend); examples/plugins/ (create); docs/plugins/sdk.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make safe extension development practical through typed packages, examples, synthetic artifacts, backend/registry conformance, and actionable validation without exposing internal state.
  * Restore or protect this invariant: A third party can implement and validate a plugin without importing private runtime/persistence APIs.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15.

  Where this applies

  * Primary affected components: `atlas/plugin_sdk/` (create: Publish stable descriptors, request/result models, errors, fixtures, and test helpers.); `atlas/cli.py` (extend: Add `plugin inspect`, `plugin validate`, and `plugin test` through supported APIs.); `examples/plugins/` (create: Provide minimal trusted and subprocess-safe analyzers/handlers with no secrets.); `docs/plugins/sdk.md` (create: Document lifecycle boundaries, capabilities, compatibility, testing, packaging, and release.)
  * Epic boundary: Retention, compatibility, plugin SDK, and source-provider evolution — Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Retention, compatibility, plugin SDK, and source-provider evolution.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Make safe extension development practical through typed packages, examples, synthetic artifacts, backend/registry conformance, and actionable validation without exposing internal state.
  * Component dispositions: `atlas/plugin_sdk/` (create: Publish stable descriptors, request/result models, errors, fixtures, and test helpers.); `atlas/cli.py` (extend: Add `plugin inspect`, `plugin validate`, and `plugin test` through supported APIs.); `examples/plugins/` (create: Provide minimal trusted and subprocess-safe analyzers/handlers with no secrets.); `docs/plugins/sdk.md` (create: Document lifecycle boundaries, capabilities, compatibility, testing, packaging, and release.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Package only public contracts needed by plugin authors; keep StateStore/coordinator/internal repositories inaccessible.
  * Provide fixture builders for content identities, structural reports, extracted artifacts, findings, budgets, cancellation, checkpoints, and errors.
  * Validate descriptor/schema/version/capabilities/tools/network/resources/timeout/risk and run deterministic contract tests.
  * Generate a machine-readable compatibility and capability report suitable for CI and registry admission.

  Security and safety requirements

  * Examples use synthetic inert inputs and never include credentials, exploit payloads, or unrestricted network/tool grants.
  * Validation cannot execute untrusted plugin code in-process by default; use static checks or subprocess backend under declared controls.
  * Prevent dependency/path/module confusion and verify package/executable identity according to trust policy.
  * Make dangerous capability requests explicit and policy-denied by default.

  Edge cases and outliers to handle

  * Plugin imports internal ATLAS modules.
  * Descriptor and runtime behavior disagree.
  * Plugin hangs during validation.
  * SDK/runtime versions are incompatible.

  Acceptance criteria (“done” definition)

  * A third party can implement and validate a plugin without importing private runtime/persistence APIs.
  * Contract CLI reports exact failed section, capability, compatibility, and remediation guidance.
  * Examples pass the same registry/backend conformance tests as built-ins.
  * Untrusted validation cannot mutate lifecycle state or access undeclared resources.

  Testing plan

  * SDK public-surface tests.
  * Example plugin end-to-end tests.
  * Descriptor/runtime mismatch tests.
  * Static/subprocess validation tests.
  * Compatibility matrix tests.
  * Documentation example execution tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: SDK public-surface tests., Example plugin end-to-end tests., Descriptor/runtime mismatch tests., Static/subprocess validation tests., Compatibility matrix tests., Documentation example execution tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T23.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/plugin_sdk/, atlas/cli.py, examples/plugins/, docs/plugins/sdk.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 92: Define the source-provider extension contract and defer unsupported providers

  1.2 source task(s): `T23.1.4`
  Priority: `P2`
  Estimated effort: `12 hours`
  Dependencies: `T6.1.4, T10.1.4, T14.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/sources/provider.py::SourceProvider (create); atlas/sources/registry.py::SourceProviderRegistry (create); atlas/sources/local.py (refactor); docs/architecture/source-providers.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Preserve the local filesystem as the evidenced near-term source while specifying how future read-only providers must establish stable source roots, generations, occurrences, snapshots, and mutation evidence.
  * Restore or protect this invariant: Local provider passes the contract without changing accepted local semantics.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15.

  Where this applies

  * Primary affected components: `atlas/sources/provider.py::SourceProvider` (create: Define registration, observation, stable locator, content-open, mutation token, and capability contracts.); `atlas/sources/registry.py::SourceProviderRegistry` (create: Provide deterministic provider registration and compatibility validation.); `atlas/sources/local.py` (refactor: Implement the contract for local directories/files through SourceAccessBroker.); `docs/architecture/source-providers.md` (create: Document required semantics and explicit deferred providers.)
  * Epic boundary: Retention, compatibility, plugin SDK, and source-provider evolution — Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Retention, compatibility, plugin SDK, and source-provider evolution.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Preserve the local filesystem as the evidenced near-term source while specifying how future read-only providers must establish stable source roots, generations, occurrences, snapshots, and mutation evidence.
  * Component dispositions: `atlas/sources/provider.py::SourceProvider` (create: Define registration, observation, stable locator, content-open, mutation token, and capability contracts.); `atlas/sources/registry.py::SourceProviderRegistry` (create: Provide deterministic provider registration and compatibility validation.); `atlas/sources/local.py` (refactor: Implement the contract for local directories/files through SourceAccessBroker.); `docs/architecture/source-providers.md` (create: Document required semantics and explicit deferred providers.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define provider-neutral `SourceRoot` locator/config digest, observation cursor/snapshot token, occurrence locator, metadata, safe open, mutation detection, and unavailable/changed behavior.
  * Require providers to produce immutable accepted `IntakeGeneration` manifests and exact bytes for content identity; providers cannot skip A–F phases.
  * Separate provider credentials/auth from artifact identity and store only secret references.
  * Document object storage, HTTP, repository, stream, and removable-media providers as deferred until a concrete requirement and consistency model exist.

  Security and safety requirements

  * Providers are untrusted adapters and cannot write lifecycle state, decisions, publications, or arbitrary filesystem paths.
  * Validate locators, redirects, credentials, TLS/pinning policy where applicable, snapshot consistency, size limits, and replay semantics.
  * Do not treat mutable URL/path/version labels as exact content identity.
  * Registry admission requires declared network/filesystem/tools/resources and threat-model review.

  Edge cases and outliers to handle

  * Provider cannot offer a consistent snapshot.
  * Credentials expire during intake.
  * Same locator returns different bytes.
  * Listing pagination repeats/omits objects.

  Acceptance criteria (“done” definition)

  * Local provider passes the contract without changing accepted local semantics.
  * Any provider lacking stable observation/mutation semantics is rejected or explicitly reduced-assurance, not silently accepted.
  * Deferred providers are named as non-implemented and have measurable admission criteria.
  * Provider removal leaves persisted source/intake/occurrence/content records readable.

  Testing plan

  * Local provider conformance tests.
  * Mutation/pagination/duplicate occurrence property tests.
  * Credential/redirect/size negative tests with synthetic adapters.
  * Registry determinism/compatibility tests.
  * Reduced-assurance rejection tests.
  * Persistence readability after provider removal tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Local provider conformance tests., Mutation/pagination/duplicate occurrence property tests., Credential/redirect/size negative tests with synthetic adapters., Registry determinism/compatibility tests., Reduced-assurance rejection tests., Persistence readability after provider removal tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T23.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/sources/provider.py::SourceProvider, atlas/sources/registry.py::SourceProviderRegistry, atlas/sources/local.py, docs/architecture/source-providers.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 93: Define the supported-platform matrix and mandatory CI policy

  1.2 source task(s): `T24.1.1`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T2.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `.github/workflows/quality.yml (create); pyproject.toml (extend); docs/development/quality-gates.md (create); docs/compatibility.md (extend)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Turn the current narrow test workflow into a documented, reviewable matrix of supported Python/OS/filesystem/resource controls and mandatory gates with explicit reduced-assurance rules.
  * Restore or protect this invariant: Supported and reduced-assurance platforms are explicitly resolved and versioned.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28.

  Where this applies

  * Primary affected components: `.github/workflows/quality.yml` (create: Run format, lint, type, unit, integration, schema, docs, and packaging gates.); `pyproject.toml` (extend: Pin tool configuration, supported Python metadata, extras, and test markers.); `docs/development/quality-gates.md` (create: Define mandatory/optional jobs, skips, ownership, and evidence retention.); `docs/compatibility.md` (extend: Publish supported and reduced-assurance platform matrix.)
  * Epic boundary: Continuous quality, packaging, benchmarks, and release evidence — Make every release claim traceable to clean builds, mandatory test families, security and compatibility evidence, representative benchmarks, and a practiced rollback.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-024: Establish continuous release-quality gates and benchmark evidence; evidence: R-16; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:.github/workflows/tests.yml:L1-L34]; Sections 21, 24, and 26.
  * Canonical proposed files/interfaces: `.github/workflows/*`, `pyproject.toml`, packaging/release scripts, `SECURITY.md`, `CONTRIBUTING.md`, benchmark and fixture directories. / CI/release manifest, benchmark schema, compatibility matrix, SBOM/provenance artifacts.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-024 requires: Current CI is test-only on Ubuntu/Python 3.13 and does not prove migration, packaging, security, compatibility, recovery, or performance.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Turn the current narrow test workflow into a documented, reviewable matrix of supported Python/OS/filesystem/resource controls and mandatory gates with explicit reduced-assurance rules.
  * Component dispositions: `.github/workflows/quality.yml` (create: Run format, lint, type, unit, integration, schema, docs, and packaging gates.); `pyproject.toml` (extend: Pin tool configuration, supported Python metadata, extras, and test markers.); `docs/development/quality-gates.md` (create: Define mandatory/optional jobs, skips, ownership, and evidence retention.); `docs/compatibility.md` (extend: Publish supported and reduced-assurance platform matrix.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Resolve and document supported Python versions, Linux/macOS/Windows scope, filesystems, architectures, and subprocess/resource-control assurance.
  * Define mandatory formatter, linter, type checker, unit, integration, schema/migration, docs/link, packaging, and security baseline jobs.
  * Require any skip/allowed failure to include owner, reason, issue, expiry, and release-impact marker.
  * Retain machine-readable job status, tool versions, commit, fixture/catalog versions, and coverage boundaries.

  Security and safety requirements

  * Use minimal CI permissions, pinned/reviewed actions, isolated untrusted PR handling, and no release secrets in untrusted jobs.
  * Run secret/dependency/license checks with triage policy rather than silently ignoring findings.
  * Prevent cache poisoning and artifact substitution through scoped keys and hashes.
  * Do not call a platform supported when mandatory safety/isolation tests cannot run; label reduced assurance.

  Edge cases and outliers to handle

  * Required OS runner unavailable.
  * Flaky race/fault test.
  * Dependency advisory has no fix.
  * Toolchain update changes results.

  Acceptance criteria (“done” definition)

  * Supported and reduced-assurance platforms are explicitly resolved and versioned.
  * Every mandatory job blocks release and unapproved skips fail policy.
  * CI reports what is not covered and does not use blanket production-ready claims.
  * Clean reruns preserve deterministic configuration and evidence metadata.

  Testing plan

  * Workflow syntax/policy tests.
  * Matrix expansion tests.
  * Skip-expiry/approval tests.
  * Pinned-action and permission checks.
  * Secret/dependency/license scan test fixtures.
  * Clean-run reproducibility checks.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Workflow syntax/policy tests., Matrix expansion tests., Skip-expiry/approval tests., Pinned-action and permission checks., Secret/dependency/license scan test fixtures., Clean-run reproducibility checks..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T24.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: .github/workflows/quality.yml, pyproject.toml, docs/development/quality-gates.md, docs/compatibility.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
