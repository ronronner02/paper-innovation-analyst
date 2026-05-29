# Innovation Mining Prompt

Use this prompt when the user wants implementable innovation ideas from a paper.

## Prerequisites

Complete paper analysis first (see `codex/prompts/paper-analysis.md`).

## Phase 5: Innovation Point Generation

Transform limitations into testable ideas. Each idea MUST include:

- Name, core idea, motivation
- Difference from paper
- Technical route: layer/module changes, loss modifications, dataset compatibility, deployment impact
- Required resources, key experiments, baselines, metrics
- Target measurable outcome (labeled `hypothesis unless measured`)
- Feasibility score 1-5, Novelty score 1-5, Risk score 1-5
- Difficulty, best-fit output

**Important:** All concrete benefit estimates (metric improvement, latency reduction, VRAM savings, etc.) MUST be labeled `hypothesis unless measured`. Do NOT present estimated improvements as confirmed results.

Use `templates/innovation-brief-template.md` for the output format.

## Quality Gates

Every idea MUST pass the gates in `references/idea-quality-gates.md`:

- Gate 1: Minimum 4/6 conditions (concrete limitation, affected module, measurable metric, minimal experiment, baseline, compute impact)
- Gate 2: Anti-generic check (10 banned expressions)
- Gate 3: CV/detection-specific (if applicable)
- Gate 4: Reproducibility

## Phase 6: Experiment Design

Use `templates/experiment-plan-template.md`:

- Minimal viable experiment, full plan, ablation matrix
- Dataset protocol, metrics, failure criteria
- Compute estimate (VRAM/FLOPs/latency)
- Hardware/deployment constraints
- Milestones, risks, fallbacks

## SOTA Claim Safety

For any innovation idea making SOTA-type claims, classify as:

1. `paper-claimed SOTA` — the paper itself claims SOTA
2. `supported within evaluated baselines` — outperforms tested baselines only
3. `externally verified SOTA` — confirmed by independent external search

Without external search, do NOT write `externally verified SOTA`.

See `codex/checklists/sota-claim-safety.md` for the full gate.

## Innovation-Specific Rules

- "first / 首个 / 首次 / 第一个" is BANNED even when labeled speculative. Rewrite as: `potentially underexplored; requires literature search`
- Estimates MUST be labeled `Engineering hypothesis requiring validation`
- Single-paper reports MUST distinguish: paper fact, inference, engineering hypothesis, speculative research idea
- All "expected improvement / 预期提升" MUST be rewritten as `Hypothesized measurable outcome` or `Target measurable outcome to test`

## Innovation Point Depth Requirement

Each innovation point MUST NOT be a direction-only list. At minimum, include:

- Framework Source Type
- Core idea
- Source evidence
- Modified module
- Technical route (layer/module/objective changes)
- Tensor / feature flow compatibility
- Loss / objective change
- Dataset compatibility
- Hypothesized measurable outcome
- Required validation
- Compute / memory / deployment risk
- Minimal viable experiment
- Failure criteria
- Evidence level
- Claim Safety Check

Chinese trigger words are equally enforced: 首个, 首次, 第一个, 首次提出, 全新, 完全兼容, 实时, 零开销, ONNX兼容性好, 部署完全兼容, 单GPU 8GB+, VRAM 2-4GB, 4K <200ms.
