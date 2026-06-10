import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

data = pd.read_csv("./dataset/height-weight.csv")
x = data.loc[:, "height"]
y = data.loc[:, "weight"]

m, c, r, p, std_err = stats.linregress(x, y)


y_value = lambda x: m * x + c

model = list(map(y_value, x))

plt.scatter(x, y, c="g", label="Datas")
plt.plot(x, model, c="r", label="Regression Line")
plt.title("Linear Regression")
plt.xlabel("Height in cm")
plt.ylabel("Weight in kg")
predicted = float(input("Enter the height:"))

print("The predicted weight is", y_value(predicted))

plt.scatter(
    predicted,
    y_value(predicted),
    marker="o",
    color="blue",
    label="Predicted value",
)
plt.legend(bbox_to_anchor=(1.4, 1.03))
plt.show()
