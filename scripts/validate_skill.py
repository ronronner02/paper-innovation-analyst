#!/usr/bin/env python3
"""Validator for the Paper Innovation Analyst Skill repository.

Supports two modes:
    python scripts/validate_skill.py <path>             # development mode
    python scripts/validate_skill.py <path> --release   # release cleanliness mode
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"WARNING: {message}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Required files
# ---------------------------------------------------------------------------

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "CLAUDE.md",
    "LICENSE",
    ".gitignore",
    "requirements-optional.txt",
    "scripts/validate_skill.py",
    "scripts/extract_paper_assets.py",
    "scripts/package_skill.py",
    "scripts/package_codex_adapter.py",
    "references/document-ingestion-pipeline.md",
    "references/gbt7714-2015-examples.md",
    "references/cv-detection-addendum.md",
    "references/idea-quality-gates.md",
    "references/review-rubric.md",
    "references/domain-addenda.md",
    "templates/paper-analysis-template.md",
    "templates/innovation-brief-template.md",
    "templates/experiment-plan-template.md",
    "templates/multi-paper-comparison-template.md",
    "templates/reviewer-report-template.md",
    "templates/strong-argument-template.md",
    "examples/example-prompts.md",
    ".github/workflows/validate.yml",
]

REQUIRED_SKILL_PHRASES = [
    "Input Security Rules",
    "untrusted research material",
    "Document Ingestion Scope",
    "document-ingestion-pipeline.md",
    "Separate evidence from inference",
    "Do not fabricate",
    "Innovation Point Generation",
    "Feasibility score",
    "Novelty score",
    "Risk score",
    "GB/T 7714-2015",
    "Ablation Table Integrity",
    "Engineering hypothesis requiring validation",
]

# Items that must not appear in a release package
RELEASE_BANNED = [
    ".git",
    ".pytest_cache",
    "__pycache__",
    ".claude/settings.local.json",
    ".DS_Store",
    ".env",
    ".venv",
    "outputs",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_text(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def require_contains(text: str, needle: str, source: str) -> None:
    if needle not in text:
        fail(f"Missing requirement in {source}: {needle}")


def parse_frontmatter(text: str) -> dict[str, str]:
    import re
    m = re.match(r"^---\n(?P<body>.*?)\n---\n", text, re.DOTALL)
    if not m:
        fail("SKILL.md must start with YAML frontmatter delimited by ---")
    meta: dict[str, str] = {}
    for line in m.group("body").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta


# ---------------------------------------------------------------------------
# Core validation (always runs)
# ---------------------------------------------------------------------------

def validate_required_files(root: Path) -> None:
    for rel in REQUIRED_FILES:
        p = root / rel
        if not p.exists():
            fail(f"Missing required file: {rel}")
        if p.is_file() and p.stat().st_size == 0:
            fail(f"Required file is empty: {rel}")
    # Sensitive file must never exist
    if (root / ".claude" / "settings.local.json").exists():
        fail("Sensitive file must not exist: .claude/settings.local.json")


def validate_skill_md(root: Path) -> str:
    text = read_text(root, "SKILL.md")
    meta = parse_frontmatter(text)
    if meta.get("name") != "paper-innovation-analyst":
        warn(f"Unexpected skill name: {meta.get('name')}")
    desc = meta.get("description", "")
    if len(desc) < 80:
        warn("Description may be too short to trigger reliably")
    if len(desc) > 700:
        warn("Description is long; consider tightening")
    for phrase in REQUIRED_SKILL_PHRASES:
        require_contains(text, phrase, "SKILL.md")
    if "do not fabricate" not in text.lower() and "never invent" not in text.lower():
        fail("SKILL.md must include anti-fabrication instruction")
    # Security
    lower = text.lower()
    if "untrusted research material" not in lower:
        fail("SKILL.md missing: untrusted research material")
    if "prompt injection" not in lower and "embedded instruction" not in lower:
        fail("SKILL.md missing: prompt injection / embedded instruction protection")
    # Capability boundary
    if "does not guarantee" not in lower and "document ingestion scope" not in lower:
        fail("SKILL.md missing capability boundary declaration")
    # Dynamic defaults
    if "default to" not in lower:
        fail("SKILL.md missing dynamic default output selection")
    # Reference links
    for ref in ["idea-quality-gates", "cv-detection-addendum", "gbt7714-2015-examples", "document-ingestion-pipeline"]:
        if ref not in text:
            fail(f"SKILL.md must reference {ref}.md")
    # Paper Set Routing Logic
    for needle in ["single_paper_analysis", "literature_synthesis_and_innovation",
                   "Paper Set Routing", "Multiple papers do not require multiple full reports"]:
        if needle not in text:
            fail(f"SKILL.md missing Paper Set Routing requirement: {needle}")
    # Evidence Hardening (v0.5.3)
    for needle in ["Two-pass Literature Synthesis", "Corpus Inventory",
                   "Evidence Strength", "Claim Safety", "Ablation Table Integrity"]:
        if needle not in text:
            fail(f"SKILL.md missing evidence hardening requirement: {needle}")
    # v0.5.4 gates
    for needle in ["Bibliographic Verification Gate", "Table Identity Gate",
                   "SOTA Claim Classification", "paper-claimed SOTA",
                   "supported within evaluated baselines", "externally verified SOTA"]:
        if needle not in text:
            fail(f"SKILL.md missing v0.5.4 gate requirement: {needle}")
    if "first / 首个" in text:
        # Must ban first/首个 even as speculative
        if "BANNED even when labeled speculative" not in text:
            fail("SKILL.md must ban 'first / 首个' even when labeled speculative")
    # v0.5.5 gates: Chinese trigger words
    for needle in ["首个", "首次", "第一个", "完全兼容", "实时", "零开销",
                   "ONNX兼容性好", "部署完全兼容", "单GPU 8GB+", "VRAM 2-4GB", "4K <200ms"]:
        if needle not in text:
            fail(f"SKILL.md missing v0.5.5 Chinese trigger word: {needle}")
    # v0.5.5 gates: Enhanced ablation table integrity
    for needle in ["Delta values", "final full configuration"]:
        if needle.lower() not in text.lower():
            fail(f"SKILL.md missing v0.5.5 ablation integrity requirement: {needle}")
    return text


def validate_templates(root: Path) -> None:
    templates = list((root / "templates").glob("*.md"))
    if len(templates) < 5:
        fail(f"Expected at least 5 template files, found {len(templates)}")
    for p in templates:
        t = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(root))
        if len(t.splitlines()) < 10:
            warn(f"Template may be too short: {rel}")
        if "fabricat" not in t.lower() and "missing" not in t.lower():
            fail(f"Template missing anti-fabrication/missing-info rule: {rel}")
        if "GB/T 7714" not in t:
            fail(f"Template missing GB/T 7714-2015 reference: {rel}")
    # Specific template checks
    ib = read_text(root, "templates/innovation-brief-template.md")
    require_contains(ib, "Innovation Quality Gate", "innovation-brief-template.md")
    require_contains(ib, "Anti-generic check" if "Anti-generic check" in ib else "anti-generic", "innovation-brief-template.md")
    ep = read_text(root, "templates/experiment-plan-template.md")
    require_contains(ep, "Reproducibility" if "Reproducibility" in ep else "reproducibility", "experiment-plan-template.md")
    require_contains(ep, "GPU OOM", "experiment-plan-template.md")
    require_contains(ep, "Loss divergence", "experiment-plan-template.md")
    mp = read_text(root, "templates/multi-paper-comparison-template.md")
    for needle in ["Strong Argument Construction", "Innovation Framework Recommendation",
                   "Paper Usage Decision", "Single-paper Extension", "Cross-paper Fusion",
                   "New Framework from Shared Gaps", "Paper Evidence Cards",
                   "Corpus Inventory", "Paper Tiering", "Evidence Maturity",
                   "Mechanism Compatibility Check", "Quality Audit"]:
        require_contains(mp, needle, "multi-paper-comparison-template.md")
    ib2 = read_text(root, "templates/innovation-brief-template.md")
    require_contains(ib2, "Framework Source Type", "innovation-brief-template.md")
    require_contains(ib2, "Claim Safety Check", "innovation-brief-template.md")
    require_contains(ib2, "Evidence Maturity", "innovation-brief-template.md")
    require_contains(ib2, "Mechanism Compatibility Check", "innovation-brief-template.md")
    sa = read_text(root, "templates/strong-argument-template.md")
    require_contains(sa, "Claim type", "strong-argument-template.md")
    require_contains(sa, "Cross-paper Reasoning", "strong-argument-template.md")
    require_contains(sa, "Evidence Maturity", "strong-argument-template.md")
    require_contains(sa, "cross-domain analogy", "strong-argument-template.md")
    pa = read_text(root, "templates/paper-analysis-template.md")
    for needle in ["Evidence Coverage", "Formula", "Figure", "Table", "OCR"]:
        require_contains(pa, needle, "paper-analysis-template.md")
    require_contains(pa, "Ablation Table Integrity Check", "paper-analysis-template.md")
    require_contains(pa, "Claim Safety Check", "paper-analysis-template.md")
    require_contains(pa, "Quality Audit", "paper-analysis-template.md")
    # v0.5.4 gates in templates
    require_contains(pa, "Bibliographic Verification", "paper-analysis-template.md")
    require_contains(pa, "Report Quality", "paper-analysis-template.md")
    require_contains(pa, "Paper Evidence Quality", "paper-analysis-template.md")
    ib3 = read_text(root, "templates/innovation-brief-template.md")
    require_contains(ib3, "paper-claimed SOTA", "innovation-brief-template.md")
    require_contains(ib3, "Report Quality", "innovation-brief-template.md")
    require_contains(ib3, "Paper Evidence Quality", "innovation-brief-template.md")
    # v0.5.5: innovation template must require evidence level, validation, compatibility
    require_contains(ib3, "Evidence level:", "innovation-brief-template.md")
    require_contains(ib3, "Required validation", "innovation-brief-template.md")
    require_contains(ib3, "Minimal viable experiment", "innovation-brief-template.md")
    # v0.5.5: paper analysis template must have enhanced ablation fields
    pa2 = read_text(root, "templates/paper-analysis-template.md")
    require_contains(pa2, "Fixed variables", "paper-analysis-template.md")
    require_contains(pa2, "Changed variable", "paper-analysis-template.md")
    require_contains(pa2, "Delta values recalculated", "paper-analysis-template.md")
    # v0.5.5: experiment plan template must have claim safety
    ep2 = read_text(root, "templates/experiment-plan-template.md")
    require_contains(ep2, "Claim Safety Check", "experiment-plan-template.md")
    mp2 = read_text(root, "templates/multi-paper-comparison-template.md")
    require_contains(mp2, "Report Quality", "multi-paper-comparison-template.md")
    require_contains(mp2, "Paper Evidence Quality", "multi-paper-comparison-template.md")
    require_contains(mp2, "Bibliographic verified", "multi-paper-comparison-template.md")
    sa2 = read_text(root, "templates/strong-argument-template.md")
    require_contains(sa2, "SOTA Classification", "strong-argument-template.md")
    require_contains(sa2, "Report Quality", "strong-argument-template.md")


def _validate_gbt_sections(gbt: str) -> None:
    """Check that GB/T 7714-2015 sections do not contain wrong document type identifiers."""
    import re
    # Split into sections by ## headers
    sections = re.split(r"(?m)^## ", gbt)
    for section in sections:
        # Journal [J] section
        if re.match(r"\d+\.\s*Journal|期刊论文", section):
            if "[M]" in section:
                fail("GB/T Journal [J] section must not contain [M] (monograph) examples.")
            if re.search(r"(?<!/)Conference|会议", section) and "[C]" in section:
                fail("GB/T Journal [J] section must not contain [C] (conference) examples.")
            if "[D]" in section:
                fail("GB/T Journal [J] section must not contain [D] (thesis) examples.")
        # Conference [C] section
        if re.match(r"\d+\.\s*Conference|会议论文", section):
            if "[M]" in section and "[C]" not in section:
                fail("GB/T Conference [C] section must contain [C] examples.")
        # Monograph [M] section
        if re.match(r"\d+\.\s*Monograph|Book|专著", section):
            if "[M]" not in section:
                fail("GB/T Monograph [M] section must contain [M] examples.")


def validate_references(root: Path) -> None:
    gbt = read_text(root, "references/gbt7714-2015-examples.md")
    for needle in ["[J]", "[C]", "[D]", "[M]", "[EB/OL]", "Missing metadata",
                   "not a substitute for the official GB/T 7714-2015 standard"]:
        require_contains(gbt, needle, "gbt7714-2015-examples.md")
    # Section-level type checking: ensure Journal [J] section does not contain [M], [C], [D]
    _validate_gbt_sections(gbt)
    cv = read_text(root, "references/cv-detection-addendum.md")
    for needle in ["YOLO", "Backbone", "Neck", "Head", "Assignment", "Loss", "Deployment"]:
        require_contains(cv, needle, "cv-detection-addendum.md")
    ingestion = read_text(root, "references/document-ingestion-pipeline.md")
    for needle in ["Implemented by current helper script", "Not implemented directly"]:
        require_contains(ingestion, needle, "document-ingestion-pipeline.md")
    gates = read_text(root, "references/idea-quality-gates.md")
    require_contains(gates, "at least 4", "idea-quality-gates.md")
    require_contains(gates, "Anti-generic" if "Anti-generic" in gates else "anti-generic", "idea-quality-gates.md")


def validate_readme(root: Path) -> None:
    text = read_text(root, "README.md")
    if "Tested with Claude 4.x" in text:
        fail("README contains unaudited claim: Tested with Claude 4.x")
    # Check for bare TODO (not in a Roadmap section)
    import re
    for m in re.finditer(r"(?m)^.*\bTODO\b.*$", text):
        line = m.group(0).strip()
        if line.startswith("#") or line.startswith("-") or line.startswith("*"):
            # Could be in a roadmap; allow if context is clear
            pass
        else:
            warn(f"README contains bare TODO: {line[:80]}")
    # v0.5.5: must have platform positioning
    if "Claude Skill vs Codex Adapter" not in text:
        fail("README missing 'Claude Skill vs Codex Adapter' section")


def validate_ci(root: Path) -> None:
    ci = read_text(root, ".github/workflows/validate.yml")
    require_contains(ci, "py_compile", "validate.yml")
    require_contains(ci, "pytest", "validate.yml")
    require_contains(ci, "package_skill.py", "validate.yml")
    require_contains(ci, "package_codex_adapter.py", "validate.yml")
    # v0.5.5: must explicitly validate both packages
    require_contains(ci, "Claude Skill", "validate.yml")
    require_contains(ci, "Codex Adapter", "validate.yml")
    require_contains(ci, "--release", "validate.yml")


def validate_gitignore(root: Path) -> None:
    gi = read_text(root, ".gitignore")
    for entry in [".claude/settings.local.json", "__pycache__", ".pytest_cache", ".git/"]:
        if entry not in gi:
            fail(f".gitignore missing required entry: {entry}")


def validate_codex_adapter(root: Path) -> None:
    """Validate the Codex adapter structure if codex/ directory exists."""
    codex_dir = root / "codex"
    if not codex_dir.exists():
        return  # Codex adapter is optional
    # Root AGENTS.md must exist (Codex auto-entry point)
    root_agents = root / "AGENTS.md"
    if not root_agents.exists():
        fail("Root AGENTS.md missing (Codex auto-entry point)")
    if root_agents.stat().st_size == 0:
        fail("Root AGENTS.md is empty")
    root_agents_text = root_agents.read_text(encoding="utf-8")
    if "codex/AGENTS.md" not in root_agents_text:
        fail("Root AGENTS.md must reference codex/AGENTS.md")
    # codex/AGENTS.md must exist
    agents = codex_dir / "AGENTS.md"
    if not agents.exists():
        fail("codex/AGENTS.md missing")
    if agents.stat().st_size == 0:
        fail("codex/AGENTS.md is empty")
    agents_text = agents.read_text(encoding="utf-8")
    if "SKILL.md" not in agents_text:
        fail("codex/AGENTS.md must reference SKILL.md")
    # codex/README.md must exist
    codex_readme = codex_dir / "README.md"
    if not codex_readme.exists():
        fail("codex/README.md missing")
    if codex_readme.stat().st_size == 0:
        fail("codex/README.md is empty")
    # prompts/ must have 4 files
    prompts_dir = codex_dir / "prompts"
    if not prompts_dir.exists():
        fail("codex/prompts/ directory missing")
    prompt_files = list(prompts_dir.glob("*.md"))
    if len(prompt_files) < 4:
        fail(f"codex/prompts/ must have at least 4 files, found {len(prompt_files)}")
    # validate-report-quality.md must exist
    if not (prompts_dir / "validate-report-quality.md").exists():
        fail("codex/prompts/validate-report-quality.md missing")
    # checklists/ must have 4 files
    checklists_dir = codex_dir / "checklists"
    if not checklists_dir.exists():
        fail("codex/checklists/ directory missing")
    checklist_files = list(checklists_dir.glob("*.md"))
    if len(checklist_files) < 4:
        fail(f"codex/checklists/ must have at least 4 files, found {len(checklist_files)}")
    # Each file must be non-empty
    for p in prompt_files + checklist_files:
        if p.stat().st_size == 0:
            fail(f"codex adapter file is empty: {p.relative_to(root)}")
    # v0.5.5: codex/AGENTS.md must have platform positioning
    agents_text2 = agents.read_text(encoding="utf-8")
    if "Platform Positioning" not in agents_text2:
        fail("codex/AGENTS.md missing Platform Positioning section")
    if "Codex Report Depth Requirement" not in agents_text2:
        fail("codex/AGENTS.md missing Codex Report Depth Requirement")
    # v0.5.5: codex/prompts/paper-analysis.md must have depth requirement
    pa_prompt = read_text(root, "codex/prompts/paper-analysis.md")
    if "Codex Report Depth Requirement" not in pa_prompt:
        fail("codex/prompts/paper-analysis.md missing Codex Report Depth Requirement")
    # v0.5.5: codex/prompts/innovation-mining.md must have depth requirement
    inno_prompt = read_text(root, "codex/prompts/innovation-mining.md")
    if "Innovation Point Depth Requirement" not in inno_prompt:
        fail("codex/prompts/innovation-mining.md missing Innovation Point Depth Requirement")
    # v0.5.5: codex/checklists/sota-claim-safety.md must have Chinese trigger words
    sota_cl = read_text(root, "codex/checklists/sota-claim-safety.md")
    for needle in ["首个", "首次", "完全兼容", "ONNX兼容性好"]:
        if needle not in sota_cl:
            fail(f"codex/checklists/sota-claim-safety.md missing Chinese trigger: {needle}")
    # v0.5.5: codex/checklists/quality-audit.md must have Chinese banned words
    qa_cl = read_text(root, "codex/checklists/quality-audit.md")
    if "Chinese banned words" not in qa_cl:
        fail("codex/checklists/quality-audit.md missing Chinese banned words check")


# ---------------------------------------------------------------------------
# Release mode
# ---------------------------------------------------------------------------

def validate_release(root: Path) -> None:
    """Check that the directory is clean for release packaging."""
    banned_found: list[str] = []
    for item in root.rglob("*"):
        rel = str(item.relative_to(root))
        parts = Path(rel).parts
        for ban in RELEASE_BANNED:
            if rel == ban or rel.startswith(ban + "/") or rel.startswith(ban + "\\"):
                banned_found.append(rel)
                break
        # Check for pyc
        if item.suffix == ".pyc":
            banned_found.append(rel)
        # Check for nested archives (any .zip or .skill not inside dist/)
        if item.suffix in (".zip", ".skill"):
            if "dist" not in parts:
                banned_found.append(rel)
    if banned_found:
        for f in banned_found[:20]:
            print(f"  BANNED in release: {f}", file=sys.stderr)
        if len(banned_found) > 20:
            print(f"  ... and {len(banned_found) - 20} more", file=sys.stderr)
        fail(f"Release check failed: {len(banned_found)} banned items found")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Paper Innovation Analyst Skill repository")
    parser.add_argument("root", nargs="?", default=".", help="Path to skill repository root")
    parser.add_argument("--release", action="store_true", help="Run release cleanliness checks")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        fail(f"Root path does not exist: {root}")
    if not root.is_dir():
        fail(f"Root path is not a directory: {root}")

    validate_required_files(root)
    validate_skill_md(root)
    validate_templates(root)
    validate_references(root)
    validate_readme(root)
    validate_ci(root)
    validate_gitignore(root)
    validate_codex_adapter(root)

    if args.release:
        validate_release(root)

    mode = "release" if args.release else "development"
    print(f"OK: skill repository validation passed ({mode} mode)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
