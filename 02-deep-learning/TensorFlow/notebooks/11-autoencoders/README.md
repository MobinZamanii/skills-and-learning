# Notebook 11 — Autoencoders and Unsupervised Deep Learning

This notebook introduces unsupervised representation learning with TensorFlow/Keras. It covers a basic undercomplete autoencoder, sparse and denoising autoencoders, a Variational Autoencoder (VAE), and reconstruction-based anomaly detection.

## Contents

- Encoder, decoder, bottleneck, and reconstruction objectives
- MSE, MAE, and binary cross-entropy assumptions
- Synthetic gene-expression-like data and leakage-safe standardization
- Dense undercomplete autoencoder and latent-space inspection
- Sparse autoencoder with activity regularization
- Denoising autoencoder with corrupted inputs and clean targets
- VAE with a reparameterization layer and KL-divergence regularization
- Validation-calibrated reconstruction threshold and held-out anomaly evaluation
- Saving models, exercises, and references

## Practical dataset

The notebook generates a small synthetic continuous-feature dataset with NumPy. Artificial anomalies are injected only into the held-out test set. No external dataset download is required. The data are pedagogical and are not real gene-expression data or clinical evidence.

## Environment

Recommended: Python 3.10–3.12. Install dependencies with:

```bash
python -m pip install -r requirements-notebook11.txt
```

Then open the notebook in JupyterLab or VS Code. TensorFlow can run on CPU; GPU setup depends on the operating system and the current TensorFlow installation guide.

## Execution notes

The notebook trains four neural models (basic, sparse, denoising, and variational autoencoders). Training time depends on hardware. Reduce `epochs`, `N_FEATURES`, or the sample counts for a quick smoke test. The scaler is fit only on normal training data; validation contains normal data for model selection and threshold calibration; the test set is reserved for final evaluation.

The VAE uses a custom Keras model and custom `train_step` to expose reconstruction and KL losses separately. The custom class definition must be available when reloading the full VAE object. For inference, the encoder and decoder can be saved separately.

## Mathematical rendering convention

Inline equations use `$...$`; display equations use `$$...$$` for reliable rendering in Jupyter Markdown.

## References

- TensorFlow Autoencoders: https://www.tensorflow.org/tutorials/generative/autoencoder
- Keras Variational Autoencoder example: https://keras.io/examples/generative/vae/
- Keras regularizers: https://keras.io/api/layers/regularizers/
- Hinton & Salakhutdinov (2006): https://doi.org/10.1126/science.1127647
- Kingma & Welling (2014): https://arxiv.org/abs/1312.6114
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook11.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
