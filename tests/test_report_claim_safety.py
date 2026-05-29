"""Tests for claim safety enforcement across templates and SKILL.md.

v0.5.5-beta: Enhanced claim safety with Chinese trigger words.
"""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Chinese banned words detection
# ---------------------------------------------------------------------------

class TestChineseBannedWords:
    """Chinese banned words must be detectable in templates."""

    CHINESE_BANNED = [
        "首个", "首次", "第一个", "首次提出",
        "完全兼容", "实时", "零开销",
        "ONNX兼容性好", "部署完全兼容",
        "单GPU 8GB+", "VRAM 2-4GB", "4K <200ms",
        "8GB显存", "单卡8GB",
    ]

    def test_skill_md_lists_chinese_banned(self):
        text = read("SKILL.md")
        for word in self.CHINESE_BANNED:
            assert word in text, f"SKILL.md missing Chinese banned word: {word}"

    def test_paper_analysis_template_lists_chinese_banned(self):
        text = read("templates/paper-analysis-template.md")
        for word in self.CHINESE_BANNED:
            assert word in text, f"paper-analysis-template.md missing Chinese banned word: {word}"

    def test_codex_sota_checklist_lists_chinese_banned(self):
        text = read("codex/checklists/sota-claim-safety.md")
        for word in self.CHINESE_BANNED:
            assert word in text, f"sota-claim-safety.md missing Chinese banned word: {word}"


# ---------------------------------------------------------------------------
# Claim safety check exists in templates
# ---------------------------------------------------------------------------

class TestClaimSafetyInTemplates:
    """Claim safety check must exist in all relevant templates."""

    def test_paper_analysis_has_claim_safety(self):
        text = read("templates/paper-analysis-template.md")
        assert "Claim Safety Check" in text

    def test_innovation_brief_has_claim_safety(self):
        text = read("templates/innovation-brief-template.md")
        assert "Claim Safety Check" in text

    def test_experiment_plan_has_claim_safety(self):
        text = read("templates/experiment-plan-template.md")
        assert "Claim Safety Check" in text

    def test_strong_argument_has_claim_safety(self):
        text = read("templates/strong-argument-template.md")
        assert "Claim Safety Check" in text or "SOTA Classification" in text


# ---------------------------------------------------------------------------
# Innovation template required fields
# ---------------------------------------------------------------------------

class TestInnovationRequiredFields:
    """Innovation template must require evidence level, validation, compatibility, etc."""

    def test_evidence_level_required(self):
        text = read("templates/innovation-brief-template.md")
        assert "Evidence level:" in text

    def test_required_validation_required(self):
        text = read("templates/innovation-brief-template.md")
        assert "Required validation" in text

    def test_mechanism_compatibility_required(self):
        text = read("templates/innovation-brief-template.md")
        assert "Mechanism Compatibility Check" in text

    def test_deployment_risk_required(self):
        text = read("templates/innovation-brief-template.md")
        assert "deployment" in text.lower() and "risk" in text.lower()

    def test_minimal_experiment_required(self):
        text = read("templates/innovation-brief-template.md")
        assert "Minimal viable experiment" in text

    def test_failure_criteria_present(self):
        text = read("templates/innovation-brief-template.md")
        # Innovation template should reference failure criteria
        assert "failure" in text.lower() or "Failure" in text


# ---------------------------------------------------------------------------
# Ablation table context fields
# ---------------------------------------------------------------------------

class TestAblationTableContext:
    """Ablation table integrity check must have fixed/changed/final config fields."""

    def test_paper_analysis_has_fixed_variables(self):
        text = read("templates/paper-analysis-template.md")
        assert "Fixed variables" in text

    def test_paper_analysis_has_changed_variable(self):
        text = read("templates/paper-analysis-template.md")
        assert "Changed variable" in text

    def test_paper_analysis_has_final_configuration(self):
        text = read("templates/paper-analysis-template.md")
        assert "Final full configuration" in text

    def test_paper_analysis_has_delta_recalculated(self):
        text = read("templates/paper-analysis-template.md")
        assert "Delta values recalculated" in text

    def test_paper_analysis_has_overgeneralization_risk(self):
        text = read("templates/paper-analysis-template.md")
        assert "Risk of overgeneralization" in text


# ---------------------------------------------------------------------------
# Packaging excludes caches and old artifacts
# ---------------------------------------------------------------------------

class TestPackagingExcludesCaches:
    """Packaging must exclude cache, pyc, dist, old zip/skill."""

    def test_package_skill_excludes_dist(self):
        text = read("scripts/package_skill.py")
        assert '"dist"' in text

    def test_package_skill_excludes_pycache(self):
        text = read("scripts/package_skill.py")
        assert "__pycache__" in text

    def test_package_skill_excludes_pyc(self):
        text = read("scripts/package_skill.py")
        assert ".pyc" in text

    def test_package_codex_excludes_dist(self):
        text = read("scripts/package_codex_adapter.py")
        assert '"dist"' in text

    def test_package_codex_excludes_pycache(self):
        text = read("scripts/package_codex_adapter.py")
        assert "__pycache__" in text


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
