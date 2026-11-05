import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard", "Phone"],
    "Sales": [500000, 15000, 180000, 25000, 120000],
    "Profit": [80000, 5000, 15000, 8000, 30000]
}

# Displaying the Data frame
print("-"*3+" "+"Table Display"+" "+"-"*3)
df = pd.DataFrame(data)
print(df)
print("-"*40)

# Filtering Sales above 100000
print("-"*3+" "+"Filtering Columns"+" "+"-"*3)
big_sales = df[df["Sales"] > 100000]
print(big_sales)
print("-"*40)

# Filtering both Sales and Profit
print("-"*3+" "+"Filtering"+" "+"-"*3)
new_sales_profit = df[(df["Sales"] > 100000) & (df["Profit"] > 20000)]
print(new_sales_profit)
print("-"*40)

# Sorting the Data frame by Sales column
print("-"*3+" "+"Sorting by Sales"+" "+"-"*3)
new_sort = df.sort_values(by="Sales", ascending=False).head(3)
print(new_sort)
print("-"*40)
'''
# Calculating the average sales after sorting
print("-"*3+" "+"Average Sale"+" "+"-"*3)
avg_sales = new_sort["Sales"]
print(avg_sales.mean())
print("-"*40)
'''

# Calculating total sales after sorting
print("-"*3+" "+"Total Sales"+" "+"-"*3)
total_sales = df["Sales"].sum()
print(total_sales)
print("-"*40)

# Calculating maximum sales
print("-"*3+" "+"Highest Sale"+" "+"-"*3)
high_sale = new_sort[["Sales"]].max()
print(high_sale)
print("-"*40)

# Calculating minimum sales
print("-"*3+" "+"Lowest Sale"+" "+"-"*3)
low_sale = new_sort[["Sales"]].min()
print(low_sale)
print("-"*40)

# Calculating Top Three sales
print("-"*3+" "+"Top Three Sales"+" "+"-"*3)
top_products = df.sort_values(by="Sales", ascending=False).head(3)
print(top_products)
print("-"*40)

# Calculating Average sales
print("-"*3+" "+"Average Sales"+" "+"-"*3)
avg_sales = df["Sales"].mean()
print(avg_sales)
print("-"*40)

# Shows information about the dataset and its structure
print("DATASET INFORMATION")
df.info()
print("-"*40)

# Checks data for missing values - Data Quality
print("MISSING VALUES")
print(df.isnull().sum())
print("-"*40)

# Adding a duplicate row
duplicated_row = df.iloc[[0]]
df = pd.concat([df, duplicated_row], ignore_index=True)

# Checks for duplicate records
print("DUPLICATED RECORDS")
print(df.duplicated())
print("-"*40)

print("TOTAL DUPLICATE RECORDS")
print(df.duplicated().sum())
print("-"*40)

print(df.duplicated(subset=["Product"]))
print("-"*40)

# Dropping Duplicates
cleaned_df = df.drop_duplicates()
print(cleaned_df)
print("-"*40)

print(len(cleaned_df))

