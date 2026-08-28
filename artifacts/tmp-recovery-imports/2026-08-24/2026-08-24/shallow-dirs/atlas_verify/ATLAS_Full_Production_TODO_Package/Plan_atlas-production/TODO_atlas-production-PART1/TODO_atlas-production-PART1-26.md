@BinReaper Production TODOs

## TODO

* [ ] TODO 76: Verify graceful shutdown, forced restart, and orphan containment

  1.2 source task(s): `T19.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T19.1.2, T19.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/service/shutdown.py (create); atlas/service/daemon.py (extend); tests/integration/test_daemon_recovery.py (create); docs/operations/daemon-runbook.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Demonstrate deterministic behavior when the daemon drains, is killed, loses database access, or leaves child processes and claims behind.
  * Restore or protect this invariant: Graceful stop leaves no new claims and records deterministic terminal/suspended/checkpoint state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/service/shutdown.py` (create: Coordinate drain deadlines, safe-point requests, claim release, and forced termination.); `atlas/service/daemon.py` (extend: Integrate signal handling, orphan detection, and restart summary.); `tests/integration/test_daemon_recovery.py` (create: Exercise multi-process control, kill, restart, and ownership scenarios.); `docs/operations/daemon-runbook.md` (create: Provide install/start/stop/recover/diagnose/rollback procedures.)
  * Epic boundary: Long-running local runtime ownership — Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.
  * Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-017 requires: A CLI process cannot durably own jobs or honor controls from another process; hydrating private `_jobs` is not control.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Demonstrate deterministic behavior when the daemon drains, is killed, loses database access, or leaves child processes and claims behind.
  * Component dispositions: `atlas/service/shutdown.py` (create: Coordinate drain deadlines, safe-point requests, claim release, and forced termination.); `atlas/service/daemon.py` (extend: Integrate signal handling, orphan detection, and restart summary.); `tests/integration/test_daemon_recovery.py` (create: Exercise multi-process control, kill, restart, and ownership scenarios.); `docs/operations/daemon-runbook.md` (create: Provide install/start/stop/recover/diagnose/rollback procedures.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define graceful shutdown phases, deadlines, safe-point behavior, subprocess termination, checkpoint flush, and claim release.
  * On forced restart, run fencing and recovery before accepting new commands/work.
  * Detect or reconcile orphan subprocesses/workspaces using attempt ownership and platform-supported process identity.
  * Produce a startup/shutdown recovery report with blocked items and operator actions.

  Security and safety requirements

  * Never kill unrelated processes based on reusable PID alone; bind process identity to attempt/start metadata or platform handle.
  * Preserve bounded diagnostics and sensitive-data redaction during crash handling.
  * Do not release authority before side-effect state is safely stopped or classified.
  * Run service with least privilege and safe file/socket permissions in runbook examples.

  Edge cases and outliers to handle

  * SIGTERM then SIGKILL during checkpoint.
  * Host restart loses process handles but not child process.
  * Database unavailable during claim release.
  * Daemon version changes between crash and restart.

  Acceptance criteria (“done” definition)

  * Graceful stop leaves no new claims and records deterministic terminal/suspended/checkpoint state.
  * Forced restart fences the old owner and produces one recovery decision per nonterminal attempt.
  * Orphan handling cannot terminate an unrelated process.
  * Runbook and tests cover foreground rollback for new jobs without stealing existing daemon-owned work.

  Testing plan

  * Signal/drain unit tests.
  * Kill/restart integration tests.
  * Orphan identity negative tests.
  * Database outage during shutdown tests.
  * Version-change recovery tests.
  * Runbook command smoke tests where repository-supported.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Signal/drain unit tests., Kill/restart integration tests., Orphan identity negative tests., Database outage during shutdown tests., Version-change recovery tests., Runbook command smoke tests where repository-supported..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T19.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/service/shutdown.py, atlas/service/daemon.py, tests/integration/test_daemon_recovery.py, docs/operations/daemon-runbook.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 77: Define structured logging, correlation, error catalog, and redaction

  1.2 source task(s): `T20.1.1`
  Priority: `P1`
  Estimated effort: `12 hours`
  Dependencies: `T8.1.4, T9.1.4, T18.1.4, T19.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/telemetry/logging.py (create); atlas/telemetry/errors.py::ErrorCatalog (create); atlas/telemetry/redaction.py (create); atlas/core/runtime.py (extend)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace ad hoc diagnostic text with versioned structured records that correlate lifecycle work without leaking secrets, raw payloads, or unbounded path/cardinality data.
  * Restore or protect this invariant: Every major lifecycle, control, recovery, policy, and publication action has a stable code and correlation chain.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/telemetry/logging.py` (create: Configure structured records, context propagation, sinks, and failure isolation.); `atlas/telemetry/errors.py::ErrorCatalog` (create: Map stable error codes to safe messages, severity, and operator guidance.); `atlas/telemetry/redaction.py` (create: Centralize secret, content, path, and metadata redaction/bounding.); `atlas/core/runtime.py` (extend: Inject telemetry context without hidden global mutable state.)
  * Epic boundary: Canonical status, telemetry, health, and diagnostics — Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.
  * Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-018 requires: Operators need authoritative progress, blockers, provenance, and recovery evidence without reading raw SQLite or logs.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Replace ad hoc diagnostic text with versioned structured records that correlate lifecycle work without leaking secrets, raw payloads, or unbounded path/cardinality data.
  * Component dispositions: `atlas/telemetry/logging.py` (create: Configure structured records, context propagation, sinks, and failure isolation.); `atlas/telemetry/errors.py::ErrorCatalog` (create: Map stable error codes to safe messages, severity, and operator guidance.); `atlas/telemetry/redaction.py` (create: Centralize secret, content, path, and metadata redaction/bounding.); `atlas/core/runtime.py` (extend: Inject telemetry context without hidden global mutable state.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define a versioned log envelope with time, severity, code, message template, correlation/job/phase/attempt/work/control/event/request IDs, component, and bounded attributes.
  * Propagate context explicitly across async tasks, subprocess boundaries, outbox dispatch, and command requests.
  * Classify fields as safe, hashed/minimized, secret, content-derived, or prohibited; redact before serialization.
  * Define sink failure/backpressure behavior and ensure logging cannot fail authoritative transitions.

  Security and safety requirements

  * Prevent terminal/log injection, multiline spoofing, secret/token leakage, and raw malicious filename/content rendering.
  * Use allowlisted attributes and bounded lengths/counts; hash/minimize paths where full values are not required.
  * Keep stack traces and sensitive diagnostics behind explicit local diagnostic policy.
  * Test that attacker-controlled metadata cannot change severity, code, actor, or correlation fields.

  Edge cases and outliers to handle

  * Telemetry context missing after task restart.
  * Recursive logging failure or sink disk exhaustion.
  * Huge numbers of unique paths/work IDs.
  * Exception text includes secrets or binary data.

  Acceptance criteria (“done” definition)

  * Every major lifecycle, control, recovery, policy, and publication action has a stable code and correlation chain.
  * Redaction occurs before every configured sink and diagnostic export.
  * Telemetry sink failure cannot change job state or result.
  * Golden log schema is versioned and compatibility-tested.

  Testing plan

  * Envelope/schema golden tests.
  * Async/subprocess context propagation tests.
  * Injection/redaction/secret fixture tests.
  * Sink failure/backpressure tests.
  * High-cardinality bounding tests.
  * Error catalog completeness tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Envelope/schema golden tests., Async/subprocess context propagation tests., Injection/redaction/secret fixture tests., Sink failure/backpressure tests., High-cardinality bounding tests., Error catalog completeness tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T20.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/telemetry/logging.py, atlas/telemetry/errors.py::ErrorCatalog, atlas/telemetry/redaction.py, atlas/core/runtime.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 78: Implement bounded metrics and optional distributed tracing

  1.2 source task(s): `T20.1.2`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T20.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/telemetry/metrics.py::MetricsAdapter (create); atlas/telemetry/tracing.py::TraceAdapter (create); docs/operations/metrics-catalog.md (create); tests/telemetry/ (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Expose measurable throughput, latency, resource, queue, retry, recovery, and safety behavior without making telemetry required for correctness or creating unbounded cardinality.
  * Restore or protect this invariant: Metric names, units, label sets, and bounds are documented and schema-tested.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-018; REQ-008,REQ-013,REQ-029; PDF:p.18-19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/telemetry/metrics.py::MetricsAdapter` (create: Define counters, gauges, histograms, labels, and no-op/default adapter.); `atlas/telemetry/tracing.py::TraceAdapter` (create: Provide optional spans and context propagation around canonical operations.); `docs/operations/metrics-catalog.md` (create: Define names, units, labels, bounds, interpretation, and alert suggestions.); `tests/telemetry/` (create: Validate adapters, outage behavior, and cardinality policy.)
  * Epic boundary: Canonical status, telemetry, health, and diagnostics — Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-018: Provide canonical status, telemetry, health, and diagnostic bundles; evidence: REQ-008, REQ-013, REQ-029; Sections 15 and 23.
  * Canonical proposed files/interfaces: Create status/telemetry modules; extend CLI, runtime, persistence queries; documentation. / `StatusService`, `JobStatus`, telemetry adapter, `DiagnosticBundle`, health/readiness result.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-018 requires: Operators need authoritative progress, blockers, provenance, and recovery evidence without reading raw SQLite or logs.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Expose measurable throughput, latency, resource, queue, retry, recovery, and safety behavior without making telemetry required for correctness or creating unbounded cardinality.
  * Component dispositions: `atlas/telemetry/metrics.py::MetricsAdapter` (create: Define counters, gauges, histograms, labels, and no-op/default adapter.); `atlas/telemetry/tracing.py::TraceAdapter` (create: Provide optional spans and context propagation around canonical operations.); `docs/operations/metrics-catalog.md` (create: Define names, units, labels, bounds, interpretation, and alert suggestions.); `tests/telemetry/` (create: Validate adapters, outage behavior, and cardinality policy.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define a stable metric catalog for lifecycle states, phase/operation duration, throughput, bytes/entries, budgets, retries, checkpoints, claims, outbox, publications, and failures.
  * Allow only bounded labels such as phase, operation class, backend, result, and stable error code; never raw artifact IDs or paths by default.
  * Create optional traces linking command, coordinator, work item, backend, event, and publication spans through correlation IDs.
  * Document sampling, aggregation, clock, and retention limitations and keep durable evidence independent.

  Security and safety requirements

  * Metrics/traces may not contain raw content, secrets, credentials, or uncontrolled high-cardinality identifiers.
  * Exporter endpoints and credentials are optional deployment controls and least-privileged.
  * Telemetry failure is isolated and visible through bounded local counters/status.
  * Do not use model-generated labels or unvalidated plugin attributes.

  Edge cases and outliers to handle

  * Exporter unavailable or slow.
  * Clock skew produces negative/invalid duration.
  * Millions of work items threaten cardinality.
  * Trace context is malformed or untrusted.

  Acceptance criteria (“done” definition)

  * Metric names, units, label sets, and bounds are documented and schema-tested.
  * No mandatory lifecycle path depends on exporter success.
  * Load tests demonstrate bounded cardinality and memory use for representative workloads.
  * Trace removal/no-op mode leaves persisted semantics identical.

  Testing plan

  * Metric catalog/schema tests.
  * No-op/exporter conformance tests.
  * Exporter outage/slow sink tests.
  * Cardinality/load tests.
  * Trace context validation tests.
  * Semantic equivalence tests with telemetry disabled.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Metric catalog/schema tests., No-op/exporter conformance tests., Exporter outage/slow sink tests., Cardinality/load tests., Trace context validation tests., Semantic equivalence tests with telemetry disabled..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T20.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/telemetry/metrics.py::MetricsAdapter, atlas/telemetry/tracing.py::TraceAdapter, docs/operations/metrics-catalog.md, tests/telemetry/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
