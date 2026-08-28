@BinReaper Production TODOs

## TODO

* [ ] TODO 40: Route every built-in filesystem operation through canonical access services

  1.2 source task(s): `T10.1.4`
  Priority: `P0`
  Estimated effort: `16 hours`
  Dependencies: `T10.1.2, T10.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/phases/* (refactor); atlas/safety/guardrails.py (create); tests/security/test_filesystem_authority.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Eliminate bypasses by integrating discovery, hashing, structure, extraction, analysis, and publication with SourceAccess, Workspace, and Destination services and enforcing static/runtime guards.
  * Restore or protect this invariant: Static analysis finds no unapproved direct filesystem authority in built-in phases.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-009; REQ-011; PDF:p.13,p.23.

  Where this applies

  * Primary affected components: `atlas/phases/*` (refactor: Replace direct source open/stat/walk/write paths.); `atlas/safety/guardrails.py` (create: Detect unapproved filesystem calls in built-in modules.); `tests/security/test_filesystem_authority.py` (create: Prove attribution and containment.)
  * Epic boundary: Canonical race-resistant source access — Route every source read through one registered-root, source-relative, capability-aware service that detects symlink, mount, case, Unicode, and TOCTOU hazards.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create unique per-job/phase/attempt workspaces outside source roots with restrictive permissions, quotas, ownership metadata, cleanup states, and crash reconciliation.
  * Restore or protect this invariant: No Phase-D or analyzer write occurs under any registered source root.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25.

  Where this applies

  * Primary affected components: `atlas/artifacts/workspace.py::WorkspaceManager` (create: Own create/open/account/seal/cleanup workspace lifecycle.); `workspaces migration` (create: Persist workspace identity, root, quota, status, and ownership.); `atlas/core/runtime.py` (extend: Inject one WorkspaceManager into phases/backends.)
  * Epic boundary: Quarantine, recursive archive budgets, and controlled materialization — Inspect containers before extraction, contain every side effect in attempt-owned workspaces, and enforce cumulative recursive resource limits.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Traverse nested containers without materializing them when feasible, using a bounded work queue and cumulative limits for depth, members, declared/actual bytes, ratio, temp use, and time.
  * Restore or protect this invariant: All adversarial containers terminate within configured CPU/time/byte/member/depth bounds.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-010; REQ-009,REQ-010,REQ-012; PDF:p.7,p.13,p.23,p.25.

  Where this applies

  * Primary affected components: `atlas/safety/archive_safety.py::ArchiveBudgetController` (create: Own cumulative resource counters and decisions.); `atlas/phases/structural_discovery.py` (refactor: Inspect nested containers through bounded queue.); `atlas/artifacts/structural_inspection.py` (create: Normalize member metadata and nested relationships.)
  * Epic boundary: Quarantine, recursive archive budgets, and controlled materialization — Inspect containers before extraction, contain every side effect in attempt-owned workspaces, and enforce cumulative recursive resource limits.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
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
