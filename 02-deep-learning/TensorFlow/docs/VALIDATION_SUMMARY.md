# Repository Validation Summary

**Validation date:** 2026-11-21  
**Notebooks discovered:** 12  
**Static validation result:** PASS

## Checks run during repository assembly

The included `scripts/validate_notebooks.py` script was executed successfully against all twelve notebooks.

- Jupyter notebook schema validation with `nbformat`.
- Presence and uniqueness of every notebook cell ID.
- Python AST syntax parsing for every code cell.
- Balanced Markdown inline `$...$` and display `$$...$$` delimiters.
- Scan for Persian/Arabic Unicode script in notebook cells.
- Verification that code-cell outputs are cleared for clean first runs.

The run covered all 12 notebooks, **891 cells**, and **389 Python code cells**.

## Runtime validation scope

This repository build does not claim that all TensorFlow/Keras cells were executed end-to-end. The chapter-specific `VALIDATION_REPORT.md` files describe which non-TensorFlow checks or smoke tests were run for individual chapters and explicitly identify TensorFlow-dependent sections that remained unexecuted in the assembly environment.

Before using or publishing model results, install the root `requirements.txt`, execute each notebook from top to bottom, and update the relevant validation report with the actual runtime environment and results.

## Canonical dependency environment

The integrated repository uses one shared dependency stack to avoid conflicting chapter-level pins:

- TensorFlow 2.21.0
- Keras 3.15.1
- Python 3.11 as the reference environment

The root `requirements.txt` is canonical. Each chapter-level `requirements-notebookXX.txt` mirrors the same package versions for standalone chapter installation. These are dependency targets, not a claim that the full course was executed in this build environment. Consult the official TensorFlow installation guide for platform-specific support and updates.
