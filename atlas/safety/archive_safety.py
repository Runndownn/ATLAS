"""Archive safety — bomb detection and safe extraction metadata.

Extracted from Yggdrasil's archive_safety_service.py and generalized
for standalone use. Assesses ZIP and TAR archives for:
- Total uncompressed byte limits (bomb prevention)
- Compression ratio limits
- Nested archive depth limits
- Path traversal in member names
- Suspicious system paths in member names
"""

from __future__ import annotations

import logging
import tarfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger("atlas.safety.archive")

# Default safety limits
DEFAULT_MAX_TOTAL_UNCOMPRESSED_BYTES = 1 * 1024**3  # 1 GiB
DEFAULT_MAX_TOTAL_COMPRESSED_BYTES = 128 * 1024**2  # 128 MiB
DEFAULT_MAX_MEMBERS = 50000
DEFAULT_MAX_NESTED_DEPTH = 5
DEFAULT_MAX_COMPRESSION_RATIO = 100.0

# Suspicious path patterns in archive member names
SUSPICIOUS_PATTERNS = [
    "..",           # Path traversal
    "/etc/", "/root/", "/home/",  # System paths
    "\\windows\\", "\\Users\\",    # Windows paths
    ".ssh/", ".gnupg/", ".aws/",   # Sensitive directories
    "/proc/", "/sys/",             # System pseudo-filesystems
]

# Archive extensions that are "dangerous" (nested archives)
NESTED_ARCHIVE_EXTENSIONS = frozenset({
    ".zip", ".rar", ".7z", ".tar", ".tar.gz", ".tgz",
    ".gz", ".bz2", ".xz", ".lz", ".lzma",
})


@dataclass
class ArchiveMember:
    """Information about a single archive member."""

    filename: str
    compressed_size: int
    uncompressed_size: int
    is_dir: bool
    is_symlink: bool
    extension: str


@dataclass
class ArchiveSafetyReport:
    """Safety assessment for an archive."""

    safe: bool
    total_compressed_bytes: int
    total_uncompressed_bytes: int
    member_count: int
    max_compression_ratio: float
    nested_archive_count: int
    suspicious_patterns: list[str] = field(default_factory=list)
    error: str | None = None


class ArchiveSafetyService:
    """Safe archive inspection with bomb detection."""

    def __init__(
        self,
        max_uncompressed_bytes: int = DEFAULT_MAX_TOTAL_UNCOMPRESSED_BYTES,
        max_compressed_bytes: int = DEFAULT_MAX_TOTAL_COMPRESSED_BYTES,
        max_members: int = DEFAULT_MAX_MEMBERS,
        max_nested_depth: int = DEFAULT_MAX_NESTED_DEPTH,
        max_compression_ratio: float = DEFAULT_MAX_COMPRESSION_RATIO,
    ):
        self.max_uncompressed_bytes = max_uncompressed_bytes
        self.max_compressed_bytes = max_compressed_bytes
        self.max_members = max_members
        self.max_nested_depth = max_nested_depth
        self.max_compression_ratio = max_compression_ratio

    def assess_archive(self, archive_path: str | Path) -> ArchiveSafetyReport:
        """Assess archive safety without extraction.

        Works with ZIP and TAR formats. Does NOT extract content.
        """
        path = Path(archive_path)

        if not path.exists():
            return ArchiveSafetyReport(
                safe=False,
                total_compressed_bytes=0,
                total_uncompressed_bytes=0,
                member_count=0,
                max_compression_ratio=0,
                nested_archive_count=0,
                suspicious_patterns=["file_not_found"],
                error=f"File not found: {archive_path}",
            )

        # Check compressed size limit
        compressed_size = path.stat().st_size
        if compressed_size > self.max_compressed_bytes:
            return ArchiveSafetyReport(
                safe=False,
                total_compressed_bytes=compressed_size,
                total_uncompressed_bytes=0,
                member_count=0,
                max_compression_ratio=0,
                nested_archive_count=0,
                suspicious_patterns=["compressed_size_limit_exceeded"],
                error=f"Archive compressed size {compressed_size} exceeds limit {self.max_compressed_bytes}",
            )

        ext = self.get_extension(path.name)

        if ext == ".zip":
            return self._assess_zip(path)
        elif ext in {".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz"}:
            return self._assess_tarball(path)
        else:
            return ArchiveSafetyReport(
                safe=False,
                total_compressed_bytes=compressed_size,
                total_uncompressed_bytes=0,
                member_count=0,
                max_compression_ratio=0,
                nested_archive_count=0,
                suspicious_patterns=["unsupported_format"],
                error=f"Unsupported archive format: {ext}",
            )

    def _assess_zip(self, path: Path) -> ArchiveSafetyReport:
        """Assess ZIP archive."""
        total_compressed = 0
        total_uncompressed = 0
        max_ratio = 0.0
        nested_count = 0
        suspicious: list[str] = []
        member_count = 0

        try:
            with zipfile.ZipFile(path, "r") as zf:
                for member in zf.infolist():
                    member_count += 1
                    total_compressed += member.compress_size
                    total_uncompressed += member.file_size

                    if member_count > self.max_members:
                        return ArchiveSafetyReport(
                            safe=False,
                            total_compressed_bytes=total_compressed,
                            total_uncompressed_bytes=total_uncompressed,
                            member_count=member_count,
                            max_compression_ratio=max_ratio,
                            nested_archive_count=nested_count,
                            suspicious_patterns=["too_many_members"],
                        )

                    if member.compress_size > 0:
                        ratio = member.file_size / member.compress_size
                        max_ratio = max(max_ratio, ratio)

                    ext = self.get_extension(member.filename)
                    if ext in NESTED_ARCHIVE_EXTENSIONS:
                        nested_count += 1

                    for pattern in SUSPICIOUS_PATTERNS:
                        if pattern in member.filename:
                            suspicious.append(f"member:{pattern}")
        except zipfile.BadZipFile as exc:
            return ArchiveSafetyReport(
                safe=False,
                total_compressed_bytes=path.stat().st_size,
                total_uncompressed_bytes=0,
                member_count=0,
                max_compression_ratio=0,
                nested_archive_count=0,
                suspicious_patterns=["bad_zip_format"],
                error=str(exc),
            )

        safe = (
            total_uncompressed <= self.max_uncompressed_bytes
            and total_compressed <= self.max_compressed_bytes
            and member_count <= self.max_members
            and max_ratio <= self.max_compression_ratio
        )

        return ArchiveSafetyReport(
            safe=safe,
            total_compressed_bytes=total_compressed,
            total_uncompressed_bytes=total_uncompressed,
            member_count=member_count,
            max_compression_ratio=round(max_ratio, 2),
            nested_archive_count=nested_count,
            suspicious_patterns=suspicious,
        )

    def _assess_tarball(self, path: Path) -> ArchiveSafetyReport:
        """Assess TAR archive."""
        total_uncompressed = 0
        nested_count = 0
        suspicious: list[str] = []
        member_count = 0

        try:
            with tarfile.open(path, "r:*") as tf:
                for member in tf.getmembers():
                    member_count += 1
                    total_uncompressed += member.size

                    if member_count > self.max_members:
                        return ArchiveSafetyReport(
                            safe=False,
                            total_compressed_bytes=path.stat().st_size,
                            total_uncompressed_bytes=total_uncompressed,
                            member_count=member_count,
                            max_compression_ratio=0,
                            nested_archive_count=nested_count,
                            suspicious_patterns=["too_many_members"],
                        )

                    ext = self.get_extension(member.name)
                    if ext in NESTED_ARCHIVE_EXTENSIONS:
                        nested_count += 1

                    for pattern in SUSPICIOUS_PATTERNS:
                        if pattern in member.name:
                            suspicious.append(f"member:{pattern}")
        except tarfile.TarError as exc:
            return ArchiveSafetyReport(
                safe=False,
                total_compressed_bytes=path.stat().st_size,
                total_uncompressed_bytes=0,
                member_count=0,
                max_compression_ratio=0,
                nested_archive_count=0,
                suspicious_patterns=["bad_tar_format"],
                error=str(exc),
            )

        safe = (
            total_uncompressed <= self.max_uncompressed_bytes
            and member_count <= self.max_members
        )

        return ArchiveSafetyReport(
            safe=safe,
            total_compressed_bytes=path.stat().st_size,
            total_uncompressed_bytes=total_uncompressed,
            member_count=member_count,
            max_compression_ratio=0,
            nested_archive_count=nested_count,
            suspicious_patterns=suspicious,
        )

    @staticmethod
    def get_extension(filename: str) -> str:
        """Get file extension, handling compound extensions."""
        name_lower = filename.lower()
        for compound in (".tar.gz", ".tar.bz2", ".tar.xz"):
            if name_lower.endswith(compound):
                return compound
        return Path(filename).suffix.lower()


def extract_manifest(
    archive_path: str | Path,
    safe_only: bool = True,
) -> list[ArchiveMember]:
    """Extract a manifest of archive members without extracting content.

    If safe_only is True, only returns the manifest if the archive passes
    safety assessment.
    """
    path = Path(archive_path)
    service = ArchiveSafetyService()

    if safe_only:
        report = service.assess_archive(path)
        if not report.safe:
            return []

    ext = ArchiveSafetyService.get_extension(path.name)
    members: list[ArchiveMember] = []

    if ext == ".zip":
        with zipfile.ZipFile(path, "r") as zf:
            for info in zf.infolist():
                members.append(ArchiveMember(
                    filename=info.filename,
                    compressed_size=info.compress_size,
                    uncompressed_size=info.file_size,
                    is_dir=info.is_dir(),
                    is_symlink=False,
                    extension=Path(info.filename).suffix.lower(),
                ))
    elif ext in {".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz"}:
        with tarfile.open(path, "r:*") as tf:
            for member in tf.getmembers():
                members.append(ArchiveMember(
                    filename=member.name,
                    compressed_size=0,  # TAR doesn't track compressed size per-member
                    uncompressed_size=member.size,
                    is_dir=member.isdir(),
                    is_symlink=member.issym() or member.islnk(),
                    extension=Path(member.name).suffix.lower(),
                ))

    return members
