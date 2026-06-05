import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

print("=== Original Dataset ===")
print(df)

# Inspect dataset
print("\n=== Dataset Information ===")
print(df.info())

# Check missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Filter Electronics products
electronics = df[df["Category"] == "Electronics"]

print("\n=== Electronics Products ===")
print(electronics)

# Group by Category and calculate total sales
category_sales = df.groupby("Category")["Sales"].sum()

print("\n=== Total Sales by Category ===")
print(category_sales)

# Highest selling product
top_product = df.loc[df["Sales"].idxmax()]

print("\n=== Highest Selling Product ===")
print(top_product)

# Average sales
avg_sales = df["Sales"].mean()

print("\nAverage Sales:", avg_sales)
