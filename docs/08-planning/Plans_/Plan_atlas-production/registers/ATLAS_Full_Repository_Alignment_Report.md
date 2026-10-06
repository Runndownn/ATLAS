# ATLAS Full Repository Alignment Report

## Scope and evidence mode

Evidence mode: **ATTACHED-SNAPSHOT with selective public-repository verification**.

This package preserves the predecessor production TODO registry (`sha256:ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f`) as the canonical task authority. It also preserves the architecture assessment package (`sha256:c2571cf6f6582a3e86f487e7ae817641d3b74e4425fe49e97889c9a29d9f9b97`), the attached 34-page product-direction PDF (`sha256:39cbb7ccf8384802ff45357fdf9d7abed2f00b94e62eaefadf14c2708b8fd31b`), and selected public GitHub observations retrieved on 2026-08-21.

No ATLAS checkout was available in the execution environment. The public repository perimeter exposed `main`, 35 commits, the expected root tree, the current README, and documented commands/limitations, while the exact current `main` SHA and local dirty state were not independently returned. Therefore:

* executable-code claims remain frozen to `Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5`;
* exact current-ref equivalence remains **UNRESOLVED** and is the first gate in `T1.1.1`;
* no repository command, test, migration, benchmark, build, deployment, or runtime result is claimed as executed here;
* no source file, branch, commit, pull request, deployment, or issue was created or modified.

## Frozen implementation reconstruction

| Surface | Frozen path / symbol | Implemented behavior established by the canonical assessment | Target disposition |
|---|---|---|---|
| Composition | `atlas/core/runtime.py::AtlasRuntime` | Builds the in-process job store, event bus, shared helpers, six handlers, and orchestrator; some dependencies are inconsistently wired. | Refactor into one validated composition root while preserving public construction compatibility. |
| Orchestration | `atlas/core/orchestrator.py::PipelineOrchestrator` | Starts an `asyncio` task, iterates caller-supplied phases sequentially, owns a process-local active-job map, and checks controls at phase boundaries. | Preserve six ordered semantic barriers; replace ad hoc mutation with durable state-machine services. |
| Persistence | `atlas/core/job_store.py::JobStore` | Inline SQLite jobs/phases/events tables with independent commits; no migrations, attempts, checkpoints, controls, source identity, evidence, or publication records. | Introduce `StateStore`, explicit transactions, numbered migrations, backup/restore, and conformance tests. |
| Events | `atlas/core/event_bus.py` and orchestrator event persistence | Lifecycle events are published and persisted separately; phase-detail events are transport-only; RabbitMQ is publisher-only with fallback. | Separate authoritative state, durable event history, transactional outbox, and optional transport. |
| Lifecycle contracts | `atlas/phases/base.py` | Job and phase reuse one coarse status enum; retryable metadata exists without attempt semantics or durable policy. | Define explicit job/phase/attempt/control state machines and guards. |
| Reconnaissance | `atlas/phases/reconnaissance.py` | Traverses live source paths, records risk flags and archive assessments. | Consume an accepted immutable intake generation and canonical source-access service. |
| Fingerprinting | `atlas/phases/fingerprinting.py` and `atlas/storage/hash_store.py` | Re-traverses live paths and stores hashes in memory/job metadata; not a durable CAS. | Persist occurrence-to-content identity using canonical SHA-256; optional managed content store later. |
| Structural discovery | `atlas/phases/structural_discovery.py` | Performs shallow ZIP/TAR inspection; nested containers are counted, not recursively governed. | Persist exact `StructuralReport` records under cumulative recursive budgets. |
| Extraction | `atlas/phases/extraction.py` | Reassesses and extracts beside the source into `<stem>_extracted`; durable derivation/output manifests are absent. | Materialize only exact accepted reports into attempt-owned quarantine with lineage and cleanup. |
| Analysis | `atlas/phases/analysis.py` | Runs arbitrary in-process plugins over live paths and stores bounded dictionary results in metadata. | Introduce typed descriptors/findings, capability policy, backend isolation, result validation, and durable evidence. |
| Review | `atlas/phases/review.py` | Creates ephemeral evidence/promotion candidates and summaries; no authoritative decision/publication model. | Persist evidence, review decisions, publication attempts, verification, and bidirectional lineage. |
| Filesystem safety | `atlas/safety/filesystem_discovery.py`, `archive_safety.py`, `path_safety.py` | Useful helpers exist but do not form one canonical race-resistant access path; `PathSafetyService` is not consistently wired. | Route every trusted open/list/stat/temp/destination operation through canonical services. |
| Schema package | `atlas/schema/__init__.py` | Describes migration behavior but only re-exports the inline schema. | Replace documentation-only migration surface with versioned migration authority. |
| CLI | `atlas/cli.py` | Starts/list/gets jobs through the local runtime; no daemon/API command service. | Preserve commands while routing mutations through canonical command/status services. |
| Tests | `tests/` nine frozen modules | Mostly unit/happy-path coverage for current kernel; no comprehensive state, crash, migration, adversarial, cross-platform, or soak evidence. | Preserve characterization tests and add the complete laboratory/corpus/proof program in E28–E30. |
| CI | `.github/workflows/tests.yml` | Linux/Python 3.13 test-only frozen workflow. | Establish explicit supported/reduced-assurance matrix and mandatory release-quality gates. |

## Repository/document conflicts retained

1. The README's “content-addressable” and automatic-deduplication wording is stronger than the frozen in-memory `HashStore` implementation. The target plan distinguishes durable identity from optional managed CAS.
2. The README's completed-slice and hardening markers are documentation only; task completion requires implementation, tests, runtime evidence, migration/rollback, observability, and retained hashes.
3. The public README contained future-dated project/sprint history relative to the retrieval date. It is retained as schedule/document evidence, not proof of executed work.
4. The schema package wording implies migrations that are not implemented in the frozen code.
5. Public repository consistency with the frozen SHA is strongly suggested by visible structure and selected code, but exact current HEAD remains unresolved.

## Alignment rules for implementation

* Re-read every target file at the active ref immediately before editing.
* Keep one authoritative owner for every state, identity, transition, policy, checkpoint, event, and publication.
* Preserve the ordered six-stage lifecycle; phase-internal work may parallelize only behind a phase barrier.
* Paths are locators, never content identity.
* Structural inspection precedes materialization.
* Findings, evidence, decisions, and publication are distinct records.
* Plugins, transports, workers, models, UIs, and test infrastructure cannot write lifecycle authority directly.
* SQLite/local execution remain the reference path; optional scale adapters must pass the same contracts after measured triggers.
* Emulated environments identify risk and parser behavior; only native lanes establish platform support.
* Anything that may execute twice must define idempotency and reconciliation before retry.
* No capability is complete without implementation, required tests, failure evidence, observability, compatibility/migration, documentation, rollback, and retained completion evidence.

## Resulting plan delta

The 108 predecessor tasks remain intact. E28–E30 add 18 sprint-fit tasks for:

* hermetic native/emulated test environments and exact assurance manifests;
* Linux, Windows, and macOS filesystem/process behavior;
* subprocess/container/resource-control isolation;
* deterministic service doubles and native dependencies;
* deterministic clock, disk, memory, network, and crash fault injection;
* governed filesystem, archive, plugin, persistence, event, and concurrency corpora;
* cross-platform/backend/version contract differentials;
* property, fuzz, mutation, and metamorphic verification;
* bounded lifecycle model checking with executable counterexample replay;
* source-mutation, state/event atomicity, CAS/reuse, and publication proofs;
* production qualification through clean install, upgrade, rollback, disaster recovery, security, benchmark, and soak evidence.

All 126 tasks remain proposed and incomplete.
