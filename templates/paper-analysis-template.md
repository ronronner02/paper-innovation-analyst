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

## 12. Quality Self-Check

Before finalizing, verify:

- [ ] Every factual claim is tagged as `Paper states:` or `Inference:`
- [ ] No numeric results are invented; missing data marked as `not found in provided material`
- [ ] Contributions are classified by novelty type (problem / method / data / evaluation / systems / empirical)
- [ ] Limitations cover at least: dataset, evaluation, ablation, generalization, efficiency, reproducibility
- [ ] Hardware and deployment evidence is extracted or explicitly flagged as missing
- [ ] Training-scale and deployment-scale feasibility are assessed separately
- [ ] References use GB/T 7714-2015 format with no fabricated bibliographic fields
- [ ] Analysis is technically specific, not generic advice
