@BinReaper Production TODOs

## TODO

* [ ] TODO 25: Define `ContentIdentity` and occurrence-to-content link contracts

  1.2 source task(s): `T7.1.1`
  Priority: `P0`
  Estimated effort: `12 hours`
  Dependencies: `T6.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/models.py::ContentIdentity (create); atlas/artifacts/models.py::OccurrenceContentLink (create); content_identities and occurrence_content_links migrations (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create immutable canonical content IDs and explicit observation links without implying that a retained blob exists.
  * Restore or protect this invariant: Identical bytes converge on one persistent SHA-256 identity across processes.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/models.py::ContentIdentity` (create: Represent algorithm, digest, size, and verification metadata.); `atlas/artifacts/models.py::OccurrenceContentLink` (create: Bind an occurrence read to exact content and read evidence.); `content_identities and occurrence_content_links migrations` (create: Persist cross-run identity.)
  * Epic boundary: Persistent content identity and occurrence linkage — Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Open each accepted regular-file occurrence through the canonical access boundary, verify handle metadata, stream bytes, and recheck mutation before attaching content identity.
  * Restore or protect this invariant: Stable inputs produce the expected SHA-256 and link evidence.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/identity.py::ContentIdentityService` (create: Own hashing and identity persistence.); `atlas/storage/hash_store.py::HashStore` (refactor: Delegate hashing while preserving facade behavior.); `atlas/phases/fingerprinting.py` (refactor: Use occurrence IDs and identity service.)
  * Epic boundary: Persistent content identity and occurrence linkage — Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Use content identity to recognize prior bytes while retaining occurrence provenance and deciding explicitly whether downstream work is eligible for reuse.
  * Restore or protect this invariant: A restart recognizes previously seen content without recomputing downstream identity state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-006; REQ-004,REQ-005; PDF:p.6,p.8,p.12,p.16,p.23,p.28,p.31.

  Where this applies

  * Primary affected components: `atlas/artifacts/identity.py::lookup_content` (extend: Query persistent identities and occurrence history.); `atlas/persistence/repositories/content.py` (create: Provide indexed identity and link queries.); `atlas/phases/fingerprinting.py result contract` (extend: Report new, known, stale, and capture status.)
  * Epic boundary: Persistent content identity and occurrence linkage — Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
