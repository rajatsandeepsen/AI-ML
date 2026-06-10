import sklearn.datasets as DS
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

dataset = DS.load_breast_cancer()
data, target = dataset.data, dataset.target


x_train, x_test, y_train, y_test = train_test_split(
    data, target, test_size=0.2, random_state=42
)
model = DecisionTreeClassifier(criterion="entropy", random_state=42)

trained_model = model.fit(x_train, y_train)
y_pred = model.predict(x_test)

accuracy = round(model.score(x_test, y_test) * 100, 2)

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
from sklearn.tree import plot_tree

plt.figure(figsize=(15, 10))
plot_tree(trained_model)
plt.show()
