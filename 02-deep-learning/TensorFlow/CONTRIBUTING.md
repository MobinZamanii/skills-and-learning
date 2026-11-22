# Contributing

Contributions that improve clarity, correctness, reproducibility, and accessibility are welcome.

## Notebook standards

- Write all notebook Markdown, code comments, chart labels, README files, and documentation in English.
- Use `$...$` for inline mathematics and `$$...$$` for display mathematics in Markdown cells.
- Introduce the learning objective and relevant theory before implementation.
- Explain tensor shapes and expected input/output formats where they matter.
- Prefer deterministic random generators and set seeds for reproducible examples.
- Avoid data leakage: split before fitting preprocessing transformations and preserve the intended role of train, validation, calibration, and test data.
- Keep datasets small or generate them synthetically when a real download is not essential to the teaching objective.
- Label synthetic data clearly and do not imply biological or clinical validity.
- Include references to official documentation or primary sources for nontrivial methods.

## Before submitting changes

From the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/validate_notebooks.py
```

Then open the edited notebook in JupyterLab, restart the kernel, and run all cells from top to bottom in the target environment. Static syntax checks are not a substitute for runtime execution.

If a TensorFlow-dependent notebook was executed, update its `VALIDATION_REPORT.md` with the Python, TensorFlow, Keras, and platform versions, plus a clear description of what was actually executed.
