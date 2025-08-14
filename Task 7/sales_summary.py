import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# 1. Create and connect to the database
# ------------------------------
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# ------------------------------
# 2. Create the sales table (professional example)
# ------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL,
    sale_date TEXT
)
""")

# ------------------------------
# 3. Insert sample professional data (10 rows)
# ------------------------------
cursor.execute("DELETE FROM sales")  # Clear old data

sample_data = [
    ("Laptop", 3, 75000, "2025-08-01"),
    ("Smartphone", 5, 30000, "2025-08-02"),
    ("Tablet", 2, 20000, "2025-08-03"),
    ("Monitor", 4, 15000, "2025-08-04"),
    ("Keyboard", 10, 1500, "2025-08-05"),
    ("Mouse", 8, 800, "2025-08-06"),
    ("Printer", 1, 12000, "2025-08-07"),
    ("Headphones", 6, 2500, "2025-08-08"),
    ("External HDD", 2, 5000, "2025-08-09"),
    ("Webcam", 3, 3500, "2025-08-10")
]

cursor.executemany("""
INSERT INTO sales (product, quantity, price, sale_date)
VALUES (?, ?, ?, ?)
""", sample_data)

conn.commit()

# ------------------------------
# 4. Run 4 SQL queries
# ------------------------------

# Query 1: View all sales data
print("\n--- Query 1: All Sales Data ---")
df_all = pd.read_sql_query("SELECT * FROM sales", conn)
print(df_all)

# Query 2: Total quantity sold per product
print("\n--- Query 2: Total Quantity Sold per Product ---")
df_qty = pd.read_sql_query("""
SELECT product, SUM(quantity) AS total_qty
FROM sales
GROUP BY product
""", conn)
print(df_qty)

# Query 3: Total revenue per product
print("\n--- Query 3: Total Revenue per Product ---")
df_revenue = pd.read_sql_query("""
SELECT product, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
""", conn)
print(df_revenue)

# Query 4: Total revenue overall
print("\n--- Query 4: Overall Total Revenue ---")
df_total_revenue = pd.read_sql_query("""
SELECT SUM(quantity * price) AS total_revenue
FROM sales
""", conn)
print(df_total_revenue)

# ------------------------------
# 5. Plot bar chart for revenue per product
# ------------------------------
plt.figure(figsize=(10, 6))
plt.bar(df_revenue['product'], df_revenue['revenue'], color='skyblue')
plt.xlabel("Product")
plt.ylabel("Revenue (INR)")
plt.title("Revenue per Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_chart.png")  # Save chart as file
plt.show()

# Close connection
conn.close()
