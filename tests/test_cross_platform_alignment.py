"""Tests for cross-platform quality alignment between Claude Skill and Codex Adapter.

v0.5.5-beta: Both platforms must share core quality rules.
"""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Core entry points exist for both platforms
# ---------------------------------------------------------------------------

class TestCoreEntryPoints:
    """Both platforms must have their core entry points."""

    def test_skill_md_exists(self):
        path = REPO_ROOT / "SKILL.md"
        assert path.exists(), "SKILL.md missing (Claude Skill entry)"
        assert path.stat().st_size > 0

    def test_root_agents_md_exists(self):
        path = REPO_ROOT / "AGENTS.md"
        assert path.exists(), "AGENTS.md missing (Codex auto-entry point)"
        assert path.stat().st_size > 0

    def test_codex_agents_md_exists(self):
        path = REPO_ROOT / "codex" / "AGENTS.md"
        assert path.exists(), "codex/AGENTS.md missing"
        assert path.stat().st_size > 0

    def test_codex_prompts_dir_exists(self):
        path = REPO_ROOT / "codex" / "prompts"
        assert path.is_dir(), "codex/prompts/ missing"

    def test_codex_checklists_dir_exists(self):
        path = REPO_ROOT / "codex" / "checklists"
        assert path.is_dir(), "codex/checklists/ missing"


# ---------------------------------------------------------------------------
# Shared core safety rules
# ---------------------------------------------------------------------------

class TestSharedCoreSafetyRules:
    """Both platforms must enforce the same core safety rules."""

    def test_evidence_strength_in_skill_md(self):
        text = read("SKILL.md")
        assert "Evidence Strength" in text

    def test_claim_safety_in_skill_md(self):
        text = read("SKILL.md")
        assert "Claim Safety" in text

    def test_table_identity_in_skill_md(self):
        text = read("SKILL.md")
        assert "Table Identity Gate" in text

    def test_ablation_integrity_in_skill_md(self):
        text = read("SKILL.md")
        assert "Ablation Table Integrity" in text

    def test_quality_audit_in_skill_md(self):
        text = read("SKILL.md")
        assert "Quality Audit" in text or "quality gate" in text.lower()

    def test_bibliographic_gate_in_skill_md(self):
        text = read("SKILL.md")
        assert "Bibliographic Verification Gate" in text

    def test_sota_classification_in_skill_md(self):
        text = read("SKILL.md")
        assert "SOTA Claim Classification" in text

    def test_claim_safety_in_codex_checklist(self):
        text = read("codex/checklists/sota-claim-safety.md")
        assert "Trigger Words" in text

    def test_table_identity_in_codex_checklist(self):
        text = read("codex/checklists/table-identity.md")
        assert "Table ID" in text

    def test_quality_audit_in_codex_checklist(self):
        text = read("codex/checklists/quality-audit.md")
        assert "Report Quality" in text
        assert "Paper Evidence Quality" in text

    def test_bibliographic_in_codex_checklist(self):
        text = read("codex/checklists/bibliographic-verification.md")
        assert "Title" in text
        assert "DOI" in text


# ---------------------------------------------------------------------------
# Chinese trigger words detection
# ---------------------------------------------------------------------------

class TestChineseTriggerWords:
    """Chinese strong-claim trigger words must be detected in both platforms."""

    CHINESE_TRIGGERS = [
        "首个", "首次", "第一个", "首次提出", "全新",
        "完全兼容", "实时", "零开销",
        "ONNX兼容性好", "部署完全兼容",
        "单GPU 8GB+", "VRAM 2-4GB", "4K <200ms",
        "8GB显存", "单卡8GB",
    ]

    def test_skill_md_lists_chinese_triggers(self):
        text = read("SKILL.md")
        for word in self.CHINESE_TRIGGERS:
            assert word in text, f"SKILL.md missing Chinese trigger word: {word}"

    def test_codex_sota_checklist_lists_chinese_triggers(self):
        text = read("codex/checklists/sota-claim-safety.md")
        for word in self.CHINESE_TRIGGERS:
            assert word in text, f"codex/checklists/sota-claim-safety.md missing Chinese trigger word: {word}"

    def test_paper_analysis_template_lists_chinese_triggers(self):
        text = read("templates/paper-analysis-template.md")
        for word in self.CHINESE_TRIGGERS:
            assert word in text, f"paper-analysis-template.md missing Chinese trigger word: {word}"

    def test_codex_validate_report_lists_chinese_triggers(self):
        text = read("codex/prompts/validate-report-quality.md")
        for word in self.CHINESE_TRIGGERS:
            assert word in text, f"codex/prompts/validate-report-quality.md missing Chinese trigger word: {word}"


# ---------------------------------------------------------------------------
# Version consistency
# ---------------------------------------------------------------------------

class TestVersionConsistency:
    """Version must be consistent across all files."""

    def test_package_skill_version(self):
        text = read("scripts/package_skill.py")
        assert "v0.5.5-beta" in text

    def test_package_codex_version(self):
        text = read("scripts/package_codex_adapter.py")
        assert "v0.5.5-beta" in text

    def test_readme_version(self):
        text = read("README.md")
        assert "v0.5.5-beta" in text

    def test_changelog_version(self):
        text = read("CHANGELOG.md")
        assert "v0.5.5-beta" in text

    def test_paper_analysis_template_no_hardcoded_old_version(self):
        text = read("templates/paper-analysis-template.md")
        # Should not have hardcoded old version
        assert "v0.5.3-beta" not in text
        assert "v0.5.4-beta" not in text


# ---------------------------------------------------------------------------
# Quality audit uses three-state
# ---------------------------------------------------------------------------

class TestQualityAuditThreeState:
    """Quality audit must use pass/partial/fail, not just checkboxes."""

    def test_paper_analysis_uses_pass_partial_fail(self):
        text = read("templates/paper-analysis-template.md")
        assert "pass / partial / fail" in text

    def test_innovation_brief_uses_pass_partial_fail(self):
        text = read("templates/innovation-brief-template.md")
        assert "pass / partial / fail" in text

    def test_codex_quality_audit_uses_pass_partial_fail(self):
        text = read("codex/checklists/quality-audit.md")
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
