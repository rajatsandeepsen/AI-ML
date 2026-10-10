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

# write code here

base_dir = Path(__file__).resolve().parent
download_path = base_dir / "model.joblib"

# 7) Save model
joblib.dump(model, download_path)
print("Model saved as model.joblib")

# uv run ./app/scikit/model.py
