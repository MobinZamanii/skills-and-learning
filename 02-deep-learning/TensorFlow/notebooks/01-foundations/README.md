# Deep Learning with TensorFlow — Notebook 01

**Notebook 01: Introduction to Deep Learning and Neural Networks**  
**Level:** Beginner  
**Part:** Foundations of Deep Learning

This repository contains the first notebook in a structured, 12-notebook learning path for Deep Learning with TensorFlow. The notebook is written entirely in English and introduces neural network fundamentals through explanations, mathematical notation, diagrams, NumPy examples, and a complete introductory TensorFlow/Keras classification exercise.

## Learning Objectives

By completing this notebook, you will be able to:

- Distinguish Artificial Intelligence, Machine Learning, and Deep Learning.
- Explain the components of an artificial neuron and a feedforward neural network.
- Describe weights, biases, activation functions, forward propagation, loss, and training.
- Explain the roles of TensorFlow and Keras.
- Build, compile, train, evaluate, and use a small Keras model.
- Interpret basic training curves, predictions, and a decision boundary.

## Notebook Contents

1. From Artificial Intelligence to Deep Learning
2. Artificial Neural Networks and Artificial Neurons
3. Weights, Biases, and Activation Functions
4. Layers and Neural Network Architecture
5. Forward Propagation and the Learning Process
6. TensorFlow and Keras
7. Building and Training a First Neural Network
8. Evaluation and Prediction
9. Conceptual Summary
10. Exercises and Self-Check Questions
11. Glossary and References

## Repository Files

```text
notebooks/01-foundations/
├── 01_Introduction_to_Deep_Learning_and_Neural_Networks.ipynb
├── README.md
└── requirements-notebook01.txt
```

## Environment

Use a dedicated Python virtual environment. The dependency file lists the packages required by this notebook. Check the official TensorFlow installation guide for the current Python and platform compatibility information:

https://www.tensorflow.org/install/pip

### Install

```bash
python -m venv .venv
```

Activate the environment, then run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-notebook01.txt
```

Launch Jupyter Lab or Jupyter Notebook:

```bash
jupyter lab
```

Open `01_Introduction_to_Deep_Learning_and_Neural_Networks.ipynb` and run the cells from top to bottom.

## Mathematical Notation

Mathematical expressions use standard Jupyter Markdown delimiters:

- Inline equations: `$ ... $`
- Display equations: `$$ ... $$`

Jupyter renders these expressions using MathJax.

## Dataset and Scope

The hands-on classification example uses a synthetic two-moons dataset. These data are generated for teaching purposes only and do not represent real biological or medical observations. The notebook is intended to teach foundational concepts, not to develop or validate a clinical model.

## Learning Path

This is Notebook 01 of the **Deep Learning with TensorFlow** learning path. The next notebook is:

**Notebook 02 — Mathematical Foundations of Neural Networks**

## References

- [TensorFlow — Beginner quickstart](https://www.tensorflow.org/tutorials/quickstart/beginner)
- [TensorFlow — Tutorials](https://www.tensorflow.org/tutorials)
- [Keras — The Sequential model](https://keras.io/guides/sequential_model/)
- [Keras — Activation functions](https://keras.io/api/layers/activations/)
- [TensorFlow — Install TensorFlow with pip](https://www.tensorflow.org/install/pip)
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook01.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
