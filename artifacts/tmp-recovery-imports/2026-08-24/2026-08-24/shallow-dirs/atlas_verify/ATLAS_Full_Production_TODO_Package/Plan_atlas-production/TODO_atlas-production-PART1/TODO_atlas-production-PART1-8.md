@BinReaper Production TODOs

## TODO

* [ ] TODO 22: Implement bounded deterministic intake traversal

  1.2 source task(s): `T6.1.2`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T6.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/intake/service.py::IntakeGenerationBuilder (create); atlas/safety/filesystem_discovery.py (refactor); atlas/phases/reconnaissance.py (refactor)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Build a generation in `BUILDING`, enumerate source-relative occurrences in deterministic order, and persist every accepted, skipped, excluded, or failed observation under explicit budgets.
  * Restore or protect this invariant: Traversal order and accepted manifest input are deterministic for a stable source.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31.

  Where this applies

  * Primary affected components: `atlas/intake/service.py::IntakeGenerationBuilder` (create: Own generation construction and traversal.); `atlas/safety/filesystem_discovery.py` (refactor: Provide bounded observation primitives.); `atlas/phases/reconnaissance.py` (refactor: Delegate to IntakeGenerationBuilder.)
  * Epic boundary: Registered sources and immutable intake generations — Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Turn a complete BUILDING generation into an immutable ACCEPTED observation only after completeness, policy, and budget checks pass, with deterministic digest and explicit failure states.
  * Restore or protect this invariant: Only complete generations reach ACCEPTED.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31.

  Where this applies

  * Primary affected components: `atlas/intake/service.py::accept_generation` (create: Own acceptance and manifest hashing.); `atlas/persistence/repositories/intake.py` (create: Persist generation state and occurrence sets.); `atlas/events intake events` (extend: Record accepted/failed/blocked/superseded outcomes.)
  * Epic boundary: Registered sources and immutable intake generations — Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Remove independent source rediscovery from Fingerprinting and later stages so the accepted generation is the sole occurrence authority.
  * Restore or protect this invariant: Static/runtime guards find no unauthorized downstream source enumeration.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-005; REQ-003,REQ-014; PDF:p.6,p.12,p.16,p.31.

  Where this applies

  * Primary affected components: `atlas/phases/fingerprinting.py` (refactor: Read accepted occurrences rather than traverse live source.); `atlas/phases/structural_discovery.py` (refactor: Resolve content through occurrence/content records.); `atlas/phases/extraction.py and analysis.py` (refactor: Reject arbitrary source paths after intake.)
  * Epic boundary: Registered sources and immutable intake generations — Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
