# Notebook 09 — Transfer Learning and Pretrained Models

This notebook teaches transfer learning for image classification with TensorFlow/Keras. It covers feature extraction, fine-tuning, architecture-specific preprocessing, and evaluation.

## Contents

- Transfer learning concepts and workflow
- CIFAR-10 four-class practical dataset
- Stratified train/validation/test sampling
- `tf.data` input pipeline
- MobileNetV2 ImageNet pretrained backbone (`include_top=False`)
- Global Average Pooling and a new classification head
- Frozen-backbone feature extraction
- Optional offline feature caching with Logistic Regression
- Selective fine-tuning with a low learning rate
- Batch Normalization handling
- MobileNetV2 vs ResNet50 vs EfficientNetB0
- Confusion matrix, per-class metrics, error analysis
- Model saving/reloading and limitations for biomedical use

## Files

- `09_Transfer_Learning_and_Pretrained_Models.ipynb` — complete educational notebook
- `requirements-notebook09.txt` — Python dependencies
- `VALIDATION_REPORT.md` — static and partial execution checks

## Setup

Use a clean Python environment. TensorFlow CPU installation:

```bash
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
# macOS / Linux
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-notebook09.txt
```

Then launch Jupyter:

```bash
jupyter lab
```

The first notebook run downloads CIFAR-10 and pretrained ImageNet weights for MobileNetV2. An internet connection is required for those downloads. Training can run on CPU, although a supported GPU is recommended for faster experimentation.

## Important methodological notes

- The notebook keeps the official CIFAR-10 test partition separate until final evaluation.
- For biomedical tasks, replace image-level random splitting with patient-level splitting (and consider site-level external validation).
- MobileNetV2 expects inputs scaled to `[-1, 1]`; ResNet50 and EfficientNetB0 use different preprocessing conventions. Do not mix or apply preprocessing twice.
- Fine-tuning uses a lower learning rate and keeps Batch Normalization layers in inference mode.
- The CIFAR-10 experiment is educational and does not establish clinical performance.
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook09.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
