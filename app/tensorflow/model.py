from __future__ import annotations

from pathlib import Path

import numpy as np
from datasets import load_dataset
from numpy.typing import NDArray
from tensorflow import keras

data = load_dataset("p2pfl/MNIST").with_format("numpy")

x_train: NDArray[np.float32] = np.asarray(
    data["train"]["image"], dtype=np.float32
)
y_train: NDArray[np.int64] = np.asarray(data["train"]["label"], dtype=np.int64)

x_test: NDArray[np.float32] = np.asarray(
    data["test"]["image"], dtype=np.float32
)
y_test: NDArray[np.int64] = np.asarray(data["test"]["label"], dtype=np.int64)

# [N, 28, 28] -> [N, 28, 28, 1], normalize
x_train = (x_train / 255.0)[..., np.newaxis]
x_test = (x_test / 255.0)[..., np.newaxis]

model = keras.Sequential(
    [
        keras.layers.Input(shape=(28, 28, 1)),
        keras.layers.Conv2D(32, 3, activation="relu"),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(64, 3, activation="relu"),
        keras.layers.MaxPooling2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(x_train, y_train, epochs=5, batch_size=128, verbose=1)

_, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Accuracy: {test_acc:.4f}")

save_path = Path(__file__).resolve().parent / "model.keras"
model.save(save_path)
print(f"Model saved as {save_path.name}")

# uv run ./app/tensorflow/model.py
