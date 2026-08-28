@BinReaper Production TODOs

## TODO

* [ ] TODO 115: Create the adversarial filesystem and source-mutation corpus

  1.2 source task(s): `T29.1.1`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.2, T28.1.3, T6.1.4, T10.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/fixtures/filesystems/ (create); tests/fixtures/source_mutation/ (create); tests/fixtures/fixture.schema.json (create); tests/generators/filesystem_cases.py (create); docs/testing/filesystem-corpus.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create a governed synthetic corpus that exercises path, identity, traversal, mutation, and resource limits across supported filesystems.
  * Restore or protect this invariant: Every fixture has known provenance, bounded generation, an exact oracle, and no ability to escape the disposable test root.
  * Source lineage: Expansion of T6.1.2-T6.1.4, T10.1.1-T10.1.4, and deep-review Filesystem Security; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/fixtures/filesystems/` (create: Store tiny static filesystem fixtures and metadata manifests.); `tests/fixtures/source_mutation/` (create: Define barrier-driven source mutation scenarios.); `tests/fixtures/fixture.schema.json` (create: Version provenance, bounds, oracle, sensitivity, and cleanup fields.); `tests/generators/filesystem_cases.py` (create: Generate large/bounded trees and platform-specific cases deterministically.); `docs/testing/filesystem-corpus.md` (create: Document corpus governance, native requirements, and expected outcomes.)
  * Epic boundary: E29 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/fixtures/filesystems/` (create: Store tiny static filesystem fixtures and metadata manifests.); `tests/fixtures/source_mutation/` (create: Define barrier-driven source mutation scenarios.); `tests/fixtures/fixture.schema.json` (create: Version provenance, bounds, oracle, sensitivity, and cleanup fields.); `tests/generators/filesystem_cases.py` (create: Generate large/bounded trees and platform-specific cases deterministically.); `docs/testing/filesystem-corpus.md` (create: Document corpus governance, native requirements, and expected outcomes.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Separate tiny checked-in fixtures from deterministic generators for high-count, long-name, sparse, and mutation workloads.
  * Model occurrence identity independently from content identity so renames and duplicate bytes have explicit expected results.
  * Drive mutation at named barriers—before open, after stat, during hash, before extraction, and after checkpoint—rather than probabilistic racing.
  * Tag each case with native-platform requirements and never let emulated cases satisfy native support.

  Implementation requirements

  * Define fixture metadata for generator/version/seed, expected entries, content digests, link/mount topology, platform constraints, resource cap, oracle, license/provenance, and cleanup.
  * Create cases for symlink loops, hard links, junctions/reparse points, bind mounts, special files, permission changes, case/Unicode collisions, long/reserved names, sparse files, and disappearing roots.
  * Create source mutation cases for replace, truncate, append, chmod, rename, delete, link swap, root swap, mount swap, inode/file-ID reuse, and concurrent readers.
  * Provide bounded tree generators for thousands to millions of entries without committing generated output.
  * Assert exact discovery anomalies, accepted occurrences, content identities, blocked operations, progress/checkpoint behavior, and no out-of-root reads/writes.

  Security and safety requirements

  * Use only synthetic bytes and disposable roots; no host filesystem enumeration beyond declared probes.
  * Reject fixture paths containing uncontrolled absolute locations or links outside the lab root.
  * Cap entry counts, path lengths, generated bytes, open descriptors, and runtime before materialization.
  * Scan manifests and retained samples for local paths, usernames, secrets, and personal data.
  * Require teardown to verify mounts, links, processes, and generated trees are removed.

  Edge cases and outliers to handle

  * A platform cannot create symlinks, junctions, special files, or mount variants without privilege.
  * Unicode/case collisions prevent both fixtures from coexisting on one filesystem.
  * Large-tree generation hits inode limits before intended count.
  * Mutation races complete earlier or later than the named barrier.
  * Cleanup encounters read-only, locked, or externally replaced paths.

  Acceptance criteria (“done” definition)

  * Every fixture validates against the schema and records generator, seed, bounds, native requirements, exact oracle, and provenance.
  * All static cases remain small; all scale cases are reproducibly generated and deleted.
  * Source mutations either produce verified exact-byte identity or a stable blocked/stale outcome—never silent acceptance of changed bytes.
  * No corpus case reads or writes outside the lab root, leaves mounts/processes behind, or contains uncontrolled sensitive data.

  Testing plan

  * Fixture-schema and provenance validation tests.
  * Generator determinism and bound-enforcement tests.
  * Symlink/hard-link/junction/mount/special-file adversarial tests.
  * Case/Unicode/long/reserved-name platform tests.
  * Barrier-driven mutation and occurrence/content-identity tests.
  * Large-tree progress/checkpoint/resource tests.
  * Cleanup and secret/path-leak scans.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until corpus runner and approved platform lanes exist`; execute through T28.1.1 with native requirements enforced.
  * Expected evidence: schema, deterministic generation, path/link/mutation oracles, resource bounds, and cleanup/security scans pass.
  * Completion record: corpus schema/version, fixture and generator digests, seeds, lane manifests, commands, outcomes, minimizations, cleanup, and hashes.

  Debugging checklist

  * Validate fixture metadata, native capability requirements, and generator seed before product behavior.
  * Capture barrier position, accepted occurrence identity, pre/post handle identity, and content digest.
  * Minimize failures to the fewest entries and one mutation.
  * Inspect cleanup from outside the tested source tree and retain only sanitized evidence.

* [ ] TODO 116: Create the recursive archive and container-abuse corpus

  1.2 source task(s): `T29.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.2, T28.1.3, T11.1.4, T13.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/fixtures/archives/ (create); tests/generators/archive_cases.py (create); tests/archive/test_adversarial_corpus.py (create); docs/testing/archive-corpus.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create a safe corpus that proves archive inspection and controlled materialization against traversal, link, ambiguity, malformation, and exhaustion.
  * Restore or protect this invariant: No archive member is materialized unless it belongs to the exact accepted structural report and remains within cumulative job budgets.
  * Source lineage: Expansion of T11.1.1-T11.1.4, T13.1.1-T13.1.4, and deep-review Archive Security; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/fixtures/archives/` (create: Store tiny static malformed and edge-case archive fixtures plus manifests.); `tests/generators/archive_cases.py` (create: Generate bounded nested, high-ratio, member-flood, and sparse cases.); `tests/archive/test_adversarial_corpus.py` (create: Assert structural inspection, budgets, report binding, and materialization outcomes.); `docs/testing/archive-corpus.md` (create: Document safe generation, limits, oracles, and unsupported formats.)
  * Epic boundary: E29 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/fixtures/archives/` (create: Store tiny static malformed and edge-case archive fixtures plus manifests.); `tests/generators/archive_cases.py` (create: Generate bounded nested, high-ratio, member-flood, and sparse cases.); `tests/archive/test_adversarial_corpus.py` (create: Assert structural inspection, budgets, report binding, and materialization outcomes.); `docs/testing/archive-corpus.md` (create: Document safe generation, limits, oracles, and unsupported formats.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Use tiny static malformed fixtures plus deterministic generators; never store real decompression bombs.
  * Represent nested containers as cumulative work under one job budget, not independent per-level limits.
  * Bind every extraction oracle to input content identity, inspector version, policy/config digest, structural report digest, and destination workspace.
  * Treat encrypted, unsupported, ambiguous, and platform-conflicting members as explicit blocked/skipped outcomes.

  Implementation requirements

  * Create cases for relative/absolute traversal, mixed separators, symlink/hard-link members, devices/FIFOs, duplicate/conflicting names, Unicode/case collisions, sparse files, invalid sizes, truncated headers, malformed central directories, and unsupported methods.
  * Generate bounded high compression ratio, member-count flood, deep nesting, repeated names, large metadata, and recursive mixed ZIP/TAR cases using declared ceilings.
  * Assert inspection without materialization, cumulative budget accounting, deterministic report ordering/digests, exact member allowlists, and quarantine-only output.
  * Verify extracted output manifests, parent/child identities, derivation edges, partial-failure cleanup, and stale-report rejection.
  * Record library/tool versions and platform-specific parser differences in fixture results.

  Security and safety requirements

  * Generators enforce hard compressed/uncompressed/member/depth/time/output limits below host danger thresholds.
  * Run all archive cases in disposable quarantine with no source-adjacent writes.
  * Reject absolute, parent, device, link, ambiguous, or colliding output paths before file creation.
  * Do not execute active content or invoke external viewers/tools unless separately isolated and authorized.
  * Scan retained output for path escape, special files, excessive allocation, and synthetic secret leakage.

  Edge cases and outliers to handle

  * Parser libraries disagree about duplicate names or malformed size fields.
  * A sparse member consumes logical bytes without equivalent physical allocation.
  * Nested archives change format or encryption state at each level.
  * Case/Unicode collisions differ by destination filesystem.
  * Disk exhaustion or process kill occurs after some members are staged.

  Acceptance criteria (“done” definition)

  * Every case has exact structural, budget, policy, and materialization oracles and remains within safe generator limits.
  * Traversal, links, devices, collisions, malformed metadata, and cumulative budget violations produce stable blocked results before unsafe output.
  * Successful materialization matches the exact structural report and persists complete output/derivation manifests.
  * Interrupted extraction leaves no trusted partial output and is deterministically reconcilable.

  Testing plan

  * Fixture-schema and generator-bound tests.
  * ZIP/TAR traversal and absolute-path tests.
  * Link/device/FIFO/special-member tests.
  * Malformed/truncated/duplicate/collision parser tests.
  * Nested depth/member/ratio/byte/time budget tests.
  * Stale-report and exact-allowlist binding tests.
  * Partial extraction, disk-full, crash, cleanup, and lineage tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until archive corpus runner and approved lanes exist`; run through the lab under outer quotas.
  * Expected evidence: all structural, budget, materialization, lineage, crash, cleanup, and security oracles pass without unsafe skips.
  * Completion record: corpus/generator versions and seeds, library/platform versions, commands, reports/manifests, resource peaks, minimized failures, cleanup, hashes.

  Debugging checklist

  * Inspect archive identity, parser version, policy/config digest, cumulative budget ledger, and report digest first.
  * Compare raw member metadata to normalized member identity and rejection reason.
  * Minimize nested or malformed cases while preserving the failing parser behavior.
  * Verify quarantine/output trees externally after interruption and preserve only bounded synthetic artifacts.

* [ ] TODO 117: Create the hostile plugin, analyzer, and backend corpus

  1.2 source task(s): `T29.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.4, T14.1.4, T15.1.4, T22.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/fixtures/plugins/ (create); tests/execution/hostile_plugins/ (create); tests/execution/test_hostile_plugin_matrix.py (create); docs/testing/hostile-plugin-corpus.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create a maintained inert corpus that tests plugin descriptors, capability policy, isolation, result validation, failure mapping, and cleanup.
  * Restore or protect this invariant: Plugins can propose typed results only; they cannot self-authorize capabilities, mutate lifecycle state, or survive beyond their attempt.
  * Source lineage: Expansion of T14.1.1-T14.1.4, T15.1.1-T15.1.4, T22.1.1-T22.1.4; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/fixtures/plugins/` (create: Store benign and inert hostile plugin packages with descriptors and expected outcomes.); `tests/execution/hostile_plugins/` (create: Implement bounded crash, hang, capability, protocol, and resource behaviors.); `tests/execution/test_hostile_plugin_matrix.py` (create: Run the common corpus against every approved backend/trust tier.); `docs/testing/hostile-plugin-corpus.md` (create: Document fixture safety, capabilities, limits, and oracles.)
  * Epic boundary: E29 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/fixtures/plugins/` (create: Store benign and inert hostile plugin packages with descriptors and expected outcomes.); `tests/execution/hostile_plugins/` (create: Implement bounded crash, hang, capability, protocol, and resource behaviors.); `tests/execution/test_hostile_plugin_matrix.py` (create: Run the common corpus against every approved backend/trust tier.); `docs/testing/hostile-plugin-corpus.md` (create: Document fixture safety, capabilities, limits, and oracles.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Include benign reference plugins for semantic comparison and one bounded hostile behavior per declared threat.
  * Separate requested capabilities from policy grants and actual backend enforcement.
  * Use the same immutable WorkSpec and result schema across in-process, subprocess, container, and future remote backends.
  * Make every hostile action inert and observable; do not include destructive payloads or real credential access.

  Implementation requirements

  * Create descriptor/version compatibility cases plus plugins that crash, hang, spawn descendants, flood output, exhaust bounded resources, return malformed/oversized/forged results, reuse IDs, and submit stale results.
  * Create capability probes for source writes, undeclared reads, workspace escape, network access, environment/secret discovery, external tool execution, and StateStore access.
  * Add checkpoint/result partial-write, cancellation race, timeout escalation, protocol truncation, encoding, and child-survival cases.
  * Run trusted benign plugins in all applicable backends and compare normalized findings, evidence, resource accounting, and failure taxonomy.
  * Persist fixture digests, declared/requested/granted controls, backend facts, and exact observed denial/cleanup evidence.

  Security and safety requirements

  * Fixtures use synthetic marker secrets, fake endpoints, disposable workspaces, and inert descendant processes.
  * Apply outer PID/memory/disk/output/time/network ceilings independent of plugin-controlled limits.
  * Never expose CI cloud credentials, signing material, home directories, container sockets, or production StateStore.
  * Reject forged job/phase/attempt/content/config/policy IDs before authoritative commit.
  * Quarantine any runner with surviving processes, mounts, sockets, or writable host changes.

  Edge cases and outliers to handle

  * Plugin crashes after side-effect-like local output but before result submission.
  * Malformed protocol consumes excessive parser memory or logs.
  * Child detaches from process group or ignores graceful termination.
  * Trusted and isolated backends differ in ordering or floating metadata.
  * Platform lacks a required enforcement control.

  Acceptance criteria (“done” definition)

  * Every plugin threat and failure class has an inert bounded fixture, declared capabilities, exact expected result, and cleanup oracle.
  * Hostile plugins cannot access undeclared resources, forge authoritative identity, or leave surviving authority under claimed controls.
  * Benign plugins produce semantically equivalent normalized results across supported backends.
  * Unsupported enforcement causes policy denial or explicit reduced assurance, never silent unrestricted execution.

  Testing plan

  * Descriptor/schema/version compatibility tests.
  * Capability request/grant/denial tests.
  * Crash/hang/cancel/timeout/descendant tests.
  * Output/protocol/result forgery and size-limit tests.
  * Filesystem/network/environment/secret/tool access tests.
  * Backend semantic differential and resource-accounting tests.
  * External cleanup and runner-quarantine tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until hostile corpus and backend runner exist`; execute through isolated T28.1.4 lanes.
  * Expected evidence: descriptor, capability, failure, protocol, semantic-equivalence, resource, and cleanup gates pass for every supported backend.
  * Completion record: fixture/package digests, descriptors/grants, backend/lane manifests, commands, normalized results, denial and cleanup evidence, hashes.

  Debugging checklist

  * Identify fixture behavior, descriptor, requested/granted capabilities, backend, and lane controls first.
  * Capture bounded process tree, resource counters, protocol frames, workspace diff, and policy decision.
  * Reproduce one hostile behavior with the smallest WorkSpec and limit.
  * Validate authoritative identity/result binding before investigating plugin internals.
