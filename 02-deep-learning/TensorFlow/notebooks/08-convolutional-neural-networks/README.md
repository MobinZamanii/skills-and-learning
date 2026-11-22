# Notebook 08 — Convolutional Neural Networks (CNNs) with TensorFlow

## Overview

This notebook teaches the core mechanics of CNNs and implements a complete multiclass image-classification workflow with TensorFlow and Keras 3.

The practical project uses **synthetic cell-like images generated with NumPy**. The data are designed for teaching CNN mechanics only; they are not real microscopy data and have no clinical meaning.

## Learning objectives

- Represent image batches as tensors.
- Explain convolution, kernels, filters, stride, padding, feature maps, and pooling.
- Calculate convolution output shapes and trainable parameter counts.
- Build a small image pipeline with `tf.data`.
- Apply label-preserving image augmentation.
- Train and evaluate a CNN with Keras.
- Inspect errors and intermediate activations.

## Files

- `08_Convolutional_Neural_Networks_with_TensorFlow.ipynb` — complete tutorial and practical project.
- `requirements-notebook08.txt` — Python package requirements.
- `VALIDATION_REPORT.md` — static and partial execution validation results.

## Environment

Python 3.11 is recommended. Use an environment compatible with your installed TensorFlow and Keras versions. The notebook uses the TensorFlow backend with Keras 3 APIs.

### Install

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
# source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-notebook08.txt
python -m ipykernel install --user --name dl-tf-cnn --display-name "Python (DL TensorFlow CNN)"
```

Open the notebook in Jupyter and select the `Python (DL TensorFlow CNN)` kernel.

## Execution notes

- The notebook generates its dataset locally; no external dataset download is needed.
- The default dataset contains 900 grayscale images of size 64 × 64.
- Training uses a small CNN and early stopping. CPU execution is supported, but runtime depends on hardware and the TensorFlow build.
- Reduce `SAMPLES_PER_CLASS` or `EPOCHS` if you need a shorter demonstration.
- The test set is reserved for final evaluation.

## Important limitation

This notebook is an educational computer-vision exercise. Synthetic shapes must not be used to draw conclusions about cells, disease, clinical performance, or real medical imaging systems.
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook08.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
