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
high_sales = df[df["Sales"] > 100000]
print(high_sales)
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
total_sales = new_sort[["Sales"]]
print(total_sales.sum())
print("-"*40)

# Calculating maximum salary
print("-"*3+" "+"Maximum Salary"+" "+"-"*3)
max_salary = new_sort[["Sales"]].max()
print(max_salary)
print("-"*40)

# Calculating minimum salary
print("-"*3+" "+"Minimum Salary"+" "+"-"*3)
min_salary = new_sort[["Sales"]].min()
print(min_salary)