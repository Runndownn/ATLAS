@BinReaper Production TODOs

## TODO

* [ ] TODO 100: Implement and validate the optional object-backed ContentStore

  1.2 source task(s): `T25.1.4`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T25.1.2, T25.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/storage/object_store.py::ObjectContentStore (create); atlas/config/storage.py (extend); atlas/migration/content.py (create); tests/storage/test_object_store_conformance.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Add object storage behind immutable content contracts with hash verification, staged commit, consistency handling, references, retention, reconciliation, and verified migration.
  * Restore or protect this invariant: Object backend passes immutable ContentStore, integrity, reference, retention, recovery, and replay tests.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-021; REQ-026,REQ-030; PDF:p.2,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/storage/object_store.py::ObjectContentStore` (create: Implement content operations with provider-neutral object client.); `atlas/config/storage.py` (extend: Select provider/bucket/prefix/credentials/consistency settings through typed config.); `atlas/migration/content.py` (create: Copy, verify, resume, cut over, and reconcile local/object content.); `tests/storage/test_object_store_conformance.py` (create: Run conformance with deterministic fake and approved integration provider.)
  * Epic boundary: Measured optional PostgreSQL and object-storage adapters — Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-021: Add PostgreSQL and object-storage adapters only after measured trigger conditions; evidence: REQ-026, REQ-030; ADR-003; OQ-007.
  * Canonical proposed files/interfaces: Later `atlas/persistence/postgres.py`, `atlas/artifacts/object_store.py`; migration/conformance tooling. / Existing persistence/content conformance suites; provider configuration/version.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-021 requires: Additional stores are justified only when SQLite/local CAS fail defined workloads while semantics are already stable.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Add object storage behind immutable content contracts with hash verification, staged commit, consistency handling, references, retention, reconciliation, and verified migration.
  * Component dispositions: `atlas/storage/object_store.py::ObjectContentStore` (create: Implement content operations with provider-neutral object client.); `atlas/config/storage.py` (extend: Select provider/bucket/prefix/credentials/consistency settings through typed config.); `atlas/migration/content.py` (create: Copy, verify, resume, cut over, and reconcile local/object content.); `tests/storage/test_object_store_conformance.py` (create: Run conformance with deterministic fake and approved integration provider.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Stage uploads under attempt identity, stream/hash/size verify, commit immutable canonical key, verify visibility/metadata/bytes, and record provider object version/etag as supplemental.
  * Handle provider consistency by explicit read/verify/retry rules without treating ETag/path as canonical content identity.
  * Implement resumable copy manifest, reference validation, retention/holds, orphan reconciliation, and local-to-object cutover.
  * Document durability/availability, backup/replication, lifecycle policies, cost, health, and rollback.

  Security and safety requirements

  * Use least-privilege bucket/prefix credentials, TLS, optional encryption policy, secret references, and deny public access by default.
  * Prevent key/prefix/path traversal, metadata injection, bucket confusion, cross-tenant access, and overwrite of existing different content.
  * Do not expose signed URLs/credentials broadly; scope and expire any mediated access.
  * Verify content by SHA-256 after transfer; provider metadata alone is insufficient.

  Edge cases and outliers to handle

  * Upload completes but response is lost.
  * Object is not immediately visible.
  * Same canonical key exists with wrong bytes.
  * Credentials/bucket policy change during migration.

  Acceptance criteria (“done” definition)

  * Object backend passes immutable ContentStore, integrity, reference, retention, recovery, and replay tests.
  * No-replace commit and byte verification prevent canonical-key corruption.
  * Migration/cutover/rollback preserves all referenced content hashes and one writable authority.
  * Approved workload demonstrates benefit and provider consistency limitations are explicit.

  Testing plan

  * ContentStore conformance suite.
  * Timeout/unknown upload/reconciliation tests.
  * Consistency visibility tests.
  * Wrong-byte/key/prefix injection negative tests.
  * Migration/resume/cutover/rollback tests.
  * Credential/URL redaction and least-privilege tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: ContentStore conformance suite., Timeout/unknown upload/reconciliation tests., Consistency visibility tests., Wrong-byte/key/prefix injection negative tests., Migration/resume/cutover/rollback tests., Credential/URL redaction and least-privilege tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T25.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/storage/object_store.py::ObjectContentStore, atlas/config/storage.py, atlas/migration/content.py, tests/storage/test_object_store_conformance.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 101: Define the authenticated remote worker protocol and compatibility handshake

  1.2 source task(s): `T26.1.1`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T15.1.4, T18.1.4, T21.1.4, T25.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/remote_protocol.py (create); atlas/execution/remote.py::RemoteExecutionBackend (create); atlas/worker/contracts.py (create); docs/architecture/remote-worker-protocol.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify immutable work dispatch, leases, heartbeats, fencing, scoped artifacts, result integrity, cancellation, and version negotiation without granting workers lifecycle authority.
  * Restore or protect this invariant: Protocol is versioned and compatibility failure is explicit before work starts.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29.

  Where this applies

  * Primary affected components: `atlas/execution/remote_protocol.py` (create: Define worker registration, capability, lease, WorkSpec, progress, result, cancel, and drain envelopes.); `atlas/execution/remote.py::RemoteExecutionBackend` (create: Implement coordinator-side backend contract without scheduler authority.); `atlas/worker/contracts.py` (create: Expose worker-side typed protocol and compatibility catalog integration.); `docs/architecture/remote-worker-protocol.md` (create: Document trust, identity, failure, ordering, and non-authority invariants.)
  * Epic boundary: Optional remote worker execution — Scale execution location without changing phase barriers, coordinator authority, work semantics, exact-byte identity, or durable recovery.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.
  * Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-022 requires: Remote execution is an infrastructure adapter, not a reason to redefine lifecycle semantics.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify immutable work dispatch, leases, heartbeats, fencing, scoped artifacts, result integrity, cancellation, and version negotiation without granting workers lifecycle authority.
  * Component dispositions: `atlas/execution/remote_protocol.py` (create: Define worker registration, capability, lease, WorkSpec, progress, result, cancel, and drain envelopes.); `atlas/execution/remote.py::RemoteExecutionBackend` (create: Implement coordinator-side backend contract without scheduler authority.); `atlas/worker/contracts.py` (create: Expose worker-side typed protocol and compatibility catalog integration.); `docs/architecture/remote-worker-protocol.md` (create: Document trust, identity, failure, ordering, and non-authority invariants.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define service/worker identity, protocol version, runtime/plugin/backend capability digest, WorkSpec digest, immutable input references, budgets, deadline, lease/fencing token, idempotency key, and result/evidence digest.
  * Negotiate compatible versions/capabilities before assignment and reject semantic/plugin/config mismatches.
  * Define heartbeat/lease renewal, cancellation acknowledgement, drain, progress/checkpoint reference, result upload/verification, stale rejection, and replay.
  * Keep phase/work planning and authoritative attempt transitions in coordinator/StateStore.

  Security and safety requirements

  * Use mutual service identity and encrypted transport as deployment controls; scope credentials and rotate/revoke them.
  * Workers receive no StateStore credentials and only single-job/attempt/content-scoped access.
  * Sign or authenticate protocol messages and bind all results to WorkSpec/attempt/fencing identity.
  * Reject worker-provided lifecycle state, policy, evidence authority, publication, or arbitrary capability claims.

  Edge cases and outliers to handle

  * Worker upgrades between handshake and result.
  * Clock skew and delayed heartbeat.
  * Duplicate assignment/result.
  * Malicious worker forges another work item or content digest.

  Acceptance criteria (“done” definition)

  * Protocol is versioned and compatibility failure is explicit before work starts.
  * Worker cannot mutate lifecycle state or access undeclared artifacts.
  * Stale/duplicate/forged results are rejected deterministically and retained as evidence.
  * Local and remote backends share WorkSpec/result conformance semantics.

  Testing plan

  * Protocol codec/golden/fuzz tests.
  * Compatibility negotiation tests.
  * Identity/forgery/replay negative tests.
  * Lease/heartbeat/clock tests.
  * Local/remote contract differential tests.
  * Credential scope/revocation tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Protocol codec/golden/fuzz tests., Compatibility negotiation tests., Identity/forgery/replay negative tests., Lease/heartbeat/clock tests., Local/remote contract differential tests., Credential scope/revocation tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T26.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/remote_protocol.py, atlas/execution/remote.py::RemoteExecutionBackend, atlas/worker/contracts.py, docs/architecture/remote-worker-protocol.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 102: Implement the least-privileged remote worker service

  1.2 source task(s): `T26.1.2`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T26.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/worker/service.py::AtlasWorker (create); atlas/worker/config.py (create); atlas/worker/artifacts.py (create); docs/operations/worker.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Run assigned WorkSpecs through approved execution backends with scoped artifact access, resource policy, heartbeats, cancellation, and no direct control-plane persistence.
  * Restore or protect this invariant: Worker completes only authenticated assigned WorkSpecs and cannot write lifecycle authority.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29.

  Where this applies

  * Primary affected components: `atlas/worker/service.py::AtlasWorker` (create: Own registration, assignment lifecycle, backend execution, heartbeat, result, and drain.); `atlas/worker/config.py` (create: Define service identity, capabilities, concurrency, cache, resource, and endpoint settings.); `atlas/worker/artifacts.py` (create: Fetch/verify scoped immutable inputs and upload/verify outputs.); `docs/operations/worker.md` (create: Document deployment, trust, upgrades, drain, diagnostics, and incidents.)
  * Epic boundary: Optional remote worker execution — Scale execution location without changing phase barriers, coordinator authority, work semantics, exact-byte identity, or durable recovery.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-022: Add remote workers with leases, fencing, and the existing WorkSpec contract; evidence: REQ-026, REQ-030; Option C deferred; R-11.
  * Canonical proposed files/interfaces: Later `atlas/execution/remote.py`, worker service/protocol, deployment docs. / Remote ExecutionBackend, worker protocol v1, lease/heartbeat, scoped artifact tokens.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-022 requires: Remote execution is an infrastructure adapter, not a reason to redefine lifecycle semantics.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Run assigned WorkSpecs through approved execution backends with scoped artifact access, resource policy, heartbeats, cancellation, and no direct control-plane persistence.
  * Component dispositions: `atlas/worker/service.py::AtlasWorker` (create: Own registration, assignment lifecycle, backend execution, heartbeat, result, and drain.); `atlas/worker/config.py` (create: Define service identity, capabilities, concurrency, cache, resource, and endpoint settings.); `atlas/worker/artifacts.py` (create: Fetch/verify scoped immutable inputs and upload/verify outputs.); `docs/operations/worker.md` (create: Document deployment, trust, upgrades, drain, diagnostics, and incidents.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Advertise only locally verified backend/plugin/tool/resource capabilities and apply server-approved grants per assignment.
  * Fetch immutable inputs through scoped single-use/expiring references, verify content hashes, and isolate per-attempt workspace/cache.
  * Execute using in-process only for explicitly trusted plugins or subprocess for untrusted/high-risk work under the same policy.
  * Heartbeat/renew, honor cancel/drain, upload staged results/evidence, and discard/fence after lease loss.

  Security and safety requirements

  * No StateStore/database credentials or broad content-store credentials on workers.
  * Use least-privilege service identity, secure bootstrap/rotation, host hardening, secret references, and no raw secrets in diagnostics.
  * Verify executable/plugin/tool/image identity and sanitize all inputs/outputs as with local backends.
  * Cache by content identity with integrity and retention controls; never treat cache presence as provenance.

  Edge cases and outliers to handle

  * Artifact transfer interrupted or wrong bytes received.
  * Lease lost while plugin still runs.
  * Worker disk full or cache corrupt.
  * Worker compromised or identity revoked.

  Acceptance criteria (“done” definition)

  * Worker completes only authenticated assigned WorkSpecs and cannot write lifecycle authority.
  * All input/output bytes are hash-verified and scoped to the attempt.
  * Lease loss/cancel/drain leads to deterministic backend stop/result handling.
  * Compromise/revocation can fence the worker and preserve investigation evidence.

  Testing plan

  * Worker service lifecycle tests.
  * Scoped artifact token/expiry tests.
  * Transfer corruption/interruption tests.
  * Lease-loss/cancel/drain tests.
  * Cache integrity/retention tests.
  * Identity revocation/compromise tabletop tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Worker service lifecycle tests., Scoped artifact token/expiry tests., Transfer corruption/interruption tests., Lease-loss/cancel/drain tests., Cache integrity/retention tests., Identity revocation/compromise tabletop tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T26.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/worker/service.py::AtlasWorker, atlas/worker/config.py, atlas/worker/artifacts.py, docs/operations/worker.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
