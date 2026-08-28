## TODO

* [ ] TODO 1: Freeze the active ATLAS ref and repository authority map

  1.2 source task(s): `T1.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `None`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `repository root / Git metadata (reuse); AGENTS.md, CONTRIBUTING*, SECURITY*, ADRs, CI and plan templates (reuse); planning/ATLAS production evidence map (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Confirm whether the frozen commit, paths, symbols, schemas, tests, commands, and planning authorities in the canonical ZIP still match the implementation workspace before any product change starts.
  * Restore or protect this invariant: The baseline record contains the exact current SHA, branch, dirty-state summary, repository inventory hash, and source-package hash.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze.

  Where this applies

  * Primary affected components: `repository root / Git metadata` (reuse: Use the current checkout as the highest implementation authority.); `AGENTS.md, CONTRIBUTING*, SECURITY*, ADRs, CI and plan templates` (reuse: Discover repository-native rules and commands instead of inventing them.); `planning/ATLAS production evidence map` (create: Persist the reconciled baseline and command matrix for all later tasks.)
  * Epic boundary: Evidence, baseline, and authority reconciliation — Replace the prior assessment limitations with a reproducible implementation baseline while preserving the supplied ZIP as the canonical planning truth.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Evidence, baseline, and authority reconciliation.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Confirm whether the frozen commit, paths, symbols, schemas, tests, commands, and planning authorities in the canonical ZIP still match the implementation workspace before any product change starts.
  * Component dispositions: `repository root / Git metadata` (reuse: Use the current checkout as the highest implementation authority.); `AGENTS.md, CONTRIBUTING*, SECURITY*, ADRs, CI and plan templates` (reuse: Discover repository-native rules and commands instead of inventing them.); `planning/ATLAS production evidence map` (create: Persist the reconciled baseline and command matrix for all later tasks.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Record default branch, exact commit SHA, dirty state, submodules, generated/vendor boundaries, package/toolchain versions, and supported targets.
  * Run a deterministic secret-safe repository inventory and map every path/symbol cited by the latest ZIP to present or missing state.
  * Extract authoritative build, lint, type, test, migration, packaging, and release commands from manifests and CI.
  * Publish an evidence delta showing unchanged, moved, replaced, newly implemented, and unresolved surfaces relative to `efa547cafc64b58d60d19dcc1e5ba32c6b046bc5`.

  Security and safety requirements

  * Do not execute untrusted repository scripts during the inventory pass; inspect before running.
  * Redact secrets, local usernames, absolute workstation paths, and mutable runtime state from retained evidence.
  * Treat missing or moved security controls as unresolved until code and tests prove replacement behavior.
  * Freeze writes while collecting the baseline; no implementation edits belong in this task.

  Edge cases and outliers to handle

  * Detached HEAD, shallow clone, missing tags, submodule drift, generated code, vendored code, and an already-dirty workspace.
  * A cited symbol moved while public compatibility imports still exist.
  * Repository-native commands require unavailable services, secrets, hardware, or unsupported operating systems.
  * Current HEAD contains concurrent operator changes that must not be overwritten.

  Acceptance criteria (“done” definition)

  * The baseline record contains the exact current SHA, branch, dirty-state summary, repository inventory hash, and source-package hash.
  * Every ZIP-cited ATLAS path/symbol is classified as present, moved, replaced, removed, or unverified.
  * A command matrix identifies the exact repository-native validation commands, working directory, prerequisites, and expected result class.
  * No production source file is modified.

  Testing plan

  * Inventory determinism test over two clean runs.
  * Path/symbol existence check against every ATLAS citation in the ZIP evidence ledger.
  * Repository command discovery cross-check against CI and package manifests.
  * Dirty-worktree preservation test in a disposable clone.
  * Secret-candidate scan of generated evidence.
  * Manual architecture-authority review by a repository maintainer.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Inventory determinism test over two clean runs., Path/symbol existence check against every ATLAS citation in the ZIP evidence ledger., Repository command discovery cross-check against CI and package manifests., Dirty-worktree preservation test in a disposable clone., Secret-candidate scan of generated evidence., Manual architecture-authority review by a repository maintainer..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T1.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: repository root / Git metadata, AGENTS.md, CONTRIBUTING*, SECURITY*, ADRs, CI and plan templates, planning/ATLAS production evidence map.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 2: Revalidate all product-direction requirements against the attached PDF

  1.2 source task(s): `T1.1.2`
  Priority: `P0`
  Estimated effort: `8 hours`
  Dependencies: `None`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `ATLAS.pdf (reuse); ATLAS_Requirements_Register.csv (migrate); planning/ATLAS PDF evidence index (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Close the latest package's prior PDF-access limitation by verifying all 30 requirements, page references, lifecycle diagrams, and sequencing constraints against the attached 34-page document.
  * Restore or protect this invariant: All 30 requirements have a verified page range, status, mapped production task IDs, and an ambiguity field.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze.

  Where this applies

  * Primary affected components: `ATLAS.pdf` (reuse: Treat the attached document as the desired-direction authority, not implementation proof.); `ATLAS_Requirements_Register.csv` (migrate: Replace pending revalidation status with page-verified results and ambiguity notes.); `planning/ATLAS PDF evidence index` (create: Retain page text/visual references and requirement-to-task mappings.)
  * Epic boundary: Evidence, baseline, and authority reconciliation — Replace the prior assessment limitations with a reproducible implementation baseline while preserving the supplied ZIP as the canonical planning truth.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Evidence, baseline, and authority reconciliation.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Close the latest package's prior PDF-access limitation by verifying all 30 requirements, page references, lifecycle diagrams, and sequencing constraints against the attached 34-page document.
  * Component dispositions: `ATLAS.pdf` (reuse: Treat the attached document as the desired-direction authority, not implementation proof.); `ATLAS_Requirements_Register.csv` (migrate: Replace pending revalidation status with page-verified results and ambiguity notes.); `planning/ATLAS PDF evidence index` (create: Retain page text/visual references and requirement-to-task mappings.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Verify the document page count, metadata availability, repository baseline, and the six-stage lifecycle wording.
  * Recheck REQ-001 through REQ-030 against the cited pages and record explicit versus inferred status without strengthening ambiguous language.
  * Inspect the lifecycle, end-state, and lineage visuals on pages 21, 29, and 31 and reconcile them with the prose on pages 16, 22, 27, and 28.
  * Update the production task crosswalk so every requirement maps to at least one implementation or explicit defer/reject task.

  Security and safety requirements

  * Do not treat diagrams, roadmap labels, or completion language as evidence of current code.
  * Preserve the rule that AI may analyze and propose but cannot own provenance, safety, lifecycle state, or promotion.
  * Preserve structural inspection before materialization and the source-occurrence/content-identity split.
  * Record any legibility or extraction ambiguity rather than filling it from general knowledge.

  Edge cases and outliers to handle

  * PDF text extraction differs from rendered page text.
  * A simplified diagram omits records described in the prose.
  * A requirement spans several pages with different priority labels.
  * The document has no embedded publication date or version metadata.

  Acceptance criteria (“done” definition)

  * All 30 requirements have a verified page range, status, mapped production task IDs, and an ambiguity field.
  * The end-state and lifecycle diagrams are summarized without contradicting the attached visuals.
  * The previous `PDF not independently accessible` limitation is explicitly closed for this planning run.
  * No PDF statement is promoted to current implementation fact.

  Testing plan

  * Page-by-page extraction completeness check.
  * Rendered visual review for pages 21, 29, and 31.
  * Requirement-page keyword and semantic cross-check.
  * Crosswalk completeness test: 30 requirements mapped exactly once or more.
  * Conflict check between page 16 full lineage and page 31 simplified lineage.
  * Independent reviewer spot-check of at least six high-impact requirements.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Page-by-page extraction completeness check., Rendered visual review for pages 21, 29, and 31., Requirement-page keyword and semantic cross-check., Crosswalk completeness test: 30 requirements mapped exactly once or more., Conflict check between page 16 full lineage and page 31 simplified lineage., Independent reviewer spot-check of at least six high-impact requirements..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T1.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: ATLAS.pdf, ATLAS_Requirements_Register.csv, planning/ATLAS PDF evidence index.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 3: Restore and revalidate the Yggdrasil donor baseline and license provenance

  1.2 source task(s): `T1.1.3`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `None`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `Runndownn/Yggdrasil@2b0c51b6132c2a16e63fc2e2de2d2b4598b5fe40 (reuse); ATLAS donor integration map (migrate); planning/donor-provenance.json (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Confirm the donor commit, exact symbols, dependencies, tests, and license notices before any REUSE or ADAPT decision can become implementation work.
  * Restore or protect this invariant: Every donor integration row has a verified path/symbol, commit, dependency set, license note, and final disposition.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze.

  Where this applies

  * Primary affected components: `Runndownn/Yggdrasil@2b0c51b6132c2a16e63fc2e2de2d2b4598b5fe40` (reuse: Use the frozen donor commit only after it is restored and hash-verified.); `ATLAS donor integration map` (migrate: Promote each donor row from unresolved evidence to verified ADAPT/REIMPLEMENT/DEFER/REJECT.); `planning/donor-provenance.json` (create: Record source hashes, license headers, dependencies, and tests to port.)
  * Epic boundary: Evidence, baseline, and authority reconciliation — Replace the prior assessment limitations with a reproducible implementation baseline while preserving the supplied ZIP as the canonical planning truth.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze; PROMPT:Pasted markdown (2).md:Stages 1-4.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Evidence, baseline, and authority reconciliation.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Confirm the donor commit, exact symbols, dependencies, tests, and license notices before any REUSE or ADAPT decision can become implementation work.
  * Component dispositions: `Runndownn/Yggdrasil@2b0c51b6132c2a16e63fc2e2de2d2b4598b5fe40` (reuse: Use the frozen donor commit only after it is restored and hash-verified.); `ATLAS donor integration map` (migrate: Promote each donor row from unresolved evidence to verified ADAPT/REIMPLEMENT/DEFER/REJECT.); `planning/donor-provenance.json` (create: Record source hashes, license headers, dependencies, and tests to port.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Obtain an archive or checkout of the exact frozen donor commit and verify its tree hash and default branch history.
  * Read every donor path/symbol cited by the ZIP, including registry, store, content models, release filesystem, staging, and executor code.
  * Map transitive dependencies, platform assumptions, data contracts, migrations, test fixtures, and license obligations.
  * Revise donor dispositions only where primary source changes the latest package's conclusion; never copy wholesale.

  Security and safety requirements

  * No donor code is copied until its license text, copyright notice, and dependency license posture are recorded.
  * Do not import donor service identities, governance plane, operator gates, or AI inbox into ATLAS core without a separate justified task.
  * Treat release-filesystem patterns as race-prone unless handle-relative behavior is independently verified.
  * Keep donor source unavailable status visible; no implementation task may claim REUSE while this task is incomplete.

  Edge cases and outliers to handle

  * Repository URL remains unavailable, commit exists only in an operator archive, or files differ from the cited tree.
  * Donor tests depend on services, secrets, or platform behavior absent in ATLAS.
  * A useful concept is embedded in a monolithic governance store.
  * License headers differ by path or generated code lacks clear provenance.

  Acceptance criteria (“done” definition)

  * Every donor integration row has a verified path/symbol, commit, dependency set, license note, and final disposition.
  * Tests worth porting are named with the ATLAS invariant they prove.
  * No donor mechanism is designated `REUSE` without an exact source and compatibility assessment.
  * Unavailable evidence remains `UNRESOLVED` and blocks code transplantation.

  Testing plan

  * Tree-hash and archive-integrity verification.
  * Dependency graph and import-boundary analysis.
  * License/header scan across candidate donor files.
  * Donor test inventory and fixture portability review.
  * API/data-contract diff against target ATLAS contracts.
  * Manual security review of source-access and release mutation patterns.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Tree-hash and archive-integrity verification., Dependency graph and import-boundary analysis., License/header scan across candidate donor files., Donor test inventory and fixture portability review., API/data-contract diff against target ATLAS contracts., Manual security review of source-access and release mutation patterns..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T1.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: Runndownn/Yggdrasil@2b0c51b6132c2a16e63fc2e2de2d2b4598b5fe40, ATLAS donor integration map, planning/donor-provenance.json.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 4: Publish the canonical component-ownership and scope boundary matrix

  1.2 source task(s): `T1.1.4`
  Priority: `P0`
  Estimated effort: `10 hours`
  Dependencies: `T1.1.1, T1.1.2, T1.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `ATLAS_Evidence_Driven_Architecture_Blueprint.md sections 8-17 (reuse); Pasted markdown (2).md Stages 1-5 (reuse); docs/architecture/component-responsibility-matrix.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Reconcile the latest architecture with the earlier deep-review helper candidates, assigning one owner to each authoritative state and rejecting unnecessary micro-components or generic workflow expansion.
  * Restore or protect this invariant: Every authoritative record and transition has exactly one named owner.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Assessment_Package.zip; PROMPT:Pasted markdown.md:Evidence hierarchy and baseline freeze.

  Where this applies

  * Primary affected components: `ATLAS_Evidence_Driven_Architecture_Blueprint.md sections 8-17` (reuse: Use the latest target architecture as the decision authority.); `Pasted markdown (2).md Stages 1-5` (reuse: Use helper candidates as questions, not as implementation facts.); `docs/architecture/component-responsibility-matrix.md` (create: Record final component classifications, state ownership, and prohibited authority crossings.)
  * Epic boundary: Evidence, baseline, and authority reconciliation — Replace the prior assessment limitations with a reproducible implementation baseline while preserving the supplied ZIP as the canonical planning truth.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
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
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create the canonical machine-readable fixture schema that separates current observed behavior from target behavior and ties each case to gaps, requirements, setup, cleanup, and evidence artifacts.
  * Restore or protect this invariant: The manifest schema validates all baseline fixtures and rejects missing GAP/REQ lineage.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14.

  Where this applies

  * Primary affected components: `tests/characterization/manifest.schema.json` (create: Define deterministic fixture records and evidence fields.); `tests/fixtures/v0_1/` (create: Store sanitized baseline inputs by version.); `tests/characterization/conftest.py` (create: Provide bounded setup, normalization, and cleanup helpers.)
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
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Execute the highest-consequence baseline scenarios through real public entry points and capture exit status, terminal states, rows, event sequences, exceptions, and side effects as machine-readable evidence.
  * Restore or protect this invariant: Every selected scenario records a complete, canonical evidence bundle.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-001; LATEST-ZIP:ATLAS_Evidence_Ledger.csv:GAP-001..GAP-015; PDF:p.10-14.

  Where this applies

  * Primary affected components: `tests/characterization/test_cli_api_state.py` (create: Exercise public invocation surfaces and persisted outcomes.); `tests/characterization/evidence_capture.py` (create: Capture normalized database, event, and filesystem evidence.); `atlas public CLI/Python API` (reuse: Characterize without changing production behavior.)
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

* [ ] TODO 10: Implement deterministic safe loading, merge order, and canonical digests

  1.2 source task(s): `T3.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T3.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/config/loader.py::ConfigurationResolver (create); examples/*.yaml (migrate); atlas/cli.py::pipeline preflight (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create one resolver that safely parses pipeline YAML/JSON, applies deterministic overrides, validates typed values, and computes a stable secret-free configuration digest.
  * Restore or protect this invariant: Equivalent normalized configurations produce identical digests across runs.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34.

  Where this applies

  * Primary affected components: `atlas/config/loader.py::ConfigurationResolver` (create: Own parsing, merging, validation, and canonicalization.); `examples/*.yaml` (migrate: Add schema version and typed phase sections.); `atlas/cli.py::pipeline preflight` (extend: Validate before job creation.)
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
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace opaque metadata dictionaries with phase-owned configuration models that define defaults, limits, capability requirements, and validation for each A-F stage.
  * Restore or protect this invariant: Every built-in phase receives only its typed configuration object.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34.

  Where this applies

  * Primary affected components: `atlas/config/phases.py` (create: Own Recon through Review typed configuration models.); `atlas/phases/base.py::PhaseContext` (extend: Expose validated phase configuration only.); `atlas/phases/*` (refactor: Consume typed settings instead of unstructured metadata.)
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
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Preserve current YAML, CLI syntax, and imports through an explicit compatibility window while making new definitions canonical and observable.
  * Restore or protect this invariant: All existing examples either migrate to an approved digest or fail with a documented reason.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-002; REQ-001,REQ-002,REQ-006,REQ-007; PDF:p.10,p.12,p.29,p.34.

  Where this applies

  * Primary affected components: `atlas/config/legacy.py::LegacyPipelineLoader` (create: Normalize supported v0.1 inputs without guessing.); `atlas/cli.py::pipeline migrate` (extend: Provide dry-run conversion and diagnostics.); `docs/migrations/pipeline-v1.md` (create: Document compatibility window, rollback, and deprecation.)
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

* [ ] TODO 13: Define the narrow `StateStore` transaction and repository contracts

  1.2 source task(s): `T4.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T2.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/base.py::StateStore (create); atlas/core/job_store.py::JobStore (refactor); atlas/persistence/errors.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Separate lifecycle semantics from aiosqlite details while assigning explicit transaction ownership and error taxonomy to one persistence boundary.
  * Restore or protect this invariant: No authoritative repository method commits outside a `StateStore` transaction.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15.

  Where this applies

  * Primary affected components: `atlas/persistence/base.py::StateStore` (create: Define transaction, repository, and capability protocols.); `atlas/core/job_store.py::JobStore` (refactor: Retain as compatibility facade over the new repositories.); `atlas/persistence/errors.py` (create: Normalize contention, integrity, schema, and I/O failures.)
  * Epic boundary: StateStore and SQLite migration foundation — Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]
  * Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-003 requires: Inline schema creation, independent commits, and absent schema versioning prevent safe evolution of authoritative records.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Separate lifecycle semantics from aiosqlite details while assigning explicit transaction ownership and error taxonomy to one persistence boundary.
  * Component dispositions: `atlas/persistence/base.py::StateStore` (create: Define transaction, repository, and capability protocols.); `atlas/core/job_store.py::JobStore` (refactor: Retain as compatibility facade over the new repositories.); `atlas/persistence/errors.py` (create: Normalize contention, integrity, schema, and I/O failures.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define async transaction context, read/write repository interfaces, isolation expectations, commit/rollback ownership, and nested-transaction prohibition or savepoint rules.
  * Separate repositories for jobs, phase runs, attempts, events, controls, checkpoints, artifacts, and later records without exposing raw connections.
  * Define stable persistence error codes and retryability hints without making retry decisions inside the store.
  * Create a backend conformance contract that SQLite and future PostgreSQL must satisfy.

  Security and safety requirements

  * Use parameterized SQL only and never expose raw SQL execution to plugins, adapters, or model-controlled input.
  * Database paths must be canonical, outside source roots, and created with restrictive permissions.
  * Transaction APIs must not allow partial authoritative writes after an exception.
  * Unknown integrity or schema errors fail closed and retain diagnostics.

  Edge cases and outliers to handle

  * Nested service calls attempt independent commits.
  * Cancellation occurs during commit or rollback.
  * Connection is lost or closed while a transaction is active.
  * A future backend cannot provide identical locking semantics.

  Acceptance criteria (“done” definition)

  * No authoritative repository method commits outside a `StateStore` transaction.
  * `JobStore` compatibility calls delegate without changing public results.
  * The error taxonomy distinguishes contention, corruption, schema mismatch, constraint, cancellation, and storage exhaustion.
  * A backend conformance test skeleton covers transaction atomicity and rollback.

  Testing plan

  * Protocol/type-check tests.
  * Transaction commit/rollback unit tests.
  * Nested-call and cancellation tests.
  * Parameterized-query/static checks.
  * Compatibility facade tests.
  * Backend conformance contract tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Protocol/type-check tests., Transaction commit/rollback unit tests., Nested-call and cancellation tests., Parameterized-query/static checks., Compatibility facade tests., Backend conformance contract tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T4.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/base.py::StateStore, atlas/core/job_store.py::JobStore, atlas/persistence/errors.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 14: Implement the SQLite backend with explicit connection and locking policy

  1.2 source task(s): `T4.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T4.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/sqlite.py::SQLiteStateStore (create); atlas/persistence/sqlite_repositories.py (create); atlas/core/job_store.py (migrate)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide the reference backend with foreign keys, WAL/rollback policy, busy timeout, connection lifecycle, contention behavior, and health diagnostics defined rather than implicit.
  * Restore or protect this invariant: Foreign keys and uniqueness constraints are enabled and demonstrated.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15.

  Where this applies

  * Primary affected components: `atlas/persistence/sqlite.py::SQLiteStateStore` (create: Own SQLite connections and transactions.); `atlas/persistence/sqlite_repositories.py` (create: Implement repository contracts.); `atlas/core/job_store.py` (migrate: Route all writes through SQLiteStateStore.)
  * Epic boundary: StateStore and SQLite migration foundation — Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]
  * Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-003 requires: Inline schema creation, independent commits, and absent schema versioning prevent safe evolution of authoritative records.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Provide the reference backend with foreign keys, WAL/rollback policy, busy timeout, connection lifecycle, contention behavior, and health diagnostics defined rather than implicit.
  * Component dispositions: `atlas/persistence/sqlite.py::SQLiteStateStore` (create: Own SQLite connections and transactions.); `atlas/persistence/sqlite_repositories.py` (create: Implement repository contracts.); `atlas/core/job_store.py` (migrate: Route all writes through SQLiteStateStore.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Configure and verify foreign keys, journal mode, synchronous level, busy timeout, row factory, and connection ownership at startup.
  * Use explicit transaction modes for read and write paths and document lock acquisition order.
  * Implement bounded contention retry signaling without hidden infinite loops.
  * Expose integrity, schema, lock-wait, file-permission, and capacity health information.

  Security and safety requirements

  * Reject database files or parent directories under untrusted source roots.
  * Avoid permissive file modes and unsafe temporary database locations.
  * Do not log SQL parameter values that may contain source paths, secrets, or payload text.
  * Corruption and unsupported pragmas fail readiness rather than degrade silently.

  Edge cases and outliers to handle

  * Two writers contend while a long reader is active.
  * Filesystem does not support requested journal behavior.
  * Disk fills during journal or commit.
  * Process is terminated while WAL contains committed but uncheckpointed data.

  Acceptance criteria (“done” definition)

  * Foreign keys and uniqueness constraints are enabled and demonstrated.
  * Contention yields bounded, classified behavior with lock-wait metrics.
  * All existing job/phase persistence tests pass through the new backend.
  * Startup reports actual SQLite capabilities and refuses unsafe/unsupported state.

  Testing plan

  * SQLite conformance tests.
  * Concurrent reader/writer contention tests.
  * Foreign-key and constraint negative tests.
  * Disk-full and permission fault tests.
  * WAL recovery tests.
  * Connection-leak and shutdown tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: SQLite conformance tests., Concurrent reader/writer contention tests., Foreign-key and constraint negative tests., Disk-full and permission fault tests., WAL recovery tests., Connection-leak and shutdown tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T4.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/sqlite.py::SQLiteStateStore, atlas/persistence/sqlite_repositories.py, atlas/core/job_store.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 15: Create immutable numbered migrations and the v0.1 upgrade path

  1.2 source task(s): `T4.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T4.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/migrations/ (create); atlas/schema/__init__.py (refactor); schema_migrations table (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace inline schema creation with checksummed, forward-applied migrations and deterministic schema fingerprints for fresh and upgraded databases.
  * Restore or protect this invariant: Fresh and upgraded databases have identical schema fingerprints and invariants.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15.

  Where this applies

  * Primary affected components: `atlas/persistence/migrations/` (create: Store immutable numbered migration modules or SQL.); `atlas/schema/__init__.py` (refactor: Export schema version and migration APIs.); `schema_migrations table` (create: Record version, checksum, tool version, and application result.)
  * Epic boundary: StateStore and SQLite migration foundation — Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]
  * Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-003 requires: Inline schema creation, independent commits, and absent schema versioning prevent safe evolution of authoritative records.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace inline schema creation with checksummed, forward-applied migrations and deterministic schema fingerprints for fresh and upgraded databases.
  * Component dispositions: `atlas/persistence/migrations/` (create: Store immutable numbered migration modules or SQL.); `atlas/schema/__init__.py` (refactor: Export schema version and migration APIs.); `schema_migrations table` (create: Record version, checksum, tool version, and application result.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define migration discovery, ordering, checksums, schema metadata, supported version range, and no-edit rule for applied migrations.
  * Write the initial baseline and v0.1-to-target migrations for existing jobs, phases, selected events, and required constraints.
  * Compute a canonical schema fingerprint and verify fresh versus upgraded convergence.
  * Record migration events only after successful schema/data verification.

  Security and safety requirements

  * Never auto-downgrade or run against a newer unknown schema.
  * Checksum drift, missing migration, or duplicate version fails startup.
  * Migrations use bounded data transforms and parameterized operations.
  * Sensitive row values are not written to migration logs.

  Edge cases and outliers to handle

  * Empty database, current v0.1 database, partially initialized database.
  * Migration file edited after prior application.
  * Process termination between DDL and data transform.
  * Large legacy tables exceed memory if transformed eagerly.

  Acceptance criteria (“done” definition)

  * Fresh and upgraded databases have identical schema fingerprints and invariants.
  * Migration checksums are immutable and verified on every startup.
  * Newer unsupported schema and checksum drift fail with stable diagnostics.
  * Every migration has forward test fixtures and a documented restore-based rollback.

  Testing plan

  * Fresh-install migration tests.
  * Every-version upgrade tests.
  * Schema fingerprint comparison.
  * Checksum-drift and missing-version negative tests.
  * Large-row streaming migration tests.
  * Process-kill fault injection at each migration boundary.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Fresh-install migration tests., Every-version upgrade tests., Schema fingerprint comparison., Checksum-drift and missing-version negative tests., Large-row streaming migration tests., Process-kill fault injection at each migration boundary..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T4.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/migrations/, atlas/schema/__init__.py, schema_migrations table.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 16: Implement verified backup, restore, integrity, and migration recovery

  1.2 source task(s): `T4.1.4`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T4.1.2, T4.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/backup.py (create); atlas/cli.py::database commands (extend); docs/operations/database-recovery.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make database evolution and corruption handling operationally recoverable with preflight integrity checks, verified backups, post-migration invariants, and deterministic operator diagnostics.
  * Restore or protect this invariant: A verified pre-migration backup exists before any schema change.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-003; REQ-018; PDF:p.15.

  Where this applies

  * Primary affected components: `atlas/persistence/backup.py` (create: Own safe backup, hash, restore, and verification workflows.); `atlas/cli.py::database commands` (extend: Expose inspect, backup, verify, migrate, and restore dry runs.); `docs/operations/database-recovery.md` (create: Document failure and rollback procedures.)
  * Epic boundary: StateStore and SQLite migration foundation — Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-003: Create the StateStore abstraction and versioned SQLite migration system; evidence: GAP-009, REQ-018; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/job_store.py:L19-L65,L172-L350]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/schema/__init__.py:L1-L9]
  * Canonical proposed files/interfaces: Create `atlas/persistence/base.py`, `atlas/persistence/sqlite.py`, `atlas/persistence/migrations/`; refactor `atlas/core/job_store.py`; replace `atlas/schema/__init__.py` exports. / `StateStore`, `Transaction`, repository interfaces for jobs/phases/events initially; `schema_migrations(version, checksum, applied_at, tool_version)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-003 requires: Inline schema creation, independent commits, and absent schema versioning prevent safe evolution of authoritative records.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Make database evolution and corruption handling operationally recoverable with preflight integrity checks, verified backups, post-migration invariants, and deterministic operator diagnostics.
  * Component dispositions: `atlas/persistence/backup.py` (create: Own safe backup, hash, restore, and verification workflows.); `atlas/cli.py::database commands` (extend: Expose inspect, backup, verify, migrate, and restore dry runs.); `docs/operations/database-recovery.md` (create: Document failure and rollback procedures.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Before migration, run integrity/foreign-key checks, capture schema/row fingerprints, create a verified backup, and confirm free-space requirements.
  * After migration, verify schema fingerprint, row counts, referential invariants, and representative deserialization.
  * Implement restore verification into a separate path before any destructive replacement.
  * Detect partial migration markers, stale backups, orphan temporary files, and incompatible binary/schema combinations.

  Security and safety requirements

  * Backup and restore paths are canonical, permission-restricted, and outside source roots.
  * Never overwrite the only valid database without a separately verified copy.
  * Integrity failure blocks normal startup and exposes read-only diagnostics.
  * Backup manifests contain hashes and versions but no sensitive row content.

  Edge cases and outliers to handle

  * Corrupt source DB, corrupt backup, insufficient disk, permission loss.
  * Operator selects the wrong backup or a backup from a newer schema.
  * Restore succeeds but application binary cannot read the schema.
  * Crash occurs during final database swap.

  Acceptance criteria (“done” definition)

  * A verified pre-migration backup exists before any schema change.
  * Restore drills reproduce schema and row fingerprints in a separate location.
  * Migration failure leaves the original database and backup usable.
  * Operator diagnostics identify exact failure stage, artifact hashes, and safe next action.

  Testing plan

  * Integrity and FK check tests.
  * Backup hash and restore verification tests.
  * Corruption and truncated-backup negative tests.
  * Disk-full and permission fault tests.
  * Crash-at-swap tests.
  * End-to-end v0.1 migration and rollback drill.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Integrity and FK check tests., Backup hash and restore verification tests., Corruption and truncated-backup negative tests., Disk-full and permission fault tests., Crash-at-swap tests., End-to-end v0.1 migration and rollback drill..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T4.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/backup.py, atlas/cli.py::database commands, docs/operations/database-recovery.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 17: Specify exhaustive job, phase, attempt, and control state tables

  1.2 source task(s): `T5.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T3.1.4, T4.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/states.py (create); docs/architecture/state-machines.md (create); atlas/core/lifecycle.py::TransitionPolicy (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Define states, terminal conditions, transition guards, failure propagation, skip reasons, suspension, cancellation, retry scheduling, restart, and replay before implementing mutations.
  * Restore or protect this invariant: Transition tables are exhaustive and machine-readable.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15.

  Where this applies

  * Primary affected components: `atlas/models/states.py` (create: Own enums, terminal sets, and typed transition reasons.); `docs/architecture/state-machines.md` (create: Publish transition tables and invariants.); `atlas/core/lifecycle.py::TransitionPolicy` (create: Represent legal transitions as data and guards.)
  * Epic boundary: Explicit lifecycle state machines, attempts, and fencing — Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.
  * Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-004 requires: Current mutable status fields do not define legal transitions, attempts, fencing, immutable terminal truth, or stale-result behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Define states, terminal conditions, transition guards, failure propagation, skip reasons, suspension, cancellation, retry scheduling, restart, and replay before implementing mutations.
  * Component dispositions: `atlas/models/states.py` (create: Own enums, terminal sets, and typed transition reasons.); `docs/architecture/state-machines.md` (create: Publish transition tables and invariants.); `atlas/core/lifecycle.py::TransitionPolicy` (create: Represent legal transitions as data and guards.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define job, phase-run, attempt, and control-request states with one meaning per state.
  * Enumerate every legal transition with actor, preconditions, required evidence, emitted event, and terminal behavior.
  * Define propagation from attempt outcome to phase and job, including optional/skipped/blocked/degraded distinctions.
  * Define restart and replay decisions without implying side-effect safety not yet proven.

  Security and safety requirements

  * No plugin, worker, adapter, event consumer, or AI output can author a state transition.
  * Terminal truth is immutable except through explicit reconciliation/supersession records.
  * Unknown or malformed state/version fails closed.
  * Cancellation and suspension never erase prior evidence.

  Edge cases and outliers to handle

  * Cancel requested before first attempt, during checkpoint, or after terminal completion.
  * Optional phase fails while required phases succeed.
  * Process restarts with job RUNNING but no live owner.
  * Legacy database contains a status combination not representable in the new tables.

  Acceptance criteria (“done” definition)

  * Transition tables are exhaustive and machine-readable.
  * Every state has one owner, legal predecessors/successors, and terminal semantics.
  * Invalid legacy combinations have an explicit migration or blocked-state rule.
  * The tables map to PDF lifecycle semantics without creating DAG behavior.

  Testing plan

  * Transition-table completeness tests.
  * State enum serialization/version tests.
  * Truth-table tests for failure propagation.
  * Legacy-state mapping tests.
  * Terminal immutability negative tests.
  * Model-based review against sequence diagrams.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Transition-table completeness tests., State enum serialization/version tests., Truth-table tests for failure propagation., Legacy-state mapping tests., Terminal immutability negative tests., Model-based review against sequence diagrams..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T5.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/states.py, docs/architecture/state-machines.md, atlas/core/lifecycle.py::TransitionPolicy.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 18: Persist immutable phase runs and execution attempts

  1.2 source task(s): `T5.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T5.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `phase_runs and attempts migrations (create); atlas/persistence/repositories/attempts.py (create); atlas/core/orchestrator.py (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Represent each phase execution as a durable phase run with one or more immutable attempts, linked errors, checkpoints, backend identity, and result digests.
  * Restore or protect this invariant: Every execution is represented by exactly one immutable attempt record.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15.

  Where this applies

  * Primary affected components: `phase_runs and attempts migrations` (create: Persist phase/attempt identity and relationships.); `atlas/persistence/repositories/attempts.py` (create: Own attempt reads and writes.); `atlas/core/orchestrator.py` (refactor: Delegate attempt lifecycle to the coordinator.)
  * Epic boundary: Explicit lifecycle state machines, attempts, and fencing — Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.
  * Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-004 requires: Current mutable status fields do not define legal transitions, attempts, fencing, immutable terminal truth, or stale-result behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Represent each phase execution as a durable phase run with one or more immutable attempts, linked errors, checkpoints, backend identity, and result digests.
  * Component dispositions: `phase_runs and attempts migrations` (create: Persist phase/attempt identity and relationships.); `atlas/persistence/repositories/attempts.py` (create: Own attempt reads and writes.); `atlas/core/orchestrator.py` (refactor: Delegate attempt lifecycle to the coordinator.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Add phase-run and attempt identifiers, ordinal, backend/plugin identity, fencing token, start/end, outcome, error class, checkpoint, work/result digest, and predecessor/successor links.
  * Create an attempt only after transition guards and required inputs are durably verified.
  * Append outcomes and evidence without mutating completed attempt identity.
  * Project legacy phase fields from canonical records during the compatibility window.

  Security and safety requirements

  * Prevent caller-supplied IDs from colliding or crossing jobs.
  * Do not persist unbounded error payloads or artifact content in attempt rows.
  * Foreign keys and uniqueness prevent duplicate attempt numbers and cross-phase checkpoint links.
  * Backend credentials or secrets never enter attempt metadata.

  Edge cases and outliers to handle

  * Attempt creation succeeds but execution never starts.
  * Two owners race to create the next attempt.
  * Result arrives after a successor attempt exists.
  * Legacy phase row has no attempt record.

  Acceptance criteria (“done” definition)

  * Every execution is represented by exactly one immutable attempt record.
  * Duplicate concurrent attempt creation is rejected by transaction and uniqueness guards.
  * Legacy phase status remains available as a derived compatibility projection.
  * Attempt rows link to exact input/config/policy and later result/checkpoint evidence.

  Testing plan

  * Repository unit tests.
  * Concurrent attempt-creation tests.
  * Foreign-key/uniqueness negative tests.
  * Legacy projection tests.
  * Crash after attempt creation tests.
  * Serialization and schema migration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Repository unit tests., Concurrent attempt-creation tests., Foreign-key/uniqueness negative tests., Legacy projection tests., Crash after attempt creation tests., Serialization and schema migration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T5.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: phase_runs and attempts migrations, atlas/persistence/repositories/attempts.py, atlas/core/orchestrator.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 19: Implement guarded atomic transitions and fencing tokens

  1.2 source task(s): `T5.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T5.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/lifecycle.py::LifecycleCoordinator (create); atlas/persistence/repositories/transitions.py (create); atlas/core/orchestrator.py::PipelineOrchestrator (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Apply state changes through one coordinator path that compares expected state/version, advances fencing authority, and records the transition atomically.
  * Restore or protect this invariant: Every transition requires the expected current state/version and fails deterministically when stale.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15.

  Where this applies

  * Primary affected components: `atlas/core/lifecycle.py::LifecycleCoordinator` (create: Own authoritative transition commands.); `atlas/persistence/repositories/transitions.py` (create: Perform compare-and-set mutations.); `atlas/core/orchestrator.py::PipelineOrchestrator` (refactor: Become a compatibility facade over the coordinator.)
  * Epic boundary: Explicit lifecycle state machines, attempts, and fencing — Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.
  * Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-004 requires: Current mutable status fields do not define legal transitions, attempts, fencing, immutable terminal truth, or stale-result behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Apply state changes through one coordinator path that compares expected state/version, advances fencing authority, and records the transition atomically.
  * Component dispositions: `atlas/core/lifecycle.py::LifecycleCoordinator` (create: Own authoritative transition commands.); `atlas/persistence/repositories/transitions.py` (create: Perform compare-and-set mutations.); `atlas/core/orchestrator.py::PipelineOrchestrator` (refactor: Become a compatibility facade over the coordinator.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Implement transition commands with expected state/version, actor, reason, correlation, and required evidence references.
  * Issue monotonically changing fencing tokens or equivalent lease epochs when execution authority changes.
  * Atomically update canonical state and transition sequence; event atomicity is completed in E8.
  * Reject stale, duplicate, out-of-order, or unauthorized transition requests with stable reason codes.

  Security and safety requirements

  * Only coordinator/service identities authorized by the core can call mutation repositories.
  * Treat all adapter, worker, plugin, and user-supplied state values as requests, never direct mutations.
  * Fencing values are unpredictable or integrity-protected where remote trust will later matter.
  * Rejected transitions are auditable without exposing secrets.

  Edge cases and outliers to handle

  * Two processes attempt the same transition.
  * Lease expires while a result is in flight.
  * Cancellation races with success commit.
  * Database retry replays a transition command.

  Acceptance criteria (“done” definition)

  * Every transition requires the expected current state/version and fails deterministically when stale.
  * Stale fencing tokens cannot commit result or terminal state.
  * Concurrent transition tests produce one winner and auditable losers.
  * No production code mutates lifecycle status fields outside the coordinator/repository path.

  Testing plan

  * Compare-and-set unit tests.
  * Concurrent process race tests.
  * Stale fencing-result tests.
  * Cancellation-versus-success race tests.
  * Idempotent command replay tests.
  * Static direct-mutation guard.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Compare-and-set unit tests., Concurrent process race tests., Stale fencing-result tests., Cancellation-versus-success race tests., Idempotent command replay tests., Static direct-mutation guard..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T5.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/lifecycle.py::LifecycleCoordinator, atlas/persistence/repositories/transitions.py, atlas/core/orchestrator.py::PipelineOrchestrator.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 20: Add model-based state-machine and invalid-transition verification

  1.2 source task(s): `T5.1.4`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T5.1.2, T5.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/state_machine/ (create); tests/fixtures/state_sequences/ (create); atlas diagnostics transition errors (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prove the transition system under generated sequences, concurrency, restart, and malformed input rather than relying only on hand-picked happy paths.
  * Restore or protect this invariant: Model and implementation agree across the declared generated sequence budget.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-004; REQ-014..REQ-017; PDF:p.14-15.

  Where this applies

  * Primary affected components: `tests/state_machine/` (create: Host model-based and property tests.); `tests/fixtures/state_sequences/` (create: Store minimized regression sequences.); `atlas diagnostics transition errors` (extend: Expose stable state/version/fencing context.)
  * Epic boundary: Explicit lifecycle state machines, attempts, and fencing — Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-004: Implement explicit Job, Phase, Attempt, and control transition guards; evidence: REQ-014–REQ-017; GAP-007, GAP-008; state reconstruction in Sections 3 and 10.
  * Canonical proposed files/interfaces: Create `atlas/models/states.py`, `atlas/core/lifecycle.py`; refactor `atlas/core/orchestrator.py`; add migrations/tables for phase runs and attempts. / `JobState`, `PhaseState`, `AttemptState`, `ControlRequestState`, `TransitionCommand`, `TransitionResult`, `TransitionError(code, current, requested)`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-004 requires: Current mutable status fields do not define legal transitions, attempts, fencing, immutable terminal truth, or stale-result behavior.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prove the transition system under generated sequences, concurrency, restart, and malformed input rather than relying only on hand-picked happy paths.
  * Component dispositions: `tests/state_machine/` (create: Host model-based and property tests.); `tests/fixtures/state_sequences/` (create: Store minimized regression sequences.); `atlas diagnostics transition errors` (extend: Expose stable state/version/fencing context.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Build a reference model for job, phase, attempt, and control transitions.
  * Generate valid and invalid command sequences, compare implementation state to the model, and minimize failures.
  * Inject cancellation, process loss, duplicate commands, stale results, and storage faults at transition boundaries.
  * Retain counterexample sequences and transition histories as regression fixtures.

  Security and safety requirements

  * Generated tests must remain bounded in steps, state size, and runtime.
  * Do not include raw source payloads in counterexample artifacts.
  * Malformed actor/correlation/state data is rejected before mutation.
  * A diagnostics failure cannot change transition outcome.

  Edge cases and outliers to handle

  * Long valid sequence with repeated pause/resume/retry.
  * Invalid transition from every terminal state.
  * Crash between attempt result and phase/job propagation.
  * Version skew in serialized state or command.

  Acceptance criteria (“done” definition)

  * Model and implementation agree across the declared generated sequence budget.
  * Every illegal transition class has a stable error code and zero authoritative mutation.
  * Counterexamples are reproducible and retained.
  * State-machine tests run in mandatory CI without unapproved skips.

  Testing plan

  * Property-based transition sequence tests.
  * Concurrency and compare-and-set tests.
  * Crash/restart fault injection.
  * Malformed command fuzz tests.
  * Version-skew serialization tests.
  * Regression replay of minimized counterexamples.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Property-based transition sequence tests., Concurrency and compare-and-set tests., Crash/restart fault injection., Malformed command fuzz tests., Version-skew serialization tests., Regression replay of minimized counterexamples..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T5.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/state_machine/, tests/fixtures/state_sequences/, atlas diagnostics transition errors.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 21: Define `SourceRoot`, `IntakeGeneration`, and `ArtifactOccurrence` schemas

  1.2 source task(s): `T6.1.1`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T4.1.4, T5.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/models.py::SourceRoot (create); atlas/artifacts/models.py::IntakeGeneration (create); atlas/artifacts/models.py::ArtifactOccurrence (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create typed, versioned records that separate registered source authority, one observation generation, and each location/type observed under that generation.
  * Restore or protect this invariant: Occurrence and content concepts remain structurally distinct.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/models.py::SourceRoot` (create: Represent stable source identity and provider locator.); `atlas/artifacts/models.py::IntakeGeneration` (create: Represent BUILDING/ACCEPTED/FAILED/BLOCKED observations.); `atlas/artifacts/models.py::ArtifactOccurrence` (create: Represent source-relative observed entries and decisions.)
  * Epic boundary: Registered sources and immutable intake generations — Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]
  * Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-005 requires: Downstream phases currently rediscover mutable sources, so a job has no immutable occurrence set or completeness decision.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create typed, versioned records that separate registered source authority, one observation generation, and each location/type observed under that generation.
  * Component dispositions: `atlas/artifacts/models.py::SourceRoot` (create: Represent stable source identity and provider locator.); `atlas/artifacts/models.py::IntakeGeneration` (create: Represent BUILDING/ACCEPTED/FAILED/BLOCKED observations.); `atlas/artifacts/models.py::ArtifactOccurrence` (create: Represent source-relative observed entries and decisions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define stable IDs, provider type, normalized locator, allowed-root policy, generation state, manifest digest, traversal policy digest, and timestamps.
  * Define occurrence relative path, entry type, size, mode, timestamps, device/inode where available, link/special status, exclusion/error reason, and observation sequence.
  * Define uniqueness, foreign keys, immutability, and supersession relationships.
  * Publish serialization/schema versions and authority classification for each field.

  Security and safety requirements

  * Do not store arbitrary absolute paths as downstream artifact identity.
  * Canonical locators and relative paths are validated separately from byte identity.
  * Sensitive source names can be redacted in telemetry while canonical records remain protected.
  * Provider-specific metadata cannot grant filesystem authority.

  Edge cases and outliers to handle

  * Case-insensitive path collisions and Unicode normalization variants.
  * Dangling links, sockets, devices, FIFOs, inaccessible entries.
  * Source root is renamed, remounted, or points to a different object.
  * Provider lacks inode/device semantics.

  Acceptance criteria (“done” definition)

  * Occurrence and content concepts remain structurally distinct.
  * Every occurrence belongs to exactly one generation and one source root.
  * Accepted generation records are immutable and supersession is explicit.
  * Schema supports local filesystem now without claiming unsupported provider semantics.

  Testing plan

  * Schema and serialization unit tests.
  * Uniqueness/FK negative tests.
  * Case/Unicode collision fixtures.
  * Provider-capability compatibility tests.
  * Immutability/supersession tests.
  * Migration round-trip tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Schema and serialization unit tests., Uniqueness/FK negative tests., Case/Unicode collision fixtures., Provider-capability compatibility tests., Immutability/supersession tests., Migration round-trip tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T6.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/models.py::SourceRoot, atlas/artifacts/models.py::IntakeGeneration, atlas/artifacts/models.py::ArtifactOccurrence.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 22: Implement bounded deterministic intake traversal

  1.2 source task(s): `T6.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T6.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/intake/service.py::IntakeGenerationBuilder (create); atlas/safety/filesystem_discovery.py (refactor); atlas/phases/reconnaissance.py (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Build a generation in `BUILDING`, enumerate source-relative occurrences in deterministic order, and persist every accepted, skipped, excluded, or failed observation under explicit budgets.
  * Restore or protect this invariant: Traversal order and accepted manifest input are deterministic for a stable source.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31.

  Where this applies

  * Primary affected components: `atlas/intake/service.py::IntakeGenerationBuilder` (create: Own generation construction and traversal.); `atlas/safety/filesystem_discovery.py` (refactor: Provide bounded observation primitives.); `atlas/phases/reconnaissance.py` (refactor: Delegate to IntakeGenerationBuilder.)
  * Epic boundary: Registered sources and immutable intake generations — Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]
  * Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-005 requires: Downstream phases currently rediscover mutable sources, so a job has no immutable occurrence set or completeness decision.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Build a generation in `BUILDING`, enumerate source-relative occurrences in deterministic order, and persist every accepted, skipped, excluded, or failed observation under explicit budgets.
  * Component dispositions: `atlas/intake/service.py::IntakeGenerationBuilder` (create: Own generation construction and traversal.); `atlas/safety/filesystem_discovery.py` (refactor: Provide bounded observation primitives.); `atlas/phases/reconnaissance.py` (refactor: Delegate to IntakeGenerationBuilder.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Resolve a registered root, snapshot policy/capabilities, create a BUILDING generation, and enumerate entries in deterministic relative-path order.
  * Persist occurrence candidates incrementally with traversal sequence, exclusion/error reason, and resource counters.
  * Enforce entry, depth, byte-metadata, elapsed-time, and error-policy budgets without unbounded memory.
  * Checkpoint traversal position only where deterministic resume can be proven.

  Security and safety requirements

  * Default no symlink follow and no mount crossing until policy explicitly allows a safe mode.
  * Never descend through special files or paths that fail canonical containment.
  * Bound directory fan-out, path length, error retention, and progress event volume.
  * Do not treat permission denial or traversal truncation as an empty successful source.

  Edge cases and outliers to handle

  * Millions of entries and deeply nested directories.
  * Directory mutates while being traversed.
  * Unreadable child after earlier entries were persisted.
  * Duplicate/colliding relative paths from platform normalization.

  Acceptance criteria (“done” definition)

  * Traversal order and accepted manifest input are deterministic for a stable source.
  * Every skipped/error entry has a persisted reason and no silent omission.
  * Budget exhaustion yields BLOCKED or FAILED, not ACCEPTED.
  * Memory use is bounded independently of total entry count.

  Testing plan

  * Small/empty/deep/wide tree integration tests.
  * Million-entry synthetic benchmark.
  * Mutation-during-traversal tests.
  * Permission and special-file negative tests.
  * Budget exhaustion tests.
  * Deterministic ordering/property tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Small/empty/deep/wide tree integration tests., Million-entry synthetic benchmark., Mutation-during-traversal tests., Permission and special-file negative tests., Budget exhaustion tests., Deterministic ordering/property tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T6.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/intake/service.py::IntakeGenerationBuilder, atlas/safety/filesystem_discovery.py, atlas/phases/reconnaissance.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 23: Implement generation acceptance, manifest digests, and supersession

  1.2 source task(s): `T6.1.3`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T6.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/intake/service.py::accept_generation (create); atlas/persistence/repositories/intake.py (create); atlas/events intake events (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Turn a complete BUILDING generation into an immutable ACCEPTED observation only after completeness, policy, and budget checks pass, with deterministic digest and explicit failure states.
  * Restore or protect this invariant: Only complete generations reach ACCEPTED.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31.

  Where this applies

  * Primary affected components: `atlas/intake/service.py::accept_generation` (create: Own acceptance and manifest hashing.); `atlas/persistence/repositories/intake.py` (create: Persist generation state and occurrence sets.); `atlas/events intake events` (extend: Record accepted/failed/blocked/superseded outcomes.)
  * Epic boundary: Registered sources and immutable intake generations — Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]
  * Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-005 requires: Downstream phases currently rediscover mutable sources, so a job has no immutable occurrence set or completeness decision.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Turn a complete BUILDING generation into an immutable ACCEPTED observation only after completeness, policy, and budget checks pass, with deterministic digest and explicit failure states.
  * Component dispositions: `atlas/intake/service.py::accept_generation` (create: Own acceptance and manifest hashing.); `atlas/persistence/repositories/intake.py` (create: Persist generation state and occurrence sets.); `atlas/events intake events` (extend: Record accepted/failed/blocked/superseded outcomes.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Compute a canonical manifest over ordered occurrence records and policy/config versions.
  * Validate traversal completeness, unresolved errors, budgets, source guard, and required entry classes before acceptance.
  * Atomically transition BUILDING to ACCEPTED/FAILED/BLOCKED with reason and durable event hook.
  * Create explicit superseding generation relationships when a new observation is requested.

  Security and safety requirements

  * Manifest serialization must be canonical and collision-resistant.
  * No caller may force ACCEPTED after a partial or failed traversal.
  * Rejection reasons are bounded and redacted without losing machine-readable codes.
  * Accepted records cannot be mutated in place.

  Edge cases and outliers to handle

  * Zero regular files but valid directories or metadata-only sources.
  * Source changes after last occurrence but before acceptance.
  * Process crashes while computing digest or transitioning state.
  * Duplicate acceptance request is replayed.

  Acceptance criteria (“done” definition)

  * Only complete generations reach ACCEPTED.
  * Equivalent stable observations yield the same manifest digest.
  * Duplicate acceptance is idempotent and conflicting acceptance fails.
  * Supersession preserves both generations and lineage.

  Testing plan

  * Canonical manifest golden tests.
  * Acceptance-guard truth-table tests.
  * Crash-at-acceptance fault injection.
  * Duplicate/idempotent acceptance tests.
  * Source-change boundary tests.
  * Supersession lineage tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Canonical manifest golden tests., Acceptance-guard truth-table tests., Crash-at-acceptance fault injection., Duplicate/idempotent acceptance tests., Source-change boundary tests., Supersession lineage tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T6.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/intake/service.py::accept_generation, atlas/persistence/repositories/intake.py, atlas/events intake events.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 24: Make all downstream phases consume accepted occurrence IDs only

  1.2 source task(s): `T6.1.4`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T6.1.2, T6.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/phases/fingerprinting.py (refactor); atlas/phases/structural_discovery.py (refactor); atlas/phases/extraction.py and analysis.py (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Remove independent source rediscovery from Fingerprinting and later stages so the accepted generation is the sole occurrence authority.
  * Restore or protect this invariant: Static/runtime guards find no unauthorized downstream source enumeration.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31.

  Where this applies

  * Primary affected components: `atlas/phases/fingerprinting.py` (refactor: Read accepted occurrences rather than traverse live source.); `atlas/phases/structural_discovery.py` (refactor: Resolve content through occurrence/content records.); `atlas/phases/extraction.py and analysis.py` (refactor: Reject arbitrary source paths after intake.)
  * Epic boundary: Registered sources and immutable intake generations — Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-005: Introduce SourceRoot and accepted IntakeGeneration records; evidence: GAP-001, GAP-004, REQ-003, REQ-014; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/reconnaissance.py:L20-L111]
  * Canonical proposed files/interfaces: Create `atlas/intake/service.py`, `atlas/artifacts/models.py`; refactor `atlas/phases/reconnaissance.py`, `atlas/safety/filesystem_discovery.py`; add persistence migrations. / `SourceRoot`, `IntakeGeneration`, `ArtifactOccurrenceCandidate`, `IntakePolicy`, `IntakeAcceptanceResult`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-005 requires: Downstream phases currently rediscover mutable sources, so a job has no immutable occurrence set or completeness decision.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Remove independent source rediscovery from Fingerprinting and later stages so the accepted generation is the sole occurrence authority.
  * Component dispositions: `atlas/phases/fingerprinting.py` (refactor: Read accepted occurrences rather than traverse live source.); `atlas/phases/structural_discovery.py` (refactor: Resolve content through occurrence/content records.); `atlas/phases/extraction.py and analysis.py` (refactor: Reject arbitrary source paths after intake.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Change phase inputs to `intake_generation_id` and occurrence/content references.
  * Add guards that reject non-ACCEPTED generations, foreign-job occurrences, stale/superseded generations, and arbitrary absolute paths.
  * Remove or isolate legacy re-traversal behavior behind a temporary compatibility test-only adapter.
  * Add source-mutation tests proving downstream phases do not silently substitute a new occurrence set.

  Security and safety requirements

  * No built-in phase may enumerate a source root after intake acceptance.
  * Plugins receive mediated content or workspace references, never source root authority.
  * Generation supersession requires an explicit new job/policy path, not silent switching.
  * Audit every direct walk/glob/rglob use in phase code.

  Edge cases and outliers to handle

  * Occurrence deleted before fingerprinting.
  * Generation is superseded while job is queued.
  * Legacy caller supplies a path instead of occurrence ID.
  * Occurrence refers to a special or excluded entry.

  Acceptance criteria (“done” definition)

  * Static/runtime guards find no unauthorized downstream source enumeration.
  * Fingerprinting consumes exactly the accepted occurrence set.
  * Deleted/mutated occurrences produce deterministic stale/missing outcomes.
  * Compatibility behavior is documented and time-bounded.

  Testing plan

  * Phase input contract tests.
  * Static search/lint for direct traversal calls.
  * Source deletion/mutation integration tests.
  * Foreign-generation ID negative tests.
  * Supersession race tests.
  * Legacy adapter compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Phase input contract tests., Static search/lint for direct traversal calls., Source deletion/mutation integration tests., Foreign-generation ID negative tests., Supersession race tests., Legacy adapter compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T6.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/phases/fingerprinting.py, atlas/phases/structural_discovery.py, atlas/phases/extraction.py and analysis.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 25: Define `ContentIdentity` and occurrence-to-content link contracts

  1.2 source task(s): `T7.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T6.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/models.py::ContentIdentity (create); atlas/artifacts/models.py::OccurrenceContentLink (create); content_identities and occurrence_content_links migrations (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create immutable canonical content IDs and explicit observation links without implying that a retained blob exists.
  * Restore or protect this invariant: Identical bytes converge on one persistent SHA-256 identity across processes.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/models.py::ContentIdentity` (create: Represent algorithm, digest, size, and verification metadata.); `atlas/artifacts/models.py::OccurrenceContentLink` (create: Bind an occurrence read to exact content and read evidence.); `content_identities and occurrence_content_links migrations` (create: Persist cross-run identity.)
  * Epic boundary: Persistent content identity and occurrence linkage — Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]
  * Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-006 requires: Current hashes are process-local and disconnected from accepted occurrences, preventing cross-run deduplication and exact-byte lineage.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create immutable canonical content IDs and explicit observation links without implying that a retained blob exists.
  * Component dispositions: `atlas/artifacts/models.py::ContentIdentity` (create: Represent algorithm, digest, size, and verification metadata.); `atlas/artifacts/models.py::OccurrenceContentLink` (create: Bind an occurrence read to exact content and read evidence.); `content_identities and occurrence_content_links migrations` (create: Persist cross-run identity.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define canonical `sha256:<hex>` identity, byte count, optional secondary hash, first/last verification, and integrity status.
  * Define occurrence link fields for read start/end metadata, mutation result, capture status, config/algorithm version, and attempt.
  * Enforce many occurrences to one identity, one successful identity per occurrence/read attempt, and immutable digest values.
  * Separate identity existence from blob retention and replayability.

  Security and safety requirements

  * SHA-256 is canonical; optional BLAKE3 is acceleration/cross-check only and cannot replace canonical identity without a new versioned decision.
  * Digest parsing is strict and constant-format; reject malformed or ambiguous encodings.
  * No path, filename, timestamp, or size alone is treated as content identity.
  * Integrity incidents are explicit states, not overwritten records.

  Edge cases and outliers to handle

  * Empty file, sparse file, huge file, hard links, duplicate bytes at many paths.
  * Same path observed with different bytes in later generations.
  * Secondary hash unavailable or mismatched.
  * Legacy `HashStore` key format differs.

  Acceptance criteria (“done” definition)

  * Identical bytes converge on one persistent SHA-256 identity across processes.
  * All occurrences remain independently traceable to the shared identity.
  * Identity records do not falsely claim retained bytes.
  * Malformed or conflicting digest records fail integrity checks.

  Testing plan

  * Model/schema unit tests.
  * Many-occurrence-one-content tests.
  * Cross-process/restart persistence tests.
  * Digest parser and malformed-value fuzz tests.
  * Empty/sparse/large-file fixtures.
  * Legacy identity compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Model/schema unit tests., Many-occurrence-one-content tests., Cross-process/restart persistence tests., Digest parser and malformed-value fuzz tests., Empty/sparse/large-file fixtures., Legacy identity compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T7.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/models.py::ContentIdentity, atlas/artifacts/models.py::OccurrenceContentLink, content_identities and occurrence_content_links migrations.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 26: Implement race-aware streaming hashing from accepted occurrences

  1.2 source task(s): `T7.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T7.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/identity.py::ContentIdentityService (create); atlas/storage/hash_store.py::HashStore (refactor); atlas/phases/fingerprinting.py (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Open each accepted regular-file occurrence through the canonical access boundary, verify handle metadata, stream bytes, and recheck mutation before attaching content identity.
  * Restore or protect this invariant: Stable inputs produce the expected SHA-256 and link evidence.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/identity.py::ContentIdentityService` (create: Own hashing and identity persistence.); `atlas/storage/hash_store.py::HashStore` (refactor: Delegate hashing while preserving facade behavior.); `atlas/phases/fingerprinting.py` (refactor: Use occurrence IDs and identity service.)
  * Epic boundary: Persistent content identity and occurrence linkage — Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]
  * Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-006 requires: Current hashes are process-local and disconnected from accepted occurrences, preventing cross-run deduplication and exact-byte lineage.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Open each accepted regular-file occurrence through the canonical access boundary, verify handle metadata, stream bytes, and recheck mutation before attaching content identity.
  * Component dispositions: `atlas/artifacts/identity.py::ContentIdentityService` (create: Own hashing and identity persistence.); `atlas/storage/hash_store.py::HashStore` (refactor: Delegate hashing while preserving facade behavior.); `atlas/phases/fingerprinting.py` (refactor: Use occurrence IDs and identity service.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Resolve occurrence through SourceAccess, open no-follow/handle-relative where available, and compare pre-read handle metadata to the occurrence record.
  * Stream SHA-256 in bounded chunks while recording bytes read, progress, and optional capture sink.
  * Recheck handle/path-relevant metadata after read and classify stable, stale, disappeared, or indeterminate.
  * Persist identity and occurrence link atomically only when read evidence satisfies policy.

  Security and safety requirements

  * Never follow a swapped symlink or reopen by path after verification.
  * Limit chunk buffers, elapsed time, and read bytes according to resource policy.
  * Do not attach a digest when read was partial, truncated, or mutation status is unsafe.
  * Error/log output does not expose file content.

  Edge cases and outliers to handle

  * File changes size without inode change.
  * File is replaced or unlinked while handle remains open.
  * Short read, I/O error, sparse region, or permission revocation.
  * Platform lacks strong handle-relative/stat comparison.

  Acceptance criteria (“done” definition)

  * Stable inputs produce the expected SHA-256 and link evidence.
  * Mutation cannot attach the wrong identity to an occurrence.
  * Partial or indeterminate reads never appear successful.
  * Progress remains bounded and durable through the PhaseContext contract.

  Testing plan

  * Known-hash golden tests.
  * Barrier-controlled mutation/replacement tests.
  * Large/sparse/short-read tests.
  * Platform capability fallback tests.
  * Partial-read and I/O fault injection.
  * Cross-process persistence tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Known-hash golden tests., Barrier-controlled mutation/replacement tests., Large/sparse/short-read tests., Platform capability fallback tests., Partial-read and I/O fault injection., Cross-process persistence tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T7.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/identity.py::ContentIdentityService, atlas/storage/hash_store.py::HashStore, atlas/phases/fingerprinting.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 27: Add persistent cross-run duplicate lookup and processing-reuse eligibility

  1.2 source task(s): `T7.1.3`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T7.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/identity.py::lookup_content (extend); atlas/persistence/repositories/content.py (create); atlas/phases/fingerprinting.py result contract (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Use content identity to recognize prior bytes while retaining occurrence provenance and deciding explicitly whether downstream work is eligible for reuse.
  * Restore or protect this invariant: A restart recognizes previously seen content without recomputing downstream identity state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/identity.py::lookup_content` (extend: Query persistent identities and occurrence history.); `atlas/persistence/repositories/content.py` (create: Provide indexed identity and link queries.); `atlas/phases/fingerprinting.py result contract` (extend: Report new, known, stale, and capture status.)
  * Epic boundary: Persistent content identity and occurrence linkage — Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]
  * Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-006 requires: Current hashes are process-local and disconnected from accepted occurrences, preventing cross-run deduplication and exact-byte lineage.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Use content identity to recognize prior bytes while retaining occurrence provenance and deciding explicitly whether downstream work is eligible for reuse.
  * Component dispositions: `atlas/artifacts/identity.py::lookup_content` (extend: Query persistent identities and occurrence history.); `atlas/persistence/repositories/content.py` (create: Provide indexed identity and link queries.); `atlas/phases/fingerprinting.py result contract` (extend: Report new, known, stale, and capture status.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Create indexed lookup by canonical digest and size with integrity verification.
  * Return prior occurrence count, retention/replayability state, and compatible downstream result candidates without auto-reusing them.
  * Record every new occurrence even when content is already known.
  * Expose a deterministic eligibility signal consumed later by the result-reuse service.

  Security and safety requirements

  * Deduplication cannot erase source, time, case, or intake provenance.
  * A prior integrity incident or unverified blob disables automatic reuse.
  * Do not trust digest claims from plugins or external callers without core verification.
  * Query responses are bounded and paginated for high-occurrence content.

  Edge cases and outliers to handle

  * Millions of occurrences reference one common content identity.
  * Identity exists but retained blob is missing or corrupt.
  * Content was previously analyzed under incompatible config/plugin versions.
  * Digest collision or database corruption is detected.

  Acceptance criteria (“done” definition)

  * A restart recognizes previously seen content without recomputing downstream identity state.
  * Every duplicate occurrence is persisted and queryable.
  * Reuse eligibility is false unless exact downstream keys and integrity requirements are satisfied.
  * High-occurrence queries remain bounded and indexed.

  Testing plan

  * Cross-run duplicate integration tests.
  * High-cardinality occurrence query benchmark.
  * Missing/corrupt blob eligibility tests.
  * Incompatible result-key tests.
  * Integrity incident negative tests.
  * Query pagination and index-plan tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Cross-run duplicate integration tests., High-cardinality occurrence query benchmark., Missing/corrupt blob eligibility tests., Incompatible result-key tests., Integrity incident negative tests., Query pagination and index-plan tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T7.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/identity.py::lookup_content, atlas/persistence/repositories/content.py, atlas/phases/fingerprinting.py result contract.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 28: Preserve `HashStore` compatibility while removing process-local authority

  1.2 source task(s): `T7.1.4`
  Priority: `P0`
  Estimated effort: `10 hours`
  Dependencies: `T7.1.2, T7.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/storage/hash_store.py::HashStore (refactor); atlas/storage/__init__.py (extend); tests/compatibility/test_hash_store_v0_1.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Keep existing imports and expected `has_content` behavior as a facade over persistent identity without allowing the legacy in-memory manifest to remain authoritative.
  * Restore or protect this invariant: Supported legacy calls return documented equivalent results from persistent state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/storage/hash_store.py::HashStore` (refactor: Delegate to ContentIdentityService and StateStore.); `atlas/storage/__init__.py` (extend: Preserve supported public imports and deprecations.); `tests/compatibility/test_hash_store_v0_1.py` (create: Pin legacy behavior and migration.)
  * Epic boundary: Persistent content identity and occurrence linkage — Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-006: Persist occurrence-to-content identity using canonical SHA-256; evidence: GAP-004, GAP-005, REQ-004, REQ-005; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/storage/hash_store.py:L34-L63]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/fingerprinting.py:L20-L136]
  * Canonical proposed files/interfaces: Create/extend `atlas/artifacts/models.py`, `atlas/artifacts/hasher.py`; refactor `atlas/storage/hash_store.py`, `atlas/phases/fingerprinting.py`; migrations. / `ContentIdentity`, `OccurrenceContentBinding`, `HashObservation`, `Hasher` protocol; compatibility `HashStore` facade.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-006 requires: Current hashes are process-local and disconnected from accepted occurrences, preventing cross-run deduplication and exact-byte lineage.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Keep existing imports and expected `has_content` behavior as a facade over persistent identity without allowing the legacy in-memory manifest to remain authoritative.
  * Component dispositions: `atlas/storage/hash_store.py::HashStore` (refactor: Delegate to ContentIdentityService and StateStore.); `atlas/storage/__init__.py` (extend: Preserve supported public imports and deprecations.); `tests/compatibility/test_hash_store_v0_1.py` (create: Pin legacy behavior and migration.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Inventory public methods, constructors, return types, examples, and tests that depend on HashStore.
  * Implement facade calls using persistent identity repositories and explicit async/runtime ownership.
  * Emit deprecation guidance for storage semantics that were previously overstated.
  * Remove or constrain process-local caches to non-authoritative performance hints with invalidation.

  Security and safety requirements

  * A cache miss cannot be interpreted as identity absence without consulting the store.
  * Do not expose raw database or source access through the facade.
  * Compatibility logs avoid paths/content and are rate-limited.
  * Old behavior that falsely implied CAS is corrected in docs and telemetry.

  Edge cases and outliers to handle

  * HashStore used before runtime connection.
  * Multiple runtimes share the same database.
  * Legacy caller expects synchronous access.
  * Cache contains stale result after migration or process fork.

  Acceptance criteria (“done” definition)

  * Supported legacy calls return documented equivalent results from persistent state.
  * No in-memory manifest is authoritative after migration.
  * Deprecated semantics produce actionable warnings and migration docs.
  * Compatibility tests cover restart and multiple-runtime cases.

  Testing plan

  * Public import/API compatibility tests.
  * Restart and multi-runtime tests.
  * Cache invalidation tests.
  * Pre-connect and lifecycle error tests.
  * Documentation example tests.
  * Deprecation telemetry/redaction tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Public import/API compatibility tests., Restart and multi-runtime tests., Cache invalidation tests., Pre-connect and lifecycle error tests., Documentation example tests., Deprecation telemetry/redaction tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T7.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/storage/hash_store.py::HashStore, atlas/storage/__init__.py, tests/compatibility/test_hash_store_v0_1.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 29: Define versioned durable event and outbox schemas

  1.2 source task(s): `T8.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T4.1.4, T5.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/models.py::DurableEvent (create); atlas/events/models.py::OutboxRecord (create); events and outbox migrations (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify immutable event identity, ordering, correlation, causation, entity references, payload versions, and transport intent separately from authoritative state.
  * Restore or protect this invariant: Every required transition event has a stable typed schema and entity references.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23.

  Where this applies

  * Primary affected components: `atlas/events/models.py::DurableEvent` (create: Own event envelope and typed payload references.); `atlas/events/models.py::OutboxRecord` (create: Represent delivery intent and status.); `events and outbox migrations` (create: Persist immutable history and dispatch state.)
  * Epic boundary: Durable events and transactional outbox — Persist required lifecycle history atomically with authoritative state and project it to transports without making messaging a second authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]
  * Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-007 requires: Current publish-then-persist behavior can commit authoritative state without durable evidence and treats RabbitMQ as an ambiguous side channel.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify immutable event identity, ordering, correlation, causation, entity references, payload versions, and transport intent separately from authoritative state.
  * Component dispositions: `atlas/events/models.py::DurableEvent` (create: Own event envelope and typed payload references.); `atlas/events/models.py::OutboxRecord` (create: Represent delivery intent and status.); `events and outbox migrations` (create: Persist immutable history and dispatch state.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define event ID, local sequence, schema version, class, occurred/recorded times, correlation/causation IDs, actor, job/phase/attempt/work/content IDs, and typed payload.
  * Define which transitions require durable events and which high-volume observations remain current-state-only or sampled history.
  * Define outbox destination, delivery key, status, attempts, next attempt, and terminal/dead-letter fields.
  * Publish compatibility and evolution rules for event envelopes and payload schemas.

  Security and safety requirements

  * Event payloads contain references and bounded summaries, not artifact bytes, secrets, or arbitrary untrusted text.
  * Event IDs and sequence are generated by the core, not external callers.
  * Unknown payload versions remain queryable but cannot be interpreted as commands.
  * Transport routing metadata cannot alter lifecycle authority.

  Edge cases and outliers to handle

  * Clock moves backward or events are recorded after occurrence time.
  * One transaction emits several ordered events.
  * Payload schema is newer than a consumer.
  * High-volume progress would exceed storage/backlog budgets.

  Acceptance criteria (“done” definition)

  * Every required transition event has a stable typed schema and entity references.
  * Local sequence establishes deterministic within-store ordering.
  * Outbox state is distinct from event history and transport-specific payload.
  * Event evolution rules preserve old history and reject unsafe downgrade.

  Testing plan

  * Schema and serialization tests.
  * Sequence/ordering tests.
  * Unknown-version compatibility tests.
  * Payload size/redaction tests.
  * Correlation/causation integrity tests.
  * Migration round-trip tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Schema and serialization tests., Sequence/ordering tests., Unknown-version compatibility tests., Payload size/redaction tests., Correlation/causation integrity tests., Migration round-trip tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T8.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/models.py::DurableEvent, atlas/events/models.py::OutboxRecord, events and outbox migrations.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 30: Record state transitions, durable events, and outbox rows atomically

  1.2 source task(s): `T8.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T8.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/recorder.py::DurableEventRecorder (create); atlas/core/lifecycle.py (extend); atlas/core/job_store.py::store_event (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make one StateStore transaction commit the authoritative mutation, required history event, and transport intent or commit none of them.
  * Restore or protect this invariant: Fault injection at every transaction step yields all-or-nothing state/history/outbox.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23.

  Where this applies

  * Primary affected components: `atlas/events/recorder.py::DurableEventRecorder` (create: Build and append required events inside caller transactions.); `atlas/core/lifecycle.py` (extend: Invoke recorder within transition commands.); `atlas/core/job_store.py::store_event` (refactor: Delegate to canonical event repository.)
  * Epic boundary: Durable events and transactional outbox — Persist required lifecycle history atomically with authoritative state and project it to transports without making messaging a second authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]
  * Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-007 requires: Current publish-then-persist behavior can commit authoritative state without durable evidence and treats RabbitMQ as an ambiguous side channel.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Make one StateStore transaction commit the authoritative mutation, required history event, and transport intent or commit none of them.
  * Component dispositions: `atlas/events/recorder.py::DurableEventRecorder` (create: Build and append required events inside caller transactions.); `atlas/core/lifecycle.py` (extend: Invoke recorder within transition commands.); `atlas/core/job_store.py::store_event` (refactor: Delegate to canonical event repository.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Add recorder APIs that require an active StateStore transaction and validated transition context.
  * Allocate local sequence and append event/outbox records before commit.
  * Refactor orchestrator and built-in phases so required detailed events use the recorder rather than transport-only emission.
  * Define behavior when payload construction, event insert, outbox insert, or commit fails.

  Security and safety requirements

  * No state transition commits without its required event.
  * No event claims a transition that rolled back.
  * Event data is validated and bounded before persistence.
  * Transport availability is never checked inside the authoritative transaction except bounded outbox capacity policy.

  Edge cases and outliers to handle

  * Event serialization fails after state row update.
  * Outbox insert violates capacity or constraint.
  * Process dies before/after commit acknowledgement.
  * Duplicate transition command re-enters recorder.

  Acceptance criteria (“done” definition)

  * Fault injection at every transaction step yields all-or-nothing state/history/outbox.
  * Every required transition query returns its durable event.
  * Duplicate commands do not create duplicate lifecycle effects.
  * Transport outage cannot corrupt or roll back already-valid state.

  Testing plan

  * Transaction unit tests.
  * Kill/fault injection at state/event/outbox/commit boundaries.
  * Duplicate command/idempotency tests.
  * Detailed phase-event persistence integration tests.
  * Outbox capacity policy tests.
  * Recovery query reconstruction tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Transaction unit tests., Kill/fault injection at state/event/outbox/commit boundaries., Duplicate command/idempotency tests., Detailed phase-event persistence integration tests., Outbox capacity policy tests., Recovery query reconstruction tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T8.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/recorder.py::DurableEventRecorder, atlas/core/lifecycle.py, atlas/core/job_store.py::store_event.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 31: Implement the idempotent outbox dispatcher and delivery backpressure

  1.2 source task(s): `T8.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T8.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/dispatcher.py::OutboxDispatcher (create); atlas/core/event_bus.py (refactor); atlas/events/transports/base.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Project committed events to zero or more transports with at-least-once delivery, stable delivery keys, bounded retry, explicit dead-letter state, and no authority over lifecycle.
  * Restore or protect this invariant: Redelivery creates no duplicate lifecycle effect.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23.

  Where this applies

  * Primary affected components: `atlas/events/dispatcher.py::OutboxDispatcher` (create: Own leasing, delivery, retry, and acknowledgement.); `atlas/core/event_bus.py` (refactor: Retain observer/transport facade only.); `atlas/events/transports/base.py` (create: Define delivery adapter contract.)
  * Epic boundary: Durable events and transactional outbox — Persist required lifecycle history atomically with authoritative state and project it to transports without making messaging a second authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]
  * Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-007 requires: Current publish-then-persist behavior can commit authoritative state without durable evidence and treats RabbitMQ as an ambiguous side channel.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Project committed events to zero or more transports with at-least-once delivery, stable delivery keys, bounded retry, explicit dead-letter state, and no authority over lifecycle.
  * Component dispositions: `atlas/events/dispatcher.py::OutboxDispatcher` (create: Own leasing, delivery, retry, and acknowledgement.); `atlas/core/event_bus.py` (refactor: Retain observer/transport facade only.); `atlas/events/transports/base.py` (create: Define delivery adapter contract.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Lease pending outbox records with fencing, batch limits, delivery keys, and bounded concurrency.
  * Define exponential backoff/jitter, maximum attempts, dead-letter/blocked status, retention, and operator retry controls.
  * Require adapters to report delivered, retryable failure, permanent failure, or unknown outcome.
  * Expose backlog age/size and explicit degraded behavior when limits are reached.

  Security and safety requirements

  * Dispatcher cannot mutate job/phase/attempt state or interpret payloads as commands.
  * Delivery keys and signatures prevent accidental duplicate consumer effects where supported.
  * Untrusted broker errors and acknowledgements are validated and bounded.
  * Dead-letter records retain provenance without leaking payload secrets.

  Edge cases and outliers to handle

  * Broker accepts message but acknowledgement is lost.
  * Dispatcher crashes after send before marking delivered.
  * One poison event blocks a batch.
  * Backlog exceeds count, bytes, or age thresholds.

  Acceptance criteria (“done” definition)

  * Redelivery creates no duplicate lifecycle effect.
  * A poison event is isolated and does not starve later records.
  * Backlog limits produce documented block/degrade behavior and diagnostics.
  * Disabling all transports leaves core execution correct.

  Testing plan

  * Dispatcher lease/fencing tests.
  * Lost-ack and duplicate-delivery tests.
  * Poison/dead-letter tests.
  * Backoff/jitter deterministic tests.
  * Backlog saturation/load tests.
  * Transport-disabled integration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Dispatcher lease/fencing tests., Lost-ack and duplicate-delivery tests., Poison/dead-letter tests., Backoff/jitter deterministic tests., Backlog saturation/load tests., Transport-disabled integration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T8.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/dispatcher.py::OutboxDispatcher, atlas/core/event_bus.py, atlas/events/transports/base.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 32: Define progress-event sampling, retention, replay, and event diagnostics

  1.2 source task(s): `T8.1.4`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T8.1.2, T8.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/policy.py (create); atlas/events/queries.py (create); atlas diagnostics events (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prevent progress and analyzer chatter from overwhelming durable history while preserving current progress authority and enough evidence for reconstruction.
  * Restore or protect this invariant: Current progress remains exact within defined update semantics even when history is sampled.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-007; REQ-013,REQ-024; PDF:p.10,p.13,p.18,p.23.

  Where this applies

  * Primary affected components: `atlas/events/policy.py` (create: Own event class durability, sampling, coalescing, and retention policy.); `atlas/events/queries.py` (create: Provide ordered history and replay/export queries.); `atlas diagnostics events` (extend: Expose gaps, backlog, dead letters, and schema versions.)
  * Epic boundary: Durable events and transactional outbox — Persist required lifecycle history atomically with authoritative state and project it to transports without making messaging a second authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-007: Make state transition, event history, and outbox atomic; evidence: GAP-009, GAP-010, REQ-013, REQ-024; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py:L298-L339]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/event_bus.py:L24-L230]
  * Canonical proposed files/interfaces: Create `atlas/events/models.py`, `atlas/events/recorder.py`, `atlas/events/dispatcher.py`; split/refactor `atlas/core/event_bus.py`; migrations. / `DurableEvent`, `EventRecorder`, `OutboxMessage`, `EventDispatcher`, `EventTransport`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-007 requires: Current publish-then-persist behavior can commit authoritative state without durable evidence and treats RabbitMQ as an ambiguous side channel.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prevent progress and analyzer chatter from overwhelming durable history while preserving current progress authority and enough evidence for reconstruction.
  * Component dispositions: `atlas/events/policy.py` (create: Own event class durability, sampling, coalescing, and retention policy.); `atlas/events/queries.py` (create: Provide ordered history and replay/export queries.); `atlas diagnostics events` (extend: Expose gaps, backlog, dead letters, and schema versions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Classify events as required transition, evidentiary, operational, sampled progress, or transport-only.
  * Define coalescing/sampling keyed by entity and interval while persisting current progress separately.
  * Define retention/export rules that never delete authoritative state and preserve audit-critical history.
  * Add replay/export cursors for consumers without replaying events as lifecycle commands.

  Security and safety requirements

  * Sampling cannot drop terminal, rejection, safety, decision, publication, or integrity events.
  * Exports redact secrets and bound payload text.
  * Retention deletion is transactional, auditable, and policy-controlled.
  * Replay offsets are consumer state, not lifecycle state.

  Edge cases and outliers to handle

  * Millions of progress updates for one large job.
  * Consumer offset points to pruned history.
  * Event payload fails schema validation during export.
  * Retention runs while dispatcher is delivering.

  Acceptance criteria (“done” definition)

  * Current progress remains exact within defined update semantics even when history is sampled.
  * Required event classes are never sampled or pruned outside policy.
  * Replay/export detects gaps and schema incompatibility.
  * Event diagnostics identify backlog, dead letters, retention watermark, and sequence gaps.

  Testing plan

  * Sampling/coalescing property tests.
  * Required-event non-drop tests.
  * High-volume progress load tests.
  * Retention/dispatcher concurrency tests.
  * Replay gap and offset tests.
  * Redacted export tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Sampling/coalescing property tests., Required-event non-drop tests., High-volume progress load tests., Retention/dispatcher concurrency tests., Replay gap and offset tests., Redacted export tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T8.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/policy.py, atlas/events/queries.py, atlas diagnostics events.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 33: Define `PhaseContext`, progress, control-request, and checkpoint contracts

  1.2 source task(s): `T9.1.1`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T5.1.4, T8.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/context.py::PhaseContext (create); atlas/models/controls.py (create); atlas/models/checkpoints.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace mutable phase-local state with typed services for durable progress, control polling, checkpoint creation, result writes, and telemetry.
  * Restore or protect this invariant: Contracts distinguish current progress, sampled history, controls, and checkpoints.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28.

  Where this applies

  * Primary affected components: `atlas/core/context.py::PhaseContext` (create: Expose bounded phase services without StateStore authority.); `atlas/models/controls.py` (create: Define ControlRequest and acknowledgement states.); `atlas/models/checkpoints.py` (create: Define versioned checkpoint identity and compatibility fields.)
  * Epic boundary: Durable progress, controls, safe points, and checkpoints — Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.
  * Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-008 requires: Current progress and pause/resume/cancel are process-local; restart repeats phases without verified recovery state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace mutable phase-local state with typed services for durable progress, control polling, checkpoint creation, result writes, and telemetry.
  * Component dispositions: `atlas/core/context.py::PhaseContext` (create: Expose bounded phase services without StateStore authority.); `atlas/models/controls.py` (create: Define ControlRequest and acknowledgement states.); `atlas/models/checkpoints.py` (create: Define versioned checkpoint identity and compatibility fields.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define current progress fields, monotonicity/aggregation rules, update sequence, and history sampling references.
  * Define control request type, requested/applied/rejected states, actor, correlation, idempotency key, reason, and target scope.
  * Define checkpoint phase/operation/input/config/policy/schema versions, cursor, output references, integrity digest, and safe-point class.
  * Specify which PhaseContext methods are transactional, cancellable, and available to built-ins versus plugins.

  Security and safety requirements

  * PhaseContext does not expose raw StateStore, arbitrary filesystem, or lifecycle transition methods.
  * Control actor and scope are validated by CommandService/policy before persistence.
  * Checkpoint payloads contain references and validated cursors, not arbitrary pickled Python objects.
  * Progress and diagnostics are bounded and redact payload-derived text.

  Edge cases and outliers to handle

  * Progress moves backward after retry or phase fan-out.
  * Duplicate control request with same idempotency key but different payload.
  * Checkpoint schema/plugin/config version mismatch.
  * Control targets a terminal or foreign job.

  Acceptance criteria (“done” definition)

  * Contracts distinguish current progress, sampled history, controls, and checkpoints.
  * All serialized records are versioned and digestible.
  * PhaseContext grants no direct lifecycle authority.
  * Safe-point and maximum-control-latency requirements are expressible per phase.

  Testing plan

  * Model/schema unit tests.
  * Progress monotonicity/property tests.
  * Control idempotency and scope tests.
  * Checkpoint serialization/integrity tests.
  * Context capability negative tests.
  * Version-skew compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Model/schema unit tests., Progress monotonicity/property tests., Control idempotency and scope tests., Checkpoint serialization/integrity tests., Context capability negative tests., Version-skew compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T9.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/context.py::PhaseContext, atlas/models/controls.py, atlas/models/checkpoints.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 34: Persist live progress and deterministic job-level projections

  1.2 source task(s): `T9.1.2`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T9.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/repositories/progress.py (create); atlas/phases/base.py::report_progress (refactor); atlas/status/projection.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Write bounded intermediate phase progress to authoritative state and derive job-level progress so independent status clients see real work rather than post-return snapshots.
  * Restore or protect this invariant: A second process observes progress within the documented staleness bound.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28.

  Where this applies

  * Primary affected components: `atlas/persistence/repositories/progress.py` (create: Own current progress and update sequence.); `atlas/phases/base.py::report_progress` (refactor: Delegate through PhaseContext.); `atlas/status/projection.py` (create: Aggregate phase/work-item progress deterministically.)
  * Epic boundary: Durable progress, controls, safe points, and checkpoints — Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.
  * Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-008 requires: Current progress and pause/resume/cancel are process-local; restart repeats phases without verified recovery state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Write bounded intermediate phase progress to authoritative state and derive job-level progress so independent status clients see real work rather than post-return snapshots.
  * Component dispositions: `atlas/persistence/repositories/progress.py` (create: Own current progress and update sequence.); `atlas/phases/base.py::report_progress` (refactor: Delegate through PhaseContext.); `atlas/status/projection.py` (create: Aggregate phase/work-item progress deterministically.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Persist current phase progress with sequence/version, units completed/total/unknown, message code, resource counters, and update time.
  * Define aggregation weights or phase-state-based semantics without presenting false precision.
  * Coalesce writes by time/work threshold while guaranteeing bounded status staleness.
  * Link sampled progress events to authoritative current progress sequence.

  Security and safety requirements

  * Untrusted labels and paths are bounded/redacted before status or logs.
  * A plugin cannot set another phase or job's progress.
  * Progress write failure is classified and cannot silently report success.
  * High-frequency updates are rate-limited without blocking cancellation checks.

  Edge cases and outliers to handle

  * Total work becomes known only after traversal.
  * Retry restarts or resumes from checkpoint.
  * Parallel work items complete out of order.
  * Database contention delays progress writes.

  Acceptance criteria (“done” definition)

  * A second process observes progress within the documented staleness bound.
  * Job-level progress is deterministic and never decreases except by a documented retry-generation reset.
  * Progress write volume remains bounded under million-entry workloads.
  * Terminal state and final progress are mutually consistent.

  Testing plan

  * Progress repository unit tests.
  * Aggregation property tests.
  * Second-process status integration tests.
  * High-frequency load tests.
  * Retry/resume progress tests.
  * Contention and write-failure tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Progress repository unit tests., Aggregation property tests., Second-process status integration tests., High-frequency load tests., Retry/resume progress tests., Contention and write-failure tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T9.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/repositories/progress.py, atlas/phases/base.py::report_progress, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 35: Implement durable control requests and safe-point acknowledgement

  1.2 source task(s): `T9.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T9.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/control_service.py::ControlRequestService (create); atlas/phases/base.py::control_point (extend); atlas/cli.py::pause/resume/cancel (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Turn pause, resume, and cancel into idempotent commands that the active attempt polls and either applies at a declared safe point or rejects with a durable reason.
  * Restore or protect this invariant: A second process can request and observe applied/rejected control state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28.

  Where this applies

  * Primary affected components: `atlas/core/control_service.py::ControlRequestService` (create: Validate and persist control commands.); `atlas/phases/base.py::control_point` (extend: Poll and acknowledge controls through PhaseContext.); `atlas/cli.py::pause/resume/cancel` (refactor: Submit commands instead of mutating process-local maps.)
  * Epic boundary: Durable progress, controls, safe points, and checkpoints — Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.
  * Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-008 requires: Current progress and pause/resume/cancel are process-local; restart repeats phases without verified recovery state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Turn pause, resume, and cancel into idempotent commands that the active attempt polls and either applies at a declared safe point or rejects with a durable reason.
  * Component dispositions: `atlas/core/control_service.py::ControlRequestService` (create: Validate and persist control commands.); `atlas/phases/base.py::control_point` (extend: Poll and acknowledge controls through PhaseContext.); `atlas/cli.py::pause/resume/cancel` (refactor: Submit commands instead of mutating process-local maps.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Persist idempotent control requests with actor, target, expected state/version, requested time, and correlation.
  * Define phase-specific safe-point classes and maximum polling latency.
  * At a safe point, atomically checkpoint if required, acknowledge applied/rejected state, and transition attempt/phase/job according to policy.
  * Define cancellation cleanup ownership and resume preconditions.

  Security and safety requirements

  * Authorization and expected-state checks occur before control persistence or application.
  * Late or replayed commands cannot reopen terminal jobs.
  * Cancel does not delete evidence or unverified side effects.
  * Control reasons and actor identifiers are auditable and redacted.

  Edge cases and outliers to handle

  * Pause arrives while no attempt is running.
  * Cancel and success race at the same safe point.
  * Resume references stale checkpoint or superseded job.
  * Duplicate command is delivered from CLI and REST.

  Acceptance criteria (“done” definition)

  * A second process can request and observe applied/rejected control state.
  * `PAUSED` is reached only after durable safe-point acknowledgement.
  * Duplicate control requests are idempotent and conflicting payloads are rejected.
  * Built-in phases document and test maximum control latency.

  Testing plan

  * Control service unit tests.
  * Second-process integration tests.
  * Cancel-versus-success race tests.
  * Duplicate/idempotency tests.
  * Phase safe-point latency tests.
  * Cleanup/evidence preservation tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Control service unit tests., Second-process integration tests., Cancel-versus-success race tests., Duplicate/idempotency tests., Phase safe-point latency tests., Cleanup/evidence preservation tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T9.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/control_service.py::ControlRequestService, atlas/phases/base.py::control_point, atlas/cli.py::pause/resume/cancel.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 36: Implement checkpoint validation, resume decisions, and stale-checkpoint rejection

  1.2 source task(s): `T9.1.4`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T9.1.2, T9.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/checkpoint_service.py::CheckpointService (create); atlas/phases/* checkpoint adapters (extend); atlas/persistence/repositories/checkpoints.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Resume expensive work only from durable checkpoints whose phase, operation, input, config, policy, code, and output references still match current authority.
  * Restore or protect this invariant: Stale or incompatible checkpoints never resume execution.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-008; REQ-008,REQ-015,REQ-016; PDF:p.12,p.14,p.28.

  Where this applies

  * Primary affected components: `atlas/core/checkpoint_service.py::CheckpointService` (create: Create, validate, supersede, and query checkpoints.); `atlas/phases/* checkpoint adapters` (extend: Implement phase-specific cursor and reconciliation logic.); `atlas/persistence/repositories/checkpoints.py` (create: Persist versioned checkpoint records.)
  * Epic boundary: Durable progress, controls, safe points, and checkpoints — Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-008: Persist progress, control requests, safe points, and versioned checkpoints; evidence: GAP-006, GAP-007, GAP-008, REQ-008, REQ-015, REQ-016, REQ-017.
  * Canonical proposed files/interfaces: Refactor `atlas/phases/base.py`, coordinator and CLI; create checkpoint/control models and persistence tables; add `atlas/core/context.py` if useful. / `PhaseContext.report_progress`, `.poll_control`, `.checkpoint`, `ControlRequest`, `Checkpoint`, `ResumeDecision`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-008 requires: Current progress and pause/resume/cancel are process-local; restart repeats phases without verified recovery state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Resume expensive work only from durable checkpoints whose phase, operation, input, config, policy, code, and output references still match current authority.
  * Component dispositions: `atlas/core/checkpoint_service.py::CheckpointService` (create: Create, validate, supersede, and query checkpoints.); `atlas/phases/* checkpoint adapters` (extend: Implement phase-specific cursor and reconciliation logic.); `atlas/persistence/repositories/checkpoints.py` (create: Persist versioned checkpoint records.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define checkpoint creation transactions, immutable digest, predecessor chain, and latest-compatible lookup.
  * Validate job/phase/attempt, input identity, config/policy digest, plugin/backend version, schema, cursor, referenced outputs, and fencing epoch before resume.
  * Define per-phase resume-from-checkpoint versus restart-from-beginning behavior and cleanup of incompatible partial state.
  * Record rejection reason and deterministic recovery decision.

  Security and safety requirements

  * Do not deserialize arbitrary objects or execute data from checkpoints.
  * Referenced files/blobs are revalidated by identity and containment before use.
  * Stale fencing or superseded input invalidates the checkpoint.
  * Checkpoint deletion/retention cannot erase required recovery evidence prematurely.

  Edge cases and outliers to handle

  * Checkpoint record exists but referenced workspace/output is missing.
  * Code/plugin/config version changed incompatibly.
  * Crash during checkpoint creation leaves partial data.
  * Multiple checkpoints compete as latest after retry.

  Acceptance criteria (“done” definition)

  * Stale or incompatible checkpoints never resume execution.
  * Every built-in phase declares checkpoint granularity and validation inputs.
  * Crash tests resume or restart according to one deterministic rule.
  * Checkpoint rejection remains visible in status and diagnostics.

  Testing plan

  * Checkpoint service unit tests.
  * Per-phase resume integration tests.
  * Version/config/input mismatch negative tests.
  * Missing/corrupt referenced-output tests.
  * Crash-at-checkpoint fault injection.
  * Fencing and concurrent-checkpoint tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Checkpoint service unit tests., Per-phase resume integration tests., Version/config/input mismatch negative tests., Missing/corrupt referenced-output tests., Crash-at-checkpoint fault injection., Fencing and concurrent-checkpoint tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T9.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/checkpoint_service.py::CheckpointService, atlas/phases/* checkpoint adapters, atlas/persistence/repositories/checkpoints.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 37: Specify source-access policy and platform capability contracts

  1.2 source task(s): `T10.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T6.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/safety/source_access.py::SourceAccessPolicy (create); atlas/safety/path_safety.py (refactor); docs/security/source-access.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Define one policy for allowed roots, relative paths, symlinks, mounts, special files, case/Unicode normalization, reduced-assurance behavior, and source-versus-destination responsibilities.
  * Restore or protect this invariant: Policy documents exact guarantees by supported platform.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23.

  Where this applies

  * Primary affected components: `atlas/safety/source_access.py::SourceAccessPolicy` (create: Own source read containment and capability requirements.); `atlas/safety/path_safety.py` (refactor: Provide shared normalization primitives, not a bypassable optional helper.); `docs/security/source-access.md` (create: Document guarantees and platform limitations.)
  * Epic boundary: Canonical race-resistant source access — Route every source read through one registered-root, source-relative, capability-aware service that detects symlink, mount, case, Unicode, and TOCTOU hazards.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].
  * Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-009 requires: PathSafetyService is not the authoritative route for all opens, leaving bypasses and source TOCTOU exposure.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Define one policy for allowed roots, relative paths, symlinks, mounts, special files, case/Unicode normalization, reduced-assurance behavior, and source-versus-destination responsibilities.
  * Component dispositions: `atlas/safety/source_access.py::SourceAccessPolicy` (create: Own source read containment and capability requirements.); `atlas/safety/path_safety.py` (refactor: Provide shared normalization primitives, not a bypassable optional helper.); `docs/security/source-access.md` (create: Document guarantees and platform limitations.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define canonical root and relative-path representations, allowed entry classes, symlink policy, mount boundary, path length, case/Unicode strategy, and expected occurrence metadata.
  * Define platform capability probes for handle-relative open, no-follow, directory descriptors, stable file IDs, mount IDs, and no-replace operations.
  * Define strong, reduced-assurance, and unsupported modes with explicit startup/config behavior.
  * Separate source reads from workspace/destination path construction and temporary-file APIs.

  Security and safety requirements

  * Strong containment is the default; reduced assurance requires explicit policy and status disclosure.
  * Reject absolute, drive, UNC, NUL, parent traversal, reserved/device, and ambiguous normalized paths.
  * Policy cannot be weakened by plugin or pipeline metadata beyond deployment-authorized bounds.
  * Mount/symlink decisions are deterministic and auditable.

  Edge cases and outliers to handle

  * Windows reparse points, junctions, alternate data streams, and case-insensitive collisions.
  * POSIX bind mounts, hard links, procfs-like files, and disappearing directories.
  * Unicode normalization changes path comparison.
  * Network filesystems do not provide stable inode or atomic semantics.

  Acceptance criteria (“done” definition)

  * Policy documents exact guarantees by supported platform.
  * Unsafe or unsupported capability combinations fail before intake/job execution.
  * Source and destination path authorities remain separate.
  * Every normalization and policy decision has a stable error/status code.

  Testing plan

  * Path normalization unit/property tests.
  * Platform capability probe tests.
  * Symlink/reparse/mount policy matrix tests.
  * Case/Unicode collision tests.
  * Unsupported/reduced-assurance startup tests.
  * Threat-model review.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Path normalization unit/property tests., Platform capability probe tests., Symlink/reparse/mount policy matrix tests., Case/Unicode collision tests., Unsupported/reduced-assurance startup tests., Threat-model review..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T10.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/safety/source_access.py::SourceAccessPolicy, atlas/safety/path_safety.py, docs/security/source-access.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 38: Implement handle-relative no-follow opens and occurrence verification

  1.2 source task(s): `T10.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T10.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/safety/source_access.py::SourceAccessService (create); atlas/safety/source_access_posix.py (create); atlas/safety/source_access_windows.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Resolve source-relative occurrences beneath a registered root, open without following unexpected links where supported, and verify the opened object matches intake evidence.
  * Restore or protect this invariant: Symlink/reparse swap fixtures cannot escape the registered root.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23.

  Where this applies

  * Primary affected components: `atlas/safety/source_access.py::SourceAccessService` (create: Own root handles, open/stat, and validation.); `atlas/safety/source_access_posix.py` (create: Implement POSIX strong mode.); `atlas/safety/source_access_windows.py` (create: Implement Windows capability-specific mode.)
  * Epic boundary: Canonical race-resistant source access — Route every source read through one registered-root, source-relative, capability-aware service that detects symlink, mount, case, Unicode, and TOCTOU hazards.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].
  * Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-009 requires: PathSafetyService is not the authoritative route for all opens, leaving bypasses and source TOCTOU exposure.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Resolve source-relative occurrences beneath a registered root, open without following unexpected links where supported, and verify the opened object matches intake evidence.
  * Component dispositions: `atlas/safety/source_access.py::SourceAccessService` (create: Own root handles, open/stat, and validation.); `atlas/safety/source_access_posix.py` (create: Implement POSIX strong mode.); `atlas/safety/source_access_windows.py` (create: Implement Windows capability-specific mode.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Open and retain a trusted root handle/identity, resolve path components without following unapproved links, and reject root escape.
  * Open the final object with required flags, validate type and available device/inode/file-ID/size metadata against the occurrence, and return a mediated handle.
  * Revalidate relevant metadata after read and close all descriptors deterministically.
  * Surface platform capability and reduced-assurance reason with every access result.

  Security and safety requirements

  * Never reopen by untrusted absolute path after validation.
  * Protect against symlink/reparse swaps, mount changes, file replacement, and directory descriptor races.
  * Limit descriptor lifetime/count and sanitize inherited handles.
  * Do not disclose host filesystem layout to plugins or external clients.

  Edge cases and outliers to handle

  * Parent directory is renamed while handle remains open.
  * Final file is replaced between component walk and open.
  * File is a hard link to content outside policy.
  * Descriptor exhaustion or permission revocation.

  Acceptance criteria (“done” definition)

  * Symlink/reparse swap fixtures cannot escape the registered root.
  * Opened object identity is compared to the occurrence before bytes are trusted.
  * Unsupported strong primitives are reported, never silently emulated as equivalent.
  * All descriptors close on success, cancellation, and failure.

  Testing plan

  * Barrier-controlled symlink/reparse swap tests.
  * Mount/bind/junction tests on capable runners.
  * File-replacement and rename tests.
  * Descriptor leak/exhaustion tests.
  * Permission revocation tests.
  * Platform-specific conformance suite.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Barrier-controlled symlink/reparse swap tests., Mount/bind/junction tests on capable runners., File-replacement and rename tests., Descriptor leak/exhaustion tests., Permission revocation tests., Platform-specific conformance suite..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T10.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/safety/source_access.py::SourceAccessService, atlas/safety/source_access_posix.py, atlas/safety/source_access_windows.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 39: Create separate safe temporary and destination path services

  1.2 source task(s): `T10.1.3`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T10.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/workspace_paths.py (create); atlas/safety/destination_access.py (create); atlas/safety/tempfiles.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prevent source-access authority from being reused for writes by centralizing temporary file creation, workspace child paths, and destination commit paths under different contracts.
  * Restore or protect this invariant: All temp/workspace files are attempt-owned, permission-restricted, and contained.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23.

  Where this applies

  * Primary affected components: `atlas/artifacts/workspace_paths.py` (create: Construct attempt-owned workspace paths.); `atlas/safety/destination_access.py` (create: Validate configured publication destinations.); `atlas/safety/tempfiles.py` (create: Create restrictive, race-safe temporary files.)
  * Epic boundary: Canonical race-resistant source access — Route every source read through one registered-root, source-relative, capability-aware service that detects symlink, mount, case, Unicode, and TOCTOU hazards.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].
  * Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-009 requires: PathSafetyService is not the authoritative route for all opens, leaving bypasses and source TOCTOU exposure.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prevent source-access authority from being reused for writes by centralizing temporary file creation, workspace child paths, and destination commit paths under different contracts.
  * Component dispositions: `atlas/artifacts/workspace_paths.py` (create: Construct attempt-owned workspace paths.); `atlas/safety/destination_access.py` (create: Validate configured publication destinations.); `atlas/safety/tempfiles.py` (create: Create restrictive, race-safe temporary files.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define APIs for attempt workspace children, staged output names, unique temp files, destination-relative targets, and no-replace/expected-replace commits.
  * Use restrictive permissions, unpredictable names, same-filesystem staging where atomic commit is required, and explicit cleanup ownership.
  * Reject untrusted member/plugin-provided names before path construction.
  * Return mediated handles/objects rather than raw unrestricted paths where practical.

  Security and safety requirements

  * No temporary or materialized output may be created under a registered source root.
  * Avoid insecure predictable names, inherited permissions, and following existing links.
  * Destination policy is separate from source policy and later publication authorization.
  * Cleanup cannot traverse outside attempt-owned roots.

  Edge cases and outliers to handle

  * Temp root is full, shared, symlinked, or on a different filesystem.
  * Output name collides with existing file.
  * Process crashes before cleanup or final commit.
  * Destination path becomes a link after validation.

  Acceptance criteria (“done” definition)

  * All temp/workspace files are attempt-owned, permission-restricted, and contained.
  * No-replace behavior is capability-tested and collision-safe.
  * Cleanup is idempotent and cannot escape its root.
  * Source and destination APIs cannot be substituted for one another by type/interface.

  Testing plan

  * Temporary-file security tests.
  * Symlink/collision/no-replace tests.
  * Disk-full and cross-filesystem tests.
  * Crash/orphan cleanup tests.
  * Type/interface misuse tests.
  * Permission-mode tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Temporary-file security tests., Symlink/collision/no-replace tests., Disk-full and cross-filesystem tests., Crash/orphan cleanup tests., Type/interface misuse tests., Permission-mode tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T10.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/workspace_paths.py, atlas/safety/destination_access.py, atlas/safety/tempfiles.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 40: Route every built-in filesystem operation through canonical access services

  1.2 source task(s): `T10.1.4`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T10.1.2, T10.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/phases/* (refactor); atlas/safety/guardrails.py (create); tests/security/test_filesystem_authority.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Eliminate bypasses by integrating discovery, hashing, structure, extraction, analysis, and publication with SourceAccess, Workspace, and Destination services and enforcing static/runtime guards.
  * Restore or protect this invariant: Static analysis finds no unapproved direct filesystem authority in built-in phases.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23.

  Where this applies

  * Primary affected components: `atlas/phases/*` (refactor: Replace direct source open/stat/walk/write paths.); `atlas/safety/guardrails.py` (create: Detect unapproved filesystem calls in built-in modules.); `tests/security/test_filesystem_authority.py` (create: Prove attribution and containment.)
  * Epic boundary: Canonical race-resistant source access — Route every source read through one registered-root, source-relative, capability-aware service that detects symlink, mount, case, Unicode, and TOCTOU hazards.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-009: Create one canonical race-resistant SourceAccess service; evidence: GAP-004, GAP-012, REQ-011; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/path_safety.py:L26-L146].
  * Canonical proposed files/interfaces: Create `atlas/safety/source_access.py`; extend `atlas/safety/path_safety.py`; integrate all phases and intake/artifact services. / `SourceAccess.open_occurrence`, `stat_occurrence`, `read_stream`; `PathPolicy`; platform capability report.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-009 requires: PathSafetyService is not the authoritative route for all opens, leaving bypasses and source TOCTOU exposure.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Eliminate bypasses by integrating discovery, hashing, structure, extraction, analysis, and publication with SourceAccess, Workspace, and Destination services and enforcing static/runtime guards.
  * Component dispositions: `atlas/phases/*` (refactor: Replace direct source open/stat/walk/write paths.); `atlas/safety/guardrails.py` (create: Detect unapproved filesystem calls in built-in modules.); `tests/security/test_filesystem_authority.py` (create: Prove attribution and containment.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Inventory every `open`, `stat`, `walk`, `glob`, archive extract, temp, subprocess file, and destination write call.
  * Refactor each call to the appropriate source, workspace, content-store, or destination service with occurrence/attempt attribution.
  * Add a static allowlist or architecture test for unavoidable low-level implementation calls.
  * Emit access decisions and stable errors without logging sensitive paths or content.

  Security and safety requirements

  * Plugins receive only mediated AnalysisContext/WorkSpec references.
  * No built-in phase may accept arbitrary post-intake absolute source paths.
  * Subprocess and remote backends must use scoped mediated inputs.
  * Static guard exceptions require documented owner and threat rationale.

  Edge cases and outliers to handle

  * Third-party library internally opens a path.
  * Legacy compatibility code retains direct access.
  * Archive library wants a filesystem destination path.
  * Publication adapter uses an external SDK with opaque file access.

  Acceptance criteria (“done” definition)

  * Static analysis finds no unapproved direct filesystem authority in built-in phases.
  * Every source read is attributable to SourceRoot/Generation/Occurrence.
  * Every write is attributable to job/phase/attempt/workspace or publication attempt.
  * Bypass attempts fail deterministic security tests.

  Testing plan

  * Static architecture test.
  * End-to-end access-attribution tests.
  * Legacy bypass negative tests.
  * Third-party library mediation tests.
  * Publication/extraction containment tests.
  * Log/path redaction tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Static architecture test., End-to-end access-attribution tests., Legacy bypass negative tests., Third-party library mediation tests., Publication/extraction containment tests., Log/path redaction tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T10.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/phases/*, atlas/safety/guardrails.py, tests/security/test_filesystem_authority.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 41: Implement attempt-owned quarantine workspace lifecycle

  1.2 source task(s): `T11.1.1`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T7.1.4, T10.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/workspace.py::WorkspaceManager (create); workspaces migration (create); atlas/core/runtime.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create unique per-job/phase/attempt workspaces outside source roots with restrictive permissions, quotas, ownership metadata, cleanup states, and crash reconciliation.
  * Restore or protect this invariant: No Phase-D or analyzer write occurs under any registered source root.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25.

  Where this applies

  * Primary affected components: `atlas/artifacts/workspace.py::WorkspaceManager` (create: Own create/open/account/seal/cleanup workspace lifecycle.); `workspaces migration` (create: Persist workspace identity, root, quota, status, and ownership.); `atlas/core/runtime.py` (extend: Inject one WorkspaceManager into phases/backends.)
  * Epic boundary: Quarantine, recursive archive budgets, and controlled materialization — Inspect containers before extraction, contain every side effect in attempt-owned workspaces, and enforce cumulative recursive resource limits.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].
  * Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-010 requires: Current extraction writes beside the source and nested-depth configuration is not recursively enforced.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create unique per-job/phase/attempt workspaces outside source roots with restrictive permissions, quotas, ownership metadata, cleanup states, and crash reconciliation.
  * Component dispositions: `atlas/artifacts/workspace.py::WorkspaceManager` (create: Own create/open/account/seal/cleanup workspace lifecycle.); `workspaces migration` (create: Persist workspace identity, root, quota, status, and ownership.); `atlas/core/runtime.py` (extend: Inject one WorkspaceManager into phases/backends.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Allocate canonical workspace roots outside source roots using job/phase/attempt identity and unpredictable staging names.
  * Persist status CREATED/ACTIVE/SEALED/CLEANUP_PENDING/CLEANED/ORPHANED/BLOCKED, quota, permissions, provider, and manifest digest.
  * Provide mediated child creation, byte/file accounting, seal/no-more-writes, and idempotent cleanup.
  * Reconcile orphan or partial workspaces at startup without deleting unknown operator data.

  Security and safety requirements

  * Reject configured workspace roots that overlap or descend from a SourceRoot.
  * Use restrictive modes/ACLs and prevent symlink/reparse escape.
  * Cleanup operates only on persisted attempt-owned roots and never follows links.
  * Workspace names and metadata do not expose secrets or raw artifact names unnecessarily.

  Edge cases and outliers to handle

  * Workspace root full, read-only, shared by two runtimes, or on unsupported filesystem.
  * Process crash during creation, write, seal, or cleanup.
  * Malicious output creates links or permission changes.
  * Operator manually modifies an orphan workspace.

  Acceptance criteria (“done” definition)

  * No Phase-D or analyzer write occurs under any registered source root.
  * Every workspace is attributable to one attempt and has deterministic status/recovery.
  * Quotas and actual usage are persisted and enforced.
  * Cleanup is idempotent, contained, and preserves evidence when ownership is uncertain.

  Testing plan

  * Workspace lifecycle unit tests.
  * Overlap/symlink/reparse containment tests.
  * Disk-full/quota tests.
  * Crash-point reconciliation tests.
  * Permission/ACL tests.
  * Concurrent allocation collision tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Workspace lifecycle unit tests., Overlap/symlink/reparse containment tests., Disk-full/quota tests., Crash-point reconciliation tests., Permission/ACL tests., Concurrent allocation collision tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T11.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/workspace.py::WorkspaceManager, workspaces migration, atlas/core/runtime.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 42: Implement recursive structural inspection under cumulative archive budgets

  1.2 source task(s): `T11.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T11.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/safety/archive_safety.py::ArchiveBudgetController (create); atlas/phases/structural_discovery.py (refactor); atlas/artifacts/structural_inspection.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Traverse nested containers without materializing them when feasible, using a bounded work queue and cumulative limits for depth, members, declared/actual bytes, ratio, temp use, and time.
  * Restore or protect this invariant: All adversarial containers terminate within configured CPU/time/byte/member/depth bounds.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25.

  Where this applies

  * Primary affected components: `atlas/safety/archive_safety.py::ArchiveBudgetController` (create: Own cumulative resource counters and decisions.); `atlas/phases/structural_discovery.py` (refactor: Inspect nested containers through bounded queue.); `atlas/artifacts/structural_inspection.py` (create: Normalize member metadata and nested relationships.)
  * Epic boundary: Quarantine, recursive archive budgets, and controlled materialization — Inspect containers before extraction, contain every side effect in attempt-owned workspaces, and enforce cumulative recursive resource limits.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].
  * Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-010 requires: Current extraction writes beside the source and nested-depth configuration is not recursively enforced.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Traverse nested containers without materializing them when feasible, using a bounded work queue and cumulative limits for depth, members, declared/actual bytes, ratio, temp use, and time.
  * Component dispositions: `atlas/safety/archive_safety.py::ArchiveBudgetController` (create: Own cumulative resource counters and decisions.); `atlas/phases/structural_discovery.py` (refactor: Inspect nested containers through bounded queue.); `atlas/artifacts/structural_inspection.py` (create: Normalize member metadata and nested relationships.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define canonical member paths and reject absolute, drive, UNC, NUL, parent traversal, reserved/device, link, and special entries by default.
  * Inspect supported nested formats through a bounded queue while carrying cumulative depth, member, declared/actual expanded bytes, ratio, temp, and elapsed budgets.
  * Record accepted/skipped/rejected/unknown member decisions with reason and parent content/member identity.
  * Stop deterministically at limits and mark partial/unknown structure non-success.

  Security and safety requirements

  * No archive API bulk-extract call is used for structural inspection.
  * Compression metadata is untrusted; actual reads/writes remain budgeted.
  * Nested content type is verified, not inferred only from filename extension.
  * Parser faults and unsupported encryption/format do not degrade to extraction.

  Edge cases and outliers to handle

  * Recursive self-similar archives, encrypted members, overlapping/duplicate names.
  * Huge declared size with tiny actual data or vice versa.
  * Parser loops, malformed headers, truncated central directory.
  * Nested depth exactly at and beyond configured limit.

  Acceptance criteria (“done” definition)

  * All adversarial containers terminate within configured CPU/time/byte/member/depth bounds.
  * Nested limits are cumulative and recursively enforced.
  * Every member decision is recorded with stable reason and parent linkage.
  * Unknown or partial inspection cannot authorize extraction.

  Testing plan

  * Adversarial archive corpus tests.
  * Depth/member/byte/ratio boundary property tests.
  * Malformed/truncated/fuzz tests.
  * Encrypted/unsupported-format tests.
  * Nested content-type verification tests.
  * Resource/time termination tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Adversarial archive corpus tests., Depth/member/byte/ratio boundary property tests., Malformed/truncated/fuzz tests., Encrypted/unsupported-format tests., Nested content-type verification tests., Resource/time termination tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T11.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/safety/archive_safety.py::ArchiveBudgetController, atlas/phases/structural_discovery.py, atlas/artifacts/structural_inspection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 43: Implement exact-report-bound `MaterializationService`

  1.2 source task(s): `T11.1.3`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T11.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/materialization.py::MaterializationService (create); atlas/phases/extraction.py (refactor); atlas/safety/archive_safety.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Extract only members authorized by an accepted StructuralReport for the exact parent ContentIdentity into a quarantine workspace, with no-overwrite writes and continuous actual-byte accounting.
  * Restore or protect this invariant: Phase D rejects every report/content/config/policy mismatch before writing.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25.

  Where this applies

  * Primary affected components: `atlas/artifacts/materialization.py::MaterializationService` (create: Own controlled extraction and output writes.); `atlas/phases/extraction.py` (refactor: Consume report IDs and materialization plans.); `atlas/safety/archive_safety.py` (extend: Provide safe member streaming rather than bulk extract.)
  * Epic boundary: Quarantine, recursive archive budgets, and controlled materialization — Inspect containers before extraction, contain every side effect in attempt-owned workspaces, and enforce cumulative recursive resource limits.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].
  * Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-010 requires: Current extraction writes beside the source and nested-depth configuration is not recursively enforced.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Extract only members authorized by an accepted StructuralReport for the exact parent ContentIdentity into a quarantine workspace, with no-overwrite writes and continuous actual-byte accounting.
  * Component dispositions: `atlas/artifacts/materialization.py::MaterializationService` (create: Own controlled extraction and output writes.); `atlas/phases/extraction.py` (refactor: Consume report IDs and materialization plans.); `atlas/safety/archive_safety.py` (extend: Provide safe member streaming rather than bulk extract.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Validate report state, parent content identity, inspector/config/policy digests, approved member plan, workspace ownership, and current budgets before any write.
  * Stream each member to a unique staged file with no-follow/no-replace semantics, actual byte accounting, hash calculation, fsync policy, and final seal.
  * Reject links/devices/specials and canonicalize destination names independently of archive library output.
  * Persist partial results and cleanup state; never present partial extraction as complete.

  Security and safety requirements

  * Do not trust archive member sizes, paths, modes, timestamps, or link targets.
  * Prevent overwrite, path escape, hard-link surprises, sparse-file abuse, and permission elevation.
  * Hash outputs before downstream access and mediate analyzer access through workspace/content APIs.
  * Unknown write outcome enters reconciliation rather than automatic duplicate extraction.

  Edge cases and outliers to handle

  * Two members normalize to same path.
  * Disk fills mid-member or fsync fails.
  * Archive changes or report identity mismatches.
  * Cancellation arrives after some members are written.

  Acceptance criteria (“done” definition)

  * Phase D rejects every report/content/config/policy mismatch before writing.
  * No output escapes the attempt workspace or overwrites an existing file.
  * Actual written bytes and file counts remain within cumulative budgets.
  * Partial/cancelled attempts retain deterministic status, evidence, and cleanup ownership.

  Testing plan

  * Traversal/collision/link negative tests.
  * Report-binding mismatch tests.
  * Disk-full/fsync/short-write fault tests.
  * Cancellation and partial extraction tests.
  * No-overwrite/concurrent attempt tests.
  * Output hash and workspace containment tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Traversal/collision/link negative tests., Report-binding mismatch tests., Disk-full/fsync/short-write fault tests., Cancellation and partial extraction tests., No-overwrite/concurrent attempt tests., Output hash and workspace containment tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T11.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/materialization.py::MaterializationService, atlas/phases/extraction.py, atlas/safety/archive_safety.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 44: Persist derivation edges and adversarial materialization evidence

  1.2 source task(s): `T11.1.4`
  Priority: `P0`
  Estimated effort: `14 hours`
  Dependencies: `T11.1.2, T11.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/models.py::DerivationRecord (create); atlas/persistence/repositories/derivations.py (create); tests/fixtures/archives/adversarial/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Record every materialized child as a derived artifact with parent/member/report/attempt/workspace lineage and prove containment through a maintained adversarial corpus.
  * Restore or protect this invariant: Every downstream extracted identity has at least one valid derivation edge.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25.

  Where this applies

  * Primary affected components: `atlas/artifacts/models.py::DerivationRecord` (create: Link parent identity/member/report/attempt to child identity.); `atlas/persistence/repositories/derivations.py` (create: Persist derivation graph and cleanup outcome.); `tests/fixtures/archives/adversarial/` (create: Maintain inert bounded attack corpus.)
  * Epic boundary: Quarantine, recursive archive budgets, and controlled materialization — Inspect containers before extraction, contain every side effect in attempt-owned workspaces, and enforce cumulative recursive resource limits.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-010: Introduce quarantine workspaces and recursive cumulative archive budgets; evidence: GAP-012, GAP-013, REQ-009, REQ-010, REQ-012; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/extraction.py:L20-L181]; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/safety/archive_safety.py].
  * Canonical proposed files/interfaces: Create `atlas/artifacts/workspace.py`; extend `atlas/safety/archive_safety.py`, `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`. / `WorkspaceManager`, `ArchiveBudget`, `StructuralReport`, `MaterializationPlan`, `ExtractionRecord`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-010 requires: Current extraction writes beside the source and nested-depth configuration is not recursively enforced.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Record every materialized child as a derived artifact with parent/member/report/attempt/workspace lineage and prove containment through a maintained adversarial corpus.
  * Component dispositions: `atlas/artifacts/models.py::DerivationRecord` (create: Link parent identity/member/report/attempt to child identity.); `atlas/persistence/repositories/derivations.py` (create: Persist derivation graph and cleanup outcome.); `tests/fixtures/archives/adversarial/` (create: Maintain inert bounded attack corpus.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Persist parent content identity, structural report, member identity/path, extraction attempt, workspace output, child content identity, bytes, and disposition.
  * Create derivation only after the child hash is verified; keep failed/partial member attempts separately.
  * Build bidirectional lineage queries and invariant checks for orphan children or duplicate commits.
  * Version the adversarial corpus with generated provenance, expected policy decision, and resource ceiling.

  Security and safety requirements

  * Corpus contains no active malware or destructive scripts; use inert format constructs.
  * Lineage records are immutable and cannot be supplied by plugins.
  * Failed member paths and names are redacted/bounded in logs while canonical records remain protected.
  * Fuzz/minimization outputs are quarantined and size-limited.

  Edge cases and outliers to handle

  * Same child bytes derive from multiple parents/members.
  * Child hash succeeds but derivation transaction fails.
  * Duplicate member names produce one rejected and one accepted output.
  * Cleanup removes workspace path but retained content identity remains.

  Acceptance criteria (“done” definition)

  * Every downstream extracted identity has at least one valid derivation edge.
  * No derivation is committed before child hash verification.
  * Bidirectional lineage queries detect and reject orphan records.
  * Adversarial corpus tests complete within declared resource ceilings on supported platforms.

  Testing plan

  * Derivation repository unit tests.
  * Parent-to-child and child-to-parent query tests.
  * Transaction failure/orphan reconciliation tests.
  * Duplicate-content lineage tests.
  * Adversarial corpus regression tests.
  * Archive parser fuzzing with bounded minimization.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Derivation repository unit tests., Parent-to-child and child-to-parent query tests., Transaction failure/orphan reconciliation tests., Duplicate-content lineage tests., Adversarial corpus regression tests., Archive parser fuzzing with bounded minimization..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T11.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/models.py::DerivationRecord, atlas/persistence/repositories/derivations.py, tests/fixtures/archives/adversarial/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 45: Define `ContentStore` contracts and retention-mode semantics

  1.2 source task(s): `T12.1.1`
  Priority: `P1`
  Estimated effort: `12 hours`
  Dependencies: `T7.1.4, T10.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/store.py::ContentStore (create); atlas/config/phases.py::ContentRetentionPolicy (create); atlas/artifacts/models.py::BlobRecord (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify provider-neutral blob operations and the `required | preferred | identity_only` policy so provenance and replayability claims remain explicit.
  * Restore or protect this invariant: Retention mode has one documented effect on job state and replayability.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28.

  Where this applies

  * Primary affected components: `atlas/artifacts/store.py::ContentStore` (create: Define put/open/verify/stat/delete/reconcile capabilities.); `atlas/config/phases.py::ContentRetentionPolicy` (create: Own retention mode and quota behavior.); `atlas/artifacts/models.py::BlobRecord` (create: Persist provider, status, size, integrity, retention, and provenance.)
  * Epic boundary: Optional immutable local content store — Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.
  * Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-011 requires: Persistent identities enable safe deduplication, reproducibility, and stable inputs, but a true CAS must not be confused with hashing.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify provider-neutral blob operations and the `required | preferred | identity_only` policy so provenance and replayability claims remain explicit.
  * Component dispositions: `atlas/artifacts/store.py::ContentStore` (create: Define put/open/verify/stat/delete/reconcile capabilities.); `atlas/config/phases.py::ContentRetentionPolicy` (create: Own retention mode and quota behavior.); `atlas/artifacts/models.py::BlobRecord` (create: Persist provider, status, size, integrity, retention, and provenance.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define staged put, verified open, stat, integrity check, lease/reference, retention class, delete/tombstone, and orphan reconciliation contracts.
  * Define retention modes and exactly how each affects job success, replayability, diagnostics, and later result reuse.
  * Define blob states STAGING/COMMITTED/ORPHANED/CORRUPT/MISSING/DELETING/DELETED with authority rules.
  * Resolve the default retention mode through an operator/product decision and record migration behavior.

  Security and safety requirements

  * Identity remains canonical even when no blob is retained.
  * A provider cannot claim a blob exists without core verification metadata.
  * Blob paths/keys derive from validated digest, never untrusted filenames.
  * Deletion/retention decisions require policy and reference checks.

  Edge cases and outliers to handle

  * Quota prevents preferred capture.
  * Required mode cannot durably commit bytes.
  * Provider reports success but later verification fails.
  * Identity-only job later requests replay.

  Acceptance criteria (“done” definition)

  * Retention mode has one documented effect on job state and replayability.
  * Provider contract distinguishes absent, corrupt, unknown, and verified blobs.
  * Default mode and compatibility policy are approved and recorded.
  * No API equates `ContentIdentity` existence with managed-byte availability.

  Testing plan

  * Protocol/model unit tests.
  * Retention-mode truth-table tests.
  * Provider conformance skeleton.
  * Replayability status tests.
  * Quota/fallback negative tests.
  * Version/compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Protocol/model unit tests., Retention-mode truth-table tests., Provider conformance skeleton., Replayability status tests., Quota/fallback negative tests., Version/compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T12.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/store.py::ContentStore, atlas/config/phases.py::ContentRetentionPolicy, atlas/artifacts/models.py::BlobRecord.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 46: Implement staged, verified, no-replace local CAS writes

  1.2 source task(s): `T12.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T12.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/local_store.py::LocalContentStore (create); atlas/artifacts/store_paths.py (create); atlas/artifacts/identity.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Store bytes at digest-derived immutable locations using one-pass hash/copy, exclusive staging, verification, fsync policy, and collision-safe finalization.
  * Restore or protect this invariant: Repeated identical bytes consume one verified blob payload.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28.

  Where this applies

  * Primary affected components: `atlas/artifacts/local_store.py::LocalContentStore` (create: Implement local immutable blob storage.); `atlas/artifacts/store_paths.py` (create: Derive safe digest paths and staging roots.); `atlas/artifacts/identity.py` (extend: Tee verified reads into the content store.)
  * Epic boundary: Optional immutable local content store — Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.
  * Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-011 requires: Persistent identities enable safe deduplication, reproducibility, and stable inputs, but a true CAS must not be confused with hashing.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Store bytes at digest-derived immutable locations using one-pass hash/copy, exclusive staging, verification, fsync policy, and collision-safe finalization.
  * Component dispositions: `atlas/artifacts/local_store.py::LocalContentStore` (create: Implement local immutable blob storage.); `atlas/artifacts/store_paths.py` (create: Derive safe digest paths and staging roots.); `atlas/artifacts/identity.py` (extend: Tee verified reads into the content store.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Derive provider-relative paths from canonical SHA-256 with bounded directory fan-out.
  * Write to an exclusive attempt-owned staging file while hashing and accounting bytes; verify digest/size before commit.
  * Fsync file and parent directory where supported, then perform no-replace commit or verified platform-safe equivalent.
  * If target exists, verify its digest/size before reuse; mismatch becomes an integrity incident.

  Security and safety requirements

  * No untrusted path component enters CAS paths.
  * Concurrent writers cannot overwrite or truncate an existing blob.
  * Unsupported durability/no-replace capabilities are reported and policy-controlled.
  * Staging permissions and cleanup prevent other users/processes from substituting content.

  Edge cases and outliers to handle

  * Two writers store same digest concurrently.
  * Crash before/after fsync or final rename.
  * Existing digest path contains wrong bytes.
  * Cross-filesystem staging prevents atomic rename.

  Acceptance criteria (“done” definition)

  * Repeated identical bytes consume one verified blob payload.
  * Concurrent writes yield one commit and safe verified reuse.
  * Existing mismatch is blocked and surfaced as integrity incident.
  * Crash points leave valid blob, detectable orphan, or no blob—never false commit.

  Testing plan

  * Known-hash put/open/verify tests.
  * Concurrent same/different content tests.
  * Crash-point fault injection.
  * Existing-corrupt-target tests.
  * Fsync/no-replace capability tests.
  * Disk-full and permission tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Known-hash put/open/verify tests., Concurrent same/different content tests., Crash-point fault injection., Existing-corrupt-target tests., Fsync/no-replace capability tests., Disk-full and permission tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T12.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/local_store.py::LocalContentStore, atlas/artifacts/store_paths.py, atlas/artifacts/identity.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 47: Persist blob provenance, references, quotas, and replayability status

  1.2 source task(s): `T12.1.3`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T12.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/repositories/blobs.py (create); atlas/artifacts/store.py::ContentCaptureService (create); atlas/status/projection.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Link retained blobs to content identities, occurrences/capture attempts, retention classes, references, verification history, and capacity accounting.
  * Restore or protect this invariant: Every committed blob has verifiable identity, provider, provenance, and retention status.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28.

  Where this applies

  * Primary affected components: `atlas/persistence/repositories/blobs.py` (create: Persist blob/provider/reference/integrity records.); `atlas/artifacts/store.py::ContentCaptureService` (create: Coordinate identity read and retention result.); `atlas/status/projection.py` (extend: Expose managed-byte and replayability status.)
  * Epic boundary: Optional immutable local content store — Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.
  * Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-011 requires: Persistent identities enable safe deduplication, reproducibility, and stable inputs, but a true CAS must not be confused with hashing.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Link retained blobs to content identities, occurrences/capture attempts, retention classes, references, verification history, and capacity accounting.
  * Component dispositions: `atlas/persistence/repositories/blobs.py` (create: Persist blob/provider/reference/integrity records.); `atlas/artifacts/store.py::ContentCaptureService` (create: Coordinate identity read and retention result.); `atlas/status/projection.py` (extend: Expose managed-byte and replayability status.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Persist provider key, canonical identity, size, status, capture attempt/occurrence, verification time, retention class, and reference counts/leases.
  * Make identity hashing and capture one pass where configured, with separate success/failure outcomes.
  * Enforce provider/job/global quotas before and during writes and report capacity decisions.
  * Expose `replayable_from_managed_bytes` and exact reason.

  Security and safety requirements

  * Reference counts are derived/transactional and cannot be decremented by untrusted callers.
  * Quota races are handled with reservation or bounded overcommit policy.
  * Integrity verification precedes replay or reuse.
  * Status does not reveal sensitive provider paths.

  Edge cases and outliers to handle

  * Blob retained but DB transaction fails.
  * DB says committed but file is missing.
  * Quota reservation is abandoned.
  * Blob referenced by active checkpoint/publication while retention changes.

  Acceptance criteria (“done” definition)

  * Every committed blob has verifiable identity, provider, provenance, and retention status.
  * Replayability is accurate after restart and missing/corrupt file detection.
  * Quota use and reservations reconcile deterministically.
  * Identity-only and captured modes remain distinguishable in APIs/events.

  Testing plan

  * Repository/model tests.
  * One-pass hash/capture integration tests.
  * Quota race/reservation tests.
  * DB/file split-brain fault tests.
  * Restart replayability tests.
  * Status redaction tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Repository/model tests., One-pass hash/capture integration tests., Quota race/reservation tests., DB/file split-brain fault tests., Restart replayability tests., Status redaction tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T12.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/repositories/blobs.py, atlas/artifacts/store.py::ContentCaptureService, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 48: Implement CAS integrity scans and orphan reconciliation hooks

  1.2 source task(s): `T12.1.4`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T12.1.2, T12.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/reconcile.py::ContentStoreReconciler (create); atlas/cli.py::content verify/reconcile (extend); docs/operations/content-store-recovery.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Detect filesystem/DB divergence, corruption, abandoned staging, and unreferenced blobs without deleting uncertain data or blocking normal identity-only operation.
  * Restore or protect this invariant: Reconciliation classifies every observed divergence with deterministic next action.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28.

  Where this applies

  * Primary affected components: `atlas/artifacts/reconcile.py::ContentStoreReconciler` (create: Scan and classify blob/store divergence.); `atlas/cli.py::content verify/reconcile` (extend: Provide dry-run and controlled repair commands.); `docs/operations/content-store-recovery.md` (create: Document integrity incident and rollback handling.)
  * Epic boundary: Optional immutable local content store — Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-011: Add an optional local immutable content-addressable store; evidence: REQ-005, REQ-029; GAP-005; ADR-005.
  * Canonical proposed files/interfaces: Create `atlas/artifacts/store.py`; extend runtime/config/persistence; preserve `HashStore` facade. / `ContentStore.put/open/verify/has/reconcile`, `BlobRecord`, provider capability descriptor.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-011 requires: Persistent identities enable safe deduplication, reproducibility, and stable inputs, but a true CAS must not be confused with hashing.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Detect filesystem/DB divergence, corruption, abandoned staging, and unreferenced blobs without deleting uncertain data or blocking normal identity-only operation.
  * Component dispositions: `atlas/artifacts/reconcile.py::ContentStoreReconciler` (create: Scan and classify blob/store divergence.); `atlas/cli.py::content verify/reconcile` (extend: Provide dry-run and controlled repair commands.); `docs/operations/content-store-recovery.md` (create: Document integrity incident and rollback handling.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Compare committed records to provider objects and digest/size metadata under bounded scan budgets.
  * Classify missing, corrupt, orphaned, abandoned staging, unreferenced, and unknown objects.
  * Provide dry-run plans and idempotent repairs for safe cases; quarantine or block uncertain cases.
  * Emit integrity events/metrics and retain reconciliation manifests.

  Security and safety requirements

  * Never delete an object solely because a DB reference is missing; confirm ownership, age, and policy.
  * Integrity scan inputs and provider listings are untrusted/bounded.
  * Repair cannot overwrite a canonical blob or bypass retention holds.
  * Operator actions are authenticated/policy-controlled in networked deployments.

  Edge cases and outliers to handle

  * Millions of blobs make full scan expensive.
  * Partial listing or provider outage.
  * Digest verification is interrupted.
  * Object appears during scan due to concurrent capture.

  Acceptance criteria (“done” definition)

  * Reconciliation classifies every observed divergence with deterministic next action.
  * Safe repairs are idempotent and uncertain objects remain preserved/quarantined.
  * Scans are resumable/bounded and expose progress.
  * Integrity incidents disable replay/reuse until resolved.

  Testing plan

  * Synthetic divergence matrix tests.
  * Concurrent capture/reconcile tests.
  * Large-store scan benchmark.
  * Provider outage/partial listing tests.
  * Interrupted verification/resume tests.
  * Deletion-safety negative tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Synthetic divergence matrix tests., Concurrent capture/reconcile tests., Large-store scan benchmark., Provider outage/partial listing tests., Interrupted verification/resume tests., Deletion-safety negative tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T12.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/reconcile.py::ContentStoreReconciler, atlas/cli.py::content verify/reconcile, docs/operations/content-store-recovery.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 49: Define and persist versioned `StructuralReport` records

  1.2 source task(s): `T13.1.1`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T11.1.4, T12.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/models.py::StructuralReport (create); atlas/persistence/repositories/structures.py (create); atlas/phases/structural_discovery.py (refactor)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Capture container structure, inspector attribution, exact content identity, config/policy digests, member manifest, risk assessment, and acceptance state as durable evidence.
  * Restore or protect this invariant: Every report binds to exact parent bytes, inspector, config, policy, and schema versions.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/models.py::StructuralReport` (create: Own exact-byte structural evidence.); `atlas/persistence/repositories/structures.py` (create: Persist reports and member records.); `atlas/phases/structural_discovery.py` (refactor: Write typed reports instead of metadata.)
  * Epic boundary: Structural and extraction lineage contracts — Persist exact-byte structural reports and extraction records whose bindings are verified before materialization and reusable only under exact deterministic keys.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.
  * Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-012 requires: Current structural and extraction phases exchange summaries/live paths rather than durable records bound to exact content.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Capture container structure, inspector attribution, exact content identity, config/policy digests, member manifest, risk assessment, and acceptance state as durable evidence.
  * Component dispositions: `atlas/artifacts/models.py::StructuralReport` (create: Own exact-byte structural evidence.); `atlas/persistence/repositories/structures.py` (create: Persist reports and member records.); `atlas/phases/structural_discovery.py` (refactor: Write typed reports instead of metadata.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define report ID, parent ContentIdentity, inspector/plugin/version, operation/config/policy digest, schema version, member manifest digest, budget summary, warnings, confidence/unknown state, and acceptance decision.
  * Persist normalized member records and nested parent relationships without embedding unbounded raw metadata.
  * Make reports immutable and allow supersession only by a new report.
  * Define deterministic report reuse key and non-cacheable/partial semantics.

  Security and safety requirements

  * Report input identity and policy are core-authored and cannot be supplied by an analyzer.
  * Malformed member names/data are normalized and bounded before persistence.
  * Unknown/partial/unsupported inspection never becomes accepted structure.
  * Sensitive embedded filenames can be redacted in telemetry while protected records retain lineage.

  Edge cases and outliers to handle

  * Encrypted or unsupported container.
  * Inspector crashes after some member records.
  * Same content inspected under new policy/version.
  * Huge member manifest requires streaming/pagination.

  Acceptance criteria (“done” definition)

  * Every report binds to exact parent bytes, inspector, config, policy, and schema versions.
  * Partial and unknown outcomes are visibly non-success.
  * Member manifests are deterministic and queryable without unbounded loads.
  * Reports are immutable and supersession preserves history.

  Testing plan

  * Model/repository unit tests.
  * Inspector attribution/version tests.
  * Partial/unknown state tests.
  * Large manifest pagination tests.
  * Canonical digest/reuse-key tests.
  * Schema migration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Model/repository unit tests., Inspector attribution/version tests., Partial/unknown state tests., Large manifest pagination tests., Canonical digest/reuse-key tests., Schema migration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T13.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/models.py::StructuralReport, atlas/persistence/repositories/structures.py, atlas/phases/structural_discovery.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 50: Define and persist `ExtractionRecord` and output manifests

  1.2 source task(s): `T13.1.2`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T13.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/models.py::ExtractionRecord (create); atlas/persistence/repositories/extractions.py (create); atlas/artifacts/materialization.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Record the extraction plan, attempt, workspace, actual outputs, budgets, derivation edges, failure state, cleanup, and final manifest for every materialization attempt.
  * Restore or protect this invariant: Every extraction attempt has one immutable record and output manifest.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/models.py::ExtractionRecord` (create: Own materialization attempt lineage.); `atlas/persistence/repositories/extractions.py` (create: Persist plan/outcome/output records.); `atlas/artifacts/materialization.py` (extend: Commit records during extraction.)
  * Epic boundary: Structural and extraction lineage contracts — Persist exact-byte structural reports and extraction records whose bindings are verified before materialization and reusable only under exact deterministic keys.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.
  * Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-012 requires: Current structural and extraction phases exchange summaries/live paths rather than durable records bound to exact content.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Record the extraction plan, attempt, workspace, actual outputs, budgets, derivation edges, failure state, cleanup, and final manifest for every materialization attempt.
  * Component dispositions: `atlas/artifacts/models.py::ExtractionRecord` (create: Own materialization attempt lineage.); `atlas/persistence/repositories/extractions.py` (create: Persist plan/outcome/output records.); `atlas/artifacts/materialization.py` (extend: Commit records during extraction.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define report binding, attempt/workspace IDs, planned members, actual outputs, child identities, budget start/end, status, error, cleanup, and output manifest digest.
  * Persist per-member attempt outcome and derivation reference incrementally under one attempt.
  * Seal a successful record only after all approved outputs are hashed and workspace state is consistent.
  * Retain failed/cancelled/partial records for recovery and audit.

  Security and safety requirements

  * Only MaterializationService can author output/derivation facts.
  * Do not store unbounded member content or raw parser errors.
  * A successful record cannot reference unverified or missing child identity.
  * Cleanup records cannot erase evidence of failed side effects.

  Edge cases and outliers to handle

  * No outputs, one output, thousands of outputs.
  * Duplicate child content from different members.
  * Cancellation after seal but before terminal phase transition.
  * Workspace cleanup succeeds before record finalization.

  Acceptance criteria (“done” definition)

  * Every extraction attempt has one immutable record and output manifest.
  * Successful records reference only verified child identities and derivations.
  * Partial/failure cleanup state remains explicit.
  * Output manifest supports deterministic bidirectional lineage queries.

  Testing plan

  * Repository/model tests.
  * Zero/large-output tests.
  * Cancellation/crash boundary tests.
  * Duplicate-content derivation tests.
  * Workspace-record consistency tests.
  * Manifest digest tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Repository/model tests., Zero/large-output tests., Cancellation/crash boundary tests., Duplicate-content derivation tests., Workspace-record consistency tests., Manifest digest tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T13.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/models.py::ExtractionRecord, atlas/persistence/repositories/extractions.py, atlas/artifacts/materialization.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 51: Enforce exact content, configuration, policy, and report binding before extraction

  1.2 source task(s): `T13.1.3`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T13.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/phases/extraction.py::execute (refactor); atlas/artifacts/structural_validation.py (create); atlas/core/lifecycle.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make Phase D consume a report ID and reject any mismatch between current input/material, report authority, extraction policy, and workspace attempt.
  * Restore or protect this invariant: All mismatches are detected before workspace creation or output writes.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/phases/extraction.py::execute` (refactor: Validate bindings before invoking MaterializationService.); `atlas/artifacts/structural_validation.py` (create: Centralize report compatibility checks.); `atlas/core/lifecycle.py` (extend: Block Phase D on missing/incompatible report.)
  * Epic boundary: Structural and extraction lineage contracts — Persist exact-byte structural reports and extraction records whose bindings are verified before materialization and reusable only under exact deterministic keys.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-012: Persist StructuralReport and ExtractionRecord as exact-byte contracts; evidence: REQ-009, REQ-019, REQ-028; GAP-004, GAP-012, GAP-013.
  * Canonical proposed files/interfaces: Extend `atlas/artifacts/models.py`; refactor `atlas/phases/structural_discovery.py`, `atlas/phases/extraction.py`; migrations. / `StructuralReport`, `ArchiveMember`, `ExtractionRecord`, `ArtifactDerivation`, `MaterializationOutcome`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-012 requires: Current structural and extraction phases exchange summaries/live paths rather than durable records bound to exact content.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Make Phase D consume a report ID and reject any mismatch between current input/material, report authority, extraction policy, and workspace attempt.
  * Component dispositions: `atlas/phases/extraction.py::execute` (refactor: Validate bindings before invoking MaterializationService.); `atlas/artifacts/structural_validation.py` (create: Centralize report compatibility checks.); `atlas/core/lifecycle.py` (extend: Block Phase D on missing/incompatible report.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Load report and verify ACCEPTED state, parent content identity, inspector/schema, config/policy digest, selected member plan, and job/intake ownership.
  * Verify current material source is the same retained/validated ContentIdentity.
  * Create extraction attempt/workspace only after binding validation succeeds.
  * Return stable blocked/error reasons and durable event without side effects on mismatch.

  Security and safety requirements

  * No fallback to re-inspecting or live archive selection inside Phase D.
  * Report IDs from another job/tenant/source are rejected.
  * Policy downgrade or stale report cannot be forced by caller input.
  * Binding errors are auditable without exposing sensitive member names.

  Edge cases and outliers to handle

  * Report accepted under earlier policy version.
  * Blob missing but source occurrence still exists.
  * Report superseded after job queued.
  * Config digest differs only in irrelevant/normalized field.

  Acceptance criteria (“done” definition)

  * All mismatches are detected before workspace creation or output writes.
  * Exact-key equality is based on canonical normalized values.
  * A valid report/material pair proceeds through one controlled path.
  * Blocked reasons are visible in state, event history, and status.

  Testing plan

  * Report/content mismatch tests.
  * Config/policy/version mismatch tests.
  * Cross-job/report authorization tests.
  * Missing blob/source fallback tests.
  * No-side-effect assertion tests.
  * Canonical equality property tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Report/content mismatch tests., Config/policy/version mismatch tests., Cross-job/report authorization tests., Missing blob/source fallback tests., No-side-effect assertion tests., Canonical equality property tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T13.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/phases/extraction.py::execute, atlas/artifacts/structural_validation.py, atlas/core/lifecycle.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 52: Add deterministic structure reuse and end-to-end lineage invariants

  1.2 source task(s): `T13.1.4`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T13.1.2, T13.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/reuse.py::StructuralReusePolicy (create); atlas/artifacts/lineage.py (create); tests/lineage/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Reuse only declared deterministic structural results under exact operation keys and prove complete source-to-derived lineage, including the full model omitted by simplified diagrams.
  * Restore or protect this invariant: Reuse occurs only on exact key equality and records current use provenance.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-012; REQ-009,REQ-028,REQ-029; PDF:p.6-8,p.16,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/reuse.py::StructuralReusePolicy` (create: Evaluate exact-key report reuse.); `atlas/artifacts/lineage.py` (create: Query SourceRoot through extraction outputs bidirectionally.); `tests/lineage/` (create: Enforce graph invariants and PDF model completeness.)
  * Epic boundary: Structural and extraction lineage contracts — Persist exact-byte structural reports and extraction records whose bindings are verified before materialization and reusable only under exact deterministic keys.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
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
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace arbitrary analyzer dictionaries with versioned descriptors, mediated contexts, normalized finding envelopes, and explicit resource/capability declarations.
  * Restore or protect this invariant: No arbitrary dictionary reaches durable findings.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23.

  Where this applies

  * Primary affected components: `atlas/plugins/contracts.py::PluginDescriptor` (create: Declare identity, compatibility, inputs, outputs, capabilities, and resources.); `atlas/plugins/contracts.py::AnalysisContext` (create: Expose mediated reads, derived outputs, progress, and diagnostics.); `atlas/plugins/contracts.py::AnalysisFinding` (create: Normalize attributed analyzer output.)
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
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create one ordered registry that rejects duplicate IDs, incompatible API ranges, conflicting providers, and source-declared capabilities that are not actually deployed.
  * Restore or protect this invariant: Two clean registry builds produce identical order and digest.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-013; REQ-021,REQ-022,REQ-023,REQ-027; PDF:p.17,p.22,p.23.

  Where this applies

  * Primary affected components: `atlas/plugins/registry.py::PluginRegistry` (create: Own discovery, validation, enablement, and snapshot digest.); `atlas/core/runtime.py` (extend: Construct and freeze registries during composition.); `atlas/plugins/discovery.py` (create: Load approved built-ins/entry points deterministically.)
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

* [ ] TODO 58: Implement the trusted `InProcessBackend`

  1.2 source task(s): `T15.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T15.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/inprocess.py::InProcessBackend (create); atlas/core/runtime.py (extend); atlas/plugins/registry.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Run bundled trusted handlers through the same backend contract, context, deadlines, progress, and result normalization later isolation backends must satisfy.
  * Restore or protect this invariant: A bundled analyzer produces identical normalized findings through WorkSpec/WorkResult.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21.

  Where this applies

  * Primary affected components: `atlas/execution/inprocess.py::InProcessBackend` (create: Execute approved factories in the current process.); `atlas/core/runtime.py` (extend: Register backend and approved handlers deterministically.); `atlas/plugins/registry.py` (extend: Resolve factories by frozen descriptor snapshot.)
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

  * Run bundled trusted handlers through the same backend contract, context, deadlines, progress, and result normalization later isolation backends must satisfy.
  * Component dispositions: `atlas/execution/inprocess.py::InProcessBackend` (create: Execute approved factories in the current process.); `atlas/core/runtime.py` (extend: Register backend and approved handlers deterministically.); `atlas/plugins/registry.py` (extend: Resolve factories by frozen descriptor snapshot.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Resolve approved operation/plugin factory from frozen registries and create mediated context from WorkSpec.
  * Execute asynchronously with deadline/cancellation propagation and capture normalized result/usage/diagnostics.
  * Prevent handler access to runtime globals, raw StateStore, source roots, or unrestricted workspace paths through provided interfaces.
  * Return WorkResult without committing lifecycle state.

  Security and safety requirements

  * Only explicitly trusted policy-approved code runs in process.
  * Sanitize exception diagnostics and bound traceback/log output.
  * Cancellation and timeout cannot leave coordinator locks or partial authoritative writes.
  * Global mutable registries are frozen after composition.

  Edge cases and outliers to handle

  * Handler blocks event loop or ignores cancellation.
  * Handler raises BaseException or process-level error.
  * Registry changes during execution.
  * Handler returns outputs after deadline.

  Acceptance criteria (“done” definition)

  * A bundled analyzer produces identical normalized findings through WorkSpec/WorkResult.
  * Backend has no direct persistence/lifecycle mutation capability.
  * Timeout/cancel outcomes are explicit and later recovery-classifiable.
  * Registry and policy versions used are echoed and validated.

  Testing plan

  * Backend unit tests.
  * Trusted analyzer integration tests.
  * Cancellation/deadline tests.
  * Blocking/exception diagnostics tests.
  * Registry freeze/version tests.
  * Architecture tests for forbidden dependencies.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Backend unit tests., Trusted analyzer integration tests., Cancellation/deadline tests., Blocking/exception diagnostics tests., Registry freeze/version tests., Architecture tests for forbidden dependencies..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T15.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/inprocess.py::InProcessBackend, atlas/core/runtime.py, atlas/plugins/registry.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 59: Implement coordinator-side result validation and commit

  1.2 source task(s): `T15.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T15.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/lifecycle.py::accept_work_result (create); atlas/execution/validation.py (create); atlas/persistence/repositories/work_results.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Validate every WorkResult against attempt state, fencing, exact WorkSpec, schemas, budgets, output integrity, and cancellation before accepting findings or transitioning state.
  * Restore or protect this invariant: Only fully validated current results can change attempt/phase state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21.

  Where this applies

  * Primary affected components: `atlas/core/lifecycle.py::accept_work_result` (create: Own result validation and authoritative commit.); `atlas/execution/validation.py` (create: Validate spec/result/output/budget bindings.); `atlas/persistence/repositories/work_results.py` (create: Persist accepted/rejected result evidence.)
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

  * Validate every WorkResult against attempt state, fencing, exact WorkSpec, schemas, budgets, output integrity, and cancellation before accepting findings or transitioning state.
  * Component dispositions: `atlas/core/lifecycle.py::accept_work_result` (create: Own result validation and authoritative commit.); `atlas/execution/validation.py` (create: Validate spec/result/output/budget bindings.); `atlas/persistence/repositories/work_results.py` (create: Persist accepted/rejected result evidence.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Load expected attempt/work/spec digest and compare all echoed authority fields and fencing token.
  * Validate result schema, status, deadlines, usage, finding limits, output manifest, content identities, and workspace ownership.
  * Persist accepted or rejected result evidence, then invoke guarded attempt/phase transition in one transaction/event path.
  * Make duplicate identical results idempotent and conflicting duplicates/stale results explicit.

  Security and safety requirements

  * Never trust backend success, paths, byte counts, or hashes without core verification.
  * Rejected results cannot publish outputs, findings, or lifecycle changes.
  * Diagnostics are bounded/redacted and retained for incident review.
  * Cancellation or expired authority wins over late success unless deterministic reconciliation proves otherwise.

  Edge cases and outliers to handle

  * Identical result redelivered.
  * Conflicting result with same idempotency key.
  * Stale success after retry or cancel.
  * Output exists but usage or manifest exceeds budget.

  Acceptance criteria (“done” definition)

  * Only fully validated current results can change attempt/phase state.
  * Duplicate identical results have one authoritative effect.
  * Stale/malformed/conflicting results are retained and rejected with stable codes.
  * Output integrity and budgets are verified before downstream use.

  Testing plan

  * Validation unit/property tests.
  * Duplicate/conflicting result tests.
  * Stale fencing/cancel tests.
  * Output manifest corruption tests.
  * Budget overrun tests.
  * Transaction/event atomicity integration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Validation unit/property tests., Duplicate/conflicting result tests., Stale fencing/cancel tests., Output manifest corruption tests., Budget overrun tests., Transaction/event atomicity integration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T15.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/lifecycle.py::accept_work_result, atlas/execution/validation.py, atlas/persistence/repositories/work_results.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 60: Create the reusable backend conformance and fault suite

  1.2 source task(s): `T15.1.4`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T15.1.2, T15.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/execution/conformance.py (create); tests/execution/fixtures/ (create); atlas/execution/testing.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Define one test contract that every in-process, subprocess, local-pool, and remote backend must pass before it can execute governed work.
  * Restore or protect this invariant: InProcessBackend passes every applicable mandatory case.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21.

  Where this applies

  * Primary affected components: `tests/execution/conformance.py` (create: Host backend-neutral behavior and failure tests.); `tests/execution/fixtures/` (create: Provide deterministic plugins/specs/results/faults.); `atlas/execution/testing.py` (create: Expose test-only backend harness utilities.)
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

  * Define one test contract that every in-process, subprocess, local-pool, and remote backend must pass before it can execute governed work.
  * Component dispositions: `tests/execution/conformance.py` (create: Host backend-neutral behavior and failure tests.); `tests/execution/fixtures/` (create: Provide deterministic plugins/specs/results/faults.); `atlas/execution/testing.py` (create: Expose test-only backend harness utilities.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Test spec acceptance, result echo/schema, cancellation, deadline, progress, resource reporting, duplicate submission, stale fencing, output mediation, and health.
  * Inject backend crash/loss, malformed result, delayed result, partial output, cancellation race, and unavailable capability.
  * Compare normalized result semantics across backends for the same deterministic fixture.
  * Publish required versus platform-optional conformance cases and unsupported-control evidence.

  Security and safety requirements

  * Fixtures remain inert, bounded, and cannot access operator files/network.
  * A backend cannot skip mandatory authority/isolation tests because a control is inconvenient.
  * Platform skips require explicit capability evidence and affect deployment claims.
  * Conformance logs/fixtures contain no secrets.

  Edge cases and outliers to handle

  * Backend accepts duplicate spec concurrently.
  * Cancellation acknowledgement is lost.
  * Process/backend disappears after output write before result.
  * Unsupported CPU/memory control on one OS.

  Acceptance criteria (“done” definition)

  * InProcessBackend passes every applicable mandatory case.
  * The suite can be reused unchanged by subprocess and remote backends.
  * Unsupported controls are reported and block claims that they are enforced.
  * Fault cases produce deterministic coordinator outcomes.

  Testing plan

  * Backend conformance matrix.
  * Deterministic cross-backend result comparison.
  * Crash/loss/cancel fault tests.
  * Stale/duplicate submission tests.
  * Isolation/output mediation tests.
  * Platform capability reporting tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Backend conformance matrix., Deterministic cross-backend result comparison., Crash/loss/cancel fault tests., Stale/duplicate submission tests., Isolation/output mediation tests., Platform capability reporting tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T15.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/execution/conformance.py, tests/execution/fixtures/, atlas/execution/testing.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 61: Define durable `WorkItem` and phase-barrier semantics

  1.2 source task(s): `T16.1.1`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T8.1.4, T9.1.4, T12.1.4, T13.1.4, T15.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/work_items.py::WorkItem (create); atlas/core/work_planner.py (create); docs/architecture/work-items.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Model bounded fan-out/fan-in within one phase without introducing generic DAG semantics, alternate phase authority, or dynamic cross-phase dependencies.
  * Restore or protect this invariant: The model supports bounded parallelism while A-F order remains immutable.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend.

  Where this applies

  * Primary affected components: `atlas/models/work_items.py::WorkItem` (create: Represent phase-scoped units, dependencies, state, attempt, and result.); `atlas/core/work_planner.py` (create: Expand validated phase inputs into deterministic work sets.); `docs/architecture/work-items.md` (create: Define barrier, ordering, and non-DAG constraints.)
  * Epic boundary: Phase-internal work items, deterministic reuse, and unified budgets — Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Phase-internal work items, deterministic reuse, and unified budgets.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Model bounded fan-out/fan-in within one phase without introducing generic DAG semantics, alternate phase authority, or dynamic cross-phase dependencies.
  * Component dispositions: `atlas/models/work_items.py::WorkItem` (create: Represent phase-scoped units, dependencies, state, attempt, and result.); `atlas/core/work_planner.py` (create: Expand validated phase inputs into deterministic work sets.); `docs/architecture/work-items.md` (create: Define barrier, ordering, and non-DAG constraints.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define work item identity, phase run, operation/plugin, input references, parent/partition key, deterministic ordinal, state, attempt, dependencies limited to same phase, and result reference.
  * Define phase barrier completion: all required work items terminal and valid aggregation before next semantic phase.
  * Define bounded dynamic expansion only from verified work results with deterministic IDs and depth/count limits.
  * Define optional/skipped/failed item propagation without allowing work items to transition job/phase state directly.

  Security and safety requirements

  * Work-item inputs are immutable references and cannot add source paths or capabilities.
  * Dynamic expansion is bounded, validated, and cannot create cycles or cross-phase edges.
  * Only LifecycleCoordinator closes the phase barrier.
  * Untrusted plugin/model output cannot author new operations outside the allowed planner schema.

  Edge cases and outliers to handle

  * Zero items, one item, millions of items, duplicate deterministic IDs.
  * Required and optional items fail differently.
  * Expansion result arrives after cancel or retry.
  * Aggregator sees partial or conflicting item results.

  Acceptance criteria (“done” definition)

  * The model supports bounded parallelism while A-F order remains immutable.
  * Work-item IDs/order are deterministic for identical phase inputs.
  * Cross-phase dependencies and cycles are structurally impossible or rejected.
  * Barrier closure requires all declared invariants and aggregate validation.

  Testing plan

  * Model/schema tests.
  * Deterministic planning property tests.
  * Cycle/cross-phase negative tests.
  * Zero/large workset tests.
  * Dynamic expansion bound tests.
  * Barrier truth-table tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Model/schema tests., Deterministic planning property tests., Cycle/cross-phase negative tests., Zero/large workset tests., Dynamic expansion bound tests., Barrier truth-table tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T16.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/work_items.py::WorkItem, atlas/core/work_planner.py, docs/architecture/work-items.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 62: Implement the bounded local work-item scheduler and aggregation path

  1.2 source task(s): `T16.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T16.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/work_scheduler.py (create); atlas/persistence/repositories/work_items.py (create); atlas/core/work_aggregator.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Execute ready work items with explicit concurrency, fairness, cancellation, checkpoint, and resource limits, then validate and aggregate results before phase completion.
  * Restore or protect this invariant: Concurrency never exceeds configured/effective budgets.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend.

  Where this applies

  * Primary affected components: `atlas/core/work_scheduler.py` (create: Select and submit ready phase-scoped work items.); `atlas/persistence/repositories/work_items.py` (create: Persist work-item states and claims.); `atlas/core/work_aggregator.py` (create: Validate required outputs and phase aggregate.)
  * Epic boundary: Phase-internal work items, deterministic reuse, and unified budgets — Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Phase-internal work items, deterministic reuse, and unified budgets.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Execute ready work items with explicit concurrency, fairness, cancellation, checkpoint, and resource limits, then validate and aggregate results before phase completion.
  * Component dispositions: `atlas/core/work_scheduler.py` (create: Select and submit ready phase-scoped work items.); `atlas/persistence/repositories/work_items.py` (create: Persist work-item states and claims.); `atlas/core/work_aggregator.py` (create: Validate required outputs and phase aggregate.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Persist deterministic work plans and ready/running/terminal item states with claims/fencing.
  * Schedule only within current phase using configured per-job/per-phase/per-plugin concurrency and fair queueing.
  * Integrate control polling, cancellation, deadlines, retries, and checkpointable planner cursors.
  * Aggregate accepted results into phase outputs and close the barrier through LifecycleCoordinator.

  Security and safety requirements

  * No scheduler path bypasses WorkSpec, plugin policy, backend conformance, or resource budgets.
  * Queue size, in-memory ready set, and result aggregation are bounded.
  * Cancellation prevents new submissions and fences late results.
  * Fairness policy prevents one job/plugin from starving others.

  Edge cases and outliers to handle

  * Millions of work items exceed memory.
  * One item hangs while others finish.
  * Scheduler crashes after claim before submit.
  * Dynamic expansion floods queue near limits.

  Acceptance criteria (“done” definition)

  * Concurrency never exceeds configured/effective budgets.
  * Ready sets and aggregation remain bounded under large worksets.
  * Crash/restart does not duplicate accepted work effects.
  * Phase barrier closes only after deterministic aggregate validation.

  Testing plan

  * Scheduler unit tests.
  * Concurrency/fairness tests.
  * Million-item planning/streaming benchmark.
  * Crash-after-claim recovery tests.
  * Cancellation/late-result tests.
  * Aggregate partial/conflict tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Scheduler unit tests., Concurrency/fairness tests., Million-item planning/streaming benchmark., Crash-after-claim recovery tests., Cancellation/late-result tests., Aggregate partial/conflict tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T16.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/work_scheduler.py, atlas/persistence/repositories/work_items.py, atlas/core/work_aggregator.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 63: Implement exact-key deterministic result reuse

  1.2 source task(s): `T16.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T16.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/reuse.py::DeterministicResultIndex (create); atlas/core/reuse_service.py (create); analysis/structure work planners (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Avoid repeated deterministic analysis only when content, operation, plugin/tool/model, config, policy, schema, and relevant environment identities exactly match and outputs verify.
  * Restore or protect this invariant: Reuse occurs only under exact canonical key and verified outputs.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend.

  Where this applies

  * Primary affected components: `atlas/artifacts/reuse.py::DeterministicResultIndex` (create: Index reusable operation results by exact key.); `atlas/core/reuse_service.py` (create: Evaluate eligibility, verify outputs, and record reuse.); `analysis/structure work planners` (extend: Consult reuse without bypassing phase attempts.)
  * Epic boundary: Phase-internal work items, deterministic reuse, and unified budgets — Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Phase-internal work items, deterministic reuse, and unified budgets.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Avoid repeated deterministic analysis only when content, operation, plugin/tool/model, config, policy, schema, and relevant environment identities exactly match and outputs verify.
  * Component dispositions: `atlas/artifacts/reuse.py::DeterministicResultIndex` (create: Index reusable operation results by exact key.); `atlas/core/reuse_service.py` (create: Evaluate eligibility, verify outputs, and record reuse.); `analysis/structure work planners` (extend: Consult reuse without bypassing phase attempts.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define canonical operation key from operation/version, input identities, plugin/tool/model version, config/policy/registry/schema digests, deterministic flag, and declared environment inputs.
  * Persist result digest, output references, findings/report IDs, integrity status, and invalidation reason.
  * Before reuse, verify current policy, output existence/integrity, schema compatibility, and no prior incident.
  * Record a reuse decision/attempt tied to the current job rather than pretending the prior execution reran.

  Security and safety requirements

  * Non-deterministic or AI outputs default non-cacheable unless a stronger reproducibility contract is explicitly proven.
  * Cache keys cannot omit safety policy, model/prompt, external tool, or environment inputs that change output.
  * Corrupt/missing outputs invalidate reuse and create diagnostics.
  * Reuse never grants review or publication authority.

  Edge cases and outliers to handle

  * Plugin version unchanged but code/package hash changed.
  * Same content under new safety/config policy.
  * Output blob removed or retention changed.
  * Partial/failed result accidentally indexed.

  Acceptance criteria (“done” definition)

  * Reuse occurs only under exact canonical key and verified outputs.
  * Every reuse is attributable to original result and current decision.
  * Stale/missing/corrupt/non-deterministic results are not reused.
  * Metrics quantify hit rate and avoided work without losing occurrence provenance.

  Testing plan

  * Exact-key unit/property tests.
  * Omitted-key-component mutation tests.
  * Missing/corrupt output tests.
  * Package/model/prompt version tests.
  * Concurrent index lookup/commit tests.
  * Performance benchmark for duplicate-heavy runs.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Exact-key unit/property tests., Omitted-key-component mutation tests., Missing/corrupt output tests., Package/model/prompt version tests., Concurrent index lookup/commit tests., Performance benchmark for duplicate-heavy runs..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T16.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/reuse.py::DeterministicResultIndex, atlas/core/reuse_service.py, analysis/structure work planners.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 64: Implement a unified hierarchical `ResourceBudgetManager`

  1.2 source task(s): `T16.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T16.1.2, T16.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/resources/budgets.py::ResourceBudgetManager (create); atlas/core/context.py (extend); atlas/status/projection.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Reserve, account, enforce, and report time, CPU hints, memory, bytes read/written, temp space, files, processes, events, and concurrency across job, phase, work item, workspace, archive, and backend scopes.
  * Restore or protect this invariant: All core resource-consuming operations use scoped budget handles.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend.

  Where this applies

  * Primary affected components: `atlas/resources/budgets.py::ResourceBudgetManager` (create: Own hierarchical limits, reservations, accounting, and violations.); `atlas/core/context.py` (extend: Expose scoped budget handles.); `atlas/status/projection.py` (extend: Report limits, use, reservations, and blockers.)
  * Epic boundary: Phase-internal work items, deterministic reuse, and unified budgets — Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Phase-internal work items, deterministic reuse, and unified budgets.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Reserve, account, enforce, and report time, CPU hints, memory, bytes read/written, temp space, files, processes, events, and concurrency across job, phase, work item, workspace, archive, and backend scopes.
  * Component dispositions: `atlas/resources/budgets.py::ResourceBudgetManager` (create: Own hierarchical limits, reservations, accounting, and violations.); `atlas/core/context.py` (extend: Expose scoped budget handles.); `atlas/status/projection.py` (extend: Report limits, use, reservations, and blockers.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define budget dimensions, hierarchy/inheritance, reservation/commit/release, soft versus hard limits, and platform-enforceability metadata.
  * Integrate archive, workspace, hashing, event, scheduler, plugin, and backend accounting with one scoped API.
  * Persist authoritative counters/reservations needed for restart and reconcile abandoned reservations.
  * Define deterministic behavior on soft warning, hard exceed, unknown usage, and unsupported enforcement.

  Security and safety requirements

  * Untrusted plugins/backends cannot increase their budgets or under-report usage without core verification where possible.
  * Hard-limit violation cancels/contains work and records exact dimension/scope.
  * Unsupported OS controls are visible and cannot be advertised as enforced.
  * Counters and labels are bounded to prevent telemetry/storage DoS.

  Edge cases and outliers to handle

  * Nested archive and subprocess consume the same temp quota.
  * Concurrent work items race on shared job budget.
  * Crash leaves reservations but no live work.
  * Actual memory/CPU cannot be measured reliably on a platform.

  Acceptance criteria (“done” definition)

  * All core resource-consuming operations use scoped budget handles.
  * Concurrent reservations cannot exceed hard shared limits.
  * Restart reconciliation clears or transfers abandoned reservations deterministically.
  * Status and diagnostics distinguish requested, reserved, used, exceeded, and unenforceable.

  Testing plan

  * Budget hierarchy unit/property tests.
  * Concurrent reservation tests.
  * Crash/orphan reservation reconciliation tests.
  * Cross-subsystem shared quota tests.
  * Unsupported-control reporting tests.
  * Resource-exhaustion integration/soak tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Budget hierarchy unit/property tests., Concurrent reservation tests., Crash/orphan reservation reconciliation tests., Cross-subsystem shared quota tests., Unsupported-control reporting tests., Resource-exhaustion integration/soak tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T16.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/resources/budgets.py::ResourceBudgetManager, atlas/core/context.py, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 65: Persist normalized analysis findings and typed relationships

  1.2 source task(s): `T17.1.1`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T7.1.4, T8.1.4, T13.1.4, T14.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/findings.py::AnalysisFinding (create); atlas/review/repository.py::FindingRepository (create); atlas/phases/analyze.py (refactor); atlas/schema/migrations/*_analysis_findings.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace transient analyzer dictionaries with versioned, queryable `AnalysisFinding` records that remain non-authoritative claims linked to exact inputs, plugin versions, phase attempts, and deterministic relationship types.
  * Restore or protect this invariant: Every persisted finding identifies exact input content, analyzer/plugin version, configuration digest, phase attempt, and schema version.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31.

  Where this applies

  * Primary affected components: `atlas/models/findings.py::AnalysisFinding` (create: Define the durable finding identity, subject, predicate/type, value, confidence, provenance, and status contract.); `atlas/review/repository.py::FindingRepository` (create: Persist and query findings without granting them review or publication authority.); `atlas/phases/analyze.py` (refactor: Normalize analyzer results through the finding contract while preserving a compatibility projection.); `atlas/schema/migrations/*_analysis_findings.sql` (create: Create versioned tables, indexes, constraints, and legacy migration fields.)
  * Epic boundary: Durable findings, evidence, review, and publication — Separate analytical output from evidence, trust decisions, and externally verified publications while preserving exact-byte lineage and fail-closed authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].
  * Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-015 requires: Review currently produces transient candidates rather than durable approve/reject/hold decisions and verifiable publications.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace transient analyzer dictionaries with versioned, queryable `AnalysisFinding` records that remain non-authoritative claims linked to exact inputs, plugin versions, phase attempts, and deterministic relationship types.
  * Component dispositions: `atlas/models/findings.py::AnalysisFinding` (create: Define the durable finding identity, subject, predicate/type, value, confidence, provenance, and status contract.); `atlas/review/repository.py::FindingRepository` (create: Persist and query findings without granting them review or publication authority.); `atlas/phases/analyze.py` (refactor: Normalize analyzer results through the finding contract while preserving a compatibility projection.); `atlas/schema/migrations/*_analysis_findings.sql` (create: Create versioned tables, indexes, constraints, and legacy migration fields.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define stable finding IDs, finding schema version, content/derived-artifact subject, analyzer and plugin-version identity, attempt/work-item origin, confidence/uncertainty, observed time, and supersession state.
  * Define a closed initial relationship vocabulary plus an extension namespace; reject unknown unversioned relationship semantics.
  * Persist findings transactionally with the phase result and durable event; expose deterministic ordering and pagination.
  * Keep legacy metadata output as a derived compatibility view and mark unmappable legacy records as `authority=none`.

  Security and safety requirements

  * Treat plugin and AI output as untrusted claims; validate types, sizes, encodings, identifiers, and relationship namespaces before persistence.
  * Do not permit finding payloads to contain executable commands, destination credentials, lifecycle transitions, or direct publication instructions.
  * Bound free-text and binary-derived samples; redact or reference sensitive values rather than copying them into logs/events.
  * Make analyzer identity, code/config digest, input content identity, and attempt lineage tamper-evident in the record.

  Edge cases and outliers to handle

  * Duplicate findings from the same and different analyzers.
  * Conflicting or low-confidence findings.
  * Analyzer emits malformed, oversized, cyclic, or self-referential relationships.
  * Legacy analyzer omits version, confidence, or subject identity.

  Acceptance criteria (“done” definition)

  * Every persisted finding identifies exact input content, analyzer/plugin version, configuration digest, phase attempt, and schema version.
  * Finding persistence cannot create evidence, a promotion decision, or a publication.
  * Duplicate policy and supersession behavior are deterministic and documented.
  * Legacy findings remain readable without being misrepresented as approved knowledge.

  Testing plan

  * Schema and repository unit tests.
  * Analyzer-contract integration tests.
  * Malformed/oversized output negative tests.
  * Duplicate/conflict property tests.
  * Legacy compatibility fixture tests.
  * Transaction/event atomicity tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Schema and repository unit tests., Analyzer-contract integration tests., Malformed/oversized output negative tests., Duplicate/conflict property tests., Legacy compatibility fixture tests., Transaction/event atomicity tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T17.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/findings.py::AnalysisFinding, atlas/review/repository.py::FindingRepository, atlas/phases/analyze.py, atlas/schema/migrations/*_analysis_findings.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 66: Define and persist evidence records with explicit provenance and confidence

  1.2 source task(s): `T17.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T17.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/evidence.py::EvidenceRecord (create); atlas/review/evidence.py::EvidenceService (create); atlas/review/repository.py::EvidenceRepository (create); atlas/schema/migrations/*_evidence.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create an evidence layer that cites immutable observations, structural reports, extraction records, findings, and verifier outputs without collapsing them into a final trust decision.
  * Restore or protect this invariant: Evidence-set digests are stable under deterministic canonical ordering and change when any cited record changes.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31.

  Where this applies

  * Primary affected components: `atlas/models/evidence.py::EvidenceRecord` (create: Define evidence types, cited subjects, source records, verifier, confidence, validity, and supersession.); `atlas/review/evidence.py::EvidenceService` (create: Validate, assemble, digest, and query exact evidence sets.); `atlas/review/repository.py::EvidenceRepository` (create: Persist evidence and citations with immutable lineage.); `atlas/schema/migrations/*_evidence.sql` (create: Add evidence, citation, digest, and supersession tables.)
  * Epic boundary: Durable findings, evidence, review, and publication — Separate analytical output from evidence, trust decisions, and externally verified publications while preserving exact-byte lineage and fail-closed authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].
  * Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-015 requires: Review currently produces transient candidates rather than durable approve/reject/hold decisions and verifiable publications.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create an evidence layer that cites immutable observations, structural reports, extraction records, findings, and verifier outputs without collapsing them into a final trust decision.
  * Component dispositions: `atlas/models/evidence.py::EvidenceRecord` (create: Define evidence types, cited subjects, source records, verifier, confidence, validity, and supersession.); `atlas/review/evidence.py::EvidenceService` (create: Validate, assemble, digest, and query exact evidence sets.); `atlas/review/repository.py::EvidenceRepository` (create: Persist evidence and citations with immutable lineage.); `atlas/schema/migrations/*_evidence.sql` (create: Add evidence, citation, digest, and supersession tables.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define evidence classes for deterministic observation, structural validation, extraction verification, analyzer corroboration, policy evaluation, and external verification.
  * Require every evidence record to cite one or more immutable source records and an exact subject identity.
  * Compute a canonical evidence-record digest and an ordered evidence-set digest for review binding.
  * Define validity, expiry where applicable, revocation/supersession, and provenance-completeness rules without rewriting history.

  Security and safety requirements

  * Deterministic framework evidence outranks unverified model/plugin assertions for safety and lifecycle decisions.
  * Reject citations to missing, mutable, cross-job, or incompatible-schema records unless an explicit import/provenance contract exists.
  * Never embed secrets, full raw content, or unbounded analyzer text in evidence; use immutable references and bounded summaries.
  * Record actor/verifier identity and policy/tool/configuration digests for every evidence creation or supersession action.

  Edge cases and outliers to handle

  * Evidence cites a finding later superseded.
  * Two records claim incompatible facts about one content identity.
  * Evidence set contains duplicate or differently ordered citations.
  * Verifier fails after creating some evidence inputs.

  Acceptance criteria (“done” definition)

  * Evidence-set digests are stable under deterministic canonical ordering and change when any cited record changes.
  * Every evidence record resolves to immutable source observations or explicitly labeled external authority.
  * Unverified findings cannot silently become deterministic evidence.
  * Superseded evidence remains queryable and cannot satisfy a current-decision policy unless allowed explicitly.

  Testing plan

  * Canonical digest golden tests.
  * Citation integrity and foreign-key tests.
  * Conflicting/superseded evidence tests.
  * Missing/mutable citation negative tests.
  * Verifier transaction/failure tests.
  * Lineage-query integration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Canonical digest golden tests., Citation integrity and foreign-key tests., Conflicting/superseded evidence tests., Missing/mutable citation negative tests., Verifier transaction/failure tests., Lineage-query integration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T17.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/evidence.py::EvidenceRecord, atlas/review/evidence.py::EvidenceService, atlas/review/repository.py::EvidenceRepository, atlas/schema/migrations/*_evidence.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 67: Implement evidence-bound promotion decisions and review policy

  1.2 source task(s): `T17.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T17.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/review.py::PromotionDecision (create); atlas/review/service.py::ReviewService (create); atlas/review/policy.py::ReviewPolicy (create); atlas/phases/review.py (refactor); atlas/schema/migrations/*_promotion_decisions.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create durable `APPROVE`, `REJECT`, and `HOLD` decisions that bind an actor and policy version to an exact current evidence set and never treat analyzer or AI output as final authority.
  * Restore or protect this invariant: Only one current decision is authoritative for a subject/policy scope.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31.

  Where this applies

  * Primary affected components: `atlas/models/review.py::PromotionDecision` (create: Define decision state, subject, evidence-set digest, actor/policy identity, reason, validity, and supersession.); `atlas/review/service.py::ReviewService` (create: Evaluate policy, record review requests, and persist guarded decisions.); `atlas/review/policy.py::ReviewPolicy` (create: Separate deterministic framework mechanisms from deployment-specific approval policy.); `atlas/phases/review.py` (refactor: Replace transient promotion candidates with durable review requests and compatibility summaries.); `atlas/schema/migrations/*_promotion_decisions.sql` (create: Persist review requests, decisions, actors, policies, and supersession history.)
  * Epic boundary: Durable findings, evidence, review, and publication — Separate analytical output from evidence, trust decisions, and externally verified publications while preserving exact-byte lineage and fail-closed authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].
  * Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-015 requires: Review currently produces transient candidates rather than durable approve/reject/hold decisions and verifiable publications.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create durable `APPROVE`, `REJECT`, and `HOLD` decisions that bind an actor and policy version to an exact current evidence set and never treat analyzer or AI output as final authority.
  * Component dispositions: `atlas/models/review.py::PromotionDecision` (create: Define decision state, subject, evidence-set digest, actor/policy identity, reason, validity, and supersession.); `atlas/review/service.py::ReviewService` (create: Evaluate policy, record review requests, and persist guarded decisions.); `atlas/review/policy.py::ReviewPolicy` (create: Separate deterministic framework mechanisms from deployment-specific approval policy.); `atlas/phases/review.py` (refactor: Replace transient promotion candidates with durable review requests and compatibility summaries.); `atlas/schema/migrations/*_promotion_decisions.sql` (create: Persist review requests, decisions, actors, policies, and supersession history.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define which harmless local outcomes may receive deterministic policy decisions and which publication classes require an attributed human or external authority.
  * Bind every decision to subject identity, evidence-set digest, policy ID/version/digest, actor type/ID, reason code/text, time, and predecessor when superseding.
  * Reject stale decision attempts if the evidence set, subject version, policy, or lifecycle version changed.
  * Expose a versioned review command through canonical `CommandService`; no plugin, model, event consumer, or destination adapter may write decisions directly.

  Security and safety requirements

  * AI and plugins may propose classifications or reasons but cannot be the sole actor for final promotion.
  * Require authorization as an optional deployment adapter for consequential decisions while preserving local single-operator usability.
  * Use optimistic version/fencing and idempotency keys to prevent replayed or concurrent review commands.
  * Audit actor, request, policy evaluation, denied action, decision, supersession, and current-authority resolution.

  Edge cases and outliers to handle

  * Concurrent approve and reject.
  * Evidence changes while a reviewer has stale UI/CLI state.
  * Policy version is retired or unavailable.
  * Imported legacy candidate has no actor or evidence-set digest.

  Acceptance criteria (“done” definition)

  * Only one current decision is authoritative for a subject/policy scope.
  * `REJECT` and `HOLD` structurally block publication.
  * A stale or replayed review command cannot overwrite a newer decision.
  * The deployment-specific rule for interactive versus automatic review is resolved and documented before publication is enabled.

  Testing plan

  * State/transition table tests.
  * Concurrent review and stale-version tests.
  * Policy adapter conformance tests.
  * AI/plugin authority negative tests.
  * Legacy candidate migration tests.
  * Audit and status projection tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: State/transition table tests., Concurrent review and stale-version tests., Policy adapter conformance tests., AI/plugin authority negative tests., Legacy candidate migration tests., Audit and status projection tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T17.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/review.py::PromotionDecision, atlas/review/service.py::ReviewService, atlas/review/policy.py::ReviewPolicy, atlas/phases/review.py, atlas/schema/migrations/*_promotion_decisions.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 68: Implement staged idempotent publication and bidirectional lineage

  1.2 source task(s): `T17.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T17.1.2, T17.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/publication.py (create); atlas/review/publication.py::PublicationCoordinator (create); atlas/review/adapters.py::PublicationAdapter (create); atlas/schema/migrations/*_publications.sql (create); atlas/cli.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Publish only after a current authorized decision, using staged writes, exact idempotency identity, destination verification, unknown-outcome reconciliation, and a complete path back to source bytes.
  * Restore or protect this invariant: No publication begins without a current authorized `APPROVE` decision bound to the exact evidence set.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31.

  Where this applies

  * Primary affected components: `atlas/models/publication.py` (create: Define `PublicationRequest`, `PublicationAttempt`, and `DestinationPublication` records.); `atlas/review/publication.py::PublicationCoordinator` (create: Own request validation, attempt state, adapter execution, verification, and reconciliation.); `atlas/review/adapters.py::PublicationAdapter` (create: Define versioned destination capability and no-replace/expected-replace contracts.); `atlas/schema/migrations/*_publications.sql` (create: Persist publication requests, attempts, destination identities, verification, and lineage.); `atlas/cli.py` (extend: Expose submit/status/reconcile commands through canonical services without direct destination writes.)
  * Epic boundary: Durable findings, evidence, review, and publication — Separate analytical output from evidence, trust decisions, and externally verified publications while preserving exact-byte lineage and fail-closed authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].
  * Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-015 requires: Review currently produces transient candidates rather than durable approve/reject/hold decisions and verifiable publications.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Publish only after a current authorized decision, using staged writes, exact idempotency identity, destination verification, unknown-outcome reconciliation, and a complete path back to source bytes.
  * Component dispositions: `atlas/models/publication.py` (create: Define `PublicationRequest`, `PublicationAttempt`, and `DestinationPublication` records.); `atlas/review/publication.py::PublicationCoordinator` (create: Own request validation, attempt state, adapter execution, verification, and reconciliation.); `atlas/review/adapters.py::PublicationAdapter` (create: Define versioned destination capability and no-replace/expected-replace contracts.); `atlas/schema/migrations/*_publications.sql` (create: Persist publication requests, attempts, destination identities, verification, and lineage.); `atlas/cli.py` (extend: Expose submit/status/reconcile commands through canonical services without direct destination writes.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Validate a current `APPROVE` decision, exact evidence-set digest, subject content identity, destination policy, and adapter capability before creating an attempt.
  * Derive a stable idempotency key from publication request identity and persist it before any external side effect.
  * Stage destination content/metadata, commit with no-replace or explicit expected-replace semantics, then independently verify bytes and destination identity.
  * Record `SUCCEEDED`, `FAILED`, or `UNKNOWN/RECONCILIATION_REQUIRED`; never infer destination success from a request or transport acknowledgement.
  * Expose forward and reverse lineage queries from source occurrence/content through derived records to every verified publication.

  Security and safety requirements

  * Resolve destinations through typed adapters; never concatenate untrusted paths, shell commands, SQL, URLs, or credentials.
  * Use least-privilege secret references and capability grants; keep secrets out of request/event/audit payloads.
  * Fence stale attempts and reject unauthorized or policy-incompatible adapters.
  * For unknown external outcomes, query by exact idempotency/destination identity before retrying; fail closed when verification is impossible.

  Edge cases and outliers to handle

  * Destination already exists with same or different bytes.
  * Timeout occurs after remote commit but before response.
  * Partial staged upload, verifier outage, or destination rollback.
  * Decision/evidence becomes stale before or during publication.

  Acceptance criteria (“done” definition)

  * No publication begins without a current authorized `APPROVE` decision bound to the exact evidence set.
  * Duplicate requests converge on one verified destination effect or a deterministic conflict.
  * Unknown outcome is reconciled rather than blindly repeated.
  * Every verified publication resolves bidirectionally to source root, intake generation, occurrence, exact content, derivations, findings, evidence, decision, actor, policy, and attempt.

  Testing plan

  * Approve/reject/hold end-to-end tests.
  * Idempotency and duplicate-request tests.
  * Partial/timeout/unknown-outcome fault injection.
  * No-replace and expected-replace tests.
  * Unauthorized/path/command-injection negative tests.
  * Bidirectional lineage and legacy compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Approve/reject/hold end-to-end tests., Idempotency and duplicate-request tests., Partial/timeout/unknown-outcome fault injection., No-replace and expected-replace tests., Unauthorized/path/command-injection negative tests., Bidirectional lineage and legacy compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T17.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/publication.py, atlas/review/publication.py::PublicationCoordinator, atlas/review/adapters.py::PublicationAdapter, atlas/schema/migrations/*_publications.sql, atlas/cli.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 69: Define the error taxonomy and operation-semantics registry

  1.2 source task(s): `T18.1.1`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T9.1.4, T15.1.4, T17.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/errors.py::AtlasError (refactor); atlas/recovery/semantics.py::OperationSemantics (create); atlas/recovery/registry.py::OperationSemanticsRegistry (create); docs/operations/operation-semantics.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Give every built-in operation a typed failure class and explicit semantics for restartability, checkpoints, idempotent side effects, external reconciliation, and unsafe unknown outcomes.
  * Restore or protect this invariant: Every built-in operation has exactly one current, versioned semantics classification.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27.

  Where this applies

  * Primary affected components: `atlas/errors.py::AtlasError` (refactor: Create stable categories, reason codes, retry hints, safe operator text, and causation fields.); `atlas/recovery/semantics.py::OperationSemantics` (create: Declare duplicate-effect, checkpoint, timeout, reconciliation, and compensation behavior.); `atlas/recovery/registry.py::OperationSemanticsRegistry` (create: Provide deterministic registration and compatibility validation.); `docs/operations/operation-semantics.md` (create: Document classifications for every built-in phase and consequential helper.)
  * Epic boundary: Retry, timeout, idempotency, reconciliation, and crash recovery — Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.
  * Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-016 requires: Replay is unsafe unless each operation declares duplicate effects, checkpoints, and unknown-outcome handling.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Give every built-in operation a typed failure class and explicit semantics for restartability, checkpoints, idempotent side effects, external reconciliation, and unsafe unknown outcomes.
  * Component dispositions: `atlas/errors.py::AtlasError` (refactor: Create stable categories, reason codes, retry hints, safe operator text, and causation fields.); `atlas/recovery/semantics.py::OperationSemantics` (create: Declare duplicate-effect, checkpoint, timeout, reconciliation, and compensation behavior.); `atlas/recovery/registry.py::OperationSemanticsRegistry` (create: Provide deterministic registration and compatibility validation.); `docs/operations/operation-semantics.md` (create: Document classifications for every built-in phase and consequential helper.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define error categories for validation, policy, input mutation, resource limit, timeout, cancellation, dependency, persistence, protocol, plugin, invariant, and unknown external outcome.
  * Classify each built-in operation as pure/restartable, checkpoint-resumable, idempotent side effect, externally reconcilable side effect, or non-retriable/manual.
  * Require operation semantics ID/version/digest in phase/plugin descriptors and persisted attempts.
  * Map legacy exceptions conservatively and preserve original causes without exposing secrets or raw payloads.

  Security and safety requirements

  * Do not let plugins declare stronger safety semantics than policy permits; registry validation can downgrade or reject.
  * Never classify an unknown external mutation as retryable by default.
  * Sanitize exception text and structured context before persistence/logging.
  * Record semantic version/digest so a restarted job cannot silently use changed duplicate-effect rules.

  Edge cases and outliers to handle

  * One operation raises multiple nested error categories.
  * Plugin version changes semantics between attempts.
  * Legacy error has no code or retry hint.
  * Cancellation races with timeout or external side effect.

  Acceptance criteria (“done” definition)

  * Every built-in operation has exactly one current, versioned semantics classification.
  * Unknown/unregistered semantics block automatic retry.
  * Error codes are stable, serializable, and safe for API/event/log projection.
  * Policy can prove why an outcome is retryable, blocked, terminal, or requires reconciliation.

  Testing plan

  * Registry completeness tests.
  * Error serialization/golden tests.
  * Legacy exception mapping tests.
  * Plugin overclaim negative tests.
  * Semantics-version compatibility tests.
  * Secret-redaction tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Registry completeness tests., Error serialization/golden tests., Legacy exception mapping tests., Plugin overclaim negative tests., Semantics-version compatibility tests., Secret-redaction tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T18.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/errors.py::AtlasError, atlas/recovery/semantics.py::OperationSemantics, atlas/recovery/registry.py::OperationSemanticsRegistry, docs/operations/operation-semantics.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 70: Implement retry, deadline, timeout, and idempotency policy

  1.2 source task(s): `T18.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T18.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/recovery/policy.py::RetryPolicyResolver (create); atlas/recovery/idempotency.py::IdempotencyService (create); atlas/core/coordinator.py (extend); atlas/schema/migrations/*_recovery_policy.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create bounded retry decisions that derive from operation semantics, attempt history, verified checkpoints, deadlines, and idempotency identity rather than ad hoc exception handling.
  * Restore or protect this invariant: Retry decisions are deterministic for the same durable state and policy version.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27.

  Where this applies

  * Primary affected components: `atlas/recovery/policy.py::RetryPolicyResolver` (create: Compute retry/block/fail/reconcile decisions and bounded schedules.); `atlas/recovery/idempotency.py::IdempotencyService` (create: Reserve, look up, and finalize operation-level idempotency records.); `atlas/core/coordinator.py` (extend: Create successor attempts and enforce deadlines without mutating predecessor history.); `atlas/schema/migrations/*_recovery_policy.sql` (create: Persist idempotency, retry schedule, deadline, and recovery reason.)
  * Epic boundary: Retry, timeout, idempotency, reconciliation, and crash recovery — Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.
  * Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-016 requires: Replay is unsafe unless each operation declares duplicate effects, checkpoints, and unknown-outcome handling.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create bounded retry decisions that derive from operation semantics, attempt history, verified checkpoints, deadlines, and idempotency identity rather than ad hoc exception handling.
  * Component dispositions: `atlas/recovery/policy.py::RetryPolicyResolver` (create: Compute retry/block/fail/reconcile decisions and bounded schedules.); `atlas/recovery/idempotency.py::IdempotencyService` (create: Reserve, look up, and finalize operation-level idempotency records.); `atlas/core/coordinator.py` (extend: Create successor attempts and enforce deadlines without mutating predecessor history.); `atlas/schema/migrations/*_recovery_policy.sql` (create: Persist idempotency, retry schedule, deadline, and recovery reason.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define maximum attempts, bounded exponential backoff/jitter, total deadline, per-attempt timeout, retry budget, and dependency-specific circuit behavior.
  * Generate or validate idempotency keys from stable operation identity and immutable inputs before side effects.
  * Create a new attempt for every retry and link predecessor, reason, checkpoint, policy version, and next eligible time.
  * Ensure cancellation and pause requests take precedence at defined safe points and cannot be lost inside retry sleep.

  Security and safety requirements

  * Bound retries and jitter to prevent retry storms and deliberate resource amplification.
  * Do not expose idempotency keys as authorization credentials; scope them to job/operation/version.
  * Reject replay across tenant/deployment/source scope where optional deployment identity applies.
  * Timeout handling must revoke/fence the attempt and verify child/external operation state before successor execution.

  Edge cases and outliers to handle

  * Host restarts during backoff.
  * Clock moves backward/forward or differs from remote dependency.
  * Timeout fires while operation actually committed.
  * Multiple coordinators schedule the same retry.

  Acceptance criteria (“done” definition)

  * Retry decisions are deterministic for the same durable state and policy version.
  * No unsafe or unknown-outcome operation is automatically retried.
  * Duplicate idempotency identity returns the prior canonical result or conflict rather than repeating an effect.
  * Attempt/deadline/backoff state survives process restart.

  Testing plan

  * Retry policy truth-table tests.
  * Backoff/jitter bounded property tests.
  * Concurrent idempotency reservation tests.
  * Timeout-versus-commit race tests.
  * Restart-during-backoff tests.
  * Cancellation/pause precedence tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Retry policy truth-table tests., Backoff/jitter bounded property tests., Concurrent idempotency reservation tests., Timeout-versus-commit race tests., Restart-during-backoff tests., Cancellation/pause precedence tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T18.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/recovery/policy.py::RetryPolicyResolver, atlas/recovery/idempotency.py::IdempotencyService, atlas/core/coordinator.py, atlas/schema/migrations/*_recovery_policy.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 71: Implement startup reconciliation and deterministic recovery decisions

  1.2 source task(s): `T18.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T18.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/recovery/service.py::RecoveryService (create); atlas/recovery/reconcilers.py (create); atlas/core/runtime.py (extend); atlas/status/projection.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Scan nonterminal jobs, phase runs, attempts, controls, work items, checkpoints, workspaces, and publications after restart and choose exactly one safe action from durable evidence.
  * Restore or protect this invariant: Each nonterminal attempt maps to one persisted recovery disposition.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27.

  Where this applies

  * Primary affected components: `atlas/recovery/service.py::RecoveryService` (create: Inspect durable state and emit resume/retry/reconcile/block/fail decisions.); `atlas/recovery/reconcilers.py` (create: Host operation-specific and external-effect reconciliation adapters.); `atlas/core/runtime.py` (extend: Invoke recovery before claiming new work and expose a recovery summary.); `atlas/status/projection.py` (extend: Show recovery requirement, reason, evidence, and operator action.)
  * Epic boundary: Retry, timeout, idempotency, reconciliation, and crash recovery — Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.
  * Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-016 requires: Replay is unsafe unless each operation declares duplicate effects, checkpoints, and unknown-outcome handling.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Scan nonterminal jobs, phase runs, attempts, controls, work items, checkpoints, workspaces, and publications after restart and choose exactly one safe action from durable evidence.
  * Component dispositions: `atlas/recovery/service.py::RecoveryService` (create: Inspect durable state and emit resume/retry/reconcile/block/fail decisions.); `atlas/recovery/reconcilers.py` (create: Host operation-specific and external-effect reconciliation adapters.); `atlas/core/runtime.py` (extend: Invoke recovery before claiming new work and expose a recovery summary.); `atlas/status/projection.py` (extend: Show recovery requirement, reason, evidence, and operator action.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define startup scan order and snapshot/transaction boundaries so recovery does not race normal claims.
  * Validate checkpoint schema/config/input/content/attempt lineage before resuming.
  * Reconcile staged workspaces, orphan child processes where observable, outbox state, idempotency records, and external publication attempts.
  * Persist one `RecoveryDecision` with reason, evidence, policy/semantics version, and successor action before execution.
  * Conservatively block legacy nonterminal jobs whose safe continuation cannot be established.

  Security and safety requirements

  * Recovery cannot trust stale in-memory maps, unverified files, model output, or transport events.
  * Use least-privilege external reconciliation and exact destination/idempotency identities.
  * Fence stale owners before accepting results or deleting resources.
  * Preserve failed/unknown evidence; cleanup cannot erase information needed to determine duplicate effects.

  Edge cases and outliers to handle

  * Database is partially corrupted or migration incomplete.
  * Checkpoint exists but source/content/config/plugin changed.
  * External service is unavailable during reconciliation.
  * Repeated restart occurs while a recovery action is in progress.

  Acceptance criteria (“done” definition)

  * Each nonterminal attempt maps to one persisted recovery disposition.
  * Unsafe or insufficient evidence becomes `BLOCKED/RECONCILIATION_REQUIRED`, never guessed success.
  * Repeated startup converges without duplicating the selected action.
  * Recovery summary identifies exact job/phase/attempt/checkpoint/effect boundary and next operator action.

  Testing plan

  * Recovery decision table tests.
  * Repeated-start idempotency tests.
  * Stale checkpoint/source/plugin tests.
  * External outage/unknown publication tests.
  * Legacy job conservative migration tests.
  * Corrupt-state and partial-migration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Recovery decision table tests., Repeated-start idempotency tests., Stale checkpoint/source/plugin tests., External outage/unknown publication tests., Legacy job conservative migration tests., Corrupt-state and partial-migration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T18.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/recovery/service.py::RecoveryService, atlas/recovery/reconcilers.py, atlas/core/runtime.py, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 72: Build the phase-by-phase crash and replay verification matrix

  1.2 source task(s): `T18.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T18.1.2, T18.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/faults/crash_matrix/ (create); tests/integration/test_recovery_matrix.py (create); scripts/run_recovery_matrix.py (create); docs/operations/recovery-matrix.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prove recovery behavior at transaction, checkpoint, materialization, plugin, event, control, and publication boundaries for every built-in phase and operation class.
  * Restore or protect this invariant: The matrix covers all built-in phases and every declared operation-semantics class.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27.

  Where this applies

  * Primary affected components: `tests/faults/crash_matrix/` (create: Store deterministic fault points, fixtures, expected recovery decisions, and evidence.); `tests/integration/test_recovery_matrix.py` (create: Run multi-process kill/restart and replay scenarios.); `scripts/run_recovery_matrix.py` (create: Execute and summarize the matrix in CI/operator environments.); `docs/operations/recovery-matrix.md` (create: Document supported outcomes, gaps, and manual recovery.)
  * Epic boundary: Retry, timeout, idempotency, reconciliation, and crash recovery — Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.
  * Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-016 requires: Replay is unsafe unless each operation declares duplicate effects, checkpoints, and unknown-outcome handling.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prove recovery behavior at transaction, checkpoint, materialization, plugin, event, control, and publication boundaries for every built-in phase and operation class.
  * Component dispositions: `tests/faults/crash_matrix/` (create: Store deterministic fault points, fixtures, expected recovery decisions, and evidence.); `tests/integration/test_recovery_matrix.py` (create: Run multi-process kill/restart and replay scenarios.); `scripts/run_recovery_matrix.py` (create: Execute and summarize the matrix in CI/operator environments.); `docs/operations/recovery-matrix.md` (create: Document supported outcomes, gaps, and manual recovery.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Enumerate fault points immediately before and after each authoritative transaction, filesystem commit, checkpoint, plugin launch/result, outbox write, and external publication boundary.
  * For each fault point define expected durable rows/files, allowed duplicate effects, recovery decision, cleanup, and retained evidence.
  * Run repeated restart and duplicate-delivery scenarios, not only one crash.
  * Produce machine-readable results tied to schema, code, fixture, platform, and operation-semantics versions.

  Security and safety requirements

  * Use isolated temporary roots and fake/replayable external adapters; never point fault tests at production destinations.
  * Include malicious/stale checkpoint, forged result, stale fencing, and event-injection scenarios.
  * Secret and payload fixtures must be synthetic and scanned before retention.
  * A skipped platform control must be explicit, owned, and cannot count as proof.

  Edge cases and outliers to handle

  * Kill occurs while SQLite lock or fsync is pending.
  * Disk-full or permission error masks the intended crash point.
  * Flaky timing makes a result nondeterministic.
  * Cleanup removes evidence before assertions.

  Acceptance criteria (“done” definition)

  * The matrix covers all built-in phases and every declared operation-semantics class.
  * Each fault point produces exactly the documented recovery disposition across repeated clean runs.
  * No unsafe side effect is repeated and no unknown outcome is reported as success.
  * CI publishes machine-readable crash/replay evidence and blocks regressions for mandatory platforms.

  Testing plan

  * Fault-injection unit tests.
  * Multi-process crash/restart integration tests.
  * Replay/idempotency property tests.
  * Disk/lock/dependency fault tests.
  * Stale fencing/forged result security tests.
  * Evidence determinism and secret-scan tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Fault-injection unit tests., Multi-process crash/restart integration tests., Replay/idempotency property tests., Disk/lock/dependency fault tests., Stale fencing/forged result security tests., Evidence determinism and secret-scan tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T18.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/faults/crash_matrix/, tests/integration/test_recovery_matrix.py, scripts/run_recovery_matrix.py, docs/operations/recovery-matrix.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 73: Define the daemon lifecycle, configuration, and ownership contract

  1.2 source task(s): `T19.1.1`
  Priority: `P1`
  Estimated effort: `12 hours`
  Dependencies: `T5.1.4, T9.1.4, T18.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/service/daemon.py::AtlasDaemon (create); atlas/service/config.py::DaemonConfig (create); atlas/core/runtime.py (refactor); docs/operations/daemon.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify a single local service that owns active execution, recovers durable jobs, and exposes explicit startup, readiness, drain, shutdown, and embedded-mode semantics.
  * Restore or protect this invariant: Readiness is false until store, migration, recovery, and ownership checks succeed.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/service/daemon.py::AtlasDaemon` (create: Own service lifecycle, claim loop, recovery startup, drain, and shutdown.); `atlas/service/config.py::DaemonConfig` (create: Define typed local service, polling, lease, shutdown, and IPC configuration.); `atlas/core/runtime.py` (refactor: Separate composition from process lifetime and provide daemon/embedded construction modes.); `docs/operations/daemon.md` (create: Document ownership, service modes, installation, and failure behavior.)
  * Epic boundary: Long-running local runtime ownership — Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.
  * Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-017 requires: A CLI process cannot durably own jobs or honor controls from another process; hydrating private `_jobs` is not control.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify a single local service that owns active execution, recovers durable jobs, and exposes explicit startup, readiness, drain, shutdown, and embedded-mode semantics.
  * Component dispositions: `atlas/service/daemon.py::AtlasDaemon` (create: Own service lifecycle, claim loop, recovery startup, drain, and shutdown.); `atlas/service/config.py::DaemonConfig` (create: Define typed local service, polling, lease, shutdown, and IPC configuration.); `atlas/core/runtime.py` (refactor: Separate composition from process lifetime and provide daemon/embedded construction modes.); `docs/operations/daemon.md` (create: Document ownership, service modes, installation, and failure behavior.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define states `STARTING`, `RECOVERING`, `READY`, `DRAINING`, `STOPPING`, `STOPPED`, and `FAILED` with deterministic readiness semantics.
  * Define one authoritative owner of job advancement per deployment and an explicit embedded-mode ownership contract for tests/library use.
  * Run migration/integrity/recovery checks before readiness and stop claiming work during drain.
  * Define local IPC or database-mediated command access without opening a network listener by default.

  Security and safety requirements

  * Run under a least-privileged local account with restricted database, workspace, configuration, and IPC permissions.
  * Reject insecure socket/pipe paths, world-writable parent directories, and symlinked service state.
  * Attribute startup/shutdown/control actors and avoid logging secrets or raw source data.
  * Embedded mode cannot run concurrently with a daemon against the same writable store unless claims/fencing make it safe.

  Edge cases and outliers to handle

  * Two daemon processes start simultaneously.
  * Host sleeps longer than lease duration.
  * Migration or recovery fails during startup.
  * Shutdown receives repeated or conflicting signals.

  Acceptance criteria (“done” definition)

  * Readiness is false until store, migration, recovery, and ownership checks succeed.
  * Only one valid local owner can advance an attempt.
  * Drain stops new claims while allowing documented safe completion/cancellation behavior.
  * Embedded and daemon modes use identical lifecycle/state/policy services.

  Testing plan

  * Daemon state-machine unit tests.
  * Competing-start integration tests.
  * Startup migration/recovery failure tests.
  * Permission/symlink negative tests.
  * Drain/shutdown signal tests.
  * Embedded/daemon semantic conformance tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Daemon state-machine unit tests., Competing-start integration tests., Startup migration/recovery failure tests., Permission/symlink negative tests., Drain/shutdown signal tests., Embedded/daemon semantic conformance tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T19.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/service/daemon.py::AtlasDaemon, atlas/service/config.py::DaemonConfig, atlas/core/runtime.py, docs/operations/daemon.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 74: Implement durable claims, leases, heartbeats, and fenced execution

  1.2 source task(s): `T19.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T19.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/claims.py::JobClaim (create); atlas/service/claims.py::ClaimService (create); atlas/core/coordinator.py (extend); atlas/schema/migrations/*_claims.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Allow the daemon to discover runnable work and acquire time-bounded authority that stale processes cannot use to commit results.
  * Restore or protect this invariant: Two daemons cannot validly own or commit the same attempt.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/models/claims.py::JobClaim` (create: Represent owner, lease, heartbeat, fencing token, state version, and release reason.); `atlas/service/claims.py::ClaimService` (create: Acquire, renew, release, expire, and query claims transactionally.); `atlas/core/coordinator.py` (extend: Require valid claim/fencing token for attempt advancement and result commit.); `atlas/schema/migrations/*_claims.sql` (create: Persist claims, heartbeat history, and fencing generations.)
  * Epic boundary: Long-running local runtime ownership — Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.
  * Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-017 requires: A CLI process cannot durably own jobs or honor controls from another process; hydrating private `_jobs` is not control.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Allow the daemon to discover runnable work and acquire time-bounded authority that stale processes cannot use to commit results.
  * Component dispositions: `atlas/models/claims.py::JobClaim` (create: Represent owner, lease, heartbeat, fencing token, state version, and release reason.); `atlas/service/claims.py::ClaimService` (create: Acquire, renew, release, expire, and query claims transactionally.); `atlas/core/coordinator.py` (extend: Require valid claim/fencing token for attempt advancement and result commit.); `atlas/schema/migrations/*_claims.sql` (create: Persist claims, heartbeat history, and fencing generations.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Select runnable jobs with deterministic ordering and transactionally acquire one claim with monotonic fencing generation.
  * Renew before expiry, stop authority on failed renewal, and persist release/expiry reasons.
  * Require claim and attempt fencing tokens at every authoritative transition and side-effect result commit.
  * Recover expired claims only after operation-specific reconciliation; never steal an active unknown effect.

  Security and safety requirements

  * Treat claim identity as authority metadata, not a bearer secret exposed to plugins or clients.
  * Reject stale, forged, cross-job, or lower-generation tokens.
  * Bound polling/renewal to avoid database denial of service and thundering herds.
  * Audit claim acquisition, renewal failure, expiry, stale result rejection, and recovery action.

  Edge cases and outliers to handle

  * Database lock prevents heartbeat but work still runs.
  * Lease expires during slow external call.
  * Host clock changes.
  * Stale daemon reports a late success after a successor attempt begins.

  Acceptance criteria (“done” definition)

  * Two daemons cannot validly own or commit the same attempt.
  * A lost lease immediately removes authority at the next guarded boundary.
  * Stale results are rejected and retained as diagnostic evidence.
  * Claim recovery follows operation semantics and never blindly re-executes an unknown effect.

  Testing plan

  * Claim transaction/concurrency tests.
  * Lease expiry/renewal tests.
  * Stale/forged token negative tests.
  * Clock/long-call tests.
  * Late-result fencing tests.
  * Recovery-after-expiry tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Claim transaction/concurrency tests., Lease expiry/renewal tests., Stale/forged token negative tests., Clock/long-call tests., Late-result fencing tests., Recovery-after-expiry tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T19.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/claims.py::JobClaim, atlas/service/claims.py::ClaimService, atlas/core/coordinator.py, atlas/schema/migrations/*_claims.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 75: Route CLI and Python controls through canonical command and status services

  1.2 source task(s): `T19.1.3`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T19.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/service/commands.py::CommandService (create); atlas/status/service.py::StatusService (create); atlas/cli.py (refactor); atlas/__init__.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Remove CLI hydration and private runtime mutation by making foreground, daemon, Python, and future API clients use the same typed command and status contracts.
  * Restore or protect this invariant: A separate CLI process can control a daemon-owned job without private runtime mutation.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/service/commands.py::CommandService` (create: Validate and persist submit/pause/resume/cancel/retry/reconcile/review commands.); `atlas/status/service.py::StatusService` (create: Read authoritative projections without mutating runtime state.); `atlas/cli.py` (refactor: Become a client of command/status services while retaining documented verbs and output modes.); `atlas/__init__.py` (extend: Expose supported Python service interfaces and compatibility shims.)
  * Epic boundary: Long-running local runtime ownership — Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.
  * Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-017 requires: A CLI process cannot durably own jobs or honor controls from another process; hydrating private `_jobs` is not control.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Remove CLI hydration and private runtime mutation by making foreground, daemon, Python, and future API clients use the same typed command and status contracts.
  * Component dispositions: `atlas/service/commands.py::CommandService` (create: Validate and persist submit/pause/resume/cancel/retry/reconcile/review commands.); `atlas/status/service.py::StatusService` (create: Read authoritative projections without mutating runtime state.); `atlas/cli.py` (refactor: Become a client of command/status services while retaining documented verbs and output modes.); `atlas/__init__.py` (extend: Expose supported Python service interfaces and compatibility shims.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define versioned commands with actor, idempotency key, expected state/version, reason, and request/correlation IDs.
  * Persist command acceptance/rejection and let the daemon/coordinator apply controls at valid state/safe-point boundaries.
  * Preserve existing CLI verbs through a compatibility window; add explicit foreground/daemon connection behavior.
  * Remove access to private `_jobs` or orchestrator handler maps from CLI and public Python surfaces.

  Security and safety requirements

  * Validate all fields and reject replay, stale state version, unauthorized deployment action, and lifecycle bypass.
  * Separate event notifications from commands; no event envelope can be deserialized as an accepted command.
  * Use local IPC/database permissions and actor attribution; no implicit trust from process name or transport.
  * Keep raw paths/content out of status by default and apply stable redaction rules.

  Edge cases and outliers to handle

  * Command submitted while daemon drains or is offline.
  * Same idempotency key with different payload.
  * Legacy CLI expects immediate foreground completion.
  * Status read sees partially migrated or corrupted record.

  Acceptance criteria (“done” definition)

  * A separate CLI process can control a daemon-owned job without private runtime mutation.
  * Equivalent CLI/Python commands produce identical persisted command and lifecycle results.
  * Replayed or stale commands return deterministic prior result/conflict.
  * Compatibility behavior and deprecation window are documented and tested.

  Testing plan

  * Command schema/unit tests.
  * CLI/Python equivalence tests.
  * Cross-process pause/resume/cancel tests.
  * Replay/stale-version negative tests.
  * Daemon-offline/draining tests.
  * Legacy CLI compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Command schema/unit tests., CLI/Python equivalence tests., Cross-process pause/resume/cancel tests., Replay/stale-version negative tests., Daemon-offline/draining tests., Legacy CLI compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T19.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/service/commands.py::CommandService, atlas/status/service.py::StatusService, atlas/cli.py, atlas/__init__.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 76: Verify graceful shutdown, forced restart, and orphan containment

  1.2 source task(s): `T19.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T19.1.2, T19.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/service/shutdown.py (create); atlas/service/daemon.py (extend); tests/integration/test_daemon_recovery.py (create); docs/operations/daemon-runbook.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Demonstrate deterministic behavior when the daemon drains, is killed, loses database access, or leaves child processes and claims behind.
  * Restore or protect this invariant: Graceful stop leaves no new claims and records deterministic terminal/suspended/checkpoint state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/service/shutdown.py` (create: Coordinate drain deadlines, safe-point requests, claim release, and forced termination.); `atlas/service/daemon.py` (extend: Integrate signal handling, orphan detection, and restart summary.); `tests/integration/test_daemon_recovery.py` (create: Exercise multi-process control, kill, restart, and ownership scenarios.); `docs/operations/daemon-runbook.md` (create: Provide install/start/stop/recover/diagnose/rollback procedures.)
  * Epic boundary: Long-running local runtime ownership — Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.
  * Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-017 requires: A CLI process cannot durably own jobs or honor controls from another process; hydrating private `_jobs` is not control.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Demonstrate deterministic behavior when the daemon drains, is killed, loses database access, or leaves child processes and claims behind.
  * Component dispositions: `atlas/service/shutdown.py` (create: Coordinate drain deadlines, safe-point requests, claim release, and forced termination.); `atlas/service/daemon.py` (extend: Integrate signal handling, orphan detection, and restart summary.); `tests/integration/test_daemon_recovery.py` (create: Exercise multi-process control, kill, restart, and ownership scenarios.); `docs/operations/daemon-runbook.md` (create: Provide install/start/stop/recover/diagnose/rollback procedures.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define graceful shutdown phases, deadlines, safe-point behavior, subprocess termination, checkpoint flush, and claim release.
  * On forced restart, run fencing and recovery before accepting new commands/work.
  * Detect or reconcile orphan subprocesses/workspaces using attempt ownership and platform-supported process identity.
  * Produce a startup/shutdown recovery report with blocked items and operator actions.

  Security and safety requirements

  * Never kill unrelated processes based on reusable PID alone; bind process identity to attempt/start metadata or platform handle.
  * Preserve bounded diagnostics and sensitive-data redaction during crash handling.
  * Do not release authority before side-effect state is safely stopped or classified.
  * Run service with least privilege and safe file/socket permissions in runbook examples.

  Edge cases and outliers to handle

  * SIGTERM then SIGKILL during checkpoint.
  * Host restart loses process handles but not child process.
  * Database unavailable during claim release.
  * Daemon version changes between crash and restart.

  Acceptance criteria (“done” definition)

  * Graceful stop leaves no new claims and records deterministic terminal/suspended/checkpoint state.
  * Forced restart fences the old owner and produces one recovery decision per nonterminal attempt.
  * Orphan handling cannot terminate an unrelated process.
  * Runbook and tests cover foreground rollback for new jobs without stealing existing daemon-owned work.

  Testing plan

  * Signal/drain unit tests.
  * Kill/restart integration tests.
  * Orphan identity negative tests.
  * Database outage during shutdown tests.
  * Version-change recovery tests.
  * Runbook command smoke tests where repository-supported.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Signal/drain unit tests., Kill/restart integration tests., Orphan identity negative tests., Database outage during shutdown tests., Version-change recovery tests., Runbook command smoke tests where repository-supported..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T19.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/service/shutdown.py, atlas/service/daemon.py, tests/integration/test_daemon_recovery.py, docs/operations/daemon-runbook.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 77: Define structured logging, correlation, error catalog, and redaction

  1.2 source task(s): `T20.1.1`
  Priority: `P1`
  Estimated effort: `12 hours`
  Dependencies: `T8.1.4, T9.1.4, T18.1.4, T19.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/telemetry/logging.py (create); atlas/telemetry/errors.py::ErrorCatalog (create); atlas/telemetry/redaction.py (create); atlas/core/runtime.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace ad hoc diagnostic text with versioned structured records that correlate lifecycle work without leaking secrets, raw payloads, or unbounded path/cardinality data.
  * Restore or protect this invariant: Every major lifecycle, control, recovery, policy, and publication action has a stable code and correlation chain.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/telemetry/logging.py` (create: Configure structured records, context propagation, sinks, and failure isolation.); `atlas/telemetry/errors.py::ErrorCatalog` (create: Map stable error codes to safe messages, severity, and operator guidance.); `atlas/telemetry/redaction.py` (create: Centralize secret, content, path, and metadata redaction/bounding.); `atlas/core/runtime.py` (extend: Inject telemetry context without hidden global mutable state.)
  * Epic boundary: Canonical status, telemetry, health, and diagnostics — Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.
  * Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-018 requires: Operators need authoritative progress, blockers, provenance, and recovery evidence without reading raw SQLite or logs.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace ad hoc diagnostic text with versioned structured records that correlate lifecycle work without leaking secrets, raw payloads, or unbounded path/cardinality data.
  * Component dispositions: `atlas/telemetry/logging.py` (create: Configure structured records, context propagation, sinks, and failure isolation.); `atlas/telemetry/errors.py::ErrorCatalog` (create: Map stable error codes to safe messages, severity, and operator guidance.); `atlas/telemetry/redaction.py` (create: Centralize secret, content, path, and metadata redaction/bounding.); `atlas/core/runtime.py` (extend: Inject telemetry context without hidden global mutable state.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define a versioned log envelope with time, severity, code, message template, correlation/job/phase/attempt/work/control/event/request IDs, component, and bounded attributes.
  * Propagate context explicitly across async tasks, subprocess boundaries, outbox dispatch, and command requests.
  * Classify fields as safe, hashed/minimized, secret, content-derived, or prohibited; redact before serialization.
  * Define sink failure/backpressure behavior and ensure logging cannot fail authoritative transitions.

  Security and safety requirements

  * Prevent terminal/log injection, multiline spoofing, secret/token leakage, and raw malicious filename/content rendering.
  * Use allowlisted attributes and bounded lengths/counts; hash/minimize paths where full values are not required.
  * Keep stack traces and sensitive diagnostics behind explicit local diagnostic policy.
  * Test that attacker-controlled metadata cannot change severity, code, actor, or correlation fields.

  Edge cases and outliers to handle

  * Telemetry context missing after task restart.
  * Recursive logging failure or sink disk exhaustion.
  * Huge numbers of unique paths/work IDs.
  * Exception text includes secrets or binary data.

  Acceptance criteria (“done” definition)

  * Every major lifecycle, control, recovery, policy, and publication action has a stable code and correlation chain.
  * Redaction occurs before every configured sink and diagnostic export.
  * Telemetry sink failure cannot change job state or result.
  * Golden log schema is versioned and compatibility-tested.

  Testing plan

  * Envelope/schema golden tests.
  * Async/subprocess context propagation tests.
  * Injection/redaction/secret fixture tests.
  * Sink failure/backpressure tests.
  * High-cardinality bounding tests.
  * Error catalog completeness tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Envelope/schema golden tests., Async/subprocess context propagation tests., Injection/redaction/secret fixture tests., Sink failure/backpressure tests., High-cardinality bounding tests., Error catalog completeness tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T20.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/telemetry/logging.py, atlas/telemetry/errors.py::ErrorCatalog, atlas/telemetry/redaction.py, atlas/core/runtime.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 78: Implement bounded metrics and optional distributed tracing

  1.2 source task(s): `T20.1.2`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T20.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/telemetry/metrics.py::MetricsAdapter (create); atlas/telemetry/tracing.py::TraceAdapter (create); docs/operations/metrics-catalog.md (create); tests/telemetry/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Expose measurable throughput, latency, resource, queue, retry, recovery, and safety behavior without making telemetry required for correctness or creating unbounded cardinality.
  * Restore or protect this invariant: Metric names, units, label sets, and bounds are documented and schema-tested.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/telemetry/metrics.py::MetricsAdapter` (create: Define counters, gauges, histograms, labels, and no-op/default adapter.); `atlas/telemetry/tracing.py::TraceAdapter` (create: Provide optional spans and context propagation around canonical operations.); `docs/operations/metrics-catalog.md` (create: Define names, units, labels, bounds, interpretation, and alert suggestions.); `tests/telemetry/` (create: Validate adapters, outage behavior, and cardinality policy.)
  * Epic boundary: Canonical status, telemetry, health, and diagnostics — Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.
  * Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-018 requires: Operators need authoritative progress, blockers, provenance, and recovery evidence without reading raw SQLite or logs.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Expose measurable throughput, latency, resource, queue, retry, recovery, and safety behavior without making telemetry required for correctness or creating unbounded cardinality.
  * Component dispositions: `atlas/telemetry/metrics.py::MetricsAdapter` (create: Define counters, gauges, histograms, labels, and no-op/default adapter.); `atlas/telemetry/tracing.py::TraceAdapter` (create: Provide optional spans and context propagation around canonical operations.); `docs/operations/metrics-catalog.md` (create: Define names, units, labels, bounds, interpretation, and alert suggestions.); `tests/telemetry/` (create: Validate adapters, outage behavior, and cardinality policy.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define a stable metric catalog for lifecycle states, phase/operation duration, throughput, bytes/entries, budgets, retries, checkpoints, claims, outbox, publications, and failures.
  * Allow only bounded labels such as phase, operation class, backend, result, and stable error code; never raw artifact IDs or paths by default.
  * Create optional traces linking command, coordinator, work item, backend, event, and publication spans through correlation IDs.
  * Document sampling, aggregation, clock, and retention limitations and keep durable evidence independent.

  Security and safety requirements

  * Metrics/traces may not contain raw content, secrets, credentials, or uncontrolled high-cardinality identifiers.
  * Exporter endpoints and credentials are optional deployment controls and least-privileged.
  * Telemetry failure is isolated and visible through bounded local counters/status.
  * Do not use model-generated labels or unvalidated plugin attributes.

  Edge cases and outliers to handle

  * Exporter unavailable or slow.
  * Clock skew produces negative/invalid duration.
  * Millions of work items threaten cardinality.
  * Trace context is malformed or untrusted.

  Acceptance criteria (“done” definition)

  * Metric names, units, label sets, and bounds are documented and schema-tested.
  * No mandatory lifecycle path depends on exporter success.
  * Load tests demonstrate bounded cardinality and memory use for representative workloads.
  * Trace removal/no-op mode leaves persisted semantics identical.

  Testing plan

  * Metric catalog/schema tests.
  * No-op/exporter conformance tests.
  * Exporter outage/slow sink tests.
  * Cardinality/load tests.
  * Trace context validation tests.
  * Semantic equivalence tests with telemetry disabled.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Metric catalog/schema tests., No-op/exporter conformance tests., Exporter outage/slow sink tests., Cardinality/load tests., Trace context validation tests., Semantic equivalence tests with telemetry disabled..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T20.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/telemetry/metrics.py::MetricsAdapter, atlas/telemetry/tracing.py::TraceAdapter, docs/operations/metrics-catalog.md, tests/telemetry/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 79: Build the canonical versioned job status projection

  1.2 source task(s): `T20.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T20.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/status/models.py::JobStatusV1 (create); atlas/status/projection.py::StatusProjection (create); atlas/status/service.py (extend); atlas/cli.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide one read model derived from authoritative state for current phase/attempt, progress, controls, checkpoints, blockers, retries, budgets, events, lineage, and recovery.
  * Restore or protect this invariant: An operator can identify exact current phase, attempt, checkpoint, control, blocker, retry/recovery action, and provenance completeness without raw DB access.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/status/models.py::JobStatusV1` (create: Define the stable status schema and completeness/degradation markers.); `atlas/status/projection.py::StatusProjection` (create: Read and combine authoritative state using a consistent snapshot.); `atlas/status/service.py` (extend: Expose job/list/watch/export queries with pagination and versioning.); `atlas/cli.py` (extend: Render human and JSON status without inventing missing state.)
  * Epic boundary: Canonical status, telemetry, health, and diagnostics — Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.
  * Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-018 requires: Operators need authoritative progress, blockers, provenance, and recovery evidence without reading raw SQLite or logs.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Provide one read model derived from authoritative state for current phase/attempt, progress, controls, checkpoints, blockers, retries, budgets, events, lineage, and recovery.
  * Component dispositions: `atlas/status/models.py::JobStatusV1` (create: Define the stable status schema and completeness/degradation markers.); `atlas/status/projection.py::StatusProjection` (create: Read and combine authoritative state using a consistent snapshot.); `atlas/status/service.py` (extend: Expose job/list/watch/export queries with pagination and versioning.); `atlas/cli.py` (extend: Render human and JSON status without inventing missing state.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define status fields and authority source for job/phase/attempt/work, progress numerator/denominator, pending control, checkpoint age, claim/lease, retry, blocker, budget, outbox backlog, provenance completeness, and publication state.
  * Read from a consistent StateStore transaction/snapshot and mark unavailable/corrupt/legacy fields explicitly.
  * Define stable pagination, filtering, ordering, and optional incremental sequence cursor.
  * Keep projection rebuildable; never write lifecycle state from status code.

  Security and safety requirements

  * Apply path/content minimization and authorization filters in deployment adapters before returning sensitive details.
  * Do not derive success from event transport, logs, worker claims, or model output.
  * Reject query injection and bound list/page/time-range parameters.
  * Expose stale/partial/degraded status explicitly rather than filling defaults that imply safety.

  Edge cases and outliers to handle

  * Legacy job lacks attempts/checkpoints/lineage.
  * Rows change during projection.
  * Corrupt or incompatible record.
  * Status query over millions of artifacts/work items.

  Acceptance criteria (“done” definition)

  * An operator can identify exact current phase, attempt, checkpoint, control, blocker, retry/recovery action, and provenance completeness without raw DB access.
  * Status is rebuildable from authoritative state and events are supplemental only.
  * Legacy/partial/corrupt fields are explicit and never mistaken for complete.
  * Query performance and pagination are measured on representative large jobs.

  Testing plan

  * Projection golden tests.
  * Consistent-snapshot concurrency tests.
  * Legacy/degraded/corrupt record tests.
  * Authorization/redaction adapter tests.
  * Large-job query benchmarks.
  * CLI/JSON/API schema compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Projection golden tests., Consistent-snapshot concurrency tests., Legacy/degraded/corrupt record tests., Authorization/redaction adapter tests., Large-job query benchmarks., CLI/JSON/API schema compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T20.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/status/models.py::JobStatusV1, atlas/status/projection.py::StatusProjection, atlas/status/service.py, atlas/cli.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 80: Implement health, readiness, and sanitized diagnostic bundles

  1.2 source task(s): `T20.1.4`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T20.1.2, T20.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/status/health.py (create); atlas/diagnostics/bundle.py::DiagnosticBundleBuilder (create); atlas/cli.py (extend); docs/operations/diagnostics.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Define deterministic service health/readiness and produce integrity-manifested diagnostic bundles that operators can share without raw content or secrets.
  * Restore or protect this invariant: Health/readiness results are deterministic and identify each failed dependency/control.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/status/health.py` (create: Evaluate process, store, migration, recovery, claim, workspace, outbox, and optional dependency health.); `atlas/diagnostics/bundle.py::DiagnosticBundleBuilder` (create: Collect bounded status/config/schema/runtime/evidence summaries and manifest hashes.); `atlas/cli.py` (extend: Expose health, readiness, and diagnostic bundle commands.); `docs/operations/diagnostics.md` (create: Document collection, redaction, interpretation, and secure handling.)
  * Epic boundary: Canonical status, telemetry, health, and diagnostics — Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.
  * Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-018 requires: Operators need authoritative progress, blockers, provenance, and recovery evidence without reading raw SQLite or logs.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Define deterministic service health/readiness and produce integrity-manifested diagnostic bundles that operators can share without raw content or secrets.
  * Component dispositions: `atlas/status/health.py` (create: Evaluate process, store, migration, recovery, claim, workspace, outbox, and optional dependency health.); `atlas/diagnostics/bundle.py::DiagnosticBundleBuilder` (create: Collect bounded status/config/schema/runtime/evidence summaries and manifest hashes.); `atlas/cli.py` (extend: Expose health, readiness, and diagnostic bundle commands.); `docs/operations/diagnostics.md` (create: Document collection, redaction, interpretation, and secure handling.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Separate liveness from readiness and dependency degradation; define exact reason codes and recovery guidance.
  * Include schema/config/runtime/plugin versions, sanitized status, recent stable error codes, migration/integrity state, resource summary, and selected evidence references.
  * Create a bundle manifest with file sizes, schema versions, SHA-256 hashes, omissions, and redaction policy version.
  * Bound time, size, rows, and path samples; permit partial bundle with explicit missing-component records.

  Security and safety requirements

  * Redact and scan before archive creation; exclude raw artifact bytes, secrets, credentials, unrestricted environment, and arbitrary logs by default.
  * Write to a safe caller-selected/controlled directory using no-replace semantics and secure permissions.
  * Do not execute plugins or external commands during bundle collection unless an explicit trusted diagnostic adapter exists.
  * Treat diagnostic export as potentially sensitive and document optional deployment authorization/encryption.

  Edge cases and outliers to handle

  * Store unavailable or corrupt.
  * Bundle target is symlink/path traversal or disk becomes full.
  * A collector times out or emits malformed data.
  * Secret-like fixture appears in metadata/error text.

  Acceptance criteria (“done” definition)

  * Health/readiness results are deterministic and identify each failed dependency/control.
  * Diagnostic bundle verifies against its manifest and records all omissions/degraded collectors.
  * Synthetic secret/raw-content tests find no prohibited data.
  * Bundle failure cannot mutate lifecycle state or overwrite an existing file.

  Testing plan

  * Health truth-table tests.
  * Dependency outage tests.
  * Diagnostic reproducibility/hash tests.
  * Secret/redaction scan tests.
  * Path/symlink/no-replace tests.
  * Partial/disk-full/collector-timeout tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Health truth-table tests., Dependency outage tests., Diagnostic reproducibility/hash tests., Secret/redaction scan tests., Path/symlink/no-replace tests., Partial/disk-full/collector-timeout tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T20.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/status/health.py, atlas/diagnostics/bundle.py::DiagnosticBundleBuilder, atlas/cli.py, docs/operations/diagnostics.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 81: Define versioned external command, status, and error schemas

  1.2 source task(s): `T21.1.1`
  Priority: `P2`
  Estimated effort: `14 hours`
  Dependencies: `T8.1.4, T19.1.4, T20.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/api/contracts.py (create); atlas/service/commands.py (extend); atlas/status/models.py (extend); docs/api/contracts-v1.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create transport-neutral request/response contracts that preserve command idempotency, expected state, actor attribution, lifecycle guards, and status authority across CLI, Python, REST, and future clients.
  * Restore or protect this invariant: Equivalent local and external contracts produce identical authoritative command outcomes.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/api/contracts.py` (create: Define v1 command, status, pagination, problem/error, and compatibility envelopes.); `atlas/service/commands.py` (extend: Map transport-neutral contracts to canonical command validation and results.); `atlas/status/models.py` (extend: Expose stable external projection schemas without transport coupling.); `docs/api/contracts-v1.md` (create: Document fields, semantics, idempotency, versioning, and lifecycle restrictions.)
  * Epic boundary: Versioned external command and event adapters — Expose REST, RabbitMQ, and webhook surfaces only as adapters over canonical command, status, and durable event contracts.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.
  * Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-019 requires: External interfaces are useful only after durable semantics exist and must not create alternate lifecycle authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create transport-neutral request/response contracts that preserve command idempotency, expected state, actor attribution, lifecycle guards, and status authority across CLI, Python, REST, and future clients.
  * Component dispositions: `atlas/api/contracts.py` (create: Define v1 command, status, pagination, problem/error, and compatibility envelopes.); `atlas/service/commands.py` (extend: Map transport-neutral contracts to canonical command validation and results.); `atlas/status/models.py` (extend: Expose stable external projection schemas without transport coupling.); `docs/api/contracts-v1.md` (create: Document fields, semantics, idempotency, versioning, and lifecycle restrictions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define submit, pause, resume, cancel, retry, reconcile, review, and publication command bodies with request ID, idempotency key, actor, expected state/version, reason, and typed payload.
  * Define stable success, accepted/pending, conflict, validation, policy, unavailable, and internal error responses.
  * Define schema/version negotiation and additive/deprecation rules; reject unknown major versions and ambiguous duplicate fields.
  * Map every contract to the same `CommandService`/`StatusService` used by local clients.

  Security and safety requirements

  * Validate size, encoding, duplicate keys, unknown fields policy, enum values, IDs, paths/URLs, and content types before command handling.
  * Do not infer authorization from transport or event origin; pass authenticated identity/claims through an optional deployment adapter.
  * Prevent mass assignment of internal state, actor, policy, fencing, claim, or completion fields.
  * Separate errors safe for remote clients from diagnostic details and secret-bearing causes.

  Edge cases and outliers to handle

  * Same idempotency key with a different body.
  * Client uses stale expected version.
  * Unknown/old schema version.
  * Malformed JSON, duplicate keys, huge nested payload, or unsupported content type.

  Acceptance criteria (“done” definition)

  * Equivalent local and external contracts produce identical authoritative command outcomes.
  * No request field can directly set job/phase/attempt state, fencing, policy result, or publication success.
  * Replay/stale/version conflicts are deterministic and machine-readable.
  * Schemas and examples are generated or CI-checked against implementation.

  Testing plan

  * Contract serialization/golden tests.
  * Duplicate-key/malformed/size fuzz tests.
  * CLI/Python/external equivalence tests.
  * Replay/stale-version tests.
  * Mass-assignment and lifecycle-bypass negative tests.
  * Schema compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Contract serialization/golden tests., Duplicate-key/malformed/size fuzz tests., CLI/Python/external equivalence tests., Replay/stale-version tests., Mass-assignment and lifecycle-bypass negative tests., Schema compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T21.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/api/contracts.py, atlas/service/commands.py, atlas/status/models.py, docs/api/contracts-v1.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 82: Implement REST v1 and generate the OpenAPI contract

  1.2 source task(s): `T21.1.2`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T21.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/api/rest.py (create); atlas/api/dependencies.py (create); openapi/atlas-v1.yaml (create); tests/api/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide an optional HTTP adapter for commands, status, evidence, lineage, and health without embedding lifecycle authority or mandatory multi-user IAM in the core.
  * Restore or protect this invariant: REST and CLI/Python commands converge on the same persisted result for equivalent requests.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/api/rest.py` (create: Host REST v1 routes and adapter lifecycle.); `atlas/api/dependencies.py` (create: Inject command/status/evidence services and optional auth/rate-limit adapters.); `openapi/atlas-v1.yaml` (create: Generate and retain the versioned public contract.); `tests/api/` (create: Validate schema, equivalence, security, and failure behavior.)
  * Epic boundary: Versioned external command and event adapters — Expose REST, RabbitMQ, and webhook surfaces only as adapters over canonical command, status, and durable event contracts.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.
  * Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-019 requires: External interfaces are useful only after durable semantics exist and must not create alternate lifecycle authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Provide an optional HTTP adapter for commands, status, evidence, lineage, and health without embedding lifecycle authority or mandatory multi-user IAM in the core.
  * Component dispositions: `atlas/api/rest.py` (create: Host REST v1 routes and adapter lifecycle.); `atlas/api/dependencies.py` (create: Inject command/status/evidence services and optional auth/rate-limit adapters.); `openapi/atlas-v1.yaml` (create: Generate and retain the versioned public contract.); `tests/api/` (create: Validate schema, equivalence, security, and failure behavior.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Expose bounded endpoints for command submission/results, job list/status, events/evidence/lineage reads, health/readiness, and API schema.
  * Use canonical error objects, request/correlation IDs, idempotency, conditional expected-version/ETag semantics, pagination, and content negotiation.
  * Keep server startup/configuration optional and disabled by default for local library/CLI use.
  * Generate OpenAPI from contracts or verify it bidirectionally in CI, including examples and error cases.

  Security and safety requirements

  * Require configurable bind address/TLS/authn/authz/rate-limit/request-size deployment controls before non-loopback exposure.
  * Prevent path/query/JSON/log injection, CSRF where cookie auth is used, CORS overexposure, SSRF in destination/source inputs, and XSS in rendered examples.
  * Do not return raw artifact bytes, secrets, plugin environment, or unrestricted filesystem paths by default.
  * Audit accepted/denied consequential commands with actor, subject, policy, request, and result IDs.

  Edge cases and outliers to handle

  * Client disconnects after command commit.
  * Proxy retries POST.
  * API restarts while response is pending.
  * Slow-list/query or huge evidence lineage request.

  Acceptance criteria (“done” definition)

  * REST and CLI/Python commands converge on the same persisted result for equivalent requests.
  * OpenAPI is versioned, complete for implemented endpoints, and fails CI on drift.
  * Client disconnect/retry cannot duplicate authoritative effects.
  * Disabling/removing REST leaves core job execution and status semantics unchanged.

  Testing plan

  * OpenAPI/schema conformance tests.
  * End-to-end REST/CLI equivalence tests.
  * Proxy retry/client disconnect tests.
  * Auth/rate-limit/TLS adapter tests where configured.
  * Injection/CSRF/CORS/size negative tests.
  * Pagination/load and API restart tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: OpenAPI/schema conformance tests., End-to-end REST/CLI equivalence tests., Proxy retry/client disconnect tests., Auth/rate-limit/TLS adapter tests where configured., Injection/CSRF/CORS/size negative tests., Pagination/load and API restart tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T21.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/api/rest.py, atlas/api/dependencies.py, openapi/atlas-v1.yaml, tests/api/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 83: Implement outbox-backed RabbitMQ event delivery

  1.2 source task(s): `T21.1.3`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T21.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/rabbitmq.py (refactor); atlas/events/dispatcher.py (extend); atlas/events/contracts.py (extend); tests/events/test_rabbitmq_transport.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Complete RabbitMQ as a durable notification transport driven from the outbox with confirms, bounded retry, dead-letter evidence, offsets, and no consumer authority over lifecycle state.
  * Restore or protect this invariant: Broker outage cannot roll back or falsely fail an already committed lifecycle transition.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/events/rabbitmq.py` (refactor: Publish versioned event envelopes from committed outbox rows with confirms.); `atlas/events/dispatcher.py` (extend: Add transport-specific retry, backoff, delivery status, and capacity policy.); `atlas/events/contracts.py` (extend: Define routing/version headers and consumer compatibility guidance.); `tests/events/test_rabbitmq_transport.py` (create: Exercise outage, redelivery, confirm, DLQ, and event-injection cases.)
  * Epic boundary: Versioned external command and event adapters — Expose REST, RabbitMQ, and webhook surfaces only as adapters over canonical command, status, and durable event contracts.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.
  * Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-019 requires: External interfaces are useful only after durable semantics exist and must not create alternate lifecycle authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Complete RabbitMQ as a durable notification transport driven from the outbox with confirms, bounded retry, dead-letter evidence, offsets, and no consumer authority over lifecycle state.
  * Component dispositions: `atlas/events/rabbitmq.py` (refactor: Publish versioned event envelopes from committed outbox rows with confirms.); `atlas/events/dispatcher.py` (extend: Add transport-specific retry, backoff, delivery status, and capacity policy.); `atlas/events/contracts.py` (extend: Define routing/version headers and consumer compatibility guidance.); `tests/events/test_rabbitmq_transport.py` (create: Exercise outage, redelivery, confirm, DLQ, and event-injection cases.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Read committed outbox rows in sequence, publish canonical event envelope and headers, wait for publisher confirm, then persist delivery state.
  * Define bounded retry/dead-letter terminal status, broker topology declarations, message TTL/size, and consumer offset/replay guidance.
  * Preserve legacy routing keys through a versioned compatibility adapter and publish deprecation telemetry.
  * Keep lifecycle state and event history authoritative in StateStore even when broker is unavailable.

  Security and safety requirements

  * Use TLS/credentials/vhost permissions as optional deployment controls and keep secrets out of events/logs.
  * Reject untrusted consumer messages as lifecycle commands; commands require a separately authenticated command endpoint.
  * Bound payload size, headers, retry rate, connection attempts, and backlog policy.
  * Validate event schema/version and prevent routing-key/header injection from artifact/plugin data.

  Edge cases and outliers to handle

  * Broker outage during transition.
  * Confirm lost after broker accepted message.
  * Duplicate/redelivered event.
  * Slow/poison consumer or schema-incompatible consumer.

  Acceptance criteria (“done” definition)

  * Broker outage cannot roll back or falsely fail an already committed lifecycle transition.
  * Delivery retries are bounded and duplicate event IDs/sequences support idempotent consumers.
  * No replayed event can mutate lifecycle state.
  * Legacy routing and new envelopes have a tested compatibility/deprecation path.

  Testing plan

  * Transport conformance tests with test broker.
  * Outage/confirm-loss/redelivery tests.
  * Backlog/capacity/backpressure tests.
  * Schema/routing injection negative tests.
  * Legacy routing compatibility tests.
  * Consumer replay/idempotency reference tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Transport conformance tests with test broker., Outage/confirm-loss/redelivery tests., Backlog/capacity/backpressure tests., Schema/routing injection negative tests., Legacy routing compatibility tests., Consumer replay/idempotency reference tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T21.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/rabbitmq.py, atlas/events/dispatcher.py, atlas/events/contracts.py, tests/events/test_rabbitmq_transport.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 84: Implement signed idempotent webhook notifications

  1.2 source task(s): `T21.1.4`
  Priority: `P2`
  Estimated effort: `14 hours`
  Dependencies: `T21.1.2, T21.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/webhooks.py::WebhookDispatcher (create); atlas/models/webhooks.py (create); atlas/schema/migrations/*_webhooks.sql (create); docs/integrations/webhooks.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide optional destination-neutral webhooks with durable delivery attempts, signatures, replay resistance, bounded retries, and no authority to acknowledge lifecycle truth.
  * Restore or protect this invariant: Receivers can verify authenticity, schema version, event identity, and replay window.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/events/webhooks.py::WebhookDispatcher` (create: Select subscriptions and perform durable delivery attempts.); `atlas/models/webhooks.py` (create: Define subscription, secret reference, delivery attempt, response summary, and status.); `atlas/schema/migrations/*_webhooks.sql` (create: Persist subscriptions, attempts, retries, and disablement.); `docs/integrations/webhooks.md` (create: Document signature verification, idempotency, retries, and security.)
  * Epic boundary: Versioned external command and event adapters — Expose REST, RabbitMQ, and webhook surfaces only as adapters over canonical command, status, and durable event contracts.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.
  * Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-019 requires: External interfaces are useful only after durable semantics exist and must not create alternate lifecycle authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Provide optional destination-neutral webhooks with durable delivery attempts, signatures, replay resistance, bounded retries, and no authority to acknowledge lifecycle truth.
  * Component dispositions: `atlas/events/webhooks.py::WebhookDispatcher` (create: Select subscriptions and perform durable delivery attempts.); `atlas/models/webhooks.py` (create: Define subscription, secret reference, delivery attempt, response summary, and status.); `atlas/schema/migrations/*_webhooks.sql` (create: Persist subscriptions, attempts, retries, and disablement.); `docs/integrations/webhooks.md` (create: Document signature verification, idempotency, retries, and security.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define explicit event subscriptions, endpoint policy, schema version, signing key reference, timeout, retry/dead-letter, and disable controls.
  * Sign canonical body plus event ID/sequence/time/version and expose a stable delivery ID for receiver idempotency.
  * Persist attempt before request and store bounded response metadata; never store arbitrary response bodies.
  * Treat 2xx as transport acknowledgement only; it cannot alter ATLAS lifecycle state.

  Security and safety requirements

  * Validate endpoint scheme/host against deployment policy and defend against SSRF, DNS rebinding, redirect abuse, private-network access, and credential-in-URL.
  * Use rotating secret references, constant-time verification guidance, timestamp/nonce replay window, and no secrets in logs.
  * Bound concurrency, retries, body, response, redirect, DNS, and timeout resources.
  * Disable subscriptions after policy-defined repeated permanent failure without deleting evidence.

  Edge cases and outliers to handle

  * Receiver times out after accepting.
  * DNS changes between validation and connection.
  * Redirect crosses policy boundary.
  * Secret rotates while deliveries are pending.

  Acceptance criteria (“done” definition)

  * Receivers can verify authenticity, schema version, event identity, and replay window.
  * Duplicate delivery is expected and safely identifiable.
  * Webhook failure never changes lifecycle state or loses durable event history.
  * SSRF/redirect/rebinding tests demonstrate deployment-policy enforcement.

  Testing plan

  * Signature golden/rotation tests.
  * Duplicate/replay receiver tests.
  * SSRF/DNS-rebinding/redirect negative tests.
  * Timeout/partial-response/retry tests.
  * Backpressure/concurrency tests.
  * Disable/reenable and audit tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Signature golden/rotation tests., Duplicate/replay receiver tests., SSRF/DNS-rebinding/redirect negative tests., Timeout/partial-response/retry tests., Backpressure/concurrency tests., Disable/reenable and audit tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T21.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/webhooks.py::WebhookDispatcher, atlas/models/webhooks.py, atlas/schema/migrations/*_webhooks.sql, docs/integrations/webhooks.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 85: Define the subprocess protocol and mediated artifact contract

  1.2 source task(s): `T22.1.1`
  Priority: `P2`
  Estimated effort: `14 hours`
  Dependencies: `T14.1.4, T15.1.4, T16.1.4, T18.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/subprocess.py::SubprocessBackend (create); atlas/execution/protocol.py (create); atlas/execution/artifact_access.py (extend); docs/plugins/subprocess-protocol.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create a minimal versioned protocol in which a plugin receives only declared immutable inputs and capability grants and returns bounded typed results without StateStore or source-root authority.
  * Restore or protect this invariant: Subprocess cannot receive StateStore credentials or undeclared source/workspace paths through the protocol/environment.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/execution/subprocess.py::SubprocessBackend` (create: Implement the backend contract and protocol lifecycle.); `atlas/execution/protocol.py` (create: Define handshake, request, progress, result, error, and cancellation messages.); `atlas/execution/artifact_access.py` (extend: Issue mediated read-only content/derived-artifact handles or copies.); `docs/plugins/subprocess-protocol.md` (create: Document compatibility, limits, capability model, and trust assumptions.)
  * Epic boundary: Subprocess plugin isolation and enforceable resource controls — Run untrusted or high-risk plugins outside the core process with mediated inputs, explicit capabilities, bounded resources, deterministic termination, and visible platform limitations.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.
  * Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-020 requires: Third-party analyzers should not share process authority, unrestricted filesystem, or StateStore credentials.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create a minimal versioned protocol in which a plugin receives only declared immutable inputs and capability grants and returns bounded typed results without StateStore or source-root authority.
  * Component dispositions: `atlas/execution/subprocess.py::SubprocessBackend` (create: Implement the backend contract and protocol lifecycle.); `atlas/execution/protocol.py` (create: Define handshake, request, progress, result, error, and cancellation messages.); `atlas/execution/artifact_access.py` (extend: Issue mediated read-only content/derived-artifact handles or copies.); `docs/plugins/subprocess-protocol.md` (create: Document compatibility, limits, capability model, and trust assumptions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define protocol major/minor version, plugin identity/digest, operation, inputs, grants, budgets, deadline, attempt/fencing context, progress, result, evidence, and errors.
  * Use length-delimited or equivalent framing with strict size/encoding/order rules; reject extra/ambiguous/duplicate fields according to version policy.
  * Provide read-only mediated content handles/copies and an attempt-owned output workspace; never expose StateStore credentials or unrestricted source paths.
  * Validate all output through the same typed analyzer/phase contracts before persistence.

  Security and safety requirements

  * Sanitize environment, current directory, inherited file descriptors/handles, locale, PATH, Python/module path, and secret variables.
  * Capability grants are explicit, attempt-scoped, least-privilege, non-transferable metadata; plugin text cannot self-grant.
  * Treat stdout/stderr/protocol bytes as untrusted and bounded; do not parse shell commands or unsafe serialization.
  * Authenticate/verify the configured executable or package digest according to plugin trust policy.

  Edge cases and outliers to handle

  * Protocol version mismatch or truncated frame.
  * Plugin emits stdout noise before handshake.
  * Input content disappears or handle expires.
  * Plugin fabricates another attempt/content/result identity.

  Acceptance criteria (“done” definition)

  * Subprocess cannot receive StateStore credentials or undeclared source/workspace paths through the protocol/environment.
  * Malformed or forged protocol messages fail the attempt without lifecycle mutation.
  * Equivalent trusted plugin results normalize identically in in-process and subprocess backends.
  * Protocol compatibility and capability negotiation are versioned and tested.

  Testing plan

  * Protocol codec/golden tests.
  * Malformed/truncated/fuzz tests.
  * Environment/fd/secret leakage tests.
  * Forged identity/grant negative tests.
  * In-process/subprocess conformance tests.
  * Large output/input-handle expiry tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Protocol codec/golden tests., Malformed/truncated/fuzz tests., Environment/fd/secret leakage tests., Forged identity/grant negative tests., In-process/subprocess conformance tests., Large output/input-handle expiry tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T22.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/subprocess.py::SubprocessBackend, atlas/execution/protocol.py, atlas/execution/artifact_access.py, docs/plugins/subprocess-protocol.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 86: Implement deterministic process lifecycle, timeout, and tree termination

  1.2 source task(s): `T22.1.2`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T22.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/process_supervisor.py (create); atlas/execution/subprocess.py (extend); atlas/recovery/reconcilers.py (extend); tests/execution/hostile_plugins/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Own launch, handshake, progress, cancellation, deadline, termination, reaping, and cleanup so a plugin crash or timeout becomes one fenced attempt outcome.
  * Restore or protect this invariant: Timeout/cancel kills and reaps the entire controlled process tree on supported platforms.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/execution/process_supervisor.py` (create: Manage process group/job object, lifecycle, deadlines, output limits, and termination escalation.); `atlas/execution/subprocess.py` (extend: Integrate supervisor, checkpoints/progress, and backend result mapping.); `atlas/recovery/reconcilers.py` (extend: Classify orphan/unknown subprocess state on restart.); `tests/execution/hostile_plugins/` (create: Provide synthetic crash, hang, fork, flood, and signal fixtures.)
  * Epic boundary: Subprocess plugin isolation and enforceable resource controls — Run untrusted or high-risk plugins outside the core process with mediated inputs, explicit capabilities, bounded resources, deterministic termination, and visible platform limitations.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.
  * Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-020 requires: Third-party analyzers should not share process authority, unrestricted filesystem, or StateStore credentials.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Own launch, handshake, progress, cancellation, deadline, termination, reaping, and cleanup so a plugin crash or timeout becomes one fenced attempt outcome.
  * Component dispositions: `atlas/execution/process_supervisor.py` (create: Manage process group/job object, lifecycle, deadlines, output limits, and termination escalation.); `atlas/execution/subprocess.py` (extend: Integrate supervisor, checkpoints/progress, and backend result mapping.); `atlas/recovery/reconcilers.py` (extend: Classify orphan/unknown subprocess state on restart.); `tests/execution/hostile_plugins/` (create: Provide synthetic crash, hang, fork, flood, and signal fixtures.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Launch in a dedicated process group/session or platform job object and record robust process identity with attempt.
  * Enforce handshake/start/idle/total deadlines, cancellation, graceful termination grace, forced tree kill, wait/reap, and deterministic outcome mapping.
  * Bound stdout, stderr, protocol, child count, open handles, and retained diagnostics; truncate with explicit evidence.
  * On restart, never kill by PID alone; reconcile platform process identity and fenced attempt ownership.

  Security and safety requirements

  * Prevent process-tree escape where the supported platform primitive can enforce it; report reduced assurance otherwise.
  * Close inherited descriptors/handles and ensure child cannot signal/control unrelated processes.
  * Do not treat a successful exit code as valid until protocol result, identity, schema, and content/output verification pass.
  * Retain bounded crash evidence without core dumps or secret-bearing memory by default.

  Edge cases and outliers to handle

  * Child forks then parent exits.
  * Child ignores termination or floods output.
  * Cancellation races with valid result.
  * PID is reused after daemon restart.

  Acceptance criteria (“done” definition)

  * Timeout/cancel kills and reaps the entire controlled process tree on supported platforms.
  * Late or stale results cannot commit after fencing/cancellation.
  * Unsupported containment controls are explicit in status and release evidence.
  * No zombie, leaked handle, or unbounded output remains after hostile fixtures.

  Testing plan

  * Lifecycle state-machine tests.
  * Hang/fork/output-flood hostile tests.
  * Cancel/result race tests.
  * PID reuse/orphan restart tests.
  * Resource leak/reaping tests.
  * Platform-specific conformance tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Lifecycle state-machine tests., Hang/fork/output-flood hostile tests., Cancel/result race tests., PID reuse/orphan restart tests., Resource leak/reaping tests., Platform-specific conformance tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T22.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/process_supervisor.py, atlas/execution/subprocess.py, atlas/recovery/reconcilers.py, tests/execution/hostile_plugins/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 87: Enforce subprocess resource, network, tool, and secret policy

  1.2 source task(s): `T22.1.3`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T22.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/limits.py (create); atlas/execution/capabilities.py::CapabilityGrant (extend); atlas/security/plugin_policy.py (extend); docs/security/subprocess-enforcement-matrix.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Apply the unified resource budget and plugin capability policy using available OS controls while failing closed or visibly reducing assurance when enforcement is unavailable.
  * Restore or protect this invariant: Each subprocess attempt records requested, enforced, unavailable, and exceeded controls plus measured usage.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/execution/limits.py` (create: Translate hierarchical budgets to platform CPU, memory, process, file, and time controls.); `atlas/execution/capabilities.py::CapabilityGrant` (extend: Resolve filesystem, network, tool, and secret grants for one attempt.); `atlas/security/plugin_policy.py` (extend: Decide trusted/in-process versus subprocess eligibility and grant set.); `docs/security/subprocess-enforcement-matrix.md` (create: Record per-platform controls, gaps, and release claims.)
  * Epic boundary: Subprocess plugin isolation and enforceable resource controls — Run untrusted or high-risk plugins outside the core process with mediated inputs, explicit capabilities, bounded resources, deterministic termination, and visible platform limitations.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.
  * Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-020 requires: Third-party analyzers should not share process authority, unrestricted filesystem, or StateStore credentials.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Apply the unified resource budget and plugin capability policy using available OS controls while failing closed or visibly reducing assurance when enforcement is unavailable.
  * Component dispositions: `atlas/execution/limits.py` (create: Translate hierarchical budgets to platform CPU, memory, process, file, and time controls.); `atlas/execution/capabilities.py::CapabilityGrant` (extend: Resolve filesystem, network, tool, and secret grants for one attempt.); `atlas/security/plugin_policy.py` (extend: Decide trusted/in-process versus subprocess eligibility and grant set.); `docs/security/subprocess-enforcement-matrix.md` (create: Record per-platform controls, gaps, and release claims.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Enforce or monitor wall time, CPU, memory, process/thread count, file descriptors, output bytes, workspace/temp bytes, and opened files.
  * Deny network and external tools by default; grant allowlisted endpoints/tools with resolved immutable executable identity and arguments contract.
  * Provide secrets only through explicit short-lived references/channels and never general environment inheritance.
  * Record each control as enforced, monitored-only, unavailable, or not requested and feed actual usage to `ResourceBudgetManager`.

  Security and safety requirements

  * Do not claim sandboxing from subprocess separation alone.
  * Canonicalize and validate executable/tool paths, arguments, environment, endpoint scope, and workspace before launch.
  * Prevent command injection by using argument arrays and typed tool adapters, never shell interpolation.
  * If a required control is unavailable, reject untrusted plugin execution or require an explicit trusted reduced-assurance policy.

  Edge cases and outliers to handle

  * Memory spike before monitor samples.
  * Plugin execs another binary or opens inherited network socket.
  * Tool path replaced after validation.
  * Secret reference expires or is read repeatedly.

  Acceptance criteria (“done” definition)

  * Each subprocess attempt records requested, enforced, unavailable, and exceeded controls plus measured usage.
  * Network/tools/secrets are absent unless explicitly granted by deterministic policy.
  * Required unavailable controls block untrusted execution rather than silently weakening policy.
  * Tool and command-injection tests show no shell interpretation of plugin-controlled values.

  Testing plan

  * CPU/memory/process/temp/output exhaustion tests.
  * Network deny/allow tests.
  * Tool replacement/argument injection tests.
  * Secret leakage/expiry tests.
  * Reduced-assurance policy tests.
  * Platform enforcement matrix verification.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: CPU/memory/process/temp/output exhaustion tests., Network deny/allow tests., Tool replacement/argument injection tests., Secret leakage/expiry tests., Reduced-assurance policy tests., Platform enforcement matrix verification..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T22.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/limits.py, atlas/execution/capabilities.py::CapabilityGrant, atlas/security/plugin_policy.py, docs/security/subprocess-enforcement-matrix.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 88: Establish hostile-plugin and backend conformance gates

  1.2 source task(s): `T22.1.4`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T22.1.2, T22.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/execution/hostile_plugins/ (extend); tests/execution/test_backend_conformance.py (extend); scripts/run_plugin_isolation_matrix.py (create); .github/workflows/plugin-isolation.yml (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prove subprocess containment, failure mapping, cleanup, resource accounting, and semantic equivalence using a maintained synthetic hostile-plugin corpus on every supported platform.
  * Restore or protect this invariant: Every supported platform has a current pass/fail/reduced-assurance enforcement matrix.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `tests/execution/hostile_plugins/` (extend: Cover traversal, source access, network, spawn, flood, timeout, memory/temp exhaustion, protocol forgery, and secret discovery.); `tests/execution/test_backend_conformance.py` (extend: Run common WorkSpec/result/state/recovery expectations for all backends.); `scripts/run_plugin_isolation_matrix.py` (create: Produce machine-readable platform/control/test evidence.); `.github/workflows/plugin-isolation.yml` (create: Gate supported platform claims and retain reports.)
  * Epic boundary: Subprocess plugin isolation and enforceable resource controls — Run untrusted or high-risk plugins outside the core process with mediated inputs, explicit capabilities, bounded resources, deterministic termination, and visible platform limitations.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.
  * Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-020 requires: Third-party analyzers should not share process authority, unrestricted filesystem, or StateStore credentials.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prove subprocess containment, failure mapping, cleanup, resource accounting, and semantic equivalence using a maintained synthetic hostile-plugin corpus on every supported platform.
  * Component dispositions: `tests/execution/hostile_plugins/` (extend: Cover traversal, source access, network, spawn, flood, timeout, memory/temp exhaustion, protocol forgery, and secret discovery.); `tests/execution/test_backend_conformance.py` (extend: Run common WorkSpec/result/state/recovery expectations for all backends.); `scripts/run_plugin_isolation_matrix.py` (create: Produce machine-readable platform/control/test evidence.); `.github/workflows/plugin-isolation.yml` (create: Gate supported platform claims and retain reports.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define benign reference plugins and one synthetic fixture for every declared threat/failure mode.
  * Run in-process only for trusted fixtures and subprocess for hostile/untrusted cases; compare normalized valid results.
  * Verify workspace containment, process cleanup, budget metrics, denied grants, error taxonomy, checkpoint/recovery, and status evidence.
  * Publish a versioned enforcement report tied to OS/kernel/runtime, plugin digest, and test suite.

  Security and safety requirements

  * Use inert synthetic payloads and loopback/fake services; do not include live destructive exploit code or credentials.
  * Fail the release gate when a mandatory supported-platform containment test regresses or is skipped without approved exception.
  * Scan retained output/bundles for synthetic secret leakage and path escape.
  * Ensure test plugins cannot access CI release credentials or host-wide writable locations.

  Edge cases and outliers to handle

  * CI runner itself lacks required kernel controls.
  * Hostile plugin destabilizes or fills shared runner.
  * Test passes due to missing assertion after early failure.
  * Platform semantics differ in child-tree cleanup.

  Acceptance criteria (“done” definition)

  * Every supported platform has a current pass/fail/reduced-assurance enforcement matrix.
  * Hostile fixtures cannot commit lifecycle state or escape mediated inputs under claimed controls.
  * Cleanup and resource-accounting assertions pass after every failure class.
  * No unsupported control is marketed as enforced and no mandatory isolation test is silently skipped.

  Testing plan

  * Backend conformance suite.
  * Hostile corpus integration tests.
  * Runner resource/cleanup assertions.
  * Secret/path escape scans.
  * Skip/exception policy tests.
  * Repeated/soak hostile-plugin tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Backend conformance suite., Hostile corpus integration tests., Runner resource/cleanup assertions., Secret/path escape scans., Skip/exception policy tests., Repeated/soak hostile-plugin tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T22.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/execution/hostile_plugins/, tests/execution/test_backend_conformance.py, scripts/run_plugin_isolation_matrix.py, .github/workflows/plugin-isolation.yml.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 89: Define retention classes and implement reference-safe cleanup

  1.2 source task(s): `T23.1.1`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T12.1.4, T17.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/retention/models.py (create); atlas/retention/service.py::RetentionManager (create); atlas/schema/migrations/*_retention.sql (create); docs/operations/retention.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create a policy-driven retention and garbage-collection service that distinguishes authoritative history, replay-critical content, workspaces, caches, telemetry, and publications while never deleting referenced evidence.
  * Restore or protect this invariant: Retention periods and required preserved classes are explicitly resolved and versioned before deletion is enabled.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15.

  Where this applies

  * Primary affected components: `atlas/retention/models.py` (create: Define retention classes, holds, eligibility, plan, attempt, and result records.); `atlas/retention/service.py::RetentionManager` (create: Plan, verify, execute, and reconcile safe deletions.); `atlas/schema/migrations/*_retention.sql` (create: Persist holds, cleanup plans/attempts, tombstones, and verification.); `docs/operations/retention.md` (create: Document policy, dry-run, legal/incident holds, recovery, and limitations.)
  * Epic boundary: Retention, compatibility, plugin SDK, and source-provider evolution — Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Retention, compatibility, plugin SDK, and source-provider evolution.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create a policy-driven retention and garbage-collection service that distinguishes authoritative history, replay-critical content, workspaces, caches, telemetry, and publications while never deleting referenced evidence.
  * Component dispositions: `atlas/retention/models.py` (create: Define retention classes, holds, eligibility, plan, attempt, and result records.); `atlas/retention/service.py::RetentionManager` (create: Plan, verify, execute, and reconcile safe deletions.); `atlas/schema/migrations/*_retention.sql` (create: Persist holds, cleanup plans/attempts, tombstones, and verification.); `docs/operations/retention.md` (create: Document policy, dry-run, legal/incident holds, recovery, and limitations.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Classify lifecycle records, events/outbox, content blobs, quarantine/workspaces, checkpoints, plugin outputs, diagnostics, and telemetry by minimum retention and replay/lineage dependency.
  * Compute deletion eligibility from reference graph, current/nonterminal state, holds, publication lineage, backup policy, and configured retention version.
  * Require dry-run plan with counts/bytes/reasons, explicit confirmation/policy for consequential deletion, then no-follow/no-replace safe execution and post-delete verification.
  * Persist tombstone and cleanup evidence without retaining prohibited content; support interrupted-run reconciliation.

  Security and safety requirements

  * Never follow symlinks or delete outside managed roots; operate by durable managed identity rather than arbitrary path strings.
  * Do not delete content/evidence/checkpoints needed for current decisions, publications, active recovery, audit, or declared replay guarantees.
  * Apply least-privilege filesystem/store access and bound traversal/query/delete batches.
  * Treat model/plugin recommendations as proposals only; deterministic policy and reference checks authorize deletion.

  Edge cases and outliers to handle

  * Content blob referenced by multiple jobs/publications.
  * Hold is added between plan and execution.
  * Deletion succeeds but database update fails or vice versa.
  * Legacy/unindexed object cannot prove ownership.

  Acceptance criteria (“done” definition)

  * Retention periods and required preserved classes are explicitly resolved and versioned before deletion is enabled.
  * Dry-run and execution use the same immutable plan or fail on changed preconditions.
  * No referenced, held, active, or unknown-ownership object is deleted.
  * Interrupted cleanup is idempotently reconciled with durable per-object evidence.

  Testing plan

  * Eligibility/reference graph tests.
  * Symlink/path escape negative tests.
  * Concurrent hold/reference race tests.
  * Partial deletion/transaction fault tests.
  * Large-batch/quota performance tests.
  * Backup/restore and audit evidence tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Eligibility/reference graph tests., Symlink/path escape negative tests., Concurrent hold/reference race tests., Partial deletion/transaction fault tests., Large-batch/quota performance tests., Backup/restore and audit evidence tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T23.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/retention/models.py, atlas/retention/service.py::RetentionManager, atlas/schema/migrations/*_retention.sql, docs/operations/retention.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 90: Implement the compatibility catalog and deprecation telemetry

  1.2 source task(s): `T23.1.2`
  Priority: `P2`
  Estimated effort: `14 hours`
  Dependencies: `T3.1.4, T4.1.4, T8.1.4, T14.1.4, T18.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/compat/catalog.py::CompatibilityCatalog (create); atlas/compat/translators.py (create); atlas/status/projection.py (extend); docs/compatibility.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Centralize supported versions, translators, compatibility windows, deprecation state, and stored-data/API/plugin/config/checkpoint decisions so adapters cannot silently reinterpret records.
  * Restore or protect this invariant: Every persisted/public contract has one catalog entry and explicit read/write/deprecation policy.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15.

  Where this applies

  * Primary affected components: `atlas/compat/catalog.py::CompatibilityCatalog` (create: Declare supported producers/consumers, migration paths, read/write ranges, and deprecations.); `atlas/compat/translators.py` (create: Host explicit deterministic one-version transformations with provenance.); `atlas/status/projection.py` (extend: Expose compatibility/deprecation/reduced-readability markers.); `docs/compatibility.md` (create: Publish matrices and support/deprecation policy.)
  * Epic boundary: Retention, compatibility, plugin SDK, and source-provider evolution — Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Retention, compatibility, plugin SDK, and source-provider evolution.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Centralize supported versions, translators, compatibility windows, deprecation state, and stored-data/API/plugin/config/checkpoint decisions so adapters cannot silently reinterpret records.
  * Component dispositions: `atlas/compat/catalog.py::CompatibilityCatalog` (create: Declare supported producers/consumers, migration paths, read/write ranges, and deprecations.); `atlas/compat/translators.py` (create: Host explicit deterministic one-version transformations with provenance.); `atlas/status/projection.py` (extend: Expose compatibility/deprecation/reduced-readability markers.); `docs/compatibility.md` (create: Publish matrices and support/deprecation policy.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Register database, config, pipeline, event, plugin, finding/evidence, checkpoint, protocol, API, and manifest schemas with current/read/write ranges.
  * Require an explicit translator or hard incompatibility; never best-effort unknown-field guessing for authority-bearing records.
  * Record original version/digest, translator chain, output version/digest, warnings, and lossiness.
  * Emit bounded deprecation telemetry and operator reports before write support is removed.

  Security and safety requirements

  * Reject downgrade paths that discard authority, provenance, safety, actor, or signature fields.
  * Treat external/plugin schema declarations as untrusted until catalog validation.
  * Sign/hash release compatibility artifacts as part of package provenance.
  * Do not expose customer identifiers or raw payloads in deprecation metrics.

  Edge cases and outliers to handle

  * Record is newer than runtime.
  * Translator chain is missing, cyclic, or lossy.
  * Read compatibility exists but write-back would corrupt data.
  * Plugin supports overlapping but incompatible minor versions.

  Acceptance criteria (“done” definition)

  * Every persisted/public contract has one catalog entry and explicit read/write/deprecation policy.
  * Unsupported or lossy authority-bearing conversions fail closed with actionable status.
  * Compatibility reports identify affected records/plugins/configurations before upgrade.
  * Deprecation removal requires evidence that migration and rollback gates passed.

  Testing plan

  * Catalog completeness tests.
  * Translator golden/property tests.
  * Unknown/newer/downgrade negative tests.
  * Plugin/protocol negotiation tests.
  * Deprecation telemetry cardinality tests.
  * Upgrade/rollback compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Catalog completeness tests., Translator golden/property tests., Unknown/newer/downgrade negative tests., Plugin/protocol negotiation tests., Deprecation telemetry cardinality tests., Upgrade/rollback compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T23.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/compat/catalog.py::CompatibilityCatalog, atlas/compat/translators.py, atlas/status/projection.py, docs/compatibility.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 91: Deliver the plugin SDK, fixtures, and contract-validation CLI

  1.2 source task(s): `T23.1.3`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T14.1.4, T15.1.4, T22.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/plugin_sdk/ (create); atlas/cli.py (extend); examples/plugins/ (create); docs/plugins/sdk.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make safe extension development practical through typed packages, examples, synthetic artifacts, backend/registry conformance, and actionable validation without exposing internal state.
  * Restore or protect this invariant: A third party can implement and validate a plugin without importing private runtime/persistence APIs.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15.

  Where this applies

  * Primary affected components: `atlas/plugin_sdk/` (create: Publish stable descriptors, request/result models, errors, fixtures, and test helpers.); `atlas/cli.py` (extend: Add `plugin inspect`, `plugin validate`, and `plugin test` through supported APIs.); `examples/plugins/` (create: Provide minimal trusted and subprocess-safe analyzers/handlers with no secrets.); `docs/plugins/sdk.md` (create: Document lifecycle boundaries, capabilities, compatibility, testing, packaging, and release.)
  * Epic boundary: Retention, compatibility, plugin SDK, and source-provider evolution — Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
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
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Preserve the local filesystem as the evidenced near-term source while specifying how future read-only providers must establish stable source roots, generations, occurrences, snapshots, and mutation evidence.
  * Restore or protect this invariant: Local provider passes the contract without changing accepted local semantics.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15.

  Where this applies

  * Primary affected components: `atlas/sources/provider.py::SourceProvider` (create: Define registration, observation, stable locator, content-open, mutation token, and capability contracts.); `atlas/sources/registry.py::SourceProviderRegistry` (create: Provide deterministic provider registration and compatibility validation.); `atlas/sources/local.py` (refactor: Implement the contract for local directories/files through SourceAccessBroker.); `docs/architecture/source-providers.md` (create: Document required semantics and explicit deferred providers.)
  * Epic boundary: Retention, compatibility, plugin SDK, and source-provider evolution — Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
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
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Turn the current narrow test workflow into a documented, reviewable matrix of supported Python/OS/filesystem/resource controls and mandatory gates with explicit reduced-assurance rules.
  * Restore or protect this invariant: Supported and reduced-assurance platforms are explicitly resolved and versioned.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-024; REQ-029; PDF:p.20,p.24,p.26,p.27,p.28.

  Where this applies

  * Primary affected components: `.github/workflows/quality.yml` (create: Run format, lint, type, unit, integration, schema, docs, and packaging gates.); `pyproject.toml` (extend: Pin tool configuration, supported Python metadata, extras, and test markers.); `docs/development/quality-gates.md` (create: Define mandatory/optional jobs, skips, ownership, and evidence retention.); `docs/compatibility.md` (extend: Publish supported and reduced-assurance platform matrix.)
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

* [ ] TODO 97: Define and approve quantitative scale-adapter trigger evidence

  1.2 source task(s): `T25.1.1`
  Priority: `P3`
  Estimated effort: `12 hours`
  Dependencies: `T4.1.4, T12.1.4, T18.1.4, T24.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `docs/decisions/scale-adapter-trigger.md (create); benchmarks/scale_triggers/ (create); atlas/config/scale.py (create); ATLAS_Production_Task_Crosswalk.csv (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Require a workload-specific decision record showing why SQLite or local content storage fails measured contention, capacity, durability, recovery, availability, or multi-host requirements before adapter implementation begins.
  * Restore or protect this invariant: Trigger criteria, measurement procedure, and decision authority are resolved and versioned.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `docs/decisions/scale-adapter-trigger.md` (create: Record workload, environment, measurements, alternatives, cost, risks, and decision.); `benchmarks/scale_triggers/` (create: Retain repeatable local-backend workloads and raw results.); `atlas/config/scale.py` (create: Represent selected backend only after an approved compatibility decision.); `ATLAS_Production_Task_Crosswalk.csv` (extend: Link trigger evidence to deferred adapter tasks and original AT-021.)
  * Epic boundary: Measured optional PostgreSQL and object-storage adapters — Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.
  * Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-021 requires: Additional stores are justified only when SQLite/local CAS fail defined workloads while semantics are already stable.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Require a workload-specific decision record showing why SQLite or local content storage fails measured contention, capacity, durability, recovery, availability, or multi-host requirements before adapter implementation begins.
  * Component dispositions: `docs/decisions/scale-adapter-trigger.md` (create: Record workload, environment, measurements, alternatives, cost, risks, and decision.); `benchmarks/scale_triggers/` (create: Retain repeatable local-backend workloads and raw results.); `atlas/config/scale.py` (create: Represent selected backend only after an approved compatibility decision.); `ATLAS_Production_Task_Crosswalk.csv` (extend: Link trigger evidence to deferred adapter tasks and original AT-021.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define candidate triggers: write/read contention, dataset/row/blob size, recovery objective, multi-host coordination, storage durability/availability, operational backup, and lifecycle cost.
  * Benchmark/soak the local backends under the actual target workload and identify the bottleneck with raw evidence.
  * Compare logic/index/batching/checkpoint/retention improvements before infrastructure replacement.
  * Record selected/no-go decision, expected measurable benefit, complexity/operational cost, compatibility, migration, rollback, and disproof criteria.

  Security and safety requirements

  * Do not put production data/secrets into benchmark artifacts.
  * A vendor/backend choice cannot override lifecycle, provenance, event, or safety invariants.
  * Record deployment IAM/TLS/secret requirements separately from core semantics.
  * Reject pressure to implement scale adapters from terminology, fashion, or an arbitrary task completion target.

  Edge cases and outliers to handle

  * No local workload reproduces the claimed bottleneck.
  * Benchmark bottleneck is filesystem/analyzer rather than database/store.
  * Multi-host requirement appears before remote-worker semantics are ready.
  * Measurements vary by hardware or cache.

  Acceptance criteria (“done” definition)

  * Trigger criteria, measurement procedure, and decision authority are resolved and versioned.
  * Raw evidence demonstrates a specific local limitation and the proposed adapter addresses it.
  * Simpler local optimizations are tested or explicitly rejected with evidence.
  * A no-go result keeps adapter tasks deferred without being treated as failure.

  Testing plan

  * Benchmark repeatability tests.
  * Bottleneck attribution experiments.
  * Semantic equivalence checks under local optimizations.
  * Decision-record completeness validation.
  * Secret/provenance scans.
  * Independent review/reproduction.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Benchmark repeatability tests., Bottleneck attribution experiments., Semantic equivalence checks under local optimizations., Decision-record completeness validation., Secret/provenance scans., Independent review/reproduction..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T25.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: docs/decisions/scale-adapter-trigger.md, benchmarks/scale_triggers/, atlas/config/scale.py, ATLAS_Production_Task_Crosswalk.csv.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 98: Finalize backend conformance and one-authority migration contracts

  1.2 source task(s): `T25.1.2`
  Priority: `P3`
  Estimated effort: `14 hours`
  Dependencies: `T25.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/conformance.py (extend); atlas/storage/conformance.py (extend); atlas/migration/backend.py (create); docs/architecture/backend-conformance.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify the exact semantic, transactional, consistency, backup, cutover, and rollback obligations that any alternate StateStore or ContentStore must pass unchanged.
  * Restore or protect this invariant: Conformance suites are backend-neutral and pass for SQLite/local content before alternate implementation.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/persistence/conformance.py` (extend: Cover transactions, locks, migrations, events, claims, idempotency, recovery, and queries.); `atlas/storage/conformance.py` (extend: Cover immutable writes, hash verification, references, reconciliation, and retention.); `atlas/migration/backend.py` (create: Define copy, verify, freeze/cutover, authority marker, and rollback protocols.); `docs/architecture/backend-conformance.md` (create: Document consistency model and no-dual-writer invariant.)
  * Epic boundary: Measured optional PostgreSQL and object-storage adapters — Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.
  * Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-021 requires: Additional stores are justified only when SQLite/local CAS fail defined workloads while semantics are already stable.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify the exact semantic, transactional, consistency, backup, cutover, and rollback obligations that any alternate StateStore or ContentStore must pass unchanged.
  * Component dispositions: `atlas/persistence/conformance.py` (extend: Cover transactions, locks, migrations, events, claims, idempotency, recovery, and queries.); `atlas/storage/conformance.py` (extend: Cover immutable writes, hash verification, references, reconciliation, and retention.); `atlas/migration/backend.py` (create: Define copy, verify, freeze/cutover, authority marker, and rollback protocols.); `docs/architecture/backend-conformance.md` (create: Document consistency model and no-dual-writer invariant.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define exact StateStore isolation/transaction/constraint/sequence/locking/time semantics and ContentStore integrity/read-after-write/list/delete semantics.
  * Define source and target schema/provider version compatibility, snapshot/copy strategy, verification manifest, maintenance/read-only window, and authority marker.
  * Require one writable authoritative backend at a time; shadow copies remain non-authoritative until verified cutover.
  * Define rollback preconditions after new writes and how copied/unknown objects are retained/reconciled.

  Security and safety requirements

  * Prevent split-brain through a deployment authority token/config digest and startup refusal on conflicting writable backends.
  * Use least-privilege migration credentials, encrypted transport where external, and secret references.
  * Verify row/blob counts, identities, hashes, constraints, lineage, decisions, events, and checkpoints before cutover.
  * Do not accept eventual consistency where a core invariant requires read-after-write without an explicit adapter mechanism.

  Edge cases and outliers to handle

  * Partial snapshot/copy.
  * Writes occur during verification.
  * Source and target clocks/order semantics differ.
  * Rollback target cannot represent new schema records.

  Acceptance criteria (“done” definition)

  * Conformance suites are backend-neutral and pass for SQLite/local content before alternate implementation.
  * Migration protocol makes writable authority explicit and prevents dual writers.
  * Verification manifest covers all authority-bearing rows/blobs and lineage.
  * Rollback feasibility and cutoff are explicit before cutover.

  Testing plan

  * Reference-backend conformance tests.
  * Authority-marker/split-brain negative tests.
  * Partial copy/write-race fault tests.
  * Consistency/order/transaction tests.
  * Verification manifest tests.
  * Rollback cutoff compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Reference-backend conformance tests., Authority-marker/split-brain negative tests., Partial copy/write-race fault tests., Consistency/order/transaction tests., Verification manifest tests., Rollback cutoff compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T25.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/conformance.py, atlas/storage/conformance.py, atlas/migration/backend.py, docs/architecture/backend-conformance.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 99: Implement and validate the optional PostgreSQL StateStore

  1.2 source task(s): `T25.1.3`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T25.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/persistence/postgres.py::PostgresStateStore (create); atlas/schema/postgres/ (create); atlas/config/persistence.py (extend); tests/persistence/test_postgres_conformance.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Add PostgreSQL only behind the proven StateStore contract with equivalent transitions, transactions, events, claims, recovery, migrations, and diagnostics.
  * Restore or protect this invariant: PostgreSQL passes the same StateStore, state-machine, crash, event, claim, idempotency, migration, and status tests as SQLite.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/persistence/postgres.py::PostgresStateStore` (create: Implement StateStore with explicit transaction and connection ownership.); `atlas/schema/postgres/` (create: Provide versioned PostgreSQL migrations with parity mapping.); `atlas/config/persistence.py` (extend: Select one backend with typed DSN secret reference and pool settings.); `tests/persistence/test_postgres_conformance.py` (create: Run full conformance, fault, migration, and load suites.)
  * Epic boundary: Measured optional PostgreSQL and object-storage adapters — Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.
  * Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-021 requires: Additional stores are justified only when SQLite/local CAS fail defined workloads while semantics are already stable.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Add PostgreSQL only behind the proven StateStore contract with equivalent transitions, transactions, events, claims, recovery, migrations, and diagnostics.
  * Component dispositions: `atlas/persistence/postgres.py::PostgresStateStore` (create: Implement StateStore with explicit transaction and connection ownership.); `atlas/schema/postgres/` (create: Provide versioned PostgreSQL migrations with parity mapping.); `atlas/config/persistence.py` (extend: Select one backend with typed DSN secret reference and pool settings.); `tests/persistence/test_postgres_conformance.py` (create: Run full conformance, fault, migration, and load suites.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Implement transactions, guarded transitions, sequence allocation, outbox, claims/leases/fencing, idempotency, checkpoints, lineage queries, and migration locks under documented isolation.
  * Use bounded connection pool/lifecycle, timeouts, cancellation, retryable transaction handling, and health/readiness.
  * Implement SQLite-to-PostgreSQL snapshot/copy/verify/cutover tooling using the one-authority contract.
  * Document backup/restore, maintenance, upgrades, operational dependencies, and rollback cutoff.

  Security and safety requirements

  * Require TLS/credential/role/schema isolation as deployment controls and secret references rather than config plaintext.
  * Use parameterized SQL and bounded queries; test injection and denial-of-service inputs.
  * Fence duplicate coordinators and handle serializable/deadlock retries only when operation transaction semantics permit.
  * Do not expose database credentials to plugins, workers, events, or diagnostics.

  Edge cases and outliers to handle

  * Network partition or failover during commit.
  * Deadlock/serialization failure.
  * Pool exhaustion or long transaction.
  * Migration partially applies or old runtime reconnects.

  Acceptance criteria (“done” definition)

  * PostgreSQL passes the same StateStore, state-machine, crash, event, claim, idempotency, migration, and status tests as SQLite.
  * Cutover/rollback drill preserves counts, identities, constraints, sequence, event order, and hashes.
  * One writable backend authority is enforced at startup and during migration.
  * Measured workload shows the approved benefit without changing lifecycle semantics.

  Testing plan

  * StateStore conformance suite.
  * Network/failover/deadlock fault tests.
  * Pool/contention/load tests.
  * Migration/cutover/rollback tests.
  * SQL injection/credential-redaction tests.
  * SQLite/PostgreSQL semantic differential tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: StateStore conformance suite., Network/failover/deadlock fault tests., Pool/contention/load tests., Migration/cutover/rollback tests., SQL injection/credential-redaction tests., SQLite/PostgreSQL semantic differential tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T25.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/persistence/postgres.py::PostgresStateStore, atlas/schema/postgres/, atlas/config/persistence.py, tests/persistence/test_postgres_conformance.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 100: Implement and validate the optional object-backed ContentStore

  1.2 source task(s): `T25.1.4`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T25.1.2, T25.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/storage/object_store.py::ObjectContentStore (create); atlas/config/storage.py (extend); atlas/migration/content.py (create); tests/storage/test_object_store_conformance.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Add object storage behind immutable content contracts with hash verification, staged commit, consistency handling, references, retention, reconciliation, and verified migration.
  * Restore or protect this invariant: Object backend passes immutable ContentStore, integrity, reference, retention, recovery, and replay tests.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/storage/object_store.py::ObjectContentStore` (create: Implement content operations with provider-neutral object client.); `atlas/config/storage.py` (extend: Select provider/bucket/prefix/credentials/consistency settings through typed config.); `atlas/migration/content.py` (create: Copy, verify, resume, cut over, and reconcile local/object content.); `tests/storage/test_object_store_conformance.py` (create: Run conformance with deterministic fake and approved integration provider.)
  * Epic boundary: Measured optional PostgreSQL and object-storage adapters — Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.
  * Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-021 requires: Additional stores are justified only when SQLite/local CAS fail defined workloads while semantics are already stable.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Add object storage behind immutable content contracts with hash verification, staged commit, consistency handling, references, retention, reconciliation, and verified migration.
  * Component dispositions: `atlas/storage/object_store.py::ObjectContentStore` (create: Implement content operations with provider-neutral object client.); `atlas/config/storage.py` (extend: Select provider/bucket/prefix/credentials/consistency settings through typed config.); `atlas/migration/content.py` (create: Copy, verify, resume, cut over, and reconcile local/object content.); `tests/storage/test_object_store_conformance.py` (create: Run conformance with deterministic fake and approved integration provider.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Stage uploads under attempt identity, stream/hash/size verify, commit immutable canonical key, verify visibility/metadata/bytes, and record provider object version/etag as supplemental.
  * Handle provider consistency by explicit read/verify/retry rules without treating ETag/path as canonical content identity.
  * Implement resumable copy manifest, reference validation, retention/holds, orphan reconciliation, and local-to-object cutover.
  * Document durability/availability, backup/replication, lifecycle policies, cost, health, and rollback.

  Security and safety requirements

  * Use least-privilege bucket/prefix credentials, TLS, optional encryption policy, secret references, and deny public access by default.
  * Prevent key/prefix/path traversal, metadata injection, bucket confusion, cross-tenant access, and overwrite of existing different content.
  * Do not expose signed URLs/credentials broadly; scope and expire any mediated access.
  * Verify content by SHA-256 after transfer; provider metadata alone is insufficient.

  Edge cases and outliers to handle

  * Upload completes but response is lost.
  * Object is not immediately visible.
  * Same canonical key exists with wrong bytes.
  * Credentials/bucket policy change during migration.

  Acceptance criteria (“done” definition)

  * Object backend passes immutable ContentStore, integrity, reference, retention, recovery, and replay tests.
  * No-replace commit and byte verification prevent canonical-key corruption.
  * Migration/cutover/rollback preserves all referenced content hashes and one writable authority.
  * Approved workload demonstrates benefit and provider consistency limitations are explicit.

  Testing plan

  * ContentStore conformance suite.
  * Timeout/unknown upload/reconciliation tests.
  * Consistency visibility tests.
  * Wrong-byte/key/prefix injection negative tests.
  * Migration/resume/cutover/rollback tests.
  * Credential/URL redaction and least-privilege tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: ContentStore conformance suite., Timeout/unknown upload/reconciliation tests., Consistency visibility tests., Wrong-byte/key/prefix injection negative tests., Migration/resume/cutover/rollback tests., Credential/URL redaction and least-privilege tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T25.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/storage/object_store.py::ObjectContentStore, atlas/config/storage.py, atlas/migration/content.py, tests/storage/test_object_store_conformance.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 101: Define the authenticated remote worker protocol and compatibility handshake

  1.2 source task(s): `T26.1.1`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T15.1.4, T18.1.4, T21.1.4, T25.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/remote_protocol.py (create); atlas/execution/remote.py::RemoteExecutionBackend (create); atlas/worker/contracts.py (create); docs/architecture/remote-worker-protocol.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify immutable work dispatch, leases, heartbeats, fencing, scoped artifacts, result integrity, cancellation, and version negotiation without granting workers lifecycle authority.
  * Restore or protect this invariant: Protocol is versioned and compatibility failure is explicit before work starts.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29.

  Where this applies

  * Primary affected components: `atlas/execution/remote_protocol.py` (create: Define worker registration, capability, lease, WorkSpec, progress, result, cancel, and drain envelopes.); `atlas/execution/remote.py::RemoteExecutionBackend` (create: Implement coordinator-side backend contract without scheduler authority.); `atlas/worker/contracts.py` (create: Expose worker-side typed protocol and compatibility catalog integration.); `docs/architecture/remote-worker-protocol.md` (create: Document trust, identity, failure, ordering, and non-authority invariants.)
  * Epic boundary: Optional remote worker execution — Scale execution location without changing phase barriers, coordinator authority, work semantics, exact-byte identity, or durable recovery.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.
  * Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-022 requires: Remote execution is an infrastructure adapter, not a reason to redefine lifecycle semantics.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify immutable work dispatch, leases, heartbeats, fencing, scoped artifacts, result integrity, cancellation, and version negotiation without granting workers lifecycle authority.
  * Component dispositions: `atlas/execution/remote_protocol.py` (create: Define worker registration, capability, lease, WorkSpec, progress, result, cancel, and drain envelopes.); `atlas/execution/remote.py::RemoteExecutionBackend` (create: Implement coordinator-side backend contract without scheduler authority.); `atlas/worker/contracts.py` (create: Expose worker-side typed protocol and compatibility catalog integration.); `docs/architecture/remote-worker-protocol.md` (create: Document trust, identity, failure, ordering, and non-authority invariants.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define service/worker identity, protocol version, runtime/plugin/backend capability digest, WorkSpec digest, immutable input references, budgets, deadline, lease/fencing token, idempotency key, and result/evidence digest.
  * Negotiate compatible versions/capabilities before assignment and reject semantic/plugin/config mismatches.
  * Define heartbeat/lease renewal, cancellation acknowledgement, drain, progress/checkpoint reference, result upload/verification, stale rejection, and replay.
  * Keep phase/work planning and authoritative attempt transitions in coordinator/StateStore.

  Security and safety requirements

  * Use mutual service identity and encrypted transport as deployment controls; scope credentials and rotate/revoke them.
  * Workers receive no StateStore credentials and only single-job/attempt/content-scoped access.
  * Sign or authenticate protocol messages and bind all results to WorkSpec/attempt/fencing identity.
  * Reject worker-provided lifecycle state, policy, evidence authority, publication, or arbitrary capability claims.

  Edge cases and outliers to handle

  * Worker upgrades between handshake and result.
  * Clock skew and delayed heartbeat.
  * Duplicate assignment/result.
  * Malicious worker forges another work item or content digest.

  Acceptance criteria (“done” definition)

  * Protocol is versioned and compatibility failure is explicit before work starts.
  * Worker cannot mutate lifecycle state or access undeclared artifacts.
  * Stale/duplicate/forged results are rejected deterministically and retained as evidence.
  * Local and remote backends share WorkSpec/result conformance semantics.

  Testing plan

  * Protocol codec/golden/fuzz tests.
  * Compatibility negotiation tests.
  * Identity/forgery/replay negative tests.
  * Lease/heartbeat/clock tests.
  * Local/remote contract differential tests.
  * Credential scope/revocation tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Protocol codec/golden/fuzz tests., Compatibility negotiation tests., Identity/forgery/replay negative tests., Lease/heartbeat/clock tests., Local/remote contract differential tests., Credential scope/revocation tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T26.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/remote_protocol.py, atlas/execution/remote.py::RemoteExecutionBackend, atlas/worker/contracts.py, docs/architecture/remote-worker-protocol.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 102: Implement the least-privileged remote worker service

  1.2 source task(s): `T26.1.2`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T26.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/worker/service.py::AtlasWorker (create); atlas/worker/config.py (create); atlas/worker/artifacts.py (create); docs/operations/worker.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Run assigned WorkSpecs through approved execution backends with scoped artifact access, resource policy, heartbeats, cancellation, and no direct control-plane persistence.
  * Restore or protect this invariant: Worker completes only authenticated assigned WorkSpecs and cannot write lifecycle authority.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29.

  Where this applies

  * Primary affected components: `atlas/worker/service.py::AtlasWorker` (create: Own registration, assignment lifecycle, backend execution, heartbeat, result, and drain.); `atlas/worker/config.py` (create: Define service identity, capabilities, concurrency, cache, resource, and endpoint settings.); `atlas/worker/artifacts.py` (create: Fetch/verify scoped immutable inputs and upload/verify outputs.); `docs/operations/worker.md` (create: Document deployment, trust, upgrades, drain, diagnostics, and incidents.)
  * Epic boundary: Optional remote worker execution — Scale execution location without changing phase barriers, coordinator authority, work semantics, exact-byte identity, or durable recovery.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.
  * Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-022 requires: Remote execution is an infrastructure adapter, not a reason to redefine lifecycle semantics.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Run assigned WorkSpecs through approved execution backends with scoped artifact access, resource policy, heartbeats, cancellation, and no direct control-plane persistence.
  * Component dispositions: `atlas/worker/service.py::AtlasWorker` (create: Own registration, assignment lifecycle, backend execution, heartbeat, result, and drain.); `atlas/worker/config.py` (create: Define service identity, capabilities, concurrency, cache, resource, and endpoint settings.); `atlas/worker/artifacts.py` (create: Fetch/verify scoped immutable inputs and upload/verify outputs.); `docs/operations/worker.md` (create: Document deployment, trust, upgrades, drain, diagnostics, and incidents.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Advertise only locally verified backend/plugin/tool/resource capabilities and apply server-approved grants per assignment.
  * Fetch immutable inputs through scoped single-use/expiring references, verify content hashes, and isolate per-attempt workspace/cache.
  * Execute using in-process only for explicitly trusted plugins or subprocess for untrusted/high-risk work under the same policy.
  * Heartbeat/renew, honor cancel/drain, upload staged results/evidence, and discard/fence after lease loss.

  Security and safety requirements

  * No StateStore/database credentials or broad content-store credentials on workers.
  * Use least-privilege service identity, secure bootstrap/rotation, host hardening, secret references, and no raw secrets in diagnostics.
  * Verify executable/plugin/tool/image identity and sanitize all inputs/outputs as with local backends.
  * Cache by content identity with integrity and retention controls; never treat cache presence as provenance.

  Edge cases and outliers to handle

  * Artifact transfer interrupted or wrong bytes received.
  * Lease lost while plugin still runs.
  * Worker disk full or cache corrupt.
  * Worker compromised or identity revoked.

  Acceptance criteria (“done” definition)

  * Worker completes only authenticated assigned WorkSpecs and cannot write lifecycle authority.
  * All input/output bytes are hash-verified and scoped to the attempt.
  * Lease loss/cancel/drain leads to deterministic backend stop/result handling.
  * Compromise/revocation can fence the worker and preserve investigation evidence.

  Testing plan

  * Worker service lifecycle tests.
  * Scoped artifact token/expiry tests.
  * Transfer corruption/interruption tests.
  * Lease-loss/cancel/drain tests.
  * Cache integrity/retention tests.
  * Identity revocation/compromise tabletop tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Worker service lifecycle tests., Scoped artifact token/expiry tests., Transfer corruption/interruption tests., Lease-loss/cancel/drain tests., Cache integrity/retention tests., Identity revocation/compromise tabletop tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T26.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/worker/service.py::AtlasWorker, atlas/worker/config.py, atlas/worker/artifacts.py, docs/operations/worker.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 103: Implement remote scheduling, result verification, cancellation, and fallback policy

  1.2 source task(s): `T26.1.3`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T26.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/remote_scheduler.py (create); atlas/execution/remote.py (extend); atlas/recovery/reconcilers.py (extend); atlas/status/projection.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Select eligible remote capacity within phase-internal work semantics, verify results before commit, and define loss/fallback behavior without changing phase order or duplicating side effects.
  * Restore or protect this invariant: One valid fenced result can commit for each work attempt.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29.

  Where this applies

  * Primary affected components: `atlas/execution/remote_scheduler.py` (create: Match WorkSpecs to compatible workers using bounded deterministic policy.); `atlas/execution/remote.py` (extend: Own assignment, lease, progress, cancel, result verification, and recovery mapping.); `atlas/recovery/reconcilers.py` (extend: Handle worker loss, transfer unknowns, stale result, and safe reassignment.); `atlas/status/projection.py` (extend: Show worker/lease/transfer/backend state without exposing secrets.)
  * Epic boundary: Optional remote worker execution — Scale execution location without changing phase barriers, coordinator authority, work semantics, exact-byte identity, or durable recovery.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.
  * Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-022 requires: Remote execution is an infrastructure adapter, not a reason to redefine lifecycle semantics.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Select eligible remote capacity within phase-internal work semantics, verify results before commit, and define loss/fallback behavior without changing phase order or duplicating side effects.
  * Component dispositions: `atlas/execution/remote_scheduler.py` (create: Match WorkSpecs to compatible workers using bounded deterministic policy.); `atlas/execution/remote.py` (extend: Own assignment, lease, progress, cancel, result verification, and recovery mapping.); `atlas/recovery/reconcilers.py` (extend: Handle worker loss, transfer unknowns, stale result, and safe reassignment.); `atlas/status/projection.py` (extend: Show worker/lease/transfer/backend state without exposing secrets.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Filter workers by protocol/runtime/plugin/capability/resource/data-locality compatibility and apply deterministic or explainable tie-breaking.
  * Persist assignment/lease before dispatch; verify authenticated result envelope, fencing, WorkSpec digest, output content hashes, schema, and budget evidence before commit.
  * Define cancellation/drain and local fallback/reassignment only for operations whose semantics and idempotency allow it.
  * Preserve work-item phase barrier and coordinator-owned aggregation/transition.

  Security and safety requirements

  * Scheduling metadata cannot grant capabilities beyond policy or leak sensitive source identity unnecessarily.
  * Reject stale worker, invalid signature, wrong WorkSpec/content, over-budget, or incompatible result.
  * Bound assignment/retry/transfer concurrency and protect against a malicious worker advertising infinite capacity.
  * Fallback cannot silently switch to a weaker isolation/trust backend.

  Edge cases and outliers to handle

  * Partition after assignment or after result upload.
  * Worker completes twice.
  * Cancel is lost and successor starts.
  * No compatible worker or capacity changes rapidly.

  Acceptance criteria (“done” definition)

  * One valid fenced result can commit for each work attempt.
  * Worker loss maps to deterministic wait/retry/reconcile/block behavior from operation semantics.
  * Fallback/reassignment is disabled for unsafe/unknown side effects and never weakens policy.
  * Remote execution preserves the same phase barriers, persistence, events, lineage, and status as local execution.

  Testing plan

  * Scheduling determinism/compatibility tests.
  * Partition/duplicate/stale result tests.
  * Cancel-loss/successor race tests.
  * Malicious capacity/capability negative tests.
  * Local/remote semantic differential tests.
  * High-volume assignment/backpressure tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Scheduling determinism/compatibility tests., Partition/duplicate/stale result tests., Cancel-loss/successor race tests., Malicious capacity/capability negative tests., Local/remote semantic differential tests., High-volume assignment/backpressure tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T26.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/remote_scheduler.py, atlas/execution/remote.py, atlas/recovery/reconcilers.py, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 104: Gate distributed execution with chaos, security, load, and operational evidence

  1.2 source task(s): `T26.1.4`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T26.1.2, T26.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/distributed/ (create); benchmarks/remote_workers/ (create); scripts/run_remote_chaos_matrix.py (create); docs/operations/remote-workers-runbook.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Demonstrate that remote execution adds measurable value and preserves semantics under partitions, worker loss, skew, incompatibility, malicious behavior, and sustained load before deployment.
  * Restore or protect this invariant: Remote backend passes all local backend/state/recovery/lineage conformance suites.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29.

  Where this applies

  * Primary affected components: `tests/distributed/` (create: Host network, worker, protocol, security, and semantic conformance scenarios.); `benchmarks/remote_workers/` (create: Measure transfer, queue, execution, recovery, throughput, and operational cost.); `scripts/run_remote_chaos_matrix.py` (create: Produce machine-readable partition/loss/replay/upgrade evidence.); `docs/operations/remote-workers-runbook.md` (create: Define rollout, drain, incident, revocation, recovery, and rollback.)
  * Epic boundary: Optional remote worker execution — Scale execution location without changing phase barriers, coordinator authority, work semantics, exact-byte identity, or durable recovery.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.
  * Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-022 requires: Remote execution is an infrastructure adapter, not a reason to redefine lifecycle semantics.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Demonstrate that remote execution adds measurable value and preserves semantics under partitions, worker loss, skew, incompatibility, malicious behavior, and sustained load before deployment.
  * Component dispositions: `tests/distributed/` (create: Host network, worker, protocol, security, and semantic conformance scenarios.); `benchmarks/remote_workers/` (create: Measure transfer, queue, execution, recovery, throughput, and operational cost.); `scripts/run_remote_chaos_matrix.py` (create: Produce machine-readable partition/loss/replay/upgrade evidence.); `docs/operations/remote-workers-runbook.md` (create: Define rollout, drain, incident, revocation, recovery, and rollback.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Test partitions at dispatch/heartbeat/result/ack, worker kill/restart, duplicate delivery, stale result, clock skew, protocol/plugin mismatch, artifact corruption, and control-plane outage.
  * Run malicious-worker scenarios for forged identities/results, capability overclaim, data access, resource reporting, and replay.
  * Benchmark against local execution including transfer overhead, utilization, throughput, recovery time, event/database pressure, and operator burden.
  * Progressively roll out by operation/plugin with canary, drain, fallback rules, and a local rollback path where safe.

  Security and safety requirements

  * Use isolated synthetic infrastructure and credentials; do not expose production stores or payloads.
  * Require service identity revocation, artifact-token revocation/expiry, audit retention, and incident containment evidence.
  * A chaos test may not silently bypass unknown-outcome or publication safeguards.
  * Document tenant isolation as unresolved/optional until a deployment requires it.

  Edge cases and outliers to handle

  * Control plane and workers partition asymmetrically.
  * Upgrade leaves mixed protocol/plugin versions.
  * Remote path is slower and less reliable than local.
  * Rollback occurs with leased in-flight work.

  Acceptance criteria (“done” definition)

  * Remote backend passes all local backend/state/recovery/lineage conformance suites.
  * Chaos matrix demonstrates stale fencing and no duplicate authoritative effects.
  * Benchmark and operations evidence justify distributed complexity for a defined workload.
  * Drain/rollback/revocation drill handles in-flight work without alternate authority.

  Testing plan

  * Network chaos/fault tests.
  * Malicious worker security tests.
  * Mixed-version/upgrade tests.
  * Load/soak/transfer benchmarks.
  * Canary/drain/rollback drills.
  * Evidence manifest and independent review.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Network chaos/fault tests., Malicious worker security tests., Mixed-version/upgrade tests., Load/soak/transfer benchmarks., Canary/drain/rollback drills., Evidence manifest and independent review..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T26.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/distributed/, benchmarks/remote_workers/, scripts/run_remote_chaos_matrix.py, docs/operations/remote-workers-runbook.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 105: Expose read-only and proposal-only MCP resources and tools

  1.2 source task(s): `T27.1.1`
  Priority: `P3`
  Estimated effort: `14 hours`
  Dependencies: `T17.1.4, T19.1.4, T20.1.4, T21.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/integrations/mcp.py (create); atlas/models/proposals.py::AnalysisProposal (create); docs/integrations/mcp.md (create); tests/integrations/test_mcp_read_tools.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide versioned MCP resources/tools for status, lineage, evidence, and bounded analytical proposals without direct lifecycle, filesystem, policy, review, or publication authority.
  * Restore or protect this invariant: MCP read/proposal tools cannot mutate lifecycle state, safety records, evidence authority, decisions, or publications.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/integrations/mcp.py` (create: Implement optional MCP server adapter over status/evidence/lineage/proposal services.); `atlas/models/proposals.py::AnalysisProposal` (create: Persist bounded non-authoritative model/agent proposals and provenance.); `docs/integrations/mcp.md` (create: Document tool semantics, trust boundaries, configuration, and disabled-by-default behavior.); `tests/integrations/test_mcp_read_tools.py` (create: Validate schemas, authority, hostile content, and compatibility.)
  * Epic boundary: Bounded MCP and operator interfaces — Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.
  * Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-023 requires: Agent/UI convenience must not become an alternate provenance, policy, or promotion authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Provide versioned MCP resources/tools for status, lineage, evidence, and bounded analytical proposals without direct lifecycle, filesystem, policy, review, or publication authority.
  * Component dispositions: `atlas/integrations/mcp.py` (create: Implement optional MCP server adapter over status/evidence/lineage/proposal services.); `atlas/models/proposals.py::AnalysisProposal` (create: Persist bounded non-authoritative model/agent proposals and provenance.); `docs/integrations/mcp.md` (create: Document tool semantics, trust boundaries, configuration, and disabled-by-default behavior.); `tests/integrations/test_mcp_read_tools.py` (create: Validate schemas, authority, hostile content, and compatibility.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Expose read-only job/status, artifact lineage, structural/evidence summaries, capability catalog, and proposal submission with strict schemas and pagination.
  * Label all model/agent output as proposed/inferred, record model/provider/prompt/tool/config/input evidence versions, and keep it separate from findings/evidence/decisions unless deterministic services accept it.
  * Use canonical service calls and return stable IDs/references rather than raw unrestricted files/content.
  * Make MCP an optional package/process that can be removed without core behavior changes.

  Security and safety requirements

  * Treat artifact text, finding text, external resources, prompts, and model output as untrusted data, never instructions to the server.
  * Grant least-privilege tool set and disable filesystem/network/command/publication capabilities by default.
  * Apply output encoding, content/size limits, secret/path redaction, rate/resource limits, and actor/session attribution.
  * Reject tool enumeration or arguments that request internal credentials, private APIs, StateStore access, or hidden capabilities.

  Edge cases and outliers to handle

  * Prompt injection embedded in archive metadata/finding/evidence.
  * Model hallucinates IDs or requests unsupported tool.
  * Very large lineage/evidence result.
  * Model/provider timeout or partial proposal.

  Acceptance criteria (“done” definition)

  * MCP read/proposal tools cannot mutate lifecycle state, safety records, evidence authority, decisions, or publications.
  * Every proposal is visibly non-authoritative and provenance-versioned.
  * Hostile artifact text cannot create an unrequested tool call or expand capabilities.
  * Removing/disabling MCP leaves core semantics and data readable.

  Testing plan

  * Tool/resource schema tests.
  * Prompt-injection and confused-deputy negative tests.
  * Hallucinated/stale ID tests.
  * Output encoding/redaction/size tests.
  * Model outage/timeout tests.
  * Core-without-MCP conformance tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Tool/resource schema tests., Prompt-injection and confused-deputy negative tests., Hallucinated/stale ID tests., Output encoding/redaction/size tests., Model outage/timeout tests., Core-without-MCP conformance tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T27.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/integrations/mcp.py, atlas/models/proposals.py::AnalysisProposal, docs/integrations/mcp.md, tests/integrations/test_mcp_read_tools.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 106: Route consequential MCP actions through deterministic command and review gates

  1.2 source task(s): `T27.1.2`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T27.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/integrations/mcp.py (extend); atlas/service/commands.py (extend); atlas/security/agent_policy.py (create); tests/integrations/test_mcp_commands.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Permit optional pause/cancel/review/publication requests only when they use the same CommandService, policy, idempotency, expected-version, attribution, and confirmation controls as human clients.
  * Restore or protect this invariant: No MCP command bypasses CommandService, lifecycle guards, review policy, publication checks, or expected-version/idempotency.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/integrations/mcp.py` (extend: Add explicitly configured consequential command adapters.); `atlas/service/commands.py` (extend: Accept agent actor type and confirmation/policy context without weakening guards.); `atlas/security/agent_policy.py` (create: Map tool, actor, environment, subject, and side-effect class to allowed request behavior.); `tests/integrations/test_mcp_commands.py` (create: Exercise replay, stale state, prompt injection, confirmation, and authority assertions.)
  * Epic boundary: Bounded MCP and operator interfaces — Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.
  * Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-023 requires: Agent/UI convenience must not become an alternate provenance, policy, or promotion authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Permit optional pause/cancel/review/publication requests only when they use the same CommandService, policy, idempotency, expected-version, attribution, and confirmation controls as human clients.
  * Component dispositions: `atlas/integrations/mcp.py` (extend: Add explicitly configured consequential command adapters.); `atlas/service/commands.py` (extend: Accept agent actor type and confirmation/policy context without weakening guards.); `atlas/security/agent_policy.py` (create: Map tool, actor, environment, subject, and side-effect class to allowed request behavior.); `tests/integrations/test_mcp_commands.py` (create: Exercise replay, stale state, prompt injection, confirmation, and authority assertions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Classify MCP tools by read, proposal, reversible control, review request, and external side effect; disable consequential classes by default.
  * Require deployment authorization, exact subject/state version, idempotency key, reason, policy evaluation, and explicit confirmation/approval for configured side effects.
  * Record requested versus accepted command and final authoritative outcome separately.
  * Never allow an AI actor to be the sole final promotion authority; it may submit a proposal/request for deterministic or human review.

  Security and safety requirements

  * Separate system policy/instructions from retrieved artifact/plugin text and never concatenate untrusted text into tool authorization.
  * Use actor/session/tool/model/provider IDs and audit denied/accepted/replayed/stale commands.
  * Prevent cross-job/tenant confused deputy behavior and tool-argument injection.
  * Limit request rate/cost/duration and revoke sessions/capabilities on suspicious behavior.

  Edge cases and outliers to handle

  * Artifact says to approve or publish itself.
  * Model repeats a stale command after timeout.
  * User confirmation changes subject/evidence before execution.
  * Agent session is revoked mid-request.

  Acceptance criteria (“done” definition)

  * No MCP command bypasses CommandService, lifecycle guards, review policy, publication checks, or expected-version/idempotency.
  * Prompt-injected artifact text cannot authorize or alter a tool action.
  * AI-only output cannot create an approved PromotionDecision.
  * Replay, stale state, revoked session, and changed confirmation return deterministic non-success outcomes.

  Testing plan

  * Authority-path integration tests.
  * Stored/indirect prompt-injection tests.
  * Replay/stale/confirmation race tests.
  * Cross-job/tenant confused-deputy tests.
  * Revocation/rate/cost-limit tests.
  * AI final-authority negative tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Authority-path integration tests., Stored/indirect prompt-injection tests., Replay/stale/confirmation race tests., Cross-job/tenant confused-deputy tests., Revocation/rate/cost-limit tests., AI final-authority negative tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T27.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/integrations/mcp.py, atlas/service/commands.py, atlas/security/agent_policy.py, tests/integrations/test_mcp_commands.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 107: Build an operator UI that preserves authority and uncertainty distinctions

  1.2 source task(s): `T27.1.3`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T27.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `ui/ (create); atlas/api/rest.py (extend); docs/operations/operator-ui.md (create); tests/ui/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Render jobs, phases, attempts, progress, controls, provenance, findings, evidence, decisions, publications, health, and diagnostics without collapsing observed, inferred, proposed, approved, or published states.
  * Restore or protect this invariant: UI never labels a finding/proposal as evidence, a request as decision, or an attempt as verified publication.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `ui/` (create: Host the optional operator client with generated API types and secure rendering.); `atlas/api/rest.py` (extend: Expose UI-required bounded status/evidence/review/publication endpoints only.); `docs/operations/operator-ui.md` (create: Document deployment, roles, workflows, status semantics, and incidents.); `tests/ui/` (create: Validate authority labels, stale state, accessibility, encoding, and command paths.)
  * Epic boundary: Bounded MCP and operator interfaces — Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.
  * Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-023 requires: Agent/UI convenience must not become an alternate provenance, policy, or promotion authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Render jobs, phases, attempts, progress, controls, provenance, findings, evidence, decisions, publications, health, and diagnostics without collapsing observed, inferred, proposed, approved, or published states.
  * Component dispositions: `ui/` (create: Host the optional operator client with generated API types and secure rendering.); `atlas/api/rest.py` (extend: Expose UI-required bounded status/evidence/review/publication endpoints only.); `docs/operations/operator-ui.md` (create: Document deployment, roles, workflows, status semantics, and incidents.); `tests/ui/` (create: Validate authority labels, stale state, accessibility, encoding, and command paths.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Design views for job/phase/attempt/work progress, controls, blockers/recovery, artifact/provenance graph, findings/evidence, review, publications, events, health, and diagnostics.
  * Use generated versioned API contracts and expected-version/idempotency for all commands; refresh and surface stale data before confirmation.
  * Label observed, derived, inferred, proposed, evidence, approved/rejected/held, attempted, verified published, unknown, and degraded states distinctly.
  * Provide accessible keyboard/navigation/status/error behavior and bounded pagination for large jobs.

  Security and safety requirements

  * Encode all artifact/plugin/model/error text and sanitize any rich rendering; prevent XSS, URL injection, unsafe downloads, and clickjacking.
  * Use CSRF/session/authz/TLS/content-security deployment controls where exposed; never store secrets in browser storage.
  * Do not expose raw files/paths/secrets by default; mediated downloads require policy and audit.
  * Display denied/stale/unknown/reconciliation states rather than optimistic success.

  Edge cases and outliers to handle

  * Status changes during review form.
  * Finding contains HTML/terminal escape/huge text.
  * Publication outcome is unknown.
  * API compatibility mismatch or partial outage.

  Acceptance criteria (“done” definition)

  * UI never labels a finding/proposal as evidence, a request as decision, or an attempt as verified publication.
  * All commands traverse canonical APIs and reject stale/replayed input.
  * Hostile rendered content cannot execute or create unauthorized navigation/actions.
  * Accessibility, large-job performance, partial outage, and compatibility behavior are tested.

  Testing plan

  * Authority-label golden tests.
  * XSS/URL/content rendering tests.
  * Stale/replay command E2E tests.
  * Accessibility automated/manual checks.
  * Large-job pagination/performance tests.
  * API mismatch/partial outage tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Authority-label golden tests., XSS/URL/content rendering tests., Stale/replay command E2E tests., Accessibility automated/manual checks., Large-job pagination/performance tests., API mismatch/partial outage tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T27.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: ui/, atlas/api/rest.py, docs/operations/operator-ui.md, tests/ui/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 108: Resolve tenant, authentication, authorization, and deployment-governance scope

  1.2 source task(s): `T27.1.4`
  Priority: `P3`
  Estimated effort: `14 hours`
  Dependencies: `T27.1.2, T27.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `docs/decisions/deployment-identity-and-tenancy.md (create); atlas/security/interfaces.py (create); atlas/config/security.py (create); tests/security/test_deployment_identity_adapters.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Determine from real deployment requirements whether ATLAS needs single-operator local identity, team RBAC, tenant isolation, service identities, or external policy adapters without burdening the compact core prematurely.
  * Restore or protect this invariant: Deployment identity/tenancy requirements, non-goals, and decision authority are evidenced and approved.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `docs/decisions/deployment-identity-and-tenancy.md` (create: Record users, tenants, trust zones, consequential actions, alternatives, and decision.); `atlas/security/interfaces.py` (create: Define optional actor/authentication/authorization/policy adapter contracts only after decision.); `atlas/config/security.py` (create: Represent deployment adapter selection and safe local defaults.); `tests/security/test_deployment_identity_adapters.py` (create: Validate selected policy and no-adapter local behavior.)
  * Epic boundary: Bounded MCP and operator interfaces — Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.
  * Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-023 requires: Agent/UI convenience must not become an alternate provenance, policy, or promotion authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Determine from real deployment requirements whether ATLAS needs single-operator local identity, team RBAC, tenant isolation, service identities, or external policy adapters without burdening the compact core prematurely.
  * Component dispositions: `docs/decisions/deployment-identity-and-tenancy.md` (create: Record users, tenants, trust zones, consequential actions, alternatives, and decision.); `atlas/security/interfaces.py` (create: Define optional actor/authentication/authorization/policy adapter contracts only after decision.); `atlas/config/security.py` (create: Represent deployment adapter selection and safe local defaults.); `tests/security/test_deployment_identity_adapters.py` (create: Validate selected policy and no-adapter local behavior.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Inventory deployment actors, service boundaries, data sensitivity, source/destination ownership, concurrent users, audit obligations, and tenant separation needs.
  * Classify actions: local harmless analysis, controls, plugin grants, review, publication, retention deletion, configuration, and administration.
  * Compare local OS identity, API gateway/IdP, RBAC/ABAC, tenant-scoped stores/content, and service identity adapters against requirements and cost.
  * Keep deterministic lifecycle/state/source/safety enforcement in core and define deployment auth/policy adapters only where justified.

  Security and safety requirements

  * Fail closed for consequential network-exposed operations when no required identity/policy adapter is configured.
  * Prevent tenant/job/source/content/publication cross-scope access and confused deputy behavior if multi-tenancy is selected.
  * Use external secret references, least privilege, revocation, audit, and break-glass policy with evidence.
  * Do not invent enterprise IAM requirements or claim isolation before tested deployment controls exist.

  Edge cases and outliers to handle

  * Single local user later migrates to team service.
  * One content identity is referenced by multiple tenants.
  * Service identity revoked during work.
  * Policy service unavailable or returns stale decision.

  Acceptance criteria (“done” definition)

  * Deployment identity/tenancy requirements, non-goals, and decision authority are evidenced and approved.
  * Selected adapters preserve core semantics and local mode remains safe and documented.
  * If multi-tenancy is required, isolation is modeled across state, content, events, caches, workers, diagnostics, and publications before implementation.
  * Auth/policy outage, revocation, and rollback behavior are deterministic and tested.

  Testing plan

  * Threat-model and requirement review.
  * Local no-adapter behavior tests.
  * Selected auth/policy adapter conformance tests.
  * Cross-scope/tenant negative tests if applicable.
  * Revocation/outage/stale-policy tests.
  * Migration/rollback decision drill.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Threat-model and requirement review., Local no-adapter behavior tests., Selected auth/policy adapter conformance tests., Cross-scope/tenant negative tests if applicable., Revocation/outage/stale-policy tests., Migration/rollback decision drill..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T27.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: docs/decisions/deployment-identity-and-tenancy.md, atlas/security/interfaces.py, atlas/config/security.py, tests/security/test_deployment_identity_adapters.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
