import sklearn.datasets as DS
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

dataset = DS.load_breast_cancer()
data, target = dataset.data, dataset.target

x_train, x_test, y_train, y_test = train_test_split(
    data, target, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100, criterion="entropy", random_state=42
)
trained_model = model.fit(x_train, y_train)

y_pred = trained_model.predict(x_test)

accuracy = round(trained_model.score(x_test, y_test) * 100, 2)
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

import matplotlib.pyplot as plt

feature_importance = trained_model.feature_importances_
feature_names = dataset.feature_names

plt.figure(figsize=(14, 6))
plt.bar(feature_names, feature_importance)
plt.title("Random Forest Feature Importance")
plt.xlabel("Feature Name")
plt.ylabel("Importance")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
