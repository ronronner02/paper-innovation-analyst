"""Tests for the Codex adapter structure and verification gates."""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Codex adapter structure
# ---------------------------------------------------------------------------

class TestCodexAdapterStructure:
    """codex/ directory must exist with correct structure."""

    def test_root_agents_md_exists(self):
        """Root AGENTS.md is the Codex auto-entry point."""
        path = REPO_ROOT / "AGENTS.md"
        assert path.exists(), "Root AGENTS.md missing (Codex auto-entry point)"
        assert path.stat().st_size > 0, "Root AGENTS.md is empty"

    def test_root_agents_md_references_codex_agents(self):
        text = read("AGENTS.md")
        assert "codex/AGENTS.md" in text

    def test_codex_directory_exists(self):
        assert (REPO_ROOT / "codex").is_dir()

    def test_agents_md_exists(self):
        path = REPO_ROOT / "codex" / "AGENTS.md"
        assert path.exists(), "codex/AGENTS.md missing"
        assert path.stat().st_size > 0, "codex/AGENTS.md is empty"

    def test_agents_md_references_skill_md(self):
        text = read("codex/AGENTS.md")
        assert "SKILL.md" in text

    def test_codex_readme_exists(self):
        path = REPO_ROOT / "codex" / "README.md"
        assert path.exists(), "codex/README.md missing"
        assert path.stat().st_size > 0, "codex/README.md is empty"

    def test_prompts_directory_has_4_files(self):
        prompts = list((REPO_ROOT / "codex" / "prompts").glob("*.md"))
        assert len(prompts) >= 4, f"Expected 4+ prompt files, found {len(prompts)}"

    def test_validate_report_quality_exists(self):
        path = REPO_ROOT / "codex" / "prompts" / "validate-report-quality.md"
        assert path.exists(), "codex/prompts/validate-report-quality.md missing"
        assert path.stat().st_size > 0

    def test_checklists_directory_has_4_files(self):
        checklists = list((REPO_ROOT / "codex" / "checklists").glob("*.md"))
        assert len(checklists) >= 4, f"Expected 4+ checklist files, found {len(checklists)}"

    def test_all_codex_files_nonempty(self):
        codex_dir = REPO_ROOT / "codex"
        for p in codex_dir.rglob("*.md"):
            assert p.stat().st_size > 0, f"Empty codex file: {p.relative_to(REPO_ROOT)}"


# ---------------------------------------------------------------------------
# Codex README distinguishes Claude Skill vs Codex Adapter
# ---------------------------------------------------------------------------

class TestCodexReadmeDistinction:
    """README must distinguish Claude Skill from Codex Adapter."""

    def test_readme_has_codex_adapter_section(self):
        text = read("README.md")
        assert "Codex Adapter" in text

    def test_readme_clarifies_not_standalone(self):
        text = read("README.md")
        assert "NOT a standalone" in text or "not a standalone" in text.lower()

    def test_ci_has_package_codex_adapter(self):
        text = read(".github/workflows/validate.yml")
        assert "package_codex_adapter.py" in text


# ---------------------------------------------------------------------------
# Bibliographic Verification Gate (requirement 5)
# ---------------------------------------------------------------------------

class TestBibliographicVerificationGate:
    """SKILL.md and templates must include bibliographic verification."""

    def test_skill_md_has_bibliographic_gate(self):
        text = read("SKILL.md")
        assert "Bibliographic Verification Gate" in text

    def test_skill_md_has_doi_verification(self):
        text = read("SKILL.md")
        assert "DOI" in text

    def test_paper_analysis_template_has_bibliographic_verification(self):
        text = read("templates/paper-analysis-template.md")
        assert "Bibliographic Verification" in text

    def test_multi_paper_template_has_bibliographic_verified(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "Bibliographic verified" in text

    def test_codex_checklist_exists(self):
        path = REPO_ROOT / "codex" / "checklists" / "bibliographic-verification.md"
        assert path.exists()
        text = path.read_text(encoding="utf-8")
        assert "Title" in text
        assert "DOI" in text


# ---------------------------------------------------------------------------
# Table Identity Gate (requirement 6)
# ---------------------------------------------------------------------------

class TestTableIdentityGate:
    """SKILL.md and templates must include table identity verification."""

    def test_skill_md_has_table_identity_gate(self):
        text = read("SKILL.md")
        assert "Table Identity Gate" in text

    def test_skill_md_has_noise_setting(self):
        text = read("SKILL.md")
        assert "noise setting" in text.lower()

    def test_codex_checklist_exists(self):
        path = REPO_ROOT / "codex" / "checklists" / "table-identity.md"
        assert path.exists()
        text = path.read_text(encoding="utf-8")
        assert "Table ID" in text
        assert "noise setting" in text.lower()


# ---------------------------------------------------------------------------
# SOTA Claim Classification (requirement 7)
# ---------------------------------------------------------------------------

class TestSOTAClaimClassification:
    """SKILL.md and templates must classify SOTA claims."""

    def test_skill_md_has_sota_classification(self):
        text = read("SKILL.md")
        assert "SOTA Claim Classification" in text

    def test_skill_md_has_tripartite(self):
        text = read("SKILL.md")
        assert "paper-claimed SOTA" in text
        assert "supported within evaluated baselines" in text
        assert "externally verified SOTA" in text

    def test_innovation_template_has_sota_classification(self):
        text = read("templates/innovation-brief-template.md")
        assert "paper-claimed SOTA" in text

    def test_strong_argument_has_sota_classification(self):
        text = read("templates/strong-argument-template.md")
        assert "SOTA Classification" in text

    def test_codex_checklist_exists(self):
        path = REPO_ROOT / "codex" / "checklists" / "sota-claim-safety.md"
        assert path.exists()
        text = path.read_text(encoding="utf-8")
        assert "paper-claimed SOTA" in text


# ---------------------------------------------------------------------------
# Quality Audit: report vs paper evidence (requirement 8)
# ---------------------------------------------------------------------------

class TestQualityAuditDistinction:
    """Templates must distinguish report quality from paper evidence quality."""

    def test_paper_analysis_has_report_quality(self):
        text = read("templates/paper-analysis-template.md")
        assert "Report Quality" in text

    def test_paper_analysis_has_paper_evidence_quality(self):
        text = read("templates/paper-analysis-template.md")
        assert "Paper Evidence Quality" in text

    def test_innovation_brief_has_report_quality(self):
        text = read("templates/innovation-brief-template.md")
        assert "Report Quality" in text

    def test_innovation_brief_has_paper_evidence_quality(self):
        text = read("templates/innovation-brief-template.md")
        assert "Paper Evidence Quality" in text

    def test_multi_paper_has_report_quality(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "Report Quality" in text

    def test_multi_paper_has_paper_evidence_quality(self):
        text = read("templates/multi-paper-comparison-template.md")
        assert "Paper Evidence Quality" in text

    def test_codex_checklist_exists(self):
        path = REPO_ROOT / "codex" / "checklists" / "quality-audit.md"
        assert path.exists()
        text = path.read_text(encoding="utf-8")
        assert "Report Quality" in text
        assert "Paper Evidence Quality" in text


# ---------------------------------------------------------------------------
# first/首个 banned even as speculative (requirement 9)
# ---------------------------------------------------------------------------

class TestFirstBanned:
    """'first / 首个' must be banned even when labeled speculative."""

    def test_skill_md_bans_first_as_speculative(self):
        text = read("SKILL.md")
        assert "BANNED even when labeled speculative" in text

    def test_codex_checklist_bans_first(self):
        text = read("codex/checklists/sota-claim-safety.md")
        assert "BANNED even when labeled speculative" in text

    def test_codex_prompt_bans_first(self):
        text = read("codex/prompts/innovation-mining.md")
        assert "BANNED even when labeled speculative" in text


# ---------------------------------------------------------------------------
# DOI extraction from PDF footer/header
# ---------------------------------------------------------------------------

class TestDOIExtraction:
    """Bibliographic gate must require scanning PDF for DOI."""

    def test_checklist_requires_doi_scanning(self):
        text = read("codex/checklists/bibliographic-verification.md")
        assert "scan the PDF" in text.lower() or "scan" in text.lower()
        assert "doi.org" in text.lower() or "DOI:" in text

    def test_checklist_dn_tod_example(self):
        text = read("codex/checklists/bibliographic-verification.md")
        assert "10.1016/j.patcog.2026.113448" in text

    def test_checklist_rejects_not_found_when_doi_present(self):
        text = read("codex/checklists/bibliographic-verification.md")
        assert "Do NOT write" in text and "not found" in text.lower()

    def test_skill_md_requires_doi_extraction(self):
        text = read("SKILL.md")
        assert "DOI extraction is mandatory" in text

    def test_template_requires_doi_scanning(self):
        text = read("templates/paper-analysis-template.md")
        assert "scan" in text.lower() and "doi" in text.lower()


# ---------------------------------------------------------------------------
# Table metric from caption
# ---------------------------------------------------------------------------

class TestTableMetricFromCaption:
    """Table metric must come from caption, not convention."""

    def test_checklist_requires_metric_from_caption(self):
        text = read("codex/checklists/table-identity.md")
        assert "caption" in text.lower() and "metric" in text.lower()

    def test_checklist_m_map_example(self):
        text = read("codex/checklists/table-identity.md")
        assert "We report mAP" in text

    def test_checklist_rejects_relabeling(self):
        text = read("codex/checklists/table-identity.md")
        assert "do NOT relabel" in text.lower() or "do NOT" in text

    def test_skill_md_metric_from_caption(self):
        text = read("SKILL.md")
        assert "read from the table caption" in text.lower() or "table caption" in text.lower()


# ---------------------------------------------------------------------------
# Paper-claimed SOTA not rewritten
# ---------------------------------------------------------------------------

class TestPaperClaimedSOTAPreservation:
    """Paper-claimed SOTA must not be rewritten as 'did not claim SOTA'."""

    def test_checklist_preserves_paper_claimed_sota(self):
        text = read("codex/checklists/sota-claim-safety.md")
        assert "Do NOT write" in text and "did not claim SOTA" in text

    def test_checklist_has_example(self):
        text = read("codex/checklists/sota-claim-safety.md")
        assert "state-of-the-art" in text.lower()
        assert "paper-claimed SOTA; supported within evaluated baselines; not externally verified" in text

    def test_skill_md_preserves_paper_claimed_sota(self):
        text = read("SKILL.md")
        assert "Do NOT write" in text and "did not claim SOTA" in text


# ---------------------------------------------------------------------------
# Innovation: hypothesis unless measured
# ---------------------------------------------------------------------------

class TestInnovationHypothesisLabel:
    """Innovation estimates must be labeled as hypothesis unless measured."""

    def test_innovation_prompt_labels_estimates(self):
        text = read("codex/prompts/innovation-mining.md")
        assert "hypothesis unless measured" in text.lower()

    def test_innovation_template_labels_outcome(self):
        text = read("templates/innovation-brief-template.md")
        assert "hypothesis unless measured" in text.lower() or "Target measurable outcome" in text


# ---------------------------------------------------------------------------
# Validator passes with codex adapter
# ---------------------------------------------------------------------------

class TestValidatorPasses:
    def test_validate_skill_script_runs(self, tmp_path: Path) -> None:
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
