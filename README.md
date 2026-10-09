# Iris Classification Experiments

A learning project by **Bil Enkhbileg** comparing supervised classifiers on the four measurements in the Iris dataset. The complete experiment is in `iris-vscode.ipynb`; `project.py` only loads and summarizes the dataset, and `iris.ipynb` is an earlier partial notebook.

## Implemented Workflow

1. Load the public Iris CSV, inspect class counts and summary statistics, and plot feature distributions.
2. Compare Logistic Regression, Linear Discriminant Analysis, K-nearest neighbors, a decision tree, Gaussian Naive Bayes and an SVM using shuffled 10-fold stratified cross-validation on a training subset.
3. Train scaled SVM pipelines and inspect held-out accuracy, a classification report and confusion matrix.
4. Predict three example measurements, serialize a fitted pipeline with joblib, and search RBF SVM hyperparameters with `GridSearchCV`.

The notebook contains successive experiments with different split/scaling choices, not one production training pipeline. The baseline comparison uses an unstratified 80/20 split; later SVM experiments use a stratified split. An estimator named `best` is manually selected, not automatically chosen from the baseline results. Recorded outputs are illustrative, not a general performance guarantee.

## Run Locally

Use Python 3 in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install jupyterlab
jupyter lab iris-vscode.ipynb
```

Run cells from top to bottom. The original notebook fetches the CSV from [Jason Brownlee's public dataset mirror](https://github.com/jbrownlee/Datasets/blob/master/iris.csv), so it needs internet access. It writes `iris_svm.joblib` in the current directory. Only load serialized models you trust: joblib/pickle loading can execute code.

```bash
python verify_notebook.py
```

This added verification harness executes the original notebook cells with the built-in scikit-learn Iris dataset substituted in memory, a non-interactive plotting backend, and a temporary output directory. It checks shape, class coverage and model predictions without downloading data or loading the bundled model. It does not replace or modify the coursework notebook.

## Scope and Attribution

This repository demonstrates exploratory analysis, model comparison, preprocessing pipelines and evaluation, not a novel classifier or deployed API. The methods and dataset are third-party educational resources. The dataset mirror is credited above; commit history records Bil's notebook submission, but does not independently establish the origin of every baseline snippet.

The small existing model artifact is retained as coursework evidence; regenerate it locally rather than assuming compatibility with a different scikit-learn version. `test_numpy.py`, `test_pandas.py` and `test_scipy.py` are import checks, not a model test suite.
