import pandas as pd

df = pd.read_csv("employee.csv")

names = df["name"]
print(names)
print("-"*50)

subset = df[["name", "department"]]
print(subset)
print("-"*50)

dept_name = df[df["department"] == "Marketing"]
print(dept_name)
print("-"*50)

sal_ary = df[df["salary"] > 70000]
print(sal_ary)
print("-"*50)

new_param = df[(df["department"] == "Engineering") & (df["salary"] > 70000)]
print(new_param)
print("-"*50)

new_var = df[(df["department"] == "Marketing") | (df["department"] == "HR")]
print(new_var)