import pandas as pd

data = {
    "product": ["books", "shoes", "jumpsuits", "bags"],
    "price": [260, 500, 1000, 400],
    "quantity": [50, 40, 200, 70]
}

df = pd.DataFrame(data)
print(df)