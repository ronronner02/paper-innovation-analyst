# Paper Analysis Prompt

Use this prompt when the user wants a deep single-paper analysis.

## Phase 1: Intake and Scope

Identify: objective (summary / analysis / innovation / review / reproduction) and material (PDF / abstract / code / supplementary / extracted assets). If incomplete, continue and state the limitation.

## Phase 2: Paper Decomposition

Extract all of the following. Use `templates/paper-analysis-template.md`.

- Title, authors, year/venue, research area, task
- Motivation, contribution claims, method overview
- Architecture/pipeline, key equations (machine-readable / OCR / figure-only)
- Framework diagrams, figures, charts, captions
- Tables with header/unit reliability assessment
- Training/inference procedure, datasets, metrics
- Model scale: parameters, FLOPs, hardware, VRAM, latency
- Baselines, results, ablations
- Stated limitations, assumptions
- Reference-section extraction status, supplementary coverage

## Phase 3: Contribution and Novelty

Classify each contribution as: problem / method / data / evaluation / systems / empirical novelty.

For each: what is new, what it compares against, evidence strength, incremental vs substantial.

## Phase 4: Limitation Mining

Analyze from: dataset, evaluation, ablation, generalization, efficiency, theory, reproducibility, safety/ethics.

For DL papers: separate training-scale feasibility from deployment-scale feasibility.

Checklists:
- `references/review-rubric.md` — 12-dimension review
- `references/cv-detection-addendum.md` — for CV/detection papers
- `references/domain-addenda.md` — for domain-specific angles

## Bibliographic Verification

Before writing the report, verify every cited paper:
- Title: match against PDF header or reference list
- Authors: match against PDF header
- Year: match against copyright year, conference date, or DOI
- Venue: match against header, DOI, or reference list
- DOI: verify format and match if available

Mark any unverified field as `unverified — not found in provided material`.

See `codex/checklists/bibliographic-verification.md` for the full gate.

## Table Identity

For every experimental table:
- Identify the Table ID as printed in the paper
- Identify noise setting, metric, dataset from the table caption or header
- Do NOT re-label or merge table results

See `codex/checklists/table-identity.md` for the full gate.

## Codex Report Depth Requirement

When generating a single-paper report, the output MUST NOT be a shallow abstract-level summary. At minimum, include:

1. Bibliographic Verification
2. Evidence Coverage
3. Formula / Figure / Table Evidence
4. Method Decomposition
5. Dataset and Evaluation
6. Key Quantitative Results
7. Hardware / Deployment Evidence
8. Contribution and Novelty Assessment
9. Limitations
10. Research Opportunities
11. Innovation Proposals (if requested)
12. Minimal Viable Experiment (if innovation requested)
13. Claim Safety Check
14. Ablation Table Integrity Check
15. Quality Audit

If the user explicitly requests "brief summary" or "short overview", compression is allowed. Otherwise, maintain medium-to-full depth.

## Claim Safety

Any claim containing trigger words (first / 首个 / 首次 / novel / SOTA / ONNX compatible / real-time / 部署完全兼容 / specific VRAM / 4K <200ms) MUST pass the Claim Safety Check in `codex/checklists/sota-claim-safety.md`.

Chinese trigger words are equally enforced: 首个, 首次, 第一个, 首次提出, 全新, 完全兼容, 实时, 零开销, ONNX兼容性好, 部署完全兼容, 单GPU 8GB+, VRAM 2-4GB, 4K <200ms.
