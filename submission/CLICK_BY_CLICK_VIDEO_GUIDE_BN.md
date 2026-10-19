# চারটি প্রজেক্টের ভিডিও: কোন পেজ দেখাবে, কী বলবে

এটি Windows ল্যাপটপে স্ক্রিন রেকর্ডিং করার জন্য বাংলা নির্দেশনা এবং ইংরেজি বলার কথা। প্রতিটি প্রজেক্টের জন্য আলাদা ভিডিও বানাতে পারো। এই গাইড কোনো ভিডিও রেকর্ড বা পোস্ট করে না।

## প্রতিবার রেকর্ড করার আগে

1. একটি প্রজেক্টের নিচের পাঁচটি লিঙ্কে Right-click → Open link in new tab দিয়ে পাঁচটি ট্যাব খোলো। একবারে একটি প্রজেক্ট নিয়েই কাজ করো।
2. এই গাইডটি মোবাইলে বা কাগজে পাশে রাখো। স্ক্রিনে করো অংশটি তোমার কাজ; বলো অংশটি ভিডিওতে পড়ার ইংরেজি কথা।
3. প্রথম ট্যাব খোলো। Windows + G → Capture থেকে microphone চালু আছে কি না দেখো। Windows + Alt + R দিয়ে রেকর্ডিং শুরু করো।
4. নিচের ধাপ 1 থেকে 5 পর্যন্ত ট্যাব বদলে দেখাও এবং সংশ্লিষ্ট ইংরেজি কথাগুলো বলো। প্রয়োজন হলে ধীরে স্ক্রল করো। স্ক্রিপ্ট নিজের বোঝাপড়ার সঙ্গে মিলিয়ে বলবে।
5. শেষ হলে Windows + Alt + R দিয়ে বন্ধ করো। সাধারণত Videos → Captures-এ MP4 পাওয়া যায়। শব্দ ও স্ক্রিন দেখে নাও। প্রথমবার 10 সেকেন্ডের একটি টেস্ট করে নেওয়া ভালো।

## ভিডিও 1: Iris Flower Classification

### ধাপ 1: পরিচয়ের পেজ

**ক্লিক করো:** [পরিচয়ের পেজ](https://github.com/nisa3131/CodeAlpha_IrisFlowerClassification/blob/main/README.md)

**স্ক্রিনে করো:** README-তে প্রজেক্টের নাম দেখাও।

**বলো:**

> Hello, this is my CodeAlpha Iris Flower Classification project. The goal is to identify three Iris species using sepal and petal measurements.

### ধাপ 2: ডেটার টেবিল

**ক্লিক করো:** [ডেটার টেবিল](https://github.com/nisa3131/CodeAlpha_IrisFlowerClassification/blob/main/data/Iris.csv)

**স্ক্রিনে করো:** টেবিলে ফুলের মাপ এবং Species কলাম দেখাও।

**বলো:**

> The dataset contains 150 flowers, with 50 examples of each species. I used four flower measurements as inputs and excluded the ID column from the predictors.

### ধাপ 3: মডেল তৈরির কোড

**ক্লিক করো:** [মডেল তৈরির কোড](https://github.com/nisa3131/CodeAlpha_IrisFlowerClassification/blob/main/analysis.py#L220-L240)

**স্ক্রিনে করো:** লিঙ্কে যে কোডের অংশটি হাইলাইট হবে, সেটি দেখাও।

**বলো:**

> I used 120 flowers for training and 30 for testing. Identical measurement groups were kept together to reduce data leakage. I compared several models using cross-validation on the training data only.

### ধাপ 4: ফলাফলের টেবিল

**ক্লিক করো:** [ফলাফলের টেবিল](https://github.com/nisa3131/CodeAlpha_IrisFlowerClassification/blob/main/outputs/summary.md#results)

**স্ক্রিনে করো:** Results অংশে নির্বাচিত মডেল ও accuracy দেখাও; প্রয়োজন হলে একটু নিচে স্ক্রল করো।

**বলো:**

> Logistic regression was selected through cross-validation. On the held-out test set, it achieved 100 percent accuracy and a macro F1 score of one.

### ধাপ 5: Confusion matrix ছবিটি

**ক্লিক করো:** [Confusion matrix ছবিটি](https://github.com/nisa3131/CodeAlpha_IrisFlowerClassification/blob/main/outputs/confusion_matrix.png)

**স্ক্রিনে করো:** ছবির তির্যক লাইনের তিনটি 10 দেখাও, তারপর শেষ কথাটি বলো।

**বলো:**

> This confusion matrix shows ten correct predictions for each species. This is a small educational dataset, so the result does not guarantee performance on new data. The code, notebook and report are available in the repository. Thank you.

**শেষে:** Windows + Alt + R চাপো। ফাইলের নাম দিতে পারো: Task1_Iris_Explanation.mp4। পুরো ভিডিওটি দেখে শব্দ ও লেখা বোঝা যাচ্ছে কি না যাচাই করো।

## ভিডিও 2: Unemployment Analysis

### ধাপ 1: পরিচয়ের পেজ

**ক্লিক করো:** [পরিচয়ের পেজ](https://github.com/nisa3131/CodeAlpha_UnemploymentAnalysis/blob/main/README.md)

**স্ক্রিনে করো:** README-তে প্রজেক্টের নাম দেখাও।

**বলো:**

> Hello, this is my CodeAlpha Unemployment Analysis project. I used Python to clean unemployment data, visualize trends and describe changes around the Covid period.

### ধাপ 2: ডেটার টেবিল

**ক্লিক করো:** [ডেটার টেবিল](https://github.com/nisa3131/CodeAlpha_UnemploymentAnalysis/blob/main/data/Unemployment_Rate_upto_11_2020.csv)

**স্ক্রিনে করো:** Region, Date এবং unemployment rate-এর কলামগুলো দেখাও।

**বলো:**

> I used two datasets. One contains rural and urban observations, while the other contains state observations for January to October 2020. I kept them separate because their observation units differ.

### ধাপ 3: ডেটা পরিষ্কারের কোড

**ক্লিক করো:** [ডেটা পরিষ্কারের কোড](https://github.com/nisa3131/CodeAlpha_UnemploymentAnalysis/blob/main/analysis.py#L45-L70)

**স্ক্রিনে করো:** blank row বাদ দেওয়া, column name ও date পরিষ্কারের কোড দেখাও।

**বলো:**

> I cleaned column names and dates, removed fully blank rows and checked the data for missing values and duplicate records. I did not replace missing unemployment rates with zero.

### ধাপ 4: ফলাফলের অংশ

**ক্লিক করো:** [ফলাফলের অংশ](https://github.com/nisa3131/CodeAlpha_UnemploymentAnalysis/blob/main/outputs/summary.md#results)

**স্ক্রিনে করো:** Results অংশে 9.20%, 23.20% এবং 8.90% লেখা দেখাও।

**বলো:**

> For the same 25 states and territories, the unweighted average unemployment rate rose from 9.20 percent in January to March to 23.20 percent in April and May. It later fell to 8.90 percent in August to October. These are equal-state averages, not official national rates.

### ধাপ 5: Rural–Urban তুলনার চার্ট

**ক্লিক করো:** [Rural–Urban তুলনার চার্ট](https://github.com/nisa3131/CodeAlpha_UnemploymentAnalysis/blob/main/outputs/charts/rural_urban_period_comparison.png)

**স্ক্রিনে করো:** Rural ও Urban-এর বারগুলো দেখাও, তারপর সীমাবদ্ধতা বলে শেষ করো।

**বলো:**

> This chart compares matched rural and urban unemployment rates. Urban rates were higher in these comparisons. The findings support monitoring unemployment and labour participation together. This descriptive analysis does not prove what caused the changes. Thank you.

**শেষে:** Windows + Alt + R চাপো। ফাইলের নাম দিতে পারো: Task2_Unemployment_Explanation.mp4। পুরো ভিডিওটি দেখে শব্দ ও লেখা বোঝা যাচ্ছে কি না যাচাই করো।

## ভিডিও 3: Car Price Prediction

### ধাপ 1: পরিচয়ের পেজ

**ক্লিক করো:** [পরিচয়ের পেজ](https://github.com/nisa3131/CodeAlpha_CarPricePrediction/blob/main/README.md)

**স্ক্রিনে করো:** README-তে প্রজেক্টের নাম দেখাও।

**বলো:**

> Hello, this is my CodeAlpha Car Price Prediction project. The goal is to predict selling prices from historical vehicle features. The supplied data include cars and two-wheelers.

### ধাপ 2: ডেটার টেবিল

**ক্লিক করো:** [ডেটার টেবিল](https://github.com/nisa3131/CodeAlpha_CarPricePrediction/blob/main/data/car%20data.csv)

**স্ক্রিনে করো:** Year, Selling_Price, Present_Price, Driven_kms ও Fuel_Type কলাম দেখাও।

**বলো:**

> The original dataset contains 301 records. After removing two exact duplicates, 299 records remained. Inputs include vehicle age, present price, distance driven, fuel type and other vehicle attributes.

### ধাপ 3: মডেল তৈরির কোড

**ক্লিক করো:** [মডেল তৈরির কোড](https://github.com/nisa3131/CodeAlpha_CarPricePrediction/blob/main/analysis.py#L253-L282)

**স্ক্রিনে করো:** group split এবং model comparison-এর কোড দেখাও।

**বলো:**

> I used 229 records for training and 70 for testing. Vehicle-name groups were kept separate, so the test measures performance on unseen vehicle models. Candidate models were compared using training-only cross-validation.

### ধাপ 4: ফলাফলের টেবিল

**ক্লিক করো:** [ফলাফলের টেবিল](https://github.com/nisa3131/CodeAlpha_CarPricePrediction/blob/main/outputs/summary.md#held-out-results)

**স্ক্রিনে করো:** random_forest সারির MAE, RMSE ও R-squared দেখাও।

**বলো:**

> Random forest was selected. On the held-out test, mean absolute error was about 2.06 in dataset price units, and R-squared was about 0.584. It reduced mean absolute error by 41.2 percent compared with the median baseline.

### ধাপ 5: Prediction ও residual-এর চার্ট

**ক্লিক করো:** [Prediction ও residual-এর চার্ট](https://github.com/nisa3131/CodeAlpha_CarPricePrediction/blob/main/outputs/charts/heldout_predictions_and_residuals.png)

**স্ক্রিনে করো:** actual বনাম predicted price এবং error-এর চার্ট দেখাও।

**বলো:**

> These charts compare actual and predicted prices and show prediction errors. The small historical sample limits the results, so this is not a current-market valuation service. The code, notebook and report are available in the repository. Thank you.

**শেষে:** Windows + Alt + R চাপো। ফাইলের নাম দিতে পারো: Task3_CarPrice_Explanation.mp4। পুরো ভিডিওটি দেখে শব্দ ও লেখা বোঝা যাচ্ছে কি না যাচাই করো।

## ভিডিও 4: Sales Prediction

### ধাপ 1: পরিচয়ের পেজ

**ক্লিক করো:** [পরিচয়ের পেজ](https://github.com/nisa3131/CodeAlpha_SalesPrediction/blob/main/README.md)

**স্ক্রিনে করো:** README-তে প্রজেক্টের নাম দেখাও।

**বলো:**

> Hello, this is my CodeAlpha Sales Prediction project. The goal is to predict sales from TV, radio and newspaper advertising measurements using regression models.

### ধাপ 2: ডেটার টেবিল

**ক্লিক করো:** [ডেটার টেবিল](https://github.com/nisa3131/CodeAlpha_SalesPrediction/blob/main/data/Advertising.csv)

**স্ক্রিনে করো:** TV, Radio, Newspaper এবং Sales কলাম দেখাও।

**বলো:**

> The dataset contains 200 observations. I used TV, radio and newspaper as predictors, with sales as the target. The sequential row identifier was excluded from the model.

### ধাপ 3: মডেল তৈরির কোড

**ক্লিক করো:** [মডেল তৈরির কোড](https://github.com/nisa3131/CodeAlpha_SalesPrediction/blob/main/analysis.py#L178-L209)

**স্ক্রিনে করো:** train/test split এবং cross-validation-এর কোড দেখাও।

**বলো:**

> I reserved 40 observations for testing and used 160 for training. Six candidate pipelines were compared using five-fold cross-validation on training data only. Preprocessing was fitted within each training fold.

### ধাপ 4: ফলাফলের টেবিল

**ক্লিক করো:** [ফলাফলের টেবিল](https://github.com/nisa3131/CodeAlpha_SalesPrediction/blob/main/outputs/summary.md#held-out-results)

**স্ক্রিনে করো:** Quadratic ridge সারির MAE, RMSE ও R-squared দেখাও।

**বলো:**

> Quadratic ridge regression was selected. On the held-out test, mean absolute error was 0.485, root mean squared error was 0.621 and R-squared was 0.988.

### ধাপ 5: Advertising association-এর চার্ট

**ক্লিক করো:** [Advertising association-এর চার্ট](https://github.com/nisa3131/CodeAlpha_SalesPrediction/blob/main/outputs/charts/04_linear_association_coefficients.png)

**স্ক্রিনে করো:** TV, Radio ও Newspaper-এর বারগুলো দেখাও, তারপর সীমাবদ্ধতা বলে শেষ করো।

**বলো:**

> This linear reference chart shows stronger conditional associations for TV and radio than newspaper in the training sample. It does not prove that changing advertising spend causes a sales change. The data contain no dates, so this is not a validated future forecast. Thank you.

**শেষে:** Windows + Alt + R চাপো। ফাইলের নাম দিতে পারো: Task4_Sales_Explanation.mp4। পুরো ভিডিওটি দেখে শব্দ ও লেখা বোঝা যাচ্ছে কি না যাচাই করো।

## রেকর্ডিং শেষে

নির্বাচিত প্রজেক্টের MP4 ভিডিও LinkedIn পোস্টে যুক্ত করো এবং সেই প্রজেক্টের GitHub লিঙ্ক দাও। internship-status পোস্টে সঠিক CodeAlpha পেজ tag করো। অফিসিয়াল submission form-এ যা চাওয়া হবে, সেই লিঙ্ক ও ফাইল দেবে। প্রদত্ত PDF যেকোনো 2 বা 3টি টাস্ক অনুমোদন করে; চারটিই প্রস্তুত আছে। ফর্মের প্রকৃত নির্দেশনা অনুসরণ করো। দেওয়া নথিতে নির্দিষ্ট ভিডিও দৈর্ঘ্য, form URL বা deadline নেই।
