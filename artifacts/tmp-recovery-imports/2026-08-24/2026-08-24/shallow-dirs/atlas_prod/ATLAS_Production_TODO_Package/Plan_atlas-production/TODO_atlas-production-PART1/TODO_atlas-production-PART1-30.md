@BinReaper Production TODOs

## TODO

* [ ] TODO 88: Establish hostile-plugin and backend conformance gates

  1.2 source task(s): `T22.1.4`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T22.1.2, T22.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/execution/hostile_plugins/ (extend); tests/execution/test_backend_conformance.py (extend); scripts/run_plugin_isolation_matrix.py (create); .github/workflows/plugin-isolation.yml (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Prove subprocess containment, failure mapping, cleanup, resource accounting, and semantic equivalence using a maintained synthetic hostile-plugin corpus on every supported platform.
  * Restore or protect this invariant: Every supported platform has a current pass/fail/reduced-assurance enforcement matrix.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `tests/execution/hostile_plugins/` (extend: Cover traversal, source access, network, spawn, flood, timeout, memory/temp exhaustion, protocol forgery, and secret discovery.); `tests/execution/test_backend_conformance.py` (extend: Run common WorkSpec/result/state/recovery expectations for all backends.); `scripts/run_plugin_isolation_matrix.py` (create: Produce machine-readable platform/control/test evidence.); `.github/workflows/plugin-isolation.yml` (create: Gate supported platform claims and retain reports.)
  * Epic boundary: Subprocess plugin isolation and enforceable resource controls — Run untrusted or high-risk plugins outside the core process with mediated inputs, explicit capabilities, bounded resources, deterministic termination, and visible platform limitations.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-020: Add subprocess execution with mediated artifacts and enforceable limits; evidence: GAP-014, REQ-022; ADR-010.
  * Canonical proposed files/interfaces: Create `atlas/execution/subprocess.py`; extend plugin descriptors/policy and workspace/artifact access. / Subprocess backend implementing ExecutionBackend; `CapabilityGrant`; mediated artifact token/locator.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-020 requires: Third-party analyzers should not share process authority, unrestricted filesystem, or StateStore credentials.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Prove subprocess containment, failure mapping, cleanup, resource accounting, and semantic equivalence using a maintained synthetic hostile-plugin corpus on every supported platform.
  * Component dispositions: `tests/execution/hostile_plugins/` (extend: Cover traversal, source access, network, spawn, flood, timeout, memory/temp exhaustion, protocol forgery, and secret discovery.); `tests/execution/test_backend_conformance.py` (extend: Run common WorkSpec/result/state/recovery expectations for all backends.); `scripts/run_plugin_isolation_matrix.py` (create: Produce machine-readable platform/control/test evidence.); `.github/workflows/plugin-isolation.yml` (create: Gate supported platform claims and retain reports.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define benign reference plugins and one synthetic fixture for every declared threat/failure mode.
  * Run in-process only for trusted fixtures and subprocess for hostile/untrusted cases; compare normalized valid results.
  * Verify workspace containment, process cleanup, budget metrics, denied grants, error taxonomy, checkpoint/recovery, and status evidence.
  * Publish a versioned enforcement report tied to OS/kernel/runtime, plugin digest, and test suite.

  Security and safety requirements

  * Use inert synthetic payloads and loopback/fake services; do not include live destructive exploit code or credentials.
  * Fail the release gate when a mandatory supported-platform containment test regresses or is skipped without approved exception.
  * Scan retained output/bundles for synthetic secret leakage and path escape.
  * Ensure test plugins cannot access CI release credentials or host-wide writable locations.

  Edge cases and outliers to handle

  * CI runner itself lacks required kernel controls.
  * Hostile plugin destabilizes or fills shared runner.
  * Test passes due to missing assertion after early failure.
  * Platform semantics differ in child-tree cleanup.

  Acceptance criteria (“done” definition)

  * Every supported platform has a current pass/fail/reduced-assurance enforcement matrix.
  * Hostile fixtures cannot commit lifecycle state or escape mediated inputs under claimed controls.
  * Cleanup and resource-accounting assertions pass after every failure class.
  * No unsupported control is marketed as enforced and no mandatory isolation test is silently skipped.

  Testing plan

  * Backend conformance suite.
  * Hostile corpus integration tests.
  * Runner resource/cleanup assertions.
  * Secret/path escape scans.
  * Skip/exception policy tests.
  * Repeated/soak hostile-plugin tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Backend conformance suite., Hostile corpus integration tests., Runner resource/cleanup assertions., Secret/path escape scans., Skip/exception policy tests., Repeated/soak hostile-plugin tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T22.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/execution/hostile_plugins/, tests/execution/test_backend_conformance.py, scripts/run_plugin_isolation_matrix.py, .github/workflows/plugin-isolation.yml.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 89: Define retention classes and implement reference-safe cleanup

  1.2 source task(s): `T23.1.1`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T12.1.4, T17.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/retention/models.py (create); atlas/retention/service.py::RetentionManager (create); atlas/schema/migrations/*_retention.sql (create); docs/operations/retention.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create a policy-driven retention and garbage-collection service that distinguishes authoritative history, replay-critical content, workspaces, caches, telemetry, and publications while never deleting referenced evidence.
  * Restore or protect this invariant: Retention periods and required preserved classes are explicitly resolved and versioned before deletion is enabled.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15.

  Where this applies

  * Primary affected components: `atlas/retention/models.py` (create: Define retention classes, holds, eligibility, plan, attempt, and result records.); `atlas/retention/service.py::RetentionManager` (create: Plan, verify, execute, and reconcile safe deletions.); `atlas/schema/migrations/*_retention.sql` (create: Persist holds, cleanup plans/attempts, tombstones, and verification.); `docs/operations/retention.md` (create: Document policy, dry-run, legal/incident holds, recovery, and limitations.)
  * Epic boundary: Retention, compatibility, plugin SDK, and source-provider evolution — Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Retention, compatibility, plugin SDK, and source-provider evolution.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create a policy-driven retention and garbage-collection service that distinguishes authoritative history, replay-critical content, workspaces, caches, telemetry, and publications while never deleting referenced evidence.
  * Component dispositions: `atlas/retention/models.py` (create: Define retention classes, holds, eligibility, plan, attempt, and result records.); `atlas/retention/service.py::RetentionManager` (create: Plan, verify, execute, and reconcile safe deletions.); `atlas/schema/migrations/*_retention.sql` (create: Persist holds, cleanup plans/attempts, tombstones, and verification.); `docs/operations/retention.md` (create: Document policy, dry-run, legal/incident holds, recovery, and limitations.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Classify lifecycle records, events/outbox, content blobs, quarantine/workspaces, checkpoints, plugin outputs, diagnostics, and telemetry by minimum retention and replay/lineage dependency.
  * Compute deletion eligibility from reference graph, current/nonterminal state, holds, publication lineage, backup policy, and configured retention version.
  * Require dry-run plan with counts/bytes/reasons, explicit confirmation/policy for consequential deletion, then no-follow/no-replace safe execution and post-delete verification.
  * Persist tombstone and cleanup evidence without retaining prohibited content; support interrupted-run reconciliation.

  Security and safety requirements

  * Never follow symlinks or delete outside managed roots; operate by durable managed identity rather than arbitrary path strings.
  * Do not delete content/evidence/checkpoints needed for current decisions, publications, active recovery, audit, or declared replay guarantees.
  * Apply least-privilege filesystem/store access and bound traversal/query/delete batches.
  * Treat model/plugin recommendations as proposals only; deterministic policy and reference checks authorize deletion.

  Edge cases and outliers to handle

  * Content blob referenced by multiple jobs/publications.
  * Hold is added between plan and execution.
  * Deletion succeeds but database update fails or vice versa.
  * Legacy/unindexed object cannot prove ownership.

  Acceptance criteria (“done” definition)

  * Retention periods and required preserved classes are explicitly resolved and versioned before deletion is enabled.
  * Dry-run and execution use the same immutable plan or fail on changed preconditions.
  * No referenced, held, active, or unknown-ownership object is deleted.
  * Interrupted cleanup is idempotently reconciled with durable per-object evidence.

  Testing plan

  * Eligibility/reference graph tests.
  * Symlink/path escape negative tests.
  * Concurrent hold/reference race tests.
  * Partial deletion/transaction fault tests.
  * Large-batch/quota performance tests.
  * Backup/restore and audit evidence tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Eligibility/reference graph tests., Symlink/path escape negative tests., Concurrent hold/reference race tests., Partial deletion/transaction fault tests., Large-batch/quota performance tests., Backup/restore and audit evidence tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T23.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/retention/models.py, atlas/retention/service.py::RetentionManager, atlas/schema/migrations/*_retention.sql, docs/operations/retention.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 90: Implement the compatibility catalog and deprecation telemetry

  1.2 source task(s): `T23.1.2`
  Priority: `P2`
  Estimated effort: `14 hours`
  Dependencies: `T3.1.4, T4.1.4, T8.1.4, T14.1.4, T18.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/compat/catalog.py::CompatibilityCatalog (create); atlas/compat/translators.py (create); atlas/status/projection.py (extend); docs/compatibility.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Centralize supported versions, translators, compatibility windows, deprecation state, and stored-data/API/plugin/config/checkpoint decisions so adapters cannot silently reinterpret records.
  * Restore or protect this invariant: Every persisted/public contract has one catalog entry and explicit read/write/deprecation policy.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15.

  Where this applies

  * Primary affected components: `atlas/compat/catalog.py::CompatibilityCatalog` (create: Declare supported producers/consumers, migration paths, read/write ranges, and deprecations.); `atlas/compat/translators.py` (create: Host explicit deterministic one-version transformations with provenance.); `atlas/status/projection.py` (extend: Expose compatibility/deprecation/reduced-readability markers.); `docs/compatibility.md` (create: Publish matrices and support/deprecation policy.)
  * Epic boundary: Retention, compatibility, plugin SDK, and source-provider evolution — Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8,#13,#22,#27,#29; PROMPT:Pasted markdown (2).md:Stages 3,7,8,13,15; PDF:p.17,p.18,p.24,p.26,p.28.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Retention, compatibility, plugin SDK, and source-provider evolution.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Centralize supported versions, translators, compatibility windows, deprecation state, and stored-data/API/plugin/config/checkpoint decisions so adapters cannot silently reinterpret records.
  * Component dispositions: `atlas/compat/catalog.py::CompatibilityCatalog` (create: Declare supported producers/consumers, migration paths, read/write ranges, and deprecations.); `atlas/compat/translators.py` (create: Host explicit deterministic one-version transformations with provenance.); `atlas/status/projection.py` (extend: Expose compatibility/deprecation/reduced-readability markers.); `docs/compatibility.md` (create: Publish matrices and support/deprecation policy.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Register database, config, pipeline, event, plugin, finding/evidence, checkpoint, protocol, API, and manifest schemas with current/read/write ranges.
  * Require an explicit translator or hard incompatibility; never best-effort unknown-field guessing for authority-bearing records.
  * Record original version/digest, translator chain, output version/digest, warnings, and lossiness.
  * Emit bounded deprecation telemetry and operator reports before write support is removed.

  Security and safety requirements

  * Reject downgrade paths that discard authority, provenance, safety, actor, or signature fields.
  * Treat external/plugin schema declarations as untrusted until catalog validation.
  * Sign/hash release compatibility artifacts as part of package provenance.
  * Do not expose customer identifiers or raw payloads in deprecation metrics.

  Edge cases and outliers to handle

  * Record is newer than runtime.
  * Translator chain is missing, cyclic, or lossy.
  * Read compatibility exists but write-back would corrupt data.
  * Plugin supports overlapping but incompatible minor versions.

  Acceptance criteria (“done” definition)

  * Every persisted/public contract has one catalog entry and explicit read/write/deprecation policy.
  * Unsupported or lossy authority-bearing conversions fail closed with actionable status.
  * Compatibility reports identify affected records/plugins/configurations before upgrade.
  * Deprecation removal requires evidence that migration and rollback gates passed.

  Testing plan

  * Catalog completeness tests.
  * Translator golden/property tests.
  * Unknown/newer/downgrade negative tests.
  * Plugin/protocol negotiation tests.
  * Deprecation telemetry cardinality tests.
  * Upgrade/rollback compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Catalog completeness tests., Translator golden/property tests., Unknown/newer/downgrade negative tests., Plugin/protocol negotiation tests., Deprecation telemetry cardinality tests., Upgrade/rollback compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T23.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/compat/catalog.py::CompatibilityCatalog, atlas/compat/translators.py, atlas/status/projection.py, docs/compatibility.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
