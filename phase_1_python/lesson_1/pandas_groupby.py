import pandas as pd

df = pd.read_csv("employee.csv")
print(df)
print("-"*40)

# Printing Average salary
avg_sal = df["salary"].mean()
print(avg_sal)
print("-"*40)

# Printing the minimum salary
min_sal = df["salary"].min()
print(min_sal)
print("-"*40)

# Printing Maximum salary
max_sal = df["salary"].max()
print(max_sal)
print("-"*40)

# Average salary by department
print(df.groupby("department")["salary"].mean())
print("-"*40)

# Total salary by department
print(df.groupby("department")["salary"].sum())
print("-"*40)

# Summary of the whole employee per department
print(df.groupby("department")["salary"].agg(["sum", "mean", "count"]))
print("-"*40)
#
print(df[df["department"] != "HR"].groupby("department")["salary"].mean())