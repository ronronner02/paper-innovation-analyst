# Literature Synthesis Prompt

Use this prompt when the user provides multiple papers and wants synthesis, not N separate reports.

## Routing Rule

- 1 paper → deep analysis (see `codex/prompts/paper-analysis.md`)
- 2+ papers → literature synthesis (this prompt)

## Two-pass Workflow

### Pass 0: Corpus Inventory

Before any synthesis, build the inventory:

```
- Claimed paper count:
- Detected PDF/document count:
- Successfully parsed:
- Failed/unreadable:
- Duplicates:
- Out-of-domain papers:
- Missing files suspected:
- Proceed / stop decision:
```

If claimed count differs from detected, report mismatch explicitly.

### Pass 1: Evidence Cards

Each paper gets a minimum-quality evidence card (NOT a full report):

| Field | Content |
|---|---|
| Paper ID | |
| Title | |
| Domain fit | core / relevant / background / out-of-domain |
| Extraction confidence | high / medium / low |
| Method evidence | |
| Formula / architecture evidence | |
| Experiment evidence | |
| Limitation evidence | |
| Useful mechanism | |
| Role in synthesis | core evidence / mechanism source / contrastive evidence / background / excluded |
| Reason for use or exclusion | |

If only read at title/abstract level: `Evidence insufficient for mechanism-level synthesis.`

### Pass 2: Synthesis and Innovation

Only after completing Pass 0 and Pass 1:

1. Paper Tiering (A/B/C/Excluded)
2. Research clustering and method family map
3. Shared assumptions and common limitations
4. Strong argument construction (requires 2+ Tier A/B papers)
5. Innovation framework (Type A: single-paper extension, Type B: cross-paper fusion, Type C: new framework from shared gaps)

Use `templates/multi-paper-comparison-template.md`.

## Multi-paper Rules

- Multiple papers do NOT require multiple full reports
- A paper set should produce synthesis, not a pile of summaries
- The final framework may use all, some, or only one paper
- Do not force weakly related papers into the innovation
- Cross-domain papers: label as `cross-domain analogy` unless explicit mechanism mapping exists

## Bibliographic Verification

Every cited paper in the synthesis MUST be verified. See `codex/checklists/bibliographic-verification.md`.

## Quality Audit

The final report MUST include a Quality Audit that distinguishes:
- **Report quality**: did the report label missing evidence, mark unverified fields, classify claims correctly?
- **Paper evidence quality**: does the paper itself lack ablation, hardware details, deployment evidence?

See `codex/checklists/quality-audit.md` for the full checklist.
