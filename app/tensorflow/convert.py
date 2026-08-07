from __future__ import annotations

from pathlib import Path

from tensorflow import keras, lite

base_dir = Path(__file__).resolve().parent
download_path = base_dir / "model.keras"

model = keras.models.load_model(download_path)

converter = lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open(base_dir / "model.tflite", "wb") as f:
    f.write(tflite_model)

# uv run ./app/tensorflow/convert.py
