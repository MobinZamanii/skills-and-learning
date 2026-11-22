# Notebook 02 — Mathematical Foundations of Neural Networks

This folder contains the second notebook in the **Deep Learning with TensorFlow** learning path. The notebook develops the mathematics used by neural networks and applies it through NumPy-based examples.

## Contents

- Scalars, vectors, matrices, and higher-dimensional tensors
- Vector operations, dot products, norms, and transposes
- Matrix multiplication, array shapes, and broadcasting
- Linear transformations and affine neural-network layers
- Derivatives, partial derivatives, gradients, and the chain rule
- Loss functions and gradient descent
- Numerical gradient checking
- A one-hidden-layer neural network implemented with NumPy and manual backpropagation
- Exercises, glossary, and further reading

## Requirements

- Python 3.10 or newer
- NumPy
- Matplotlib
- Jupyter Notebook or JupyterLab

Install the notebook dependencies from this folder:

```bash
pip install -r requirements-notebook02.txt
```

Launch JupyterLab or Notebook, open `02_Mathematical_Foundations_of_Neural_Networks.ipynb`, and run the cells from top to bottom.

## Mathematical notation

All mathematical expressions are written in standard Jupyter Markdown using `$...$` for inline mathematics and `$$...$$` for display equations.

## Data and reproducibility

The regression dataset in the final implementation section is synthetic and is generated inside the notebook. Random-number generation uses an explicit NumPy generator seed so that the example is reproducible. No external dataset or GPU is required.
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook02.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
