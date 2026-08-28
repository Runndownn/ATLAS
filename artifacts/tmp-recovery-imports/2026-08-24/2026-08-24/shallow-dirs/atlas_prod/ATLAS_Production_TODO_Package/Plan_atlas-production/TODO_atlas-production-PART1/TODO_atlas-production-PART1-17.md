@BinReaper Production TODOs

## TODO

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
