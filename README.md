
# Breast Tumor Classification

## Project Overview

This project focuses on classifying breast tumor observations as Benign or Malignant using the UCI Breast Cancer Wisconsin Diagnostic dataset.

A Random Forest Classifier was developed with data preprocessing, hyperparameter tuning, threshold analysis, model evaluation, and error analysis. K-Means and hierarchical clustering were also performed for exploratory pattern segmentation.

## Dataset

- Dataset: UCI Breast Cancer Wisconsin Diagnostic
- Observations: 569
- Diagnostic Features: 30
- Benign Cases: 357
- Malignant Cases: 212
- Missing Values: None

The ID column was removed because it is only an identifier and is not a diagnostic feature.

## Project Workflow

1. Exploratory Data Analysis
2. Data Preprocessing
3. Stratified Train-Validation-Test Split
4. Random Forest Model Development
5. Hyperparameter Tuning using GridSearchCV
6. Threshold Analysis
7. Model Evaluation
8. Error Analysis
9. K-Means Clustering
10. Hierarchical Clustering

## Model

Random Forest Classifier

Final configuration:

- n_estimators: 200
- max_depth: 5
- min_samples_split: 2
- min_samples_leaf: 1
- max_features: sqrt
- class_weight: balanced
- random_state: 42

## Final Test Results

- Accuracy: 96.49%
- Precision: 100.00%
- Malignant Recall: 90.48%
- F1 Score: 95.00%
- ROC-AUC: 99.74%

Confusion Matrix:

- True Negatives: 36
- False Positives: 0
- False Negatives: 2
- True Positives: 19

## Project Files

- `01_EDA.ipynb` – Exploratory Data Analysis
- `02_Preprocessing.ipynb` – Data preprocessing and splitting
- `03_Random_Forest_Model.ipynb` – Model development and tuning
- `04_Evaluate.ipynb` – Final model evaluation
- `05_Clustering.ipynb` – K-Means and hierarchical clustering
- `rf_model.joblib` – Saved Random Forest model
- `inference.py` – Example model inference script
- `wdbc.data` – Dataset
- `Breast_Tumor_Classification_Final_Report.docx` – Final project report
- `Breast_Tumor_Classification_Capstone_Presentation.pptx` – Project presentation

## Important Note

This project is intended for learning and demonstration purposes. It does not establish clinical validity and should not be used as a medical diagnostic system.
