from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
from PIL import Image

base_dir = Path(__file__).resolve().parent
download_path = base_dir / "model.joblib"
image_path = base_dir.parent / "5.jpg"

model = joblib.load(download_path)

# read image and convert to MNIST-like input (1, 784)
image = Image.open(image_path).convert("L").resize((28, 28))
arr = np.array(image, dtype=np.float32)
if float(arr.mean()) > 127:
    arr = 255.0 - arr
x = (arr / 255.0).reshape(1, 784)


p = model.predict(x)
print("prediction", p)


probabilities = model.predict_proba(x)[0]
classes = model.classes_.tolist()

for cls, prob in zip(classes, probabilities):
    print(cls, ":", round(prob, 3))
