from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image
from tensorflow import keras

base_dir = Path(__file__).resolve().parent
download_path = base_dir / "model.keras"
image_path = base_dir.parent / "5.jpg"

model = keras.models.load_model(download_path)

# read image and convert to MNIST-like input (1, 28, 28, 1)
image = Image.open(image_path).convert("L").resize((28, 28))
arr = np.array(image, dtype=np.float32)
if float(arr.mean()) > 127:
    arr = 255.0 - arr
x = (arr / 255.0).reshape(1, 28, 28, 1)

probabilities = model.predict(x, verbose=0)[0]
prediction = int(np.argmax(probabilities))
print("prediction", prediction)

classes = list(range(len(probabilities)))
for cls, prob in zip(classes, probabilities):
    print(cls, ":", round(float(prob), 3))

# uv run ./app/tensorflow/test.py
