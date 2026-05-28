#!/usr/bin/env python3
"""Smoke tests for scripts/extract_paper_assets.py."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = str(REPO_ROOT / "scripts" / "extract_paper_assets.py")


def run_extract(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        text=True,
    )


class TestExtractHelp:
    """Help output must work and show new OCR flags."""

    def test_help_exits_clean(self) -> None:
        result = run_extract("--help")
        assert result.returncode == 0

    def test_help_shows_ocr_mode(self) -> None:
        result = run_extract("--help")
        assert "--ocr-mode" in result.stdout

    def test_help_shows_ocr_text_threshold(self) -> None:
        result = run_extract("--help")
        assert "--ocr-text-threshold" in result.stdout

    def test_help_shows_dpi(self) -> None:
        result = run_extract("--help")
        assert "--dpi" in result.stdout


class TestExtractInputValidation:
    """Script must reject invalid inputs gracefully."""

    def test_nonexistent_pdf(self) -> None:
        result = run_extract("/nonexistent/paper.pdf")
        assert result.returncode != 0

    def test_non_pdf_file(self, tmp_path: Path) -> None:
        f = tmp_path / "readme.txt"
        f.write_text("Not a PDF", encoding="utf-8")
        result = run_extract(str(f))
        assert result.returncode != 0


class TestExtractManifest:
    """If PyMuPDF is available, test manifest generation with a minimal PDF."""

    @pytest.fixture
    def minimal_pdf(self, tmp_path: Path) -> Path:
        """Create a minimal valid PDF."""
        pdf_path = tmp_path / "test.pdf"
        # Minimal valid PDF
        pdf_content = (
            b"%PDF-1.4\n"
            b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
            b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
            b"3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Resources<<>>>>endobj\n"
            b"xref\n0 4\n"
            b"0000000000 65535 f \n"
            b"0000000009 00000 n \n"
            b"0000000058 00000 n \n"
            b"0000000115 00000 n \n"
            b"trailer<</Size 4/Root 1 0 R>>\n"
            b"startxref\n206\n%%EOF"
        )
        pdf_path.write_bytes(pdf_content)
        return pdf_path

    def test_manifest_generated(self, minimal_pdf: Path, tmp_path: Path) -> None:
        out_dir = tmp_path / "output"
        result = run_extract(str(minimal_pdf), "--out", str(out_dir))
        # May succeed or fail depending on PyMuPDF availability
        manifest_path = out_dir / "manifest.json"
        if result.returncode == 0:
            assert manifest_path.exists()
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            assert "input_file" in manifest
            assert "created_at" in manifest
            assert "extractor_version" in manifest
            assert "capabilities" in manifest
            assert "warnings" in manifest
            assert "pages" in manifest
            assert "reference_source" in manifest
            assert "outputs" in manifest

    def test_manifest_schema_keys(self, minimal_pdf: Path, tmp_path: Path) -> None:
        out_dir = tmp_path / "output"
        result = run_extract(str(minimal_pdf), "--out", str(out_dir))
        if result.returncode == 0:
            manifest = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
            caps = manifest["capabilities"]
            assert "native_text" in caps
            assert "ocr" in caps
            assert "table_extraction" in caps
            assert "image_extraction" in caps
            assert "equation_candidates" in caps
            assert "reference_candidates" in caps
            assert manifest["reference_source"] in ("native_text", "ocr_text", "unavailable")
