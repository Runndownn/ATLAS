@BinReaper Production TODOs

## TODO

* [ ] TODO 61: Define durable `WorkItem` and phase-barrier semantics

  1.2 source task(s): `T16.1.1`
  Priority: `P1`
  Estimated effort: `14 hours`
  Dependencies: `T8.1.4, T9.1.4, T12.1.4, T13.1.4, T15.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/models/work_items.py::WorkItem (create); atlas/core/work_planner.py (create); docs/architecture/work-items.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Model bounded fan-out/fan-in within one phase without introducing generic DAG semantics, alternate phase authority, or dynamic cross-phase dependencies.
  * Restore or protect this invariant: The model supports bounded parallelism while A-F order remains immutable.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend.

  Where this applies

  * Primary affected components: `atlas/models/work_items.py::WorkItem` (create: Represent phase-scoped units, dependencies, state, attempt, and result.); `atlas/core/work_planner.py` (create: Expand validated phase inputs into deterministic work sets.); `docs/architecture/work-items.md` (create: Define barrier, ordering, and non-DAG constraints.)
  * Epic boundary: Phase-internal work items, deterministic reuse, and unified budgets — Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Phase-internal work items, deterministic reuse, and unified budgets.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Model bounded fan-out/fan-in within one phase without introducing generic DAG semantics, alternate phase authority, or dynamic cross-phase dependencies.
  * Component dispositions: `atlas/models/work_items.py::WorkItem` (create: Represent phase-scoped units, dependencies, state, attempt, and result.); `atlas/core/work_planner.py` (create: Expand validated phase inputs into deterministic work sets.); `docs/architecture/work-items.md` (create: Define barrier, ordering, and non-DAG constraints.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define work item identity, phase run, operation/plugin, input references, parent/partition key, deterministic ordinal, state, attempt, dependencies limited to same phase, and result reference.
  * Define phase barrier completion: all required work items terminal and valid aggregation before next semantic phase.
  * Define bounded dynamic expansion only from verified work results with deterministic IDs and depth/count limits.
  * Define optional/skipped/failed item propagation without allowing work items to transition job/phase state directly.

  Security and safety requirements

  * Work-item inputs are immutable references and cannot add source paths or capabilities.
  * Dynamic expansion is bounded, validated, and cannot create cycles or cross-phase edges.
  * Only LifecycleCoordinator closes the phase barrier.
  * Untrusted plugin/model output cannot author new operations outside the allowed planner schema.

  Edge cases and outliers to handle

  * Zero items, one item, millions of items, duplicate deterministic IDs.
  * Required and optional items fail differently.
  * Expansion result arrives after cancel or retry.
  * Aggregator sees partial or conflicting item results.

  Acceptance criteria (“done” definition)

  * The model supports bounded parallelism while A-F order remains immutable.
  * Work-item IDs/order are deterministic for identical phase inputs.
  * Cross-phase dependencies and cycles are structurally impossible or rejected.
  * Barrier closure requires all declared invariants and aggregate validation.

  Testing plan

  * Model/schema tests.
  * Deterministic planning property tests.
  * Cycle/cross-phase negative tests.
  * Zero/large workset tests.
  * Dynamic expansion bound tests.
  * Barrier truth-table tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Model/schema tests., Deterministic planning property tests., Cycle/cross-phase negative tests., Zero/large workset tests., Dynamic expansion bound tests., Barrier truth-table tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T16.1.1`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/models/work_items.py::WorkItem, atlas/core/work_planner.py, docs/architecture/work-items.md.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 62: Implement the bounded local work-item scheduler and aggregation path

  1.2 source task(s): `T16.1.2`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T16.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/core/work_scheduler.py (create); atlas/persistence/repositories/work_items.py (create); atlas/core/work_aggregator.py (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Execute ready work items with explicit concurrency, fairness, cancellation, checkpoint, and resource limits, then validate and aggregate results before phase completion.
  * Restore or protect this invariant: Concurrency never exceeds configured/effective budgets.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend.

  Where this applies

  * Primary affected components: `atlas/core/work_scheduler.py` (create: Select and submit ready phase-scoped work items.); `atlas/persistence/repositories/work_items.py` (create: Persist work-item states and claims.); `atlas/core/work_aggregator.py` (create: Validate required outputs and phase aggregate.)
  * Epic boundary: Phase-internal work items, deterministic reuse, and unified budgets — Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Phase-internal work items, deterministic reuse, and unified budgets.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Execute ready work items with explicit concurrency, fairness, cancellation, checkpoint, and resource limits, then validate and aggregate results before phase completion.
  * Component dispositions: `atlas/core/work_scheduler.py` (create: Select and submit ready phase-scoped work items.); `atlas/persistence/repositories/work_items.py` (create: Persist work-item states and claims.); `atlas/core/work_aggregator.py` (create: Validate required outputs and phase aggregate.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Persist deterministic work plans and ready/running/terminal item states with claims/fencing.
  * Schedule only within current phase using configured per-job/per-phase/per-plugin concurrency and fair queueing.
  * Integrate control polling, cancellation, deadlines, retries, and checkpointable planner cursors.
  * Aggregate accepted results into phase outputs and close the barrier through LifecycleCoordinator.

  Security and safety requirements

  * No scheduler path bypasses WorkSpec, plugin policy, backend conformance, or resource budgets.
  * Queue size, in-memory ready set, and result aggregation are bounded.
  * Cancellation prevents new submissions and fences late results.
  * Fairness policy prevents one job/plugin from starving others.

  Edge cases and outliers to handle

  * Millions of work items exceed memory.
  * One item hangs while others finish.
  * Scheduler crashes after claim before submit.
  * Dynamic expansion floods queue near limits.

  Acceptance criteria (“done” definition)

  * Concurrency never exceeds configured/effective budgets.
  * Ready sets and aggregation remain bounded under large worksets.
  * Crash/restart does not duplicate accepted work effects.
  * Phase barrier closes only after deterministic aggregate validation.

  Testing plan

  * Scheduler unit tests.
  * Concurrency/fairness tests.
  * Million-item planning/streaming benchmark.
  * Crash-after-claim recovery tests.
  * Cancellation/late-result tests.
  * Aggregate partial/conflict tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Scheduler unit tests., Concurrency/fairness tests., Million-item planning/streaming benchmark., Crash-after-claim recovery tests., Cancellation/late-result tests., Aggregate partial/conflict tests..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T16.1.2`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/core/work_scheduler.py, atlas/persistence/repositories/work_items.py, atlas/core/work_aggregator.py.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.

* [ ] TODO 63: Implement exact-key deterministic result reuse

  1.2 source task(s): `T16.1.3`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T16.1.1`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `atlas/artifacts/reuse.py::DeterministicResultIndex (create); atlas/core/reuse_service.py (create); analysis/structure work planners (extend)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Avoid repeated deterministic analysis only when content, operation, plugin/tool/model, config, policy, schema, and relevant environment identities exactly match and outputs verify.
  * Restore or protect this invariant: Reuse occurs only under exact canonical key and verified outputs.
  * Source lineage: Earlier deep-review refinement incorporated under latest-ZIP authority; LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend.

  Where this applies

  * Primary affected components: `atlas/artifacts/reuse.py::DeterministicResultIndex` (create: Index reusable operation results by exact key.); `atlas/core/reuse_service.py` (create: Evaluate eligibility, verify outputs, and record reuse.); `analysis/structure work planners` (extend: Consult reuse without bypassing phase attempts.)
  * Epic boundary: Phase-internal work items, deterministic reuse, and unified budgets — Add bounded parallel work and content-derived computation reuse inside fixed phase barriers while preserving one lifecycle authority and one resource accounting model.
  * Trust boundary: untrusted source/plugin/model/transport/external-system input must cross deterministic ATLAS validation before authoritative state or side effects.

  Repository and authority evidence

  * Evidence mode: ATTACHED-SNAPSHOT; canonical predecessor production package sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; embedded architecture package sha256=c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97.
  * Public ATLAS main page retrieved 2026-08-21 shows branch `main`, 35 commits, the expected root tree, current README, and documented limitations; frozen code baseline remains Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; exact current HEAD/dirty state requires T1.1.1.
  * Latest architecture and earlier deep-review material support this refinement: LATEST-ZIP:ATLAS_Evidence_Driven_Architecture_Blueprint.md:#8 Phase-internal worksets and content-derived memoization; #13 ExecutionBackend; #24 Performance.
  * This is a planning decomposition/new support capability, not a claim that the current repository implements it.

  Current-state assessment and gap analysis

  * The latest canonical package defines ATLAS as a single-process sequential artifact kernel evolving toward a durable lifecycle control plane; this task remains proposed and incomplete.
  * The latest architecture does not define this as a completed repository capability; the earlier deep review identified the supporting responsibility and this plan consolidates it under Phase-internal work items, deterministic reuse, and unified budgets.
  * Evidence limitations: repository paths and runtime commands must be revalidated against the active workspace under A1; document and plan statements are not implementation proof.

  Design and integration strategy

  * Avoid repeated deterministic analysis only when content, operation, plugin/tool/model, config, policy, schema, and relevant environment identities exactly match and outputs verify.
  * Component dispositions: `atlas/artifacts/reuse.py::DeterministicResultIndex` (create: Index reusable operation results by exact key.); `atlas/core/reuse_service.py` (create: Evaluate eligibility, verify outputs, and record reuse.); `analysis/structure work planners` (extend: Consult reuse without bypassing phase attempts.)
  * Preserve one authoritative owner for each state and route all side effects through typed, versioned, testable contracts; adapters and plugins never become lifecycle authority.

  Implementation requirements

  * Define canonical operation key from operation/version, input identities, plugin/tool/model version, config/policy/registry/schema digests, deterministic flag, and declared environment inputs.
  * Persist result digest, output references, findings/report IDs, integrity status, and invalidation reason.
  * Before reuse, verify current policy, output existence/integrity, schema compatibility, and no prior incident.
  * Record a reuse decision/attempt tied to the current job rather than pretending the prior execution reran.

  Security and safety requirements

  * Non-deterministic or AI outputs default non-cacheable unless a stronger reproducibility contract is explicitly proven.
  * Cache keys cannot omit safety policy, model/prompt, external tool, or environment inputs that change output.
  * Corrupt/missing outputs invalidate reuse and create diagnostics.
  * Reuse never grants review or publication authority.

  Edge cases and outliers to handle

  * Plugin version unchanged but code/package hash changed.
  * Same content under new safety/config policy.
  * Output blob removed or retention changed.
  * Partial/failed result accidentally indexed.

  Acceptance criteria (“done” definition)

  * Reuse occurs only under exact canonical key and verified outputs.
  * Every reuse is attributable to original result and current decision.
  * Stale/missing/corrupt/non-deterministic results are not reused.
  * Metrics quantify hit rate and avoided work without losing occurrence provenance.

  Testing plan

  * Exact-key unit/property tests.
  * Omitted-key-component mutation tests.
  * Missing/corrupt output tests.
  * Package/model/prompt version tests.
  * Concurrent index lookup/commit tests.
  * Performance benchmark for duplicate-heavy runs.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until T1.1.1 records the active repository's exact formatter, linter, type-checker, test, migration, benchmark, and packaging commands`; execute this task's named suites with the pinned toolchain and retain the exact command lines and exit codes.
  * Expected evidence: all task acceptance criteria and these test families pass with no unapproved skips: Exact-key unit/property tests., Omitted-key-component mutation tests., Missing/corrupt output tests., Package/model/prompt version tests., Concurrent index lookup/commit tests., Performance benchmark for duplicate-heavy runs..
  * Completion record: retain inspected commit/dirty state, changed paths and symbols, migration/config/schema versions, exact commands and outputs, test/fault/benchmark/security evidence, compatibility and observability results, rollout/rollback proof, documentation, reviewer approval, and artifact hashes.

  Debugging checklist

  * Start from the first failed invariant or acceptance criterion for `T16.1.3`; do not infer success from partial rows, emitted events, logs, filenames, or process exit alone.
  * Trace authoritative identities and versions across the affected components: atlas/artifacts/reuse.py::DeterministicResultIndex, atlas/core/reuse_service.py, analysis/structure work planners.
  * Inspect state transition, transaction boundary, idempotency/fencing identity, resource budget, policy decision, and retained evidence before retrying or cleaning up.
  * Reproduce with the smallest versioned fixture, enable bounded structured diagnostics, compare against the characterization baseline, and preserve the failing artifact/seed without secrets.
