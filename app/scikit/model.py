from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
from datasets import load_dataset
from numpy.typing import NDArray
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1)
data = load_dataset("p2pfl/MNIST").with_format("numpy")

train_ds = data["train"]
test_ds = data["test"]

x_train: NDArray[np.float32] = np.asarray(train_ds["image"], dtype=np.float32)
x_test: NDArray[np.float32] = np.asarray(test_ds["image"], dtype=np.float32)

y_train: NDArray[np.int64] = np.asarray(train_ds["label"], dtype=np.int64)
y_test: NDArray[np.int64] = np.asarray(test_ds["label"], dtype=np.int64)

x_train = x_train.reshape(x_train.shape[0], -1) / 255.0
x_test = x_test.reshape(x_test.shape[0], -1) / 255.0

print("Dataset Splitted")

# 4)
model = LogisticRegression(
    max_iter=200,
    n_jobs=-1,
)
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

# uv run ./app/scikit/model.py
