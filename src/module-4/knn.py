from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = load_iris()
x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)


KNN = KNeighborsClassifier(n_neighbors=3)
KNN.fit(x_train, y_train)

y_predict = KNN.predict(x_test)

accuracy = accuracy_score(y_test, y_predict)
print("Accuracy:", accuracy * 100, "%")

print("Sample", " │ Actual \t│", "Predicted \t", "\t│ Prediction ")
print("──────────────────────────────────────────────────────────────")
for sample in range(len(y_test)):
    predict = y_predict[sample]
    test = y_test[sample]

    result = " Correct ✅" if (predict == test) else "Incorrect❌"

    print(
        sample + 1,
        "\t│",
        data.target_names[test],
        "\t│ ",
        data.target_names[predict],
        " \t\t│",
        result,
    )

mse = mean_squared_error(y_test, y_predict)
print("Mean Square Error:", mse)
