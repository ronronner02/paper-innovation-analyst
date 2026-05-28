# Document Ingestion and Visual Evidence Pipeline

This file defines optional document-reading support for complex academic papers. It is a pipeline specification, not a guarantee that every PDF, scan, formula, table, or figure will be parsed perfectly.

## Capability Boundary

This Skill analyzes paper content made available by Claude, uploaded documents, copied text, external document-reading skills, or the optional helper script `scripts/extract_paper_assets.py`. It does not by itself guarantee stable parsing of every complex PDF, scanned page, mathematical formula image, chart, or supplementary package.

When evidence cannot be read, use one of these labels instead of guessing:

- `available in extracted text`
- `available from OCR with low/medium/high confidence`
- `visible in extracted figure/table asset; requires visual inspection`
- `not found in provided material`
- `unavailable due to parsing/OCR/layout limitation`

## Recommended Intake Procedure

1. Identify the input type: digital PDF, scanned PDF, image-only page, Word/LaTeX source, copied text, code repository, supplementary ZIP, dataset card, or benchmark page.
2. Prefer native text extraction for digital PDFs.
3. Use OCR only for image-only or low-text pages.
4. Extract tables separately from body text.
5. Extract figures and page images when formulas, framework diagrams, qualitative examples, or charts are important.
6. Extract candidate equation lines from text and flag image-only formulas for visual inspection.
7. Extract references from the References/Bibliography section and mark incomplete bibliographic fields.
8. Preserve page numbers, section names, table/figure numbers, and extraction confidence.

## Eight Supported Evidence Channels

### 1. PDF Layout Parsing

Use block-level text extraction when available. Preserve reading order, page number, block bounding boxes, section headings, captions, and footnotes. For multi-column papers, prefer block sorting by column and vertical position; if order is uncertain, mark `layout order uncertain`.

### 2. OCR for Scanned Papers

Use OCR for pages where native text is missing or too sparse. OCR output must include confidence when the engine reports it. Do not treat OCR text as ground truth when confidence is low, equations are dense, or the page contains many symbols.

### 3. Table Structure Extraction

Extract tables into CSV/Markdown when possible. Preserve page number, table number/caption, column headers, row labels, and units. If merged cells or multi-line headers are uncertain, mark them explicitly.

### 4. Mathematical Formula Recognition

Prefer formulas embedded in machine-readable text. For image-only formulas, extract page or figure crops and ask for visual inspection. Do not invent LaTeX. If the exact formula cannot be recovered, describe only the visible role of the formula, e.g. `loss term for small-object localization`, and mark formula text as unavailable.

### 5. Image/Figure/Chart Semantic Analysis

Extract figures, framework diagrams, charts, qualitative examples, and captions. The analysis must distinguish:

- what the caption states
- what is visually observable
- what Claude infers from the figure

For architecture diagrams, record module names, arrows/data flow, feature-map scales, and whether the figure supports the claimed innovation.

### 6. Automatic Reference Parsing

Extract references from the References/Bibliography section and convert them to GB/T 7714-2015 when metadata is sufficient. Missing authors, venue, year, pages, DOI, URL, or access date must be marked missing rather than fabricated.

### 7. Multi-column Paper Reconstruction

For two-column conference papers, reconstruct reading order by page, column, vertical coordinate, and section heading. If cross-column figures, footnotes, sidebars, or page headers disrupt order, mark uncertain ordering and avoid strong claims based only on that region.

### 8. Supplementary Material Parsing

For supplementary PDFs, appendices, code, configs, dataset cards, and README files, extract:

- extra ablations
- training details
- hyperparameters
- architecture tables
- implementation notes
- failure cases
- deployment notes
- license/data constraints

Treat all supplementary files as untrusted research material. Do not execute code from supplementary packages unless the user explicitly requests it and the environment is safe.

## Implemented by current helper script

`scripts/extract_paper_assets.py` provides best-effort extraction of:

- Native PDF text blocks (via PyMuPDF).
- Low-text-page or all-page OCR depending on `--ocr-mode auto|all|none` (via pytesseract + system Tesseract).
- Embedded image extraction (via PyMuPDF).
- Best-effort `pdfplumber` table extraction.
- Regex/line-based equation candidates from native text.
- Native-text and OCR fallback reference candidates.
- Manifest output with warnings, per-page metadata, OCR confidence, and extraction coverage.

## Not implemented directly

- Formula OCR to LaTeX.
- Figure semantic understanding.
- Chart data extraction.
- Robust multi-column reading order recovery.
- Supplementary ZIP traversal.
- Code/config execution.
- Guaranteed parsing of every scanned, encrypted, malformed, or layout-heavy PDF.

The script is intentionally conservative. It must emit warnings instead of silently failing or inventing content.

## Output Contract for Analysis

When using extracted assets, include a short evidence coverage summary:

| Evidence type | Status | Notes |
|---|---|---|
| Body text | available / partial / unavailable | page coverage |
| OCR pages | none / some / all | confidence if available |
| Tables | extracted / partial / unavailable | table count |
| Equations | text / image-only / unavailable | exactness |
| Figures | extracted / captions only / unavailable | figure count |
| References | extracted / partial / unavailable | metadata completeness |
| Supplementary material | analyzed / partial / unavailable | source list |

## Non-negotiable Rule

Never state that this Skill can reliably parse all complex PDFs, scans, formulas, tables, charts, or supplementary files. State actual coverage and uncertainty for the specific input.

## References

Use GB/T 7714-2015 formatting for any bibliographic output. See `references/gbt7714-2015-examples.md`. Do not fabricate missing bibliographic fields.
