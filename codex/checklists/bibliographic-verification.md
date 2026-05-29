# Bibliographic Verification Gate

Every cited paper MUST pass this gate before appearing in the final report.

## Required Fields

For each paper cited in the report:

| Field | Verification Method | Status |
|---|---|---|
| Title | Match against PDF header or reference list | verified / unverified |
| Authors | Match against PDF header | verified / unverified |
| Year | Match against copyright year, conference date, or DOI | verified / unverified |
| Venue | Match against header, DOI, or reference list | verified / unverified |
| DOI | Verify format (10.xxxx/...) and match if available | verified / unverified / not found |

## Rules

- **DOI extraction is mandatory.** Before writing "DOI not found", scan the PDF for:
  - First page header or footer: look for `doi.org/`, `DOI:`, `https://doi.org/`, or `10.xxxx/` patterns.
  - Copyright notice on first page: often contains the DOI.
  - Article metadata area (usually top or bottom of page 1).
  - If ANY of these locations contain a DOI, extract it and mark as `verified`. Do NOT write "DOI not found" if the DOI is visible in the PDF.
- If ANY field cannot be verified from the provided material, mark as `unverified — not found in provided material`.
- Do NOT guess year, venue, or DOI from memory or training data.
- Do NOT write "2025" for a paper whose PDF shows 2026, or vice versa.
- If the PDF header says Pattern Recognition 178 (2026) 113448, write exactly that.
- If the DOI is 10.1016/j.patcog.2026.113448, write exactly that.

## Example

**Wrong:** DN-TOD (2025, arXiv)
**Wrong:** DN-TOD, DOI not found
**Correct:** DN-TOD, Pattern Recognition 178 (2026) 113448, DOI 10.1016/j.patcog.2026.113448

The DOI `10.1016/j.patcog.2026.113448` is visible in the PDF footer/header. If the PDF contains it, extract it — do NOT write "not found".

## Enforcement

- Reports with unverified bibliographic fields MUST have `partial` or `fail` on the bibliographic verification row in the Quality Audit.
- Do NOT default bibliographic verification to `pass` if any field is unverified.
