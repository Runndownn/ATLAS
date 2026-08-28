@BinReaper Production TODOs

## TODO

* [ ] TODO 79: Build the canonical versioned job status projection

  1.2 source task(s): `T20.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T20.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/status/models.py::JobStatusV1 (create); atlas/status/projection.py::StatusProjection (create); atlas/status/service.py (extend); atlas/cli.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide one read model derived from authoritative state for current phase/attempt, progress, controls, checkpoints, blockers, retries, budgets, events, lineage, and recovery.
  * Restore or protect this invariant: An operator can identify exact current phase, attempt, checkpoint, control, blocker, retry/recovery action, and provenance completeness without raw DB access.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/status/models.py::JobStatusV1` (create: Define the stable status schema and completeness/degradation markers.); `atlas/status/projection.py::StatusProjection` (create: Read and combine authoritative state using a consistent snapshot.); `atlas/status/service.py` (extend: Expose job/list/watch/export queries with pagination and versioning.); `atlas/cli.py` (extend: Render human and JSON status without inventing missing state.)
  * Epic boundary: Canonical status, telemetry, health, and diagnostics — Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.
  * Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-018 requires: Operators need authoritative progress, blockers, provenance, and recovery evidence without reading raw SQLite or logs.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Provide one read model derived from authoritative state for current phase/attempt, progress, controls, checkpoints, blockers, retries, budgets, events, lineage, and recovery.
  * Component dispositions: `atlas/status/models.py::JobStatusV1` (create: Define the stable status schema and completeness/degradation markers.); `atlas/status/projection.py::StatusProjection` (create: Read and combine authoritative state using a consistent snapshot.); `atlas/status/service.py` (extend: Expose job/list/watch/export queries with pagination and versioning.); `atlas/cli.py` (extend: Render human and JSON status without inventing missing state.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define status fields and authority source for job/phase/attempt/work, progress numerator/denominator, pending control, checkpoint age, claim/lease, retry, blocker, budget, outbox backlog, provenance completeness, and publication state.
  * Read from a consistent StateStore transaction/snapshot and mark unavailable/corrupt/legacy fields explicitly.
  * Define stable pagination, filtering, ordering, and optional incremental sequence cursor.
  * Keep projection rebuildable; never write lifecycle state from status code.

  Security and safety requirements

  * Apply path/content minimization and authorization filters in deployment adapters before returning sensitive details.
  * Do not derive success from event transport, logs, worker claims, or model output.
  * Reject query injection and bound list/page/time-range parameters.
  * Expose stale/partial/degraded status explicitly rather than filling defaults that imply safety.

  Edge cases and outliers to handle

  * Legacy job lacks attempts/checkpoints/lineage.
  * Rows change during projection.
  * Corrupt or incompatible record.
  * Status query over millions of artifacts/work items.

  Acceptance criteria (“done” definition)

  * An operator can identify exact current phase, attempt, checkpoint, control, blocker, retry/recovery action, and provenance completeness without raw DB access.
  * Status is rebuildable from authoritative state and events are supplemental only.
  * Legacy/partial/corrupt fields are explicit and never mistaken for complete.
  * Query performance and pagination are measured on representative large jobs.

  Testing plan

  * Projection golden tests.
  * Consistent-snapshot concurrency tests.
  * Legacy/degraded/corrupt record tests.
  * Authorization/redaction adapter tests.
  * Large-job query benchmarks.
  * CLI/JSON/API schema compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Projection golden tests., Consistent-snapshot concurrency tests., Legacy/degraded/corrupt record tests., Authorization/redaction adapter tests., Large-job query benchmarks., CLI/JSON/API schema compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T20.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/status/models.py::JobStatusV1, atlas/status/projection.py::StatusProjection, atlas/status/service.py, atlas/cli.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 80: Implement health, readiness, and sanitized diagnostic bundles

  1.2 source task(s): `T20.1.4`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T20.1.2, T20.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/status/health.py (create); atlas/diagnostics/bundle.py::DiagnosticBundleBuilder (create); atlas/cli.py (extend); docs/operations/diagnostics.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Define deterministic service health/readiness and produce integrity-manifested diagnostic bundles that operators can share without raw content or secrets.
  * Restore or protect this invariant: Health/readiness results are deterministic and identify each failed dependency/control.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/status/health.py` (create: Evaluate process, store, migration, recovery, claim, workspace, outbox, and optional dependency health.); `atlas/diagnostics/bundle.py::DiagnosticBundleBuilder` (create: Collect bounded status/config/schema/runtime/evidence summaries and manifest hashes.); `atlas/cli.py` (extend: Expose health, readiness, and diagnostic bundle commands.); `docs/operations/diagnostics.md` (create: Document collection, redaction, interpretation, and secure handling.)
  * Epic boundary: Canonical status, telemetry, health, and diagnostics — Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.
  * Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-018 requires: Operators need authoritative progress, blockers, provenance, and recovery evidence without reading raw SQLite or logs.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Define deterministic service health/readiness and produce integrity-manifested diagnostic bundles that operators can share without raw content or secrets.
  * Component dispositions: `atlas/status/health.py` (create: Evaluate process, store, migration, recovery, claim, workspace, outbox, and optional dependency health.); `atlas/diagnostics/bundle.py::DiagnosticBundleBuilder` (create: Collect bounded status/config/schema/runtime/evidence summaries and manifest hashes.); `atlas/cli.py` (extend: Expose health, readiness, and diagnostic bundle commands.); `docs/operations/diagnostics.md` (create: Document collection, redaction, interpretation, and secure handling.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Separate liveness from readiness and dependency degradation; define exact reason codes and recovery guidance.
  * Include schema/config/runtime/plugin versions, sanitized status, recent stable error codes, migration/integrity state, resource summary, and selected evidence references.
  * Create a bundle manifest with file sizes, schema versions, SHA-256 hashes, omissions, and redaction policy version.
  * Bound time, size, rows, and path samples; permit partial bundle with explicit missing-component records.

  Security and safety requirements

  * Redact and scan before archive creation; exclude raw artifact bytes, secrets, credentials, unrestricted environment, and arbitrary logs by default.
  * Write to a safe caller-selected/controlled directory using no-replace semantics and secure permissions.
  * Do not execute plugins or external commands during bundle collection unless an explicit trusted diagnostic adapter exists.
  * Treat diagnostic export as potentially sensitive and document optional deployment authorization/encryption.

  Edge cases and outliers to handle

  * Store unavailable or corrupt.
  * Bundle target is symlink/path traversal or disk becomes full.
  * A collector times out or emits malformed data.
  * Secret-like fixture appears in metadata/error text.

  Acceptance criteria (“done” definition)

  * Health/readiness results are deterministic and identify each failed dependency/control.
  * Diagnostic bundle verifies against its manifest and records all omissions/degraded collectors.
  * Synthetic secret/raw-content tests find no prohibited data.
  * Bundle failure cannot mutate lifecycle state or overwrite an existing file.

  Testing plan

  * Health truth-table tests.
  * Dependency outage tests.
  * Diagnostic reproducibility/hash tests.
  * Secret/redaction scan tests.
  * Path/symlink/no-replace tests.
  * Partial/disk-full/collector-timeout tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Health truth-table tests., Dependency outage tests., Diagnostic reproducibility/hash tests., Secret/redaction scan tests., Path/symlink/no-replace tests., Partial/disk-full/collector-timeout tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T20.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/status/health.py, atlas/diagnostics/bundle.py::DiagnosticBundleBuilder, atlas/cli.py, docs/operations/diagnostics.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 81: Define versioned external command, status, and error schemas

  1.2 source task(s): `T21.1.1`
  Priority: `P2`
  Estimated effort: `14 hours`
  Dependencies: `T8.1.4, T19.1.4, T20.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/api/contracts.py (create); atlas/service/commands.py (extend); atlas/status/models.py (extend); docs/api/contracts-v1.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create transport-neutral request/response contracts that preserve command idempotency, expected state, actor attribution, lifecycle guards, and status authority across CLI, Python, REST, and future clients.
  * Restore or protect this invariant: Equivalent local and external contracts produce identical authoritative command outcomes.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/api/contracts.py` (create: Define v1 command, status, pagination, problem/error, and compatibility envelopes.); `atlas/service/commands.py` (extend: Map transport-neutral contracts to canonical command validation and results.); `atlas/status/models.py` (extend: Expose stable external projection schemas without transport coupling.); `docs/api/contracts-v1.md` (create: Document fields, semantics, idempotency, versioning, and lifecycle restrictions.)
  * Epic boundary: Versioned external command and event adapters — Expose REST, RabbitMQ, and webhook surfaces only as adapters over canonical command, status, and durable event contracts.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-019: Implement REST, RabbitMQ, and webhook adapters over the shared command/event contracts; evidence: REQ-024, REQ-025, REQ-030; current RabbitMQ publisher-only behavior.
  * Canonical proposed files/interfaces: Create `atlas/api/`; complete event transport/dispatcher; optional webhook adapter; CLI/Python remain canonical clients. / REST v1, event envelope v1, webhook delivery record; no alternate phase/workflow semantics.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-019 requires: External interfaces are useful only after durable semantics exist and must not create alternate lifecycle authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create transport-neutral request/response contracts that preserve command idempotency, expected state, actor attribution, lifecycle guards, and status authority across CLI, Python, REST, and future clients.
  * Component dispositions: `atlas/api/contracts.py` (create: Define v1 command, status, pagination, problem/error, and compatibility envelopes.); `atlas/service/commands.py` (extend: Map transport-neutral contracts to canonical command validation and results.); `atlas/status/models.py` (extend: Expose stable external projection schemas without transport coupling.); `docs/api/contracts-v1.md` (create: Document fields, semantics, idempotency, versioning, and lifecycle restrictions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define submit, pause, resume, cancel, retry, reconcile, review, and publication command bodies with request ID, idempotency key, actor, expected state/version, reason, and typed payload.
  * Define stable success, accepted/pending, conflict, validation, policy, unavailable, and internal error responses.
  * Define schema/version negotiation and additive/deprecation rules; reject unknown major versions and ambiguous duplicate fields.
  * Map every contract to the same `CommandService`/`StatusService` used by local clients.

  Security and safety requirements

  * Validate size, encoding, duplicate keys, unknown fields policy, enum values, IDs, paths/URLs, and content types before command handling.
  * Do not infer authorization from transport or event origin; pass authenticated identity/claims through an optional deployment adapter.
  * Prevent mass assignment of internal state, actor, policy, fencing, claim, or completion fields.
  * Separate errors safe for remote clients from diagnostic details and secret-bearing causes.

  Edge cases and outliers to handle

  * Same idempotency key with a different body.
  * Client uses stale expected version.
  * Unknown/old schema version.
  * Malformed JSON, duplicate keys, huge nested payload, or unsupported content type.

  Acceptance criteria (“done” definition)

  * Equivalent local and external contracts produce identical authoritative command outcomes.
  * No request field can directly set job/phase/attempt state, fencing, policy result, or publication success.
  * Replay/stale/version conflicts are deterministic and machine-readable.
  * Schemas and examples are generated or CI-checked against implementation.

  Testing plan

  * Contract serialization/golden tests.
  * Duplicate-key/malformed/size fuzz tests.
  * CLI/Python/external equivalence tests.
  * Replay/stale-version tests.
  * Mass-assignment and lifecycle-bypass negative tests.
  * Schema compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Contract serialization/golden tests., Duplicate-key/malformed/size fuzz tests., CLI/Python/external equivalence tests., Replay/stale-version tests., Mass-assignment and lifecycle-bypass negative tests., Schema compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T21.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/api/contracts.py, atlas/service/commands.py, atlas/status/models.py, docs/api/contracts-v1.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
