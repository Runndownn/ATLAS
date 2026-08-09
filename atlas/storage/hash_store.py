# Systems: ATLAS / Storage
# Provenance: Authored here, extracted from Yggdrasil hashing
# Tag confidence: High

"""Content-addressable storage with SHA-256 + BLAKE3 hashing.

Extracted from Yggdrasil's hashing_service.py pattern.
Provides streaming hash computation for large files with
content deduplication support.
"""

from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger("atlas.storage.hashing")

# Default chunk size for streaming (1 MiB)
DEFAULT_CHUNK_SIZE = 1024 * 1024

# Supported hash algorithms
SUPPORTED_ALGORITHMS = frozenset({"sha256", "sha384", "sha512", "blake3"})

# Try to import blake3
try:
    import blake3  # type: ignore
    _HAS_BLAKE3 = True
except ImportError:
    _HAS_BLAKE3 = False
    logger.debug("blake3 not available; SHA-256 fallback will be used")


@dataclass
class HashResult:
    """Result of a hashing operation."""

    sha256: str
    blake3: str | None = None
    size_bytes: int = 0
    algorithm: str = "sha256"
    chunk_count: int = 0
    duration_seconds: float = 0.0


class HashStore:
    """Content-addressable storage with multi-algorithm hashing.

    Computes SHA-256 (always) and BLAKE3 (when available) for files
    using streaming I/O to handle large files without loading into memory.

    Provides automatic deduplication: if a content hash already exists
    in the manifest store, no re-hashing is needed on subsequent runs.
    """

    def __init__(
        self,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        prefer_blake3: bool = True,
    ):
        self.chunk_size = chunk_size
        self.prefer_blake3 = prefer_blake3 and _HAS_BLAKE3
        # In a full implementation, this would be a content-addressable
        # blob store. For now, we compute and return hashes.
        self._manifest: dict[str, HashResult] = {}

    def hash_file(self, path: str | Path) -> HashResult:
        """Compute hashes for a file using streaming I/O.

        Returns HashResult with SHA-256 (always) and BLAKE3 (if available).
        """
        import time

        path_obj = Path(path)
        if not path_obj.exists():
            raise FileNotFoundError(f"File not found: {path}")

        if not path_obj.is_file():
            raise ValueError(f"Path is not a file: {path}")

        start = time.monotonic()
        sha256_hasher = hashlib.sha256()
        blake3_hasher = blake3.blake3() if self.prefer_blake3 else None

        size = 0
        chunk_count = 0

        with open(path_obj, "rb") as f:
            while True:
                chunk = f.read(self.chunk_size)
                if not chunk:
                    break
                sha256_hasher.update(chunk)
                if blake3_hasher:
                    blake3_hasher.update(chunk)
                size += len(chunk)
                chunk_count += 1

        duration = time.monotonic() - start
        sha256_hex = sha256_hasher.hexdigest()
        blake3_hex = blake3_hasher.hexdigest() if blake3_hasher else None

        result = HashResult(
            sha256=sha256_hex,
            blake3=blake3_hex,
            size_bytes=size,
            algorithm="blake3" if blake3_hex else "sha256",
            chunk_count=chunk_count,
            duration_seconds=round(duration, 6),
        )

        # Cache in manifest for dedup — store under both raw digest and
        # content_id format so has_content() works regardless of caller
        self._manifest[sha256_hex] = result
        self._manifest[f"sha256:{sha256_hex}"] = result
        if blake3_hex:
            self._manifest[blake3_hex] = result
            self._manifest[f"blake3:{blake3_hex}"] = result

        logger.debug(
            "hashed_file path=%s sha256=%s size=%d chunks=%d duration=%.3fs",
            path_obj,
            sha256_hex,
            size,
            chunk_count,
            duration,
        )

        return result

    def hash_bytes(self, data: bytes, algorithm: str = "sha256") -> str:
        """Compute hash of in-memory bytes."""
        if algorithm == "blake3" and _HAS_BLAKE3:
            return blake3.blake3(data).hexdigest()
        hasher = hashlib.new(algorithm)
        hasher.update(data)
        return hasher.hexdigest()

    def has_content(self, content_hash: str) -> bool:
        """Check if content with this hash was previously hashed.

        This is the content deduplication entry point.
        """
        return content_hash in self._manifest

    def get_content(self, content_hash: str) -> HashResult | None:
        """Retrieve a previously computed hash result by content hash."""
        return self._manifest.get(content_hash)

    @staticmethod
    def get_content_id(sha256: str) -> str:
        """Generate a content identifier from a SHA-256 hash."""
        return f"sha256:{sha256}"
