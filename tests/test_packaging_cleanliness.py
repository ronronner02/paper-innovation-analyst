#!/usr/bin/env python3
"""Tests for packaging script cleanliness and versioned output."""

from __future__ import annotations

import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

# Import version from package_skill.py to avoid hardcoding
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from package_skill import DEFAULT_VERSION


def run_package(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "package_skill.py"), *args],
        capture_output=True,
        text=True,
    )


def find_archive(dist: Path, ext: str) -> Path:
    """Find the versioned archive by pattern, avoiding hardcoded version."""
    pattern = f"paper-innovation-analyst-v*.{ext}"
    matches = sorted(dist.glob(pattern))
    assert matches, f"No {pattern} found in {dist}"
    return matches[-1]


class TestPackagingOutput:
    """Packaging script must produce versioned .skill and .zip archives."""

    def test_default_version_output(self, tmp_path: Path) -> None:
        result = run_package(str(REPO_ROOT), "--dist", str(tmp_path / "dist"))
        assert result.returncode == 0, f"Packaging failed:\n{result.stderr}"
        skill = find_archive(tmp_path / "dist", "skill")
        zipf = find_archive(tmp_path / "dist", "zip")
        assert skill.exists(), ".skill not found"
        assert zipf.exists(), ".zip not found"
        assert skill.stat().st_size > 0
        assert zipf.stat().st_size > 0

    def test_default_version_matches_constant(self, tmp_path: Path) -> None:
        result = run_package(str(REPO_ROOT), "--dist", str(tmp_path / "dist"))
        assert result.returncode == 0
        skill = find_archive(tmp_path / "dist", "skill")
        assert DEFAULT_VERSION in skill.name

    def test_custom_version_output(self, tmp_path: Path) -> None:
        result = run_package(str(REPO_ROOT), "--version", "v1.0.0", "--dist", str(tmp_path / "dist"))
        assert result.returncode == 0
        assert (tmp_path / "dist" / "paper-innovation-analyst-v1.0.0.skill").exists()
        assert (tmp_path / "dist" / "paper-innovation-analyst-v1.0.0.zip").exists()


class TestArchiveCleanliness:
    """Archives must not contain banned artifacts."""

    BANNED = [".git/", ".pytest_cache/", "__pycache__/", ".claude/settings.local.json",
              ".DS_Store", ".env", ".venv/", "outputs/"]

    @pytest.fixture(autouse=True)
    def build_archives(self, tmp_path: Path) -> None:
        self.dist = tmp_path / "dist"
        run_package(str(REPO_ROOT), "--dist", str(self.dist))
        self.skill_path = find_archive(self.dist, "skill")
        self.zip_path = find_archive(self.dist, "zip")

    def _get_names(self, path: Path) -> list[str]:
        with zipfile.ZipFile(path) as zf:
            return zf.namelist()

    def test_skill_no_banned_items(self) -> None:
        names = self._get_names(self.skill_path)
        for ban in self.BANNED:
            assert not any(ban in n for n in names), f".skill contains banned: {ban}"

    def test_zip_no_banned_items(self) -> None:
        names = self._get_names(self.zip_path)
        for ban in self.BANNED:
            assert not any(ban in n for n in names), f".zip contains banned: {ban}"

    def test_no_pyc_in_archives(self) -> None:
        for path in [self.skill_path, self.zip_path]:
            names = self._get_names(path)
            assert not any(n.endswith(".pyc") for n in names), f"{path.name} contains .pyc"

    def test_root_is_paper_innovation_analyst(self) -> None:
        for path in [self.skill_path, self.zip_path]:
            names = self._get_names(path)
            assert any(n.startswith("paper-innovation-analyst/") for n in names), \
                f"{path.name} missing paper-innovation-analyst/ root"

    def test_key_files_present(self) -> None:
        names = self._get_names(self.zip_path)
        for key in ["SKILL.md", "scripts/validate_skill.py", "scripts/extract_paper_assets.py",
                     "scripts/package_skill.py", "references/document-ingestion-pipeline.md"]:
            full = f"paper-innovation-analyst/{key}"
            assert full in names, f"Missing {key} in archive"
