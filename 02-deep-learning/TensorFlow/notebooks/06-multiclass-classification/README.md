# Notebook 06 — Multiclass Classification and Model Evaluation

This notebook extends the TensorFlow learning track from binary to single-label multiclass classification. It explains softmax outputs, integer and one-hot targets, categorical cross-entropy, class imbalance, confusion matrices, multiclass averaging, ROC-AUC, average precision, and error analysis.

## Learning outcomes

- Distinguish binary, single-label multiclass, and multilabel classification.
- Use softmax outputs for mutually exclusive classes.
- Match sparse and one-hot labels with the appropriate categorical loss.
- Build and train multiclass MLP models with TensorFlow/Keras.
- Compare an unweighted model with a class-weighted model using validation data.
- Report per-class, micro, macro, and weighted metrics.
- Evaluate OvR ROC-AUC and average precision from probability scores.
- Preserve the test set for final model evaluation.

## Dataset

The notebook generates a synthetic three-class dataset with 14 numeric features and an intentionally imbalanced class distribution. The data are for education only; they do not represent clinical or biological measurements.

## Files

- `06_Multiclass_Classification_and_Model_Evaluation.ipynb` — complete educational notebook.
- `requirements-notebook06.txt` — Python dependencies.
- `VALIDATION_REPORT.md` — structural and code validation notes.

## Environment

The dependency file pins TensorFlow 2.21.0 and Keras 3.15.1, consistent with the stable release combination selected for this learning track on 2026-11-21. Use Python 3.11 or a compatible newer version. TensorFlow CPU execution is sufficient for this small synthetic example.

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-notebook06.txt
```

Start Jupyter:

```bash
jupyter lab
```

## Recommended execution order

Run the notebook from top to bottom. The scaler and class weights are fitted using training data only. The validation set is used for early stopping and model selection. The test set is held back for final evaluation.

## Important limitation

This notebook is a learning exercise, not a clinical or scientific model. Results on synthetic data do not establish external validity, calibration, or fitness for a real-world application.
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook06.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
