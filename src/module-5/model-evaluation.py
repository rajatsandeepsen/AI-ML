from math import sqrt

import matplotlib.pyplot as plt
import pandas as pd
import sklearn.datasets as DS
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

dataset = DS.load_breast_cancer()
data, target = dataset.data, dataset.target

x_train, x_test, y_train, y_test = train_test_split(
    data, target, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100, criterion="entropy", random_state=42
)
trained_model = model.fit(x_train, y_train)
y_pred = trained_model.predict(x_test)

# Accuracy = (TP + TN) / (TP + TN + FP + FN)
accuracy = accuracy_score(y_test, y_pred)

# Precision = TP / (TP + FP)
precision = precision_score(y_test, y_pred)

# Recall = TP / (TP + FN)
recall = recall_score(y_test, y_pred)

# F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
f1 = f1_score(y_test, y_pred)

# MAE = (1/n) * Σ|y_true - y_pred|
mae = mean_absolute_error(y_test, y_pred)

# MSE = (1/n) * Σ(y_true - y_pred)^2
mse = mean_squared_error(y_test, y_pred)

# RMSE = sqrt(MSE)
rmse = sqrt(mse)

# R² = 1 - [Σ(y_true - y_pred)^2 / Σ(y_true - mean(y_true))^2]
r2 = r2_score(y_test, y_pred)

cm_display = ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    display_labels=dataset.target_names,
    cmap="Blues",
)

print("\nModel Evaluation Metrics")
print("-" * 40)

# Accuracy = (TP + TN) / (TP + TN + FP + FN)
print(f"Accuracy Score        : {accuracy:.4f}")

# Precision = TP / (TP + FP)
print(f"Precision Score       : {precision:.4f}")

# Recall = TP / (TP + FN)
print(f"Recall Score          : {recall:.4f}")

# F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
print(f"F1 Score              : {f1:.4f}")

# MAE = (1/n) * Σ|y_true - y_pred|
print(f"MAE                   : {mae:.4f}")

# MSE = (1/n) * Σ(y_true - y_pred)^2
print(f"MSE                   : {mse:.4f}")

# RMSE = sqrt(MSE)
print(f"RMSE                  : {rmse:.4f}")

# R² = 1 - [Σ(y_true - y_pred)^2 / Σ(y_true - mean(y_true))^2]
print(f"R² Score              : {r2:.4f}")

plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()

print("\nSample Predictions")
print("-" * 60)

sample_count = min(20, len(y_test))
actual_labels = [dataset.target_names[label] for label in y_test[:sample_count]]
predicted_labels = [
    dataset.target_names[label] for label in y_pred[:sample_count]
]
results = [
    "Correct ✅" if predicted == actual else "Incorrect ❌"
    for actual, predicted in zip(y_test[:sample_count], y_pred[:sample_count])
]

sample_predictions_df = pd.DataFrame(
    {
        "Actual": actual_labels,
        "Predicted": predicted_labels,
        "Prediction": results,
    }
)
print(sample_predictions_df.to_string(index=False))

feature_importance = trained_model.feature_importances_
feature_names = dataset.feature_names

plt.figure(figsize=(14, 6))
plt.bar(feature_names, feature_importance)
plt.title("Random Forest Feature Importance")
plt.xlabel("Feature Name")
plt.ylabel("Importance")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
