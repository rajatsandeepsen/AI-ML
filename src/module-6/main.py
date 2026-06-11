import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.cluster import KMeans

dataset = pd.read_csv("./dataset/social-media.csv")
feature_data: NDArray[np.float64] = dataset[
    ["visit_score", "spending_rank"]
].to_numpy(dtype=np.float64)

# only X, no Y, because K-Means is an unsupervised learning algorithm

# n_clusters=3 because Iris dataset has 3 natural groups
model = KMeans(n_clusters=5, random_state=42, n_init=10)

model.fit(feature_data)

cluster_labels = model.predict(feature_data)

# print("K-Means clustering completed successfully")
# print("-----------------------------------------------")
# print("Sample\t Predicted Cluster")
# print("-----------------------------------------------")

# for i in range(20):
#     print(i, "\t", cluster_labels[i])

# Visualize clusters using first two features
plt.figure(figsize=(10, 6))
plt.scatter(
    feature_data[:, 0],
    feature_data[:, 1],
    c=cluster_labels,
    cmap="viridis",
    edgecolors="k",
    s=60,
)

# Plot cluster centers
centers = model.cluster_centers_
print(centers)
plt.scatter(
    centers[:, 0],
    centers[:, 1],
    c="red",
    marker="X",
    s=200,
    label="Centroids",
)

plt.title("K-Means Clustering (Social Media)")
plt.xlabel("visit_score")
plt.ylabel("spending_rank")


colors = {
    "adult_male": "blue",
    "adult_female": "red",
    "young_female": "pink",
    "young_male": "cyan",
    "elder": "orange",
}


labelled_dataset = pd.read_csv("./dataset/social-media-labelled.csv")

x_vals: NDArray[np.float64] = labelled_dataset["visit_score"].to_numpy(
    dtype=np.float64
)
y_vals: NDArray[np.float64] = labelled_dataset["spending_rank"].to_numpy(
    dtype=np.float64
)
labels: list[str] = labelled_dataset["label"].astype(str).tolist()

for visit_score, spending_rank, label in zip(
    x_vals, y_vals, labels, strict=True
):
    plt.scatter(
        visit_score,
        spending_rank,
        c=colors[label],
        marker=".",
        s=200,
        label=label,
    )


plt.legend()
plt.tight_layout()
plt.show()
