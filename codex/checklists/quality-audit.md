# Quality Audit Checklist

Every report MUST include a Quality Audit that distinguishes **report quality** from **paper evidence quality**.

## Two-Distinction Principle

- **Report quality**: Did the *report* correctly label, verify, and flag issues?
- **Paper evidence quality**: Does the *paper itself* have gaps in evidence?

Do NOT confuse these. A paper with no ONNX test is a paper evidence gap. A report that writes "ONNX compatible" without flagging it is a report quality failure.

## Report Quality Audit

| Check | Status: pass / partial / fail | Evidence |
|---|---|---|
| Every factual claim tagged as Paper states / Inference | | |
| Bibliographic fields verified (Title/Authors/Year/Venue/DOI) | | |
| Table identity preserved (Table ID, noise setting, metric, dataset) | | |
| SOTA claims classified (paper-claimed / supported within baselines / externally verified) | | |
| "first / 首个" not present even as speculative | | |
| Engineering claims labeled as assumptions unless measured | | |
| No unsupported ONNX/TensorRT/edge/deployment claims | | |
| References use GB/T 7714-2015 or missing metadata marked | | |
| Ablation tables preserve critical rows | | |
| Cross-domain papers labeled as analogy, not direct evidence | | |
| No Chinese banned words (首个/首次/第一个/完全兼容/实时/零开销/ONNX兼容性好/单GPU 8GB+/VRAM 2-4GB/4K <200ms) | | |
| Ablation table integrity: fixed/changed variables, final config, deltas recalculated | | |
| Report version matches current version (v0.5.5-beta) | | |

## Paper Evidence Quality Audit

| Check | Status: pass / partial / fail | Evidence |
|---|---|---|
| Paper provides hardware details (GPU model, VRAM, training time) | | |
| Paper provides inference latency/FPS on target device | | |
| Paper provides peak memory or model-size report | | |
| Paper provides export/runtime validation (ONNX/TensorRT/etc.) | | |
| Paper provides ablation of efficient module vs accuracy | | |
| Paper provides comparison under matched compute budgets | | |
| Paper provides dataset splits and evaluation protocol | | |
| Paper provides ablation of each core component | | |

## Rules

- Do NOT default all checks to `pass`.
- If missing metadata exists, reference check is `partial` at most.
- If ablation rows were omitted, ablation check is `partial` or `fail`.
- If the paper itself lacks hardware evidence, mark the Paper Evidence row as `partial` or `fail` — this is NOT a report failure.
- If the report fails to flag the missing hardware evidence, mark the Report Quality row as `partial` or `fail`.
