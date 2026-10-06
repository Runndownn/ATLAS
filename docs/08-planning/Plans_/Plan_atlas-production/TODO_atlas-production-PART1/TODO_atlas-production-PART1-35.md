@BinReaper Production TODOs

## TODO

* [ ] TODO 103: Implement remote scheduling, result verification, cancellation, and fallback policy

  1.2 source task(s): `T26.1.3`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T26.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/execution/remote_scheduler.py (create); atlas/execution/remote.py (extend); atlas/recovery/reconcilers.py (extend); atlas/status/projection.py (extend)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Select eligible remote capacity within phase-internal work semantics, verify results before commit, and define loss/fallback behavior without changing phase order or duplicating side effects.
  * Restore or protect this invariant: One valid fenced result can commit for each work attempt.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29.

  Where this applies

  * Primary affected components: `atlas/execution/remote_scheduler.py` (create: Match WorkSpecs to compatible workers using bounded deterministic policy.); `atlas/execution/remote.py` (extend: Own assignment, lease, progress, cancel, result verification, and recovery mapping.); `atlas/recovery/reconcilers.py` (extend: Handle worker loss, transfer unknowns, stale result, and safe reassignment.); `atlas/status/projection.py` (extend: Show worker/lease/transfer/backend state without exposing secrets.)
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

  * Select eligible remote capacity within phase-internal work semantics, verify results before commit, and define loss/fallback behavior without changing phase order or duplicating side effects.
  * Component dispositions: `atlas/execution/remote_scheduler.py` (create: Match WorkSpecs to compatible workers using bounded deterministic policy.); `atlas/execution/remote.py` (extend: Own assignment, lease, progress, cancel, result verification, and recovery mapping.); `atlas/recovery/reconcilers.py` (extend: Handle worker loss, transfer unknowns, stale result, and safe reassignment.); `atlas/status/projection.py` (extend: Show worker/lease/transfer/backend state without exposing secrets.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Filter workers by protocol/runtime/plugin/capability/resource/data-locality compatibility and apply deterministic or explainable tie-breaking.
  * Persist assignment/lease before dispatch; verify authenticated result envelope, fencing, WorkSpec digest, output content hashes, schema, and budget evidence before commit.
  * Define cancellation/drain and local fallback/reassignment only for operations whose semantics and idempotency allow it.
  * Preserve work-item phase barrier and coordinator-owned aggregation/transition.

  Security and safety requirements

  * Scheduling metadata cannot grant capabilities beyond policy or leak sensitive source identity unnecessarily.
  * Reject stale worker, invalid signature, wrong WorkSpec/content, over-budget, or incompatible result.
  * Bound assignment/retry/transfer concurrency and protect against a malicious worker advertising infinite capacity.
  * Fallback cannot silently switch to a weaker isolation/trust backend.

  Edge cases and outliers to handle

  * Partition after assignment or after result upload.
  * Worker completes twice.
  * Cancel is lost and successor starts.
  * No compatible worker or capacity changes rapidly.

  Acceptance criteria (“done” definition)

  * One valid fenced result can commit for each work attempt.
  * Worker loss maps to deterministic wait/retry/reconcile/block behavior from operation semantics.
  * Fallback/reassignment is disabled for unsafe/unknown side effects and never weakens policy.
  * Remote execution preserves the same phase barriers, persistence, events, lineage, and status as local execution.

  Testing plan

  * Scheduling determinism/compatibility tests.
  * Partition/duplicate/stale result tests.
  * Cancel-loss/successor race tests.
  * Malicious capacity/capability negative tests.
  * Local/remote semantic differential tests.
  * High-volume assignment/backpressure tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Scheduling determinism/compatibility tests., Partition/duplicate/stale result tests., Cancel-loss/successor race tests., Malicious capacity/capability negative tests., Local/remote semantic differential tests., High-volume assignment/backpressure tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T26.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/execution/remote_scheduler.py, atlas/execution/remote.py, atlas/recovery/reconcilers.py, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 104: Gate distributed execution with chaos, security, load, and operational evidence

  1.2 source task(s): `T26.1.4`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T26.1.2, T26.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/distributed/ (create); benchmarks/remote_workers/ (create); scripts/run_remote_chaos_matrix.py (create); docs/operations/remote-workers-runbook.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Demonstrate that remote execution adds measurable value and preserves semantics under partitions, worker loss, skew, incompatibility, malicious behavior, and sustained load before deployment.
  * Restore or protect this invariant: Remote backend passes all local backend/state/recovery/lineage conformance suites.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-022; REQ-026,REQ-030; PDF:p.19,p.21,p.27,p.29.

  Where this applies

  * Primary affected components: `tests/distributed/` (create: Host network, worker, protocol, security, and semantic conformance scenarios.); `benchmarks/remote_workers/` (create: Measure transfer, queue, execution, recovery, throughput, and operational cost.); `scripts/run_remote_chaos_matrix.py` (create: Produce machine-readable partition/loss/replay/upgrade evidence.); `docs/operations/remote-workers-runbook.md` (create: Define rollout, drain, incident, revocation, recovery, and rollback.)
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

  * Demonstrate that remote execution adds measurable value and preserves semantics under partitions, worker loss, skew, incompatibility, malicious behavior, and sustained load before deployment.
  * Component dispositions: `tests/distributed/` (create: Host network, worker, protocol, security, and semantic conformance scenarios.); `benchmarks/remote_workers/` (create: Measure transfer, queue, execution, recovery, throughput, and operational cost.); `scripts/run_remote_chaos_matrix.py` (create: Produce machine-readable partition/loss/replay/upgrade evidence.); `docs/operations/remote-workers-runbook.md` (create: Define rollout, drain, incident, revocation, recovery, and rollback.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Test partitions at dispatch/heartbeat/result/ack, worker kill/restart, duplicate delivery, stale result, clock skew, protocol/plugin mismatch, artifact corruption, and control-plane outage.
  * Run malicious-worker scenarios for forged identities/results, capability overclaim, data access, resource reporting, and replay.
  * Benchmark against local execution including transfer overhead, utilization, throughput, recovery time, event/database pressure, and operator burden.
  * Progressively roll out by operation/plugin with canary, drain, fallback rules, and a local rollback path where safe.

  Security and safety requirements

  * Use isolated synthetic infrastructure and credentials; do not expose production stores or payloads.
  * Require service identity revocation, artifact-token revocation/expiry, audit retention, and incident containment evidence.
  * A chaos test may not silently bypass unknown-outcome or publication safeguards.
  * Document tenant isolation as unresolved/optional until a deployment requires it.

  Edge cases and outliers to handle

  * Control plane and workers partition asymmetrically.
  * Upgrade leaves mixed protocol/plugin versions.
  * Remote path is slower and less reliable than local.
  * Rollback occurs with leased in-flight work.

  Acceptance criteria (“done” definition)

  * Remote backend passes all local backend/state/recovery/lineage conformance suites.
  * Chaos matrix demonstrates stale fencing and no duplicate authoritative effects.
  * Benchmark and operations evidence justify distributed complexity for a defined workload.
  * Drain/rollback/revocation drill handles in-flight work without alternate authority.

  Testing plan

  * Network chaos/fault tests.
  * Malicious worker security tests.
  * Mixed-version/upgrade tests.
  * Load/soak/transfer benchmarks.
  * Canary/drain/rollback drills.
  * Evidence manifest and independent review.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Network chaos/fault tests., Malicious worker security tests., Mixed-version/upgrade tests., Load/soak/transfer benchmarks., Canary/drain/rollback drills., Evidence manifest and independent review..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T26.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: tests/distributed/, benchmarks/remote_workers/, scripts/run_remote_chaos_matrix.py, docs/operations/remote-workers-runbook.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 105: Expose read-only and proposal-only MCP resources and tools

  1.2 source task(s): `T27.1.1`
  Priority: `P3`
  Estimated effort: `14 hours`
  Dependencies: `T17.1.4, T19.1.4, T20.1.4, T21.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/integrations/mcp.py (create); atlas/models/proposals.py::AnalysisProposal (create); docs/integrations/mcp.md (create); tests/integrations/test_mcp_read_tools.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide versioned MCP resources/tools for status, lineage, evidence, and bounded analytical proposals without direct lifecycle, filesystem, policy, review, or publication authority.
  * Restore or protect this invariant: MCP read/proposal tools cannot mutate lifecycle state, safety records, evidence authority, decisions, or publications.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/integrations/mcp.py` (create: Implement optional MCP server adapter over status/evidence/lineage/proposal services.); `atlas/models/proposals.py::AnalysisProposal` (create: Persist bounded non-authoritative model/agent proposals and provenance.); `docs/integrations/mcp.md` (create: Document tool semantics, trust boundaries, configuration, and disabled-by-default behavior.); `tests/integrations/test_mcp_read_tools.py` (create: Validate schemas, authority, hostile content, and compatibility.)
  * Epic boundary: Bounded MCP and operator interfaces — Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.
  * Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-023 requires: Agent/UI convenience must not become an alternate provenance, policy, or promotion authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Provide versioned MCP resources/tools for status, lineage, evidence, and bounded analytical proposals without direct lifecycle, filesystem, policy, review, or publication authority.
  * Component dispositions: `atlas/integrations/mcp.py` (create: Implement optional MCP server adapter over status/evidence/lineage/proposal services.); `atlas/models/proposals.py::AnalysisProposal` (create: Persist bounded non-authoritative model/agent proposals and provenance.); `docs/integrations/mcp.md` (create: Document tool semantics, trust boundaries, configuration, and disabled-by-default behavior.); `tests/integrations/test_mcp_read_tools.py` (create: Validate schemas, authority, hostile content, and compatibility.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Expose read-only job/status, artifact lineage, structural/evidence summaries, capability catalog, and proposal submission with strict schemas and pagination.
  * Label all model/agent output as proposed/inferred, record model/provider/prompt/tool/config/input evidence versions, and keep it separate from findings/evidence/decisions unless deterministic services accept it.
  * Use canonical service calls and return stable IDs/references rather than raw unrestricted files/content.
  * Make MCP an optional package/process that can be removed without core behavior changes.

  Security and safety requirements

  * Treat artifact text, finding text, external resources, prompts, and model output as untrusted data, never instructions to the server.
  * Grant least-privilege tool set and disable filesystem/network/command/publication capabilities by default.
  * Apply output encoding, content/size limits, secret/path redaction, rate/resource limits, and actor/session attribution.
  * Reject tool enumeration or arguments that request internal credentials, private APIs, StateStore access, or hidden capabilities.

  Edge cases and outliers to handle

  * Prompt injection embedded in archive metadata/finding/evidence.
  * Model hallucinates IDs or requests unsupported tool.
  * Very large lineage/evidence result.
  * Model/provider timeout or partial proposal.

  Acceptance criteria (“done” definition)

  * MCP read/proposal tools cannot mutate lifecycle state, safety records, evidence authority, decisions, or publications.
  * Every proposal is visibly non-authoritative and provenance-versioned.
  * Hostile artifact text cannot create an unrequested tool call or expand capabilities.
  * Removing/disabling MCP leaves core semantics and data readable.

  Testing plan

  * Tool/resource schema tests.
  * Prompt-injection and confused-deputy negative tests.
  * Hallucinated/stale ID tests.
  * Output encoding/redaction/size tests.
  * Model outage/timeout tests.
  * Core-without-MCP conformance tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Tool/resource schema tests., Prompt-injection and confused-deputy negative tests., Hallucinated/stale ID tests., Output encoding/redaction/size tests., Model outage/timeout tests., Core-without-MCP conformance tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T27.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/integrations/mcp.py, atlas/models/proposals.py::AnalysisProposal, docs/integrations/mcp.md, tests/integrations/test_mcp_read_tools.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
