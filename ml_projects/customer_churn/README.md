# Customer Churn Prediction (End-to-End ML Pipeline)

Predict whether a customer will churn using structured customer and account data.

This project demonstrates a **production-minded machine learning workflow**:

**EDA → preprocessing → model training & evaluation → model persistence → CLI-based batch inference**

---

## 📌 Project Highlights

- Built a complete churn prediction pipeline with clean separation between:
  - Data preparation
  - Modeling
  - Inference
- Addressed class imbalance with appropriate evaluation metrics:
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix
- Persisted trained models using **joblib**
- Implemented a **CLI-based batch inference script** (`predict.py`)

---

## 📁 Repository Structure

```text
customer_churn/
├── churn_part1_eda.ipynb
├── churn_part2_preprocessing.ipynb
├── churn_part3_modeling.ipynb
├── predict.py
├── models/
│ └── customer_churn_rf.joblib
└── README.md
```

---

## 📊 Datasets

Stored in: `ml_projects/data/`

- `customer_churn.csv` — raw dataset
- `customer_churn_cleaned.csv` — cleaned dataset
- `customer_churn_preprocessed.csv` — final model-ready features

---

## 🎯 Problem Definition

- **Goal:** Identify customers likely to churn so a business can prioritize retention strategies
- **Target column:** `Churn` (binary classification)

---

## 🔄 Workflow

### 1️⃣ Exploratory Data Analysis  
**Notebook:** `churn_part1_eda.ipynb`

- Basic inspection and missing value checks
- Target distribution (churn vs non-churn)
- Feature-level analysis (categorical and numeric)
- Initial observations on potential drivers of churn

---

### 2️⃣ Preprocessing  
**Notebook:** `churn_part2_preprocessing.ipynb`

- Cleaned data and standardized column formats
- Encoded categorical variables
- Scaled numeric variables where required
- Exported final feature matrix:

---

`ml_projects/data/customer_churn_preprocessed.csv/`

---

### 3️⃣ Modeling  
**Notebook:** `churn_part3_modeling.ipynb`

#### Models Trained

- Logistic Regression (baseline)
- Random Forest (non-linear model)

#### Evaluation Metrics

- Precision
- Recall
- F1-score
- Confusion Matrix

#### Saved Model Artifact

`models/customer_churn_rf.joblib`

---

## 📈 Results

### Logistic Regression

- **Precision:** 0.7887
- **Recall:** 0.8763
- **F1-score:** 0.8302

### Random Forest

- **Precision:** 0.8456
- **Recall:** 0.8522
- **F1-score:** 0.8489

✅ **Conclusion:**  
Random Forest performed better overall (higher Recall and F1-score), making it more suitable for **retention-focused churn prediction** use cases.

---

## 🖥️ Batch Inference (CLI)

Run predictions on a CSV containing the same features used during training.

> If the input file contains the `Churn` column, the script automatically drops it.

### Run from repository root:

```bash
python ml_projects/customer_churn/predict.py \
  --input ml_projects/data/customer_churn_preprocessed.csv \
  --output ml_projects/customer_churn/predictions.csv \
  --model ml_projects/customer_churn/models/customer_churn_rf.joblib
```

### Output

- `ml_projects/customer_churn/predictions.csv`
- Includes an additional column:
  - `churn_prediction`

---

## 🧠 Tools & Technologies

- **Python**
- **Pandas**, **NumPy**
- **scikit-learn**
- **SMOTE** (imbalanced-learn)
- **Jupyter Notebooks**
- **joblib**
- **Git / GitHub**

