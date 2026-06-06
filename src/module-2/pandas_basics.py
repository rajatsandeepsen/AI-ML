"""
Introduction to Pandas - Fundamentals
"""

import numpy as np
import pandas as pd

# Series - One-dimensional labeled array
series1 = pd.Series([10, 20, 30, 40, 50])
print(series1)

series2 = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
print(series2)

data_dict = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
series3 = pd.Series(data_dict)
print(series3)

# DataFrame - Two-dimensional labeled data structure
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 30, 35, 28, 32],
    "Salary": [50000, 60000, 75000, 55000, 70000],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
}
df = pd.DataFrame(data)
print(df)

# Creating DataFrame from 2D list
data_list = [[1, "Alice", 85], [2, "Bob", 92], [3, "Charlie", 78]]
df2 = pd.DataFrame(data_list, columns=["ID", "Name", "Score"])
print(df2)

# Accessing columns
print(df["Name"])

print(df[["Name", "Age"]])

# Accessing rows
print(df.iloc[0])

print(df.iloc[1:3])

# Accessing specific cells
print(df.loc[0, "Name"])
print(df.iloc[0, 0])

# Boolean indexing
print(df[df["Age"] > 28])

# DataFrame shape and info
print(df.shape)
print(df.info())

# Descriptive statistics
print(df.describe())

# Data types
print(df.dtypes)

# Missing data handling
df_missing = pd.DataFrame(
    {"A": [1, 2, np.nan, 4], "B": [5, np.nan, 7, 8], "C": [9, 10, 11, 12]}
)
print(df_missing)

print(df_missing.isnull())

print(df_missing.isnull().sum())

print(df_missing.dropna())

print(df_missing.fillna(0))

# Grouping and aggregation
print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Salary"].agg(["mean", "min", "max", "count"]))

print(df.groupby("Department").size())

# Sorting
print(df.sort_values("Age"))

print(df.sort_values("Salary", ascending=False))

print(df.sort_values(["Department", "Age"]))

# Adding and modifying columns
df_copy = df.copy()
df_copy["Years_Experience"] = [2, 5, 8, 3, 6]
print(df_copy)

df_copy["Salary_Increase"] = df_copy["Salary"] * 1.1
print(df_copy)

df_renamed = df_copy.rename(
    columns={"Name": "Employee_Name", "Age": "Employee_Age"}
)
print(df_renamed)

# Statistics
print(df["Age"].mean())
print(df["Age"].median())
print(df["Age"].min())
print(df["Age"].max())
print(df["Age"].std())
print(df["Salary"].sum())

# Reading and writing data
# df.to_csv('employees.csv', index=False)
# df_read = pd.read_csv('employees.csv')
# df.to_excel('employees.xlsx', index=False, sheet_name='Employees')

csv_string = df.to_csv(index=False)
print(csv_string)
