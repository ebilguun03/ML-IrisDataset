"""Verify the original notebook offline without changing its saved source."""

import json
import os
from pathlib import Path
import tempfile

os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


def main():
    notebook = json.loads(Path(__file__).with_name("iris-vscode.ipynb").read_text())
    iris = load_iris()
    frame = pd.DataFrame(iris.data, columns=[
        "sepal-length", "sepal-width", "petal-length", "petal-width",
    ])
    frame["class"] = ["Iris-" + iris.target_names[i] for i in iris.target]
    original_read_csv = pd.read_csv

    def read_demo_csv(source, *args, **kwargs):
        if source == "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv":
            return frame.copy()
        return original_read_csv(source, *args, **kwargs)

    previous_dir = Path.cwd()
    namespace = {"__name__": "__notebook_verification__"}
    count = 0
    try:
        pd.read_csv = read_demo_csv
        with tempfile.TemporaryDirectory(prefix="iris-check-") as output:
            os.chdir(output)
            for index, cell in enumerate(notebook["cells"]):
                if cell["cell_type"] != "code":
                    continue
                source = "".join(cell.get("source", []))
                # Use one worker in this smoke check; keep original notebook unchanged.
                source = source.replace("n_jobs=-1", "n_jobs=1")
                exec(compile(source, f"notebook-cell-{index}", "exec"), namespace)
                plt.close("all")
                count += 1
            assert namespace["dataset"].shape == (150, 5)
            assert namespace["X_train"].shape == (120, 4)
            assert namespace["X_test"].shape == (30, 4)
            predictions = namespace["model"].predict(namespace["new_samples"])
            assert predictions.shape == (3,)
            assert set(predictions) <= set(frame["class"])
            assert np.array_equal(predictions, namespace["loaded"].predict(namespace["new_samples"]))
            assert set(namespace["Y_test"]) == set(frame["class"])
        print(f"PASS: {count} original code cells executed; shape, classes and round-trip predictions agree.")
    finally:
        pd.read_csv = original_read_csv
        os.chdir(previous_dir)


if __name__ == "__main__":
    main()
