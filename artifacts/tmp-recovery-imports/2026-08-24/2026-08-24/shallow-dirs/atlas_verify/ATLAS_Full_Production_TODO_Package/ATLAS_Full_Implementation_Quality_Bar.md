# ATLAS Full Implementation Quality Bar

## Authority

The canonical task registry is the only completion authority. This document summarizes the evidence threshold; it does not create or close tasks.

## Universal completion rule

A capability is not complete because a class, interface, migration stub, README checkbox, diagram, TODO marker, or happy-path test exists. Completion requires all applicable evidence:

1. implementation at the active inspected ref;
2. unit/component verification;
3. integration and end-to-end verification;
4. state/replay/crash/failure evidence for consequential operations;
5. security and malformed-input evidence at every trust boundary;
6. compatibility and stored-data migration evidence;
7. structured observability and operator diagnostics;
8. representative performance/resource evidence where claims are made;
9. documentation and executable examples;
10. rollout, backup, rollback or forward-fix procedure;
11. exact commands, environment/fixture versions, results, and artifact hashes;
12. review approval with no unresolved blocking defect or unapproved skip.

## Priority quality bars

| Priority | Minimum completion evidence | Release effect |
|---|---|---|
| P0 | All universal evidence plus deterministic characterization, adversarial/fault tests, migration/recovery proof, and explicit invariant review. | Blocks all dependent implementation and release. |
| P1 | All applicable universal evidence, native supported-lane verification, failure/recovery, compatibility, observability, and rollback. | Blocks production qualification and release. |
| P2 | Complete capability-specific evidence, contract/security/compatibility proof, and documented optionality. | Blocks claiming or enabling that capability. |
| P3 | Measured adoption trigger, full core-contract conformance, security/chaos/load/operations evidence, and safe disable/rollback. | Optional; cannot weaken or replace the local reference path. |

## Native and emulated environments

* Native lanes are required for operating-system, filesystem, locking, durability, process-control, and isolation support claims.
* Emulated lanes may provide parser, protocol, deterministic fault, and early compatibility evidence.
* An emulated or skipped lane never satisfies a native support gate.
* Every skip/exception has an owner, reason, issue, expiry, assurance impact, and release decision.
* Missing mandatory controls fail closed or produce an explicit reduced-assurance policy decision.

## Evidence integrity

Completion records retain the exact repository SHA and dirty state, tool/dependency versions, environment manifest, fixture/corpus digest, scenario/seed, command/cwd, exit code, raw and normalized results, resource peaks, state/event/lineage evidence, diagnostic artifacts, and SHA-256 hashes. Sensitive or raw untrusted data is excluded unless synthetic and necessary.

## Production-qualification gate

The phrase “production-qualified” is permitted only after `T30.1.6` has executed against approved native lanes and a packaged release candidate, including clean install, predecessor upgrade, migration, sustained workload, process/host/service/storage failures, backup/restore, rollback or forward-fix, security gates, observability, teardown, and independently revalidated evidence.

## Current status

Canonical tasks: **126**  
Completed: **0**  
Incomplete: **126**

This package is an implementation program, not evidence that the proposed architecture has been implemented.
