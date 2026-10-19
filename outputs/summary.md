# Iris flower classification: results and design report

## Objective
Classify Iris setosa, versicolor, and virginica using four flower measurements in centimetres. This is an educational supervised learning exercise.

## Data and provenance
The user supplied `data/Iris.csv`: 150 observations, 50 per species. There are no missing values or duplicate complete rows; Id distinguishes records. There are 3 repeated measurement-and-label rows and 147 unique measurement groups. No measurement group has conflicting labels. The Id identifier is excluded from predictors.
The assignment links to https://www.kaggle.com/datasets/saurabh00007/iriscsv. The actual input is the user-uploaded CSV, not a fresh download from that page. Collection details, independence of observations, and redistribution license were not independently established. The file is retained as supplied; no license is asserted.

## Method and evaluation design
Seed 42; the first fold from a five-fold shuffled StratifiedGroupKFold defines the held-out set. This produces 120 training and 30 test rows. Identical measurement groups stay together. Stratification is approximate under group constraints.
Model families and grids were fixed in code before evaluation. A most-frequent baseline, standardized logistic regression, standardized k-nearest neighbours, and standardized radial-basis SVM are compared with five-fold group-aware cross-validation on training data only. Scaling is fit within each training fold. Mean macro F1 selects hyperparameters, with grid order breaking ties within a model. The model with highest best CV macro F1 is selected; mean CV accuracy and alphabetical model name break model-level ties. The selected estimator is refit on the training partition, then the held-out set is evaluated once. The baseline test result is reported for context; no model is chosen using test performance.

## Results
| Candidate | Best mean CV macro F1 | CV standard deviation | Best mean CV accuracy |
|---|---:|---:|---:|
| logistic_regression | 0.9666 | 0.0312 | 0.9667 |
| knn | 0.9582 | 0.0264 | 0.9583 |
| rbf_svm | 0.9582 | 0.0264 | 0.9583 |
| dummy_most_frequent | 0.1667 | 0.0000 | 0.3333 |

Selected **logistic_regression**, parameters `{"classifier__C": 10.0}`. Held-out accuracy **1.0000** and macro F1 **1.0000**, with 0 misclassified observations out of 30. Baseline held-out accuracy is 0.3333 and macro F1 is 0.1667.

| Species | Test support | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Iris-setosa | 10 | 1.0000 | 1.0000 | 1.0000 |
| Iris-versicolor | 10 | 1.0000 | 1.0000 | 1.0000 |
| Iris-virginica | 10 | 1.0000 | 1.0000 | 1.0000 |

The descriptive petal plot shows strong setosa separation and greater overlap between versicolor and virginica. The confusion matrix and `test_predictions.csv` identify the observed held-out errors. These plots summarize the supplied data and held-out predictions; they do not establish causal feature effects.

## Limitations
A small, balanced educational dataset and one held-out split provide a noisy estimate of performance. A high score is not evidence of production readiness or performance on new locations, instruments, or flower populations. Hyperparameter selection adds training-set selection uncertainty. Grouping identical measurement vectors reduces direct duplicate leakage but cannot identify unrecorded relationships between flowers. Species labels and measurements have not been externally verified. No unseen external dataset or deployment testing was performed.

## Reproducibility
Run `python analysis.py`, then `python -m unittest discover -s tests -v`. The notebook calls the same pipeline. `metrics.json` records versions, split sizes, class counts, parameters, and complete test metrics; `split_assignments.csv` records every row's split and feature group; `cv_results.csv` records all tried configurations. The selected estimator is evaluated after fitting on training data only; it is not refit on the held-out observations.
