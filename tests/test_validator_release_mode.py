#!/usr/bin/env python3
"""Tests for validate_skill.py --release mode."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_validator(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "validate_skill.py"), *args],
        capture_output=True,
        text=True,
    )


def copy_repo_to(tmp_path: Path) -> Path:
    """Copy the repo to a tmp directory for isolated testing."""
    import shutil
    dst = tmp_path / "paper-innovation-analyst"
    shutil.copytree(
        REPO_ROOT,
        dst,
        ignore=shutil.ignore_patterns(".git", ".pytest_cache", "__pycache__", "dist", "outputs"),
    )
    return dst


class TestDevMode:
    """Development mode should be permissive about .git/ but strict about sensitive files."""

    def test_dev_mode_passes_on_clean_repo(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        result = run_validator(str(repo))
        assert result.returncode == 0

    def test_dev_mode_fails_on_settings_local(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        (repo / ".claude").mkdir(parents=True, exist_ok=True)
        (repo / ".claude" / "settings.local.json").write_text("{}", encoding="utf-8")
        result = run_validator(str(repo))
        assert result.returncode != 0
        assert "settings.local.json" in result.stderr


class TestReleaseMode:
    """Release mode must reject all banned artifacts."""

    def test_release_mode_passes_on_clean_repo(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        result = run_validator(str(repo), "--release")
        assert result.returncode == 0, f"Release check failed:\n{result.stderr}"

    def test_release_fails_on_git_dir(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        (repo / ".git").mkdir(parents=True, exist_ok=True)
        (repo / ".git" / "HEAD").write_text("ref: refs/heads/main", encoding="utf-8")
        result = run_validator(str(repo), "--release")
        assert result.returncode != 0

    def test_release_fails_on_pytest_cache(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        (repo / ".pytest_cache").mkdir(parents=True, exist_ok=True)
        result = run_validator(str(repo), "--release")
        assert result.returncode != 0

    def test_release_fails_on_pycache(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        (repo / "scripts" / "__pycache__").mkdir(parents=True, exist_ok=True)
        (repo / "scripts" / "__pycache__" / "test.pyc").write_text("", encoding="utf-8")
        result = run_validator(str(repo), "--release")
        assert result.returncode != 0

    def test_release_fails_on_pyc(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        (repo / "scripts" / "validate.cpython-311.pyc").write_text("", encoding="utf-8")
        result = run_validator(str(repo), "--release")
        assert result.returncode != 0

    def test_release_fails_on_nested_zip(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        (repo / "old-archive.zip").write_bytes(b"PK\x03\x04fake")
        result = run_validator(str(repo), "--release")
        assert result.returncode != 0

    def test_release_fails_on_nested_skill(self, tmp_path: Path) -> None:
        repo = copy_repo_to(tmp_path)
        (repo / "old-archive.skill").write_bytes(b"PK\x03\x04fake")
        result = run_validator(str(repo), "--release")
        assert result.returncode != 0

    def test_release_passes_on_packaged_output(self, tmp_path: Path) -> None:
        """Package, unpack, then --release should pass."""
        import zipfile
        subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "package_skill.py"), str(REPO_ROOT),
             "--dist", str(tmp_path / "dist")],
            capture_output=True, text=True,
        )
        zips = list((tmp_path / "dist").glob("*.zip"))
        assert zips, "No .zip produced"
        unpack_dir = tmp_path / "unpacked"
        with zipfile.ZipFile(zips[0]) as zf:
            zf.extractall(unpack_dir)
        inner = unpack_dir / "paper-innovation-analyst"
        assert inner.exists(), "Archive missing paper-innovation-analyst/ root"
        result = run_validator(str(inner), "--release")
        assert result.returncode == 0, f"Release check on unpacked archive failed:\n{result.stderr}"
