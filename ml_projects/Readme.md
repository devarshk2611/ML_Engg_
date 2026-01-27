# Machine Learning Projects

This folder contains my **hands-on machine learning projects**, organized to demonstrate both **foundational learning** and **end-to-end applied ML workflows**.

The projects focus on clean structure, reproducibility, evaluation, and deployment readiness.

---

## 📘 Iris Classification (Learning Project)

**Folder:** `iris/`

This project documents my **step-by-step learning of the complete machine learning pipeline** using the classic Iris dataset.

### Covered Topics

- Exploratory Data Analysis (EDA) with Pandas
- Data cleaning and preprocessing
- Feature engineering
- Scaling and transformations
- Logistic Regression
- Tree-based models
- Model evaluation and comparison
- Basic inference scripting

### Purpose

Build strong fundamentals in **data preparation**, **modeling**, and **evaluation**, forming a solid base for more advanced ML projects.

---

## 🚀 Customer Churn Prediction (Applied ML Project)

**Folder:** `customer_churn/`  
**Data:** `data/customer_churn*.csv`

This is an **end-to-end applied machine learning project** focused on predicting customer churn.  
It is designed to reflect **real-world ML engineering workflows**.

### Workflow

- Exploratory Data Analysis (EDA)
- Data cleaning and validation
- Feature engineering
- Handling class imbalance using **SMOTE**
- Train-test splitting
- Model training and evaluation:
  - Logistic Regression
  - Random Forest
- Performance metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
- Model persistence for deployment

### Purpose

Demonstrate **applied machine learning**, understanding of the **model lifecycle**, and **production readiness**.

---

## 📰 BBC News Text Classification (NLP Project)

**Folder:** `nlp_bbc_news/`

This is an **end-to-end NLP text classification project** that predicts the category of a news article using classical machine learning with TF-IDF features.

### Covered Topics

- Dataset exploration and class distribution analysis
- Text preprocessing and cleaning
- TF-IDF feature extraction (unigrams + bigrams)
- Model training and comparison:
  - Logistic Regression
  - Linear SVM
- Macro-F1 based evaluation
- Saving a full sklearn pipeline with **joblib**
- CLI-based batch inference using `predict.py`

### Purpose

Demonstrate a practical NLP workflow with:
- strong evaluation (multi-class)
- reproducibility (saved pipeline)
- deployment-style inference (CLI)

---

## 📂 Data and Models

- Datasets are stored in the `data/` directory (project-specific where applicable)
- Trained models are saved using **joblib** for reuse and deployment
- Each project follows a clean separation of **data**, **code**, and **notebooks**

---

## 🧠 Tools and Technologies

- **Python**
- **Pandas**, **NumPy**
- **scikit-learn**
- **Matplotlib**
- **Jupyter Notebooks**
- **Git / GitHub**