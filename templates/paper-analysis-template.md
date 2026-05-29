# Paper Analysis Template

## 1. Bibliographic Information

- Title:
- Authors:
- Year:
- Venue:
- Paper type:
- URL/DOI/arXiv ID:

### Bibliographic Verification

| Field | Source in PDF | Status |
|---|---|---|
| Title | PDF header / reference list | verified / unverified |
| Authors | PDF header | verified / unverified |
| Year | Copyright year / conference date / DOI | verified / unverified |
| Venue | Header / DOI / reference list | verified / unverified |
| DOI | First-page header/footer, copyright notice, doi.org link | verified / unverified / not found |

Before writing "DOI not found", scan the PDF first-page header/footer for `doi.org/`, `DOI:`, `https://doi.org/`, or `10.xxxx/` patterns. If the DOI is visible, extract it. If any field cannot be verified from the provided material, mark as `unverified — not found in provided material`. Do NOT guess from memory.

## 1A. Evidence Coverage and Extraction Status

Use `references/document-ingestion-pipeline.md` when extracted assets are available.

| Evidence type | Status | Notes |
|---|---|---|
| Body text / layout blocks | available / partial / unavailable |  |
| OCR text for scanned pages | none / partial / available | confidence and pages |
| Tables | extracted / partial / unavailable | count, page, caption, structural uncertainty |
| Equations | text / OCR / figure-only / unavailable | exactness and page |
| Figures / framework diagrams | extracted / captions only / unavailable | figure number, page, visible modules |
| Charts / qualitative examples | extracted / partial / unavailable | what is observable |
| References | extracted / partial / unavailable | metadata completeness |
| Supplementary material | analyzed / partial / unavailable | source list |

Do not fabricate missing information. If formulas, tables, figures, or scanned pages are unavailable, mark them explicitly and avoid strong claims based on them.

## 1B. Formula, Figure, and Table Evidence

- Key formulas/objectives found:
  - Formula/equation ID:
  - Source: machine-readable text / OCR / figure-only / not found
  - Exact expression if available:
  - Role in method:
  - Uncertainty:
- Framework diagrams and visual architecture evidence:
  - Figure ID/page:
  - Visible modules:
  - Data flow/arrows:
  - Claimed innovation supported by figure:
  - Uncertainty:
- Important tables:
  - Table ID/page:
  - What the table measures:
  - Header/unit reliability:
  - Values used in analysis:
  - Uncertainty:

## 2. Problem and Motivation

- Research problem:
- Why the problem matters:
- Limitations of prior work claimed by the paper:
- Practical setting assumed by the paper:

## 3. Method Summary

- High-level pipeline:
- Architecture / algorithm:
- Key equations or objectives:
- Training procedure:
- Inference procedure:
- Implementation details found in the paper:

## 4. Dataset and Evaluation

- Dataset(s):
- Data characteristics:
- Split/protocol:
- Metrics:
- Baselines:
- Main quantitative results:
- Qualitative results:
- Ablations:

## 5. Hardware, Complexity, and Deployment Evidence

- Parameter count:
- FLOPs/MACs:
- Input size and batch size:
- Training hardware, time, and peak VRAM:
- Inference hardware, latency/FPS, RAM/VRAM, precision:
- Runtime/export path, e.g. PyTorch, ONNX, TensorRT, OpenVINO, CoreML, TFLite, vendor NPU SDK:
- Operator-support risks:
- Deployment target assumed or missing:
- Missing efficiency/deployment evidence:

## 6. Claimed Contributions

List each claimed contribution and the evidence provided.

| Claimed contribution | Evidence | Strength of evidence |
|---|---|---|
|  |  |  |

## 7. Actual Novelty Assessment

- Genuinely new aspects:
- Incremental aspects:
- Engineering integration aspects:
- Weak or unsupported novelty claims:

## 8. Limitations

- Dataset limitations:
- Evaluation limitations:
- Ablation limitations:
- Generalization limitations:
- Efficiency/deployment limitations:
- Reproducibility limitations:
- Safety/ethics limitations:

## 9. Research Opportunities

| Opportunity | Source limitation | Why it may be publishable | First experiment | Hardware/deployment risk |
|---|---|---|---|---|
|  |  |  |  |  |

## 10. Key Takeaway

One concise paragraph explaining what the user should remember and what to do next.

## 11. References

Use GB/T 7714-2015 formatting. See `references/gbt7714-2015-examples.md`. Do not fabricate missing bibliographic fields.

## 12. Ablation Table Integrity Check

For each ablation table summarized in the report:

- Table ID:
- Task / dataset / metric:
- Full table or selected rows:
- Fixed variables:
- Changed variable:
- Baseline:
- Alternative configurations:
- Final full configuration:
- Delta values recalculated from raw numbers:
- Omitted rows:
- Could omitted rows change interpretation? (pass / partial / fail)
- Baseline vs final configuration distinction:
- Claims supported by this table:
- Claims not supported by this table:
- Risk of overgeneralization:

If only selected rows are shown, add: `Selected rows only; omitted rows may affect interpretation.`

Rules:
- If a table changes only one variable, explicitly state what is fixed.
- Do NOT write final full configuration as if it were a single-module result.
- For kernel-size ablation tables, specify which branch is fixed and which is varied.
- Delta values MUST be recalculated from original table numbers.

## 13. Claim Safety Check

For any claim containing trigger words:

**English trigger words:** first, novel, SOTA, state-of-the-art, fully compatible, ONNX compatible, TensorRT compatible, deployment-ready, real-time, negligible FLOPs, zero overhead, specific VRAM, low latency, all tasks, all datasets, edge-ready, production-ready, 4K <200ms, INT8 1.5-2x, VRAM 2-4GB.

**Chinese trigger words:** 首个, 首次, 第一个, 首次提出, 全新, 完全兼容, 实时, 零开销, 可忽略, 单卡8GB, 8GB显存, 4K <200ms, VRAM 2-4GB, ONNX兼容性好, 部署完全兼容, 单GPU 8GB+.

**Rules:**
- Any claim containing these words MUST enter this check.
- "first / 首个 / 首次 / 第一个" without external literature search → rewrite as `potentially underexplored; requires literature search`.
- "ONNX/TensorRT compatible" without export test → rewrite as `requires export validation`.
- "edge-ready / real-time / deployment-ready / 部署完全兼容" without edge-device test → rewrite as `edge deployment requires profiling`.
- Specific VRAM, latency, FPS, 4K<200ms, INT8 1.5-2x values without profiling → label as `Engineering hypothesis requiring validation`.
- All engineering deployment estimates → label as `Engineering hypothesis requiring validation`.
- All "expected improvement / 预期提升" → rewrite as `Hypothesized measurable outcome` or `Target measurable outcome to test`.

| Claim | Evidence level | Required validation | Rewrite if unsafe |
|---|---|---|---|
|  |  |  |  |

Evidence levels:
1. `Directly supported by the paper`
2. `Supported by cited related work`
3. `Cross-paper inference`
4. `Engineering hypothesis requiring validation`
5. `Unsupported; remove or rewrite`

## 14. Quality Audit

### Report Quality

Did the report correctly label, verify, and flag issues?

| Check | Status: pass / partial / fail | Evidence | Required fix |
|---|---|---|---|
| Every factual claim tagged as Paper states / Inference |  |  |  |
| No numeric results invented |  |  |  |
| Bibliographic fields verified (Title/Authors/Year/Venue/DOI) |  |  |  |
| Table identity preserved (Table ID, noise setting, metric, dataset) |  |  |  |
| SOTA claims classified (paper-claimed / supported within baselines / externally verified) |  |  |  |
| "first / 首个" not present even as speculative |  |  |  |
| References use GB/T 7714-2015 or missing metadata marked |  |  |  |
| Ablation tables preserve critical rows |  |  |  |
| Engineering claims labeled as assumptions unless measured |  |  |  |
| Ablation table integrity: fixed/changed variables, final config, deltas recalculated |  |  |  |
| No Chinese banned words (首个/首次/第一个/完全兼容/实时/零开销/ONNX兼容性好/单GPU 8GB+/VRAM 2-4GB/4K <200ms) |  |  |  |
| Report version matches current version (v0.5.5-beta) |  |  |  |

### Paper Evidence Quality

Does the paper itself have gaps in evidence?

| Check | Status: pass / partial / fail | Evidence |
|---|---|---|
| Paper provides hardware details (GPU, VRAM, training time) |  |  |
| Paper provides inference latency/FPS on target device |  |  |
| Paper provides peak memory or model-size report |  |  |
| Paper provides export/runtime validation (ONNX/TensorRT) |  |  |
| Paper provides ablation of each core component |  |  |
| Contributions classified by novelty type |  |  |
| Limitations cover dataset/evaluation/ablation/generalization/efficiency/reproducibility |  |  |
| Training-scale and deployment-scale feasibility assessed separately |  |  |

Do NOT default all checks to `pass`. If missing metadata exists, reference check is `partial` at most. If ablation rows were omitted, ablation check is `partial` or `fail`. A paper with no ONNX test is a paper evidence gap; a report that writes "ONNX compatible" without flagging it is a report quality failure.
