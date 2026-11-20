"""
Sales Data Analysis Project
Run: python sales_analysis.py
Requirements: pandas, matplotlib
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sales_data.csv"
CHART_DIR = BASE_DIR / "charts"
CHART_DIR.mkdir(exist_ok=True)

# 1. Load and prepare the data
df = pd.read_csv(DATA_FILE)
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df = df.dropna(subset=["Order_Date", "Sales", "Profit"])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("=" * 55)
print("SALES DATA ANALYSIS")
print("=" * 55)
print(f"Number of orders: {len(df)}")
print(f"Total sales: Rs. {df['Sales'].sum():,.2f}")
print(f"Total profit: Rs. {df['Profit'].sum():,.2f}")
print(f"Total quantity sold: {df['Quantity'].sum():,}")
print(f"Average order value: Rs. {df['Sales'].mean():,.2f}")
print("\nSales by category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False).round(2))
print("\nSales by region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False).round(2))

# Visualization 1: Monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales in 2025")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_DIR / "1_monthly_sales.png", dpi=150)
plt.close()

# Visualization 2: Category-wise sales
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
category_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Sales Share by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig(CHART_DIR / "2_category_sales.png", dpi=150)
plt.close()

# Visualization 3: Top 10 products by sales
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales (Rs.)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(CHART_DIR / "3_top_products.png", dpi=150)
plt.close()

# Visualization 4: Sales vs profit
plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.7)
plt.title("Sales vs Profit per Order")
plt.xlabel("Sales (Rs.)")
plt.ylabel("Profit (Rs.)")
plt.tight_layout()
plt.savefig(CHART_DIR / "4_sales_vs_profit.png", dpi=150)
plt.close()

# Visualization 5: Region-wise sales
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(CHART_DIR / "5_region_sales.png", dpi=150)
plt.close()

print(f"\nFive charts saved in: {CHART_DIR}")
print("Analysis complete!")
