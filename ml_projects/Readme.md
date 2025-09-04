# ML Projects

This folder contains my **learning + demo projects** for data analysis and machine learning.  
Each notebook builds on the previous one, showing a step-by-step workflow from raw data to a trained model.

---

## Project: Iris Dataset (Step-by-Step)

### 1. `pandas_intro.ipynb`
- Load the Iris dataset into Pandas
- Explore dataset with `.head()`, `.info()`, `.describe()`
- Groupby examples
- Basic histograms & scatterplots

### 2. `pandas_intro_part2.ipynb`
- Handle **missing values** (drop vs mean imputation)
- Add **feature engineering**: sepal_area, petal_area
- Apply **scaling** (StandardScaler)
- Extra plots: boxplot & scatter
- Demonstrate **joins/merges** with employees/departments demo tables
- Save a cleaned dataset: `iris_cleaned_engineered.csv`

### 3. `pandas_intro_part3.ipynb`
- Train/test split
- Train a **Logistic Regression classifier**
- Evaluate with **accuracy** and **confusion matrix**
- Inspect **coefficients/feature importance**

### 4. `pandas_intro_part4.ipynb`
- Compare **RandomForestClassifier** vs **GradientBoostingClassifier**
- Use **GridSearchCV** with Macro-F1 scoring
- Evaluate on test set (accuracy + F1 + confusion matrices)
- Plot **feature importances**
- Save the best model → `ml_projects/models/best_model.joblib`

---

## What this shows
- Strong **data wrangling with Pandas**
- Ability to **handle missing data, feature engineering, scaling**
- Experience with **ML pipelines** (sklearn)
- Understanding of **evaluation metrics** (accuracy, F1, confusion matrix)
- End-to-end workflow: **EDA → preprocessing → modeling → saving model**
