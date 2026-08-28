@BinReaper Production TODOs

## TODO

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
