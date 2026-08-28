@BinReaper Production TODOs

## TODO

* [ ] TODO 73: Define the daemon lifecycle, configuration, and ownership contract

  1.2 source task(s): `T19.1.1`
  Priority: `P1`
  Estimated effort: `12 hours`
  Dependencies: `T5.1.4, T9.1.4, T18.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/service/daemon.py::AtlasDaemon (create); atlas/service/config.py::DaemonConfig (create); atlas/core/runtime.py (refactor); docs/operations/daemon.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Specify a single local service that owns active execution, recovers durable jobs, and exposes explicit startup, readiness, drain, shutdown, and embedded-mode semantics.
  * Restore or protect this invariant: Readiness is false until store, migration, recovery, and ownership checks succeed.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/service/daemon.py::AtlasDaemon` (create: Own service lifecycle, claim loop, recovery startup, drain, and shutdown.); `atlas/service/config.py::DaemonConfig` (create: Define typed local service, polling, lease, shutdown, and IPC configuration.); `atlas/core/runtime.py` (refactor: Separate composition from process lifetime and provide daemon/embedded construction modes.); `docs/operations/daemon.md` (create: Document ownership, service modes, installation, and failure behavior.)
  * Epic boundary: Long-running local runtime ownership — Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.
  * Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-017 requires: A CLI process cannot durably own jobs or honor controls from another process; hydrating private `_jobs` is not control.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Specify a single local service that owns active execution, recovers durable jobs, and exposes explicit startup, readiness, drain, shutdown, and embedded-mode semantics.
  * Component dispositions: `atlas/service/daemon.py::AtlasDaemon` (create: Own service lifecycle, claim loop, recovery startup, drain, and shutdown.); `atlas/service/config.py::DaemonConfig` (create: Define typed local service, polling, lease, shutdown, and IPC configuration.); `atlas/core/runtime.py` (refactor: Separate composition from process lifetime and provide daemon/embedded construction modes.); `docs/operations/daemon.md` (create: Document ownership, service modes, installation, and failure behavior.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define states `STARTING`, `RECOVERING`, `READY`, `DRAINING`, `STOPPING`, `STOPPED`, and `FAILED` with deterministic readiness semantics.
  * Define one authoritative owner of job advancement per deployment and an explicit embedded-mode ownership contract for tests/library use.
  * Run migration/integrity/recovery checks before readiness and stop claiming work during drain.
  * Define local IPC or database-mediated command access without opening a network listener by default.

  Security and safety requirements

  * Run under a least-privileged local account with restricted database, workspace, configuration, and IPC permissions.
  * Reject insecure socket/pipe paths, world-writable parent directories, and symlinked service state.
  * Attribute startup/shutdown/control actors and avoid logging secrets or raw source data.
  * Embedded mode cannot run concurrently with a daemon against the same writable store unless claims/fencing make it safe.

  Edge cases and outliers to handle

  * Two daemon processes start simultaneously.
  * Host sleeps longer than lease duration.
  * Migration or recovery fails during startup.
  * Shutdown receives repeated or conflicting signals.

  Acceptance criteria (“done” definition)

  * Readiness is false until store, migration, recovery, and ownership checks succeed.
  * Only one valid local owner can advance an attempt.
  * Drain stops new claims while allowing documented safe completion/cancellation behavior.
  * Embedded and daemon modes use identical lifecycle/state/policy services.

  Testing plan

  * Daemon state-machine unit tests.
  * Competing-start integration tests.
  * Startup migration/recovery failure tests.
  * Permission/symlink negative tests.
  * Drain/shutdown signal tests.
  * Embedded/daemon semantic conformance tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Daemon state-machine unit tests., Competing-start integration tests., Startup migration/recovery failure tests., Permission/symlink negative tests., Drain/shutdown signal tests., Embedded/daemon semantic conformance tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T19.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/service/daemon.py::AtlasDaemon, atlas/service/config.py::DaemonConfig, atlas/core/runtime.py, docs/operations/daemon.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 74: Implement durable claims, leases, heartbeats, and fenced execution

  1.2 source task(s): `T19.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T19.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/claims.py::JobClaim (create); atlas/service/claims.py::ClaimService (create); atlas/core/coordinator.py (extend); atlas/schema/migrations/*_claims.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Allow the daemon to discover runnable work and acquire time-bounded authority that stale processes cannot use to commit results.
  * Restore or protect this invariant: Two daemons cannot validly own or commit the same attempt.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/models/claims.py::JobClaim` (create: Represent owner, lease, heartbeat, fencing token, state version, and release reason.); `atlas/service/claims.py::ClaimService` (create: Acquire, renew, release, expire, and query claims transactionally.); `atlas/core/coordinator.py` (extend: Require valid claim/fencing token for attempt advancement and result commit.); `atlas/schema/migrations/*_claims.sql` (create: Persist claims, heartbeat history, and fencing generations.)
  * Epic boundary: Long-running local runtime ownership — Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.
  * Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-017 requires: A CLI process cannot durably own jobs or honor controls from another process; hydrating private `_jobs` is not control.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Allow the daemon to discover runnable work and acquire time-bounded authority that stale processes cannot use to commit results.
  * Component dispositions: `atlas/models/claims.py::JobClaim` (create: Represent owner, lease, heartbeat, fencing token, state version, and release reason.); `atlas/service/claims.py::ClaimService` (create: Acquire, renew, release, expire, and query claims transactionally.); `atlas/core/coordinator.py` (extend: Require valid claim/fencing token for attempt advancement and result commit.); `atlas/schema/migrations/*_claims.sql` (create: Persist claims, heartbeat history, and fencing generations.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Select runnable jobs with deterministic ordering and transactionally acquire one claim with monotonic fencing generation.
  * Renew before expiry, stop authority on failed renewal, and persist release/expiry reasons.
  * Require claim and attempt fencing tokens at every authoritative transition and side-effect result commit.
  * Recover expired claims only after operation-specific reconciliation; never steal an active unknown effect.

  Security and safety requirements

  * Treat claim identity as authority metadata, not a bearer secret exposed to plugins or clients.
  * Reject stale, forged, cross-job, or lower-generation tokens.
  * Bound polling/renewal to avoid database denial of service and thundering herds.
  * Audit claim acquisition, renewal failure, expiry, stale result rejection, and recovery action.

  Edge cases and outliers to handle

  * Database lock prevents heartbeat but work still runs.
  * Lease expires during slow external call.
  * Host clock changes.
  * Stale daemon reports a late success after a successor attempt begins.

  Acceptance criteria (“done” definition)

  * Two daemons cannot validly own or commit the same attempt.
  * A lost lease immediately removes authority at the next guarded boundary.
  * Stale results are rejected and retained as diagnostic evidence.
  * Claim recovery follows operation semantics and never blindly re-executes an unknown effect.

  Testing plan

  * Claim transaction/concurrency tests.
  * Lease expiry/renewal tests.
  * Stale/forged token negative tests.
  * Clock/long-call tests.
  * Late-result fencing tests.
  * Recovery-after-expiry tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Claim transaction/concurrency tests., Lease expiry/renewal tests., Stale/forged token negative tests., Clock/long-call tests., Late-result fencing tests., Recovery-after-expiry tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T19.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/claims.py::JobClaim, atlas/service/claims.py::ClaimService, atlas/core/coordinator.py, atlas/schema/migrations/*_claims.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 75: Route CLI and Python controls through canonical command and status services

  1.2 source task(s): `T19.1.3`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T19.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/service/commands.py::CommandService (create); atlas/status/service.py::StatusService (create); atlas/cli.py (refactor); atlas/__init__.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Remove CLI hydration and private runtime mutation by making foreground, daemon, Python, and future API clients use the same typed command and status contracts.
  * Restore or protect this invariant: A separate CLI process can control a daemon-owned job without private runtime mutation.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-017; REQ-014,REQ-015; PDF:p.14,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/service/commands.py::CommandService` (create: Validate and persist submit/pause/resume/cancel/retry/reconcile/review commands.); `atlas/status/service.py::StatusService` (create: Read authoritative projections without mutating runtime state.); `atlas/cli.py` (refactor: Become a client of command/status services while retaining documented verbs and output modes.); `atlas/__init__.py` (extend: Expose supported Python service interfaces and compatibility shims.)
  * Epic boundary: Long-running local runtime ownership — Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-017: Add a long-running local daemon as the authoritative active-job owner; evidence: GAP-007, REQ-014, REQ-015; README remaining limitation on process-local controls.
  * Canonical proposed files/interfaces: Create `atlas/service/daemon.py`; refactor `atlas/cli.py`, runtime/coordinator; add claim/lease tables as needed. / `AtlasDaemon`, `JobClaim`, `CommandService`, local IPC choice or database-mediated commands; unchanged public CLI verbs.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-017 requires: A CLI process cannot durably own jobs or honor controls from another process; hydrating private `_jobs` is not control.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Remove CLI hydration and private runtime mutation by making foreground, daemon, Python, and future API clients use the same typed command and status contracts.
  * Component dispositions: `atlas/service/commands.py::CommandService` (create: Validate and persist submit/pause/resume/cancel/retry/reconcile/review commands.); `atlas/status/service.py::StatusService` (create: Read authoritative projections without mutating runtime state.); `atlas/cli.py` (refactor: Become a client of command/status services while retaining documented verbs and output modes.); `atlas/__init__.py` (extend: Expose supported Python service interfaces and compatibility shims.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define versioned commands with actor, idempotency key, expected state/version, reason, and request/correlation IDs.
  * Persist command acceptance/rejection and let the daemon/coordinator apply controls at valid state/safe-point boundaries.
  * Preserve existing CLI verbs through a compatibility window; add explicit foreground/daemon connection behavior.
  * Remove access to private `_jobs` or orchestrator handler maps from CLI and public Python surfaces.

  Security and safety requirements

  * Validate all fields and reject replay, stale state version, unauthorized deployment action, and lifecycle bypass.
  * Separate event notifications from commands; no event envelope can be deserialized as an accepted command.
  * Use local IPC/database permissions and actor attribution; no implicit trust from process name or transport.
  * Keep raw paths/content out of status by default and apply stable redaction rules.

  Edge cases and outliers to handle

  * Command submitted while daemon drains or is offline.
  * Same idempotency key with different payload.
  * Legacy CLI expects immediate foreground completion.
  * Status read sees partially migrated or corrupted record.

  Acceptance criteria (“done” definition)

  * A separate CLI process can control a daemon-owned job without private runtime mutation.
  * Equivalent CLI/Python commands produce identical persisted command and lifecycle results.
  * Replayed or stale commands return deterministic prior result/conflict.
  * Compatibility behavior and deprecation window are documented and tested.

  Testing plan

  * Command schema/unit tests.
  * CLI/Python equivalence tests.
  * Cross-process pause/resume/cancel tests.
  * Replay/stale-version negative tests.
  * Daemon-offline/draining tests.
  * Legacy CLI compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Command schema/unit tests., CLI/Python equivalence tests., Cross-process pause/resume/cancel tests., Replay/stale-version negative tests., Daemon-offline/draining tests., Legacy CLI compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T19.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/service/commands.py::CommandService, atlas/status/service.py::StatusService, atlas/cli.py, atlas/__init__.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
