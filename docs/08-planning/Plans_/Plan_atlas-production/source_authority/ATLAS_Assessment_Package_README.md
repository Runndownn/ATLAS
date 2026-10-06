# ATLAS Assessment Package

This directory contains the read-only architecture and implementation-planning package produced on 2026-08-21.

## Primary deliverables

- `ATLAS_Evidence_Driven_Architecture_Blueprint.md` — complete 30-section assessment in the requested order, including current-state reconstruction, requirements, gaps, donor dispositions, options, target architecture, data/state/event/provenance/plugin/security/observability designs, changeset map, ADRs, roadmap, 24 detailed task specifications, tests, migration, failure recovery, performance, threat model, release strategy, risks, open questions, and immediate actions.
- `ATLAS_Execution_Plan.md` — standalone execution plan using the repository-quality task contract. It contains 24 independently reviewable tasks and passes the bundled structural linter with zero errors and zero warnings.
- `ATLAS_Evidence_Ledger.csv` — stable evidence IDs with source, observation, implication, confidence, and follow-up.
- `ATLAS_Task_Registry.json` — machine-readable task registry.
- `ATLAS_Requirements_Register.csv` — 30 extracted product-direction requirements, each marked for original-document revalidation.
- `ATLAS_ADR_Index.csv` — 13 decision records and their core decisions/validation.
- `ATLAS_Risk_Register.csv` — 18 ranked technical/architectural risks.
- `ATLAS_Assessment_Validation.json` — machine-readable structural and consistency checks.
- `ATLAS_Assessment_Manifest.json` — SHA-256 hashes and byte sizes for the package.

## Frozen evidence boundary

- ATLAS line-level baseline: `efa547cafc64b58d60d19dcc1e5ba32c6b046bc5`
- Yggdrasil donor baseline: `2b0c51b6132c2a16e63fc2e2de2d2b4598b5fe40`

On 2026-08-21 the ATLAS repository was publicly visible on `main`, but the exact current HEAD SHA was not exposed through the available fetch path. The Yggdrasil URL returned 404. The original 34-page product-direction document was not separately accessible; its page references are preserved from the attached frozen assessment. These are explicit pre-implementation revalidation gates, not silently ignored limitations.

## Recommended implementation start

Begin with AT-001 through AT-010. Do not introduce distributed infrastructure or broader interfaces before the canonical lifecycle order, StateStore migrations, explicit transitions, immutable intake, persistent content identity, atomic event history/outbox, durable controls/checkpoints, canonical source access, quarantine, and recursive archive budgets pass their failure/restart gates.
