# Notebook 03 — TensorFlow, Keras, and Data Pipelines

Part I — Foundations of Deep Learning | Beginner to Intermediate

## Overview

This notebook introduces TensorFlow tensors, shapes and data types, tensor operations, automatic differentiation with `tf.GradientTape`, the Keras model-construction APIs, and input pipelines with `tf.data`. It concludes with an end-to-end regression example using a small synthetic dataset.

## Contents

- Tensor creation, inspection, and manipulation
- Broadcasting, reductions, matrix operations, and NumPy interoperability
- Automatic differentiation and a gradient-descent update
- Eager execution and `tf.function`
- Keras Sequential, Functional, and subclassing APIs
- Train/validation/test splitting and training-only normalization
- `tf.data`: map, cache, shuffle, batch, and prefetch
- Model training, evaluation, prediction, and saving

## Requirements

- Python 3.10–3.13 (check the TensorFlow installation guide for the version you install)
- TensorFlow 2.16 or newer, below 2.22 for this tested API range
- NumPy, Matplotlib, and scikit-learn
- Jupyter Notebook or JupyterLab

Install into the active Jupyter environment:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-notebook03.txt
```

Then open `03_TensorFlow_Keras_and_Data_Pipelines.ipynb` and run the cells from top to bottom. The model is intentionally small and can be trained on a CPU.

## Platform note

Modern TensorFlow releases do not provide native-Windows NVIDIA GPU support. Native Windows CPU execution is supported; use WSL2 for a modern NVIDIA GPU setup. Always consult the official installation guide for current platform and Python requirements.

## Reproducibility

The notebook sets NumPy and TensorFlow random seeds. Exact numerical results can still vary with TensorFlow version, hardware, and parallel execution.

## References

- https://www.tensorflow.org/guide/tensor
- https://www.tensorflow.org/guide/autodiff
- https://www.tensorflow.org/guide/data
- https://www.tensorflow.org/guide/data_performance
- https://keras.io/api/models/
- https://keras.io/guides/functional_api/
- https://www.tensorflow.org/install/pip
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook03.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
