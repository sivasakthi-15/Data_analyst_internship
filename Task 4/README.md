📊 Olist E-Commerce Data Analysis – PostgreSQL
📌 Overview
This project is part of Task 4 of my internship, where I performed E-Commerce data analysis using PostgreSQL.
The dataset used is the Olist Brazilian E-Commerce Public Dataset, which contains information about customers, orders, products, and order items.
The goal is to explore sales trends, customer behavior, and category performance using SQL queries.

📂 Dataset
The dataset is publicly available on Kaggle:
🔗 Brazilian E-Commerce Public Dataset by Olist

Files used in this project:

olist_customers_dataset.csv – Customer details

olist_orders_dataset.csv – Orders data

olist_products_dataset.csv – Product details

olist_order_items_dataset.csv – Order items

product_category_name_translation.csv – Category name translations

🛠 Technologies Used
PostgreSQL 16 (Windows)

pgAdmin 4 / psql

SQL for data analysis

(Optional) Power BI / Metabase for dashboards

⚙ Steps to Reproduce
Create Database


CREATE DATABASE olist_ecommerce;
Connect to Database


\c olist_ecommerce
Create Tables
Use the CREATE TABLE statements from schema.sql in this repo.

Import Data

\copy customers FROM 'C:/path/olist_customers_dataset.csv' DELIMITER ',' CSV HEADER;
\copy categories FROM 'C:/path/product_category_name_translation.csv' DELIMITER ',' CSV HEADER;
\copy products FROM 'C:/path/olist_products_dataset.csv' DELIMITER ',' CSV HEADER;
\copy orders FROM 'C:/path/olist_orders_dataset.csv' DELIMITER ',' CSV HEADER;
\copy order_items FROM 'C:/path/olist_order_items_dataset.csv' DELIMITER ',' CSV HEADER;
Run Analysis Queries
The analysis_queries.sql file contains 13 SQL queries for insights.

📊 Analysis Queries
The analysis covers:

Total number of customers

Orders per customer state

Top 10 most ordered products

Top 10 product categories by revenue

Monthly orders trend

Average delivery time

Orders by status

Highest value single order

Top 10 sellers by revenue

Customers with more than 5 orders

Revenue by month

Products never sold

Average freight value per state

📷 Output
Screenshots of query outputs are saved in the outputs/ folder.

Each output corresponds to the query number.

📈 Optional Dashboard
You can connect PostgreSQL to Power BI or Metabase to create:

Revenue trends

Orders by state

Top-selling categories

