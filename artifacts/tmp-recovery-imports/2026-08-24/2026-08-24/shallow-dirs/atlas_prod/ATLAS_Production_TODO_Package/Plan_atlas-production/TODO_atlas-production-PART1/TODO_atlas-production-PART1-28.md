@BinReaper Production TODOs

## TODO

* [ ] TODO 82: Implement REST v1 and generate the OpenAPI contract

  1.2 source task(s): `T21.1.2`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T21.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/api/rest.py (create); atlas/api/dependencies.py (create); openapi/atlas-v1.yaml (create); tests/api/ (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide an optional HTTP adapter for commands, status, evidence, lineage, and health without embedding lifecycle authority or mandatory multi-user IAM in the core.
  * Restore or protect this invariant: REST and CLI/Python commands converge on the same persisted result for equivalent requests.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/api/rest.py` (create: Host REST v1 routes and adapter lifecycle.); `atlas/api/dependencies.py` (create: Inject command/status/evidence services and optional auth/rate-limit adapters.); `openapi/atlas-v1.yaml` (create: Generate and retain the versioned public contract.); `tests/api/` (create: Validate schema, equivalence, security, and failure behavior.)
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

  * Provide an optional HTTP adapter for commands, status, evidence, lineage, and health without embedding lifecycle authority or mandatory multi-user IAM in the core.
  * Component dispositions: `atlas/api/rest.py` (create: Host REST v1 routes and adapter lifecycle.); `atlas/api/dependencies.py` (create: Inject command/status/evidence services and optional auth/rate-limit adapters.); `openapi/atlas-v1.yaml` (create: Generate and retain the versioned public contract.); `tests/api/` (create: Validate schema, equivalence, security, and failure behavior.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Expose bounded endpoints for command submission/results, job list/status, events/evidence/lineage reads, health/readiness, and API schema.
  * Use canonical error objects, request/correlation IDs, idempotency, conditional expected-version/ETag semantics, pagination, and content negotiation.
  * Keep server startup/configuration optional and disabled by default for local library/CLI use.
  * Generate OpenAPI from contracts or verify it bidirectionally in CI, including examples and error cases.

  Security and safety requirements

  * Require configurable bind address/TLS/authn/authz/rate-limit/request-size deployment controls before non-loopback exposure.
  * Prevent path/query/JSON/log injection, CSRF where cookie auth is used, CORS overexposure, SSRF in destination/source inputs, and XSS in rendered examples.
  * Do not return raw artifact bytes, secrets, plugin environment, or unrestricted filesystem paths by default.
  * Audit accepted/denied consequential commands with actor, subject, policy, request, and result IDs.

  Edge cases and outliers to handle

  * Client disconnects after command commit.
  * Proxy retries POST.
  * API restarts while response is pending.
  * Slow-list/query or huge evidence lineage request.

  Acceptance criteria (“done” definition)

  * REST and CLI/Python commands converge on the same persisted result for equivalent requests.
  * OpenAPI is versioned, complete for implemented endpoints, and fails CI on drift.
  * Client disconnect/retry cannot duplicate authoritative effects.
  * Disabling/removing REST leaves core job execution and status semantics unchanged.

  Testing plan

  * OpenAPI/schema conformance tests.
  * End-to-end REST/CLI equivalence tests.
  * Proxy retry/client disconnect tests.
  * Auth/rate-limit/TLS adapter tests where configured.
  * Injection/CSRF/CORS/size negative tests.
  * Pagination/load and API restart tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: OpenAPI/schema conformance tests., End-to-end REST/CLI equivalence tests., Proxy retry/client disconnect tests., Auth/rate-limit/TLS adapter tests where configured., Injection/CSRF/CORS/size negative tests., Pagination/load and API restart tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T21.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/api/rest.py, atlas/api/dependencies.py, openapi/atlas-v1.yaml, tests/api/.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 83: Implement outbox-backed RabbitMQ event delivery

  1.2 source task(s): `T21.1.3`
  Priority: `P2`
  Estimated effort: `16 hours`
  Dependencies: `T21.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/rabbitmq.py (refactor); atlas/events/dispatcher.py (extend); atlas/events/contracts.py (extend); tests/events/test_rabbitmq_transport.py (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Complete RabbitMQ as a durable notification transport driven from the outbox with confirms, bounded retry, dead-letter evidence, offsets, and no consumer authority over lifecycle state.
  * Restore or protect this invariant: Broker outage cannot roll back or falsely fail an already committed lifecycle transition.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/events/rabbitmq.py` (refactor: Publish versioned event envelopes from committed outbox rows with confirms.); `atlas/events/dispatcher.py` (extend: Add transport-specific retry, backoff, delivery status, and capacity policy.); `atlas/events/contracts.py` (extend: Define routing/version headers and consumer compatibility guidance.); `tests/events/test_rabbitmq_transport.py` (create: Exercise outage, redelivery, confirm, DLQ, and event-injection cases.)
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

  * Complete RabbitMQ as a durable notification transport driven from the outbox with confirms, bounded retry, dead-letter evidence, offsets, and no consumer authority over lifecycle state.
  * Component dispositions: `atlas/events/rabbitmq.py` (refactor: Publish versioned event envelopes from committed outbox rows with confirms.); `atlas/events/dispatcher.py` (extend: Add transport-specific retry, backoff, delivery status, and capacity policy.); `atlas/events/contracts.py` (extend: Define routing/version headers and consumer compatibility guidance.); `tests/events/test_rabbitmq_transport.py` (create: Exercise outage, redelivery, confirm, DLQ, and event-injection cases.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Read committed outbox rows in sequence, publish canonical event envelope and headers, wait for publisher confirm, then persist delivery state.
  * Define bounded retry/dead-letter terminal status, broker topology declarations, message TTL/size, and consumer offset/replay guidance.
  * Preserve legacy routing keys through a versioned compatibility adapter and publish deprecation telemetry.
  * Keep lifecycle state and event history authoritative in StateStore even when broker is unavailable.

  Security and safety requirements

  * Use TLS/credentials/vhost permissions as optional deployment controls and keep secrets out of events/logs.
  * Reject untrusted consumer messages as lifecycle commands; commands require a separately authenticated command endpoint.
  * Bound payload size, headers, retry rate, connection attempts, and backlog policy.
  * Validate event schema/version and prevent routing-key/header injection from artifact/plugin data.

  Edge cases and outliers to handle

  * Broker outage during transition.
  * Confirm lost after broker accepted message.
  * Duplicate/redelivered event.
  * Slow/poison consumer or schema-incompatible consumer.

  Acceptance criteria (“done” definition)

  * Broker outage cannot roll back or falsely fail an already committed lifecycle transition.
  * Delivery retries are bounded and duplicate event IDs/sequences support idempotent consumers.
  * No replayed event can mutate lifecycle state.
  * Legacy routing and new envelopes have a tested compatibility/deprecation path.

  Testing plan

  * Transport conformance tests with test broker.
  * Outage/confirm-loss/redelivery tests.
  * Backlog/capacity/backpressure tests.
  * Schema/routing injection negative tests.
  * Legacy routing compatibility tests.
  * Consumer replay/idempotency reference tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Transport conformance tests with test broker., Outage/confirm-loss/redelivery tests., Backlog/capacity/backpressure tests., Schema/routing injection negative tests., Legacy routing compatibility tests., Consumer replay/idempotency reference tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T21.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/rabbitmq.py, atlas/events/dispatcher.py, atlas/events/contracts.py, tests/events/test_rabbitmq_transport.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 84: Implement signed idempotent webhook notifications

  1.2 source task(s): `T21.1.4`
  Priority: `P2`
  Estimated effort: `14 hours`
  Dependencies: `T21.1.2, T21.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/events/webhooks.py::WebhookDispatcher (create); atlas/models/webhooks.py (create); atlas/schema/migrations/*_webhooks.sql (create); docs/integrations/webhooks.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide optional destination-neutral webhooks with durable delivery attempts, signatures, replay resistance, bounded retries, and no authority to acknowledge lifecycle truth.
  * Restore or protect this invariant: Receivers can verify authenticity, schema version, event identity, and replay window.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-019; REQ-024,REQ-025,REQ-030; PDF:p.18,p.19,p.21,p.27.

  Where this applies

  * Primary affected components: `atlas/events/webhooks.py::WebhookDispatcher` (create: Select subscriptions and perform durable delivery attempts.); `atlas/models/webhooks.py` (create: Define subscription, secret reference, delivery attempt, response summary, and status.); `atlas/schema/migrations/*_webhooks.sql` (create: Persist subscriptions, attempts, retries, and disablement.); `docs/integrations/webhooks.md` (create: Document signature verification, idempotency, retries, and security.)
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

  * Provide optional destination-neutral webhooks with durable delivery attempts, signatures, replay resistance, bounded retries, and no authority to acknowledge lifecycle truth.
  * Component dispositions: `atlas/events/webhooks.py::WebhookDispatcher` (create: Select subscriptions and perform durable delivery attempts.); `atlas/models/webhooks.py` (create: Define subscription, secret reference, delivery attempt, response summary, and status.); `atlas/schema/migrations/*_webhooks.sql` (create: Persist subscriptions, attempts, retries, and disablement.); `docs/integrations/webhooks.md` (create: Document signature verification, idempotency, retries, and security.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define explicit event subscriptions, endpoint policy, schema version, signing key reference, timeout, retry/dead-letter, and disable controls.
  * Sign canonical body plus event ID/sequence/time/version and expose a stable delivery ID for receiver idempotency.
  * Persist attempt before request and store bounded response metadata; never store arbitrary response bodies.
  * Treat 2xx as transport acknowledgement only; it cannot alter ATLAS lifecycle state.

  Security and safety requirements

  * Validate endpoint scheme/host against deployment policy and defend against SSRF, DNS rebinding, redirect abuse, private-network access, and credential-in-URL.
  * Use rotating secret references, constant-time verification guidance, timestamp/nonce replay window, and no secrets in logs.
  * Bound concurrency, retries, body, response, redirect, DNS, and timeout resources.
  * Disable subscriptions after policy-defined repeated permanent failure without deleting evidence.

  Edge cases and outliers to handle

  * Receiver times out after accepting.
  * DNS changes between validation and connection.
  * Redirect crosses policy boundary.
  * Secret rotates while deliveries are pending.

  Acceptance criteria (“done” definition)

  * Receivers can verify authenticity, schema version, event identity, and replay window.
  * Duplicate delivery is expected and safely identifiable.
  * Webhook failure never changes lifecycle state or loses durable event history.
  * SSRF/redirect/rebinding tests demonstrate deployment-policy enforcement.

  Testing plan

  * Signature golden/rotation tests.
  * Duplicate/replay receiver tests.
  * SSRF/DNS-rebinding/redirect negative tests.
  * Timeout/partial-response/retry tests.
  * Backpressure/concurrency tests.
  * Disable/reenable and audit tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Signature golden/rotation tests., Duplicate/replay receiver tests., SSRF/DNS-rebinding/redirect negative tests., Timeout/partial-response/retry tests., Backpressure/concurrency tests., Disable/reenable and audit tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T21.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/events/webhooks.py::WebhookDispatcher, atlas/models/webhooks.py, atlas/schema/migrations/*_webhooks.sql, docs/integrations/webhooks.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
