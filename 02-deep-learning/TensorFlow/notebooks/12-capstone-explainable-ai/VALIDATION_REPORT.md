# Validation Report — Notebook 12

## Static validation

- Notebook JSON and nbformat structure: **passed**.
- Python syntax compilation for all code cells: **passed**.
- Markdown math delimiters (`$...$`, `$$...$$`): **balanced**.
- Repository text (notebook, README, requirements, report): English.
- ZIP archive integrity: checked after packaging.

## Executed checks in the build environment

- Synthetic image rendering with Pillow: executed.
- Development and external cohort generation: executed.
- Metadata generation and specimen-level split logic: executed.
- Disjoint specimen-ID assertions: executed.
- Image tensor dimensions and class counts: checked.

## Not executed in the build environment

TensorFlow is not installed in the file-generation environment. Therefore the following notebook sections were **not** run end-to-end here:

- CNN and MobileNetV2 model construction/training;
- ImageNet weight download and transfer learning;
- temperature scaling on model predictions;
- TensorFlow Grad-CAM computation;
- Keras model saving/reloading.

These code cells were syntax-checked, but syntax validation is not the same as runtime validation. Run the notebook from top to bottom in the target TensorFlow environment before considering the capstone fully executed.

## Important interpretation limits

The input images and labels are synthetic. The external cohort is a simulated domain shift, not a real independent clinical cohort. No metric from this notebook supports diagnostic or clinical claims. Grad-CAM is a model-behavior visualization and is not a causal explanation.

## Build counts

- Total cells: 55
- Markdown cells: 27
- Code cells: 28
- Development images: 960
- External synthetic images: 240
- Training images: 672
- Model-selection validation images: 72
- Calibration images: 72
- Internal test images: 144
