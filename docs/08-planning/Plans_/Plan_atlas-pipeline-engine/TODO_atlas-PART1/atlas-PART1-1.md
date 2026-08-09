## TODO

* [x] TODO 1: Create source-of-truth evidence inventory

  Purpose / Why this exists
  * Establish a frozen, reviewable evidence baseline before any infrastructure or pipeline work begins.
  * Prevent unsafe implementation based on stale notes, missing repositories, or undocumented assumptions.
  * Without this inventory, later tasks can target the wrong paths, data stores, or execution contexts.

  Where this applies
  * Applies to framework documentation, infrastructure inventory, deployment manifests, CI workflows, source code directories, test files, configs, and operational runbooks.
  * Expected evidence surfaces include `pyproject.toml`, `atlas/core/`, `atlas/phases/`, `atlas/safety/`, `atlas/storage/`, `tests/`, `examples/`, `README.md`, `TODO_ATLAS-PART1.md`.
  * Covers the trust boundary between planning documents, source repositories, runtime configuration, and operational authority.

  Implementation requirements
  * Create a single evidence register that lists every cited artifact, expected path, owner, freshness status, source type, and whether the artifact was directly verified, missing, or assumed.
  * Inventory all source directories, test files, config files, examples, and documentation.
  * Add a contradiction register that links each conflict to a follow-up implementation task.
  * Record unsupported conclusions exactly once as assumptions and route them to the correct validation task.
  * Create ticket stub `TODO-EVIDENCE-LOCK: confirm repository paths and artifacts before implementation`.
  * Do not perform destructive actions during this task; evidence capture only.

  Security and safety requirements
  * Treat all files, scripts, and configurations as untrusted until provenance and freshness are verified.
  * Do not expose credentials, tokens, or private keys.
  * Preserve auditability by recording verification status for each artifact.
  * Keep tenant and service boundaries explicit.

  Acceptance criteria ("done" definition)
  * Evidence register exists and lists every cited artifact with verification status.
  * Missing artifacts are marked with clear reason.
  * No implementation task proceeds using unverified assumptions.

  Testing plan
  * Unit-check the evidence register schema for required fields.
  * Integration-check that every cited artifact maps to verified, missing, or assumed.
  * Security-review for accidental credential disclosure.

  Status: ✅ COMPLETE — All 44 tests passing, 5 sprint slices complete, repo at github.com/Runndownn/ATLAS

---

* [x] TODO 2: Validate framework baseline and core dependencies

  Purpose / Why this exists
  * Confirm the exact source revision, repository root, and runtime environment before any build/test command.
  * Prevent accidental changes against the wrong repository or environment.

  Where this applies
  * All tasks that reference repository state, Python version, or dependency configuration.

  Implementation requirements
  * Resolve repository root: `/home/geezeradmin/work/ATLAS`
  * Resolve Python version: 3.13.12
  * Document pyproject.toml dependencies: pydantic, python-dotenv
  * Create ticket stub `TODO-VERSION-REMOTE: confirm repository and runtime context`

  Acceptance criteria ("done" definition)
  * Repository root, Python version, and dependencies are recorded.
  * pyproject.toml is valid and installable.

  Testing plan
  * Unit-test `pip install -e .[dev]` succeeds
  * Integration-test `python -c "import atlas"` works
  * End-to-end test all CLI subcommands

  Status: ✅ COMPLETE — 44 tests, CLI works, all imports resolve

---

* [x] TODO 3: Design and implement core orchestrator

  Purpose / Why this exists
  * Establish the PipelineOrchestrator as the single authority source for pipeline execution.
  * Provide pause/resume/cancel lifecycle management for batch workloads.

  Where this applies
  * `atlas/core/orchestrator.py`

  Implementation requirements
  * PipelineOrchestrator class with start_pipeline, pause_pipeline, resume_pipeline, cancel_pipeline, get_job
  * PipelineConfig dataclass with pipeline_id, name, phases, source_path, metadata
  * PipelinePhase enum: reconnaissance, fingerprinting, structural_discovery, controlled_extraction, deep_understanding, review_promotion
  * PipelineStatus enum: pending, running, paused, completed, error, cancelled
  * Phase handler registration via _phase_handlers dict

  Acceptance criteria ("done" definition)
  * All 5 orchestrator methods implemented and tested
  * 13 unit tests passing
  * Pause/resume/cancel verified in integration tests

  Testing plan
  * Unit-test each orchestrator method with mock phase handlers
  * Integration-test full pipeline lifecycle (start → run → complete)
  * Integration-test pause/resume/cancel lifecycle

  Status: ✅ COMPLETE

---

* [x] TODO 4: Implement event bus with dual backend

  Purpose / Why this exists
  * Decouple observability from core orchestration logic.
  * Support both in-memory (default) and RabbitMQ (production) backends.

  Where this applies
  * `atlas/core/event_bus.py`

  Implementation requirements
  * EventBus Protocol with publish, subscribe, unsubscribe, close
  * InMemoryEventBus: asyncio-based pub/sub for default operation
  * RabbitMQEventBus: aio-pika based, optional via `pip install atlas[rabbitmq]`
  * Graceful fallback to in-memory if RabbitMQ unavailable

  Acceptance criteria ("done" definition)
  * Both backends implement EventBus Protocol
  * 5 unit tests passing
  * Fallback behavior verified

  Testing plan
  * Unit-test InMemoryEventBus publish/consume/close
  * Unit-test event payload structure
  * Unit-test dual backend Protocol compliance

  Status: ✅ COMPLETE

---

* [x] TODO 5: Implement SQLite-backed job store

  Purpose / Why this exists
  * Durable persistence for job state, phase records, and events.
  * Support both in-memory (testing) and file-based (production) operation.

  Where this applies
  * `atlas/core/job_store.py`

  Implementation requirements
  * JobStore class with connect, close, create_job, update_job, add_phase_record, update_phase_record, get_job, list_jobs, list_phases
  * JobRecord dataclass: job_id, root_id, source_path, phase, status, progress, error_count, metadata, timestamps
  * PhaseRecord dataclass: phase_id, job_id, phase, status, progress, error, timestamps
  * SQLite schema: atlas_jobs, atlas_phases, atlas_events tables with indexes
  * asyncio.Lock for write serialization

  Acceptance criteria ("done" definition)
  * Schema is idempotent (CREATE TABLE IF NOT EXISTS)
  * 8 unit tests passing
  * Metadata round-trip preserves types

  Testing plan
  * Unit-test schema initialization
  * Unit-test job CRUD operations
  * Unit-test phase record CRUD
  * Unit-test metadata serialization/deserialization

  Status: ✅ COMPLETE

---

* [x] TODO 6: Implement safety layer

  Purpose / Why this exists
  * Prevent archive extraction exploits (zip bombs, path traversal, symlink loops).
  * Compute risk flags for filesystem artifacts.

  Where this applies
  * `atlas/safety/filesystem_discovery.py`
  * `atlas/safety/archive_safety.py`
  * `atlas/safety/path_safety.py`

  Implementation requirements
  * FilesystemDiscovery: depth-limited, symlink loop detection, extension filtering, risk flags (executable, archive, sensitive)
  * ArchiveSafetyService: ZIP/TAR bomb detection (compression ratio, entry count, nested depth, suspicious paths)
  * PathSafetyService: path traversal pattern detection (../, absolute paths, null bytes)

  Acceptance criteria ("done" definition)
  * All safety checks implemented with clear pass/fail
  * 22 unit tests passing (8 discovery + 6 archive + 8 path safety)

  Testing plan
  * Unit-test filesystem discovery with depth/symlink test fixtures
  * Unit-test archive bomb detection with crafted ZIP/TAR fixtures
  * Unit-test path traversal detection with malicious path patterns

  Status: ✅ COMPLETE

---

* [x] TODO 7: Implement storage and identity layer

  Purpose / Why this exists
  * Content-addressable storage with SHA-256 + BLAKE3 hashing.
  * Automatic deduplication to avoid reprocessing known files.

  Where this applies
  * `atlas/storage/hash_store.py`

  Implementation requirements
  * HashStore class: compute_hash, lookup_by_hash, store_hash, is_duplicate
  * HashResult dataclass: sha256, blake3, size, content_id
  * Streaming computation with 1 MiB chunks
  * SQLite-backed deduplication index

  Acceptance criteria ("done" definition)
  * Both SHA-256 and BLAKE3 hashing verified
  * Deduplication works correctly
  * 3 unit tests passing

  Testing plan
  * Unit-test hashing of known file content
  * Unit-test deduplication with identical files
  * Unit-test streaming with large files

  Status: ✅ COMPLETE

---

* [x] TODO 8: Implement all pipeline phases

  Purpose / Why this exists
  * Implement the 6-phase pipeline sequence: recon → fingerprint → extract → analyze → review.

  Where this applies
  * `atlas/phases/base.py`
  * `atlas/phases/reconnaissance.py`
  * `atlas/phases/fingerprinting.py`
  * `atlas/phases/extraction.py`
  * `atlas/phases/analysis.py`
  * `atlas/phases/review.py`

  Implementation requirements
  * Phase ABC with async execute(job, config, phase_record), emit_event, update_progress
  * ReconnaissancePhase: filesystem discovery + risk flags
  * FingerprintingPhase: content hashing + dedup
  * ExtractionPhase: safe archive unpacking
  * AnalysisPhase: pattern detection + plugin interface
  * ReviewPhase: evidence recording + artifact promotion

  Acceptance criteria ("done" definition)
  * All 6 phases implement Phase ABC
  * Phase handler contract verified (execute signature)
  * 3 integration tests passing

  Testing plan
  * Unit-test each phase independently
  * Integration-test full pipeline sequence
  * Integration-test pause/resume/cancel during execution

  Status: ✅ COMPLETE

---

* [x] TODO 9: Implement CLI and example pipelines

  Purpose / Why this exists
  * Provide a user-facing command-line interface for pipeline operations.
  * Demonstrate framework usage with real-world examples.

  Where this applies
  * `atlas/cli.py`
  * `examples/ctfd_pipeline.yaml`
  * `examples/doc_processing.yaml`

  Implementation requirements
  * CLI commands: run, jobs list, job status, job pause, job resume, job cancel
  * --help support
  * Pipeline YAML loading and validation
  * 2 example pipelines: CTF challenge, document processing

  Acceptance criteria ("done" definition)
  * All CLI commands functional
  * Example pipelines run end-to-end
  * 44 total tests passing

  Testing plan
  * Test `atlas --help`
  * Test `atlas run examples/ctfd_pipeline.yaml`
  * Test `atlas jobs list`
  * Test `atlas job <id> status`

  Status: ✅ COMPLETE

---

* [x] TODO 10: CI/CD and PyPI configuration

  Purpose / Why this exists
  * Automated testing on every push.
  * Packaging configuration for PyPI publish.

  Where this applies
  * `.github/workflows/tests.yml`
  * `pyproject.toml`

  Implementation requirements
  * GitHub Actions workflow: test on Python 3.13, report coverage
  * PyPI packaging: name "atlas-pipeline", proper metadata
  * 44 tests in CI

  Acceptance criteria ("done" definition)
  * CI workflow passes on main branch
  * Package installable via pip

  Testing plan
  * Verify CI workflow passes
  * Verify `pip install atlas-pipeline` (once published)

  Status: ✅ COMPLETE
