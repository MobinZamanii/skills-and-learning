# Notebook 04 — Artificial Neural Networks and Regression with TensorFlow

This notebook introduces supervised regression with multilayer perceptrons (MLPs). It covers dataset creation, leakage-aware data splitting, feature normalization, network architecture, regression losses, Keras training, model evaluation, and residual diagnostics.

## Learning outcomes

- Define features, targets, predictions, and residuals for regression.
- Create training, validation, and test sets.
- Fit normalization parameters on training data only.
- Build and train a Keras MLP for a continuous target.
- Compare MSE, MAE, and Huber loss.
- Evaluate models with MAE, RMSE, and R-squared.
- Compare against mean and linear-regression baselines.
- Interpret observed-versus-predicted and residual plots.

## Contents

- `04_Artificial_Neural_Networks_and_Regression_with_TensorFlow.ipynb` — complete educational notebook.
- `requirements-notebook04.txt` — Python package dependencies.
- `VALIDATION_REPORT.md` — structural and runtime-validation notes.

## Environment

Use a 64-bit Python environment supported by the installed TensorFlow release. Install the packages with:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-notebook04.txt
```

Then launch Jupyter:

```bash
jupyter lab
```

Open the notebook and run all cells from top to bottom.

### Windows note

TensorFlow can be used on native Windows for CPU workflows. Native-Windows NVIDIA GPU support is not available in current TensorFlow releases; use WSL2 for supported NVIDIA GPU workflows. See the official TensorFlow installation guide for current platform and Python requirements:

- https://www.tensorflow.org/install/pip

## Dataset

The notebook generates its own small synthetic dataset at runtime. No external dataset download is required. The data-generating equation contains linear and nonlinear components, random noise, and a small deliberately contaminated subset for demonstrating robust regression losses. It is an educational simulation and must not be interpreted as real biomedical data.

## Reproducibility

A fixed random seed is used for the synthetic data generation, Keras initialization, and data splitting. Hardware, library versions, and some operations can still affect exact numerical results.

## Mathematical notation

Use `$...$` for inline equations and `$$...$$` for display equations in notebook Markdown cells.

## Suggested study order

1. Read the conceptual sections.
2. Run the data-generation and split sections.
3. Inspect the normalization and MLP architecture.
4. Train the model and review learning curves.
5. Evaluate once on the held-out test set.
6. Compare baselines and loss functions.
7. Complete the exercises.

## Next

Notebook 05: Neural Network Classification with TensorFlow.
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook04.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
