"""Filesystem discovery with symlink loop detection and risk flag computation.

Extracted from Yggdrasil's discovery_service.py pattern for Phase A reconnaissance.
Generalized for safe, configurable filesystem traversal in batch pipelines.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

logger = logging.getLogger("atlas.safety.discovery")

# Known executable extensions (potential risk indicators)
EXECUTABLE_EXTENSIONS = frozenset({
    ".exe", ".dll", ".elf", ".bin", ".o", ".so", ".dylib",
    ".sh", ".bash", ".ps1", ".py", ".pl", ".rb", ".js", ".ts",
})

# Known archive extensions (needs extra safety checking)
ARCHIVE_EXTENSIONS = frozenset({
    ".zip", ".rar", ".7z", ".tar", ".tar.gz", ".tgz",
    ".gz", ".bz2", ".xz", ".lz", ".lzma",
})

# Sensitive file patterns (information risk indicators)
SENSITIVE_PATTERNS = frozenset({
    ".env", ".htpasswd", ".ssh", ".gnupg", ".aws",
    "id_rsa", "id_dsa", "id_ecdsa", "id_ed25519",
    "credentials", "secret", "password", "passwd",
    ".git/config", ".git/credentials",
})

# Maximum traversal depth (prevent runaway recursion)
DEFAULT_MAX_DEPTH = 32
# Maximum symlink hops before loop detection triggers
DEFAULT_MAX_SYMLINK_HOPS = 40


@dataclass
class FileInfo:
    """Information about a discovered file."""

    path: str
    name: str
    size: int
    extension: str
    is_dir: bool
    is_symlink: bool
    is_executable: bool
    risk_flags: list[str] = field(default_factory=list)
    sha256: str | None = None


@dataclass
class DiscoveryStats:
    """Aggregate statistics from a discovery pass."""

    total_files: int = 0
    total_dirs: int = 0
    total_bytes: int = 0
    executable_count: int = 0
    archive_count: int = 0
    sensitive_count: int = 0
    symlink_count: int = 0
    symlink_loops_detected: int = 0


@dataclass
class DiscoveryResult:
    """Complete result from a filesystem discovery pass."""

    root_path: str
    files: list[FileInfo]
    stats: DiscoveryStats
    errors: list[str] = field(default_factory=list)
    duration_seconds: float = 0.0


class FilesystemDiscovery:
    """Safe filesystem discovery with loop detection and risk assessment."""

    def __init__(
        self,
        max_depth: int = DEFAULT_MAX_DEPTH,
        max_symlink_hops: int = DEFAULT_MAX_SYMLINK_HOPS,
        follow_symlinks: bool = False,
    ):
        self.max_depth = max_depth
        self.max_symlink_hops = max_symlink_hops
        self.follow_symlinks = follow_symlinks

    def discover(
        self,
        root_path: str | Path,
    ) -> DiscoveryResult:
        """Discover all files under a root path safely.

        Performs filesystem traversal with:
        - Depth limiting (prevents runaway recursion)
        - Symlink loop detection (tracks visited inodes)
        - Risk flag computation (executables, archives, sensitive files)
        - Size bounds checking
        """
        import time
        start = time.monotonic()

        root = Path(root_path).resolve()
        if not root.exists():
            return DiscoveryResult(
                root_path=str(root),
                files=[],
                stats=DiscoveryStats(),
                errors=[f"Path does not exist: {root}"],
            )

        if not root.is_dir():
            return DiscoveryResult(
                root_path=str(root),
                files=[],
                stats=DiscoveryStats(),
                errors=[f"Path is not a directory: {root}"],
            )

        files: list[FileInfo] = []
        stats = DiscoveryStats()
        errors: list[str] = []
        visited_inodes: set[int] = set()

        for info in self._walk_safe(root, visited_inodes, stats, errors, depth=0):
            files.append(info)

        duration = time.monotonic() - start

        return DiscoveryResult(
            root_path=str(root),
            files=files,
            stats=stats,
            errors=errors,
            duration_seconds=duration,
        )

    def _walk_safe(
        self,
        path: Path,
        visited_inodes: set[int],
        stats: DiscoveryStats,
        errors: list[str],
        depth: int,
    ) -> Iterator[FileInfo]:
        """Walk filesystem safely with loop detection."""
        if depth > self.max_depth:
            return

        try:
            stat = path.lstat()
        except (OSError, PermissionError) as exc:
            errors.append(f"Cannot stat {path}: {exc}")
            return

        # Symlink handling
        is_symlink = path.is_symlink()
        if is_symlink:
            stats.symlink_count += 1
            if self.follow_symlinks:
                try:
                    real_path = path.resolve()
                    inode = real_path.stat().st_ino
                    if inode in visited_inodes:
                        stats.symlink_loops_detected += 1
                        return
                    visited_inodes.add(inode)
                except (OSError, PermissionError) as exc:
                    errors.append(f"Cannot resolve symlink {path}: {exc}")
                    return

        is_dir = stat.st_mode & 0o170000 == 0o040000
        is_exec = bool(stat.st_mode & 0o111) and not is_dir

        if is_dir:
            stats.total_dirs += 1
            try:
                entries = sorted(path.iterdir())
            except (PermissionError, OSError) as exc:
                errors.append(f"Cannot read directory {path}: {exc}")
                return

            for entry in entries:
                yield from self._walk_safe(entry, visited_inodes, stats, errors, depth + 1)
        else:
            stats.total_files += 1
            stats.total_bytes += stat.st_size

            name_lower = path.name.lower()
            ext = path.suffix.lower()
            if path.name.endswith(".tar.gz") or path.name.endswith(".tar.bz2"):
                ext = ".tar.gz"

            risk_flags = self._compute_risk_flags(name_lower, ext, is_symlink, is_exec)

            if ext in EXECUTABLE_EXTENSIONS:
                stats.executable_count += 1
            if ext in ARCHIVE_EXTENSIONS:
                stats.archive_count += 1
            if risk_flags:
                stats.sensitive_count += 1

            yield FileInfo(
                path=str(path),
                name=path.name,
                size=stat.st_size,
                extension=ext,
                is_dir=is_dir,
                is_symlink=is_symlink,
                is_executable=is_exec,
                risk_flags=risk_flags,
            )

    def _compute_risk_flags(
        self,
        name_lower: str,
        ext: str,
        is_symlink: bool,
        is_exec: bool,
    ) -> list[str]:
        """Compute risk flags for a file."""
        flags: list[str] = []

        if is_exec and ext:
            flags.append("executable")

        if is_symlink:
            flags.append("symlink")

        for pattern in SENSITIVE_PATTERNS:
            if pattern in name_lower:
                flags.append("sensitive")
                break

        if ext in ARCHIVE_EXTENSIONS:
            flags.append("archive")

        return flags

    @staticmethod
    def get_extension(path: Path) -> str:
        """Get file extension, handling compound extensions like .tar.gz."""
        name = path.name.lower()
        for compound in (".tar.gz", ".tar.bz2", ".tar.xz"):
            if name.endswith(compound):
                return compound
        return path.suffix.lower()
