@BinReaper Production TODOs

## TODO

* [ ] TODO 46: Implement staged, verified, no-replace local CAS writes

  1.2 source task(s): `T12.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T12.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/local_store.py::LocalContentStore (create); atlas/artifacts/store_paths.py (create); atlas/artifacts/identity.py (extend)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Store bytes at digest-derived immutable locations using one-pass hash/copy, exclusive staging, verification, fsync policy, and collision-safe finalization.
  * Restore or protect this invariant: Repeated identical bytes consume one verified blob payload.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28.

  Where this applies

  * Primary affected components: `atlas/artifacts/local_store.py::LocalContentStore` (create: Implement local immutable blob storage.); `atlas/artifacts/store_paths.py` (create: Derive safe digest paths and staging roots.); `atlas/artifacts/identity.py` (extend: Tee verified reads into the content store.)
  * Epic boundary: Optional immutable local content store — Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Link retained blobs to content identities, occurrences/capture attempts, retention classes, references, verification history, and capacity accounting.
  * Restore or protect this invariant: Every committed blob has verifiable identity, provider, provenance, and retention status.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28.

  Where this applies

  * Primary affected components: `atlas/persistence/repositories/blobs.py` (create: Persist blob/provider/reference/integrity records.); `atlas/artifacts/store.py::ContentCaptureService` (create: Coordinate identity read and retention result.); `atlas/status/projection.py` (extend: Expose managed-byte and replayability status.)
  * Epic boundary: Optional immutable local content store — Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Detect filesystem/DB divergence, corruption, abandoned staging, and unreferenced blobs without deleting uncertain data or blocking normal identity-only operation.
  * Restore or protect this invariant: Reconciliation classifies every observed divergence with deterministic next action.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-011; REQ-005,REQ-026,REQ-029; PDF:p.19,p.23,p.24,p.28.

  Where this applies

  * Primary affected components: `atlas/artifacts/reconcile.py::ContentStoreReconciler` (create: Scan and classify blob/store divergence.); `atlas/cli.py::content verify/reconcile` (extend: Provide dry-run and controlled repair commands.); `docs/operations/content-store-recovery.md` (create: Document integrity incident and rollback handling.)
  * Epic boundary: Optional immutable local content store — Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
