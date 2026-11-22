#!/usr/bin/env python3
"""Run structural, syntax, language, and Markdown-math checks on course notebooks."""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"
PERSIAN_ARABIC_RE = re.compile(r"[\u0600-\u06FF]")


def check_math(markdown: str) -> list[str]:
    issues: list[str] = []
    display_count = markdown.count("$$")
    if display_count % 2:
        issues.append("unbalanced display-math $$ delimiters")
    without_display = markdown.replace("$$", "")
    # Ignore escaped dollar signs.
    unescaped_dollars = re.findall(r"(?<!\\)\$", without_display)
    if len(unescaped_dollars) % 2:
        issues.append("unbalanced inline-math $ delimiters")
    if r"\(" in markdown or r"\[" in markdown:
        issues.append("found \\( or \\[ delimiters; use $...$ and $$...$$")
    return issues


def main() -> int:
    files = sorted(NOTEBOOK_DIR.rglob("*.ipynb"))
    if len(files) != 12:
        print(f"ERROR: expected 12 notebooks, found {len(files)}")
        return 1

    total_cells = total_code = 0
    failures: list[str] = []
    print("Deep Learning with TensorFlow — notebook validation")
    print("=" * 58)

    for path in files:
        rel = path.relative_to(ROOT)
        try:
            nb = nbformat.read(path, as_version=4)
            nbformat.validate(nb)
        except Exception as exc:
            failures.append(f"{rel}: nbformat validation failed: {exc}")
            continue

        code_cells = 0
        markdown_cells = 0
        cell_ids = [cell.get("id") for cell in nb.cells if cell.get("id")]
        if len(cell_ids) != len(nb.cells):
            failures.append(f"{rel}: one or more cells are missing IDs")
        if len(cell_ids) != len(set(cell_ids)):
            failures.append(f"{rel}: duplicate cell IDs")

        for idx, cell in enumerate(nb.cells):
            source = cell.get("source", "")
            if isinstance(source, list):
                source = "".join(source)
            if PERSIAN_ARABIC_RE.search(source):
                failures.append(f"{rel}: non-English-script text detected in cell {idx}")
            if cell.cell_type == "markdown":
                markdown_cells += 1
                for issue in check_math(source):
                    failures.append(f"{rel}: {issue} in Markdown cell {idx}")
            elif cell.cell_type == "code":
                code_cells += 1
                try:
                    ast.parse(source)
                except SyntaxError as exc:
                    failures.append(f"{rel}: Python syntax error in cell {idx}: {exc}")
                if cell.get("outputs"):
                    failures.append(f"{rel}: code outputs are not cleared in cell {idx}")

        total_cells += len(nb.cells)
        total_code += code_cells
        print(f"PASS  {rel}  ({len(nb.cells)} cells; {markdown_cells} Markdown; {code_cells} code)")

    print("=" * 58)
    if failures:
        print(f"FAILED: {len(failures)} issue(s)")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"PASS: {len(files)} notebooks, {total_cells} cells, {total_code} Python code cells")
    print("Checks: nbformat schema, unique cell IDs, Python syntax, math delimiters, English-script scan, cleared outputs")
    print("Note: these are static checks; they do not execute TensorFlow training cells.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
