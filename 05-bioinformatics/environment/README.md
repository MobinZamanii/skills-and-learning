# Environment Setup

The root environment is intentionally limited to broadly used foundations. Specialist modules may require additional tools and separately tested environments.

## Conda

```bash
conda env create -f environment.yml
conda activate bioinformatics-learning
python -m ipykernel install --user --name bioinformatics-learning
jupyter lab
```

## pip

```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install --upgrade pip
python -m pip install -r environment/requirements.txt
jupyter lab
```

Always consult module-specific instructions before installing specialist packages. Some genomics tools require operating-system packages or separate executables.
