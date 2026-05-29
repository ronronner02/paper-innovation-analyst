#!/usr/bin/env python3
"""Packaging script for the Codex Adapter.

Generates a .zip archive containing the Codex Adapter (codex/) alongside
the full Claude Skill (SKILL.md, references/, templates/, scripts/, etc.).

This is NOT a replacement for package_skill.py — it produces a separate
archive for Codex CLI users.

Usage:
    python scripts/package_codex_adapter.py .
    python scripts/package_codex_adapter.py . --version v0.5.4-beta
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

DEFAULT_VERSION = "v0.5.5-beta"

EXCLUDE_DIRS = {
    ".git",
    ".pytest_cache",
    "__pycache__",
    ".mypy_cache",
    ".tox",
    ".eggs",
    ".venv",
    "venv",
    "env",
    "outputs",
    "dist",
    "build",
    "node_modules",
}

EXCLUDE_FILES = {
    ".DS_Store",
    ".env",
    ".env.local",
    "Thumbs.db",
    "desktop.ini",
}

EXCLUDE_SUFFIXES = {".pyc", ".pyo", ".class", ".o", ".so", ".dylib"}

BANNED_IN_ARCHIVE = [
    ".git/",
    ".pytest_cache/",
    "__pycache__/",
    ".claude/settings.local.json",
    ".DS_Store",
    ".env",
    ".venv/",
    "outputs/",
]


def should_exclude(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    parts = rel.parts
    for part in parts:
        if part in EXCLUDE_DIRS:
            return True
        if part in EXCLUDE_FILES:
            return True
        if any(part.endswith(s) for s in EXCLUDE_SUFFIXES):
            return True
    if parts == (".claude", "settings.local.json"):
        return True
    return False


def build_archive(root: Path, output: Path, arc_root: str) -> tuple[int, list[str]]:
    """Build a zip archive. Returns (file_count, warnings)."""
    warnings: list[str] = []
    count = 0
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if should_exclude(path, root):
                continue
            arcname = f"{arc_root}/{path.relative_to(root)}"
            zf.write(path, arcname)
            count += 1

    # Verify no banned content
    with zipfile.ZipFile(output, "r") as zf:
        for name in zf.namelist():
            for ban in BANNED_IN_ARCHIVE:
                if ban in name:
                    warnings.append(f"Banned item in archive: {name}")

    return count, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Package the Codex Adapter alongside the Claude Skill."
    )
    parser.add_argument("root", nargs="?", default=".", help="Path to repository root")
    parser.add_argument("--version", default=DEFAULT_VERSION, help="Version string")
    parser.add_argument("--dist", default="dist", help="Output directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"ERROR: Root path does not exist: {root}", file=sys.stderr)
        return 2
    if not (root / "SKILL.md").exists():
        print("ERROR: SKILL.md not found in root directory", file=sys.stderr)
        return 2
    if not (root / "codex").is_dir():
        print("ERROR: codex/ directory not found in root directory", file=sys.stderr)
        return 2

    dist = Path(args.dist).resolve()
    dist.mkdir(parents=True, exist_ok=True)
    arc_root = "paper-innovation-analyst"
    name_base = f"paper-innovation-analyst-codex-adapter-{args.version}"

    all_warnings: list[str] = []

    # Build .zip only (not .skill — this is not a Claude Skill package)
    zip_path = dist / f"{name_base}.zip"
    count_z, warns_z = build_archive(root, zip_path, arc_root)
    all_warnings.extend(warns_z)
    size_z = zip_path.stat().st_size / 1024
    print(f"OK: packaged {count_z} files into {zip_path} ({size_z:.1f} KB)")

    # Verify codex/ is in the archive
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = zf.namelist()
        codex_files = [n for n in names if "/codex/" in n]
        if not codex_files:
            all_warnings.append("No codex/ files found in archive")
        else:
            print(f"OK: {len(codex_files)} codex adapter files in archive")

    if all_warnings:
        for w in all_warnings:
            print(f"WARNING: {w}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
