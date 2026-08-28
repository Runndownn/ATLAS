# ATLAS Production TODO Package

This package converts the canonical ATLAS architecture assessment into one deterministic, implementation-grade TODO system. It is a read-only planning deliverable: no ATLAS or Yggdrasil repository files were modified, and no task is marked complete.

## Canonical authority

`Plan_atlas-production/TODO_atlas-production-registry.json` is the **only editable task authority**. Every Markdown plan, machine-readable index, manifest, and PART1 pack is generated from that registry.

Authority order for this package:

1. `ATLAS_Assessment_Package.zip` — latest truth for architecture, frozen findings, requirements, ADRs, risks, and 24 macro tasks.
2. `ATLAS.pdf` — primary desired-direction source, used to revalidate the latest package's 30 requirements.
3. Earlier prompts and plans — supporting analysis only; they cannot override the latest ZIP.
4. Frozen ATLAS and Yggdrasil code citations — pending primary workspace/archive verification.

## Package summary

| Item | Count |
|---|---:|
| Epics | 27 |
| Canonical tasks | 108 |
| P0 | 44 |
| P1 | 40 |
| P2 | 12 |
| P3 | 12 |
| Estimated hours | 1,566 |
| Original macro tasks covered | 24 / 24 |
| Justified refinement tasks | 12 |
| PART1 documents | 36 |
| Tasks per PART1 | 3 |
| Completed | 0 |
| Incomplete | 108 |

The 12 refinements are not unrelated features. They make the latest architecture implementable by adding evidence reconciliation, bounded phase-internal work, deterministic reuse, unified budgets, retention, compatibility, plugin SDK, and source-provider contracts.

## Directory layout

```text
ATLAS_Production_TODO_Package/
├── README.md
├── PART1_HEADER.md
├── ATLAS_Production_Source_Manifest.json
├── ATLAS_Production_Source_Delta_Report.md
├── ATLAS_Production_Task_Crosswalk.csv
├── ATLAS_Production_Macro_Coverage.csv
├── ATLAS_Production_PDF_Requirements_Revalidation.csv
├── ATLAS_Production_Component_Responsibility_Matrix.csv
├── ATLAS_Production_TODO_Validation.json
├── ATLAS_Production_Package_Manifest.json
├── tools/
│   ├── canonical-registry.schema.json
│   ├── todo_system_lib.py
│   ├── generate_todo_system.py
│   └── validate_todo_system.py
└── Plan_atlas-production/
    ├── Plan-MASTER_atlas-production.md
    ├── TODO_atlas-production-registry.json
    ├── TODO_atlas-production-manifest.json
    ├── TODO-MASTER_atlas-production-v2.1/
    │   └── TODO-MASTER_atlas-production-v2.1.md
    ├── TODO_atlas-production-v1.2/
    │   └── TODO_atlas-production-v1.2.md
    └── TODO_atlas-production-PART1/
        ├── TODO_atlas-production-PART1-1.md
        └── ... through PART1-36.md
```

Every PART1 file begins byte-for-byte with the operator header in `PART1_HEADER.md` and contains exactly three consecutive canonical TODOs.

## Use

Validate the existing package from its extracted root:

```bash
python3 tools/validate_todo_system.py --registry Plan_atlas-production/TODO_atlas-production-registry.json --plan-dir Plan_atlas-production --part1-header PART1_HEADER.md
```

Preview regeneration without writing:

```bash
python3 tools/generate_todo_system.py --registry Plan_atlas-production/TODO_atlas-production-registry.json --part1-header PART1_HEADER.md --output-root .
```

Regenerate after an intentional registry edit:

```bash
python3 tools/generate_todo_system.py --registry Plan_atlas-production/TODO_atlas-production-registry.json --part1-header PART1_HEADER.md --output-root . --apply --replace-conflicts
python3 tools/validate_todo_system.py --registry Plan_atlas-production/TODO_atlas-production-registry.json --plan-dir Plan_atlas-production --part1-header PART1_HEADER.md --write-validation
```

`--replace-conflicts` is intentionally explicit. Review generated-file differences before using it.

## Editing rules

* Edit the canonical registry only.
* Keep task sequence contiguous and dependencies backward-pointing.
* Keep task estimates between 1 and 16 hours.
* Keep the total task count divisible by three; do not add filler.
* Preserve stable IDs unless a task is genuinely replaced.
* Add one validation task per unresolved assumption.
* Do not mark a task complete without implementation, integration, mandatory tests, security and observability evidence, migration/rollout/rollback proof, documentation, review, and hashes.
* Do not manually edit v1.2, v2.1, PART1, or manifest projections.
* Re-run validation after every registry change.

## Evidence limitations that block implementation claims

* The current ATLAS workspace was not supplied. `T1.1.1` must verify the active ref, dirty state, paths, symbols, repository authorities, and exact commands.
* The Yggdrasil source archive was not supplied. `T1.1.3` blocks donor reuse until code, dependencies, tests, and license provenance are verified.
* The PDF confirms desired direction, not current code behavior.
* Exact platform support, content retention mode, review actor policy, retention periods, scale triggers, and deployment tenancy remain explicit assumptions with one validation task each.

## Architectural invariant

ATLAS remains a sequential artifact lifecycle control plane:

`Reconnaissance → Fingerprinting → Structural Discovery → Controlled Extraction → Deep Understanding → Review / Promotion`

Infrastructure may change where work executes or where bytes/state are stored. It may not create another lifecycle authority or change the meaning of those six barriers.
