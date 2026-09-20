import joblib
import numpy as np

# Load trained Random Forest model
model = joblib.load("rf_model.joblib")

# Selected classification threshold
threshold = 0.50

# Example input with 30 WDBC diagnostic features
sample = np.array([[
    14.0, 20.0, 90.0, 600.0, 0.10,
    0.12, 0.10, 0.05, 0.18, 0.06,
    0.40, 1.20, 2.50, 30.0, 0.007,
    0.03, 0.04, 0.02, 0.02, 0.004,
    16.0, 25.0, 105.0, 800.0, 0.13,
    0.25, 0.30, 0.12, 0.28, 0.08
]])

# Get class probabilities
probabilities = model.predict_proba(sample)[0]

probability_benign = probabilities[0]
probability_malignant = probabilities[1]

# Apply selected threshold
predicted_class = int(probability_malignant >= threshold)

diagnosis = "Malignant" if predicted_class == 1 else "Benign"

# Display results
print("Predicted Class:", diagnosis)
print("Probability of Benign:", round(probability_benign, 4))
print("Probability of Malignant:", round(probability_malignant, 4))
print("Classification Threshold:", threshold)