# Environment Setup

## Reference environment

The repository-level environment is designed around this reference stack:

- Python 3.11
- TensorFlow 2.21.0
- Keras 3.15.1
- NumPy, Pandas, Matplotlib, scikit-learn, Pillow, SciPy, JupyterLab, and TensorBoard

The dependency ranges and pins are recorded in the root `requirements.txt`. TensorFlow's supported Python versions and platform-specific installation instructions can change; consult the [official TensorFlow pip installation guide](https://www.tensorflow.org/install/pip) before creating a new environment.

## Windows CPU setup

Native Windows CPU execution is supported by the available TensorFlow Windows packages. Use PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name dl-tf --display-name "Python (Deep Learning with TensorFlow)"
jupyter lab
```

If PowerShell blocks activation scripts, use the activation guidance in the official Python documentation or activate the environment from Command Prompt with `.venv\Scripts\activate.bat`.

## macOS / Linux CPU setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name dl-tf --display-name "Python (Deep Learning with TensorFlow)"
jupyter lab
```

## NVIDIA GPU setup

For current TensorFlow releases, native-Windows NVIDIA GPU support is not available; TensorFlow documents WSL2 as the Windows route for GPU use. On supported Linux or WSL2 systems, follow the TensorFlow guide for the matching NVIDIA driver and CUDA dependencies. Do not assume that installing the regular Windows package enables CUDA acceleration.

Official guide: https://www.tensorflow.org/install/pip

## Verify the environment

Run the following in a terminal or notebook cell:

```python
import tensorflow as tf
import keras
import numpy as np
import sklearn

print("TensorFlow:", tf.__version__)
print("Keras:", keras.__version__)
print("NumPy:", np.__version__)
print("scikit-learn:", sklearn.__version__)
print("GPU devices:", tf.config.list_physical_devices("GPU"))
```

An empty GPU list is expected for CPU-only installations. The notebooks are designed to be educational and lightweight, but CNNs, pretrained backbones, and Transformer training may take longer on CPU.

## Common installation advice

- Upgrade `pip` before installing TensorFlow.
- Use a fresh virtual environment rather than mixing packages across projects.
- Select the environment's registered Jupyter kernel after launching JupyterLab.
- If dependency resolution fails, compare your Python version and operating system with the current TensorFlow installation matrix before changing pins.
- Do not combine incompatible chapter-level package pins. The repository root `requirements.txt` is the canonical environment for this integrated course.
