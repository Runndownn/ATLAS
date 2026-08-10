"""Structural Discovery phase — inspect archive structure without extraction.

Maps to Yggdrasil Phase C: Structural Discovery.
Analyzes archive members, nested archives, compression ratios, and
suspicious patterns — but does NOT extract content. That is the job
of Controlled Extraction (Phase D).
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

from atlas.core.event_bus import EventBus
from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig
from atlas.phases.base import Phase, PhaseHandler
from atlas.safety.archive_safety import ArchiveSafetyService, extract_manifest

logger = logging.getLogger("atlas.phases.structural_discovery")


@dataclass
class ArchiveStructuralReport:
    """Structural report for a single archive."""

    path: str
    member_count: int
    suspicious_patterns: list[str]
    nested_archive_count: int
    safe: bool
    error: str | None = None


class StructuralDiscoveryPhase(Phase):
    """Phase C — Structural Discovery.

    Inspects archive structure (member count, compression ratio, nested
    archives, suspicious paths) without extracting content. Produces
    a structural report that feeds into Controlled Extraction (Phase D).
    """

    name = "structural_discovery"
    retryable = True

    _ARCHIVE_SUFFIXES = (".zip", ".tar.gz", ".tgz", ".tar", ".tar.bz2",
                         ".tar.xz", ".tar.lz", ".tar.lzma", ".gz", ".bz2", ".xz")

    def __init__(
        self,
        archive_safety: ArchiveSafetyService | None = None,
        event_bus: EventBus | None = None,
    ):
        super().__init__(event_bus=event_bus)
        self._archive_safety = archive_safety or ArchiveSafetyService()

    def _is_archive(self, path: str) -> bool:
        """Check if a path is an archive, handling compound extensions."""
        return Path(path).name.lower().endswith(self._ARCHIVE_SUFFIXES)

    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        """Execute structural discovery phase."""
        discovery = job.metadata.get("discovery", {})
        risky_files = discovery.get("risky_files", [])

        # Find archives from discovery metadata
        archive_paths = [p for p in risky_files if self._is_archive(p)]
        # Also check discovery files list for archives that may not be "risky"
        for f in discovery.get("risky_files", []):
            pass  # already covered above

        # Re-discover to get all archive paths, not just risky ones
        from atlas.safety.filesystem_discovery import FilesystemDiscovery

        source_path = config.source_path or job.source_path
        if source_path and not archive_paths:
            ds = FilesystemDiscovery()
            result = ds.discover(source_path)
            for file_info in result.files:
                if self._is_archive(file_info.path) and not file_info.is_dir:
                    archive_paths.append(file_info.path)

        if not archive_paths:
            await self.emit_event(job, "no_archives_to_inspect")
            self.update_progress(percent=100.0, message="No archives found")
            return

        total = len(archive_paths)
        processed = 0
        reports: list[dict] = []
        unsafe_count = 0

        await self.emit_event(job, "structural_discovery_started", {"total_archives": total})

        for archive_path in archive_paths:
            report = self._archive_safety.assess_archive(archive_path)
            unsafe_count += 1 if not report.safe else 0

            structural = ArchiveStructuralReport(
                path=archive_path,
                member_count=report.member_count,
                suspicious_patterns=report.suspicious_patterns,
                nested_archive_count=report.nested_archive_count,
                safe=report.safe,
                error=report.error,
            )
            reports.append({
                "path": structural.path,
                "member_count": structural.member_count,
                "suspicious": structural.suspicious_patterns,
                "nested_archives": structural.nested_archive_count,
                "safe": structural.safe,
                "error": structural.error,
            })

            processed += 1
            self.update_progress(
                percent=(processed / total) * 100 if total > 0 else 100,
                processed=processed,
                total=total,
                message=f"Inspected {processed}/{total} archives",
            )

        await self.emit_event(job, "structural_discovery_complete", {
            "total_archives": total,
            "safe_archives": total - unsafe_count,
            "unsafe_archives": unsafe_count,
            "reports": reports,
        })

        job.metadata["structural_discovery"] = {
            "total_archives": total,
            "safe_archives": total - unsafe_count,
            "unsafe_archives": unsafe_count,
            "reports": reports,
        }

        self.update_progress(percent=100.0, message="Structural discovery complete")


def create_handler(
    archive_safety: ArchiveSafetyService | None = None,
) -> StructuralDiscoveryPhase:
    """Create a phase handler factory."""
    return StructuralDiscoveryPhase(archive_safety=archive_safety)
