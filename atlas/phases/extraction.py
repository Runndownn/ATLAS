"""Extraction phase — safe archive extraction.

Maps to Yggdrasil Phase D: Controlled Extraction.
Safely extracts archive contents after safety assessment passes.
"""

from __future__ import annotations

import logging
from pathlib import Path

from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig
from atlas.phases.base import Phase, PhaseHandler
from atlas.safety.archive_safety import ArchiveSafetyService, extract_manifest

logger = logging.getLogger("atlas.phases.extraction")


class ExtractionPhase(Phase):
    """Phase D — Controlled Extraction.

    Extracts archive contents safely. Only extracts after safety
    assessment passes. Prevents archive bombs and path traversal.
    """

    name = "controlled_extraction"
    retryable = True

    def __init__(self, archive_safety: ArchiveSafetyService | None = None):
        super().__init__()
        self._archive_safety = archive_safety or ArchiveSafetyService()

    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        """Execute extraction phase."""
        discovery = job.metadata.get("discovery", {})
        risky_files = discovery.get("risky_files", [])

        # Get archives from discovery metadata
        archive_paths = [
            p for p in risky_files
            if Path(p).suffix.lower() in {".zip", ".tar", ".tar.gz", ".tgz"}
        ]

        if not archive_paths:
            await self.emit_event(job, "no_archives_to_extract")
            self.update_progress(percent=100.0, message="No archives found")
            return

        total = len(archive_paths)
        processed = 0
        extracted_count = 0
        errors: list[str] = []

        await self.emit_event(job, "extraction_started", {"total_archives": total})

        for archive_path in archive_paths:
            report = self._archive_safety.assess_archive(archive_path)

            if not report.safe:
                errors.append(
                    f"Archive unsafe: {archive_path} — {report.error or report.suspicious_patterns}"
                )
                logger.warning("Skipping unsafe archive: %s", archive_path)
                processed += 1
                continue

            # Get manifest and extract safely
            members = extract_manifest(archive_path, safe_only=False)
            try:
                extract_dir = Path(archive_path).parent / f"{Path(archive_path).stem}_extracted"
                extract_dir.mkdir(exist_ok=True)

                extracted = await self._safe_extract(archive_path, extract_dir, members)
                extracted_count += extracted

                await self.emit_event(job, "archive_extracted", {
                    "path": archive_path,
                    "members": len(members),
                    "extracted": extracted,
                })
            except Exception as exc:
                errors.append(f"Extraction failed for {archive_path}: {exc}")
                logger.error("Extraction failed: %s", exc, exc_info=True)

            processed += 1
            self.update_progress(
                percent=(processed / total) * 100 if total > 0 else 100,
                processed=processed,
                total=total,
                message=f"Processed {processed}/{total} archives",
            )

        await self.emit_event(job, "extraction_complete", {
            "total": total,
            "extracted": extracted_count,
            "errors": errors,
        })

        job.metadata["extraction"] = {
            "total_archives": total,
            "extracted_count": extracted_count,
            "errors": errors,
        }

        self.update_progress(percent=100.0, message="Extraction complete")

    async def _safe_extract(
        self,
        archive_path: str,
        dest_dir: Path,
        members,
    ) -> int:
        """Extract archive safely (path traversal prevention)."""
        import tarfile
        import zipfile

        ext = Path(archive_path).suffix.lower()
        extracted = 0

        if ext == ".zip":
            with zipfile.ZipFile(archive_path, "r") as zf:
                for member in zf.namelist():
                    # Prevent path traversal
                    member_path = Path(dest_dir / member)
                    if not member_path.resolve().is_relative_to(dest_dir.resolve()):
                        logger.warning("Skipping path traversal attempt: %s", member)
                        continue
                    zf.extract(member, dest_dir)
                    extracted += 1
        elif ext in {".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz"}:
            with tarfile.open(archive_path, "r:*") as tf:
                for member in tf.getmembers():
                    # Prevent path traversal
                    member_path = Path(dest_dir / member.name)
                    if not member_path.resolve().is_relative_to(dest_dir.resolve()):
                        logger.warning("Skipping path traversal attempt: %s", member.name)
                        continue
                    tf.extract(member, dest_dir)
                    extracted += 1

        return extracted


def create_handler(archive_safety: ArchiveSafetyService | None = None) -> ExtractionPhase:
    """Create a phase handler factory."""
    return ExtractionPhase(archive_safety=archive_safety)
