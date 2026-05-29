# Table Identity Gate

Every experimental table summarized in the report MUST pass this gate.

## Required Fields

For each table referenced or summarized:

| Field | Description | Example |
|---|---|---|
| Table ID | As printed in the paper | Table 9 |
| Noise setting | Experimental condition | cross-framework noise / box noise / mixed noise / clean |
| Metric | What is measured | mAP@0.5 / PSNR / SSIM / FID |
| Dataset | Which dataset | COCO val / VisDrone test-dev / SIDD / DND |

## Rules

- Identify the Table ID exactly as printed in the paper. Do NOT renumber or relabel.
- Identify the noise setting from the table caption, header, or surrounding text. Do NOT merge or re-label settings.
- **Read the metric from the table caption.** If the caption says "We report mAP in this table", the metric is `mAP` — do NOT relabel as `AP@0.5` or `mAP@0.5` unless the caption explicitly states that.
  - Example: Table 1 caption says "We report mAP" → metric is `mAP`, NOT `AP@0.5`.
  - Example: Table 2 caption says "AP0.5 results" → metric is `AP@0.5`.
  - Do NOT infer metric from other tables or from convention. Each table's metric comes from its own caption.
- If a table reports "cross-framework box noise" results, do NOT write "mixed noise" — write exactly what the table says.
- If the table caption is ambiguous about metric or noise setting, mark: `ambiguous — caption does not specify`.
- If only selected rows are shown, add: `Selected rows only; omitted rows may affect interpretation.`

## Enforcement

- Reports that re-label table results MUST have `fail` on the Table Identity row in the Quality Audit.
- Reports that omit the Table ID MUST have `partial` or `fail` on the Table Identity row.
