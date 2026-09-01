# Paper Innovation Analyst

A Claude Skill that turns academic papers into structured research understanding and implementable innovation points — with every claim tagged by evidence strength, so the analysis never quietly upgrades a guess into a finding.

**Status:** beta · **Version:** v0.5.5-beta · **License:** MIT

It reads a paper the way a careful reviewer does: separating what the paper actually claims from what you might infer, marking formulas, tables, and figures it could not parse as unavailable rather than guessing, and refusing to fabricate a bibliographic field it cannot verify.

## Features

- **Structured paper decomposition** — identity, problem, method, datasets, metrics, baselines, results, and evidence coverage.
- **Claim/inference separation** — paper claims stay distinct from the model's own reasoning.
- **Real novelty assessment** — evaluates what is actually new instead of restating the abstract.
- **Limitation mining** — converts weaknesses into concrete research opportunities.
- **Implementable innovation points** — each with experiments, baselines, metrics, risks, and a feasibility score.
- **Multi-paper synthesis** — cross-paper research directions, positioning, and innovation frameworks.
- **Evidence-aware asset reading** — formulas, framework diagrams, charts, tables, references, multi-column layout, OCR text, and supplementary material, each with an uncertainty label.
- **Safety gates** — Evidence Strength, Claim Safety (including Chinese trigger words), Table Identity, Ablation Table Integrity, Bibliographic Verification, SOTA Claim Classification, and a three-state Quality Audit (pass / partial / fail).
- **GB/T 7714-2015 citations** by default, with incomplete fields marked missing rather than invented.
- **Optional Codex Adapter** for repository-level maintenance, report review, and PR workflows.

## How it works

```text
paper input (PDF / text / extracted assets)
  -> identity + problem + method parsing
  -> evidence coverage assessment      [unavailable assets marked, not guessed]
  -> claim / inference separation
  -> novelty + limitation analysis
  -> innovation point generation       [experiments, baselines, metrics, risks, feasibility]
  -> safety gates                      [evidence · claim · table · bibliographic · SOTA]
  -> quality audit                     [pass / partial / fail]
  -> report
```

Behavior depends on how many papers you supply:

| Input | Output |
| --- | --- |
| One paper | Paper-centered deep analysis; innovation points are single-paper extensions |
| Multiple papers | Literature synthesis and innovation framework by default — **not** N separate full reports |

For multiple papers the Skill first builds an inventory and evidence cards, then uses only papers with sufficient evidence. Weakly related or poorly parsed papers are marked as background or excluded. Separate full reports are produced only on explicit request.

## Quick start

### Install for Claude Code

```bash
# Personal skill — available across all projects
mkdir -p ~/.claude/skills
cp -r paper-innovation-analyst ~/.claude/skills/

# Project skill — available only in the current repository
mkdir -p .claude/skills
cp -r paper-innovation-analyst .claude/skills/
```

Then invoke it in a prompt:

```text
Use paper-innovation-analyst to analyze this paper and propose implementable innovation points.
```

### Install for Claude.ai custom Skills

Build a clean release archive, then upload the `.skill` file through Claude's Skills settings:

```bash
python scripts/package_skill.py .
# -> dist/paper-innovation-analyst-v0.5.5-beta.skill
# -> dist/paper-innovation-analyst-v0.5.5-beta.zip
```

Works with Claude products that support custom Skills, including Claude Code and Claude.ai.

### Optional: local PDF asset extraction

The Skill reads papers supplied through Claude's own document handling, uploaded PDFs, pasted text, or other document-reading Skills. When you want local extraction instead:

```bash
pip install -r requirements-optional.txt   # OCR also needs a system Tesseract install
python scripts/extract_paper_assets.py path/to/paper.pdf --out outputs/paper_assets --ocr-mode auto
```

### Validate the Skill locally

```bash
python -m py_compile scripts/validate_skill.py scripts/extract_paper_assets.py scripts/package_skill.py
python scripts/validate_skill.py .
python -m pytest tests -q
python scripts/package_skill.py .
```

## Repository layout

```text
paper-innovation-analyst/
├── SKILL.md                    # Primary instruction source: the 8-phase workflow
├── CHANGELOG.md
├── CLAUDE.md
├── requirements-optional.txt   # Optional deps for local PDF extraction
├── references/                 # Rules the Skill consults while analyzing
│   ├── review-rubric.md
│   ├── domain-addenda.md
│   ├── document-ingestion-pipeline.md
│   ├── cv-detection-addendum.md
│   ├── gbt7714-2015-examples.md
│   └── idea-quality-gates.md
├── templates/                  # Output shapes the Skill fills in
│   ├── paper-analysis-template.md
│   ├── innovation-brief-template.md
│   ├── experiment-plan-template.md
│   ├── multi-paper-comparison-template.md
│   └── reviewer-report-template.md
├── examples/example-prompts.md
├── scripts/                    # Validation, extraction, packaging
├── tests/
├── codex/                      # Optional Codex Adapter (see below)
└── .github/workflows/validate.yml
```

`references/` and `templates/` carry the two halves of the Skill's behavior: `references/` holds the rules and gates applied while reading a paper, `templates/` holds the report structures those rules produce. `SKILL.md` is the entry point that ties them together.

## Codex Adapter (optional)

A lightweight repository-level layer for the OpenAI Codex CLI, in `codex/`. It is **not** a standalone `.skill` package — it references the full Claude Skill.

| | Claude Skill | Codex Adapter |
| --- | --- | --- |
| Entry point | `SKILL.md` | `AGENTS.md` and `codex/AGENTS.md` |
| Best for | Deep single-paper analysis, synthesis, innovation mining, experiment design | Repository maintenance, report review, template improvement, testing, PR workflows |
| Output | Full detail, complete formula/table/figure expansion | Reports too, but must not over-compress |

```bash
# Option A: copy the adapter into your own project alongside SKILL.md
cp -r codex/ /path/to/your/project/

# Option B: use this repository directly
codex
```

Codex CLI reads `codex/AGENTS.md` as project instructions, which references `SKILL.md` for the full workflow. `codex/prompts/` holds task-specific rules; `codex/checklists/` holds the verification gates. Both platforms share the same core safety rules listed under Features.

## Limitations

- **Not certified across every Claude product or PDF type.** The repository has local validation and pytest coverage; it has not been formally certified beyond that.
- **Complex documents may parse partially.** Scanned pages, formula images, charts, tables, multi-column reading order, and supplementary packages are best-effort. Anything unreadable is marked unavailable or uncertain — never guessed.
- **Batch mode is for synthesis, not depth.** Batch outputs are research planning drafts and need human verification before use in proposals, theses, or publications.

## License

MIT — see [LICENSE](LICENSE).

Version history: [CHANGELOG.md](CHANGELOG.md).
