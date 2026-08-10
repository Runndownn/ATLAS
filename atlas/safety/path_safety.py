"""Path safety — traversal prevention and risk computation."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# Maximum path length (prevent buffer overflow / DoS)
MAX_PATH_LENGTH = 4096
# Maximum number of path components
MAX_PATH_COMPONENTS = 255

# Path patterns that are inherently risky
RISKY_PATTERNS = [
    "..",          # Path traversal
    "/etc/",       # System config
    "/root/",      # Root home
    "/proc/",      # Proc filesystem
    "/sys/",       # Sys filesystem
    "/dev/",       # Device files
    ".ssh/",       # SSH keys
    ".gnupg/",     # GPG keys
    "\\windows\\", # Windows paths
    "\\Users\\",   # Windows user dirs
]


@dataclass
class PathSafetyReport:
    """Safety assessment for a filesystem path."""

    safe: bool
    resolved_path: str
    is_within_root: bool
    max_depth_exceeded: bool
    path_too_long: bool
    risky_patterns: list[str]
    depth: int
    error: str | None = None


class PathSafetyService:
    """Validates filesystem paths for safety before processing."""

    def __init__(
        self,
        root_path: str | Path,
        max_depth: int = 32,
        max_path_length: int = MAX_PATH_LENGTH,
    ):
        self._root = Path(root_path).resolve()
        self._max_depth = max_depth
        self._max_path_length = max_path_length

    def assess_path(self, path: str | Path) -> PathSafetyReport:
        """Assess a path for safety violations."""
        path_obj = Path(path)

        # Check raw path length
        raw_path = str(path_obj)
        path_too_long = len(raw_path) > self._max_path_length

        # Resolve and check containment
        try:
            resolved = path_obj.resolve()
        except (OSError, RuntimeError, ValueError) as exc:
            return PathSafetyReport(
                safe=False,
                resolved_path="",
                is_within_root=False,
                max_depth_exceeded=False,
                path_too_long=path_too_long,
                risky_patterns=[],
                depth=0,
                error=str(exc),
            )

        # Check containment within root
        try:
            resolved.relative_to(self._root)
            is_within = True
        except ValueError:
            is_within = False

        # Check depth
        try:
            relative_depth = len(resolved.relative_to(self._root).parts)
        except ValueError:
            relative_depth = len(resolved.parts)
        depth_exceeded = relative_depth > self._max_depth

        # Check risky patterns on resolved path (avoids false positives on
        # intermediate directory names like /tmp/.../root/)
        risky_found = self._check_risky_patterns(str(resolved), raw_path)

        safe = (
            is_within
            and not path_too_long
            and not depth_exceeded
            and not risky_found
        )

        return PathSafetyReport(
            safe=safe,
            resolved_path=str(resolved),
            is_within_root=is_within,
            max_depth_exceeded=depth_exceeded,
            path_too_long=path_too_long,
            risky_patterns=risky_found,
            depth=relative_depth,
        )

    def _check_risky_patterns(self, resolved_path: str, raw_path: str) -> list[str]:
        """Check path for risky patterns using path-component matching.

        Uses prefix matching for absolute patterns (e.g. '/etc/'),
        and component matching for relative patterns (e.g. '.ssh/').
        Substring matching is only used for '..' traversal detection.
        """
        risky: list[str] = []

        for pattern in RISKY_PATTERNS:
            if pattern == "..":
                # Path traversal: check raw path for '..' component
                if ".." in Path(raw_path).parts:
                    risky.append(pattern)
            elif pattern.startswith("/"):
                # Absolute path pattern: check if resolved path starts with it
                if resolved_path == pattern.rstrip("/") or resolved_path.startswith(pattern):
                    risky.append(pattern)
            elif pattern.startswith("\\"):
                # Windows-style pattern: substring check on raw path
                if pattern in raw_path:
                    risky.append(pattern)
            else:
                # Relative pattern (e.g. '.ssh/'): check path components
                root_part = pattern.rstrip("/")
                if root_part in Path(resolved_path).parts:
                    risky.append(pattern)

        return risky
