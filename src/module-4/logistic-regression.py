import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("./dataset/cancer.csv")
x = np.array(data["radius_mean"]).reshape(-1, 1)
y = data["diagnosis"]


model = LogisticRegression()
model.fit(x, y)

radius = float(input("Enter the radius of the tumor: "))  # eg: 25
prediction = model.predict(np.array(radius).reshape(-1, 1))
if prediction == "B":
    print("It is benign tumor 💞 ")
else:
    print("It is Malignant tumor 💀")
