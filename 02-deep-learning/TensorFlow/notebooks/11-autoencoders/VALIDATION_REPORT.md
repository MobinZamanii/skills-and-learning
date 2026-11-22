# Validation Report — Notebook 11

## Static validation

- Notebook format: valid (5.10.4).
- Total cells: 62.
- Markdown cells: 30.
- Code cells: 32.
- Python syntax errors: 0.
- Mathematical delimiter issues: 0.
- Non-English-script text in notebook cells: 0.
- Notebook metadata and cell structure: valid.

## Executed checks

TensorFlow is not installed in the build environment. TensorFlow/Keras training cells were therefore syntax-checked but not executed here. The following TensorFlow-independent checks were executed separately:

- Synthetic feature generation and shape checks.
- Training-only standardization and train/validation/test partition checks.
- Artificial anomaly generation and test-label alignment.
- NumPy reconstruction-error calculation.
- A deterministic PCA reconstruction proxy, fit on normal training samples only, to smoke-test validation-quantile thresholding and the scikit-learn anomaly metrics.

### PCA reconstruction-proxy smoke test

To verify the data and evaluation pipeline without claiming TensorFlow model execution, an 8-component PCA reconstruction proxy was fitted on the standardized normal training set. The 99th-percentile threshold was calibrated on normal validation errors and then evaluated on the held-out test set:

- Train shape: `(1600, 48)`.
- Validation shape: `(350, 48)`.
- Test shape: `(490, 48)`; 350 normal and 140 artificial anomalies.
- Confusion matrix (true rows: normal/anomaly; predicted columns: normal/anomaly): `[[346, 4], [0, 140]]`.
- Precision: `0.972`; recall: `1.000`; F1: `0.986`.
- ROC-AUC: `1.000`; average precision: `1.000`.

These results validate only the synthetic data generation and score/threshold/evaluation plumbing with a PCA proxy. They are **not** TensorFlow autoencoder results and should not be interpreted as expected performance on real data.

## TensorFlow execution limitation

The basic, sparse, denoising, and variational autoencoder training loops, Keras custom `train_step`, model saving/loading, and TensorFlow plotting outputs were not executed in the build environment because TensorFlow is unavailable. Run the notebook in the target TensorFlow environment to validate these runtime-dependent steps.

## Methodological review

- The scaler is fit only on normal training observations.
- Autoencoders are trained only on normal training observations.
- Normal validation observations are used for model selection and anomaly-threshold calibration.
- Artificial anomalies are included only in the held-out test set.
- The 99th-percentile threshold is illustrative and calibrated from validation-normal errors, not selected using test labels.
- The synthetic feature data and injected anomalies are pedagogical, not biological or clinical evidence.
