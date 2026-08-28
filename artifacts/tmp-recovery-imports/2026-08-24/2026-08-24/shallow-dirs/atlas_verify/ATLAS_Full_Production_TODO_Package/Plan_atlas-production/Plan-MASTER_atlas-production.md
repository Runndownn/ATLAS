# Plan-MASTER — ATLAS Full Production Implementation, Verification, and Environment-Qualification Program

## Plan metadata

* Evidence mode: `ATTACHED-SNAPSHOT`
* Target repository: `Runndownn/ATLAS`
* Target plan: `ATLAS_Production_TODO_Package.zip::Plan_atlas-production/TODO_atlas-production-registry.json`
* Frozen ATLAS ref: `efa547cafc64b58d60d19dcc1e5ba32c6b046bc5`
* Frozen Yggdrasil ref: `2b0c51b6132c2a16e63fc2e2de2d2b4598b5fe40`
* Canonical task authority: `TODO_atlas-production-registry.json`
* Status: `PROPOSED / NOT IMPLEMENTED`

## Objective

Convert the canonical ATLAS architecture package into a deterministic, repository-ready production TODO family that preserves the six-stage artifact lifecycle, closes correctness and safety gaps before scale, and gives implementers sprint-fit tasks with exact invariants, dependencies, failure behavior, security controls, tests, migration, rollback, and completion evidence.

## Scope

* Use the latest ATLAS assessment ZIP as the sole architecture and macro-task authority.
* Revalidate its product-direction claims against the attached 34-page PDF without promoting desired direction into implementation fact.
* Use earlier prompts/plans only to explain lineage, test architectural coherence, and add justified support-system detail that does not conflict with the latest package.
* Decompose 24 canonical macro tasks into 96 sprint-fit implementation tasks and add 12 evidence-backed refinement tasks for authority reconciliation, phase-internal work/reuse/budgets, retention, compatibility, plugin SDK, and source-provider evolution.
* Generate one canonical registry plus synchronized master, v1.2, v2.1, manifest, and exact three-task PART1 documents.
* Produce source/delta/crosswalk/requirement/component/validation records and a reproducible generator/validator package.
* Preserve all 108 predecessor TODOs and add a hermetic cross-platform test laboratory, governed adversarial corpora, differential runners, model-based proofs, and production-qualification drills.
* Reconcile the production plan with the current public ATLAS repository perimeter while keeping exact active-checkout and runtime verification explicitly unresolved.

## Architecture and system boundaries

* ATLAS remains an artifact-lifecycle-specific control plane with six ordered semantic barriers: Reconnaissance → Fingerprinting → Structural Discovery → Controlled Extraction → Deep Understanding → Review / Promotion.
* Parallelism and bounded dynamic expansion are permitted only inside a phase barrier; no generic cross-phase DAG is introduced.
* An accepted `IntakeGeneration` is immutable observation truth; downstream work consumes it rather than independently rediscovering mutable sources.
* `ArtifactOccurrence` identifies where bytes were observed; `ContentIdentity` identifies exact bytes. Path, filename, size, and time never substitute for byte identity.
* Authoritative lifecycle state is transactionally persisted with durable event history; event transports, status projections, workers, plugins, models, CLI, APIs, MCP, and UI are adapters/actors, not alternate authorities.
* Structural inspection and cumulative safety budgets precede materialization; materialization occurs in attempt-owned quarantine and records explicit derivation lineage.
* Findings, evidence, decisions, publication attempts, and verified destinations remain separate durable records with exact-byte bidirectional lineage.
* SQLite and local execution/content storage remain reference implementations; PostgreSQL, object storage, remote workers, MCP, and UI require measured triggers and preserve identical semantics.
* AI may analyze, correlate, classify, and propose, but deterministic ATLAS mechanisms own provenance, filesystem safety, lifecycle state, policy enforcement, and final promotion.
* A versioned test-laboratory controller provisions disposable environments, records exact platform/tool/filesystem capabilities, and never becomes product runtime authority.
* Synthetic filesystem, archive, plugin, persistence, transport, and failure corpora are first-class governed test inputs with provenance, bounds, oracles, and minimization.
* Advanced mechanisms are promoted only after differential, fault, compatibility, performance, and falsification evidence demonstrates a better tradeoff than the simpler alternative.

## Trust boundaries

* Source roots, paths, symlinks, mounts, archives, extracted members, temporary files, and destination paths are untrusted until canonical deterministic policy validates them.
* Pipeline/configuration, serialized records, event envelopes, API/MCP/UI inputs, plugin descriptors/results, worker messages, and external responses are untrusted and version/schema/capability validated.
* Plugins, analyzers, tools, subprocesses, remote workers, models, event consumers, webhooks, and destination adapters cannot access StateStore authority or create decisions/publication success directly.
* StateStore transactions and guarded transitions are authoritative; logs, metrics, traces, caches, queues, projections, process memory, and model output are non-authoritative.
* Deployment authentication, authorization, service identity, tenancy, TLS, and secrets are adapters around the deterministic core and must fail closed for enabled consequential network operations.
* Cleanup, migration, publication, and external side effects require idempotency/reconciliation, evidence retention, and practiced rollback.
* Test runners, containers, emulators, hostile fixtures, and fault injectors operate only in disposable roots with synthetic credentials and no production destination authority.

## Constraints

* This run generates planning artifacts only; it does not implement ATLAS product features or modify a repository.
* Evidence mode is ATTACHED-SNAPSHOT. Frozen code citations are not a substitute for inspecting the implementation workspace before edits.
* The latest ZIP overrides earlier plans/prompts on architecture, priorities, baselines, and task semantics.
* Every task is 1–16 hours, dependencies point backward, and all 108 tasks remain unchecked until implementation/test/release evidence exists.
* No generic DAG, mandatory distributed infrastructure, mandatory enterprise IAM, mandatory interactive review for harmless local work, or model authority is introduced without evidence.
* Exact repository-native build/test commands remain unresolved until T1.1.1; no commands or passing results are fabricated.
* Donor code is not copied until Yggdrasil source, dependencies, tests, and license provenance are restored and verified.
* No operating-system, filesystem, isolation, durability, exactly-once, or scale claim is accepted from documentation or a skipped/emulated lane; each claim names the environment and retained evidence.
* The test laboratory may emulate failure and platform semantics, but release support requires at least one native execution lane for every claimed supported platform/control.

## Evidence and authority map

* `AUTH-LATEST-ZIP` — `found` — `operator attachment@ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f:ATLAS_Production_TODO_Package.zip` — Canonical predecessor task authority: 108-task production TODO registry, generated plan family, source reconciliation, and validation evidence. Limitation: Planning package, not implementation proof; this run preserves all 108 tasks and adds repository-aligned test-laboratory and production-qualification work.
* `AUTH-ARCHITECTURE-ZIP` — `found` — `operator attachment@c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97:ATLAS_Assessment_Package.zip` — Canonical architecture assessment, 24 macro tasks, evidence ledger, ADRs, requirements, and risk baseline beneath the production TODO package. Limitation: Frozen assessment snapshot; source runtime was not executed.
* `AUTH-BLUEPRINT` — `found` — `operator attachment / latest ZIP@a65bd3d3e3788d18f937912eb9fdf6c50db03989cadf822c6cadd0edf61b8215:ATLAS_Evidence_Driven_Architecture_Blueprint.md` — Target architecture, data/state/event/provenance/security/failure/performance model and implementation trajectory. Limitation: Static assessment; frozen repositories were not executed.
* `AUTH-EXECUTION-PLAN` — `found` — `operator attachment / latest ZIP@1027eb460a5dbb07e72b04c6376a15bcf944b7b8d0a63a992cbc27879e3fe571:ATLAS_Execution_Plan.md` — Canonical 24 macro tasks, dependencies, priorities, repository changes, acceptance, migration, and rollback requirements. Limitation: Macro tasks exceed sprint size and are decomposed here without changing their architectural decisions.
* `AUTH-DIRECTION-PDF` — `found` — `operator attachment@39cbb7ccf8384802ff45357fdf9d7abed2f00b94e62eaefadf14c2708b8fd31b:ATLAS.pdf` — Desired product direction, lifecycle invariants, sequencing, trust boundaries, and end-state control-plane thesis. Limitation: No separate embedded document version/date beyond its frozen ATLAS baseline; desired direction is not implementation proof.
* `AUTH-ORIGINAL-PROMPT` — `found` — `operator attachment@3a97138d367a095e0b8991a1df3b6f712b3e9d6f14de1b70086aca3c4fe5154f:Pasted markdown.md` — Evidence hierarchy, required assessment passes, classifications, diagrams, task fields, and 30-section deliverable constraints. Limitation: Instruction source, not repository behavior.
* `AUTH-DEEP-REVIEW` — `found` — `operator attachment@c635b8087c61e54d61be8b76a63910bb23e117d96cd38867f7945435df309c62:Pasted markdown (2).md` — Second-order coherence, helper/support-system, security, edge-case, performance, and developer-experience questions. Limitation: Candidate improvements are questions/recommendations and cannot override the latest ZIP.
* `AUTH-EARLIER-ASSESSMENT` — `found` — `operator attachment@2c64fddcfa0aebcc81796c173046a78f29055e25993fe5b1f80f568051a9454c:Pasted markdown (3).md` — Earlier frozen assessment and repository evidence index used to understand the lineage of the latest package. Limitation: Superseded wherever it conflicts with the latest ZIP; source citations still require live/archive verification.
* `AUTH-EARLIER-PLAN` — `found` — `operator attachment@936872038e2b40fea6576fd23737e155e1cc9241fd73f112cd9c76749b2fb776:Pasted markdown (4).md` — Earlier narrative execution plan used for terminology and gap comparison. Limitation: Superseded by the latest ZIP task registry and architecture.
* `AUTH-FROZEN-ATLAS-CODE` — `unresolved` — `Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:repository tree at frozen commit` — Highest implementation authority for current behavior, paths, symbols, tests, schemas, packaging, and commands once inspected. Limitation: No live or archived repository tree is attached; exact current HEAD and dirty state are unknown.
* `AUTH-FROZEN-YGGDRASIL` — `unresolved` — `Runndownn/Yggdrasil@2b0c51b6132c2a16e63fc2e2de2d2b4598b5fe40:repository tree at frozen donor commit` — Donor implementation, dependencies, tests, data contracts, and license provenance for any REUSE/ADAPT/REIMPLEMENT decision. Limitation: No donor archive is attached and the live URL was unavailable during the latest assessment.
* `AUTH-LATEST-VALIDATION` — `found` — `operator attachment / latest ZIP@4bc47d287ca3acaf546b45b1b860e62a89d06013e98c1edadc9b7bd53185b5ef:ATLAS_Assessment_Validation.json` — Structural validation and explicit limitations of the latest architecture package. Limitation: Does not independently prove repository behavior or runtime tests.
* `AUTH-LIVE-ATLAS-WEB` — `found` — `Runndownn/ATLAS@UNRESOLVED:GitHub repository main page retrieved 2026-08-21` — Current public repository perimeter, default branch label, visible file tree, README claims, documented commands, and declared remaining limitations. Limitation: Retrieved 2026-08-21 without a local clone; the dynamic GitHub page exposed `main` and 35 commits but did not expose the exact current HEAD SHA.
* `AUTH-ATLAS-ORCHESTRATOR-WEB` — `found` — `Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5:atlas/core/orchestrator.py` — Selected executable-code verification for phase ordering, in-process job ownership, process-local controls, error policy, and non-transactional event persistence. Limitation: One selected source file was independently fetched; full-tree and runtime execution remain T1.1.1 work.

## Assumptions

* `A1` → `T1.1.1` — The frozen ATLAS commit and cited repository paths/symbols appear consistent with the public repository perimeter, but the exact active HEAD, dirty state, complete tree, and executable command results remain unverified until a checkout is inspected.
* `A2` → `T1.1.3` — The frozen Yggdrasil donor commit and cited donor symbols can be restored with their dependency, test, and MIT-license provenance intact.
* `A3` → `T24.1.1` — ATLAS's supported Python, operating-system, filesystem, and subprocess/resource-control platform matrix has not yet been authoritatively selected.
* `A4` → `T12.1.1` — The deployment-default content retention mode—reference-only, managed immutable content, or hybrid—remains unresolved.
* `A5` → `T1.1.4` — Local filesystem sources are the only evidenced near-term source class; remote/source-provider scope is intentionally deferred pending repository and deployment requirements.
* `A6` → `T17.1.3` — The classes of work that require human review, external authorization, or deterministic local policy before publication are deployment-specific and unresolved.
* `A7` → `T23.1.1` — Retention periods, legal/incident holds, and minimum preservation rules for state, events, content, workspaces, checkpoints, diagnostics, and publications are not defined.
* `A8` → `T25.1.1` — Numeric workload thresholds that justify PostgreSQL, object storage, or multi-host execution are not derivable from the supplied evidence.
* `A9` → `T27.1.4` — The intended deployment identity, authorization, tenancy, and service-boundary model is not established by the supplied package.

## Conflicts and safest interpretations

* `C1` → `T1.1.2` — The canonical package preserved a primary-document access limitation, while the current run includes the original 34-page PDF. Safest interpretation: Keep the ZIP architecture authoritative, use the PDF only to revalidate and annotate source requirements, and do not silently rewrite implementation claims.
* `C2` → `T1.1.3` — Donor mechanisms are described in detail but the current run lacks the donor source archive needed to verify code, dependencies, tests, and license headers. Safest interpretation: Retain donor-derived recommendations as unresolved ADAPT/REIMPLEMENT guidance and block direct reuse until the frozen donor source is restored.
* `C3` → `T1.1.1` — The public repository perimeter is consistent with the frozen plan, but exact current-ref equivalence and workspace state are not independently proven. Safest interpretation: Use the predecessor registry unchanged as task authority, cite the frozen SHA for code claims, and make exact checkout reconciliation the first implementation gate.
* `C4` → `T1.1.4` — Earlier material explores a larger component vocabulary that could over-fragment the target or imply generic workflow/platform expansion. Safest interpretation: Consolidate helpers under cohesive owners, preserve six ordered semantic barriers, add only evidenced support services, and keep scale/agent/governance adapters optional.
* `C5` → `T1.1.2` — The simplified lineage diagram could be misread as replacing the fuller data model. Safest interpretation: Treat page 31 as a visual simplification; page 16 and the latest blueprint govern the complete lineage model.
* `C6` → `T1.1.1` — The current README contains future-dated execution history and completion markers that cannot be treated as runtime or release evidence on the retrieval date. Safest interpretation: Treat those dates as planned schedule metadata and all completion marks as unverified until commit, test, artifact, and runtime evidence are reproduced.

## Intended delivery sequence

1. E1–E2: reconcile live authority and freeze deterministic characterization before behavior changes.
2. E3–E5: establish typed pipeline semantics, transactional persistence/migrations, and exhaustive lifecycle state/attempt/fencing rules.
3. E6–E10: create immutable intake, persistent exact-byte identity, durable events, controls/checkpoints, and canonical source access.
4. E11–E13: contain materialization, enforce recursive archive budgets, add optional managed content, and persist structure/extraction lineage.
5. E14–E16: standardize plugin/execution contracts, phase-internal work items, deterministic reuse, and unified resource budgets.
6. E17–E20: make findings/evidence/decisions/publications durable, define replay-safe recovery, add daemon ownership, and expose authoritative status/diagnostics.
7. E21–E23: add optional transport/API adapters, subprocess isolation, retention, compatibility, SDK, and future source-provider contracts.
8. E24: continuously expand release gates, adversarial validation, packaging/provenance, benchmarks, soak, and rollback evidence.
9. E25–E27: implement scale, remote-worker, MCP, UI, and deployment-governance adapters only after their explicit evidence/decision gates pass.
10. Provision and validate the hermetic platform/service/fault laboratory after the core state, source-access, recovery, and quality contracts exist.
11. Build governed adversarial corpora and cross-platform differential runners, then execute advanced invariant proofs and production-qualification drills.

## Unresolved decisions

* A1: The frozen ATLAS commit, cited repository paths/symbols, build commands, and repository authorities in the latest package still correspond to the workspace that will receive implementation changes.
* A2: The frozen Yggdrasil donor commit and cited donor symbols can be restored with their dependency, test, and MIT-license provenance intact.
* A3: ATLAS's supported Python, operating-system, filesystem, and subprocess/resource-control platform matrix has not yet been authoritatively selected.
* A4: The deployment-default content retention mode—reference-only, managed immutable content, or hybrid—remains unresolved.
* A5: Local filesystem sources are the only evidenced near-term source class; remote/source-provider scope is intentionally deferred pending repository and deployment requirements.
* A6: The classes of work that require human review, external authorization, or deterministic local policy before publication are deployment-specific and unresolved.
* A7: Retention periods, legal/incident holds, and minimum preservation rules for state, events, content, workspaces, checkpoints, diagnostics, and publications are not defined.
* A8: Numeric workload thresholds that justify PostgreSQL, object storage, or multi-host execution are not derivable from the supplied evidence.
* A9: The intended deployment identity, authorization, tenancy, and service-boundary model is not established by the supplied package.
* Exact current `main` HEAD and local checkout state remain unresolved until T1.1.1.
* Native versus emulated platform support and reduced-assurance controls remain governed by A3/T24.1.1; emulation alone cannot establish support.

## E1. Evidence, baseline, and authority reconciliation

Replace the prior assessment limitations with a reproducible implementation baseline while preserving the supplied ZIP as the canonical planning truth.

* [ ] `T1.1.1` — Freeze the active ATLAS ref and repository authority map (`P0`, 12h; dependencies: None)
* [ ] `T1.1.2` — Revalidate all product-direction requirements against the attached PDF (`P0`, 8h; dependencies: None)
* [ ] `T1.1.3` — Restore and revalidate the Yggdrasil donor baseline and license provenance (`P0`, 12h; dependencies: None)
* [ ] `T1.1.4` — Publish the canonical component-ownership and scope boundary matrix (`P0`, 10h; dependencies: T1.1.1, T1.1.2, T1.1.3)

## E2. Deterministic current-behavior characterization

Create executable evidence for every consequential current defect and compatibility surface before production behavior changes.

* [ ] `T2.1.1` — Define the versioned characterization fixture manifest (`P0`, 8h; dependencies: T1.1.4)
* [ ] `T2.1.2` — Characterize CLI, API, persistence, event, and filesystem outcomes (`P0`, 16h; dependencies: T2.1.1)
* [ ] `T2.1.3` — Add adversarial source, archive, analyzer, and control baselines (`P0`, 16h; dependencies: T2.1.1)
* [ ] `T2.1.4` — Integrate characterization evidence into CI and correction gates (`P0`, 10h; dependencies: T2.1.2, T2.1.3)

## E3. Versioned pipeline semantics and configuration

Make the six lifecycle slots, failure policy, typed phase configuration, and canonical configuration digest one deterministic contract across CLI, Python, tests, and future services.

* [ ] `T3.1.1` — Define `PipelineDefinitionV1`, canonical phase slots, and one failure policy (`P0`, 12h; dependencies: T2.1.4)
* [ ] `T3.1.2` — Implement deterministic safe loading, merge order, and canonical digests (`P0`, 16h; dependencies: T3.1.1)
* [ ] `T3.1.3` — Create typed configuration contracts for all six built-in phases (`P0`, 16h; dependencies: T3.1.1)
* [ ] `T3.1.4` — Add legacy pipeline migration, dual support, and deprecation telemetry (`P0`, 12h; dependencies: T3.1.2, T3.1.3)

## E4. StateStore and SQLite migration foundation

Create one transactional persistence authority with versioned schema evolution, verified backup/restore, and a reusable conformance contract.

* [ ] `T4.1.1` — Define the narrow `StateStore` transaction and repository contracts (`P0`, 12h; dependencies: T2.1.4)
* [ ] `T4.1.2` — Implement the SQLite backend with explicit connection and locking policy (`P0`, 16h; dependencies: T4.1.1)
* [ ] `T4.1.3` — Create immutable numbered migrations and the v0.1 upgrade path (`P0`, 16h; dependencies: T4.1.1)
* [ ] `T4.1.4` — Implement verified backup, restore, integrity, and migration recovery (`P0`, 16h; dependencies: T4.1.2, T4.1.3)

## E5. Explicit lifecycle state machines, attempts, and fencing

Make every job, phase, attempt, and control transition legal, atomic, testable, and resistant to stale or duplicate execution.

* [ ] `T5.1.1` — Specify exhaustive job, phase, attempt, and control state tables (`P0`, 12h; dependencies: T3.1.4, T4.1.4)
* [ ] `T5.1.2` — Persist immutable phase runs and execution attempts (`P0`, 16h; dependencies: T5.1.1)
* [ ] `T5.1.3` — Implement guarded atomic transitions and fencing tokens (`P0`, 16h; dependencies: T5.1.1)
* [ ] `T5.1.4` — Add model-based state-machine and invalid-transition verification (`P0`, 14h; dependencies: T5.1.2, T5.1.3)

## E6. Registered sources and immutable intake generations

Turn Reconnaissance into a durable, deterministic observation manifest that downstream phases consume without re-traversing mutable sources.

* [ ] `T6.1.1` — Define `SourceRoot`, `IntakeGeneration`, and `ArtifactOccurrence` schemas (`P0`, 14h; dependencies: T4.1.4, T5.1.4)
* [ ] `T6.1.2` — Implement bounded deterministic intake traversal (`P0`, 16h; dependencies: T6.1.1)
* [ ] `T6.1.3` — Implement generation acceptance, manifest digests, and supersession (`P0`, 14h; dependencies: T6.1.1)
* [ ] `T6.1.4` — Make all downstream phases consume accepted occurrence IDs only (`P0`, 14h; dependencies: T6.1.2, T6.1.3)

## E7. Persistent content identity and occurrence linkage

Establish canonical SHA-256 byte identity across runs while preserving every source occurrence and detecting mutation during reads.

* [ ] `T7.1.1` — Define `ContentIdentity` and occurrence-to-content link contracts (`P0`, 12h; dependencies: T6.1.4)
* [ ] `T7.1.2` — Implement race-aware streaming hashing from accepted occurrences (`P0`, 16h; dependencies: T7.1.1)
* [ ] `T7.1.3` — Add persistent cross-run duplicate lookup and processing-reuse eligibility (`P0`, 12h; dependencies: T7.1.1)
* [ ] `T7.1.4` — Preserve `HashStore` compatibility while removing process-local authority (`P0`, 10h; dependencies: T7.1.2, T7.1.3)

## E8. Durable events and transactional outbox

Persist required lifecycle history atomically with authoritative state and project it to transports without making messaging a second authority.

* [ ] `T8.1.1` — Define versioned durable event and outbox schemas (`P0`, 12h; dependencies: T4.1.4, T5.1.4)
* [ ] `T8.1.2` — Record state transitions, durable events, and outbox rows atomically (`P0`, 16h; dependencies: T8.1.1)
* [ ] `T8.1.3` — Implement the idempotent outbox dispatcher and delivery backpressure (`P0`, 16h; dependencies: T8.1.1)
* [ ] `T8.1.4` — Define progress-event sampling, retention, replay, and event diagnostics (`P0`, 12h; dependencies: T8.1.2, T8.1.3)

## E9. Durable progress, controls, safe points, and checkpoints

Give a second process truthful live progress and durable pause/resume/cancel semantics that resume only from verified recovery points.

* [ ] `T9.1.1` — Define `PhaseContext`, progress, control-request, and checkpoint contracts (`P0`, 14h; dependencies: T5.1.4, T8.1.4)
* [ ] `T9.1.2` — Persist live progress and deterministic job-level projections (`P0`, 14h; dependencies: T9.1.1)
* [ ] `T9.1.3` — Implement durable control requests and safe-point acknowledgement (`P0`, 16h; dependencies: T9.1.1)
* [ ] `T9.1.4` — Implement checkpoint validation, resume decisions, and stale-checkpoint rejection (`P0`, 16h; dependencies: T9.1.2, T9.1.3)

## E10. Canonical race-resistant source access

Route every source read through one registered-root, source-relative, capability-aware service that detects symlink, mount, case, Unicode, and TOCTOU hazards.

* [ ] `T10.1.1` — Specify source-access policy and platform capability contracts (`P0`, 12h; dependencies: T6.1.4)
* [ ] `T10.1.2` — Implement handle-relative no-follow opens and occurrence verification (`P0`, 16h; dependencies: T10.1.1)
* [ ] `T10.1.3` — Create separate safe temporary and destination path services (`P0`, 12h; dependencies: T10.1.1)
* [ ] `T10.1.4` — Route every built-in filesystem operation through canonical access services (`P0`, 16h; dependencies: T10.1.2, T10.1.3)

## E11. Quarantine, recursive archive budgets, and controlled materialization

Inspect containers before extraction, contain every side effect in attempt-owned workspaces, and enforce cumulative recursive resource limits.

* [ ] `T11.1.1` — Implement attempt-owned quarantine workspace lifecycle (`P0`, 16h; dependencies: T7.1.4, T10.1.4)
* [ ] `T11.1.2` — Implement recursive structural inspection under cumulative archive budgets (`P0`, 16h; dependencies: T11.1.1)
* [ ] `T11.1.3` — Implement exact-report-bound `MaterializationService` (`P0`, 16h; dependencies: T11.1.1)
* [ ] `T11.1.4` — Persist derivation edges and adversarial materialization evidence (`P0`, 14h; dependencies: T11.1.2, T11.1.3)

## E12. Optional immutable local content store

Add managed byte retention as an optional content-addressable capability without confusing identity with storage or overstating replayability.

* [ ] `T12.1.1` — Define `ContentStore` contracts and retention-mode semantics (`P1`, 12h; dependencies: T7.1.4, T10.1.4)
* [ ] `T12.1.2` — Implement staged, verified, no-replace local CAS writes (`P1`, 16h; dependencies: T12.1.1)
* [ ] `T12.1.3` — Persist blob provenance, references, quotas, and replayability status (`P1`, 14h; dependencies: T12.1.1)
* [ ] `T12.1.4` — Implement CAS integrity scans and orphan reconciliation hooks (`P1`, 14h; dependencies: T12.1.2, T12.1.3)

## E13. Structural and extraction lineage contracts

Persist exact-byte structural reports and extraction records whose bindings are verified before materialization and reusable only under exact deterministic keys.

* [ ] `T13.1.1` — Define and persist versioned `StructuralReport` records (`P1`, 14h; dependencies: T11.1.4, T12.1.4)
* [ ] `T13.1.2` — Define and persist `ExtractionRecord` and output manifests (`P1`, 14h; dependencies: T13.1.1)
* [ ] `T13.1.3` — Enforce exact content, configuration, policy, and report binding before extraction (`P1`, 14h; dependencies: T13.1.1)
* [ ] `T13.1.4` — Add deterministic structure reuse and end-to-end lineage invariants (`P1`, 14h; dependencies: T13.1.2, T13.1.3)

## E14. Typed plugin contracts, registry, and trust policy

Turn Deep Understanding into a deterministic, versioned capability platform whose plugins emit normalized findings without receiving lifecycle or host authority.

* [ ] `T14.1.1` — Define `PluginDescriptor`, `AnalysisContext`, and `AnalysisFinding` schemas (`P1`, 16h; dependencies: T3.1.4, T7.1.4)
* [ ] `T14.1.2` — Implement deterministic plugin discovery and registry snapshots (`P1`, 16h; dependencies: T14.1.1)
* [ ] `T14.1.3` — Implement plugin capability and trust-tier policy (`P1`, 14h; dependencies: T14.1.1)
* [ ] `T14.1.4` — Add the legacy `AnalyzerPlugin` adapter and lossless finding migration (`P1`, 12h; dependencies: T14.1.2, T14.1.3)

## E15. ExecutionBackend contracts and trusted in-process execution

Separate lifecycle authority from execution location using immutable WorkSpec/WorkResult contracts and a conformance-tested trusted backend.

* [ ] `T15.1.1` — Define immutable `WorkSpec`, `WorkResult`, and backend protocols (`P1`, 16h; dependencies: T5.1.4, T14.1.4)
* [ ] `T15.1.2` — Implement the trusted `InProcessBackend` (`P1`, 16h; dependencies: T15.1.1)
* [ ] `T15.1.3` — Implement coordinator-side result validation and commit (`P1`, 16h; dependencies: T15.1.1)
* [ ] `T15.1.4` — Create the reusable backend conformance and fault suite (`P1`, 14h; dependencies: T15.1.2, T15.1.3)

## E16. Phase-internal work items, deterministic reuse, and unified budgets

Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.

* [ ] `T16.1.1` — Define durable `WorkItem` and phase-barrier semantics (`P1`, 14h; dependencies: T8.1.4, T9.1.4, T12.1.4, T13.1.4, T15.1.4)
* [ ] `T16.1.2` — Implement the bounded local work-item scheduler and aggregation path (`P1`, 16h; dependencies: T16.1.1)
* [ ] `T16.1.3` — Implement exact-key deterministic result reuse (`P1`, 16h; dependencies: T16.1.1)
* [ ] `T16.1.4` — Implement a unified hierarchical `ResourceBudgetManager` (`P1`, 16h; dependencies: T16.1.2, T16.1.3)

## E17. Durable findings, evidence, review, and publication

Separate analytical output from evidence, trust decisions, and externally verified publications while preserving exact-byte lineage and fail-closed authority.

* [ ] `T17.1.1` — Persist normalized analysis findings and typed relationships (`P1`, 16h; dependencies: T7.1.4, T8.1.4, T13.1.4, T14.1.4)
* [ ] `T17.1.2` — Define and persist evidence records with explicit provenance and confidence (`P1`, 16h; dependencies: T17.1.1)
* [ ] `T17.1.3` — Implement evidence-bound promotion decisions and review policy (`P1`, 16h; dependencies: T17.1.1)
* [ ] `T17.1.4` — Implement staged idempotent publication and bidirectional lineage (`P1`, 16h; dependencies: T17.1.2, T17.1.3)

## E18. Retry, timeout, idempotency, reconciliation, and crash recovery

Classify every operation's duplicate-effect behavior and make restart decisions deterministic from verified durable evidence.

* [ ] `T18.1.1` — Define the error taxonomy and operation-semantics registry (`P1`, 14h; dependencies: T9.1.4, T15.1.4, T17.1.4)
* [ ] `T18.1.2` — Implement retry, deadline, timeout, and idempotency policy (`P1`, 16h; dependencies: T18.1.1)
* [ ] `T18.1.3` — Implement startup reconciliation and deterministic recovery decisions (`P1`, 16h; dependencies: T18.1.1)
* [ ] `T18.1.4` — Build the phase-by-phase crash and replay verification matrix (`P1`, 16h; dependencies: T18.1.2, T18.1.3)

## E19. Long-running local runtime ownership

Move active-job ownership from ephemeral CLI memory to a recoverable local daemon without adding distributed scheduling semantics.

* [ ] `T19.1.1` — Define the daemon lifecycle, configuration, and ownership contract (`P1`, 12h; dependencies: T5.1.4, T9.1.4, T18.1.4)
* [ ] `T19.1.2` — Implement durable claims, leases, heartbeats, and fenced execution (`P1`, 16h; dependencies: T19.1.1)
* [ ] `T19.1.3` — Route CLI and Python controls through canonical command and status services (`P1`, 14h; dependencies: T19.1.1)
* [ ] `T19.1.4` — Verify graceful shutdown, forced restart, and orphan containment (`P1`, 16h; dependencies: T19.1.2, T19.1.3)

## E20. Canonical status, telemetry, health, and diagnostics

Give operators authoritative, bounded, and shareable visibility while keeping logs, metrics, and traces non-authoritative.

* [ ] `T20.1.1` — Define structured logging, correlation, error catalog, and redaction (`P1`, 12h; dependencies: T8.1.4, T9.1.4, T18.1.4, T19.1.4)
* [ ] `T20.1.2` — Implement bounded metrics and optional distributed tracing (`P1`, 14h; dependencies: T20.1.1)
* [ ] `T20.1.3` — Build the canonical versioned job status projection (`P1`, 16h; dependencies: T20.1.1)
* [ ] `T20.1.4` — Implement health, readiness, and sanitized diagnostic bundles (`P1`, 14h; dependencies: T20.1.2, T20.1.3)

## E21. Versioned external command and event adapters

Expose REST, RabbitMQ, and webhook surfaces only as adapters over canonical command, status, and durable event contracts.

* [ ] `T21.1.1` — Define versioned external command, status, and error schemas (`P2`, 14h; dependencies: T8.1.4, T19.1.4, T20.1.4)
* [ ] `T21.1.2` — Implement REST v1 and generate the OpenAPI contract (`P2`, 16h; dependencies: T21.1.1)
* [ ] `T21.1.3` — Implement outbox-backed RabbitMQ event delivery (`P2`, 16h; dependencies: T21.1.1)
* [ ] `T21.1.4` — Implement signed idempotent webhook notifications (`P2`, 14h; dependencies: T21.1.2, T21.1.3)

## E22. Subprocess plugin isolation and enforceable resource controls

Run untrusted or high-risk plugins outside the core process with mediated inputs, explicit capabilities, bounded resources, deterministic termination, and visible platform limitations.

* [ ] `T22.1.1` — Define the subprocess protocol and mediated artifact contract (`P2`, 14h; dependencies: T14.1.4, T15.1.4, T16.1.4, T18.1.4)
* [ ] `T22.1.2` — Implement deterministic process lifecycle, timeout, and tree termination (`P2`, 16h; dependencies: T22.1.1)
* [ ] `T22.1.3` — Enforce subprocess resource, network, tool, and secret policy (`P2`, 16h; dependencies: T22.1.1)
* [ ] `T22.1.4` — Establish hostile-plugin and backend conformance gates (`P2`, 16h; dependencies: T22.1.2, T22.1.3)

## E23. Retention, compatibility, plugin SDK, and source-provider evolution

Fill operational and developer-experience gaps without widening core authority or prematurely implementing remote source systems.

* [ ] `T23.1.1` — Define retention classes and implement reference-safe cleanup (`P2`, 16h; dependencies: T12.1.4, T17.1.4)
* [ ] `T23.1.2` — Implement the compatibility catalog and deprecation telemetry (`P2`, 14h; dependencies: T3.1.4, T4.1.4, T8.1.4, T14.1.4, T18.1.4)
* [ ] `T23.1.3` — Deliver the plugin SDK, fixtures, and contract-validation CLI (`P2`, 16h; dependencies: T14.1.4, T15.1.4, T22.1.4)
* [ ] `T23.1.4` — Define the source-provider extension contract and defer unsupported providers (`P2`, 12h; dependencies: T6.1.4, T10.1.4, T14.1.4)

## E24. Continuous quality, packaging, benchmarks, and release evidence

Make every release claim traceable to clean builds, mandatory test families, security and compatibility evidence, representative benchmarks, and a practiced rollback.

* [ ] `T24.1.1` — Define the supported-platform matrix and mandatory CI policy (`P1`, 14h; dependencies: T2.1.4)
* [ ] `T24.1.2` — Add state-machine, migration, crash, adversarial, compatibility, and fuzz gates (`P1`, 16h; dependencies: T5.1.4, T11.1.4, T18.1.4, T22.1.4)
* [ ] `T24.1.3` — Produce reproducible packages, SBOMs, provenance, and integrity manifests (`P1`, 16h; dependencies: T24.1.1, T4.1.4, T23.1.2)
* [ ] `T24.1.4` — Build representative benchmarks, soak tests, and release rollback evidence (`P1`, 16h; dependencies: T24.1.2, T24.1.3, T23.1.1)

## E25. Measured optional PostgreSQL and object-storage adapters

Adopt additional persistence only when benchmark and operational evidence proves the local reference backends cannot satisfy a defined workload.

* [ ] `T25.1.1` — Define and approve quantitative scale-adapter trigger evidence (`P3`, 12h; dependencies: T4.1.4, T12.1.4, T18.1.4, T24.1.4)
* [ ] `T25.1.2` — Finalize backend conformance and one-authority migration contracts (`P3`, 14h; dependencies: T25.1.1)
* [ ] `T25.1.3` — Implement and validate the optional PostgreSQL StateStore (`P3`, 16h; dependencies: T25.1.1)
* [ ] `T25.1.4` — Implement and validate the optional object-backed ContentStore (`P3`, 16h; dependencies: T25.1.2, T25.1.3)

## E26. Optional remote worker execution

Scale execution location without changing phase barriers, coordinator authority, work semantics, exact-byte identity, or durable recovery.

* [ ] `T26.1.1` — Define the authenticated remote worker protocol and compatibility handshake (`P3`, 16h; dependencies: T15.1.4, T18.1.4, T21.1.4, T25.1.4)
* [ ] `T26.1.2` — Implement the least-privileged remote worker service (`P3`, 16h; dependencies: T26.1.1)
* [ ] `T26.1.3` — Implement remote scheduling, result verification, cancellation, and fallback policy (`P3`, 16h; dependencies: T26.1.1)
* [ ] `T26.1.4` — Gate distributed execution with chaos, security, load, and operational evidence (`P3`, 16h; dependencies: T26.1.2, T26.1.3)

## E27. Bounded MCP and operator interfaces

Add optional agent and operator clients that present authoritative distinctions and submit only validated commands, while keeping AI analytical and deployment IAM outside the small core.

* [ ] `T27.1.1` — Expose read-only and proposal-only MCP resources and tools (`P3`, 14h; dependencies: T17.1.4, T19.1.4, T20.1.4, T21.1.4)
* [ ] `T27.1.2` — Route consequential MCP actions through deterministic command and review gates (`P3`, 16h; dependencies: T27.1.1)
* [ ] `T27.1.3` — Build an operator UI that preserves authority and uncertainty distinctions (`P3`, 16h; dependencies: T27.1.1)
* [ ] `T27.1.4` — Resolve tenant, authentication, authorization, and deployment-governance scope (`P3`, 14h; dependencies: T27.1.2, T27.1.3)

## E28. Hermetic test laboratory and platform emulation

Establish disposable native and emulated environments with exact capability/assurance manifests, bounded service doubles, isolation lanes, and deterministic fault injection.

* [ ] `T28.1.1` — Build the hermetic test-laboratory controller and environment manifest (`P1`, 16h; dependencies: T1.1.1, T24.1.1)
* [ ] `T28.1.2` — Emulate Linux filesystem, storage, and kernel-control variants (`P1`, 16h; dependencies: T28.1.1, T10.1.4, T24.1.1)
* [ ] `T28.1.3` — Emulate Windows and macOS path and process semantics (`P1`, 16h; dependencies: T28.1.1, T10.1.4, T22.1.2, T24.1.1)
* [ ] `T28.1.4` — Build isolated process, container, and resource-control test lanes (`P1`, 16h; dependencies: T28.1.1, T22.1.3, T22.1.4)
* [ ] `T28.1.5` — Build deterministic dependency-service and transport emulators (`P1`, 16h; dependencies: T28.1.1, T4.1.4, T8.1.4, T21.1.3)
* [ ] `T28.1.6` — Implement deterministic time, disk, memory, network, and crash fault injection (`P1`, 16h; dependencies: T28.1.1, T18.1.4, T24.1.2)

## E29. Governed adversarial corpora and differential verification

Version synthetic filesystem, archive, plugin, state, event, and concurrency corpora and prove semantic conformance through differential, property, fuzz, mutation, and metamorphic testing.

* [ ] `T29.1.1` — Create the adversarial filesystem and source-mutation corpus (`P1`, 16h; dependencies: T28.1.2, T28.1.3, T6.1.4, T10.1.4)
* [ ] `T29.1.2` — Create the recursive archive and container-abuse corpus (`P1`, 16h; dependencies: T28.1.2, T28.1.3, T11.1.4, T13.1.4)
* [ ] `T29.1.3` — Create the hostile plugin, analyzer, and backend corpus (`P1`, 16h; dependencies: T28.1.4, T14.1.4, T15.1.4, T22.1.4)
* [ ] `T29.1.4` — Create the persistence, event, control, and concurrency scenario corpus (`P1`, 16h; dependencies: T28.1.5, T28.1.6, T5.1.4, T8.1.4, T9.1.4, T19.1.4)
* [ ] `T29.1.5` — Build cross-platform contract, differential, and semantic-equivalence runners (`P1`, 16h; dependencies: T29.1.1, T29.1.2, T29.1.3, T29.1.4, T15.1.4, T23.1.3)
* [ ] `T29.1.6` — Add mutation, property, fuzz, metamorphic, and corpus-triage automation (`P1`, 16h; dependencies: T29.1.1, T29.1.2, T29.1.3, T29.1.4, T24.1.2)

## E30. Advanced invariant proofs and production qualification

Attempt to falsify lifecycle, source-access, atomicity, content-reuse, and publication invariants, then qualify release candidates through native upgrade, rollback, disaster-recovery, security, benchmark, and soak evidence.

* [ ] `T30.1.1` — Model-check lifecycle, lease, fencing, and recovery invariants (`P2`, 16h; dependencies: T5.1.4, T9.1.4, T18.1.4, T29.1.4)
* [ ] `T30.1.2` — Prove immutable intake and race-resistant source access under mutation (`P1`, 16h; dependencies: T6.1.4, T7.1.4, T10.1.4, T29.1.1)
* [ ] `T30.1.3` — Prove transaction, durable-event, and outbox crash atomicity (`P1`, 16h; dependencies: T4.1.4, T8.1.4, T18.1.4, T28.1.6)
* [ ] `T30.1.4` — Prove CAS, deterministic reuse, and derivation correctness under contention (`P2`, 16h; dependencies: T12.1.4, T16.1.3, T29.1.5)
* [ ] `T30.1.5` — Prove idempotent publication and unknown-outcome reconciliation (`P2`, 16h; dependencies: T17.1.4, T18.1.4, T21.1.4, T29.1.4)
* [ ] `T30.1.6` — Run the production-qualification upgrade, rollback, disaster, and soak program (`P1`, 16h; dependencies: T30.1.1, T30.1.2, T30.1.3, T30.1.4, T30.1.5, T24.1.4)
