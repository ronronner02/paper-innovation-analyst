# Innovation Idea Quality Gates

Every innovation idea must pass these gates before being presented as a formal output.

---

## Gate 1: Minimum Information Requirement

An idea MUST satisfy at least 4 of the following 6 conditions. If it fails, rewrite it or mark as `REJECTED: insufficient specificity`.

1. **Names a concrete limitation from the paper** — not a generic weakness, but a specific finding, missing experiment, or unsupported claim.
2. **Names the affected module/layer/objective/dataset** — specifies which part of the pipeline changes.
3. **Has a measurable metric** — mAP, BLEU, F1, latency, VRAM, FPS, or other quantifiable outcome.
4. **Has a minimal viable experiment** — a concrete first test that can be run in hours to days.
5. **Has a baseline** — a specific prior method or ablation to compare against.
6. **Has an expected compute/deployment impact** — FLOPs, parameters, VRAM, latency, or export compatibility estimate.

---

## Gate 2: Anti-generic Check

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

If any of these appear without supporting detail, the idea MUST be rewritten to specify:

- Which layer, pipeline stage, or module is affected
- How the input/output tensor or feature map changes (shape, channels, resolution)
- Whether the loss function or assignment strategy changes
- Impact on FLOPs, parameters, VRAM, and inference latency
- Which specific dataset validates the idea (COCO val / VisDrone test-dev / DOTA test / etc.)
- Targeted pain point: small objects, occlusion, long-tail classes, dense prediction, remote-sensing tiling, etc.

---

## Gate 3: CV/Detection-specific Gate

For computer vision and object detection papers, apply `references/cv-detection-addendum.md` requirements. The idea must specify at least 3 items from the CV innovation checklist.

---

## Gate 4: Reproducibility Gate

Each idea should have a feasible path to reproducibility:
- Can the experiment be run on a single GPU (8-24 GB VRAM)?
- Is the required dataset publicly available?
- Is the baseline code available or reproducible?
- Can results be verified within a reasonable compute budget?

---

## Scoring Reference

### Feasibility (1-5)

| Score | Definition | Example |
|---|---|---|
| 5 | Quick prototype, PyTorch built-ins only, single GPU, hours | Replace CIoU loss with SIoU loss |
| 4 | Moderate effort, standard tools, single GPU, 1-2 days | Add BiFPN neck with pretrained backbone |
| 3 | Meaningful architecture change, single 8 GB GPU, 1-2 weeks | New attention module in detection head |
| 2 | Significant engineering, multi-GPU or large dataset needed | Full pipeline redesign with new backbone |
| 1 | Requires unavailable data, proprietary system, or extreme compute | Train foundation model from scratch |

### Novelty (1-5)

| Score | Definition | Example |
|---|---|---|
| 1 | Trivial change, direct replication | Change learning rate schedule |
| 2 | Minor extension, well-known technique | Add dropout to existing module |
| 3 | Meaningful recombination for specific setting | Apply DFL to VisDrone small objects |
| 4 | Strong thesis/conference candidate | New assignment strategy for dense remote-sensing |
| 5 | Paradigm shift applicable across subfields | New problem formulation or theoretical result |

### Risk (1-5)

| Score | Definition | Example |
|---|---|---|
| 1 | Well-understood, likely to work | Standard loss replacement |
| 2 | Some risk, manageable | New module with known failure modes |
| 3 | Moderate uncertainty | Novel architecture without prior validation |
| 4 | High chance of null result | Depends on unstable training dynamics |
| 5 | Very high uncertainty | Unpublished data or unsupported operators |
