@BinReaper Production TODOs

## TODO

* [ ] TODO 112: Build isolated process, container, and resource-control test lanes

  1.2 source task(s): `T28.1.4`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.1, T22.1.3, T22.1.4`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/lab/environments/isolation/ (create); tests/execution/isolation_conformance/ (create); scripts/run_isolation_matrix.py (create); docs/security/execution-isolation-assurance.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Verify subprocess and future worker isolation under realistic host controls without making containers a core dependency.
  * Restore or protect this invariant: Untrusted plugins receive only declared capabilities and cannot outlive, escape, or mutate authority beyond the mediated WorkSpec.
  * Source lineage: Expansion of T22.1.1-T22.1.4 and deep-review Plugin Security; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/lab/environments/isolation/` (create: Declare rootless container, namespace/cgroup, Job Object, and reduced-assurance lanes.); `tests/execution/isolation_conformance/` (create: Prove filesystem, network, process, environment, secret, and resource boundaries.); `scripts/run_isolation_matrix.py` (create: Execute one hostile WorkSpec corpus across backends.); `docs/security/execution-isolation-assurance.md` (create: State enforced, detected, advisory, and unsupported controls.)
  * Epic boundary: E28 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/lab/environments/isolation/` (create: Declare rootless container, namespace/cgroup, Job Object, and reduced-assurance lanes.); `tests/execution/isolation_conformance/` (create: Prove filesystem, network, process, environment, secret, and resource boundaries.); `scripts/run_isolation_matrix.py` (create: Execute one hostile WorkSpec corpus across backends.); `docs/security/execution-isolation-assurance.md` (create: State enforced, detected, advisory, and unsupported controls.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Treat isolation as a control matrix, not a boolean; separate prevention, detection, cleanup, and reduced assurance.
  * Use rootless containers/namespaces/cgroups, Windows Job Objects/restricted tokens, and explicit macOS limitations.
  * Run one backend conformance corpus so execution location changes but WorkSpec/WorkResult semantics do not.
  * Do not grant test lanes StateStore credentials or production source/destination paths.

  Implementation requirements

  * Probe identity, mounts, network, environment, process tree, CPU, memory, PIDs, file/output/temp limits, timeouts, and tools.
  * Provision read-only code/input, attempt-owned writable workspace, synthetic secrets, fake dependencies, and bounded evidence output.
  * Run trusted in-process, subprocess, rootless-container, and native restricted-process lanes against identical benign and hostile WorkSpecs.
  * Record enforced/advisory controls and reject plugin/backend combinations whose requirements exceed the lane.
  * Verify kill escalation, descendant cleanup, mount/socket leakage, quota accounting, and crash reconciliation.

  Security and safety requirements

  * Never mount container sockets, home directories, SSH agents, cloud credentials, signing material, or host-wide writable paths.
  * Use inert hostile fixtures under a second outer quota boundary.
  * Quarantine runners on surviving process, mount, listener, or writable host change.
  * Expose control degradation as a structured denial, not an unrestricted fallback.

  Edge cases and outliers to handle

  * Runtime is absent, rootful only, or misconfigured.
  * Children change process group/session or spawn grandchildren during termination.
  * Controllers appear available but are not delegated.
  * Output flood fills evidence before process limits fire.
  * A hosted platform cannot enforce required network/resource controls.

  Acceptance criteria (“done” definition)

  * Every backend publishes an enforced/detected/advisory/unsupported control matrix and passes valid-result conformance.
  * Hostile fixtures cannot reach undeclared files, secrets, networks, tools, StateStore, or surviving process authority under claimed controls.
  * Timeout/resource/protocol/controller failures produce deterministic results and external cleanup evidence.
  * Policy refuses unsupported plugin/backend combinations instead of downgrading silently.

  Testing plan

  * Capability-probe and policy-decision tests.
  * Benign backend semantic conformance tests.
  * Filesystem/network/environment/secret negative tests.
  * CPU/memory/PID/file/output/time exhaustion tests.
  * Process-group escape and descendant-survival tests.
  * Controller/runner crash reconciliation tests.
  * Cross-platform reduced-assurance policy tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until backend names and platform lanes exist`; execute the common isolation matrix through T28.1.1.
  * Expected evidence: probes, conformance, hostile denials, resource faults, cleanup, crash reconciliation, and downgrade tests pass.
  * Completion record: backend/control versions, lane manifests, corpus digest, commands, process/resource evidence, leaks/cleanup, assurance report, hashes.

  Debugging checklist

  * Inspect selected backend, grants, capability probes, and outer limits first.
  * Capture process tree, containment membership, mounts, sockets, environment allowlist, and resource counters.
  * Reproduce one hostile action under the smallest limit.
  * Verify cleanup from outside the isolation boundary, not from child exit status.

* [ ] TODO 113: Build deterministic dependency-service and transport emulators

  1.2 source task(s): `T28.1.5`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.1, T4.1.4, T8.1.4, T21.1.3`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/lab/services/ (create); tests/doubles/ (create); tests/integration/test_service_failure_matrix.py (create); docs/testing/service-emulation.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Provide deterministic doubles and pinned native services for dependency and transport failure testing.
  * Restore or protect this invariant: Dependencies and transports never become authoritative; outage, delay, duplication, or corruption yields deterministic state and recoverable evidence.
  * Source lineage: Expansion of T4.1.4, T8.1.3-T8.1.4, T21.1.2-T21.1.4, and T25; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/lab/services/` (create: Define pinned SQLite, RabbitMQ, fake HTTP/webhook, and optional adapter lanes.); `tests/doubles/` (create: Provide deterministic service doubles with scripted faults and bounded logs.); `tests/integration/test_service_failure_matrix.py` (create: Verify outage, delay, duplicate, reorder, corruption, and recovery.); `docs/testing/service-emulation.md` (create: Document fidelity, native gates, and limitations.)
  * Epic boundary: E28 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/lab/services/` (create: Define pinned SQLite, RabbitMQ, fake HTTP/webhook, and optional adapter lanes.); `tests/doubles/` (create: Provide deterministic service doubles with scripted faults and bounded logs.); `tests/integration/test_service_failure_matrix.py` (create: Verify outage, delay, duplicate, reorder, corruption, and recovery.); `docs/testing/service-emulation.md` (create: Document fidelity, native gates, and limitations.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Use deterministic doubles for fast faults and pinned native services for driver/protocol proof; mocks alone cannot prove native behavior.
  * Script faults by stable scenario ID and logical boundary instead of uncontrolled sleeps.
  * Capture requests, responses, delivery tags, duplicates, delays, resets, and injected faults in bounded logs.
  * Keep optional PostgreSQL/object-store lanes disabled until evidence-gated tasks authorize them.

  Implementation requirements

  * Define service manifests and probes for SQLite modes, RabbitMQ, loopback HTTP/webhook, and optional PostgreSQL/object storage.
  * Implement scenarios for unavailable, timeout, slow, duplicate, reorder, reset, malformed, poison, and ambiguous-commit outcomes.
  * Expose test APIs to arm one fault at a named operation boundary and assert exact requests/effects.
  * Run adapters against doubles and pinned native services, comparing normalized state/event/outbox/publication outcomes.
  * Use per-run synthetic credentials, ports, volumes, networks, and bounded logs; destroy them after evidence capture.

  Security and safety requirements

  * Bind to isolated networks or loopback and block cloud metadata/arbitrary egress.
  * Generate per-run credentials/certificates and exclude them from retained output.
  * Reject non-lab destinations in fake HTTP/webhook services.
  * Validate all malformed service/event input by schema, correlation, and identity.
  * Never connect tests to shared production brokers, databases, stores, or webhooks.

  Edge cases and outliers to handle

  * Double and native service differ on ordering, acknowledgement, timeout, or connection semantics.
  * Fault arming races with concurrent requests.
  * Service restarts with durable data but a new epoch.
  * Native image/tag changes without manifest update.
  * Cleanup fails while messages, connections, or volumes remain.

  Acceptance criteria (“done” definition)

  * Every supported adapter has deterministic-double tests and a pinned native integration lane before support is claimed.
  * Outage, timeout, duplicate, reorder, poison, malformed, and ambiguous scenarios produce specified retry/reconciliation evidence.
  * No emulator or service can mutate lifecycle state except through canonical contracts.
  * Services, credentials, ports, networks, and volumes are per-run, bounded, and verifiably removed.

  Testing plan

  * Scenario parser and deterministic sequencing tests.
  * Double/native differential tests.
  * Outage, delay, reset, restart, duplicate, reorder, poison, and DLQ tests.
  * Malformed-response and event-injection tests.
  * Ambiguous-effect reconciliation tests.
  * Credential redaction and network-containment tests.
  * Teardown and volume-cleanup tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until service definitions and adapter commands exist`; execute through the lab with pinned digests.
  * Expected evidence: double/native tests, differentials, outage/replay/reconciliation scenarios, and teardown/security checks pass.
  * Completion record: service/image/driver versions, scenario IDs, manifests, commands, request/effect logs, state/event evidence, teardown, secret scan, hashes.

  Debugging checklist

  * Distinguish ATLAS, scenario script, network, driver, and native service failures.
  * Compare scenario step, correlation/idempotency IDs, request log, outbox, and authoritative transition.
  * Reproduce with one connection and one armed fault without sleeps.
  * Preserve bounded protocol traces and normalized state diff without credentials.

* [ ] TODO 114: Implement deterministic time, disk, memory, network, and crash fault injection

  1.2 source task(s): `T28.1.6`
  Priority: `P1`
  Estimated effort: `16 hours`
  Dependencies: `T28.1.1, T18.1.4, T24.1.2`
  Evidence basis: `ATTACHED-SNAPSHOT`
  Repository scope: `tests/faults/injector.py (create); tests/faults/scenarios/ (create); atlas/testing/fault_hooks.py (create); scripts/run_fault_matrix.py (create); docs/testing/fault-injection.md (create)`
  Required authorities: `ATLAS_Production_TODO_Package.zip; ATLAS_Assessment_Package.zip; ATLAS_Evidence_Driven_Architecture_Blueprint.md; ATLAS_Execution_Plan.md; ATLAS.pdf; Pasted markdown.md; Pasted markdown (2).md; Pasted markdown (3).md; Pasted markdown (4).md; ATLAS_Assessment_Validation.json; GitHub repository main page retrieved 2026-08-21; atlas/core/orchestrator.py; unresolved: repository tree at frozen commit; repository tree at frozen donor commit`

  Purpose / Why this exists

  * Make crash and resource-failure verification deterministic rather than timing-dependent.
  * Restore or protect this invariant: Each named fault point has an exact allowed durable state, duplicate-effect policy, recovery decision, and retained evidence.
  * Source lineage: Expansion of T18.1.4, T24.1.2, and deep-review crash-point matrix; predecessor package and full direction PDF.

  Where this applies

  * Primary affected components: `tests/faults/injector.py` (create: Expose named deterministic fault points and typed injected failures.); `tests/faults/scenarios/` (create: Version crash, clock, disk, memory, network, lock, and process scenarios.); `atlas/testing/fault_hooks.py` (create: Provide test-only no-op seams at selected boundaries, disabled in production.); `scripts/run_fault_matrix.py` (create: Execute repeated scenarios and emit machine-readable recovery results.); `docs/testing/fault-injection.md` (create: Document fault fidelity, safety, and oracles.)
  * Epic boundary: E28 — test-laboratory, corpus, proof, and production-qualification work; it validates but never owns product lifecycle state.
  * Trust boundary: all hostile inputs, emulators, fault injectors, and external-service doubles run in disposable, bounded environments with synthetic identities and no production authority.

  Repository and authority evidence

  * Canonical predecessor production package: ATLAS_Production_TODO_Package.zip sha256=ca960729b67579b1b08fdedea786feb4594d0649353521c9dbcaf0f2fdb2d09f; all 108 predecessor tasks remain authoritative and incomplete.
  * Frozen implementation baseline: Runndownn/ATLAS@efa547cafc64b58d60d19dcc1e5ba32c6b046bc5; current public main page retrieved 2026-08-21 shows `main`, 35 commits, expected root surfaces, and the same documented remaining limitations.
  * Current frozen CI evidence: `.github/workflows/tests.yml` is Linux/Python 3.13 test-only; README documents `python -m pytest tests/ -v` but no run was executed in this planning workflow.
  * Deep-review source: `Pasted markdown (2).md`, Stage 8 security review, Stage 9 performance/resource review, and Stage 16 testing architecture upgrade.
  * Proposed component surface: `tests/faults/injector.py` (create: Expose named deterministic fault points and typed injected failures.); `tests/faults/scenarios/` (create: Version crash, clock, disk, memory, network, lock, and process scenarios.); `atlas/testing/fault_hooks.py` (create: Provide test-only no-op seams at selected boundaries, disabled in production.); `scripts/run_fault_matrix.py` (create: Execute repeated scenarios and emit machine-readable recovery results.); `docs/testing/fault-injection.md` (create: Document fault fidelity, safety, and oracles.)
  * This is a planned repository change; path creation and command execution require active-checkout verification under T1.1.1.

  Current-state assessment and gap analysis

  * The predecessor package contains 108 implementation tasks and broad test requirements, but it does not yet provide an executable, versioned laboratory that proves platform, filesystem, service, and fault assumptions.
  * The current public repository documents a Linux/Python 3.13 test command and 67 tests; no native multi-platform, fault-laboratory, or production-qualification execution evidence was supplied.
  * This task is proposed work. Test plans, future paths, and completion markers are not implementation proof.

  Design and integration strategy

  * Prefer narrow dependency seams and test hooks at transaction/side-effect boundaries over broad monkeypatching.
  * Separate logical faults from host faults and label fidelity.
  * Use stable scenario IDs, barriers, deterministic seeds, and external observers instead of sleeps.
  * Ensure release builds default hooks to no-op and cannot arm them through user configuration.

  Implementation requirements

  * Enumerate pre/post points for transitions, events/outbox, checkpoints, hash/CAS, extraction, plugins, controls, publication, and cleanup.
  * Implement injectable clocks for forward/backward wall time, deadlines, lease expiry, and stale timestamps while preserving monotonic ordering.
  * Create bounded disk/inode/permission/SQLite-lock, memory/PID/output, network, pause, SIGTERM, and SIGKILL lanes.
  * Define expected rows/files/events, unknown outcomes, recovery/reconciliation, retry, cleanup, and evidence for every scenario.
  * Repeat critical scenarios and compare normalized outcomes; quarantine nondeterministic cases.

  Security and safety requirements

  * Fault arming is test-only and inaccessible from production config, APIs, and plugins.
  * Apply outer ceilings so resource faults cannot destabilize the host.
  * Limit network faults to isolated lab networks and synthetic services.
  * Retain no raw memory/content unless synthetic, bounded, and required.
  * Fail tests that cannot prove cleanup or evidence preservation.

  Edge cases and outliers to handle

  * The real side effect occurs before the intended logical hook.
  * Clock changes affect harness timeouts or certificates.
  * Host OOM kills the controller instead of target.
  * Disk-full prevents writing diagnostic evidence.
  * Scheduling differs despite the same scenario ID.

  Acceptance criteria (“done” definition)

  * Critical transaction and side-effect boundaries have named fault points or explicit host-fault rationale.
  * Three repeated critical runs produce equivalent normalized durable state and recovery decisions.
  * Fault hooks cannot be armed through production configuration, APIs, plugins, or release artifacts.
  * Resource/crash scenarios remain bounded and verify cleanup externally.

  Testing plan

  * Hook enable/disable and production-inaccessibility tests.
  * Scenario parser, barrier, seed, and repeatability tests.
  * Clock/deadline/lease tests.
  * Disk/inode/permission/SQLite lock tests.
  * Memory/PID/output/time-limit tests.
  * Network partition/reset/delay tests.
  * SIGTERM/SIGKILL/controller-loss recovery tests.

  Validation and completion evidence

  * Commands to run: `UNRESOLVED until fault points and runner exist`; execute named scenarios through the lab controller.
  * Expected evidence: hook safety, repetition, clock/resource/network/process faults, recovery oracles, and external cleanup all pass.
  * Completion record: hook version, scenario digest, lane manifest, commands, normalized outcomes, flakes, recovery/cleanup evidence, hashes.

  Debugging checklist

  * Confirm the intended hook fired exactly once and capture pre/post durable state.
  * Separate injection failure from product recovery failure.
  * Use external observers after hard kills instead of in-process callbacks.
  * Minimize to one operation, barrier, fault, and seed before expanding.
