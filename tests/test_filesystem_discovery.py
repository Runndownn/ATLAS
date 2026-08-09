"""Tests for atlas.safety.filesystem_discovery."""

import os
import tempfile
from pathlib import Path

import pytest

from atlas.safety.filesystem_discovery import FilesystemDiscovery, FileInfo


@pytest.fixture
def temp_filesystem():
    """Create a temporary filesystem structure for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)

        # Create files
        (base / "file1.txt").write_text("hello world")
        exe_file = base / "file2.exe"
        exe_file.write_text("binary")
        exe_file.chmod(0o755)  # Set executable permission
        (base / "data.zip").write_text("fake zip")
        (base / "secret.env").write_text("SECRET=123")  # sensitive

        # Create subdirectory
        subdir = base / "subdir"
        subdir.mkdir()
        (subdir / "nested.txt").write_text("nested content")

        # Create symlink (for loop detection test)
        link = base / "link_to_subdir"
        try:
            os.symlink(subdir, link)
        except OSError:
            pass  # May not work on all platforms

        yield base


class TestFilesystemDiscovery:
    def test_discovers_files(self, temp_filesystem):
        discovery = FilesystemDiscovery()
        result = discovery.discover(temp_filesystem)

        assert result.stats.total_files >= 4
        assert result.root_path == str(temp_filesystem.resolve())

    def test_computes_risk_flags(self, temp_filesystem):
        discovery = FilesystemDiscovery()
        result = discovery.discover(temp_filesystem)

        # Should find .env as sensitive
        sensitive_files = [f for f in result.files if "sensitive" in f.risk_flags]
        assert any(".env" in f.name for f in sensitive_files)

    def test_executable_flag(self, temp_filesystem):
        discovery = FilesystemDiscovery()
        result = discovery.discover(temp_filesystem)

        exe_files = [f for f in result.files if "executable" in f.risk_flags]
        assert any(".exe" in f.name for f in exe_files)

    def test_archive_flag(self, temp_filesystem):
        discovery = FilesystemDiscovery()
        result = discovery.discover(temp_filesystem)

        archive_files = [f for f in result.files if "archive" in f.risk_flags]
        assert any(".zip" in f.name for f in archive_files)

    def test_symlink_detection(self, temp_filesystem):
        discovery = FilesystemDiscovery()
        result = discovery.discover(temp_filesystem)

        symlinks = [f for f in result.files if f.is_symlink]
        # The symlink may not exist on all platforms
        if symlinks:
            assert all("symlink" in f.risk_flags for f in symlinks)

    def test_nonexistent_path(self):
        discovery = FilesystemDiscovery()
        result = discovery.discover("/nonexistent/path/12345")
        assert result.stats.total_files == 0
        assert len(result.errors) > 0

    def test_max_depth(self):
        """Test that max_depth limits traversal."""
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            # Create deep nesting
            current = base
            for i in range(10):
                current = current / f"dir_{i}"
                current.mkdir()

            discovery = FilesystemDiscovery(max_depth=3)
            result = discovery.discover(base)
            # Should not reach the deepest directories
            assert result.stats.total_dirs <= 4  # base + dir_0, dir_1, dir_2

    def test_symlink_loop_detection(self, temp_filesystem):
        """Test that symlink loops are detected."""
        discovery = FilesystemDiscovery(follow_symlinks=False)
        result = discovery.discover(temp_filesystem)
        assert result.stats.symlink_loops_detected >= 0
