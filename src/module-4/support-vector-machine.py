import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets as DS
from numpy.typing import NDArray
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC as svm

dataset = DS.load_breast_cancer()
feature_data: NDArray[np.float64] = dataset.data
target: NDArray[np.int64] = dataset.target

x_train, x_test, y_train, y_test = train_test_split(
    feature_data, target, test_size=0.2, random_state=42
)

# Build SVM pipeline
# StandardScaler helps SVM perform better because SVM is sensitive to feature scale
svm_model = Pipeline(
    [
        ("scaler", StandardScaler()),
        (
            "classifier",
            svm(kernel="rbf", C=1.0, gamma="scale", random_state=42),
        ),
    ]
)

svm_model.fit(x_train, y_train)

y_pred = svm_model.predict(x_test)

accuracy = round(svm_model.score(x_test, y_test) * 100, 2)
print("Accuracy of the model:", accuracy)

print("-----------------------------------------------")
print("Actual\t\t Predicted\t Prediction")
print("-----------------------------------------------")

for i in range(20):
    print(
        dataset.target_names[y_test[i]],
        " \t",
        dataset.target_names[y_pred[i]],
        " \t",
        end="",
    )

    print("Correct   ✅" if y_pred[i] == y_test[i] else "Incorrect ❌")

ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    display_labels=dataset.target_names,
    cmap="Blues",
)
plt.title("SVM Confusion Matrix")
plt.tight_layout()
plt.show()
