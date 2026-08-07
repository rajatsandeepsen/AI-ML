from __future__ import annotations

from pathlib import Path

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tensorflow import keras

from app.tensorflow.web import app as web_app

base_dir = Path(__file__).resolve().parent
model_path = base_dir / "model.keras"
model = keras.models.load_model(model_path)

app = FastAPI(title="MNIST Camera Detector")

app.include_router(web_app)


class PredictRequest(BaseModel):
    pixels: list[float]


def _to_input_array(pixels: list[float]) -> np.ndarray:
    if len(pixels) != 784:
        raise ValueError("pixels must contain exactly 784 values")

    x = np.array(pixels, dtype=float).reshape(1, 784)
    if x.max() > 1.0:
        x = x / 255.0
    return x


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: PredictRequest) -> dict[str, object]:
    try:
        x = _to_input_array(payload.pixels)
        x = x.reshape(1, 28, 28, 1)

        probabilities_array = model.predict(x, verbose=0)[0]
        prediction = int(np.argmax(probabilities_array))
        probabilities = probabilities_array.astype(float).tolist()

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"prediction failed: {str(e)}"
        ) from e

    return {
        "prediction": prediction,
        "probabilities": probabilities,
    }


# uv run fastapi run ./app/tensorflow/server.py
