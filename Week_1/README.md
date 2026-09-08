VortexTech Data Science Internship – Week 1: Data Cleaning & Basic Visualization
Overview

This project is the Week 1 task for the VortexTech Data Science Internship. It focuses on cleaning a real-world dataset and preparing it for analysis and visualization.

Dataset

Titanic Passenger Dataset — 891 rows, 12 columns, sourced from the classic Kaggle Titanic competition dataset. It contains a mix of numeric columns (Age, Fare) and categorical columns (Sex, Pclass, Embarked, Survived), making it well suited for practicing data cleaning techniques.

Files in this Repository
titanic.csv — the original, unmodified dataset
titanic_cleaned.csv — the dataset after cleaning
week1_data_cleaning.ipynb — Jupyter notebook containing all cleaning steps with explanations
README.md — this file
Data Cleaning Steps Performed
Inspected the data using .info() and .shape to understand structure, column types, and non-null counts.
Checked for missing values with .isnull().sum(). Found missing data in:
Age (177 missing, ~20%) → filled with the median age (robust to outliers, preserves all rows)
Cabin (687 missing, ~77%) → dropped the column entirely (too sparse to impute reliably)
Embarked (2 missing) → filled with the mode (most frequent port)
Checked for duplicate rows using .duplicated() and removed any found with .drop_duplicates().
Fixed incorrect data types — converted Survived, Pclass, Sex, and Embarked from raw numbers/generic objects into proper category types, since they represent labels rather than continuous quantities.
Verified the result — confirmed no missing values remain and all data types are appropriate, then saved the cleaned dataset to titanic_cleaned.csv.
How to Run
Install the required libraries:
   pip install pandas jupyter
Launch the notebook:
   jupyter notebook week1_data_cleaning.ipynb
Run all cells from top to bottom.
Author

Abdul Rehman Shahid — VortexTech Data Science Intern
