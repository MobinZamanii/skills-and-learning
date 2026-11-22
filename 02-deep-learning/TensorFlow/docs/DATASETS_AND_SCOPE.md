# Datasets and Scope

The course prioritizes small, reproducible examples. Synthetic datasets are used in several chapters so that learners can focus on the algorithm without downloading large data collections.

| Notebook | Data used in the learning workflow | Interpretation limit |
|---:|---|---|
| 01 | Synthetic two-moons classification data | Demonstration only; not biological data. |
| 02 | Synthetic regression values | Used to demonstrate vectorized computation and backpropagation. |
| 03 | Small synthetic tabular regression data | Used to teach tensors, preprocessing, and `tf.data`. |
| 04 | Synthetic regression data with gene-expression-like feature framing | Not measured gene-expression data. |
| 05 | Synthetic binary-classification data | Not a diagnostic dataset. |
| 06 | Synthetic multiclass data | Not evidence of real-world class performance. |
| 07 | Synthetic regression data | Used for optimization and regularization demonstrations. |
| 08 | Synthetic geometric cell-like images | Not real microscopy, pathology, or clinical images. |
| 09 | CIFAR-10, a public general-purpose image dataset | Demonstrates transfer learning; not a medical-imaging dataset. |
| 10 | Synthetic univariate time series | Not real patient or biological time-series measurements. |
| 11 | Synthetic gene-expression-like feature matrix with artificial anomalies | Not biological measurements; anomaly injection is pedagogical. |
| 12 | Synthetic microscopy-like images and a simulated external cohort | The external cohort is simulated domain shift, not independent clinical validation. |

## Guidance for adapting to real biological or medical data

- Confirm dataset provenance, permitted use, de-identification, and any applicable ethics or governance requirements before use.
- Split at the patient, specimen, slide, or acquisition level as appropriate. Do not allow correlated images or repeated observations from the same subject to leak across partitions.
- Fit scalers, imputers, feature selectors, and other learned preprocessing steps on training data only.
- Use validation data for model selection and calibration data for calibration when separate calibration is planned. Keep the test set for final evaluation.
- Prefer a truly independent external cohort for transportability assessment. A simulated cohort or random holdout from the same source is not equivalent to external validation.
- Report class-wise metrics, confidence intervals where appropriate, calibration, failure modes, and limitations. Accuracy alone is rarely sufficient for imbalanced or high-stakes tasks.
- Treat saliency maps such as Grad-CAM as model-behavior visualizations, not as causal explanations or proof that a model attends to clinically valid evidence.

No model in this repository is a medical device or intended for clinical decision-making.
