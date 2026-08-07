from __future__ import annotations

from pathlib import Path

import joblib
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 1)
x, y = fetch_openml("mnist_784", version=1, as_frame=False, return_X_y=True)
print("Dataset Loaded")

# 2)
x = x / 255.0
y = y.astype(int)

# 3)
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
)
print("Dataset Splitted")

# 4)
model = LogisticRegression(max_iter=200)
print("Model Created")


# 5)
model.fit(x_train, y_train)
print("Model Trained")

# 6)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

base_dir = Path(__file__).resolve().parent
download_path = base_dir / "model.joblib"

# 7) Save model
joblib.dump(model, download_path)
print("Model saved as model.joblib")
