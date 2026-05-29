# Codex Adapter

This directory contains the Codex CLI adapter for the paper-innovation-analyst Claude Skill.

## What is this?

The Codex Adapter provides Codex CLI with structured entry points to the full skill. It does NOT replace the Claude Skill — it coexists alongside it.

- `AGENTS.md` — compressed repo-level rules for Codex
- `prompts/` — task-specific prompt files (paper analysis, innovation mining, literature synthesis, report quality validation)
- `checklists/` — verification gates (bibliographic, table identity, SOTA claims, quality audit)

## How Codex uses this

1. Codex CLI reads the root `AGENTS.md` as the project entry point
2. Root `AGENTS.md` points to `codex/AGENTS.md` for Codex-specific rules
3. `codex/AGENTS.md` references `SKILL.md` for the full workflow
4. Task-specific rules live in `codex/prompts/`
5. Verification gates live in `codex/checklists/`

## Files

| File | Purpose |
|---|---|
| `AGENTS.md` | Compressed Codex entry rules |
| `prompts/paper-analysis.md` | Single-paper deep analysis |
| `prompts/innovation-mining.md` | Innovation point generation |
| `prompts/literature-synthesis.md` | Multi-paper synthesis |
| `prompts/validate-report-quality.md` | Report quality self-check |
| `checklists/bibliographic-verification.md` | Title/Authors/Year/Venue/DOI gate |
| `checklists/table-identity.md` | Table ID/noise/metric/dataset gate |
| `checklists/sota-claim-safety.md` | SOTA tripartite classification |
| `checklists/quality-audit.md` | Report vs paper evidence distinction |

## NOT a standalone package

This adapter requires the full Claude Skill (`SKILL.md`, `references/`, `templates/`, `scripts/`). It is not a self-contained distribution.
