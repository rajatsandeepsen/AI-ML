import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets as DS
from numpy.typing import NDArray
from sklearn.cluster import KMeans

dataset = DS.load_iris()
feature_data: NDArray[np.float64] = dataset.data
# only X, no Y, because K-Means is an unsupervised learning algorithm

# n_clusters=3 because Iris dataset has 3 natural groups
model = KMeans(n_clusters=3, random_state=42, n_init=10)

model.fit(feature_data)

cluster_labels = model.predict(feature_data)

print("K-Means clustering completed successfully")
print("-----------------------------------------------")
print("Sample\t Predicted Cluster")
print("-----------------------------------------------")

for i in range(20):
    print(i, "\t", cluster_labels[i])

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
plt.scatter(
    centers[:, 0],
    centers[:, 1],
    c="red",
    marker="X",
    s=200,
    label="Centroids",
)

plt.title("K-Means Clustering (Iris Dataset)")
plt.xlabel(dataset.feature_names[0])
plt.ylabel(dataset.feature_names[1])
plt.legend()
plt.tight_layout()
plt.show()
