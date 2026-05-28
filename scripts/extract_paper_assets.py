#!/usr/bin/env python3
"""Best-effort academic paper asset extractor.

This helper script is optional. It extracts evidence artifacts for the
paper-innovation-analyst Skill without claiming perfect PDF/OCR/formula/table
parsing. Missing dependencies degrade gracefully and are reported in warnings.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

EXTRACTOR_VERSION = "v0.5.1-beta"


@dataclass
class PageRecord:
    page: int
    text_chars: int = 0
    native_text_path: str | None = None
    ocr_text_path: str | None = None
    block_count: int = 0
    image_count: int = 0
    table_count: int = 0
    ocr_attempted: bool = False
    ocr_available: bool = False
    ocr_confidence_mean: float | None = None
    ocr_confidence_min: float | None = None
    ocr_low_confidence: bool = False
    warnings: list[str] = field(default_factory=list)


def warn(warnings: list[str], message: str) -> None:
    warnings.append(message)
    print(f"WARNING: {message}", file=sys.stderr)


def try_import(name: str) -> Any | None:
    try:
        return __import__(name)
    except Exception:
        return None


def extract_with_pymupdf(
    pdf_path: Path, out_dir: Path, dpi: int, ocr_mode: str, ocr_threshold: int, warnings: list[str]
) -> tuple[list[PageRecord], list[dict[str, Any]]]:
    fitz = try_import("fitz")
    if fitz is None:
        warn(warnings, "PyMuPDF is not installed; native layout, images, and page rendering skipped.")
        return [], []

    try:
        doc = fitz.open(pdf_path)
    except Exception as exc:
        warn(warnings, f"PyMuPDF failed to open PDF (encrypted or corrupted?): {exc}")
        return [], []

    text_dir = out_dir / "text"
    image_dir = out_dir / "images"
    page_dir = out_dir / "pages"
    text_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)
    page_dir.mkdir(parents=True, exist_ok=True)

    page_records: list[PageRecord] = []
    equation_candidates: list[dict[str, Any]] = []
    tesseract_available = shutil.which("tesseract") is not None
    pytesseract = try_import("pytesseract") if ocr_mode != "none" else None
    pil_image = None
    if ocr_mode != "none":
        try:
            from PIL import Image as PILImage
            pil_image = PILImage
        except Exception:
            pil_image = None

    eq_patterns = [
        re.compile(r"\\(?:sum|frac|int|alpha|beta|gamma|lambda|mathcal|mathbf)"),
        re.compile(r"\b(?:loss|Loss|objective|softmax|argmax|IoU|Dice|KL|L_\w+)\b.*[=+\-*/]"),
        re.compile(r"(?:L|J|f|Q|K|V|P|R|E|H|S|W|b|mu|sigma|theta|epsilon|lambda|alpha|beta|gamma)_[\w{}]+\s*=\s*[^.]{5,}"),
    ]

    for idx, page in enumerate(doc, start=1):
        rec = PageRecord(page=idx)
        text = page.get_text("text") or ""
        rec.text_chars = len(text)
        rec.native_text_path = str((text_dir / f"page_{idx:04d}.txt").relative_to(out_dir))
        (text_dir / f"page_{idx:04d}.txt").write_text(text, encoding="utf-8")

        blocks = page.get_text("blocks") or []
        rec.block_count = len(blocks)
        block_rows = []
        for block in blocks:
            x0, y0, x1, y1, btext, block_no, block_type = block[:7]
            block_rows.append({"page": idx, "x0": x0, "y0": y0, "x1": x1, "y1": y1, "type": block_type, "text": btext})
        (text_dir / f"page_{idx:04d}_blocks.json").write_text(json.dumps(block_rows, ensure_ascii=False, indent=2), encoding="utf-8")

        for line_no, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if len(stripped) < 6 or len(stripped) > 260:
                continue
            if any(p.search(stripped) for p in eq_patterns):
                equation_candidates.append({"page": idx, "line": line_no, "text": stripped, "source": "native_text_candidate"})

        images = page.get_images(full=True)
        rec.image_count = len(images)
        for im_no, img in enumerate(images, start=1):
            xref = img[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n >= 5:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                img_path = image_dir / f"page_{idx:04d}_image_{im_no:03d}.png"
                pix.save(img_path)
            except Exception as exc:
                rec.warnings.append(f"failed to extract image {im_no}: {exc}")

        # OCR decision
        should_ocr = False
        if ocr_mode == "all":
            should_ocr = True
        elif ocr_mode == "auto" and rec.text_chars < ocr_threshold:
            should_ocr = True

        if should_ocr:
            rec.ocr_attempted = True
            if pytesseract is None or pil_image is None or not tesseract_available:
                rec.warnings.append("OCR requested but pytesseract/Pillow/system tesseract unavailable")
            else:
                try:
                    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), alpha=False)
                    page_img = page_dir / f"page_{idx:04d}.png"
                    pix.save(page_img)
                    img = pil_image.open(page_img)
                    # Try image_to_data for confidence
                    try:
                        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
                        confs = [int(c) for c in data["conf"] if str(c).strip() != "-1"]
                        if confs:
                            rec.ocr_confidence_mean = round(sum(confs) / len(confs), 1)
                            rec.ocr_confidence_min = float(min(confs))
                            rec.ocr_low_confidence = rec.ocr_confidence_mean < 60
                            ocr_text = " ".join(
                                data["text"][i] for i in range(len(data["text"])) if data["text"][i].strip()
                            )
                        else:
                            ocr_text = pytesseract.image_to_string(img)
                    except Exception:
                        ocr_text = pytesseract.image_to_string(img)
                    rec.ocr_available = True
                    rec.ocr_text_path = str((text_dir / f"page_{idx:04d}_ocr.txt").relative_to(out_dir))
                    (text_dir / f"page_{idx:04d}_ocr.txt").write_text(ocr_text, encoding="utf-8")
                except Exception as exc:
                    rec.warnings.append(f"OCR failed: {exc}")

        page_records.append(rec)

    return page_records, equation_candidates


def extract_tables_pdfplumber(pdf_path: Path, out_dir: Path, warnings: list[str]) -> list[dict[str, Any]]:
    pdfplumber = try_import("pdfplumber")
    if pdfplumber is None:
        warn(warnings, "pdfplumber is not installed; table extraction skipped.")
        return []

    table_dir = out_dir / "tables"
    table_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_idx, page in enumerate(pdf.pages, start=1):
                try:
                    tables = page.extract_tables() or []
                except Exception as exc:
                    warn(warnings, f"table extraction failed on page {page_idx}: {exc}")
                    continue
                for table_idx, table in enumerate(tables, start=1):
                    csv_path = table_dir / f"page_{page_idx:04d}_table_{table_idx:03d}.csv"
                    with csv_path.open("w", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        for row in table:
                            writer.writerow(["" if cell is None else cell for cell in row])
                    records.append({"page": page_idx, "table": table_idx, "path": str(csv_path.relative_to(out_dir)), "rows": len(table)})
    except Exception as exc:
        warn(warnings, f"pdfplumber failed to open PDF: {exc}")
    return records


def collect_references(out_dir: Path, ocr_mode: str) -> tuple[dict[str, Any], str]:
    """Extract reference candidates. Returns (result_dict, source_label)."""
    text_dir = out_dir / "text"

    # Try native text first
    pages = sorted(text_dir.glob("page_*.txt"))
    native_pages = [p for p in pages if "_blocks" not in p.name and "_ocr" not in p.name]
    joined_native = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in native_pages)
    match = re.search(r"(?is)\n\s*(references|bibliography|参考文献)\s*\n(?P<body>.+)$", joined_native)
    if match:
        body = match.group("body")[:50000]
        raw_items = re.split(r"\n\s*(?=\[?\d+\]?\s*[.\]])", body)
        items = [re.sub(r"\s+", " ", item).strip() for item in raw_items if len(item.strip()) > 20]
        if items:
            ref_path = out_dir / "references_candidates.txt"
            ref_path.write_text("\n\n".join(items), encoding="utf-8")
            return {"status": "candidate_extracted", "path": str(ref_path.relative_to(out_dir)), "items_count": len(items)}, "native_text"

    # Fallback to OCR text
    if ocr_mode != "none":
        ocr_pages = sorted(text_dir.glob("page_*_ocr.txt"))
        if ocr_pages:
            joined_ocr = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in ocr_pages)
            match = re.search(r"(?is)\n\s*(references|bibliography|参考文献)\s*\n(?P<body>.+)$", joined_ocr)
            if match:
                body = match.group("body")[:50000]
                raw_items = re.split(r"\n\s*(?=\[?\d+\]?\s*[.\]])", body)
                items = [re.sub(r"\s+", " ", item).strip() for item in raw_items if len(item.strip()) > 20]
                if items:
                    ref_path = out_dir / "references_candidates.txt"
                    ref_path.write_text("\n\n".join(items), encoding="utf-8")
                    return {"status": "candidate_extracted", "path": str(ref_path.relative_to(out_dir)), "items_count": len(items)}, "ocr_text"

    return {"status": "not_found", "items": []}, "unavailable"


def main() -> int:
    parser = argparse.ArgumentParser(description="Best-effort extraction of paper text, OCR, tables, images, equations, and references.")
    parser.add_argument("pdf", help="Path to a PDF file")
    parser.add_argument("--out", default="outputs/paper_assets", help="Output directory")
    parser.add_argument("--ocr", action="store_true", help="Enable OCR (equivalent to --ocr-mode auto)")
    parser.add_argument("--ocr-mode", choices=["auto", "all", "none"], default="none", help="OCR mode: none, auto (low-text pages), or all")
    parser.add_argument("--ocr-text-threshold", type=int, default=80, help="Character count threshold for auto OCR")
    parser.add_argument("--dpi", type=int, default=200, help="Render DPI for OCR page images")
    args = parser.parse_args()

    # --ocr overrides --ocr-mode
    if args.ocr:
        args.ocr_mode = "auto"

    pdf_path = Path(args.pdf).expanduser().resolve()
    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        return 2
    if not pdf_path.suffix.lower() == ".pdf":
        print(f"ERROR: Not a PDF file: {pdf_path}", file=sys.stderr)
        return 2

    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        warnings: list[str] = []

        # Detect capabilities
        fitz_ok = try_import("fitz") is not None
        pdfplumber_ok = try_import("pdfplumber") is not None
        tesseract_ok = shutil.which("tesseract") is not None
        pytesseract_ok = try_import("pytesseract") is not None
        ocr_capable = tesseract_ok and pytesseract_ok

        pages, eqs = extract_with_pymupdf(pdf_path, out_dir, args.dpi, args.ocr_mode, args.ocr_text_threshold, warnings)
        tables = extract_tables_pdfplumber(pdf_path, out_dir, warnings)
        refs, ref_source = collect_references(out_dir, args.ocr_mode)

        table_counts: dict[int, int] = {}
        for rec in tables:
            table_counts[rec["page"]] = table_counts.get(rec["page"], 0) + 1
        for p in pages:
            p.table_count = table_counts.get(p.page, 0)

        manifest: dict[str, Any] = {
            "input_file": str(pdf_path),
            "created_at": datetime.now(timezone.utc).isoformat(),
            "extractor_version": EXTRACTOR_VERSION,
            "capabilities": {
                "native_text": fitz_ok,
                "ocr": ocr_capable and args.ocr_mode != "none",
                "table_extraction": pdfplumber_ok,
                "image_extraction": fitz_ok,
                "equation_candidates": fitz_ok,
                "reference_candidates": True,
            },
            "warnings": warnings,
            "pages": [asdict(p) for p in pages],
            "tables": tables,
            "equation_candidates": eqs,
            "references": refs,
            "reference_source": ref_source,
            "disclaimer": "Best-effort extraction only; verify formulas, tables, figures, OCR text, and multi-column order before making strong claims.",
            "outputs": {
                "text_dir": str((out_dir / "text").relative_to(out_dir)) if (out_dir / "text").exists() else None,
                "image_dir": str((out_dir / "images").relative_to(out_dir)) if (out_dir / "images").exists() else None,
                "table_dir": str((out_dir / "tables").relative_to(out_dir)) if (out_dir / "tables").exists() else None,
                "page_dir": str((out_dir / "pages").relative_to(out_dir)) if (out_dir / "pages").exists() else None,
            },
        }
        (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"manifest": str(out_dir / "manifest.json"), "warnings": warnings}, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(f"ERROR: Extraction failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
