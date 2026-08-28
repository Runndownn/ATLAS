@BinReaper Production TODOs

## TODO

* [ ] TODO 109: Build the hermetic test-laboratory controller and environment manifest

  1.2 source task(s): `T28.1.1`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T1.1.1, T24.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/lab/controller.py (create); tests/lab/environment.schema.json (create); tests/lab/environments/ (create); scripts/run_test_lab.py (create); docs/testing/test-laboratory.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create one hermetic controller that can provision, identify, run, tear down, and attest every native or emulated verification environment.
  * Restore or protect this invariant: Every result is bound to an immutable environment manifest and disposable workspace; unknown or partial provisioning fails closed.
  * Source lineage: Expansion of T24.1.1/T24.1.2 and deep-review Stage 16; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/lab/controller.py` (create: Own deterministic lane planning, provisioning, teardown, and evidence collection.); `tests/lab/environment.schema.json` (create: Version OS, runtime, filesystem, service, isolation, and assurance facts.); `tests/lab/environments/` (create: Store declarative native and emulated lane definitions.); `scripts/run_test_lab.py` (create: Expose one dry-run/list/run/collect interface after repository command discovery.); `docs/testing/test-laboratory.md` (create: Document assurance levels, prerequisites, cleanup, and evidence.)
  * Epic boundary: E28 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/lab/controller.py` (create: Own deterministic lane planning, provisioning, teardown, and evidence collection.); `tests/lab/environment.schema.json` (create: Version OS, runtime, filesystem, service, isolation, and assurance facts.); `tests/lab/environments/` (create: Store declarative native and emulated lane definitions.); `scripts/run_test_lab.py` (create: Expose one dry-run/list/run/collect interface after repository command discovery.); `docs/testing/test-laboratory.md` (create: Document assurance levels, prerequisites, cleanup, and evidence.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Use declarative lane manifests and a replaceable controller; the manifests and results are evidence, not lifecycle authority.
  * Classify lanes as native-supported, native-reduced-assurance, emulated, or informational; only native-supported lanes establish support.
  * Bind every run to repository ref, dirty state, OS/kernel/runtime/filesystem/service versions, capability probes, fixture catalog, and test selection.
  * Keep all laboratory code outside the production composition root and public runtime API.

  Implementation requirements

  * Define schema-versioned lane manifests with prerequisites, capability probes, resource ceilings, network policy, fixture mounts, and teardown assertions.
  * Implement deterministic list, validate, plan, run, collect, and clean operations with dry-run default, lock files, and root containment.
  * Emit per-run evidence manifests containing exact commands, exit codes, durations, resource peaks, skips, artifacts, and hashes.
  * Reject symlink roots, unapproved mounts, missing mandatory controls, stale manifests, concurrent conflicts, and failed teardown.
  * Provide adapters for local runs, GitHub Actions, container runtimes, and future dedicated runners without changing test semantics.

  Security and safety requirements

  * Use synthetic credentials, loopback-only services, read-only source mounts where possible, and no cloud or release secrets.
  * Allowlist host mounts, devices, endpoints, environment variables, and retained artifact classes.
  * Redact local usernames, absolute workstation paths, tokens, and unneeded raw input from shared evidence.
  * Fail and quarantine on leaked processes, mounts, listeners, writable source changes, or incomplete cleanup.
  * Hash environment and result manifests; never accept a hand-edited summary as sole completion evidence.

  Edge cases and outliers to handle

  * A runner lacks virtualization, namespaces, filesystem controls, or privileges declared by a lane.
  * Provisioning fails after creating a subset of services, mounts, ports, or volumes.
  * Concurrent runs target the same root, service name, or port range.
  * A test fills the evidence volume or terminates the controller.
  * Native and emulated lanes share a platform label but expose different semantics.

  Acceptance criteria (“done” definition)

  * Two unchanged plans and runs produce byte-identical normalized manifests and the same lane/test selection.
  * Every result resolves to repository ref, environment digest, fixture digest, exact command, exit status, and artifact hashes.
  * Missing controls, path escape, symlink roots, lock conflicts, and cleanup leaks fail closed with typed diagnostics.
  * No production runtime module imports the laboratory controller or lane definitions.

  Testing plan

  * Environment-schema validation and compatibility tests.
  * Dry-run determinism and lane-selection property tests.
  * Path containment, symlink, mount, and concurrent-lock negative tests.
  * Partial-provision and controller-crash cleanup tests.
  * Synthetic-secret redaction and evidence-integrity tests.
  * Local/CI adapter conformance tests.
  * One approved native-lane smoke run after T24.1.1 resolves support.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 and T24.1.1 establish repository-native commands and approved lane IDs`; retain resolved commands and cwd.
  * Expected evidence: schema, determinism, containment, cleanup, redaction, adapter, and native-smoke gates pass with no unapproved skip.
  * Completion record: commit/dirty state, controller/schema versions, lane manifests, commands/results, resource and cleanup report, coverage limitations, hashes, and review.

  Debugging checklist

  * Validate the lane manifest and capability-probe output before product failures.
  * Compare requested lane, resolved lane, actual platform facts, and assurance classification.
  * Inspect lock, mount, process, port, temp-volume, and evidence state after interruption.
  * Reproduce in the smallest native lane with one fixture and preserve normalized diagnostics.

* [ ] TODO 110: Emulate Linux filesystem, storage, and kernel-control variants

  1.2 source task(s): `T28.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.1, T10.1.4, T24.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/lab/environments/linux/ (create); tests/platform/linux/ (create); .github/workflows/platform-linux.yml (create); docs/testing/linux-assurance.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Exercise source access, workspaces, persistence, subprocess controls, and cleanup against materially different Linux semantics.
  * Restore or protect this invariant: Filesystem and kernel-control claims are accepted only for exact native lanes; emulation cannot stand in for durability or isolation.
  * Source lineage: Expansion of T10.1.1-T10.1.4, T22.1.2-T22.1.4, and T24.1.1; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/lab/environments/linux/` (create: Define native and emulated Linux filesystem/kernel lanes.); `tests/platform/linux/` (create: Host link, mount, atomicity, durability, special-file, and resource-control tests.); `.github/workflows/platform-linux.yml` (create: Run approved shared and self-hosted Linux lanes.); `docs/testing/linux-assurance.md` (create: Publish exact native/emulated control coverage and gaps.)
  * Epic boundary: E28 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/lab/environments/linux/` (create: Define native and emulated Linux filesystem/kernel lanes.); `tests/platform/linux/` (create: Host link, mount, atomicity, durability, special-file, and resource-control tests.); `.github/workflows/platform-linux.yml` (create: Run approved shared and self-hosted Linux lanes.); `docs/testing/linux-assurance.md` (create: Publish exact native/emulated control coverage and gaps.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Prioritize native ext4 plus one second local filesystem; treat tmpfs, overlay, FUSE, and network filesystems as explicit variants.
  * Probe descriptor-relative/no-follow access, inode/device identity, links, mounts, atomic rename/no-replace, fsync, sparse files, quotas, cgroups, namespaces, and process cleanup.
  * Separate ordinary shared CI from privileged or self-hosted lanes and publish reduced assurance where controls cannot run safely.
  * Generate bounded datasets at runtime rather than checking large or explosive files into source control.

  Implementation requirements

  * Define lane manifests for ext4, second local FS, tmpfs, overlay/container, read-only, cross-device, low-byte, and low-inode cases.
  * Implement tests for symlinks, hard links, bind mounts, root replacement, inode reuse, special files, permissions, rename/no-replace, and fsync behavior.
  * Exercise cgroups v2 CPU/memory/PID controls, namespaces, signal delivery, descendant cleanup, and resource accounting where supported.
  * Record kernel, architecture, filesystem, mount options, container runtime, and capability probes in each result.
  * Measure filesystem-specific lock, traversal, cleanup, and durability costs without changing semantic expectations.

  Security and safety requirements

  * Never mount host root, container sockets, production volumes, or arbitrary devices.
  * Use unprivileged/rootless mechanisms where feasible and isolate privileged lanes on disposable runners.
  * Reject device nodes, FIFOs, sockets, setuid/capability bits, unexpected ownership, and out-of-root output.
  * Assert no surviving process or mount after teardown and scan retained output for synthetic secret/path leakage.

  Edge cases and outliers to handle

  * Rename is atomic but not durable without parent-directory fsync.
  * Overlay changes inode or mount semantics relative to the host filesystem.
  * Runner kernels expose but do not delegate cgroup or namespace controls.
  * Inode exhaustion occurs while byte capacity remains.
  * Hard links or bind mounts make different paths reference the same object.

  Acceptance criteria (“done” definition)

  * Every approved lane emits a capability/assurance matrix tied to exact kernel, filesystem, mount, and runner facts.
  * Source access, workspace, extraction, content-store, SQLite, resource-control, and cleanup contracts pass in supported lanes.
  * Unsupported or emulated controls remain visible and cannot satisfy native release gates.
  * Privileged lanes leave no mount, process, elevated file, or source-tree modification.

  Testing plan

  * Capability-probe unit tests.
  * Symlink, hard-link, bind-mount, root-replacement, inode-reuse, and special-file tests.
  * Atomic rename/no-replace/fsync crash tests.
  * Low-byte, low-inode, read-only, cross-device, and permission-failure tests.
  * cgroup CPU/memory/PID and process-tree termination tests.
  * Overlay/tmpfs/native differential tests.
  * Teardown and evidence-integrity tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until approved Linux lane manifests and repository-native commands exist`; execute through the test-lab controller.
  * Expected evidence: probes, all supported-lane conformance, resource/durability faults, differentials, and teardown assertions pass.
  * Completion record: kernel/filesystem/mount/container versions, lane digests, commands, results, native/emulated class, skips, resources, cleanup, and hashes.

  Debugging checklist

  * Capture mount table, filesystem/options, namespace/cgroup probes, identity, umask, and assurance class.
  * Reproduce outside overlay/container when inode, mount, or durability behavior is ambiguous.
  * Inspect descriptors, processes, mounts, quotas, and source/workspace diffs after failure.
  * Preserve the smallest generated fixture and allowed system-call diagnostics.

* [ ] TODO 111: Emulate Windows and macOS path and process semantics

  1.2 source task(s): `T28.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.1, T10.1.4, T22.1.2, T24.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/lab/environments/windows/ (create); tests/lab/environments/macos/ (create); tests/platform/windows/ (create); tests/platform/macos/ (create); docs/testing/cross-platform-assurance.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prove path, archive, workspace, subprocess, and cleanup safety under Windows and macOS rather than assuming POSIX equivalence.
  * Restore or protect this invariant: Containment and identity do not depend on string-only POSIX assumptions; platform gaps remain explicit and fail closed.
  * Source lineage: Expansion of T10.1.1, T10.1.3, T22.1.2-T22.1.4, and A3/T24.1.1; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/lab/environments/windows/` (create: Define native Windows filesystem and Job Object lanes.); `tests/lab/environments/macos/` (create: Define native APFS and process-control lanes.); `tests/platform/windows/` (create: Test path, reparse, case, lock, rename, and process semantics.); `tests/platform/macos/` (create: Test Unicode, APFS case modes, links, locks, and process cleanup.); `docs/testing/cross-platform-assurance.md` (create: Publish equivalence, reduced assurance, and gaps.)
  * Epic boundary: E28 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/lab/environments/windows/` (create: Define native Windows filesystem and Job Object lanes.); `tests/lab/environments/macos/` (create: Define native APFS and process-control lanes.); `tests/platform/windows/` (create: Test path, reparse, case, lock, rename, and process semantics.); `tests/platform/macos/` (create: Test Unicode, APFS case modes, links, locks, and process cleanup.); `docs/testing/cross-platform-assurance.md` (create: Publish equivalence, reduced assurance, and gaps.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Use native Windows/macOS runners for support claims; parser emulation cannot prove reparse, APFS, lock, or process behavior.
  * Normalize policy at the ATLAS boundary while preserving native handles and identity evidence.
  * Cover Windows drive/UNC/device namespaces, reserved names, ADS, junctions/reparse, case folding, long paths, sharing modes, and Job Objects.
  * Cover APFS case variants, Unicode normalization, symlinks, metadata, locks, rename, and process-group cleanup.
  * Classify unavailable controls as reduced assurance rather than silently weakening policy.

  Implementation requirements

  * Define native lane manifests and probes for approved OS versions, filesystem/case modes, and privilege-dependent link controls.
  * Create path vectors for separators, drive-relative/UNC/extended forms, devices, reserved/trailing characters, Unicode, case collisions, and invalid bytes.
  * Exercise strongest platform-safe handle access, link/root replacement, no-replace destination, file sharing/locking, temp permissions, and cleanup.
  * Verify timeout, descendant termination, signal/control handling, environment inheritance, and resource-control assurance.
  * Compare normalized lifecycle/evidence results while retaining platform-specific diagnostic fields.

  Security and safety requirements

  * Use disposable users/workspaces and synthetic loopback shares; never access enterprise shares, profiles, keychains, or credential stores.
  * Reject device paths, reserved names, ADS output, reparse escape, and case/Unicode collisions by explicit policy.
  * Do not globally enable elevated symlink privileges, developer mode, sandbox exceptions, or full-disk access on shared runners.
  * Prevent subprocess fixtures from reaching histories, keychains, browser stores, cloud metadata, or CI secrets.
  * Sanitize account names and native absolute paths from retained evidence.

  Edge cases and outliers to handle

  * Case-insensitive lookup resolves different casing than the accepted manifest.
  * NFC/NFD names collide across platforms or archive extraction.
  * Windows sharing modes block rename/delete while handles remain open.
  * Junction/reparse targets change after validation.
  * APFS runner case mode differs from developer volumes.

  Acceptance criteria (“done” definition)

  * Every claimed control has native evidence bound to exact OS, filesystem mode, privilege state, and probes.
  * Path corpus, mutation, extraction, workspace, SQLite locking, and process cleanup preserve expected lifecycle outcomes.
  * Reserved/device/ADS/reparse/Unicode/case-collision inputs fail with stable reasons and no out-of-root effect.
  * Reduced-assurance controls are observable and cannot satisfy stronger support claims.

  Testing plan

  * Canonical path-vector unit/property tests.
  * Native junction/reparse/symlink/root-swap tests.
  * Case-folding and Unicode-normalization collision tests.
  * UNC/long-path/reserved-name/ADS negative tests.
  * File-sharing, locking, rename, temp-permission, and cleanup tests.
  * Job Object/process-group timeout and descendant termination tests.
  * Cross-platform normalized-result differential tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T24.1.1 approves native versions and T1.1.1 records commands`; use identified native lanes.
  * Expected evidence: path vectors, link/root races, filesystem operations, process cleanup, differentials, and assurance-policy tests pass.
  * Completion record: OS/filesystem/case/privilege probes, lane and fixture digests, commands, raw results, reduced-assurance declarations, cleanup, and hashes.

  Debugging checklist

  * Capture native path, normalized ATLAS path, resolved handle identity, case mode, and reparse/link metadata.
  * Reproduce collisions on a minimal matching temporary volume/share.
  * Inspect open handles/process trees and sharing violations before cleanup retries.
  * Compare native and normalized event/error records to find policy drift.
