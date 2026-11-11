import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard"],
    "Sales": [500000, None, 180000, 25000],
    "Profit": [80000, 5000, None, 8000]
}

df = pd.DataFrame(data)
print(df)
print("-"*40)

# Checking for missing values
missing_values = df.isnull()
print(missing_values)
print("-"*40)

# Counting the number of missed values
print(missing_values.sum())
print("-"*40)

# Checking for duplicates
print(missing_values.duplicated())
df.info()
print("-"*40)

cleaned_df = df.dropna()
#print(cleaned_df)

# Filling the missed values with zero
df["Sales"] = df["Sales"].fillna(0)
print(df)
print("-"*40)

df["Profit"] = df["Profit"].fillna(12000)
print(df)
print("-"*40)

print(df.isnull().sum())
print("-"*40)

df["City"] = [" Lagos", "lagos ", "LAGOS ", "Abuja "]
df["Customer"] = [" JOHN ", "Mary", " PETER", "david "]

# Re-indexing the columns
df = df.reindex(columns=["Customer", "Product", "Sales", "Profit", "City"])
print("-"*40)

# Data cleaning
df["City"] = df["City"].str.strip().str.title()
df["Customer"] = df["Customer"].str.strip().str.title()
print(df)
print("-"*40)

# Using groupby to filter
avg_sales = df.groupby("City")["Profit"].sum()
print(avg_sales)
print("-"*40)

# Using agg function
city_report = df.groupby("City").agg({
    "Sales": "sum",
    "Profit": ["sum", "mean"]
})
print(city_report)
print("-"*40)

city_report_2 = df.groupby("City").agg(
    total_sales = ("Sales", "sum"),
    total_profit = ("Profit", "sum"),
    avg_profit = ("Profit", "mean")
)
print(city_report_2)
print("-"*40)

# Checking for the number of customers per city
customer_per_city = df.groupby("City")["Customer"].count()
print(customer_per_city)
print("-"*40)

# checking for unique values
product_per_city = df.groupby("City")["Product"].nunique()
print(product_per_city.sort_values(ascending=False))
print("-"*40)

# Calculating average sales using groupby and sorting 
avg_sales = df.groupby("City")["Profit"].sum()
print(avg_sales.sort_values(ascending=False).head(1))
print("-"*40)

# Chaining groupby, sort_values and reset_index
city_sales_report = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
print(city_sales_report)
print("-"*40)

# Creating a report
final_city_report = (
    df.groupby("City")
    .agg(
        total_sales = ("Sales", "sum"),
        total_profit = ("Profit", "sum"),
        average_profit = ("Profit", "mean"),
        customers_record = ("Customer", "count")
    )
    .sort_values(by="total_sales",ascending=False)
    .reset_index()
)
print(final_city_report)

# Exporting the dataframe to a csv file
final_city_report.to_csv("city_report.csv", index=False)

# Reading the exported csv file
verified_report = pd.read_csv("city_report.csv")
print(verified_report)