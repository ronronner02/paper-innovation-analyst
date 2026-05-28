# Paper Analysis Template

## 1. Bibliographic Information

- Title:
- Authors:
- Year:
- Venue:
- Paper type:
- URL/DOI/arXiv ID:

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

- Table name:
- Full table used or selected rows only:
- Omitted rows:
- Could omitted rows change interpretation? (pass / partial / fail)
- Baseline vs final configuration distinction:
- Claims supported by this table:
- Claims not supported by this table:

If only selected rows are shown, add: `Selected rows only; omitted rows may affect interpretation.`

## 13. Claim Safety Check

For any claim containing trigger words (first / novel / SOTA / fully compatible / ONNX compatible / deployment-ready / real-time / negligible FLOPs / specific VRAM / low latency / all tasks / all datasets / edge-ready / production-ready):

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

| Check | Status: pass / partial / fail | Evidence | Required fix |
|---|---|---|---|
| Every factual claim tagged as Paper states / Inference |  |  |  |
| No numeric results invented |  |  |  |
| Contributions classified by novelty type |  |  |  |
| Limitations cover dataset/evaluation/ablation/generalization/efficiency/reproducibility |  |  |  |
| Hardware and deployment evidence extracted or flagged as missing |  |  |  |
| Training-scale and deployment-scale feasibility assessed separately |  |  |  |
| References use GB/T 7714-2015 or missing metadata marked |  |  |  |
| No unsupported first/SOTA/deployment-ready/real-time claims |  |  |  |
| Ablation tables preserve critical rows |  |  |  |
| Engineering claims labeled as assumptions unless measured |  |  |  |

Do NOT default all checks to `pass`. If missing metadata exists, reference check is `partial` at most. If ablation rows were omitted, ablation check is `partial` or `fail`.
