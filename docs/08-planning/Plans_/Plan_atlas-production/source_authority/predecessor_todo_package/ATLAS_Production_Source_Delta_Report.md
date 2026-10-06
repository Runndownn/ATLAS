# ATLAS Production TODO Source Reconciliation and Delta Report

## Authority decision

The operator-designated latest package, `ATLAS_Assessment_Package.zip` (`sha256:c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97`), remains the sole authority for target architecture, frozen baselines, repository findings, requirements, ADRs, risks, and the original 24 implementation macros. The attached PDF is used to close the package's prior primary-document access limitation and revalidate desired-direction claims. Earlier prompts and plans are secondary: they may clarify, challenge, or deepen the canonical package, but they do not replace it.

Evidence mode: `ATTACHED-SNAPSHOT`.

## Result

| Measure | Value |
|---|---:|
| Canonical epics | 27 |
| Canonical sprint-fit tasks | 108 |
| P0 / P1 / P2 / P3 | 44 / 40 / 12 / 12 |
| Estimated engineering hours | 1,566 |
| Original ZIP macro tasks covered | 24 / 24 |
| Tasks decomposed from macros | 96 |
| Justified refinement tasks | 12 |
| PART1 documents | 36 |
| Tasks per PART1 | 3 |
| Completed tasks | 0 |
| Unresolved assumptions | 9 |
| Preserved evidence conflicts | 5 |

## What was preserved without semantic change

1. ATLAS remains artifact-lifecycle-specific rather than a generic workflow, scheduler, task-queue, governance, or agent platform.
2. The six ordered barriers remain the semantic spine:

   `Reconnaissance → Fingerprinting → Structural Discovery → Controlled Extraction → Deep Understanding → Review / Promotion`

3. Immutable intake, occurrence/content separation, deterministic byte identity, pre-materialization inspection, quarantine, durable state/events/controls/checkpoints, typed plugins, evidence/decision/publication separation, replay safety, and exact-byte lineage remain foundational.
4. SQLite and local execution remain the reference path. PostgreSQL, object storage, remote workers, MCP, and UI remain evidence-gated adapters.
5. Models and agents may analyze and propose but never become the sole authority for provenance, filesystem safety, lifecycle state, policy, or final promotion.

## Macro decomposition

Every `AT-001`–`AT-024` macro was split into four 1–16 hour tasks, producing 96 tasks. The decomposition separates schema/contract work, implementation, migration/compatibility, adversarial validation, and operational evidence so each task has a coherent review and rollback boundary. The exact mapping is in `ATLAS_Production_Macro_Coverage.csv` and `ATLAS_Production_Task_Crosswalk.csv`.

## Refinements incorporated from earlier material

### E1 — Evidence, baseline, and authority reconciliation

Four P0 tasks were added because the latest package itself records unresolved primary evidence:

* freeze the active ATLAS workspace and repository authority map;
* revalidate all 30 requirements and diagrams against the attached PDF;
* restore and verify the frozen Yggdrasil donor source and license provenance;
* publish one component-ownership/scope matrix that consolidates helper candidates and rejects architecture inflation.

### E16 — Phase-internal work, reuse, and unified budgets

The deep review correctly identified that the canonical plan needed implementable contracts for bounded parallel work without a generic DAG. Four P1 tasks define:

* durable `WorkItem` records restricted to one phase;
* a bounded local scheduler and phase-barrier aggregation;
* exact-key deterministic result reuse keyed by input, code, configuration, policy, and schema digests;
* one hierarchical `ResourceBudgetManager` shared by jobs, phases, work items, archives, plugins, and backends.

### E23 — Retention, compatibility, SDK, and source-provider evolution

Four P2 tasks close operational/developer gaps that the latest architecture implies but does not fully decompose:

* reference-safe retention, holds, cleanup, and reconciliation;
* a compatibility catalog and explicit translators/deprecation telemetry;
* a public plugin SDK, examples, fixtures, and contract-validation CLI;
* a source-provider contract that proves local semantics now and explicitly defers unsupported providers.

## Helper candidates consolidated rather than multiplied

The deep-review helper list was not converted into one class per noun. Cohesive responsibilities were combined:

* `OccurrenceResolver` is part of intake/source access.
* `QuarantineManager` is part of attempt-owned workspace management.
* `ArchiveBudgetController` uses the unified resource budget.
* `AttemptManager` remains lifecycle/StateStore behavior rather than a second state owner.
* fencing is enforced at transition, claim, and result boundaries rather than through an independent mutable service.
* cleanup reconciliation is split between recovery and retention according to authoritative state.
* schema/version concerns are covered by migration plus compatibility catalog.
* event transports, telemetry sinks, source providers, execution backends, destinations, authentication, secrets, MCP, and UI remain adapters.

The complete classification is in `ATLAS_Production_Component_Responsibility_Matrix.csv`.

## Ideas deliberately rejected or kept deferred

* A generic cross-phase DAG scheduler.
* A multi-agent orchestration layer above ATLAS.
* Mandatory PostgreSQL, object storage, broker, remote workers, MCP, or UI before measured need and completed foundations.
* Mandatory enterprise IAM or multi-tenancy in the compact local core.
* Mandatory interactive approval for harmless local analysis.
* Model/plugin self-authorization, self-certification of evidence, or final promotion.
* Direct donor-code transplantation before frozen-source, dependency, test, and license verification.
* A microservice or manager class for every helper candidate.

## PDF revalidation outcome

All 30 requirement rows from the canonical package were rechecked against the attached 34-page PDF. Each remains supported as explicit desired direction. The revalidation does not convert those requirements into current implementation facts. It also preserves unresolved deployment choices:

* managed byte-retention mode (`A4`);
* review/approval actor classes (`A6`);
* retention periods (`A7`);
* numeric scale-adapter triggers (`A8`);
* deployment identity/tenancy (`A9`);
* supported platform/isolation matrix (`A3`).

The page-by-page results and task mappings are in `ATLAS_Production_PDF_Requirements_Revalidation.csv`.

## First implementation sequence

The smallest dependency-correct sequence that removes the highest-consequence ambiguity remains:

1. `T1.1.1`–`T1.1.4`: reconcile current code, PDF, donor evidence, and component authority.
2. `T2.1.1`–`T2.1.4`: freeze deterministic characterization and adversarial baselines.
3. `T3.1.1`–`T5.1.4`: normalize pipeline semantics, migrations/transactions, and exhaustive state/attempt/fencing rules.
4. `T6.1.1`–`T10.1.4`: immutable intake, exact-byte identity, durable events, controls/checkpoints, and canonical source access.
5. `T11.1.1`–`T13.1.4`: quarantine, recursive budgets, managed content choice, and structural/extraction lineage.

Scale and agent/operator adapters remain blocked until their declared prerequisites and decision tasks pass.

## Evidence discipline

Every task is unchecked. A plan, interface, filename, comment, generated document, or disabled test is not completion evidence. Completion requires the exact active repository ref, changed paths/symbols, migrations/config/schema versions, executed commands and exit codes, mandatory test/fault/security/benchmark results, observability, compatibility, rollout/rollback proof, documentation, review, and artifact hashes.
