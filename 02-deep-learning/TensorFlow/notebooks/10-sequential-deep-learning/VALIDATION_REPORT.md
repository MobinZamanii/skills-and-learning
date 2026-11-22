# Validation Report — Notebook 10

## Static validation

- Notebook format: valid (nbformat 5.10.4).
- Total cells: 81.
- Markdown cells: 48.
- Code cells: 33.
- Python syntax errors: 0.
- Mathematical delimiter issues: 0.
- Non-English (Persian/Arabic-script) prose: none detected.

## Executed checks

The following TensorFlow-independent components were executed successfully in the build environment:

- Synthetic signal generation.
- Chronological train/validation/test window construction.
- Input and target shape checks.
- No-cross-boundary target-window checks.
- NumPy scaled dot-product attention demonstration and attention-weight normalization.
- Sinusoidal positional encoding shape check.

## TensorFlow execution limitation

TensorFlow is not installed in the build environment. Consequently, TensorFlow/Keras-specific cells (RNN/LSTM/GRU model construction and fitting, `tf.data`, Keras MultiHeadAttention, Transformer training, and model saving/loading) were syntax-checked but were not executed here. Run the notebook in the target TensorFlow environment to validate those runtime-dependent steps.

## Methodological review

- The notebook fits normalization statistics on the training time interval only.
- Validation and test targets are assigned to disjoint chronological periods.
- Architecture selection is based on validation MAE. The test period is reserved for final descriptive evaluation.
- Historical context from earlier periods is allowed for the first forecast window in a later period; later-period targets are never used to fit the scaler.
- The synthetic benchmark is pedagogical and must not be interpreted as clinical evidence.
