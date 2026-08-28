@BinReaper Production TODOs

## TODO

* [ ] TODO 85: Define the subprocess protocol and mediated artifact contract

  1.2 source task(s): `T22.1.1`
  Priority: `P2`
  Estimated effort: `14 hours`
  Dependencies: `T14.1.4, T15.1.4, T16.1.4, T18.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/subprocess.py::SubprocessBackend (create); atlas/execution/protocol.py (create); atlas/execution/artifact_access.py (extend); docs/plugins/subprocess-protocol.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create a minimal versioned protocol in which a plugin receives only declared immutable inputs and capability grants and returns bounded typed results without StateStore or source-root authority.
  * Restore or protect this invariant: Subprocess cannot receive StateStore credentials or undeclared source/workspace paths through the protocol/environment.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/execution/subprocess.py::SubprocessBackend` (create: Implement the backend contract and protocol lifecycle.); `atlas/execution/protocol.py` (create: Define handshake, request, progress, result, error, and cancellation messages.); `atlas/execution/artifact_access.py` (extend: Issue mediated read-only content/derived-artifact handles or copies.); `docs/plugins/subprocess-protocol.md` (create: Document compatibility, limits, capability model, and trust assumptions.)
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

  * Create a minimal versioned protocol in which a plugin receives only declared immutable inputs and capability grants and returns bounded typed results without StateStore or source-root authority.
  * Component dispositions: `atlas/execution/subprocess.py::SubprocessBackend` (create: Implement the backend contract and protocol lifecycle.); `atlas/execution/protocol.py` (create: Define handshake, request, progress, result, error, and cancellation messages.); `atlas/execution/artifact_access.py` (extend: Issue mediated read-only content/derived-artifact handles or copies.); `docs/plugins/subprocess-protocol.md` (create: Document compatibility, limits, capability model, and trust assumptions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define protocol major/minor version, plugin identity/digest, operation, inputs, grants, budgets, deadline, attempt/fencing context, progress, result, evidence, and errors.
  * Use length-delimited or equivalent framing with strict size/encoding/order rules; reject extra/ambiguous/duplicate fields according to version policy.
  * Provide read-only mediated content handles/copies and an attempt-owned output workspace; never expose StateStore credentials or unrestricted source paths.
  * Validate all output through the same typed analyzer/phase contracts before persistence.

  Security and safety requirements

  * Sanitize environment, current directory, inherited file descriptors/handles, locale, PATH, Python/module path, and secret variables.
  * Capability grants are explicit, attempt-scoped, least-privilege, non-transferable metadata; plugin text cannot self-grant.
  * Treat stdout/stderr/protocol bytes as untrusted and bounded; do not parse shell commands or unsafe serialization.
  * Authenticate/verify the configured executable or package digest according to plugin trust policy.

  Edge cases and outliers to handle

  * Protocol version mismatch or truncated frame.
  * Plugin emits stdout noise before handshake.
  * Input content disappears or handle expires.
  * Plugin fabricates another attempt/content/result identity.

  Acceptance criteria (“done” definition)

  * Subprocess cannot receive StateStore credentials or undeclared source/workspace paths through the protocol/environment.
  * Malformed or forged protocol messages fail the attempt without lifecycle mutation.
  * Equivalent trusted plugin results normalize identically in in-process and subprocess backends.
  * Protocol compatibility and capability negotiation are versioned and tested.

  Testing plan

  * Protocol codec/golden tests.
  * Malformed/truncated/fuzz tests.
  * Environment/fd/secret leakage tests.
  * Forged identity/grant negative tests.
  * In-process/subprocess conformance tests.
  * Large output/input-handle expiry tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Protocol codec/golden tests., Malformed/truncated/fuzz tests., Environment/fd/secret leakage tests., Forged identity/grant negative tests., In-process/subprocess conformance tests., Large output/input-handle expiry tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T22.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/subprocess.py::SubprocessBackend, atlas/execution/protocol.py, atlas/execution/artifact_access.py, docs/plugins/subprocess-protocol.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 86: Implement deterministic process lifecycle, timeout, and tree termination

  1.2 source task(s): `T22.1.2`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T22.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/process_supervisor.py (create); atlas/execution/subprocess.py (extend); atlas/recovery/reconcilers.py (extend); tests/execution/hostile_plugins/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Own launch, handshake, progress, cancellation, deadline, termination, reaping, and cleanup so a plugin crash or timeout becomes one fenced attempt outcome.
  * Restore or protect this invariant: Timeout/cancel kills and reaps the entire controlled process tree on supported platforms.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/execution/process_supervisor.py` (create: Manage process group/job object, lifecycle, deadlines, output limits, and termination escalation.); `atlas/execution/subprocess.py` (extend: Integrate supervisor, checkpoints/progress, and backend result mapping.); `atlas/recovery/reconcilers.py` (extend: Classify orphan/unknown subprocess state on restart.); `tests/execution/hostile_plugins/` (create: Provide synthetic crash, hang, fork, flood, and signal fixtures.)
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

  * Own launch, handshake, progress, cancellation, deadline, termination, reaping, and cleanup so a plugin crash or timeout becomes one fenced attempt outcome.
  * Component dispositions: `atlas/execution/process_supervisor.py` (create: Manage process group/job object, lifecycle, deadlines, output limits, and termination escalation.); `atlas/execution/subprocess.py` (extend: Integrate supervisor, checkpoints/progress, and backend result mapping.); `atlas/recovery/reconcilers.py` (extend: Classify orphan/unknown subprocess state on restart.); `tests/execution/hostile_plugins/` (create: Provide synthetic crash, hang, fork, flood, and signal fixtures.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Launch in a dedicated process group/session or platform job object and record robust process identity with attempt.
  * Enforce handshake/start/idle/total deadlines, cancellation, graceful termination grace, forced tree kill, wait/reap, and deterministic outcome mapping.
  * Bound stdout, stderr, protocol, child count, open handles, and retained diagnostics; truncate with explicit evidence.
  * On restart, never kill by PID alone; reconcile platform process identity and fenced attempt ownership.

  Security and safety requirements

  * Prevent process-tree escape where the supported platform primitive can enforce it; report reduced assurance otherwise.
  * Close inherited descriptors/handles and ensure child cannot signal/control unrelated processes.
  * Do not treat a successful exit code as valid until protocol result, identity, schema, and content/output verification pass.
  * Retain bounded crash evidence without core dumps or secret-bearing memory by default.

  Edge cases and outliers to handle

  * Child forks then parent exits.
  * Child ignores termination or floods output.
  * Cancellation races with valid result.
  * PID is reused after daemon restart.

  Acceptance criteria (“done” definition)

  * Timeout/cancel kills and reaps the entire controlled process tree on supported platforms.
  * Late or stale results cannot commit after fencing/cancellation.
  * Unsupported containment controls are explicit in status and release evidence.
  * No zombie, leaked handle, or unbounded output remains after hostile fixtures.

  Testing plan

  * Lifecycle state-machine tests.
  * Hang/fork/output-flood hostile tests.
  * Cancel/result race tests.
  * PID reuse/orphan restart tests.
  * Resource leak/reaping tests.
  * Platform-specific conformance tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Lifecycle state-machine tests., Hang/fork/output-flood hostile tests., Cancel/result race tests., PID reuse/orphan restart tests., Resource leak/reaping tests., Platform-specific conformance tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T22.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/process_supervisor.py, atlas/execution/subprocess.py, atlas/recovery/reconcilers.py, tests/execution/hostile_plugins/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 87: Enforce subprocess resource, network, tool, and secret policy

  1.2 source task(s): `T22.1.3`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T22.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/limits.py (create); atlas/execution/capabilities.py::CapabilityGrant (extend); atlas/security/plugin_policy.py (extend); docs/security/subprocess-enforcement-matrix.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Apply the unified resource budget and plugin capability policy using available OS controls while failing closed or visibly reducing assurance when enforcement is unavailable.
  * Restore or protect this invariant: Each subprocess attempt records requested, enforced, unavailable, and exceeded controls plus measured usage.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-020; REQ-022; PDF:p.17,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/execution/limits.py` (create: Translate hierarchical budgets to platform CPU, memory, process, file, and time controls.); `atlas/execution/capabilities.py::CapabilityGrant` (extend: Resolve filesystem, network, tool, and secret grants for one attempt.); `atlas/security/plugin_policy.py` (extend: Decide trusted/in-process versus subprocess eligibility and grant set.); `docs/security/subprocess-enforcement-matrix.md` (create: Record per-platform controls, gaps, and release claims.)
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

  * Apply the unified resource budget and plugin capability policy using available OS controls while failing closed or visibly reducing assurance when enforcement is unavailable.
  * Component dispositions: `atlas/execution/limits.py` (create: Translate hierarchical budgets to platform CPU, memory, process, file, and time controls.); `atlas/execution/capabilities.py::CapabilityGrant` (extend: Resolve filesystem, network, tool, and secret grants for one attempt.); `atlas/security/plugin_policy.py` (extend: Decide trusted/in-process versus subprocess eligibility and grant set.); `docs/security/subprocess-enforcement-matrix.md` (create: Record per-platform controls, gaps, and release claims.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Enforce or monitor wall time, CPU, memory, process/thread count, file descriptors, output bytes, workspace/temp bytes, and opened files.
  * Deny network and external tools by default; grant allowlisted endpoints/tools with resolved immutable executable identity and arguments contract.
  * Provide secrets only through explicit short-lived references/channels and never general environment inheritance.
  * Record each control as enforced, monitored-only, unavailable, or not requested and feed actual usage to `ResourceBudgetManager`.

  Security and safety requirements

  * Do not claim sandboxing from subprocess separation alone.
  * Canonicalize and validate executable/tool paths, arguments, environment, endpoint scope, and workspace before launch.
  * Prevent command injection by using argument arrays and typed tool adapters, never shell interpolation.
  * If a required control is unavailable, reject untrusted plugin execution or require an explicit trusted reduced-assurance policy.

  Edge cases and outliers to handle

  * Memory spike before monitor samples.
  * Plugin execs another binary or opens inherited network socket.
  * Tool path replaced after validation.
  * Secret reference expires or is read repeatedly.

  Acceptance criteria (“done” definition)

  * Each subprocess attempt records requested, enforced, unavailable, and exceeded controls plus measured usage.
  * Network/tools/secrets are absent unless explicitly granted by deterministic policy.
  * Required unavailable controls block untrusted execution rather than silently weakening policy.
  * Tool and command-injection tests show no shell interpretation of plugin-controlled values.

  Testing plan

  * CPU/memory/process/temp/output exhaustion tests.
  * Network deny/allow tests.
  * Tool replacement/argument injection tests.
  * Secret leakage/expiry tests.
  * Reduced-assurance policy tests.
  * Platform enforcement matrix verification.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: CPU/memory/process/temp/output exhaustion tests., Network deny/allow tests., Tool replacement/argument injection tests., Secret leakage/expiry tests., Reduced-assurance policy tests., Platform enforcement matrix verification..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T22.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/limits.py, atlas/execution/capabilities.py::CapabilityGrant, atlas/security/plugin_policy.py, docs/security/subprocess-enforcement-matrix.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
