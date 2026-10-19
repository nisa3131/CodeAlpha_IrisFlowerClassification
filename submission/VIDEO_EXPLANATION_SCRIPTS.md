# Video explanation prompts

Draft scripts for the user to review, understand and record. Each is approximately 60–90 seconds at a natural speaking pace. Show the matching GitHub repository, notebook, one main chart and the measured results while speaking. Adapt the wording to your understanding; do not claim methods or findings you cannot explain. No videos have been recorded or posted.

## Task 1 — Iris Flower Classification

“This is my CodeAlpha Iris Flower Classification project. The goal is to identify setosa, versicolor or virginica from sepal length, sepal width, petal length and petal width.

The supplied dataset contains 150 flowers, with 50 examples per species. I excluded the ID because it is an identifier, not a flower measurement. I also kept identical measurement groups together when separating training and test data, which helps prevent repeated observations from leaking across the split.

There are 120 training rows and 30 held-out test rows. I compared a simple baseline, logistic regression, nearest neighbours and an SVM using five-fold cross-validation on training data only. Scaling was fitted within each training fold.

Logistic regression was selected using cross-validation. On the held-out test, it correctly classified all 30 flowers, giving 100% accuracy and a macro F1 score of one. This confusion matrix shows ten correct predictions for each species.

The main limitation is the small educational dataset: a perfect score here does not guarantee performance on flowers from new locations or measuring equipment. The repository includes the source code, executed notebook, dataset, charts and report.”

Repository: https://github.com/nisa3131/CodeAlpha_IrisFlowerClassification

## Task 2 — Unemployment Analysis with Python

“This is my CodeAlpha unemployment analysis. I used Python to clean, explore and visualize the two supplied Indian unemployment datasets.

The historical file contains 740 valid state-and-area observations from May 2019 to June 2020 after removing fully blank rows. The other file contains 267 state observations from January to October 2020. I kept the datasets separate because their observation units differ. I cleaned column names and dates, checked missing values and duplicate keys, and never filled missing unemployment rates with zero.

This is descriptive analysis, so I did not train a prediction model. To make period comparisons consistent, I used the same 25 complete states and territories in every period.

Their unweighted mean unemployment rate rose from 9.20% in January to March to 23.20% in April and May, then fell to 8.90% in August to October. Participation also fell, which matters when interpreting recovery. I also examined regional patterns and matched rural and urban observations.

These are equal-state averages, not official population-weighted national estimates. The timing is associated with Covid disruption but does not prove causation. The short historical series also cannot establish recurring seasonality. The repository contains reproducible code, coverage checks, tables, charts and a detailed report.”

Repository: https://github.com/nisa3131/CodeAlpha_UnemploymentAnalysis

## Task 3 — Car Price Prediction

“This is my CodeAlpha car-price prediction project. The supplied file also includes motorcycles and scooters, so the analysis describes used vehicles rather than cars alone.

After removing two exact duplicates, 299 records remained. I used the supplied price, mileage, fuel, transmission and ownership fields, and calculated vehicle age using the dataset's maximum year, 2018. I did not invent horsepower or present-day vehicle ages.

To make evaluation stricter, I separated data by vehicle-name groups. The 70 test records contain vehicle models whose names never appear in training. I used five-fold group cross-validation on the remaining 229 rows, fitting imputation, scaling and categorical encoding inside the training folds.

A random forest was selected from the candidate models. On the held-out groups, its mean absolute error was 2.0562 in dataset price units, with R-squared of 0.5839. That is a 41.2% reduction in absolute error compared with a median-price baseline.

The test error was higher than cross-validation error, showing uncertainty when moving to unseen vehicle models. The file is small and historical, and its currency, location and collection date were not verified. This is an educational prediction workflow, not a current-market valuation service. The repository includes the notebook, predictions, charts, validation checks and report.”

Repository: https://github.com/nisa3131/CodeAlpha_CarPricePrediction

## Task 4 — Sales Prediction

“This is my CodeAlpha sales-prediction project. I used 200 supplied observations of TV, radio and newspaper advertising measurements with sales as the target.

I removed the sequential row identifier from the predictors and checked missing values and duplicates. A fixed split reserved 40 observations for the final test, leaving 160 for training. All preprocessing and candidate comparisons used five-fold cross-validation on training data only.

I compared six candidate pipelines. Quadratic ridge regression had the lowest cross-validation root mean squared error, so it was selected before looking at final test results. On the held-out set, mean absolute error was 0.485, root mean squared error was 0.621 and R-squared was 0.988, all reported in the dataset's observed units.

The analysis found stronger conditional linear associations for TV and radio than newspaper in the training sample. I also explored hypothetical input changes, but these predictions do not prove that changing advertising spend causes the same sales change.

There are no dates, customer segments or verified currency units. This therefore predicts sales conditional on the measured inputs; it is not a validated future-period forecast or a guaranteed return-on-investment estimate. A useful business next step would be properly measured channel experiments. The repository contains code, the executed notebook, held-out predictions, charts and the design report.”

Repository: https://github.com/nisa3131/CodeAlpha_SalesPrediction
