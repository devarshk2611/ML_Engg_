# BBC News Text Classification (NLP)



This project implements an *\*end-to-end NLP text classification system\*\* that automatically categorizes news articles into one of five categories.



The goal is to demonstrate a *\*production-style machine learning workflow\*\*, including preprocessing, model training, evaluation, model persistence, and batch inference via a command-line interface (CLI).



---



## News Categories



The classifier predicts one of the following categories:



- *\*Business\*\*

- *\*Entertainment\*\*

- *\*Politics\*\*

- *\*Sport\*\*

- *\*Tech\*\*



---



## Project Overview



- *\*Task:\*\* Multi-class text classification

- *\*Dataset:\*\* BBC News (2,225 articles across 5 categories)

- *\*Feature Engineering:\*\* TF-IDF (unigrams + bigrams)

- *\*Models Trained:\*\* Logistic Regression, Linear SVM

- *\*Primary Metric:\*\* Macro-F1

- *\*Best Model:\*\* Linear SVM (TF-IDF)

---


## Repository Structure



```text

nlp\_bbc\_news/

├── data/

│   └── bbc-text.csv

├── models/

│   ├── bbc\_news\_linear\_svc\_pipeline.joblib

│   └── tfidf\_vectorizer.joblib

├── part1\_eda.ipynb

├── part2\_preprocessing.ipynb

├── part3\_modeling.ipynb

├── predict.py

├── predictions.csv

└── README.md

```

---


## Workflow


### 1. Exploratory Data Analysis (`part1\_eda.ipynb`)


- Analyzed class distribution

- Examined article length (characters and word counts)

- Reviewed sample articles for each category


---


### 2. Text Preprocessing (`part2\_preprocessing.ipynb`)


- Performed stratified train-test split

- Applied TF-IDF vectorization with:

&nbsp; - Stop-word removal

&nbsp; - Unigrams and bigrams

&nbsp; - Frequency thresholds to reduce noise

- Saved the vectorizer for reuse during inference


---


### 3. Modeling and Evaluation (`part3\_modeling.ipynb`)



Models trained and compared:



- *\*Logistic Regression (TF-IDF)\*\*

- *\*Linear Support Vector Machine (TF-IDF)\*\*


Evaluation metrics included:

- Accuracy

- *\*Macro-F1\*\*

- Confusion Matrix

- Classification Report

---

## Results (Test Set)


| Model | Accuracy | Macro-F1 |

|------|----------|----------|

| Logistic Regression (TF-IDF) | 0.9865 | 0.9861 |

| *\*Linear SVM (TF-IDF)\*\* | *\*0.9888\*\* | *\*0.9882\*\* |



*\*Selected Model:\*\* Linear SVM (TF-IDF) based on superior Macro-F1 performance.

---

## Batch Inference (CLI)

The project includes a command-line script to generate predictions on new text data using the saved model pipeline.


### Run from repository root


```bash

python ml\_projects/nlp\_bbc\_news/predict.py \\

&nbsp; --input ml\_projects/nlp\_bbc\_news/data/bbc-text.csv \\

&nbsp; --text\_col text \\

&nbsp; --output ml\_projects/nlp\_bbc\_news/predictions.csv

```

---

### Output

- CSV file containing an additional column:

&nbsp; - *\*predicted\_category\*\*

---

## Technologies Used


- *\*Python 3.12\*\*

- *\*pandas\*\*

- *\*scikit-learn\*\*

- *\*TF-IDF Vectorization\*\*

- *\*Linear Support Vector Machine\*\*

- *\*joblib\*\*

- *\*Jupyter Notebooks\*\*

- *\*Git / GitHub\*\*


---


## What This Project Demonstrates


- NLP preprocessing and feature extraction

- Model comparison using appropriate metrics for multi-class classification

- End-to-end ML pipeline design

- Model persistence and reproducible inference

- Clean, production-oriented project organization

---

## Future Improvements


- Hyperparameter tuning

- Confidence-based prediction filtering

- Model explainability (top contributing n-grams)

- REST API for real-time inference

---