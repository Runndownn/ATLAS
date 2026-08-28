@BinReaper Production TODOs

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
