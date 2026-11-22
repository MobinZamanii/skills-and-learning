# Deep Learning with TensorFlow

**A 12-notebook educational roadmap from fundamentals to applied deep learning.**

This repository is a structured, hands-on learning path for understanding, implementing, training, evaluating, and interpreting deep learning models with **TensorFlow and Keras**. It is designed for beginner-to-intermediate learners and uses NumPy, scikit-learn, and synthetic datasets to make core ideas approachable before moving to computer vision, transfer learning, sequential models, autoencoders, and an end-to-end capstone.

All notebooks, documentation, code comments, chart labels, and mathematical explanations are written in **English**. Mathematical notation in notebook Markdown uses `$...$` for inline equations and `$$...$$` for display equations.

> **Educational scope:** Several chapters use synthetic tabular, time-series, or image data. These examples demonstrate methods and workflows; they are not clinical evidence and must not be used to support medical or diagnostic claims.

## Learning roadmap

| Part | Notebook | Topic | Main skills |
|---|---:|---|---|
| I — Foundations | 01 | [Introduction to Deep Learning and Neural Networks](notebooks/01-foundations/01_Introduction_to_Deep_Learning_and_Neural_Networks.ipynb) | Neurons, layers, weights, activations, forward propagation, first Keras model |
| I — Foundations | 02 | [Mathematical Foundations of Neural Networks](notebooks/02-mathematical-foundations/02_Mathematical_Foundations_of_Neural_Networks.ipynb) | Linear algebra, derivatives, gradients, chain rule, NumPy backpropagation |
| I — Foundations | 03 | [TensorFlow, Keras and Data Pipelines](notebooks/03-tensorflow-data-pipelines/03_TensorFlow_Keras_and_Data_Pipelines.ipynb) | Tensors, `GradientTape`, Keras APIs, `tf.data`, preprocessing |
| II — Model Training | 04 | [Artificial Neural Networks and Regression](notebooks/04-neural-networks-regression/04_Artificial_Neural_Networks_and_Regression_with_TensorFlow.ipynb) | MLP regression, loss functions, training, residual analysis |
| II — Model Training | 05 | [Neural Network Classification](notebooks/05-binary-classification/05_Neural_Network_Classification_with_TensorFlow.ipynb) | Binary classification, thresholds, ROC/PR, precision and recall |
| II — Model Training | 06 | [Multiclass Classification and Model Evaluation](notebooks/06-multiclass-classification/06_Multiclass_Classification_and_Model_Evaluation.ipynb) | Softmax, encoding, cross-entropy, multiclass metrics |
| II — Model Training | 07 | [Optimization, Regularization and Custom Training](notebooks/07-optimization-regularization/07_Optimization_Regularization_and_Custom_Training.ipynb) | Backpropagation, optimizers, initialization, regularization, custom loops |
| III — Architectures | 08 | [Convolutional Neural Networks](notebooks/08-convolutional-neural-networks/08_Convolutional_Neural_Networks_with_TensorFlow.ipynb) | Convolutions, filters, pooling, CNNs, feature maps |
| III — Architectures | 09 | [Transfer Learning and Pretrained Models](notebooks/09-transfer-learning/09_Transfer_Learning_and_Pretrained_Models.ipynb) | MobileNetV2, ResNet, EfficientNet, feature extraction, fine-tuning |
| III — Architectures | 10 | [Sequential Deep Learning: RNN, LSTM, GRU and Transformers](notebooks/10-sequential-deep-learning/10_Sequential_Deep_Learning_RNN_LSTM_GRU_and_Transformers.ipynb) | Sequence modeling, recurrent networks, attention, Transformers |
| IV — Applications | 11 | [Autoencoders and Unsupervised Deep Learning](notebooks/11-autoencoders/11_Autoencoders_and_Unsupervised_Deep_Learning.ipynb) | Latent spaces, denoising, VAEs, reconstruction, anomaly detection |
| IV — Applications | 12 | [Capstone: Biological Image Classification and Explainable AI](notebooks/12-capstone-explainable-ai/12_Deep_Learning_Capstone_Biological_Image_Classification_and_Explainable_AI.ipynb) | End-to-end workflow, internal/external evaluation, Grad-CAM, calibration, model cards |

## Repository structure

```text
Deep-Learning-with-TensorFlow/
├── README.md
├── requirements.txt
├── CONTRIBUTING.md
├── .gitignore
├── docs/
│   ├── ROADMAP.md
│   ├── ENVIRONMENT.md
│   ├── DATASETS_AND_SCOPE.md
│   └── VALIDATION_SUMMARY.md
├── notebooks/
│   ├── 01-foundations/
│   ├── 02-mathematical-foundations/
│   ├── 03-tensorflow-data-pipelines/
│   ├── 04-neural-networks-regression/
│   ├── 05-binary-classification/
│   ├── 06-multiclass-classification/
│   ├── 07-optimization-regularization/
│   ├── 08-convolutional-neural-networks/
│   ├── 09-transfer-learning/
│   ├── 10-sequential-deep-learning/
│   ├── 11-autoencoders/
│   └── 12-capstone-explainable-ai/
└── scripts/
    └── validate_notebooks.py
```

Each chapter folder contains its notebook, a chapter-specific README, and a validation report. The repository-level `requirements.txt` is the **single reference environment** for the integrated course.

## Quick start

### 1. Clone the repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd Deep-Learning-with-TensorFlow
```

### 2. Create and activate a virtual environment

Python 3.11 is the reference environment for this repository. Check the official TensorFlow installation guide for the current supported Python and operating-system matrix.

**Windows PowerShell**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Register and launch JupyterLab

```bash
python -m ipykernel install --user --name dl-tf --display-name "Python (Deep Learning with TensorFlow)"
jupyter lab
```

Open Notebook 01 and work through the notebooks in order. Run each notebook from top to bottom after selecting the `Python (Deep Learning with TensorFlow)` kernel.

For detailed setup notes, CPU/GPU guidance, and verification commands, see [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md). For steps to publish this prepared folder to a new GitHub repository, see [docs/GITHUB_PUBLISHING.md](docs/GITHUB_PUBLISHING.md).

## Recommended workflow

1. Follow the notebook sequence rather than jumping directly to the capstone.
2. Read the theory and mathematical sections before executing implementation cells.
3. Run all cells in order and inspect generated plots and diagnostics.
4. Complete the exercises at the end of each notebook.
5. Keep train, validation, calibration, and test roles separate. Fit preprocessing steps on training data only.
6. For medical or biological data, split at the patient/specimen level when repeated observations belong to the same subject, and use a genuinely independent external cohort when available.
7. Record package versions, random seeds, data provenance, and model limitations when adapting examples.

## Data and model scope

The notebooks are designed to be reproducible without requiring a large private dataset. Most chapters generate synthetic data inside the notebook. Notebook 09 uses CIFAR-10 as a public image-classification example. Notebook 12 uses synthetic microscopy-like images and a simulated external cohort to demonstrate a workflow; that simulated cohort is not real external clinical validation.

See [docs/DATASETS_AND_SCOPE.md](docs/DATASETS_AND_SCOPE.md) for the chapter-by-chapter data notes and interpretation limits.

## Validation status

The notebooks have been structurally checked as Jupyter notebooks, their Python code cells have been syntax-parsed, mathematical delimiters have been checked, and authored notebook content has been scanned for non-English script. Some chapter-specific NumPy/scikit-learn data and metric workflows were also smoke-tested; the exact scope is recorded in each `VALIDATION_REPORT.md` and in [docs/VALIDATION_SUMMARY.md](docs/VALIDATION_SUMMARY.md).

**Important:** Static validation is not the same as executing every notebook. TensorFlow/Keras training and model-specific runtime sections were not all executed in the repository assembly environment. Run each notebook end-to-end in your target environment before relying on its generated results.

To rerun the repository-level static checks:

```bash
python scripts/validate_notebooks.py
```

## References

- [TensorFlow tutorials](https://www.tensorflow.org/tutorials)
- [TensorFlow guides](https://www.tensorflow.org/guide)
- [TensorFlow installation guide](https://www.tensorflow.org/install/pip)
- [Keras guides](https://keras.io/guides/)
- [Keras API reference](https://keras.io/api/)
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)

## License

No license has been selected for this repository yet. Add a `LICENSE` file before public distribution if you want to grant others explicit reuse rights. Also review dataset and pretrained-weight terms before redistributing derived assets.
