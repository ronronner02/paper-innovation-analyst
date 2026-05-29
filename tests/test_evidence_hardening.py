"""Tests for v0.5.3-beta through v0.5.5-beta evidence hardening features."""

from __future__ import annotations

from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# SKILL.md evidence hardening
# ---------------------------------------------------------------------------

class TestSkillMdEvidenceHardening:
    def test_two_pass_literature_synthesis(self):
        text = read("SKILL.md")
        assert "Two-pass Literature Synthesis" in text

    def test_corpus_inventory(self):
        text = read("SKILL.md")
        assert "Corpus Inventory" in text

    def test_evidence_strength_rules(self):
        text = read("SKILL.md")
        assert "Evidence Strength" in text or "Claim Safety" in text

    def test_claim_safety_trigger_words(self):
        text = read("SKILL.md")
        for word in ["first", "SOTA", "ONNX compatible", "deployment-ready",
                      "negligible FLOPs", "Engineering hypothesis requiring validation"]:
            assert word in text, f"SKILL.md missing trigger word: {word}"

    def test_claim_safety_chinese_trigger_words(self):
        text = read("SKILL.md")
        for word in ["首个", "首次", "第一个", "完全兼容", "实时", "零开销",
                      "ONNX兼容性好", "部署完全兼容", "单GPU 8GB+", "VRAM 2-4GB", "4K <200ms"]:
            assert word in text, f"SKILL.md missing Chinese trigger word: {word}"

    def test_ablation_table_integrity(self):
        text = read("SKILL.md")
        assert "Ablation Table Integrity" in text


# ---------------------------------------------------------------------------
# Multi-paper template
# ---------------------------------------------------------------------------

class TestMultiPaperTemplate:
    def test_corpus_inventory(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "Corpus Inventory" in text

    def test_paper_tiering(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "Paper Tiering" in text
        assert "Tier A" in text
        assert "Tier B" in text

    def test_evidence_maturity(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "Evidence Maturity" in text

    def test_mechanism_compatibility_check(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "Mechanism Compatibility Check" in text

    def test_quality_audit(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "Quality Audit" in text

    def test_cross_domain_analogy_label(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "cross-domain analogy" in text


# ---------------------------------------------------------------------------
# Innovation brief template
# ---------------------------------------------------------------------------

class TestInnovationBriefTemplate:
    def test_claim_safety_check(self):
        text = read("templates/innovation-brief-template.md")
        assert "Claim Safety Check" in text

    def test_evidence_maturity(self):
        text = read("templates/innovation-brief-template.md")
        assert "Evidence Maturity" in text

    def test_mechanism_compatibility_check(self):
        text = read("templates/innovation-brief-template.md")
        assert "Mechanism Compatibility Check" in text

    def test_quality_audit(self):
        text = read("templates/innovation-brief-template.md")
        assert "Quality Audit" in text

    def test_evidence_level_field(self):
        text = read("templates/innovation-brief-template.md")
        assert "Evidence level:" in text

    def test_engineering_assumptions_field(self):
        text = read("templates/innovation-brief-template.md")
        assert "Engineering assumptions:" in text


# ---------------------------------------------------------------------------
# Paper analysis template
# ---------------------------------------------------------------------------

class TestPaperAnalysisTemplate:
    def test_ablation_table_integrity_check(self):
        text = read("templates/paper-analysis-template.md")
        assert "Ablation Table Integrity Check" in text

    def test_claim_safety_check(self):
        text = read("templates/paper-analysis-template.md")
        assert "Claim Safety Check" in text

    def test_quality_audit(self):
        text = read("templates/paper-analysis-template.md")
        assert "Quality Audit" in text


# ---------------------------------------------------------------------------
# Strong argument template
# ---------------------------------------------------------------------------

class TestStrongArgumentTemplate:
    def test_evidence_maturity(self):
        text = read("templates/strong-argument-template.md")
        assert "Evidence Maturity" in text

    def test_cross_domain_analogy(self):
        text = read("templates/strong-argument-template.md")
        assert "cross-domain analogy" in text

    def test_quality_audit(self):
        text = read("templates/strong-argument-template.md")
        assert "Quality Audit" in text


# ---------------------------------------------------------------------------
# Quality audit uses three-state (not just checkboxes)
# ---------------------------------------------------------------------------

class TestQualityAuditThreeState:
    def test_paper_analysis_uses_pass_partial_fail(self):
        text = read("templates/paper-analysis-template.md")
        assert "pass / partial / fail" in text

    def test_multi_paper_uses_pass_partial_fail(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "pass / partial / fail" in text

    def test_innovation_brief_uses_pass_partial_fail(self):
        text = read("templates/innovation-brief-template.md")
        assert "pass / partial / fail" in text

    def test_strong_argument_uses_pass_partial_fail(self):
        text = read("templates/strong-argument-template.md")
        assert "pass / partial / fail" in text


# ---------------------------------------------------------------------------
# No unsupported strong claims encouraged
# ---------------------------------------------------------------------------

class TestNoUnsupportedClaims:
    def test_skill_md_requires_evidence_for_deployment_claims(self):
        text = read("SKILL.md")
        # Must not encourage unvalidated deployment claims
        assert "requires export validation" in text or "requires profiling" in text
        assert "Engineering hypothesis requiring validation" in text

    def test_innovation_template_labels_assumptions(self):
        text = read("templates/innovation-brief-template.md")
        assert "requires validation" in text.lower() or "assumption" in text.lower()


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
