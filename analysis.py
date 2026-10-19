"""Reproducible Iris classification with group-safe model selection."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codealpha-matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(tempfile.gettempdir()) / "codealpha-cache"))
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import GridSearchCV, StratifiedGroupKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

ROOT = Path(__file__).resolve().parent
SEED = 42
FEATURES = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
TARGET = "Species"
CLASSES = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def load_and_audit(data_path: Path) -> tuple[pd.DataFrame, np.ndarray, dict]:
    """Reject unusable labels/measurements and identify identical-feature groups."""
    data = pd.read_csv(data_path)
    required = [*FEATURES, TARGET]
    missing_columns = [column for column in required if column not in data]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    audit = {
        "source_file": data_path.name,
        "sha256": hashlib.sha256(data_path.read_bytes()).hexdigest(),
        "rows": int(len(data)),
        "columns": data.columns.tolist(),
        "predictors": FEATURES,
        "excluded_identifier": "Id",
        "missing_by_column": {column: int(value) for column, value in data.isna().sum().items()},
        "duplicate_complete_rows": int(data.duplicated().sum()),
        "duplicate_measurement_and_label_rows": int(data.duplicated(required).sum()),
        "duplicate_measurement_rows": int(data.duplicated(FEATURES).sum()),
        "class_counts": {name: int(value) for name, value in data[TARGET].value_counts().sort_index().items()},
    }
    if data[required].isna().any().any():
        raise ValueError("Required measurements and species must not be missing.")
    if set(data[TARGET]) != set(CLASSES):
        raise ValueError(f"Expected exactly these species: {CLASSES}")
    if not all(pd.api.types.is_numeric_dtype(data[column]) for column in FEATURES):
        raise ValueError("All four measurement columns must be numeric.")
    if not np.isfinite(data[FEATURES].to_numpy()).all() or (data[FEATURES] <= 0).any().any():
        raise ValueError("Measurements must be finite and positive.")
    conflicts = data.groupby(FEATURES, dropna=False)[TARGET].nunique().gt(1)
    if conflicts.any():
        raise ValueError("Identical measurements have conflicting species labels; resolve the source data first.")
    groups = pd.factorize(pd.MultiIndex.from_frame(data[FEATURES]), sort=False)[0]
    audit["unique_measurement_groups"] = int(np.unique(groups).size)
    audit["duplicate_policy"] = (
        "Retain rows because repeated measurements can be separate flowers; keep all rows with "
        "identical four-feature measurements together in both the held-out split and every CV fold."
    )
    return data, groups, audit


def split_indices(data: pd.DataFrame, groups: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Use a single predetermined fold as the approximately 20% held-out test."""
    splitter = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=SEED)
    train, test = next(splitter.split(data[FEATURES], data[TARGET], groups))
    if set(groups[train]) & set(groups[test]):
        raise AssertionError("Feature groups overlap between training and test data.")
    return train, test


def candidate_models() -> dict[str, tuple[Pipeline, dict]]:
    """All hyperparameters and model families are fixed before viewing test metrics."""
    return {
        "dummy_most_frequent": (
            Pipeline([("classifier", DummyClassifier(strategy="most_frequent"))]),
            {},
        ),
        "logistic_regression": (
            Pipeline([("scale", StandardScaler()), ("classifier", LogisticRegression(max_iter=2000, random_state=SEED))]),
            {"classifier__C": [0.1, 1.0, 10.0]},
        ),
        "knn": (
            Pipeline([("scale", StandardScaler()), ("classifier", KNeighborsClassifier())]),
            {"classifier__n_neighbors": [3, 5, 7]},
        ),
        "rbf_svm": (
            Pipeline([("scale", StandardScaler()), ("classifier", SVC(kernel="rbf", gamma="scale", random_state=SEED))]),
            {"classifier__C": [0.1, 1.0, 10.0]},
        ),
    }


def evaluate(y_true: pd.Series, y_pred: np.ndarray) -> dict:
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, labels=CLASSES, average="macro", zero_division=0)),
        "classification_report": classification_report(
            y_true, y_pred, labels=CLASSES, output_dict=True, zero_division=0
        ),
        "confusion_matrix": confusion_matrix(y_true, y_pred, labels=CLASSES).tolist(),
    }


def save_plots(data: pd.DataFrame, metrics: dict, output: Path) -> None:
    plt.rcParams.update({"figure.dpi": 140, "font.size": 10})
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    counts = data[TARGET].value_counts().reindex(CLASSES)
    ax.bar([name.removeprefix("Iris-") for name in CLASSES], counts, color=["#2a9d8f", "#e9c46a", "#e76f51"])
    ax.set(title="Dataset species counts", ylabel="Observations", xlabel="Species")
    ax.set_ylim(0, max(counts) * 1.2)
    for index, count in enumerate(counts):
        ax.text(index, count + 1, str(count), ha="center")
    fig.tight_layout()
    fig.savefig(output / "class_distribution.png")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.5, 5))
    for species, color in zip(CLASSES, ["#2a9d8f", "#d4a017", "#e76f51"]):
        subset = data.loc[data[TARGET] == species]
        ax.scatter(subset["PetalLengthCm"], subset["PetalWidthCm"], label=species.removeprefix("Iris-"), color=color, alpha=0.75, edgecolor="white", linewidth=0.4)
    ax.set(title="Descriptive view of supplied Iris measurements", xlabel="Petal length (cm)", ylabel="Petal width (cm)")
    ax.legend(title="Species")
    fig.tight_layout()
    fig.savefig(output / "petal_measurements.png")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    display = ConfusionMatrixDisplay(
        confusion_matrix=np.array(metrics["test"]["confusion_matrix"]),
        display_labels=[name.removeprefix("Iris-") for name in CLASSES],
    )
    display.plot(ax=ax, cmap="Blues", colorbar=False, values_format="d")
    ax.set_title(f"Held-out confusion matrix: {metrics['selected_model']}")
    fig.tight_layout()
    fig.savefig(output / "confusion_matrix.png")
    plt.close(fig)


def create_summary(metrics: dict, audit: dict) -> str:
    test = metrics["test"]
    split = metrics["split"]
    errors = split["test_rows"] - sum(np.diag(test["confusion_matrix"]))
    rows = [
        "# Iris flower classification: results and design report",
        "",
        "## Objective",
        "Classify Iris setosa, versicolor, and virginica using four flower measurements in centimetres. This is an educational supervised learning exercise.",
        "",
        "## Data and provenance",
        f"The user supplied `data/Iris.csv`: {audit['rows']} observations, 50 per species. There are no missing values or duplicate complete rows; Id distinguishes records. There are {audit['duplicate_measurement_rows']} repeated measurement-and-label rows and {audit['unique_measurement_groups']} unique measurement groups. No measurement group has conflicting labels. The Id identifier is excluded from predictors.",
        "The assignment links to https://www.kaggle.com/datasets/saurabh00007/iriscsv. The actual input is the user-uploaded CSV, not a fresh download from that page. Collection details, independence of observations, and redistribution license were not independently established. The file is retained as supplied; no license is asserted.",
        "",
        "## Method and evaluation design",
        f"Seed {SEED}; the first fold from a five-fold shuffled StratifiedGroupKFold defines the held-out set. This produces {split['train_rows']} training and {split['test_rows']} test rows. Identical measurement groups stay together. Stratification is approximate under group constraints.",
        "Model families and grids were fixed in code before evaluation. A most-frequent baseline, standardized logistic regression, standardized k-nearest neighbours, and standardized radial-basis SVM are compared with five-fold group-aware cross-validation on training data only. Scaling is fit within each training fold. Mean macro F1 selects hyperparameters, with grid order breaking ties within a model. The model with highest best CV macro F1 is selected; mean CV accuracy and alphabetical model name break model-level ties. The selected estimator is refit on the training partition, then the held-out set is evaluated once. The baseline test result is reported for context; no model is chosen using test performance.",
        "",
        "## Results",
        "| Candidate | Best mean CV macro F1 | CV standard deviation | Best mean CV accuracy |",
        "|---|---:|---:|---:|",
    ]
    for item in metrics["model_selection"]:
        rows.append(f"| {item['model']} | {item['mean_cv_macro_f1']:.4f} | {item['std_cv_macro_f1']:.4f} | {item['mean_cv_accuracy']:.4f} |")
    rows.extend([
        "",
        f"Selected **{metrics['selected_model']}**, parameters `{json.dumps(metrics['selected_parameters'], sort_keys=True)}`. Held-out accuracy **{test['accuracy']:.4f}** and macro F1 **{test['macro_f1']:.4f}**, with {int(errors)} misclassified observations out of {split['test_rows']}. Baseline held-out accuracy is {metrics['baseline_test']['accuracy']:.4f} and macro F1 is {metrics['baseline_test']['macro_f1']:.4f}.",
        "",
        "| Species | Test support | Precision | Recall | F1 |",
        "|---|---:|---:|---:|---:|",
    ])
    for name in CLASSES:
        report = test["classification_report"][name]
        rows.append(f"| {name} | {int(report['support'])} | {report['precision']:.4f} | {report['recall']:.4f} | {report['f1-score']:.4f} |")
    rows.extend([
        "",
        "The descriptive petal plot shows strong setosa separation and greater overlap between versicolor and virginica. The confusion matrix and `test_predictions.csv` identify the observed held-out errors. These plots summarize the supplied data and held-out predictions; they do not establish causal feature effects.",
        "",
        "## Limitations",
        "A small, balanced educational dataset and one held-out split provide a noisy estimate of performance. A high score is not evidence of production readiness or performance on new locations, instruments, or flower populations. Hyperparameter selection adds training-set selection uncertainty. Grouping identical measurement vectors reduces direct duplicate leakage but cannot identify unrecorded relationships between flowers. Species labels and measurements have not been externally verified. No unseen external dataset or deployment testing was performed.",
        "",
        "## Reproducibility",
        "Run `python analysis.py`, then `python -m unittest discover -s tests -v`. The notebook calls the same pipeline. `metrics.json` records versions, split sizes, class counts, parameters, and complete test metrics; `split_assignments.csv` records every row's split and feature group; `cv_results.csv` records all tried configurations. The selected estimator is evaluated after fitting on training data only; it is not refit on the held-out observations.",
        "",
    ])
    return "\n".join(rows)


def main(argv: list[str] | None = None) -> dict:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "data" / "Iris.csv", help="Source CSV; default is anchored to this project.")
    parser.add_argument("--output", type=Path, default=ROOT / "outputs", help="Output folder; default is anchored to this project.")
    args = parser.parse_args(argv)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    data, groups, audit = load_and_audit(args.data.resolve())
    write_json(output / "data_audit.json", audit)
    train, test = split_indices(data, groups)
    X_train, X_test = data.iloc[train][FEATURES], data.iloc[test][FEATURES]
    y_train, y_test = data.iloc[train][TARGET], data.iloc[test][TARGET]
    train_groups = groups[train]
    cv = list(StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=SEED).split(X_train, y_train, train_groups))
    cv_audit = []
    for fold, (fit_rows, validation_rows) in enumerate(cv, start=1):
        if set(train_groups[fit_rows]) & set(train_groups[validation_rows]):
            raise AssertionError("Feature groups overlap within a CV fold.")
        cv_audit.append({"fold": fold, "training_rows": int(len(fit_rows)), "validation_rows": int(len(validation_rows)), "overlapping_groups": 0})
    selection = []
    all_results = []
    fitted = {}
    for name, (pipeline, grid) in candidate_models().items():
        search = GridSearchCV(
            pipeline, grid, scoring={"macro_f1": "f1_macro", "accuracy": "accuracy"},
            refit="macro_f1", cv=cv, n_jobs=1, error_score="raise", return_train_score=False,
        )
        search.fit(X_train, y_train)
        best = search.best_index_
        result = {
            "model": name,
            "mean_cv_macro_f1": float(search.cv_results_["mean_test_macro_f1"][best]),
            "std_cv_macro_f1": float(search.cv_results_["std_test_macro_f1"][best]),
            "mean_cv_accuracy": float(search.cv_results_["mean_test_accuracy"][best]),
            "parameters": search.best_params_,
        }
        selection.append(result)
        fitted[name] = search.best_estimator_
        for index, params in enumerate(search.cv_results_["params"]):
            all_results.append({
                "model": name, "parameters": json.dumps(params, sort_keys=True),
                "mean_cv_macro_f1": float(search.cv_results_["mean_test_macro_f1"][index]),
                "std_cv_macro_f1": float(search.cv_results_["std_test_macro_f1"][index]),
                "mean_cv_accuracy": float(search.cv_results_["mean_test_accuracy"][index]),
            })
    selection.sort(key=lambda item: (-item["mean_cv_macro_f1"], -item["mean_cv_accuracy"], item["model"]))
    winner = selection[0]
    prediction = fitted[winner["model"]].predict(X_test)
    baseline_prediction = fitted["dummy_most_frequent"].predict(X_test)
    metrics = {
        "seed": SEED,
        "versions": {"python": __import__("platform").python_version(), "numpy": np.__version__, "pandas": pd.__version__, "scikit_learn": sklearn.__version__, "matplotlib": matplotlib.__version__},
        "features": FEATURES,
        "class_order": CLASSES,
        "split": {
            "method": "First fold of StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)",
            "train_rows": int(len(train)), "test_rows": int(len(test)),
            "train_unique_groups": int(np.unique(groups[train]).size),
            "test_unique_groups": int(np.unique(groups[test]).size),
            "overlapping_groups": 0,
            "train_class_counts": {name: int(value) for name, value in y_train.value_counts().sort_index().items()},
            "test_class_counts": {name: int(value) for name, value in y_test.value_counts().sort_index().items()},
        },
        "cv_folds": cv_audit,
        "model_selection": selection,
        "selected_model": winner["model"],
        "selected_parameters": winner["parameters"],
        "test": evaluate(y_test, prediction),
        "baseline_test": evaluate(y_test, baseline_prediction),
    }
    write_json(output / "metrics.json", metrics)
    pd.DataFrame(all_results).to_csv(output / "cv_results.csv", index=False)
    assignments = data.copy()
    assignments.insert(0, "row_index", np.arange(len(data)))
    assignments["measurement_group"] = groups
    assignments["split"] = "train"
    assignments.loc[test, "split"] = "test"
    assignments.to_csv(output / "split_assignments.csv", index=False)
    predictions = data.iloc[test].copy()
    predictions.insert(0, "row_index", test)
    predictions["predicted_species"] = prediction
    predictions["correct"] = y_test.to_numpy() == prediction
    predictions.to_csv(output / "test_predictions.csv", index=False)
    (output / "summary.md").write_text(create_summary(metrics, audit), encoding="utf-8")
    save_plots(data, metrics, output)
    print(f"Selected: {winner['model']}; test accuracy={metrics['test']['accuracy']:.4f}; macro F1={metrics['test']['macro_f1']:.4f}")
    print(f"Outputs: {output}")
    return metrics


if __name__ == "__main__":
    main()
