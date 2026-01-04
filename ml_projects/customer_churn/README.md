# Customer Churn Prediction (End-to-End ML Pipeline)

Predict whether a customer will churn using structured customer/account data.  
This project demonstrates a **production-minded ML workflow**: EDA → preprocessing → model training/evaluation → model persistence → CLI-based batch inference.

---

## Project Highlights
- Built a complete churn prediction pipeline with **clean separation** between data prep, modeling, and inference
- Addressed **class imbalance** with appropriate evaluation (Precision/Recall/F1 + Confusion Matrix)
- Persisted trained model (`joblib`) and created a **CLI inference script** (`predict.py`) for batch predictions

---


## Repository Structure

customer_churn/
├── churn_part1_eda.ipynb
├── churn_part2_preprocessing.ipynb
├── churn_part3_modeling.ipynb
├── predict.py
├── models/
│ └── customer_churn_rf.joblib
└── README.md


**Datasets (stored in `ml_projects/data/`):**
- `customer_churn.csv` (raw)
- `customer_churn_cleaned.csv` (cleaned)
- `customer_churn_preprocessed.csv` (final model-ready features)

---

## Problem & Target
- **Goal:** Identify customers likely to churn so a business can prioritize retention
- **Target column:** `Churn` (binary)

---

## Workflow

### 1) EDA — `churn_part1_eda.ipynb`
- Basic inspection, missingness checks
- Target distribution (churn vs non-churn)
- Feature-level analysis (categorical + numeric)
- Notes on potential drivers of churn

### 2) Preprocessing — `churn_part2_preprocessing.ipynb`
- Cleaned data and standardized column formats
- Encoded categorical variables
- Scaled numeric variables when needed
- Exported final feature table:
  - `ml_projects/data/customer_churn_preprocessed.csv`

### 3) Modeling — `churn_part3_modeling.ipynb`
Trained and evaluated:
- **Logistic Regression** (baseline)
- **Random Forest** (non-linear model)

Evaluated using:
- Precision, Recall, F1-score
- Confusion Matrix

**Model artifact:**
- `models/customer_churn_rf.joblib`

---

## Results

### Logistic Regression
- Precision: **0.788695652173913**
- Recall: **0.8763285024154589**
- F1-score: **0.8302059496567505**

### Random Forest 
- Precision: **0.8456375838926175**
- Recall: **0.8521739130434782**
- F1-score: **0.848893166506256**

**Conclusion:** Random Forest performed better on churn detection (higher Recall/F1), making it more suitable for retention-focused use cases.

---

## Batch Inference (CLI)

Run predictions on a CSV of features (must match training features).  
If the input contains `Churn`, the script automatically drops it.

From repo root:

```bash
python ml_projects/customer_churn/predict.py ^
--input ml_projects/data/customer_churn_preprocessed.csv ^
--output ml_projects/customer_churn/predictions.csv ^
--model ml_projects/customer_churn/models/customer_churn_rf.joblib

## Output:

ml_projects/customer_churn/predictions.csv with an added column:

churn_prediction

