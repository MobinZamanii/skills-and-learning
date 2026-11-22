# Notebook 07 — Optimization, Regularization, and Custom Training

This notebook explains how neural networks learn and how training can be made more stable and generalizable. It covers the chain rule and backpropagation, batch strategies, common optimizers, learning-rate schedules, weight initialization, underfitting and overfitting, regularization, callbacks, gradient clipping, and a custom TensorFlow training loop.

## Learning outcomes

- Derive gradients for a small neural network and verify them numerically.
- Explain batch, stochastic, and mini-batch gradient descent.
- Compare SGD, Momentum, RMSprop, Adam, and AdamW.
- Understand learning-rate schedules and initialization choices.
- Diagnose underfitting and overfitting from training curves.
- Apply L1/L2 penalties, dropout, batch normalization, early stopping, and checkpointing.
- Use gradient clipping and TensorBoard.
- Implement a custom training loop with `tf.GradientTape` and include Keras regularization losses.
- Compare models using validation data and preserve the test set for final evaluation.

## Dataset

A small nonlinear regression dataset is generated with NumPy. It includes noise and non-informative features to make overfitting and regularization experiments observable. It is synthetic and has no biological or clinical interpretation.

## Package contents

- `07_Optimization_Regularization_and_Custom_Training.ipynb` — complete educational notebook.
- `requirements-notebook07.txt` — Python dependencies.
- `VALIDATION_REPORT.md` — structural and static validation notes.

## Environment

The dependency file uses TensorFlow 2.21.0 and Keras 3.15.1, with Python 3.11 recommended. CPU execution is sufficient for the small educational experiments. Confirm package compatibility for your operating system and Python version before installation.

Create and activate an isolated environment:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-notebook07.txt
```

Launch Jupyter:

```bash
jupyter lab
```

## Recommended execution order

Run the notebook from top to bottom. The notebook creates a fixed train/validation/test split. The scaler is fitted only on the training subset. Use validation data for callbacks and model selection; use the test set only for final evaluation.

## TensorBoard

The notebook configures a Keras TensorBoard callback. After training with that callback, launch TensorBoard from the project directory:

```bash
tensorboard --logdir logs_notebook07
```

Install TensorBoard explicitly if the command is unavailable in your environment.

## Important limitations

The generated data are synthetic. Results demonstrate workflow mechanics rather than generalization to a real-world domain. Training outputs can vary across hardware and library versions. The structural validator does not replace executing the notebook in the target environment.
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook07.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
