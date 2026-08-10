"""Tests for atlas.storage.hash_store."""

import hashlib
from pathlib import Path

import pytest

from atlas.storage.hash_store import HashStore, HashResult


@pytest.fixture
def text_file(tmp_path):
    """Create a test file with known content."""
    p = tmp_path / "test.txt"
    p.write_text("hello world")
    return p


@pytest.fixture
def unique_files(tmp_path):
    """Create multiple unique test files."""
    files = []
    for i in range(3):
        p = tmp_path / f"file_{i}.txt"
        p.write_text(f"content_{i}")
        files.append(p)
    return files


@pytest.fixture
def duplicate_files(tmp_path):
    """Create two files with identical content."""
    p1 = tmp_path / "original.txt"
    p1.write_text("same content")
    p2 = tmp_path / "duplicate.txt"
    p2.write_text("same content")
    return p1, p2


class TestHashStore:
    def test_hash_file_returns_sha256(self, text_file):
        """hash_file always returns a SHA-256 hash."""
        store = HashStore()
        result = store.hash_file(text_file)
        assert result.sha256 is not None
        assert len(result.sha256) == 64  # SHA-256 hex digest length

    def test_hash_file_matches_manual_sha256(self, text_file):
        """Hash result should match a manual hashlib computation."""
        store = HashStore()
        result = store.hash_file(text_file)

        expected = hashlib.sha256(text_file.read_bytes()).hexdigest()
        assert result.sha256 == expected

    def test_hash_file_returns_size(self, text_file):
        """Hash result should include file size."""
        store = HashStore()
        result = store.hash_file(text_file)
        assert result.size_bytes == len("hello world")

    def test_hash_file_stores_in_manifest(self, text_file):
        """hash_file should add entries to the manifest for dedup."""
        store = HashStore()
        result = store.hash_file(text_file)

        # Both raw hex and prefixed format should be in manifest
        assert store.has_content(result.sha256) is True
        assert store.has_content(f"sha256:{result.sha256}") is True

    def test_has_content_new_file(self, tmp_path):
        """has_content should return False for unhashed content."""
        store = HashStore()
        assert store.has_content("nonexistent_hash") is False
        assert store.has_content("sha256:nonexistent_hash") is False

    def test_get_content_id_format(self):
        """get_content_id should return 'sha256:<digest>' format."""
        raw = "abcd1234"
        content_id = HashStore.get_content_id(raw)
        assert content_id == "sha256:abcd1234"

    def test_streaming_chunk_size(self, tmp_path):
        """hash_file should work with files larger than chunk size."""
        # Create a file larger than 1 MiB
        large_path = tmp_path / "large.bin"
        large_path.write_bytes(b"x" * (2 * 1024 * 1024))

        store = HashStore()
        result = store.hash_file(large_path)
        assert result.size_bytes == 2 * 1024 * 1024
        assert result.sha256 is not None

    def test_duplicate_detection(self, duplicate_files):
        """Two identical files should produce the same hash."""
        original, duplicate = duplicate_files
        store = HashStore()

        result1 = store.hash_file(original)
        result2 = store.hash_file(duplicate)

        assert result1.sha256 == result2.sha256
        assert store.has_content(result1.sha256) is True

    def test_get_content_returns_stored_result(self, text_file):
        """get_content should return the previously stored HashResult."""
        store = HashStore()
        result = store.hash_file(text_file)

        retrieved = store.get_content(result.sha256)
        assert retrieved is not None
        assert retrieved.sha256 == result.sha256
        assert retrieved.size_bytes == result.size_bytes

    def test_nonexistent_file_raises(self, tmp_path):
        """hash_file should raise FileNotFoundError for missing files."""
        store = HashStore()
        with pytest.raises(FileNotFoundError):
            store.hash_file(tmp_path / "nonexistent.txt")
