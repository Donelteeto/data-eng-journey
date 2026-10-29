import pandas as pd

df = pd.read_csv("employee.csv")

print("--- FULL DATAFRAME ---")
print(df)

print("\n--- FIRST 2 ROWS ---")
print(df.head(2))

print("\n--- SHAPE ---")
print(df.shape)

print("\n--- COLUMNS ---")
print(df.columns)
