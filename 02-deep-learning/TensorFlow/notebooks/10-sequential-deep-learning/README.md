# Notebook 10 — Sequential Deep Learning: RNN, LSTM, GRU and Transformers

This notebook teaches sequence modeling with TensorFlow/Keras. It progresses from recurrent neural networks to gated recurrent architectures, attention, and an encoder-only Transformer for multi-step time-series forecasting.

## Contents

- Sequential data, tensor shapes, and forecasting task definitions
- Chronological splitting, training-only scaling, and sliding windows
- SimpleRNN, LSTM, and GRU architectures
- Vanishing/exploding gradient intuition
- Scaled dot-product and multi-head attention
- Sinusoidal positional encoding and Transformer encoder blocks
- Persistence baseline, validation-driven model selection, final test metrics, horizon-wise errors, and residual analysis

## Practical dataset

The project uses a synthetic signal generated with NumPy. No external dataset download is required. The signal is for educational sequence-modeling practice only; it is not a biological or clinical dataset.

## Environment

Recommended: Python 3.10–3.12. Install dependencies with:

```bash
python -m pip install -r requirements-notebook10.txt
```

Then open the notebook in JupyterLab or VS Code. TensorFlow can use CPU; GPU setup depends on the operating system and the current TensorFlow installation guide.

## Execution notes

The first run trains four neural models and may take several minutes on CPU. Reduce `EPOCHS`, `N_STEPS`, or model widths to make a quick smoke test. The data split is chronological, the scaler is fit only on the training period, architecture selection is based on validation MAE, and the test period is reserved for final evaluation.

## Mathematical rendering convention

Inline equations use `$...$`; display equations use `$$...$$` for reliable rendering in Jupyter Markdown.

## References

- TensorFlow Transformer tutorial: https://www.tensorflow.org/text/tutorials/transformer
- TensorFlow time-series forecasting: https://www.tensorflow.org/tutorials/structured_data/time_series
- Keras recurrent layers: https://keras.io/api/layers/recurrent_layers/
- Keras MultiHeadAttention: https://keras.io/api/layers/attention_layers/multi_head_attention/
- Vaswani et al. (2017), Attention Is All You Need: https://arxiv.org/abs/1706.03762
## Integrated Course Environment

This chapter is part of the full **Deep Learning with TensorFlow** repository. From the repository root, install the shared course environment with:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` is the canonical environment for the complete 12-notebook course. This chapter also includes `requirements-notebook10.txt`, which mirrors the same pinned course stack for standalone use. See the root `README.md` and `docs/ENVIRONMENT.md` for setup instructions.
