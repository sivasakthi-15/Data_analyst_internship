# 📊 Data Analyst Internship Projects

A collection of data analytics projects completed during my **Data Analyst Internship**, covering the complete data analysis workflow — from data cleaning and exploratory analysis to SQL analytics, Power BI dashboards, and predictive modeling.

The projects demonstrate hands-on experience with **Python, Pandas, SQL, PostgreSQL, SQLite, Power BI, Power Query, DAX, Machine Learning, XGBoost, and SHAP**.

---

## 🚀 Internship Overview

During this internship, I worked on multiple datasets and business problems involving:

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* SQL Data Analysis
* Relational Database Queries
* Sales & E-commerce Analytics
* Interactive Power BI Dashboards
* Power Query Transformations
* DAX Measures & Calculations
* Customer Segmentation & Behavioral Analysis
* Predictive Analytics
* Customer Lifetime Value (LTV) Prediction
* Model Evaluation & Explainability

---

# 🗂️ Projects

## 1. 🧹 Netflix Data Cleaning

**Tools:** Python, Pandas

Cleaned and prepared the Netflix Movies and TV Shows dataset for analysis.

### Key Tasks

* Inspected dataset structure and data types
* Identified and removed duplicate records
* Handled missing values
* Standardized categorical columns
* Cleaned text fields
* Converted date columns into appropriate formats
* Standardized column names
* Prepared the dataset for downstream analysis

### Skills Demonstrated

`Python` `Pandas` `Data Cleaning` `Data Preprocessing`

---

# 2. 📈 Sales Performance Dashboard

**Tools:** Power BI, Power Query

Built an interactive sales dashboard to analyze product and sales performance.

### Analysis Included

* Sales by product category
* Sales by SKU
* Sales by size
* Sales contribution by style
* Daily sales trends
* Top-performing categories
* Interactive product and category filters

### Skills Demonstrated

`Power BI` `Power Query` `Data Visualization` `Dashboard Development`

---

# 3. 📊 Advanced Sales Analytics Dashboard

**Tools:** Power BI, DAX, Power Query

Developed an advanced sales-performance dashboard to analyze revenue, profitability, customer segments, regions, and product performance.

### KPIs

* Total Sales
* Total Profit
* Total Orders
* Average Discount

### Analysis Included

* Sales trends over time
* Sales by category and region
* Sub-category contribution
* Profit by customer segment
* Orders by region
* Sales vs. Profit analysis
* Discount and profitability analysis

### Skills Demonstrated

`Power BI` `DAX` `Power Query` `KPI Analysis` `Business Intelligence`

---

# 4. 🛒 Brazilian E-commerce SQL Analysis

**Tools:** PostgreSQL, SQL

Analyzed the **Brazilian E-Commerce Public Dataset by Olist** using PostgreSQL.

### Analysis Included

* Orders by customer state
* Top-selling products
* Revenue by product category
* Monthly order trends
* Order-status distribution
* High-frequency customers
* Average delivery time
* Highest-value orders
* Top sellers by revenue
* Products with no sales
* Average freight value by state
* Monthly revenue trends

### SQL Concepts Used

* `SELECT`
* `WHERE`
* `JOIN`
* `GROUP BY`
* `HAVING`
* `COUNT()`
* `SUM()`
* `AVG()`
* `ORDER BY`
* `LIMIT`
* `DATE_TRUNC()`
* Aggregation and filtering

### Skills Demonstrated

`SQL` `PostgreSQL` `Data Analysis` `E-commerce Analytics` `Business Insights`

---

# 5. 🚢 Titanic Exploratory Data Analysis

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn

Performed exploratory data analysis on the Titanic passenger dataset to understand the factors associated with passenger survival.

### Analysis Included

* Dataset exploration
* Missing-value analysis
* Statistical summaries
* Age and fare distributions
* Outlier analysis
* Survival by gender
* Survival by passenger class
* Survival by embarkation port
* Correlation analysis
* Age vs. survival
* Fare vs. survival

### Key Findings

* Female passengers had substantially higher survival rates than male passengers.
* First-class passengers had higher survival rates than second- and third-class passengers.
* Fare showed a positive relationship with survival.
* Passenger class and gender were important factors associated with survival.

### Skills Demonstrated

`Python` `Pandas` `EDA` `Data Visualization` `Statistics`

---

# 6. 💰 SQL Sales Trend Analysis

**Tools:** PostgreSQL, SQL

Analyzed sales transaction data to identify revenue and order trends over time.

### Key Analysis

* Monthly sales analysis
* Year and month extraction
* Revenue calculation
* Order-volume analysis
* Product-level analysis
* Category-level analysis
* Customer and demographic analysis

### Example Revenue Calculation

```text
Revenue = Quantity × Price
```

Monthly revenue was calculated using SQL aggregation and date-based grouping.

### Skills Demonstrated

`SQL` `PostgreSQL` `Aggregation` `Time-Series Analysis` `Sales Analytics`

---

# 7. 🗄️ Python + SQLite Sales Analysis

**Tools:** Python, SQLite, SQL, Pandas, Matplotlib

Created a lightweight sales-analysis pipeline using SQLite and Python.

### Workflow

```text
Sales Data
    ↓
SQLite Database
    ↓
SQL Queries
    ↓
Pandas DataFrame
    ↓
Aggregation
    ↓
Business Metrics
    ↓
Visualization
```

### Metrics Generated

* Total quantity sold
* Total revenue
* Revenue by product
* Top-performing products
* Sales visualization

### Example

The analysis identified **Laptop** as the highest-revenue product in the sample dataset.

### Skills Demonstrated

`Python` `SQLite` `SQL` `Pandas` `Matplotlib` `Data Analysis`

---

# 8. 📊 Interactive Sales Dashboard

**Tools:** Power BI

Created an interactive dashboard to analyze sales and profitability across different dimensions.

### Dashboard Analysis

* Monthly sales trends
* Regional performance
* Category contribution
* Profitability
* Customer contribution
* Discount impact
* Top customers

### Business Insights

The dashboard was designed to help identify:

* High-performing regions
* High-performing categories
* Revenue trends
* Profitability differences
* Effects of discounting
* High-value customers

### Skills Demonstrated

`Power BI` `Data Visualization` `Dashboarding` `Business Analytics`

---

# 9. 🤖 Customer Lifetime Value Prediction

**Tools:** Python, Pandas, Scikit-learn, XGBoost, SHAP

A predictive analytics project focused on estimating customers' **future 12-month spending** based on historical transaction behavior.

## 🎯 Business Problem

Businesses need to identify customers who are likely to generate high future revenue so they can prioritize:

* Customer retention
* Marketing campaigns
* Personalized offers
* Customer targeting
* Resource allocation

The goal of this project was to predict each customer's expected spending over the following **12 months**.

---

## 📊 Dataset

The project uses approximately **250,000 transaction records**.

The data contains customer, transaction, product, demographic, payment, and behavioral information.

---

## 🔧 Data Preparation

The workflow included:

* Loading transaction data
* Data type conversion
* Date processing
* Column standardization
* Missing-value handling
* Customer-level aggregation
* Observation and prediction window creation

---

## 🧠 Feature Engineering

Customer-level behavioral features were created from historical transactions.

### Recency

Number of days since the customer's most recent purchase.

### Frequency

Number of orders made by the customer.

### Monetary Value

Total historical customer spending.

### Average Order Value

```text
Average Order Value = Total Spending / Number of Orders
```

### Customer Tenure

Time between the customer's first and most recent purchase.

### Orders per Month

Measures purchasing frequency relative to customer tenure.

### Returns Ratio

Measures the proportion of customer purchases associated with returns.

### Product Category Diversity

Measures the number of different product categories purchased.

Additional features included:

* Quantity
* Customer age
* Gender
* Payment method
* Other customer behavioral attributes

---

## 🎯 Target Variable

The target variable was:

```text
future_spend_12m
```

representing the customer's total spending during the following 12-month prediction period.

Customers without future purchases were assigned a future spend of zero.

---

## 📐 Target Transformation

Because customer spending can be highly skewed, the target was transformed using:

```text
log1p()
```

Predictions were converted back to the original scale using:

```text
expm1()
```

This helps reduce the influence of extreme spending values during model training.

---

## 🤖 Machine Learning Model

### XGBoost Regression

The project uses **XGBoost** to model the nonlinear relationship between historical customer behavior and future spending.

Important model settings included:

* Learning rate: `0.05`
* Maximum depth: `6`
* Subsample: `0.8`
* Column sampling: `0.8`
* Early stopping

The dataset was divided into:

* 70% Training
* 15% Validation
* 15% Testing

---

## 📏 Model Evaluation

The model was evaluated using:

### MAE

Mean Absolute Error measures the average absolute difference between actual and predicted future spending.

### RMSE

Root Mean Squared Error gives greater weight to larger prediction errors.

### R²

R² measures the proportion of variation in future spending explained by the model.

---

## 📈 Business Evaluation

In addition to traditional ML metrics, the project evaluates **Top-10% Customer Capture**.

Customers are ranked according to predicted LTV, and the analysis measures how much actual future revenue is captured by targeting the top 10% of predicted customers.

This connects model performance with a practical customer-marketing use case.

---

## 🔍 Model Explainability

**SHAP (SHapley Additive exPlanations)** was used to understand feature importance and explain the model's predictions.

This helps answer:

> Which customer characteristics have the greatest influence on predicted future spending?

---

## 📊 Visualizations

The project includes:

* SHAP feature importance
* Actual vs. predicted spending
* Predicted LTV distribution
* Customer lift curve

---

# 🛠️ Technology Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Databases

* PostgreSQL
* SQLite

### Business Intelligence

* Power BI
* Power Query
* DAX

### Machine Learning

* Scikit-learn
* XGBoost

### Explainable AI

* SHAP

### Model Management

* Joblib

---

# 📚 Key Skills Gained

Through these projects, I developed practical experience in:

* Data Cleaning
* Data Wrangling
* Exploratory Data Analysis
* SQL Querying
* Database Analysis
* Data Visualization
* Dashboard Development
* Business Intelligence
* Feature Engineering
* Predictive Analytics
* Regression Modeling
* Model Evaluation
* Explainable Machine Learning
* Business-oriented Data Analysis

---

# 🔄 End-to-End Analytics Workflow

The overall internship followed an end-to-end data analytics workflow:

```text
              Raw Data
                  ↓
        Data Understanding
                  ↓
          Data Cleaning
                  ↓
       Data Transformation
                  ↓
       ┌──────────┴──────────┐
       ↓                     ↓
     SQL                  Python
       ↓                     ↓
       └──────────┬──────────┘
                  ↓
                 EDA
                  ↓
          Business Analysis
                  ↓
       ┌──────────┴──────────┐
       ↓                     ↓
   Power BI            Machine Learning
       ↓                     ↓
  Dashboards          Predictions
       ↓                     ↓
       └──────────┬──────────┘
                  ↓
           Business Insights
```

---

# 📁 Repository Structure

```text
Data-Analyst-Internship/
│
├── Task-1-Netflix-Data-Cleaning/
│
├── Task-2-Sales-PowerBI/
│
├── Task-3-Advanced-Sales-Analytics/
│
├── Task-4-Olist-SQL-Analysis/
│
├── Task-5-Titanic-EDA/
│
├── Task-6-SQL-Sales-Analysis/
│
├── Task-7-Python-SQLite-Analysis/
│
├── Task-8-PowerBI-Dashboard/
│
└── Customer-LTV-Prediction/
    ├── LTV Prediction.ipynb
    ├── ecommerce_customer_data_custom_ratios.csv
    ├── xgb_ltv_model.joblib
    ├── predicted_ltv_12m.csv
    └── visualizations/
```

---

# 🎯 Internship Outcome

This internship provided hands-on exposure to the complete analytics lifecycle:

**Collect → Clean → Transform → Analyze → Visualize → Model → Evaluate → Communicate Insights**

The projects strengthened my ability to work with both structured business data and real-world analytical problems using Python, SQL, Power BI, and Machine Learning.

---

## 👨‍💻 Author

**Sivasakthi R**

B.Tech — Artificial Intelligence and Data Science

### Areas of Interest

* Data Analytics
* Data Science
* Machine Learning
* Business Intelligence
* Artificial Intelligence

---

⭐ If you find this repository useful, feel free to explore the individual projects and notebooks.
