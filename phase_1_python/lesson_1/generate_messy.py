import pandas as pd
import numpy as np

data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8],
    "customer_name": [" John Doe ", "jane smith", "Bob Jones", " Alice Brown ", "Eve Davis", "Charlie Wilson", " David Lee ", "Frank White"],
    "age": [25, 30, np.nan, 22, 35, np.nan, 40, 28],
    "purchase_amount": [150.50, -20.00, 300.00, np.nan, 75.50, 100.00, 500.00, 0.00],
    "country": ["US", "UK", "US", "US", "CA", "UK", "US", "CA"]
}

df = pd.DataFrame(data)
print(df)
print("-"*50)
df = df.dropna(subset=["age"])
print(df)
print("-"*50)
df = df[df["purchase_amount"] > 0]
print(df)
df["customer_name"] = df["customer_name"].str.strip()
print("-"*50)
def is_premium(purchase_amount):
    if purchase_amount > 200:
        return True
    else:
        return False

df["is_premium"] = df["purchase_amount"].apply(is_premium)
print(df)
print("-"*50)

df.to_csv("clean_customer.csv", index=False)

df = pd.read_csv("clean_customer.csv")
print(df)
#df = df.dropna(subset=["purchase_amount"])
#print(df)
