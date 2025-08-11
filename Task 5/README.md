# Titanic Dataset Analysis & Visualization

##  Project Overview
This project focuses on **exploratory data analysis (EDA)** and **visualization** of the Titanic dataset to identify patterns, relationships, and insights about survival rates.  
The main objectives are:
- Understand the dataset structure and contents.
- Perform data cleaning and preprocessing.
- Create meaningful visualizations.
- Identify relationships and trends between features.
- Summarize the key findings.


##  Dataset Information
- **Dataset Name**: Titanic-Dataset.csv  
- **Source**: Kaggle Titanic dataset  
- **Description**: Contains demographic and travel information of passengers aboard the Titanic, along with their survival status.

### **Main Columns Used**
| Column      | Description |
|-------------|-------------|
| PassengerId | Unique passenger identifier |
| Survived    | Survival status (0 = No, 1 = Yes) |
| Pclass      | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) |
| Name        | Passenger name |
| Sex         | Passenger gender |
| Age         | Passenger age |
| SibSp       | # of siblings/spouses aboard |
| Parch       | # of parents/children aboard |
| Ticket      | Ticket number |
| Fare        | Passenger fare |
| Cabin       | Cabin number |
| Embarked    | Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |


##  Tools & Libraries Used
- **Python**
- **Pandas** – Data manipulation
- **NumPy** – Numerical computations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical plotting

##  Methodology
1. **Data Inspection**
   - Used `.info()`, `.describe()`, `.value_counts()` to understand the dataset.
   - Checked for missing values and handled them appropriately.

2. **Data Cleaning**
   - Filled missing age values with median age.
   - Filled missing Embarked values with the most common port.
   - Dropped irrelevant columns where necessary.

3. **Data Visualization**
   - Created various plots to identify trends and patterns.

##  Data Visualization

**Tools used:** `Matplotlib`, `Seaborn`

**Plots Created:**
- **Histograms** for Age, Fare, SibSp, Parch
- **Boxplots** for Age vs Survived & Fare vs Survived
- **Bar plots** for survival by Sex, Pclass, and Embarked
- **Correlation heatmap** for numeric variables
- **Pairplot** to explore feature interactions


##  Observations from Visuals
- **Gender**: Females had a much higher survival rate than males.
- **Class**: 1st class passengers had the highest survival rate, 3rd class the lowest.
- **Age**: Younger passengers had a slightly better chance of survival.
- **Fare**: Higher ticket prices correlated with higher survival probability.
- **Embarked**: Passengers who boarded at 'C' had slightly better survival rates.
- **Family size**: Small families had better survival chances than individuals traveling alone or large families.

##  Final Summary of Findings
- **Gender and ticket class were the strongest predictors** of survival.
- Socio-economic status (Pclass + Fare) influenced survival rates.
- Age and family size showed moderate impact.
- Embarkation port had minor correlation but still provided useful insights.

