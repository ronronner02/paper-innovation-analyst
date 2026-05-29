# Paper Innovation Analyst Skill

A Claude Skill for evidence-aware academic paper analysis: technical decomposition, novelty and limitation assessment, formula/figure/table-aware reading, implementable innovation points, experiment plans, and multi-paper synthesis.

**Status:** beta | **Version:** v0.5.5-beta | **License:** MIT

## Project Status

This repository has local validation and pytest coverage, but it has not yet been formally certified across all Claude products or complex PDF types.

Local checks:

```bash
python -m py_compile scripts/validate_skill.py scripts/extract_paper_assets.py scripts/package_skill.py
python scripts/validate_skill.py .
python -m pytest tests -q
python scripts/package_skill.py .
```

## Capability boundary

This Skill analyzes paper content provided by Claude's document-reading capabilities, uploaded PDFs, copied text, other available document-reading Skills, or the optional helper script `scripts/extract_paper_assets.py`.

It does not guarantee stable parsing of every complex PDF, scanned page, mathematical formula image, figure, chart, table, or supplementary package. If tables, figures, formulas, scanned PDFs, or complex layouts are unavailable or only partially readable, Claude must mark them as unavailable or uncertain rather than guessing.

Document parsing caveat: this Skill includes best-effort document asset extraction. It does not guarantee perfect parsing of complex PDFs, scanned pages, mathematical formula images, charts, tables, multi-column reading order, or supplementary packages.

Optional extraction support can be enabled with:

```bash
python scripts/extract_paper_assets.py path/to/paper.pdf --out outputs/paper_assets --ocr-mode auto
```

Optional Python dependencies are listed in `requirements-optional.txt`; OCR additionally requires a system Tesseract installation.

## What this Skill does

This Skill helps Claude perform a repeatable research-reading workflow:

1. Parse paper identity, problem, method, datasets, metrics, baselines, results, and evidence coverage.
2. Separate paper claims from Claude's inferences.
3. Evaluate actual novelty rather than only repeating the abstract.
4. Mine limitations and convert them into research opportunities.
5. Generate implementable innovation points with experiments, baselines, metrics, risks, and feasibility scores.
6. Compare multiple papers and synthesize cross-paper research directions.
7. When evidence is available, analyze formulas, framework diagrams, charts, tables, references, multi-column layout, OCR text, and supplementary material with uncertainty labels.

## Batch Literature Synthesis Caveat

Batch mode is designed for synthesis, not for deep full-paper analysis of every paper.

For large corpora, the Skill first builds an inventory and evidence cards. Innovation frameworks should only use papers with sufficient evidence. Weakly related or insufficiently parsed papers may be marked as background or excluded.

Batch-mode outputs are research planning drafts and require human verification before use in proposals, theses, or publications.

## Claude Skill vs Codex Adapter

### Claude Skill

- Entry point: `SKILL.md`
- Best for: deep single-paper analysis, literature synthesis, innovation mining, experiment design
- Output: more complete, more detailed, with full formula/table/figure expansion
- Must enforce: Evidence Safety, Claim Safety (including Chinese trigger words), Table Integrity, Quality Audit

### Codex Adapter

- Entry point: root `AGENTS.md` and `codex/AGENTS.md`
- Best for: repository-level maintenance, report review, template improvement, testing, PR workflows
- Can also generate reports, but must not over-compress
- Codex reports use `codex/prompts/` and `codex/checklists/`
- **Codex Adapter is a repository-level adapter, not a replacement for the Claude .skill package.**

### Shared Core Rules

Both platforms share:
- Evidence Strength and Claim Safety (including Chinese trigger words)
- Table Identity Gate
- Ablation Table Integrity
- Bibliographic Verification Gate
- SOTA Claim Classification
- Quality Audit (three-state: pass / partial / fail)
- GB/T 7714-2015 citation formatting
- Deployment Hypothesis labeling

## Single Paper vs Literature Set Behavior

**Single paper input:**
- Produces a paper-centered analysis.
- Focuses on this paper's method, evidence, limitations, and direct improvement opportunities.
- Innovation points are single-paper extensions.

**Multiple paper input:**
- Produces a synthesis and innovation report by default, NOT N separate full paper reports.
- Separate full reports are generated only when explicitly requested.
- Builds strong arguments, research positioning, and innovation frameworks from the paper set.
- May use all papers or only the most relevant subset depending on evidence strength, relevance, and mechanism compatibility.
- Innovation can be: single-paper extension, cross-paper fusion, or new framework from shared gaps.

**Summary:** One paper → single-paper deep analysis. Multiple papers → literature synthesis, strong argument construction, innovation framework recommendation.

## Repository layout

```text
paper-innovation-analyst/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── CLAUDE.md
├── .gitignore
├── requirements-optional.txt
├── LICENSE
├── codex/                              # Codex Adapter (optional)
│   ├── AGENTS.md
│   ├── prompts/
│   │   ├── paper-analysis.md
│   │   ├── innovation-mining.md
│   │   └── literature-synthesis.md
│   └── checklists/
│       ├── bibliographic-verification.md
│       ├── table-identity.md
│       ├── sota-claim-safety.md
│       └── quality-audit.md
├── references/
│   ├── review-rubric.md
│   ├── domain-addenda.md
│   ├── document-ingestion-pipeline.md
│   ├── cv-detection-addendum.md
│   ├── gbt7714-2015-examples.md
│   └── idea-quality-gates.md
├── templates/
│   ├── paper-analysis-template.md
│   ├── innovation-brief-template.md
│   ├── experiment-plan-template.md
│   ├── multi-paper-comparison-template.md
│   └── reviewer-report-template.md
├── examples/
│   └── example-prompts.md
├── scripts/
│   ├── validate_skill.py
│   ├── extract_paper_assets.py
│   └── package_skill.py
├── tests/
│   ├── fixtures/
│   ├── expected/
│   ├── test_validate_skill.py
│   ├── test_validator_release_mode.py
│   ├── test_packaging_cleanliness.py
│   ├── test_extract_paper_assets_smoke.py
│   └── test_codex_adapter.py
└── .github/
    └── workflows/
        └── validate.yml
```

## Installation for Claude Code

Expected to work with Claude products that support custom Skills, including Claude Code and Claude.ai custom Skills.

Copy this directory into one of these locations:

```bash
# Personal skill, available across projects
mkdir -p ~/.claude/skills
cp -r paper-innovation-analyst ~/.claude/skills/

# Project skill, available only in current repository
mkdir -p .claude/skills
cp -r paper-innovation-analyst .claude/skills/
```

Then invoke Claude with prompts such as:

```text
Use paper-innovation-analyst to analyze this paper and propose implementable innovation points.
```

## Installation for Claude.ai custom Skills

Use the packaging script for a clean release archive:

```bash
python scripts/package_skill.py .
# Output: dist/paper-innovation-analyst-v0.5.4-beta.skill
# Output: dist/paper-innovation-analyst-v0.5.4-beta.zip
```

Upload the `.skill` file through Claude's Skills settings if your Claude plan supports custom Skills.

## Repository-level Codex Adapter Usage

This repository includes an optional **Codex Adapter** (`codex/` directory) for use with OpenAI Codex CLI. The Codex Adapter is NOT a standalone `.skill` installation package — it is a lightweight layer that references the full Claude Skill.

### Structure

```
codex/
├── AGENTS.md                  # Short repo-level rules (references SKILL.md)
├── prompts/
│   ├── paper-analysis.md      # Single-paper deep analysis rules
│   ├── innovation-mining.md   # Innovation point generation rules
│   └── literature-synthesis.md # Multi-paper synthesis rules
└── checklists/
    ├── bibliographic-verification.md  # Title/Authors/Year/Venue/DOI gate
    ├── table-identity.md              # Table ID/noise/metric/dataset gate
    ├── sota-claim-safety.md           # SOTA tripartite classification
    └── quality-audit.md               # Report vs paper evidence distinction
```

### How it works

- Codex CLI reads `codex/AGENTS.md` as project instructions
- `AGENTS.md` references `SKILL.md` for the full 8-phase workflow
- `codex/prompts/` contains task-specific detailed rules
- `codex/checklists/` contains verification gates

### Usage

```bash
# Option A: Copy codex/ into your project alongside SKILL.md
cp -r codex/ /path/to/your/project/

# Option B: Use this repository directly with Codex CLI
codex
```

The Codex Adapter and Claude Skill coexist in the same repository. The Claude Skill (`SKILL.md`) is the primary instruction source; the Codex Adapter (`codex/`) provides Codex-specific entry points and verification checklists.

## Citation format

This Skill uses **GB/T 7714-2015** (Chinese national standard for bibliographic references) as the default citation format for generated reports and reference lists. If you need a different format (APA, IEEE, ACM, etc.), specify it in your prompt. See `references/gbt7714-2015-examples.md` for format examples.

Incomplete bibliographic fields are marked as missing rather than fabricated.

## Validate the Skill locally

```bash
python -m py_compile scripts/validate_skill.py scripts/extract_paper_assets.py scripts/package_skill.py
python scripts/validate_skill.py .
python -m pytest tests -q
python scripts/package_skill.py .
```

## License

MIT License. See `LICENSE`.

## Version History

See [CHANGELOG.md](CHANGELOG.md) for full version history.
