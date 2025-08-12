# 📊 Sales Trend Analysis (SQL)

This project analyzes monthly sales trends, revenue, and order volume from an e-commerce dataset using SQL.  
It demonstrates the use of aggregation, grouping, ordering, and filtering functions to gain business insights.

##  Dataset Description
The dataset contains e-commerce order details with the following columns:

| Column Name     | Description |
|-----------------|-------------|
| `customer_id`   | Unique ID for the customer |
| `order_date`    | Date the order was placed |
| `product_id`    | Unique product identifier |
| `category_id`   | Product category identifier |
| `category_name` | Product category name |
| `product_name`  | Name of the product |
| `quantity`      | Quantity of the product ordered |
| `price`         | Price of a single unit |
| `payment_method`| Payment method used |
| `city`          | Customer's city |
| `review_score`  | Customer's review score (1-5) |
| `gender`        | Gender of the customer |
| `age`           | Age of the customer |

##  SQL Techniques Used
- `EXTRACT(YEAR/MONTH FROM order_date)` → Extract month & year
- `GROUP BY` → Aggregate data per month/year
- `SUM(quantity * price)` → Calculate monthly revenue
- `COUNT(DISTINCT order_id)` → Count unique orders
- `ORDER BY` → Sort results by date
- `LIMIT` → Restrict to specific time periods

##  Example Query
```sql
SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(quantity * price) AS total_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM orders
GROUP BY year, month
ORDER BY year, month;
