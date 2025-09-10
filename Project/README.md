**Customer Lifetime Value (LTV) Prediction**


**Project Overview**

Customer Lifetime Value (LTV) prediction is a crucial aspect of modern business analytics. It helps companies estimate the long-term value of their customers and make data-driven decisions for marketing, customer retention, and resource allocation.

In this project, we built a machine learning model to predict 12-month LTV for e-commerce customers using historical transaction and behavioral data. The model identifies high-value customers and assists businesses in optimizing marketing spend.

**Objectives**

Analyze customer purchase behavior from e-commerce data.

Engineer meaningful features and custom ratios to capture customer patterns.

Build and train a predictive model for 12-month LTV.

Visualize insights from customer behavior and LTV distribution.

Generate a final CSV file with predicted LTV values for customers.

**Tools & Technologies**

Python

Colab Jupiter Notebook (.ipynb)

Pandas, NumPy → Data preprocessing & feature engineering

Matplotlib, Seaborn → Data visualization

Scikit-learn → Machine learning utilities

XGBoost → Final predictive model

Joblib → Model persistence

**Project Structure**

├── ecommerce_customer_data_custom_ratios.csv   # Processed dataset with engineered features  
├── LTV Prediction.ipynb                        # Jupyter notebook (main analysis & model training)  
├── predicted_ltv_12m.csv                       # Final predictions (12-month LTV values)  
├── xgb_ltv_model.joblib                        # Trained XGBoost model  
└── README.md                                   # Project documentation  

**Workflow**

Data Collection & Cleaning – Preprocessed e-commerce customer data.

Feature Engineering – Added custom ratios (purchase frequency, recency, avg order value).

Exploratory Data Analysis (EDA) – Visualized customer distribution & LTV trends.

Model Training – Built and trained an XGBoost regression model.

Evaluation – Assessed model performance with error metrics.

Prediction & Export – Generated final 12-month LTV predictions as CSV.

**Results**

Successfully trained a robust XGBoost model.

Final predictions saved in predicted_ltv_12m.csv.

Insights highlight that high-value customers often show higher order frequency and early engagement.

**Deliverables**

Python Notebook (LTV Prediction.ipynb) – Model training & visualizations

Trained Model (xgb_ltv_model.joblib)

Predicted CSV (predicted_ltv_12m.csv)

Visualization (Visualization images

Future Enhancements

