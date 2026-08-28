@BinReaper Production TODOs

## TODO

* [ ] TODO 64: Implement a unified hierarchical `ResourceBudgetManager`

  1.2 source task(s): `T16.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T16.1.2, T16.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/resources/budgets.py::ResourceBudgetManager (create); atlas/core/context.py (extend); atlas/status/projection.py (extend)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Reserve, account, enforce, and report time, CPU hints, memory, bytes read/written, temp space, files, processes, events, and concurrency across job, phase, work item, workspace, archive, and backend scopes.
  * Restore or protect this invariant: All core resource-consuming operations use scoped budget handles.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend.

  Where this applies

  * Primary affected components: `atlas/resources/budgets.py::ResourceBudgetManager` (create: Own hierarchical limits, reservations, accounting, and violations.); `atlas/core/context.py` (extend: Expose scoped budget handles.); `atlas/status/projection.py` (extend: Report limits, use, reservations, and blockers.)
  * Epic boundary: Phase-internal work items, deterministic reuse, and unified budgets — Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; latest package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Frozen ATLAS implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; live workspace verification is blocked by T1.1.1 where path-dependent.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Phase-internal work items, deterministic reuse, and unified budgets.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Reserve, account, enforce, and report time, CPU hints, memory, bytes read/written, temp space, files, processes, events, and concurrency across job, phase, work item, workspace, archive, and backend scopes.
  * Component dispositions: `atlas/resources/budgets.py::ResourceBudgetManager` (create: Own hierarchical limits, reservations, accounting, and violations.); `atlas/core/context.py` (extend: Expose scoped budget handles.); `atlas/status/projection.py` (extend: Report limits, use, reservations, and blockers.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define budget dimensions, hierarchy/inheritance, reservation/commit/release, soft versus hard limits, and platform-enforceability metadata.
  * Integrate archive, workspace, hashing, event, scheduler, plugin, and backend accounting with one scoped API.
  * Persist authoritative counters/reservations needed for restart and reconcile abandoned reservations.
  * Define deterministic behavior on soft warning, hard exceed, unknown usage, and unsupported enforcement.

  Security and safety requirements

  * Untrusted plugins/backends cannot increase their budgets or under-report usage without core verification where possible.
  * Hard-limit violation cancels/contains work and records exact dimension/scope.
  * Unsupported OS controls are visible and cannot be advertised as enforced.
  * Counters and labels are bounded to prevent telemetry/storage DoS.

  Edge cases and outliers to handle

  * Nested archive and subprocess consume the same temp quota.
  * Concurrent work items race on shared job budget.
  * Crash leaves reservations but no live work.
  * Actual memory/CPU cannot be measured reliably on a platform.

  Acceptance criteria (“done” definition)

  * All core resource-consuming operations use scoped budget handles.
  * Concurrent reservations cannot exceed hard shared limits.
  * Restart reconciliation clears or transfers abandoned reservations deterministically.
  * Status and diagnostics distinguish requested, reserved, used, exceeded, and unenforceable.

  Testing plan

  * Budget hierarchy unit/property tests.
  * Concurrent reservation tests.
  * Crash/orphan reservation reconciliation tests.
  * Cross-subsystem shared quota tests.
  * Unsupported-control reporting tests.
  * Resource-exhaustion integration/soak tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Budget hierarchy unit/property tests., Concurrent reservation tests., Crash/orphan reservation reconciliation tests., Cross-subsystem shared quota tests., Unsupported-control reporting tests., Resource-exhaustion integration/soak tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T16.1.4`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/resources/budgets.py::ResourceBudgetManager, atlas/core/context.py, atlas/status/projection.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 65: Persist normalized analysis findings and typed relationships

  1.2 source task(s): `T17.1.1`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T7.1.4, T8.1.4, T13.1.4, T14.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/findings.py::AnalysisFinding (create); atlas/review/repository.py::FindingRepository (create); atlas/phases/analyze.py (refactor); atlas/schema/migrations/*_analysis_findings.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Replace transient analyzer dictionaries with versioned, queryable `AnalysisFinding` records that remain non-authoritative claims linked to exact inputs, plugin versions, phase attempts, and deterministic relationship types.
  * Restore or protect this invariant: Every persisted finding identifies exact input content, analyzer/plugin version, configuration digest, phase attempt, and schema version.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31.

  Where this applies

  * Primary affected components: `atlas/models/findings.py::AnalysisFinding` (create: Define the durable finding identity, subject, predicate/type, value, confidence, provenance, and status contract.); `atlas/review/repository.py::FindingRepository` (create: Persist and query findings without granting them review or publication authority.); `atlas/phases/analyze.py` (refactor: Normalize analyzer results through the finding contract while preserving a compatibility projection.); `atlas/schema/migrations/*_analysis_findings.sql` (create: Create versioned tables, indexes, constraints, and legacy migration fields.)
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

  * Replace transient analyzer dictionaries with versioned, queryable `AnalysisFinding` records that remain non-authoritative claims linked to exact inputs, plugin versions, phase attempts, and deterministic relationship types.
  * Component dispositions: `atlas/models/findings.py::AnalysisFinding` (create: Define the durable finding identity, subject, predicate/type, value, confidence, provenance, and status contract.); `atlas/review/repository.py::FindingRepository` (create: Persist and query findings without granting them review or publication authority.); `atlas/phases/analyze.py` (refactor: Normalize analyzer results through the finding contract while preserving a compatibility projection.); `atlas/schema/migrations/*_analysis_findings.sql` (create: Create versioned tables, indexes, constraints, and legacy migration fields.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define stable finding IDs, finding schema version, content/derived-artifact subject, analyzer and plugin-version identity, attempt/work-item origin, confidence/uncertainty, observed time, and supersession state.
  * Define a closed initial relationship vocabulary plus an extension namespace; reject unknown unversioned relationship semantics.
  * Persist findings transactionally with the phase result and durable event; expose deterministic ordering and pagination.
  * Keep legacy metadata output as a derived compatibility view and mark unmappable legacy records as `authority=none`.

  Security and safety requirements

  * Treat plugin and AI output as untrusted claims; validate types, sizes, encodings, identifiers, and relationship namespaces before persistence.
  * Do not permit finding payloads to contain executable commands, destination credentials, lifecycle transitions, or direct publication instructions.
  * Bound free-text and binary-derived samples; redact or reference sensitive values rather than copying them into logs/events.
  * Make analyzer identity, code/config digest, input content identity, and attempt lineage tamper-evident in the record.

  Edge cases and outliers to handle

  * Duplicate findings from the same and different analyzers.
  * Conflicting or low-confidence findings.
  * Analyzer emits malformed, oversized, cyclic, or self-referential relationships.
  * Legacy analyzer omits version, confidence, or subject identity.

  Acceptance criteria (“done” definition)

  * Every persisted finding identifies exact input content, analyzer/plugin version, configuration digest, phase attempt, and schema version.
  * Finding persistence cannot create evidence, a promotion decision, or a publication.
  * Duplicate policy and supersession behavior are deterministic and documented.
  * Legacy findings remain readable without being misrepresented as approved knowledge.

  Testing plan

  * Schema and repository unit tests.
  * Analyzer-contract integration tests.
  * Malformed/oversized output negative tests.
  * Duplicate/conflict property tests.
  * Legacy compatibility fixture tests.
  * Transaction/event atomicity tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Schema and repository unit tests., Analyzer-contract integration tests., Malformed/oversized output negative tests., Duplicate/conflict property tests., Legacy compatibility fixture tests., Transaction/event atomicity tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T17.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/findings.py::AnalysisFinding, atlas/review/repository.py::FindingRepository, atlas/phases/analyze.py, atlas/schema/migrations/*_analysis_findings.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 66: Define and persist evidence records with explicit provenance and confidence

  1.2 source task(s): `T17.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T17.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/evidence.py::EvidenceRecord (create); atlas/review/evidence.py::EvidenceService (create); atlas/review/repository.py::EvidenceRepository (create); atlas/schema/migrations/*_evidence.sql (create)`
  Required authorities: `ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Create an evidence layer that cites immutable observations, structural reports, extraction records, findings, and verifier outputs without collapsing them into a final trust decision.
  * Restore or protect this invariant: Evidence-set digests are stable under deterministic canonical ordering and change when any cited record changes.
  * Source lineage: LATEST-ZIP:ATLAS_Task_Registry.json:AT-015; REQ-019,REQ-020,REQ-027,REQ-028; PDF:p.8,p.16,p.21,p.22,p.23,p.31.

  Where this applies

  * Primary affected components: `atlas/models/evidence.py::EvidenceRecord` (create: Define evidence types, cited subjects, source records, verifier, confidence, validity, and supersession.); `atlas/review/evidence.py::EvidenceService` (create: Validate, assemble, digest, and query exact evidence sets.); `atlas/review/repository.py::EvidenceRepository` (create: Persist evidence and citations with immutable lineage.); `atlas/schema/migrations/*_evidence.sql` (create: Add evidence, citation, digest, and supersession tables.)
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

  * Create an evidence layer that cites immutable observations, structural reports, extraction records, findings, and verifier outputs without collapsing them into a final trust decision.
  * Component dispositions: `atlas/models/evidence.py::EvidenceRecord` (create: Define evidence types, cited subjects, source records, verifier, confidence, validity, and supersession.); `atlas/review/evidence.py::EvidenceService` (create: Validate, assemble, digest, and query exact evidence sets.); `atlas/review/repository.py::EvidenceRepository` (create: Persist evidence and citations with immutable lineage.); `atlas/schema/migrations/*_evidence.sql` (create: Add evidence, citation, digest, and supersession tables.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define evidence classes for deterministic observation, structural validation, extraction verification, analyzer corroboration, policy evaluation, and external verification.
  * Require every evidence record to cite one or more immutable source records and an exact subject identity.
  * Compute a canonical evidence-record digest and an ordered evidence-set digest for review binding.
  * Define validity, expiry where applicable, revocation/supersession, and provenance-completeness rules without rewriting history.

  Security and safety requirements

  * Deterministic framework evidence outranks unverified model/plugin assertions for safety and lifecycle decisions.
  * Reject citations to missing, mutable, cross-job, or incompatible-schema records unless an explicit import/provenance contract exists.
  * Never embed secrets, full raw content, or unbounded analyzer text in evidence; use immutable references and bounded summaries.
  * Record actor/verifier identity and policy/tool/configuration digests for every evidence creation or supersession action.

  Edge cases and outliers to handle

  * Evidence cites a finding later superseded.
  * Two records claim incompatible facts about one content identity.
  * Evidence set contains duplicate or differently ordered citations.
  * Verifier fails after creating some evidence inputs.

  Acceptance criteria (“done” definition)

  * Evidence-set digests are stable under deterministic canonical ordering and change when any cited record changes.
  * Every evidence record resolves to immutable source observations or explicitly labeled external authority.
  * Unverified findings cannot silently become deterministic evidence.
  * Superseded evidence remains queryable and cannot satisfy a current-decision policy unless allowed explicitly.

  Testing plan

  * Canonical digest golden tests.
  * Citation integrity and foreign-key tests.
  * Conflicting/superseded evidence tests.
  * Missing/mutable citation negative tests.
  * Verifier transaction/failure tests.
  * Lineage-query integration tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Canonical digest golden tests., Citation integrity and foreign-key tests., Conflicting/superseded evidence tests., Missing/mutable citation negative tests., Verifier transaction/failure tests., Lineage-query integration tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T17.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/evidence.py::EvidenceRecord, atlas/review/evidence.py::EvidenceService, atlas/review/repository.py::EvidenceRepository, atlas/schema/migrations/*_evidence.sql.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
