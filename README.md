# Data_analyst_internship
# Task-1
# Netflix Movies and TV Shows Data Cleaning – Internship Task

Welcome to my data cleaning project for the Netflix Movies and TV Shows dataset.  
This task is part of my **Data Analyst Internship submission**, where I applied essential data preprocessing techniques using Python and Pandas.

## What This Project Does

This project focuses on cleaning a real-world dataset to make it ready for analysis.  
The original dataset includes information about movies and TV shows available on Netflix.

Here’s what I did:

### 1. Identified Missing Values
- Used `.isnull().sum()` to check for missing data in columns like `director`, `cast`, `country`, etc.
- Left them untouched for now to preserve raw insight, but they can be filled with `"Unknown"` if needed.

### 2. Removed Duplicate Records
- Used `.drop_duplicates()` to clean up repeated rows and keep the dataset unique.

### 3. Standardized Text Fields
- Cleaned up `type`, `country`, and `rating` columns by removing extra spaces and making them consistent in formatting.

### 4. Converted Date Formats
- Converted `date_added` column into a proper date format: **`dd-mm-yyyy`**.

### 5. Renamed Columns for Clarity
- Changed column names to lowercase and used snake_case formatting (e.g., `release_year`, `date_added`).

### 6. Checked and Fixed Data Types
- Ensured `release_year` is an integer.
- Converted `title` and `type` columns to strings.
- Cleaned date format as string output for easier viewing.

## How to Use

To run this project on your local machine:

```bash
git clone https://github.com/sivasakthi-15/Data_analyst_internship.git
cd Data_analyst_internship
python clean_netflix_data.py
