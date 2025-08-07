# Task 3 - Power BI Sales Dashboard

##  Project Title: Sales Performance Analysis Dashboard

This Power BI project focuses on analyzing the performance of a fictional sales dataset. The dashboard provides insights into sales, profit, discounts, and order timelines, helping businesses make data-driven decisions.

###  Objectives:
- Understand and clean the dataset.
- Build an interactive Power BI dashboard.
- Visualize key performance metrics like **Sales Growth**, **Order Trends**, **Profit**, and **Discount**.
- Help stakeholders identify high/low-performing categories, customer segments, and discount impact.

##  Dataset
- **Source**: Provided sample data (Excel file)
- **Contents**: Order Date, Region, Category, Sales, Profit, Discount, Customer Segment, and more.


##  Data Cleaning Steps:
1. Removed unnecessary columns.
2. Checked and filled null values.
3. Converted data types (e.g., Date columns).
4. Added new columns using Power Query:
   - `OrderMonthYear` – formatted as MMM YYYY.
   - `Sales Growth` – calculated using DAX for month-on-month comparison.


##  Dashboard Pages & Charts

###  Page 1: Overview Dashboard
- **Total Sales**
- **Total Profit**
- **Total Orders**
- **Avg. Discount**
- **Line Chart**: Sales Trend over `OrderMonthYear`
- **Clustered Bar Chart**: Sales by Category and Region
- **Donut Chart**: Sales Share by Sub-Category
- **Pie Chart**: Profit Share by Segment
- **Column Chart**: Orders by Region
- **Line and Stacked Column Chart**: Sales and Profit

###  Page 2: Deep Dive - Sales Growth & Profitability
- **Scatter Chart**:
  - Title: `Count of OrderMonthYear and SalesGrowth by Profit and Discount`
  - X-axis: Profit
  - Y-axis: Discount
  - Size: Sales Growth
  - Color: OrderMonthYear
- Highlights how profit and discount influence sales performance and growth over time.

## Key Insights:
- Sales peaked during [Month-Year with peak value].
- High discounts often reduce overall profit.
- Top-performing category: [Insert from your chart]
- Segment with highest sales: [Insert from your chart]

##  Tools Used:
- **Microsoft Power BI**
- Power Query
- DAX
- 
##  How to View This Dashboard:
1. Open the Power BI `.pbix` file located in this folder.
2. Explore both pages of the report for full insights.
3. Use slicers and filters to analyze specific segments or time periods.

## Author
- **Sivasakthi Ramasamy**
- Pre-final year AI & Data Science Student


## 🔗 Connect With Me
- LinkedIn: [your-linkedin-profile](www.linkedin.com/in/sivasakthi-ramasamy-b21ab2281)



