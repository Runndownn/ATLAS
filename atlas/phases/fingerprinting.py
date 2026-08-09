"""Fingerprinting phase — content hashing and identity establishment.

Maps to Yggdrasil Phase B: Fingerprinting.
Computes SHA-256/BLAKE3 hashes for all discovered files, establishes
content identity, and detects duplicates.
"""

from __future__ import annotations

import logging

from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig
from atlas.phases.base import Phase, PhaseHandler
from atlas.storage.hash_store import HashStore

logger = logging.getLogger("atlas.phases.fingerprinting")


class FingerprintingPhase(Phase):
    """Phase B — Fingerprinting.

    Computes content hashes for all discovered files. This establishes
    content identity for deduplication and content-addressable storage.
    """

    name = "fingerprinting"
    retryable = True

    def __init__(self, hash_store: HashStore | None = None):
        super().__init__()
        self._hash_store = hash_store or HashStore()

    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        """Execute fingerprinting phase."""
        discovery = job.metadata.get("discovery", {})
        risky_files = discovery.get("risky_files", [])

        if not discovery.get("total_files", 0):
            await self.emit_event(job, "no_files_to_fingerprint")
            self.update_progress(percent=100.0, message="No files found")
            return

        # Re-discover to get actual file paths
        from atlas.safety.filesystem_discovery import FilesystemDiscovery

        source_path = config.source_path or job.source_path
        discovery_service = FilesystemDiscovery()
        result = discovery_service.discover(source_path)

        total = len(result.files)
        processed = 0
        duplicates = 0
        hashes: dict[str, str] = {}  # sha256 -> content_id

        await self.emit_event(job, "fingerprinting_started", {"total_files": total})

        for file_info in result.files:
            # Skip directories and symlinks
            if file_info.is_dir or file_info.is_symlink:
                continue

            # Check if already hashed (dedup) using raw sha256 hex from file_info
            try:
                if file_info.sha256 and self._hash_store.has_content(file_info.sha256):
                    duplicates += 1
                    continue

                result_hash = self._hash_store.hash_file(file_info.path)
                content_id = self._hash_store.get_content_id(result_hash.sha256)

                if self._hash_store.has_content(content_id):
                    duplicates += 1
                else:
                    hashes[result_hash.sha256] = content_id
                    file_info.sha256 = result_hash.sha256
                processed += 1

                if processed % 100 == 0:
                    self.update_progress(
                        percent=(processed / total) * 100 if total > 0 else 100,
                        processed=processed,
                        total=total,
                        message=f"Hashed {processed}/{total} files",
                    )
                    await self.emit_event(job, "progress", {
                        "processed": processed,
                        "total": total,
                        "duplicates": duplicates,
                    })
            except (FileNotFoundError, ValueError, PermissionError) as exc:
                logger.warning("Cannot hash %s: %s", file_info.path, exc)

        self.update_progress(
            percent=100.0,
            processed=processed,
            total=total,
            message=f"Fingerprinted {processed} files ({duplicates} duplicates)",
        )

        await self.emit_event(job, "fingerprinting_complete", {
            "total_files": total,
            "duplicates": duplicates,
            "unique_hashes": len(hashes),
        })

        # Store fingerprint results in job metadata
        existing_meta = job.metadata.get("fingerprinting", {})
        existing_meta.update({
            "total_files": total,
            "duplicates": duplicates,
            "content_ids": list(hashes.values()),
        })
        job.metadata["fingerprinting"] = existing_meta


def create_handler(hash_store: HashStore | None = None) -> FingerprintingPhase:
    """Create a phase handler factory."""
    return FingerprintingPhase(hash_store=hash_store)
