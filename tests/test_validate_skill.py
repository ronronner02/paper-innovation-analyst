#!/usr/bin/env python3
"""Tests for the Paper Innovation Analyst Skill validation script."""

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
        cwd=REPO_ROOT,
    )


class TestValidatorPasses:
    """The validator should pass on the current repository."""

    def test_validator_exits_clean(self, tmp_path: Path) -> None:
        """Run validator on a clean copy of the repo to avoid .claude/ recreation issues."""
        import shutil
        dst = tmp_path / "paper-innovation-analyst"
        shutil.copytree(REPO_ROOT, dst, ignore=shutil.ignore_patterns(".git", ".pytest_cache", "__pycache__", "dist", "outputs", ".claude"))
        result = run_validator(str(dst))
        assert result.returncode == 0, f"Validator failed:\n{result.stderr}"
        assert "OK: skill repository validation passed" in result.stdout

    def test_skill_md_has_security_rules(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "Input Security Rules" in text

    def test_skill_md_has_untrusted_research_material(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "untrusted research material" in text.lower()

    def test_skill_md_has_prompt_injection_protection(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "prompt injection" in text.lower() or "embedded instruction" in text.lower()

    def test_skill_md_has_quality_gate(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "quality gate" in text.lower() or "Quality Gate" in text

    def test_skill_md_has_dynamic_defaults(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "default to" in text.lower()

    def test_skill_md_references_document_ingestion(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "document-ingestion-pipeline" in text

    def test_skill_md_references_gbt7714(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "gbt7714-2015-examples" in text

    def test_skill_md_references_cv_addendum(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "cv-detection-addendum" in text

    def test_skill_md_references_quality_gates(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "idea-quality-gates" in text


class TestRequiredFiles:
    """All required files must exist and be non-empty."""

    REQUIRED = [
        "SKILL.md", "README.md", "CHANGELOG.md", "CLAUDE.md", "LICENSE",
        ".gitignore", "requirements-optional.txt",
        "scripts/validate_skill.py", "scripts/extract_paper_assets.py", "scripts/package_skill.py",
        "references/review-rubric.md", "references/domain-addenda.md",
        "references/document-ingestion-pipeline.md", "references/gbt7714-2015-examples.md",
        "references/cv-detection-addendum.md", "references/idea-quality-gates.md",
        "templates/paper-analysis-template.md", "templates/innovation-brief-template.md",
        "templates/experiment-plan-template.md", "templates/multi-paper-comparison-template.md",
        "templates/reviewer-report-template.md",
        "templates/strong-argument-template.md",
        "examples/example-prompts.md",
        ".github/workflows/validate.yml",
    ]

    @pytest.mark.parametrize("relpath", REQUIRED)
    def test_file_exists_and_nonempty(self, relpath: str) -> None:
        path = REPO_ROOT / relpath
        assert path.exists(), f"Missing required file: {relpath}"
        assert path.stat().st_size > 0, f"Required file is empty: {relpath}"


class TestGitignore:
    """The .gitignore must exclude sensitive and build files."""

    REQUIRED_ENTRIES = [".claude/settings.local.json", "__pycache__", ".pytest_cache", ".git/"]

    @pytest.mark.parametrize("entry", REQUIRED_ENTRIES)
    def test_gitignore_contains(self, entry: str) -> None:
        text = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8")
        assert entry in text, f".gitignore missing: {entry}"


class TestGBTT7714Examples:
    """GB/T 7714-2015 examples must be correct and comprehensive."""

    def test_contains_journal(self) -> None:
        text = (REPO_ROOT / "references" / "gbt7714-2015-examples.md").read_text(encoding="utf-8")
        assert "[J]" in text

    def test_contains_conference(self) -> None:
        text = (REPO_ROOT / "references" / "gbt7714-2015-examples.md").read_text(encoding="utf-8")
        assert "[C]" in text

    def test_contains_thesis(self) -> None:
        text = (REPO_ROOT / "references" / "gbt7714-2015-examples.md").read_text(encoding="utf-8")
        assert "[D]" in text

    def test_contains_monograph(self) -> None:
        text = (REPO_ROOT / "references" / "gbt7714-2015-examples.md").read_text(encoding="utf-8")
        assert "[M]" in text

    def test_contains_ebol(self) -> None:
        text = (REPO_ROOT / "references" / "gbt7714-2015-examples.md").read_text(encoding="utf-8")
        assert "[EB/OL]" in text

    def test_contains_missing_metadata(self) -> None:
        text = (REPO_ROOT / "references" / "gbt7714-2015-examples.md").read_text(encoding="utf-8")
        assert "Missing metadata" in text

    def test_contains_not_substitute(self) -> None:
        text = (REPO_ROOT / "references" / "gbt7714-2015-examples.md").read_text(encoding="utf-8")
        assert "not a substitute for the official GB/T 7714-2015 standard" in text


class TestCVDetectionAddendum:
    """CV detection addendum must cover key topics."""

    def test_contains_yolo(self) -> None:
        text = (REPO_ROOT / "references" / "cv-detection-addendum.md").read_text(encoding="utf-8")
        assert "YOLO" in text

    def test_contains_backbone_neck_head(self) -> None:
        text = (REPO_ROOT / "references" / "cv-detection-addendum.md").read_text(encoding="utf-8")
        assert "Backbone" in text
        assert "Neck" in text
        assert "Head" in text

    def test_contains_assignment_loss_deployment(self) -> None:
        text = (REPO_ROOT / "references" / "cv-detection-addendum.md").read_text(encoding="utf-8")
        assert "Assignment" in text
        assert "Loss" in text
        assert "Deployment" in text


class TestDocumentIngestionPipeline:
    """Document ingestion pipeline must clarify implemented vs not-implemented."""

    def test_contains_implemented(self) -> None:
        text = (REPO_ROOT / "references" / "document-ingestion-pipeline.md").read_text(encoding="utf-8")
        assert "Implemented by current helper script" in text

    def test_contains_not_implemented(self) -> None:
        text = (REPO_ROOT / "references" / "document-ingestion-pipeline.md").read_text(encoding="utf-8")
        assert "Not implemented directly" in text


class TestTemplates:
    """Templates must contain required sections."""

    def test_innovation_template_has_quality_gate(self) -> None:
        text = (REPO_ROOT / "templates" / "innovation-brief-template.md").read_text(encoding="utf-8")
        assert "quality gate" in text.lower() or "Quality Gate" in text

    def test_innovation_template_has_anti_generic(self) -> None:
        text = (REPO_ROOT / "templates" / "innovation-brief-template.md").read_text(encoding="utf-8")
        assert "anti-generic" in text.lower() or "Anti-generic" in text

    def test_experiment_template_has_reproducibility(self) -> None:
        text = (REPO_ROOT / "templates" / "experiment-plan-template.md").read_text(encoding="utf-8")
        assert "reproducibility" in text.lower() or "Reproducibility" in text

    def test_experiment_template_has_loss_divergence(self) -> None:
        text = (REPO_ROOT / "templates" / "experiment-plan-template.md").read_text(encoding="utf-8")
        assert "Loss divergence" in text or "loss divergence" in text.lower()

    def test_experiment_template_has_gpu_oom(self) -> None:
        text = (REPO_ROOT / "templates" / "experiment-plan-template.md").read_text(encoding="utf-8")
        assert "GPU OOM" in text

    def test_multi_paper_has_method_family_map(self) -> None:
        text = (REPO_ROOT / "templates" / "multi-paper-comparison-template.md").read_text(encoding="utf-8")
        assert "Method Family Map" in text

    def test_multi_paper_has_problem_clustering(self) -> None:
        text = (REPO_ROOT / "templates" / "multi-paper-comparison-template.md").read_text(encoding="utf-8")
        assert "Research Problem Clustering" in text

    def test_all_templates_have_fabrication_rule(self) -> None:
        for path in (REPO_ROOT / "templates").glob("*.md"):
            text = path.read_text(encoding="utf-8").lower()
            assert "fabricat" in text or "missing" in text, f"{path.name} missing anti-fabrication rule"

    def test_all_templates_have_gbt7714(self) -> None:
        for path in (REPO_ROOT / "templates").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            assert "GB/T 7714" in text, f"{path.name} missing GB/T 7714-2015 reference"


class TestREADME:
    """README must not contain unverified claims or bare TODOs."""

    def test_no_unverified_tested_claim(self) -> None:
        text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        assert "Tested with Claude 4.x" not in text

    def test_no_bare_todo(self) -> None:
        text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        # Allow TODO in structured sections but not bare lines
        for line in text.splitlines():
            stripped = line.strip()
            if "TODO" in stripped and not stripped.startswith("#") and not stripped.startswith("-"):
                pytest.fail(f"Bare TODO in README: {stripped[:80]}")

    def test_has_version_info(self) -> None:
        text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        assert "v0.5.3-beta" in text

    def test_has_capability_boundary(self) -> None:
        text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        assert "does not guarantee" in text.lower() or "capability boundary" in text.lower()


class TestCI:
    """CI workflow must include all required steps."""

    def test_ci_has_py_compile(self) -> None:
        text = (REPO_ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        assert "py_compile" in text

    def test_ci_has_pytest(self) -> None:
        text = (REPO_ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        assert "pytest" in text

    def test_ci_has_package_skill(self) -> None:
        text = (REPO_ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        assert "package_skill.py" in text

    def test_ci_has_release_check(self) -> None:
        text = (REPO_ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        assert "--release" in text


class TestNegativeCases:
    """Tests that verify the validator rejects invalid states."""

    def test_validator_rejects_missing_file(self, tmp_path: Path) -> None:
        (tmp_path / "README.md").write_text("test", encoding="utf-8")
        result = run_validator(str(tmp_path))
        assert result.returncode != 0
        assert "Missing required file" in result.stderr


class TestLiteratureSynthesisRouting:
    """SKILL.md and templates must support single-paper vs multi-paper routing."""

    def test_skill_md_has_paper_set_routing(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "Paper Set Routing" in text

    def test_skill_md_has_single_paper_analysis(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "single_paper_analysis" in text

    def test_skill_md_has_literature_synthesis(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "literature_synthesis_and_innovation" in text

    def test_skill_md_no_per_paper_default(self) -> None:
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        assert "Multiple papers do not require multiple full reports" in text

    def test_multi_paper_has_evidence_cards(self) -> None:
        text = (REPO_ROOT / "templates" / "multi-paper-comparison-template.md").read_text(encoding="utf-8")
        assert "Paper Evidence Cards" in text

    def test_multi_paper_has_strong_argument(self) -> None:
        text = (REPO_ROOT / "templates" / "multi-paper-comparison-template.md").read_text(encoding="utf-8")
        assert "Strong Argument Construction" in text

    def test_multi_paper_has_innovation_framework(self) -> None:
        text = (REPO_ROOT / "templates" / "multi-paper-comparison-template.md").read_text(encoding="utf-8")
        assert "Innovation Framework Recommendation" in text

    def test_multi_paper_has_paper_usage_decision(self) -> None:
        text = (REPO_ROOT / "templates" / "multi-paper-comparison-template.md").read_text(encoding="utf-8")
        assert "Paper Usage Decision" in text

    def test_multi_paper_has_type_a_b_c(self) -> None:
        text = (REPO_ROOT / "templates" / "multi-paper-comparison-template.md").read_text(encoding="utf-8")
        assert "Single-paper Extension" in text
        assert "Cross-paper Fusion" in text
        assert "New Framework from Shared Gaps" in text

    def test_innovation_template_has_framework_source_type(self) -> None:
        text = (REPO_ROOT / "templates" / "innovation-brief-template.md").read_text(encoding="utf-8")
        assert "Framework Source Type" in text

    def test_strong_argument_template_exists(self) -> None:
        path = REPO_ROOT / "templates" / "strong-argument-template.md"
        assert path.exists()

    def test_strong_argument_has_claim_type(self) -> None:
        text = (REPO_ROOT / "templates" / "strong-argument-template.md").read_text(encoding="utf-8")
        assert "Claim type" in text

    def test_strong_argument_has_cross_paper_reasoning(self) -> None:
        text = (REPO_ROOT / "templates" / "strong-argument-template.md").read_text(encoding="utf-8")
        assert "Cross-paper Reasoning" in text

    def test_strong_argument_has_writing_ready(self) -> None:
        text = (REPO_ROOT / "templates" / "strong-argument-template.md").read_text(encoding="utf-8")
        assert "Writing-ready" in text
