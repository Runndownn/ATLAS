@BinReaper Production TODOs

## TODO

* [ ] TODO 106: Route consequential MCP actions through deterministic command and review gates

  1.2 source task(s): `T27.1.2`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T27.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/integrations/mcp.py (extend); atlas/service/commands.py (extend); atlas/security/agent_policy.py (create); tests/integrations/test_mcp_commands.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Permit optional pause/cancel/review/publication requests only when they use the same CommandService, policy, idempotency, expected-version, attribution, and confirmation controls as human clients.
  * Restore or protect this invariant: No MCP command bypasses CommandService, lifecycle guards, review policy, publication checks, or expected-version/idempotency.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `atlas/integrations/mcp.py` (extend: Add explicitly configured consequential command adapters.); `atlas/service/commands.py` (extend: Accept agent actor type and confirmation/policy context without weakening guards.); `atlas/security/agent_policy.py` (create: Map tool, actor, environment, subject, and side-effect class to allowed request behavior.); `tests/integrations/test_mcp_commands.py` (create: Exercise replay, stale state, prompt injection, confirmation, and authority assertions.)
  * Epic boundary: Bounded MCP and operator interfaces — Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.
  * Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-023 requires: Agent/UI convenience must not become an alternate provenance, policy, or promotion authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Permit optional pause/cancel/review/publication requests only when they use the same CommandService, policy, idempotency, expected-version, attribution, and confirmation controls as human clients.
  * Component dispositions: `atlas/integrations/mcp.py` (extend: Add explicitly configured consequential command adapters.); `atlas/service/commands.py` (extend: Accept agent actor type and confirmation/policy context without weakening guards.); `atlas/security/agent_policy.py` (create: Map tool, actor, environment, subject, and side-effect class to allowed request behavior.); `tests/integrations/test_mcp_commands.py` (create: Exercise replay, stale state, prompt injection, confirmation, and authority assertions.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Classify MCP tools by read, proposal, reversible control, review request, and external side effect; disable consequential classes by default.
  * Require deployment authorization, exact subject/state version, idempotency key, reason, policy evaluation, and explicit confirmation/approval for configured side effects.
  * Record requested versus accepted command and final authoritative outcome separately.
  * Never allow an AI actor to be the sole final promotion authority; it may submit a proposal/request for deterministic or human review.

  Security and safety requirements

  * Separate system policy/instructions from retrieved artifact/plugin text and never concatenate untrusted text into tool authorization.
  * Use actor/session/tool/model/provider IDs and audit denied/accepted/replayed/stale commands.
  * Prevent cross-job/tenant confused deputy behavior and tool-argument injection.
  * Limit request rate/cost/duration and revoke sessions/capabilities on suspicious behavior.

  Edge cases and outliers to handle

  * Artifact says to approve or publish itself.
  * Model repeats a stale command after timeout.
  * User confirmation changes subject/evidence before execution.
  * Agent session is revoked mid-request.

  Acceptance criteria (“done” definition)

  * No MCP command bypasses CommandService, lifecycle guards, review policy, publication checks, or expected-version/idempotency.
  * Prompt-injected artifact text cannot authorize or alter a tool action.
  * AI-only output cannot create an approved PromotionDecision.
  * Replay, stale state, revoked session, and changed confirmation return deterministic non-success outcomes.

  Testing plan

  * Authority-path integration tests.
  * Stored/indirect prompt-injection tests.
  * Replay/stale/confirmation race tests.
  * Cross-job/tenant confused-deputy tests.
  * Revocation/rate/cost-limit tests.
  * AI final-authority negative tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Authority-path integration tests., Stored/indirect prompt-injection tests., Replay/stale/confirmation race tests., Cross-job/tenant confused-deputy tests., Revocation/rate/cost-limit tests., AI final-authority negative tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T27.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/integrations/mcp.py, atlas/service/commands.py, atlas/security/agent_policy.py, tests/integrations/test_mcp_commands.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 107: Build an operator UI that preserves authority and uncertainty distinctions

  1.2 source task(s): `T27.1.3`
  Priority: `P3`
  Estimated effort: `16 hours`
  Dependencies: `T27.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `ui/ (create); atlas/api/rest.py (extend); docs/operations/operator-ui.md (create); tests/ui/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Render jobs, phases, attempts, progress, controls, provenance, findings, evidence, decisions, publications, health, and diagnostics without collapsing observed, inferred, proposed, approved, or published states.
  * Restore or protect this invariant: UI never labels a finding/proposal as evidence, a request as decision, or an attempt as verified publication.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `ui/` (create: Host the optional operator client with generated API types and secure rendering.); `atlas/api/rest.py` (extend: Expose UI-required bounded status/evidence/review/publication endpoints only.); `docs/operations/operator-ui.md` (create: Document deployment, roles, workflows, status semantics, and incidents.); `tests/ui/` (create: Validate authority labels, stale state, accessibility, encoding, and command paths.)
  * Epic boundary: Bounded MCP and operator interfaces — Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.
  * Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-023 requires: Agent/UI convenience must not become an alternate provenance, policy, or promotion authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Render jobs, phases, attempts, progress, controls, provenance, findings, evidence, decisions, publications, health, and diagnostics without collapsing observed, inferred, proposed, approved, or published states.
  * Component dispositions: `ui/` (create: Host the optional operator client with generated API types and secure rendering.); `atlas/api/rest.py` (extend: Expose UI-required bounded status/evidence/review/publication endpoints only.); `docs/operations/operator-ui.md` (create: Document deployment, roles, workflows, status semantics, and incidents.); `tests/ui/` (create: Validate authority labels, stale state, accessibility, encoding, and command paths.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Design views for job/phase/attempt/work progress, controls, blockers/recovery, artifact/provenance graph, findings/evidence, review, publications, events, health, and diagnostics.
  * Use generated versioned API contracts and expected-version/idempotency for all commands; refresh and surface stale data before confirmation.
  * Label observed, derived, inferred, proposed, evidence, approved/rejected/held, attempted, verified published, unknown, and degraded states distinctly.
  * Provide accessible keyboard/navigation/status/error behavior and bounded pagination for large jobs.

  Security and safety requirements

  * Encode all artifact/plugin/model/error text and sanitize any rich rendering; prevent XSS, URL injection, unsafe downloads, and clickjacking.
  * Use CSRF/session/authz/TLS/content-security deployment controls where exposed; never store secrets in browser storage.
  * Do not expose raw files/paths/secrets by default; mediated downloads require policy and audit.
  * Display denied/stale/unknown/reconciliation states rather than optimistic success.

  Edge cases and outliers to handle

  * Status changes during review form.
  * Finding contains HTML/terminal escape/huge text.
  * Publication outcome is unknown.
  * API compatibility mismatch or partial outage.

  Acceptance criteria (“done” definition)

  * UI never labels a finding/proposal as evidence, a request as decision, or an attempt as verified publication.
  * All commands traverse canonical APIs and reject stale/replayed input.
  * Hostile rendered content cannot execute or create unauthorized navigation/actions.
  * Accessibility, large-job performance, partial outage, and compatibility behavior are tested.

  Testing plan

  * Authority-label golden tests.
  * XSS/URL/content rendering tests.
  * Stale/replay command E2E tests.
  * Accessibility automated/manual checks.
  * Large-job pagination/performance tests.
  * API mismatch/partial outage tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Authority-label golden tests., XSS/URL/content rendering tests., Stale/replay command E2E tests., Accessibility automated/manual checks., Large-job pagination/performance tests., API mismatch/partial outage tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T27.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: ui/, atlas/api/rest.py, docs/operations/operator-ui.md, tests/ui/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 108: Resolve tenant, authentication, authorization, and deployment-governance scope

  1.2 source task(s): `T27.1.4`
  Priority: `P3`
  Estimated effort: `14 hours`
  Dependencies: `T27.1.2, T27.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `docs/decisions/deployment-identity-and-tenancy.md (create); atlas/security/interfaces.py (create); atlas/config/security.py (create); tests/security/test_deployment_identity_adapters.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Determine from real deployment requirements whether ATLAS needs single-operator local identity, team RBAC, tenant isolation, service identities, or external policy adapters without burdening the compact core prematurely.
  * Restore or protect this invariant: Deployment identity/tenancy requirements, non-goals, and decision authority are evidenced and approved.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-023; REQ-025,REQ-027,REQ-030; PDF:p.18,p.21,p.22,p.23,p.27.

  Where this applies

  * Primary affected components: `docs/decisions/deployment-identity-and-tenancy.md` (create: Record users, tenants, trust zones, consequential actions, alternatives, and decision.); `atlas/security/interfaces.py` (create: Define optional actor/authentication/authorization/policy adapter contracts only after decision.); `atlas/config/security.py` (create: Represent deployment adapter selection and safe local defaults.); `tests/security/test_deployment_identity_adapters.py` (create: Validate selected policy and no-adapter local behavior.)
  * Epic boundary: Bounded MCP and operator interfaces — Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-023: Expose MCP and operator UI only as bounded clients of canonical services; evidence: REQ-025, REQ-027, REQ-030; R-18.
  * Canonical proposed files/interfaces: Later `atlas/integrations/mcp.py`, optional UI project/adapter. / Versioned MCP tools/resources/prompts; UI API over REST/Status; bounded proposal records.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-023 requires: Agent/UI convenience must not become an alternate provenance, policy, or promotion authority.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Determine from real deployment requirements whether ATLAS needs single-operator local identity, team RBAC, tenant isolation, service identities, or external policy adapters without burdening the compact core prematurely.
  * Component dispositions: `docs/decisions/deployment-identity-and-tenancy.md` (create: Record users, tenants, trust zones, consequential actions, alternatives, and decision.); `atlas/security/interfaces.py` (create: Define optional actor/authentication/authorization/policy adapter contracts only after decision.); `atlas/config/security.py` (create: Represent deployment adapter selection and safe local defaults.); `tests/security/test_deployment_identity_adapters.py` (create: Validate selected policy and no-adapter local behavior.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Inventory deployment actors, service boundaries, data sensitivity, source/destination ownership, concurrent users, audit obligations, and tenant separation needs.
  * Classify actions: local harmless analysis, controls, plugin grants, review, publication, retention deletion, configuration, and administration.
  * Compare local OS identity, API gateway/IdP, RBAC/ABAC, tenant-scoped stores/content, and service identity adapters against requirements and cost.
  * Keep deterministic lifecycle/state/source/safety enforcement in core and define deployment auth/policy adapters only where justified.

  Security and safety requirements

  * Fail closed for consequential network-exposed operations when no required identity/policy adapter is configured.
  * Prevent tenant/job/source/content/publication cross-scope access and confused deputy behavior if multi-tenancy is selected.
  * Use external secret references, least privilege, revocation, audit, and break-glass policy with evidence.
  * Do not invent enterprise IAM requirements or claim isolation before tested deployment controls exist.

  Edge cases and outliers to handle

  * Single local user later migrates to team service.
  * One content identity is referenced by multiple tenants.
  * Service identity revoked during work.
  * Policy service unavailable or returns stale decision.

  Acceptance criteria (“done” definition)

  * Deployment identity/tenancy requirements, non-goals, and decision authority are evidenced and approved.
  * Selected adapters preserve core semantics and local mode remains safe and documented.
  * If multi-tenancy is required, isolation is modeled across state, content, events, caches, workers, diagnostics, and publications before implementation.
  * Auth/policy outage, revocation, and rollback behavior are deterministic and tested.

  Testing plan

  * Threat-model and requirement review.
  * Local no-adapter behavior tests.
  * Selected auth/policy adapter conformance tests.
  * Cross-scope/tenant negative tests if applicable.
  * Revocation/outage/stale-policy tests.
  * Migration/rollback decision drill.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Threat-model and requirement review., Local no-adapter behavior tests., Selected auth/policy adapter conformance tests., Cross-scope/tenant negative tests if applicable., Revocation/outage/stale-policy tests., Migration/rollback decision drill..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T27.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: docs/decisions/deployment-identity-and-tenancy.md, atlas/security/interfaces.py, atlas/config/security.py, tests/security/test_deployment_identity_adapters.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
