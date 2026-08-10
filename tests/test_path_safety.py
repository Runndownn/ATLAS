"""Tests for atlas.safety.path_safety."""

import pytest

from atlas.safety.path_safety import PathSafetyService, PathSafetyReport


@pytest.fixture
def temp_root(tmp_path):
    """Create a temporary root directory for safety tests."""
    root = tmp_path / "workdir"
    root.mkdir()
    (root / "safe_file.txt").write_text("safe content")
    subdir = root / "subdir"
    subdir.mkdir()
    (subdir / "nested.txt").write_text("nested content")
    return root


class TestPathSafetyService:
    def test_safe_path_within_root(self, temp_root):
        """A path within the root should be safe."""
        service = PathSafetyService(root_path=temp_root)
        report = service.assess_path(str(temp_root / "safe_file.txt"))
        assert report.safe is True
        assert report.is_within_root is True

    def test_path_traversal_detected(self, temp_root):
        """A path with ../ should be flagged as unsafe."""
        service = PathSafetyService(root_path=temp_root)
        report = service.assess_path(str(temp_root / ".." / ".." / "etc" / "passwd"))
        assert ".." in report.risky_patterns

    def test_absolute_system_path_flagged(self, temp_root):
        """System paths like /etc/ should be flagged."""
        service = PathSafetyService(root_path=temp_root)
        report = service.assess_path("/etc/passwd")
        assert "/etc/" in report.risky_patterns

    def test_path_outside_root_flagged(self, temp_root):
        """A path outside the root should not be within root."""
        service = PathSafetyService(root_path=temp_root)
        # The path resolves outside root
        report = service.assess_path(str(temp_root.parent.parent / "etc"))
        assert report.is_within_root is False

    def test_null_byte_detection(self, temp_root):
        """Paths with null bytes should be handled gracefully (not crash)."""
        service = PathSafetyService(root_path=temp_root)
        # Python's Path.resolve() raises ValueError for null bytes
        report = service.assess_path(str(temp_root / "file\x00.txt"))
        assert report.safe is False
        assert report.error is not None

    def test_deep_path_depth_exceeded(self, temp_root):
        """Paths exceeding max_depth should be flagged."""
        service = PathSafetyService(root_path=temp_root, max_depth=1)
        report = service.assess_path(str(temp_root / "subdir" / "nested.txt"))
        assert report.max_depth_exceeded is True

    def test_symlink_path_in_root(self, temp_root):
        """Symlinks within root should be assessed."""
        symlink_path = temp_root / "safe_link.txt"
        symlink_path.symlink_to(temp_root / "safe_file.txt")
        service = PathSafetyService(root_path=temp_root)
        report = service.assess_path(str(symlink_path))
        assert report.safe is True
        assert report.is_within_root is True

    def test_ssh_key_path_flagged(self, temp_root):
        """Paths containing .ssh/ should be flagged as risky."""
        service = PathSafetyService(root_path=temp_root)
        report = service.assess_path(str(temp_root / ".ssh" / "id_rsa"))
        assert ".ssh/" in report.risky_patterns
