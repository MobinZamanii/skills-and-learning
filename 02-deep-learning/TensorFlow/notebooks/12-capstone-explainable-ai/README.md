# Notebook 12 — Deep Learning Capstone: Biological Image Classification and Model Interpretation

This capstone completes the 12-notebook **Deep Learning with TensorFlow** roadmap. It combines a reproducible image-classification workflow with specimen-level splitting, a CNN baseline, MobileNetV2 transfer learning, validation-based model selection, temperature scaling, internal and external evaluation, Grad-CAM, artifact saving, and a model card.

## Important scope limitation

The notebook generates synthetic microscopy-like images for two simulated morphology labels (`round` and `elongated`). These are not real biological or clinical images. The notebook is an educational programming and methodology exercise and must not be used to make diagnostic, screening, or treatment decisions. Performance on these synthetic images is not evidence of real-world validity.

## Package contents

- `12_Deep_Learning_Capstone_Biological_Image_Classification_and_Explainable_AI.ipynb` — complete tutorial and capstone.
- `requirements-notebook12.txt` — suggested Python dependencies.
- `VALIDATION_REPORT.md` — validation scope and known execution limitations.

## Environment

The requirements target TensorFlow 2.21.0 and Keras 3.15.1 with Python 3.11. Install dependencies in a clean virtual environment:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-notebook12.txt
```

For GPU acceleration on Windows, use a supported WSL2/Linux environment and follow the official TensorFlow installation guidance. Native Windows CPU execution is suitable for this small educational dataset.

## Running the notebook

1. Start Jupyter Lab or Jupyter Notebook from the project directory.
2. Open the notebook and run cells from top to bottom.
3. The synthetic image dataset is generated at runtime; no large dataset download is required.
4. By default, the notebook attempts to load ImageNet weights for MobileNetV2. The first run may require internet access. If loading fails, it falls back to random initialization and sets `PRETRAINED_WEIGHTS_LOADED = False`; results must then be described as a randomly initialized MobileNetV2 architecture, not transfer learning.
5. Model outputs are written to `capstone_outputs/`.

## Data split design

Images are grouped by simulated specimen. Training, model-selection validation, calibration, and internal test sets contain disjoint specimen IDs. A separately generated external synthetic cohort has a simulated acquisition-style shift and is held out from development.

## Reproducibility and interpretation

The notebook sets random seeds, records model metadata, saves models in the `.keras` format, and exports internal-test predictions. Grad-CAM is demonstrated on the CNN baseline. It is a visualization of score sensitivity, not a causal explanation or proof of biological validity.

## Official references

- TensorFlow image classification: https://www.tensorflow.org/tutorials/images/classification
- TensorFlow image loading: https://www.tensorflow.org/tutorials/load_data/images
- Keras MobileNetV2: https://keras.io/api/applications/mobilenet/
- Keras transfer learning: https://keras.io/guides/transfer_learning/
- Keras saving and serialization: https://keras.io/guides/serialization_and_saving/
- scikit-learn probability calibration: https://scikit-learn.org/stable/modules/calibration.html
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook12.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
