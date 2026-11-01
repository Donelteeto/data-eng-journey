import pandas as pd

df = pd.read_csv("employee.csv")
print("-"*40)

df = df[df["salary"] >= 65000]
print(df)
print("-"*40)

df["salary"] = df["salary"] * 1.05
print("-"*40)

df["bonus"] = df["salary"] * 0.10


def get_status(salary):
    if salary >= 75000:
        return "Senior"
    else:
        return "Junior"

df["status"] = df["salary"].apply(get_status)
df["email"] = df["name"].str.lower().str.replace(" ", ".") + "@opay.com"

# Loading - exporting the dataframe to a new file
df.to_csv("employee_processed.csv", index=False)

# Reading the new file
data = pd.read_csv("employee_processed.csv")
print(data)
