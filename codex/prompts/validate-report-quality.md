# Validate Report Quality Prompt

Use this prompt as a final self-check before delivering any report. Apply it AFTER the report is drafted.

## Step 1: Bibliographic Verification

For every cited paper in the report, verify against the provided material:

| Field | Check |
|---|---|
| Title | Matches PDF header or reference list? |
| Authors | Matches PDF header? |
| Year | Matches copyright year, conference date, or DOI? |
| Venue | Matches header, DOI, or reference list? |
| DOI | Format correct (10.xxxx/...)? Matches if available? |

- Mark any unverified field as `unverified — not found in provided material`.
- Do NOT guess from memory.

## Step 2: Table Identity Check

For every experimental table summarized:

| Field | Check |
|---|---|
| Table ID | Exactly as printed in the paper? |
| Noise setting | Matches caption/header? Not re-labeled? |
| Metric | Matches what the table measures? |
| Dataset | Matches which dataset? |

- If only selected rows shown: add `Selected rows only; omitted rows may affect interpretation.`

## Step 3: SOTA Claim Check

Scan the report for SOTA-type trigger words:

**English:** first, novel, SOTA, state-of-the-art, deployment-ready, real-time, ONNX compatible, TensorRT compatible, fully compatible, negligible FLOPs, zero overhead, specific VRAM, 4K <200ms, INT8 1.5-2x, VRAM 2-4GB.

**Chinese:** 首个, 首次, 第一个, 首次提出, 全新, 完全兼容, 实时, 零开销, ONNX兼容性好, 部署完全兼容, 单GPU 8GB+, VRAM 2-4GB, 4K <200ms, 8GB显存, 单卡8GB.

For each:
- Classified as `paper-claimed SOTA` / `supported within evaluated baselines` / `externally verified SOTA`?
- If `externally verified`: was an actual external search performed?
- "first / 首个 / 首次 / 第一个" present? → MUST be rewritten as `potentially underexplored; requires literature search`
- Specific VRAM/latency/FPS numbers without profiling? → MUST be labeled `Engineering hypothesis requiring validation`
- "ONNX/TensorRT compatible" without export test? → MUST be rewritten as `requires export validation`

## Step 4: Evidence Level Check

For every strong claim:
- Has an evidence level (1-5)?
- Engineering claims labeled as `Engineering hypothesis requiring validation`?
- Deployment claims without paper evidence flagged?

## Step 5: Quality Audit Completeness

Verify the report includes a Quality Audit with TWO sections:

1. **Report Quality** — did the report correctly label, verify, and flag?
2. **Paper Evidence Quality** — does the paper itself have gaps?

- No check defaulted to `pass` without evidence.
- Bibliographic verification: `partial` if any field unverified.
- Table identity: `fail` if results re-labeled.

## Step 6: Anti-fabrication Scan

- Any invented results, citations, or venues?
- Any numeric values not traceable to the provided material?
- Any missing fields marked as `not found` rather than guessed?

## Output

If any step fails, fix the report before delivery. State what was fixed.
