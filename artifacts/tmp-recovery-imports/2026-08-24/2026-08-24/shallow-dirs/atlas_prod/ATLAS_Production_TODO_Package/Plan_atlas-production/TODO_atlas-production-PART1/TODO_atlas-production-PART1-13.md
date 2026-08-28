@BinReaper Production TODOs

## TODO

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
