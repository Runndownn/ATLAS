"""Reconnaissance phase — filesystem discovery + safety assessment.

Maps to Yggdrasil Phase A: Reconnaissance.
Discovers files, computes risk flags, and emits discovery events.
"""

from __future__ import annotations

import logging

from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig
from atlas.phases.base import Phase, PhaseHandler
from atlas.safety.archive_safety import ArchiveSafetyService
from atlas.safety.filesystem_discovery import FilesystemDiscovery

logger = logging.getLogger("atlas.phases.reconnaissance")


class ReconnaissancePhase(Phase):
    """Phase A — Reconnaissance.

    Discovers all files under the source path, computes risk flags,
    assesses archives for safety, and records findings.
    """

    name = "reconnaissance"
    retryable = True

    def __init__(
        self,
        discovery: FilesystemDiscovery | None = None,
        archive_safety: ArchiveSafetyService | None = None,
    ):
        super().__init__()
        self._discovery = discovery or FilesystemDiscovery()
        self._archive_safety = archive_safety or ArchiveSafetyService()

    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        """Execute reconnaissance phase."""
        source_path = config.source_path or job.source_path
        if not source_path:
            raise ValueError("No source_path configured for pipeline")

        await self.emit_event(job, "discovering", {"path": source_path})

        result = self._discovery.discover(source_path)

        self.update_progress(
            percent=50.0 if result.errors else 100.0,
            processed=result.stats.total_files,
            total=result.stats.total_files,
            message=f"Discovered {result.stats.total_files} files",
        )

        # Assess archives found during discovery
        archive_count = 0
        archive_reports: list[dict] = []
        for file_info in result.files:
            if file_info.extension in {".zip", ".tar", ".tar.gz", ".tgz"}:
                archive_count += 1
                report = self._archive_safety.assess_archive(file_info.path)
                archive_reports.append({
                    "path": file_info.path,
                    "safe": report.safe,
                    "members": report.member_count,
                    "suspicious": report.suspicious_patterns,
                })

        await self.emit_event(job, "discovery_complete", {
            "total_files": result.stats.total_files,
            "total_bytes": result.stats.total_bytes,
            "archives": archive_count,
            "errors": result.errors[:10],  # Truncate for event
        })

        # Store discovery result in job metadata
        job.metadata["discovery"] = {
            "total_files": result.stats.total_files,
            "total_bytes": result.stats.total_bytes,
            "archive_count": archive_count,
            "risky_files": [f.path for f in result.files if f.risk_flags],
            "errors": result.errors,
        }

        self.update_progress(percent=100.0, message="Recon complete")


def create_handler(
    discovery: FilesystemDiscovery | None = None,
    archive_safety: ArchiveSafetyService | None = None,
) -> ReconnaissancePhase:
    """Create a phase handler factory (for orchestrator registration)."""
    return ReconnaissancePhase(discovery=discovery, archive_safety=archive_safety)
