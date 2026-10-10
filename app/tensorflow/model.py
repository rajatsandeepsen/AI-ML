from __future__ import annotations

from pathlib import Path

import numpy as np
from datasets import load_dataset
from numpy.typing import NDArray
from tensorflow import keras

data = load_dataset("p2pfl/MNIST").with_format("numpy")


# write code here


save_path = Path(__file__).resolve().parent / "model.keras"
model.save(save_path)
print(f"Model saved as {save_path.name}")

# uv run ./app/tensorflow/model.py
