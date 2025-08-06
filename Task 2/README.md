# Task 2: Power BI Sales Dashboard with Data Cleaning

## Objective

To clean, preprocess, and visualize product sales data using Power BI. The goal was to transform raw data into a meaningful dashboard that provides actionable insights for decision-making.

## Data Cleaning Steps in Power BI

### Removed Unwanted Columns
- Deleted unnecessary or irrelevant columns (e.g., empty columns, index, IDs) that were not useful for analysis.

### Renamed Columns for Clarity
- Renamed columns to be more readable and meaningful (e.g., amt_sold → Amount Sold, cust_id → Customer ID).

### Changed Data Types Appropriately
- Assigned correct data types:
  - Dates → Date
  - Amounts → Decimal Number
  - Categories → Text

### Handled Null or Missing Values
- Removed rows with nulls in key fields like Sales Amount, Region, or Product Name.
- Replaced missing values using default or average values where applicable.

### Filtered Unwanted Rows
- Removed blank rows or rows with invalid data (e.g., zero sales, unknown regions).

### Split/Merged Columns (if applicable)
- Split full names into first/last name or combined date and time columns, depending on data need.

### Trimmed and Cleaned Text Data
- Removed extra spaces and corrected inconsistent text entries (e.g., north → North).

### Created New Columns (if applicable)
- Added calculated columns such as:
  - Total Profit
  - Discount Percentage
  - Sales Category (based on thresholds)

### Standardized Values
- Unified inconsistent text values (e.g., USA, U.S.A., United States → United States).

### Verified Relationships
- Ensured foreign key relationships were valid between tables for accurate filtering and interaction in the dashboard.

## Dashboard Visualizations

1. **Total Sales by Product Category**  
   Bar chart showing total sales across each product category.

2. **Quantity and Index Trend by SKU**  
   Line and area combo chart comparing quantity sold and index per SKU.

3. **Sales Distribution by Size**  
   Bar chart displaying total sales by size using postal codes.

4. **Sales Contribution by Style**  
   Donut chart showing percentage contribution of each product style.

5. **Daily Trends of Sales Quantity and Amount**  
   Line chart showing date-wise analysis of total quantity and sales amount.

6. **Top Selling Categories with Quantity and Revenue**  
   Table listing top product categories with their quantity and total revenue.

7. **Slicer for Product Name/Category**  
   Interactive slicer to filter visuals based on selected product name or category.

## Key Insights

- Identified high-performing product categories and SKUs.
- Tracked daily trends to assist in inventory and planning decisions.
- Observed size and style preferences based on contribution to total sales.
- Enabled interactive filtering for in-depth exploration.
  
## Files Used

- `Task_2.pbix` – Power BI dashboard file
- `amazon_sales_datasheet.csv` – Raw dataset used for analysis
- `README.md` – This file (documentation for Task 2)

## Tools & Technologies

- Power BI – For data cleaning, modeling, and visual dashboard creation
- Power Query Editor – Used for preprocessing and transformation steps
