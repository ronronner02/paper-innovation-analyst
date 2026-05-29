"""Tests for Codex report depth profile requirements.

v0.5.5-beta: Codex reports must not be overly shallow.
"""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Codex report depth requirement
# ---------------------------------------------------------------------------

class TestCodexReportDepthRequirement:
    """Codex prompts must enforce minimum report depth."""

    def test_paper_analysis_has_depth_requirement(self):
        text = read("codex/prompts/paper-analysis.md")
        assert "Codex Report Depth Requirement" in text

    def test_paper_analysis_lists_15_sections(self):
        text = read("codex/prompts/paper-analysis.md")
        required_sections = [
            "Bibliographic Verification",
            "Evidence Coverage",
            "Method Decomposition",
            "Dataset and Evaluation",
            "Key Quantitative Results",
            "Hardware / Deployment Evidence",
            "Contribution and Novelty Assessment",
            "Limitations",
            "Quality Audit",
        ]
        for section in required_sections:
            assert section in text, f"codex/prompts/paper-analysis.md missing section: {section}"

    def test_codex_agents_has_depth_requirement(self):
        text = read("codex/AGENTS.md")
        assert "Codex Report Depth Requirement" in text

    def test_codex_agents_lists_minimum_sections(self):
        text = read("codex/AGENTS.md")
        required_sections = [
            "Bibliographic Verification",
            "Evidence Coverage",
            "Method Decomposition",
            "Claim Safety Check",
            "Quality Audit",
        ]
        for section in required_sections:
            assert section in text, f"codex/AGENTS.md missing section: {section}"


# ---------------------------------------------------------------------------
# Innovation point depth
# ---------------------------------------------------------------------------

class TestInnovationPointDepth:
    """Codex innovation points must not be direction-only lists."""

    def test_innovation_prompt_has_depth_requirement(self):
        text = read("codex/prompts/innovation-mining.md")
        assert "Innovation Point Depth Requirement" in text

    def test_innovation_prompt_lists_required_fields(self):
        text = read("codex/prompts/innovation-mining.md")
        required_fields = [
            "Framework Source Type",
            "Core idea",
            "Source evidence",
            "Modified module",
            "Technical route",
            "Tensor / feature flow compatibility",
            "Loss / objective change",
            "Hypothesized measurable outcome",
            "Required validation",
            "Compute / memory / deployment risk",
            "Minimal viable experiment",
            "Failure criteria",
            "Evidence level",
            "Claim Safety Check",
        ]
        for field in required_fields:
            assert field in text, f"codex/prompts/innovation-mining.md missing field: {field}"

    def test_codex_agents_lists_innovation_fields(self):
        text = read("codex/AGENTS.md")
        required_fields = [
            "Framework Source Type",
            "Technical route",
            "Tensor/feature flow compatibility",
            "Hypothesized measurable outcome",
            "Minimal viable experiment",
            "Failure criteria",
            "Evidence level",
        ]
        for field in required_fields:
            assert field in text, f"codex/AGENTS.md missing innovation field: {field}"


# ---------------------------------------------------------------------------
# Codex platform positioning
# ---------------------------------------------------------------------------

class TestCodexPlatformPositioning:
    """Codex Adapter must be positioned as repository-level adapter."""

    def test_codex_agents_has_platform_positioning(self):
        text = read("codex/AGENTS.md")
        assert "Platform Positioning" in text

    def test_codex_agents_clarifies_not_standalone(self):
        text = read("codex/AGENTS.md")
        assert "NOT a standalone" in text or "not a replacement" in text.lower()

    def test_codex_agents_references_shared_rules(self):
        text = read("codex/AGENTS.md")
        assert "Shared Quality Rules" in text

    def test_readme_has_platform_positioning(self):
        text = read("README.md")
        assert "Claude Skill vs Codex Adapter" in text

    def test_readme_clarifies_codex_not_replacement(self):
        text = read("README.md")
        assert "not a replacement" in text.lower() or "NOT a replacement" in text


# ---------------------------------------------------------------------------
# Quality audit not all-checkbox
# ---------------------------------------------------------------------------

class TestQualityAuditNotCheckbox:
    """Quality audit must use three-state, not all [x] checkboxes."""

    def test_codex_quality_audit_uses_three_state(self):
        text = read("codex/checklists/quality-audit.md")
        assert "pass / partial / fail" in text

    def test_paper_analysis_quality_audit_uses_three_state(self):
        text = read("templates/paper-analysis-template.md")
        assert "pass / partial / fail" in text

    def test_innovation_brief_quality_audit_uses_three_state(self):
        text = read("templates/innovation-brief-template.md")
        assert "pass / partial / fail" in text


# ---------------------------------------------------------------------------
# Validator passes on current repo
# ---------------------------------------------------------------------------

class TestValidatorPasses:
    def test_validate_skill_script_runs(self, tmp_path):
        import shutil
        import subprocess
        import sys
        dst = tmp_path / "paper-innovation-analyst"
        shutil.copytree(REPO_ROOT, dst, ignore=shutil.ignore_patterns(".git", ".pytest_cache", "__pycache__", "dist", "outputs", ".claude"))
        result = subprocess.run(
            [sys.executable, str(dst / "scripts" / "validate_skill.py"), str(dst)],
            capture_output=True, text=True,
        )
        assert result.returncode == 0, f"Validator failed: {result.stderr}"
