# Validation Report — Notebook 05

## Structural checks

- Notebook format: nbformat 4.5.
- Cell count: 78 total (42 Markdown, 36 code).
- All Markdown content and code comments are written in English.
- Mathematical expressions use `$...$` for inline notation and `$$...$$` for display notation.
- Python code cells parsed successfully: 36/36.

## Runtime checks

- NumPy, Pandas, Matplotlib, and scikit-learn are available in the build environment.
- Data generation, stratified splitting, train-only scaling, validation baselines, threshold selection, confusion-matrix metrics, ROC/PR utilities, and error-analysis logic passed a runtime smoke test. A scikit-learn logistic-regression model was used as a stand-in to exercise the downstream prediction/metric workflow; this does not validate TensorFlow execution.
- TensorFlow is not installed in the build environment. Therefore, Keras model construction, model fitting, Keras metric execution, and TensorFlow-dependent cells could not be executed end-to-end here.

## Important evaluation safeguards

- The scaler is fitted only on the training data.
- Class weights are calculated only from training labels.
- Threshold selection is based on validation predictions.
- Baselines are assessed on validation data during model development.
- The test partition is not evaluated until the decision threshold has been selected and fixed.
- Synthetic-data performance must not be interpreted as evidence of real-world or clinical performance.

## User-side verification

After installing the listed dependencies in the target environment, restart the Jupyter kernel and use **Run All**. Confirm that all TensorFlow/Keras cells complete and inspect the resulting learning curves and metrics.
