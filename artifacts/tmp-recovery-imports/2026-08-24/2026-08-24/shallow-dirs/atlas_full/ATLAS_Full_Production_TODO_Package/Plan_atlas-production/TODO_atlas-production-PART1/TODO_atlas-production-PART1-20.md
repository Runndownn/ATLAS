@BinReaper Production TODOs

## TODO

* [ ] TODO 58: Implement the trusted `InProcessBackend`

  1.2 source task(s): `T15.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T15.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/inprocess.py::InProcessBackend (create); atlas/core/runtime.py (extend); atlas/plugins/registry.py (extend)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Run bundled trusted handlers through the same backend contract, context, deadlines, progress, and result normalization later isolation backends must satisfy.
  * Restore or protect this invariant: A bundled analyzer produces identical normalized findings through WorkSpec/WorkResult.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21.

  Where this applies

  * Primary affected components: `atlas/execution/inprocess.py::InProcessBackend` (create: Execute approved factories in the current process.); `atlas/core/runtime.py` (extend: Register backend and approved handlers deterministically.); `atlas/plugins/registry.py` (extend: Resolve factories by frozen descriptor snapshot.)
  * Epic boundary: ExecutionBackend contracts and trusted in-process execution — Separate lifecycle authority from execution location using immutable WorkSpec/WorkResult contracts and a conformance-tested trusted backend.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.
  * Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-014 requires: A stable work/result contract is required before isolation or remote execution; the backend must never own lifecycle state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Run bundled trusted handlers through the same backend contract, context, deadlines, progress, and result normalization later isolation backends must satisfy.
  * Component dispositions: `atlas/execution/inprocess.py::InProcessBackend` (create: Execute approved factories in the current process.); `atlas/core/runtime.py` (extend: Register backend and approved handlers deterministically.); `atlas/plugins/registry.py` (extend: Resolve factories by frozen descriptor snapshot.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Resolve approved operation/plugin factory from frozen registries and create mediated context from WorkSpec.
  * Execute asynchronously with deadline/cancellation propagation and capture normalized result/usage/diagnostics.
  * Prevent handler access to runtime globals, raw StateStore, source roots, or unrestricted workspace paths through provided interfaces.
  * Return WorkResult without committing lifecycle state.

  Security and safety requirements

  * Only explicitly trusted policy-approved code runs in process.
  * Sanitize exception diagnostics and bound traceback/log output.
  * Cancellation and timeout cannot leave coordinator locks or partial authoritative writes.
  * Global mutable registries are frozen after composition.

  Edge cases and outliers to handle

  * Handler blocks event loop or ignores cancellation.
  * Handler raises BaseException or process-level error.
  * Registry changes during execution.
  * Handler returns outputs after deadline.

  Acceptance criteria (“done” definition)

  * A bundled analyzer produces identical normalized findings through WorkSpec/WorkResult.
  * Backend has no direct persistence/lifecycle mutation capability.
  * Timeout/cancel outcomes are explicit and later recovery-classifiable.
  * Registry and policy versions used are echoed and validated.

  Testing plan

  * Backend unit tests.
  * Trusted analyzer integration tests.
  * Cancellation/deadline tests.
  * Blocking/exception diagnostics tests.
  * Registry freeze/version tests.
  * Architecture tests for forbidden dependencies.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Backend unit tests., Trusted analyzer integration tests., Cancellation/deadline tests., Blocking/exception diagnostics tests., Registry freeze/version tests., Architecture tests for forbidden dependencies..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T15.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/inprocess.py::InProcessBackend, atlas/core/runtime.py, atlas/plugins/registry.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 59: Implement coordinator-side result validation and commit

  1.2 source task(s): `T15.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T15.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/lifecycle.py::accept_work_result (create); atlas/execution/validation.py (create); atlas/persistence/repositories/work_results.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Validate every WorkResult against attempt state, fencing, exact WorkSpec, schemas, budgets, output integrity, and cancellation before accepting findings or transitioning state.
  * Restore or protect this invariant: Only fully validated current results can change attempt/phase state.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21.

  Where this applies

  * Primary affected components: `atlas/core/lifecycle.py::accept_work_result` (create: Own result validation and authoritative commit.); `atlas/execution/validation.py` (create: Validate spec/result/output/budget bindings.); `atlas/persistence/repositories/work_results.py` (create: Persist accepted/rejected result evidence.)
  * Epic boundary: ExecutionBackend contracts and trusted in-process execution — Separate lifecycle authority from execution location using immutable WorkSpec/WorkResult contracts and a conformance-tested trusted backend.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.
  * Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-014 requires: A stable work/result contract is required before isolation or remote execution; the backend must never own lifecycle state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Validate every WorkResult against attempt state, fencing, exact WorkSpec, schemas, budgets, output integrity, and cancellation before accepting findings or transitioning state.
  * Component dispositions: `atlas/core/lifecycle.py::accept_work_result` (create: Own result validation and authoritative commit.); `atlas/execution/validation.py` (create: Validate spec/result/output/budget bindings.); `atlas/persistence/repositories/work_results.py` (create: Persist accepted/rejected result evidence.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Load expected attempt/work/spec digest and compare all echoed authority fields and fencing token.
  * Validate result schema, status, deadlines, usage, finding limits, output manifest, content identities, and workspace ownership.
  * Persist accepted or rejected result evidence, then invoke guarded attempt/phase transition in one transaction/event path.
  * Make duplicate identical results idempotent and conflicting duplicates/stale results explicit.

  Security and safety requirements

  * Never trust backend success, paths, byte counts, or hashes without core verification.
  * Rejected results cannot publish outputs, findings, or lifecycle changes.
  * Diagnostics are bounded/redacted and retained for incident review.
  * Cancellation or expired authority wins over late success unless deterministic reconciliation proves otherwise.

  Edge cases and outliers to handle

  * Identical result redelivered.
  * Conflicting result with same idempotency key.
  * Stale success after retry or cancel.
  * Output exists but usage or manifest exceeds budget.

  Acceptance criteria (“done” definition)

  * Only fully validated current results can change attempt/phase state.
  * Duplicate identical results have one authoritative effect.
  * Stale/malformed/conflicting results are retained and rejected with stable codes.
  * Output integrity and budgets are verified before downstream use.

  Testing plan

  * Validation unit/property tests.
  * Duplicate/conflicting result tests.
  * Stale fencing/cancel tests.
  * Output manifest corruption tests.
  * Budget overrun tests.
  * Transaction/event atomicity integration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Validation unit/property tests., Duplicate/conflicting result tests., Stale fencing/cancel tests., Output manifest corruption tests., Budget overrun tests., Transaction/event atomicity integration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T15.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/lifecycle.py::accept_work_result, atlas/execution/validation.py, atlas/persistence/repositories/work_results.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 60: Create the reusable backend conformance and fault suite

  1.2 source task(s): `T15.1.4`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T15.1.2, T15.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/execution/conformance.py (create); tests/execution/fixtures/ (create); atlas/execution/testing.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Define one test contract that every in-process, subprocess, local-pool, and remote backend must pass before it can execute governed work.
  * Restore or protect this invariant: InProcessBackend passes every applicable mandatory case.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-014; REQ-022,REQ-030; PDF:p.17,p.19-21.

  Where this applies

  * Primary affected components: `tests/execution/conformance.py` (create: Host backend-neutral behavior and failure tests.); `tests/execution/fixtures/` (create: Provide deterministic plugins/specs/results/faults.); `atlas/execution/testing.py` (create: Expose test-only backend harness utilities.)
  * Epic boundary: ExecutionBackend contracts and trusted in-process execution — Separate lifecycle authority from execution location using immutable WorkSpec/WorkResult contracts and a conformance-tested trusted backend.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-014: Separate lifecycle semantics from execution location with ExecutionBackend; evidence: REQ-022, REQ-025, REQ-030; ADR-008.
  * Canonical proposed files/interfaces: Create `atlas/execution/base.py`, `atlas/execution/inprocess.py`; integrate coordinator/plugins; later `subprocess.py` in AT-020. / `ExecutionBackend.submit/cancel/health`, `WorkSpec`, `WorkResult`, `BackendCapabilities`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-014 requires: A stable work/result contract is required before isolation or remote execution; the backend must never own lifecycle state.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Define one test contract that every in-process, subprocess, local-pool, and remote backend must pass before it can execute governed work.
  * Component dispositions: `tests/execution/conformance.py` (create: Host backend-neutral behavior and failure tests.); `tests/execution/fixtures/` (create: Provide deterministic plugins/specs/results/faults.); `atlas/execution/testing.py` (create: Expose test-only backend harness utilities.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Test spec acceptance, result echo/schema, cancellation, deadline, progress, resource reporting, duplicate submission, stale fencing, output mediation, and health.
  * Inject backend crash/loss, malformed result, delayed result, partial output, cancellation race, and unavailable capability.
  * Compare normalized result semantics across backends for the same deterministic fixture.
  * Publish required versus platform-optional conformance cases and unsupported-control evidence.

  Security and safety requirements

  * Fixtures remain inert, bounded, and cannot access operator files/network.
  * A backend cannot skip mandatory authority/isolation tests because a control is inconvenient.
  * Platform skips require explicit capability evidence and affect deployment claims.
  * Conformance logs/fixtures contain no secrets.

  Edge cases and outliers to handle

  * Backend accepts duplicate spec concurrently.
  * Cancellation acknowledgement is lost.
  * Process/backend disappears after output write before result.
  * Unsupported CPU/memory control on one OS.

  Acceptance criteria (“done” definition)

  * InProcessBackend passes every applicable mandatory case.
  * The suite can be reused unchanged by subprocess and remote backends.
  * Unsupported controls are reported and block claims that they are enforced.
  * Fault cases produce deterministic coordinator outcomes.

  Testing plan

  * Backend conformance matrix.
  * Deterministic cross-backend result comparison.
  * Crash/loss/cancel fault tests.
  * Stale/duplicate submission tests.
  * Isolation/output mediation tests.
  * Platform capability reporting tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Backend conformance matrix., Deterministic cross-backend result comparison., Crash/loss/cancel fault tests., Stale/duplicate submission tests., Isolation/output mediation tests., Platform capability reporting tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T15.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/execution/conformance.py, tests/execution/fixtures/, atlas/execution/testing.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
