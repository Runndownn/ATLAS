# ATLAS Full Execution Waves

This document is a navigation projection of the canonical registry, not a second task authority. Task bodies, dependencies, priorities, and completion state are owned only by `Plan_atlas-production/TODO_atlas-production-registry.json`.

| Wave | Task range | Objective | Exit gate |
|---|---|---|---|
| Wave 0 — Baseline and authority closure | `T1.1.1–T1.1.4` | Freeze active ref, resolve documents/donor/component authority. | Exact checkout inventory, command matrix, PDF/donor reconciliation, no product edits. |
| Wave 1 — Current-behavior characterization | `T2.1.1–T2.1.4` | Preserve observable CLI/API/persistence/event/filesystem behavior and expose disputed outputs. | Deterministic fixtures and CI characterization gate. |
| Wave 2 — Semantic and durable foundations | `T3.1.1–T5.1.4` | Normalize pipeline/config, StateStore/migrations, and explicit job/phase/attempt/control state machines. | Versioned contracts, migrations, guarded transitions, model/property tests. |
| Wave 3 — Immutable intake, identity, and events | `T6.1.1–T8.1.4` | Create accepted source generations, persistent content identity, and transactional durable events/outbox. | Downstream phases use occurrence IDs; state/event atomicity design established. |
| Wave 4 — Controls, checkpoints, and source safety | `T9.1.1–T11.1.4` | Make controls/checkpoints durable and route all source/materialization I/O through canonical safe services. | Safe-point controls, stale-checkpoint rejection, quarantine, recursive budgets, lineage. |
| Wave 5 — Content, lineage, plugins, and backends | `T12.1.1–T16.1.4` | Add optional managed content, typed reports/findings/plugins, backend contracts, WorkItems, reuse, and budgets. | Conformance suites and deterministic resource accounting. |
| Wave 6 — Trust, recovery, daemon, and status | `T17.1.1–T20.1.4` | Persist evidence/decisions/publication; define operation semantics/recovery; create daemon/claims; canonical status/telemetry. | Crash/replay matrix, command/status ownership, health/readiness/diagnostics. |
| Wave 7 — External adapters and isolation | `T21.1.1–T23.1.4` | Add versioned REST/events/webhooks, subprocess isolation, retention, compatibility, SDK, and provider extension points. | Adapters pass core contracts; isolation/retention/compatibility evidence. |
| Wave 8 — Continuous quality and release evidence | `T24.1.1–T24.1.4` | Establish supported-platform matrix, advanced verification, reproducible packaging, benchmarks, soak, and rollback. | Mandatory CI policy, SBOM/provenance, representative raw evidence. |
| Wave 9 — Hermetic laboratory | `T28.1.1–T28.1.6` | Provision native/emulated platform, service, isolation, and deterministic fault lanes. | Environment manifests, capability probes, containment, cleanup, and exact result evidence. |
| Wave 10 — Governed corpora and differential verification | `T29.1.1–T29.1.6` | Create synthetic adversarial corpora and contract/property/fuzz/metamorphic runners. | Schema-governed fixtures, native labels, oracles, minimized regressions, conformance catalog. |
| Wave 11 — Advanced proofs and production qualification | `T30.1.1–T30.1.6` | Attempt to falsify lifecycle/source/atomicity/reuse/publication invariants and qualify a release candidate. | Replayable proof counterexamples or passing bounds; native upgrade/rollback/disaster/soak evidence. |
| Wave 12 — Optional measured scale | `T25.1.1–T27.1.4` | Only after measured triggers: PostgreSQL/object storage, remote workers, MCP/UI/deployment governance. | Adapters pass all contracts; chaos/load/security/ops evidence; local reference path retained. |

## Ordering rules

* A later wave may begin only for tasks whose explicit registry dependencies are complete; wave labels do not override the DAG.
* P0/P1 foundations, migration/recovery, and native verification gates precede optional distributed or agent-facing adapters.
* E28–E30 validate implemented capabilities; they do not authorize bypassing unfinished foundation tasks.
* A task remains incomplete until the registry's acceptance and completion-evidence contract is satisfied.

## First implementation sequence

`T1.1.1 → T1.1.2 → T1.1.3 → T1.1.4 → T2.1.1 → T2.1.2 → T2.1.3 → T2.1.4`

This removes stale-baseline risk and freezes observable behavior before the first semantic or storage change.
