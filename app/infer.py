from __future__ import annotations

import json
from pathlib import Path
from urllib import request

import numpy as np
from PIL import Image

API_URL = "http://127.0.0.1:8000/predict"
IMAGE_PATH = Path(__file__).resolve().parent / "5.jpg"


def image_to_pixels(image_path: Path) -> list[float]:
    image = Image.open(image_path).convert("L").resize((28, 28))
    arr = np.array(image, dtype=np.float32)

    if float(arr.mean()) > 127:
        arr = 255.0 - arr

    arr = arr / 255.0
    return arr.reshape(784).astype(float).tolist()


pixels = image_to_pixels(IMAGE_PATH)
payload = json.dumps({"pixels": pixels}).encode("utf-8")

req = request.Request(
    API_URL,
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST",
)

with request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

print(data)

# uv run ./src/production/scikit/infer.py
