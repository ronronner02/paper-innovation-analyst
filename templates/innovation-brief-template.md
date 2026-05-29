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
- Target measurable outcome (hypothesis unless measured):
- Feasibility: 1-5
- Novelty: 1-5
- Risk: 1-5
- Difficulty: low / medium / high
- Best-fit output: course project / internship project / thesis direction / workshop paper / conference paper
- Evidence level:
- SOTA classification (select one):
  - paper-claimed SOTA — the paper itself claims SOTA
  - supported within evaluated baselines — outperforms tested baselines only
  - externally verified SOTA — confirmed by independent external search
  - not applicable — no SOTA-type claim made
- Unsupported strong claims removed or rewritten:
- Engineering assumptions:
- Required validation before claiming deployment readiness:
- Claim Safety Check (must pass before presentation):
  - No "first / 首个 / 首次 / 第一个" without literature search
  - No "ONNX/TensorRT compatible / ONNX兼容性好" without export test
  - No "real-time / 部署完全兼容 / edge-ready" without edge-device test
  - No specific VRAM/latency/FPS numbers without profiling
  - All engineering estimates labeled as `Engineering hypothesis requiring validation`
  - All "expected improvement / 预期提升" rewritten as `Hypothesized measurable outcome`

Repeat for 3-7 ideas.

## 6. Evidence Maturity

For each innovation idea, assess evidence maturity:

| Component | Source paper | Evidence type | Maturity |
|---|---|---|---|
| Problem motivation | | direct / inference / hypothesis | |
| Core mechanism | | direct / inference / hypothesis | |
| Fusion/extension design | | hypothesis / speculative | |
| Deployment claim | | measured / assumed / unknown | |
| Resource estimate | | measured / assumption / unknown | |

Rules:
- Cross-paper fusion must NOT just say "combine A and B"; must explain how mechanisms connect at tensor/feature/loss level.
- All deployment-related judgments must be labeled `measured` or `requires validation`.
- All exact resource estimates must be labeled `assumption` unless backed by profiling or paper evidence.

## 7. Mechanism Compatibility Check

For cross-paper fusion or multi-source innovation:

- Tensor shape compatibility:
- Feature domain compatibility:
- Loss/objective compatibility:
- Training conflict risk:
- Compute/FLOPs risk:
- Memory/VRAM risk:
- Deployment/operator risk:
- Dataset/protocol compatibility:
- Minimal integration test:

## 8. Claim Safety Check

| Claim | Evidence level | Required validation | Rewrite if unsafe |
|---|---|---|---|
|  |  |  |  |

Evidence levels:
1. `Directly supported by the paper`
2. `Supported by cited related work`
3. `Cross-paper inference`
4. `Engineering hypothesis requiring validation`
5. `Unsupported; remove or rewrite`

## 9. Quality Audit

### Report Quality

| Check | Status: pass / partial / fail | Evidence | Required fix |
|---|---|---|---|
| Each idea passes Innovation Quality Gate (4/6 conditions) |  |  |  |
| No unsupported first/SOTA/deployment-ready/real-time claims |  |  |  |
| SOTA claims classified (paper-claimed / supported within baselines / externally verified) |  |  |  |
| "first / 首个" not present even as speculative |  |  |  |
| Engineering claims labeled as assumptions unless measured |  |  |  |
| Cross-paper fusion includes mechanism compatibility check |  |  |  |
| Deployment claims include export validation or are flagged |  |  |  |
| References use GB/T 7714-2015 or missing metadata marked |  |  |  |
| No Chinese banned words (首个/首次/第一个/完全兼容/实时/零开销/ONNX兼容性好/单GPU 8GB+/VRAM 2-4GB/4K <200ms) |  |  |  |
| Each innovation includes: Evidence level, Required validation, Mechanism compatibility, Deployment risk, Minimal viable experiment, Failure criteria |  |  |  |

### Paper Evidence Quality

| Check | Status: pass / partial / fail | Evidence |
|---|---|---|
| Paper provides hardware details (GPU, VRAM, training time) |  |  |
| Paper provides inference latency/FPS on target device |  |  |
| Paper provides export/runtime validation (ONNX/TensorRT) |  |  |
| Paper provides ablation of each core component |  |  |

Do NOT default all checks to `pass`. A paper with no ONNX test is a paper evidence gap; a report that writes "ONNX compatible" without flagging it is a report quality failure.

## 10. Recommended Priority

Rank the ideas by expected value for the user's goal.

| Rank | Idea | Why this priority | First action | Compute/deployment concern |
|---:|---|---|---|---|
| 1 |  |  |  |  |

## 11. References

Use GB/T 7714-2015 formatting. See `references/gbt7714-2015-examples.md`. Do not fabricate missing bibliographic fields.
