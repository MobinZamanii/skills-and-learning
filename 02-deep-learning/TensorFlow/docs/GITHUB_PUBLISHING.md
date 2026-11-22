# Publishing This Repository to GitHub

This package is prepared as a local Git repository content tree. It has **not** been pushed to GitHub because no destination repository or GitHub authorization was provided.

## 1. Create an empty GitHub repository

On GitHub, create a new repository named `Deep-Learning-with-TensorFlow`. To avoid merge conflicts, create it without an automatically generated README, license, or `.gitignore`; this package already contains those project files except for a license.

## 2. Extract the ZIP and initialize Git

Open a terminal in the extracted `Deep-Learning-with-TensorFlow` folder and run:

```bash
git init
git add .
git status
git commit -m "Add 12-notebook TensorFlow deep learning course"
git branch -M main
```

## 3. Connect and push

Replace the placeholders with your GitHub account and repository URL:

```bash
git remote add origin https://github.com/<USERNAME>/Deep-Learning-with-TensorFlow.git
git push -u origin main
```

GitHub may ask you to authenticate through your configured Git credential manager or browser.

## 4. Before making the repository public

- Choose and add a `LICENSE` file if you want to grant public reuse rights.
- Review the licenses and terms for external datasets and pretrained weights referenced by the notebooks.
- Run `python scripts/validate_notebooks.py` after any edits.
- Execute each notebook end-to-end in the intended TensorFlow environment and update its `VALIDATION_REPORT.md` with the actual runtime details.
- Do not upload private, identifiable, or restricted datasets, model files, logs, or notebook outputs.
