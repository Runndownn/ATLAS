@BinReaper Production TODOs

## TODO

* [ ] TODO 67: Implement evidence-bound promotion decisions and review policy

  1.2 source task(s): `T17.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T17.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/review.py::PromotionDecision (create); atlas/review/service.py::ReviewService (create); atlas/review/policy.py::ReviewPolicy (create); atlas/phases/review.py (refactor); atlas/schema/migrations/*_promotion_decisions.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create durable `APPROVE`, `REJECT`, and `HOLD` decisions that bind an actor and policy version to an exact current evidence set and never treat analyzer or AI output as final authority.
  * Restore or protect this invariant: Only one current decision is authoritative for a subject/policy scope.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31.

  Where this applies

  * Primary affected components: `atlas/models/review.py::PromotionDecision` (create: Define decision state, subject, evidence-set digest, actor/policy identity, reason, validity, and supersession.); `atlas/review/service.py::ReviewService` (create: Evaluate policy, record review requests, and persist guarded decisions.); `atlas/review/policy.py::ReviewPolicy` (create: Separate deterministic framework mechanisms from deployment-specific approval policy.); `atlas/phases/review.py` (refactor: Replace transient promotion candidates with durable review requests and compatibility summaries.); `atlas/schema/migrations/*_promotion_decisions.sql` (create: Persist review requests, decisions, actors, policies, and supersession history.)
  * Epic boundary: Durable findings, evidence, review, and publication — Separate analytical output from evidence, trust decisions, and externally verified publications while preserving exact-byte lineage and fail-closed authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].
  * Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-015 requires: Review currently produces transient candidates rather than durable approve/reject/hold decisions and verifiable publications.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Create durable `APPROVE`, `REJECT`, and `HOLD` decisions that bind an actor and policy version to an exact current evidence set and never treat analyzer or AI output as final authority.
  * Component dispositions: `atlas/models/review.py::PromotionDecision` (create: Define decision state, subject, evidence-set digest, actor/policy identity, reason, validity, and supersession.); `atlas/review/service.py::ReviewService` (create: Evaluate policy, record review requests, and persist guarded decisions.); `atlas/review/policy.py::ReviewPolicy` (create: Separate deterministic framework mechanisms from deployment-specific approval policy.); `atlas/phases/review.py` (refactor: Replace transient promotion candidates with durable review requests and compatibility summaries.); `atlas/schema/migrations/*_promotion_decisions.sql` (create: Persist review requests, decisions, actors, policies, and supersession history.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define which harmless local outcomes may receive deterministic policy decisions and which publication classes require an attributed human or external authority.
  * Bind every decision to subject identity, evidence-set digest, policy ID/version/digest, actor type/ID, reason code/text, time, and predecessor when superseding.
  * Reject stale decision attempts if the evidence set, subject version, policy, or lifecycle version changed.
  * Expose a versioned review command through canonical `CommandService`; no plugin, model, event consumer, or destination adapter may write decisions directly.

  Security and safety requirements

  * AI and plugins may propose classifications or reasons but cannot be the sole actor for final promotion.
  * Require authorization as an optional deployment adapter for consequential decisions while preserving local single-operator usability.
  * Use optimistic version/fencing and idempotency keys to prevent replayed or concurrent review commands.
  * Audit actor, request, policy evaluation, denied action, decision, supersession, and current-authority resolution.

  Edge cases and outliers to handle

  * Concurrent approve and reject.
  * Evidence changes while a reviewer has stale UI/CLI state.
  * Policy version is retired or unavailable.
  * Imported legacy candidate has no actor or evidence-set digest.

  Acceptance criteria (“done” definition)

  * Only one current decision is authoritative for a subject/policy scope.
  * `REJECT` and `HOLD` structurally block publication.
  * A stale or replayed review command cannot overwrite a newer decision.
  * The deployment-specific rule for interactive versus automatic review is resolved and documented before publication is enabled.

  Testing plan

  * State/transition table tests.
  * Concurrent review and stale-version tests.
  * Policy adapter conformance tests.
  * AI/plugin authority negative tests.
  * Legacy candidate migration tests.
  * Audit and status projection tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: State/transition table tests., Concurrent review and stale-version tests., Policy adapter conformance tests., AI/plugin authority negative tests., Legacy candidate migration tests., Audit and status projection tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T17.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/review.py::PromotionDecision, atlas/review/service.py::ReviewService, atlas/review/policy.py::ReviewPolicy, atlas/phases/review.py, atlas/schema/migrations/*_promotion_decisions.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 68: Implement staged idempotent publication and bidirectional lineage

  1.2 source task(s): `T17.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T17.1.2, T17.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/publication.py (create); atlas/review/publication.py::PublicationCoordinator (create); atlas/review/adapters.py::PublicationAdapter (create); atlas/schema/migrations/*_publications.sql (create); atlas/cli.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Publish only after a current authorized decision, using staged writes, exact idempotency identity, destination verification, unknown-outcome reconciliation, and a complete path back to source bytes.
  * Restore or protect this invariant: No publication begins without a current authorized `APPROVE` decision bound to the exact evidence set.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31.

  Where this applies

  * Primary affected components: `atlas/models/publication.py` (create: Define `PublicationRequest`, `PublicationAttempt`, and `DestinationPublication` records.); `atlas/review/publication.py::PublicationCoordinator` (create: Own request validation, attempt state, adapter execution, verification, and reconciliation.); `atlas/review/adapters.py::PublicationAdapter` (create: Define versioned destination capability and no-replace/expected-replace contracts.); `atlas/schema/migrations/*_publications.sql` (create: Persist publication requests, attempts, destination identities, verification, and lineage.); `atlas/cli.py` (extend: Expose submit/status/reconcile commands through canonical services without direct destination writes.)
  * Epic boundary: Durable findings, evidence, review, and publication — Separate analytical output from evidence, trust decisions, and externally verified publications while preserving exact-byte lineage and fail-closed authority.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-015: Implement first-class findings, evidence, decisions, and publication attempts; evidence: GAP-011, GAP-015, REQ-019, REQ-020, REQ-027, REQ-028; [ATLAS:efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/phases/review.py:L19-L236].
  * Canonical proposed files/interfaces: Create `atlas/review/service.py`, `atlas/review/publication.py`; refactor `atlas/phases/review.py`; extend artifact/finding models and migrations. / `AnalysisFinding`, `EvidenceRecord`, `PromotionDecision`, `PublicationRequest`, `PublicationAttempt`, `DestinationPublication`, `PublicationAdapter`.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-015 requires: Review currently produces transient candidates rather than durable approve/reject/hold decisions and verifiable publications.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Publish only after a current authorized decision, using staged writes, exact idempotency identity, destination verification, unknown-outcome reconciliation, and a complete path back to source bytes.
  * Component dispositions: `atlas/models/publication.py` (create: Define `PublicationRequest`, `PublicationAttempt`, and `DestinationPublication` records.); `atlas/review/publication.py::PublicationCoordinator` (create: Own request validation, attempt state, adapter execution, verification, and reconciliation.); `atlas/review/adapters.py::PublicationAdapter` (create: Define versioned destination capability and no-replace/expected-replace contracts.); `atlas/schema/migrations/*_publications.sql` (create: Persist publication requests, attempts, destination identities, verification, and lineage.); `atlas/cli.py` (extend: Expose submit/status/reconcile commands through canonical services without direct destination writes.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Validate a current `APPROVE` decision, exact evidence-set digest, subject content identity, destination policy, and adapter capability before creating an attempt.
  * Derive a stable idempotency key from publication request identity and persist it before any external side effect.
  * Stage destination content/metadata, commit with no-replace or explicit expected-replace semantics, then independently verify bytes and destination identity.
  * Record `SUCCEEDED`, `FAILED`, or `UNKNOWN/RECONCILIATION_REQUIRED`; never infer destination success from a request or transport acknowledgement.
  * Expose forward and reverse lineage queries from source occurrence/content through derived records to every verified publication.

  Security and safety requirements

  * Resolve destinations through typed adapters; never concatenate untrusted paths, shell commands, SQL, URLs, or credentials.
  * Use least-privilege secret references and capability grants; keep secrets out of request/event/audit payloads.
  * Fence stale attempts and reject unauthorized or policy-incompatible adapters.
  * For unknown external outcomes, query by exact idempotency/destination identity before retrying; fail closed when verification is impossible.

  Edge cases and outliers to handle

  * Destination already exists with same or different bytes.
  * Timeout occurs after remote commit but before response.
  * Partial staged upload, verifier outage, or destination rollback.
  * Decision/evidence becomes stale before or during publication.

  Acceptance criteria (“done” definition)

  * No publication begins without a current authorized `APPROVE` decision bound to the exact evidence set.
  * Duplicate requests converge on one verified destination effect or a deterministic conflict.
  * Unknown outcome is reconciled rather than blindly repeated.
  * Every verified publication resolves bidirectionally to source root, intake generation, occurrence, exact content, derivations, findings, evidence, decision, actor, policy, and attempt.

  Testing plan

  * Approve/reject/hold end-to-end tests.
  * Idempotency and duplicate-request tests.
  * Partial/timeout/unknown-outcome fault injection.
  * No-replace and expected-replace tests.
  * Unauthorized/path/command-injection negative tests.
  * Bidirectional lineage and legacy compatibility tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Approve/reject/hold end-to-end tests., Idempotency and duplicate-request tests., Partial/timeout/unknown-outcome fault injection., No-replace and expected-replace tests., Unauthorized/path/command-injection negative tests., Bidirectional lineage and legacy compatibility tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T17.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/publication.py, atlas/review/publication.py::PublicationCoordinator, atlas/review/adapters.py::PublicationAdapter, atlas/schema/migrations/*_publications.sql, atlas/cli.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 69: Define the error taxonomy and operation-semantics registry

  1.2 source task(s): `T18.1.1`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T9.1.4, T15.1.4, T17.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/errors.py::AtlasError (refactor); atlas/recovery/semantics.py::OperationSemantics (create); atlas/recovery/registry.py::OperationSemanticsRegistry (create); docs/operations/operation-semantics.md (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Give every built-in operation a typed failure class and explicit semantics for restartability, checkpoints, idempotent side effects, external reconciliation, and unsafe unknown outcomes.
  * Restore or protect this invariant: Every built-in operation has exactly one current, versioned semantics classification.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-016; REQ-017; PDF:p.14-15,p.24,p.27.

  Where this applies

  * Primary affected components: `atlas/errors.py::AtlasError` (refactor: Create stable categories, reason codes, retry hints, safe operator text, and causation fields.); `atlas/recovery/semantics.py::OperationSemantics` (create: Declare duplicate-effect, checkpoint, timeout, reconciliation, and compensation behavior.); `atlas/recovery/registry.py::OperationSemanticsRegistry` (create: Provide deterministic registration and compatibility validation.); `docs/operations/operation-semantics.md` (create: Document classifications for every built-in phase and consequential helper.)
  * Epic boundary: Retry, timeout, idempotency, reconciliation, and crash recovery — Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Canonical macro task AT-016: Define retries, timeouts, idempotency, reconciliation, and crash recovery per phase; evidence: GAP-008, REQ-017; Sections 23 and ADR-011.
  * Canonical proposed files/interfaces: Coordinator/lifecycle, phase contracts, execution backends, review/publication; create error/recovery policy module if needed. / `RetryPolicy`, `OperationSemantics`, `RecoveryDecision`, `Reconciler`, typed `AtlasError` hierarchy.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * Macro AT-016 requires: Replay is unsafe unless each operation declares duplicate effects, checkpoints, and unknown-outcome handling.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Give every built-in operation a typed failure class and explicit semantics for restartability, checkpoints, idempotent side effects, external reconciliation, and unsafe unknown outcomes.
  * Component dispositions: `atlas/errors.py::AtlasError` (refactor: Create stable categories, reason codes, retry hints, safe operator text, and causation fields.); `atlas/recovery/semantics.py::OperationSemantics` (create: Declare duplicate-effect, checkpoint, timeout, reconciliation, and compensation behavior.); `atlas/recovery/registry.py::OperationSemanticsRegistry` (create: Provide deterministic registration and compatibility validation.); `docs/operations/operation-semantics.md` (create: Document classifications for every built-in phase and consequential helper.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define error categories for validation, policy, input mutation, resource limit, timeout, cancellation, dependency, persistence, protocol, plugin, invariant, and unknown external outcome.
  * Classify each built-in operation as pure/restartable, checkpoint-resumable, idempotent side effect, externally reconcilable side effect, or non-retriable/manual.
  * Require operation semantics ID/version/digest in phase/plugin descriptors and persisted attempts.
  * Map legacy exceptions conservatively and preserve original causes without exposing secrets or raw payloads.

  Security and safety requirements

  * Do not let plugins declare stronger safety semantics than policy permits; registry validation can downgrade or reject.
  * Never classify an unknown external mutation as retryable by default.
  * Sanitize exception text and structured context before persistence/logging.
  * Record semantic version/digest so a restarted job cannot silently use changed duplicate-effect rules.

  Edge cases and outliers to handle

  * One operation raises multiple nested error categories.
  * Plugin version changes semantics between attempts.
  * Legacy error has no code or retry hint.
  * Cancellation races with timeout or external side effect.

  Acceptance criteria (“done” definition)

  * Every built-in operation has exactly one current, versioned semantics classification.
  * Unknown/unregistered semantics block automatic retry.
  * Error codes are stable, serializable, and safe for API/event/log projection.
  * Policy can prove why an outcome is retryable, blocked, terminal, or requires reconciliation.

  Testing plan

  * Registry completeness tests.
  * Error serialization/golden tests.
  * Legacy exception mapping tests.
  * Plugin overclaim negative tests.
  * Semantics-version compatibility tests.
  * Secret-redaction tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Registry completeness tests., Error serialization/golden tests., Legacy exception mapping tests., Plugin overclaim negative tests., Semantics-version compatibility tests., Secret-redaction tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T18.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/errors.py::AtlasError, atlas/recovery/semantics.py::OperationSemantics, atlas/recovery/registry.py::OperationSemanticsRegistry, docs/operations/operation-semantics.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
