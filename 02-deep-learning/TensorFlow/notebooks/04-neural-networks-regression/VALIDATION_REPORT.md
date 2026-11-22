# Validation Report — Notebook 04

- Notebook schema: **passed** (`nbformat.validate`).
- Python syntax: **passed** across all 26 code cells (AST parsing).
- Markdown math checks: **passed**.
  - Inline dollar delimiters balanced.
  - Display math delimiters balanced.
  - No `\\(...\\)` or `\\[...\\]` math delimiters; equations use `$...$` and `$$...$$`.
- Authored notebook/package text: **English only**; no Persian/Arabic Unicode characters detected.
- Notebook cell IDs: unique.
- Synthetic dataset generation and train/validation/test splitting: **executed successfully**.
- Expected split sizes: 768 training, 192 validation, and 240 test observations.
- Scikit-learn mean and linear-regression baselines: **executed successfully**.
- TensorFlow installed in the build environment: **No**.

## Runtime limitation

TensorFlow is not installed in the build environment used to assemble this package. Therefore, TensorFlow-dependent cells (Keras model construction, training, callbacks, predictions, and Keras loss-function comparisons) were syntax-checked but could not be executed here. Run the notebook from top to bottom in the target TensorFlow environment to verify its numerical training results on that machine.

The notebook generates its own synthetic dataset and does not require external data downloads.
