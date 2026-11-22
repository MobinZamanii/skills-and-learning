# Notebook 05 — Neural Network Classification with TensorFlow

This notebook introduces binary classification with a multilayer perceptron (MLP). It covers sigmoid probabilities, logits, binary cross-entropy, class imbalance, stratified data splitting, Keras model training, decision-threshold selection, confusion-matrix metrics, ROC analysis, precision–recall analysis, and error inspection.

## Learning outcomes

- Explain binary labels, logits, probabilities, and decision thresholds.
- Match sigmoid outputs with `BinaryCrossentropy(from_logits=False)` and raw logits with `from_logits=True`.
- Build and train a binary MLP using TensorFlow/Keras.
- Interpret accuracy, precision, recall, specificity, F1-score, balanced accuracy, ROC-AUC, and average precision.
- Understand why accuracy alone may be misleading on imbalanced data.
- Select a decision threshold using validation data and preserve the test set for final evaluation.
- Compare an MLP with dummy and logistic-regression baselines.

## Contents

- `05_Neural_Network_Classification_with_TensorFlow.ipynb` — complete educational notebook.
- `requirements-notebook05.txt` — Python package dependencies.
- `VALIDATION_REPORT.md` — notebook structure and validation notes.

## Environment

Use a 64-bit Python environment supported by the installed TensorFlow release. Install packages with:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-notebook05.txt
```

Then launch Jupyter:

```bash
jupyter lab
```

Open the notebook and run all cells from top to bottom.

### Windows note

TensorFlow can be used on native Windows for CPU workflows. For supported NVIDIA GPU workflows with current TensorFlow releases, use WSL2. Check the official installation guide for current platform and Python compatibility:

- https://www.tensorflow.org/install/pip

## Dataset

The notebook generates a small imbalanced synthetic dataset at runtime using scikit-learn's `make_classification`. No external dataset download is required. The data are for education only and do not represent a real biological or medical population.

## Evaluation protocol

The notebook uses stratified training, validation, and test partitions. The feature scaler and class weights are fitted or calculated using training data only. Baseline comparisons and threshold selection use validation data. The test partition is not evaluated until the model and decision threshold have been fixed; it is then used for final evaluation only. Do not retune the threshold based on test results.

## Formula rendering

Mathematical expressions use standard Jupyter Markdown / MathJax delimiters: `$...$` for inline mathematics and `$$...$$` for display mathematics.
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook05.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
