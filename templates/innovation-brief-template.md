# Innovation Brief Template

Every innovation idea MUST pass the quality gates in `references/idea-quality-gates.md` before presentation. Ideas that fail must be rewritten or marked as `REJECTED`.

---

## 1. Paper Snapshot

- Title:
- Area:
- Core problem:
- Core method:
- Main evidence:
- Evidence coverage: (reference `templates/paper-analysis-template.md` Section 1A if extracted assets are available)
- Target dataset(s) and data characteristics:
- Reported model scale / FLOPs / latency / memory:
- Reported training and inference hardware:

## 2. Novelty Diagnosis

- What is genuinely new:
- What is incremental:
- What is mostly engineering integration:
- What evidence supports the novelty:
- What evidence is missing:
- Is the novelty tied to a specific architecture, dataset, metric, or deployment setting:

## 3. Limitation-to-Idea Map

| Limitation | Why it matters | Concrete affected component | Possible innovation direction | Evidence needed |
|---|---|---|---|---|
|  |  |  |  |  |

## 4. Innovation Quality Gate

Before presenting any idea, verify it satisfies at least 4 of 6 conditions:

- [ ] Names a concrete limitation from the paper
- [ ] Names the affected module/layer/objective/dataset
- [ ] Has a measurable metric
- [ ] Has a minimal viable experiment
- [ ] Has a baseline
- [ ] Has an expected compute/deployment impact

Ideas failing this gate must be rewritten or marked `REJECTED: insufficient specificity`.

### Anti-generic Check

The following expressions are BANNED unless accompanied by layer-level specification, formulas, experiments, and deployment cost:

- "add attention mechanism"
- "use a larger dataset"
- "improve feature fusion"
- "optimize the loss function"
- "make the model lightweight"
- "use transformer"
- "use multimodal information"
- "improve robustness"
- "enhance feature representation"
- "introduce prior knowledge"

If any appear without detail, rewrite to specify: which layer/pipeline stage, tensor/feature-map shape change, loss/assignment change, FLOPs/VRAM/latency impact, target dataset, and targeted pain point.

## 5. Innovation Points

### Idea 1: `<name>`

- **Framework Source Type** (select one):
  - Single-paper extension
  - Cross-paper fusion
  - New framework from shared gaps
  - Engineering deployment optimization
  - Dataset/evaluation protocol innovation
  - Loss/objective innovation
  - Architecture innovation
- Core idea:
- Motivation from the paper:
- Difference from original paper:
- **Source papers:** (list which papers contribute to this idea)
- **Directly used mechanisms:** (what is taken without modification)
- **Modified mechanisms:** (what is changed and how)
- **Newly proposed components:** (what is entirely new)
- **Why this is not a trivial combination:**
- **What must be experimentally verified:**
- Technical route (Must specify layer-level architecture changes, loss function modifications, and compatibility with specific datasets):
  - Affected module/layer/pipeline stage:
  - Expected tensor/data-flow change:
  - Loss/objective/assignment modification, if any:
  - Dataset-specific compatibility, e.g. object scale, density, occlusion, class imbalance, resolution, annotation noise:
  - For CV/detection: backbone/neck/head/FPN/PAN/feature-stride/postprocessing impact:
- **Cross-paper fusion compatibility check** (if applicable):
  - Module compatibility (input/output tensor shapes):
  - Loss/training strategy compatibility:
  - Compute/deployment cost:
  - Additional data or annotation needed:
- Anti-generic check: why this is not merely `add attention`, `use more data`, or `make the model larger`:
- Hardware/deployment impact:
  - Expected parameter/FLOPs/MACs change:
  - Expected VRAM/RAM and latency/FPS change:
  - Target deployment hardware:
  - Export/quantization/operator-support risks:
- Required data/code/resources:
- Minimal viable experiment:
- Full experiment:
- Baselines:
- Metrics:
- Expected contribution:
- Feasibility: 1-5
- Novelty: 1-5
- Risk: 1-5
- Difficulty: low / medium / high
- Best-fit output: course project / internship project / thesis direction / workshop paper / conference paper

Repeat for 3-7 ideas.

## 6. Recommended Priority

Rank the ideas by expected value for the user's goal.

| Rank | Idea | Why this priority | First action | Compute/deployment concern |
|---:|---|---|---|---|
| 1 |  |  |  |  |

## 7. References

Use GB/T 7714-2015 formatting. See `references/gbt7714-2015-examples.md`. Do not fabricate missing bibliographic fields.
