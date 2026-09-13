# VortexTech Data Science & Analytics Internship - Week 2: **Exploratory Data Analysis with Insights**.

## What this is

A structured EDA notebook on the `tips` dataset (244 restaurant bills, with numeric columns `total_bill`, `tip`, `size` and categorical columns `sex`, `smoker`, `day`, `time`). It builds a correlation heatmap, scatter plots for the two strongest numeric relationships, a categorical group comparison, and documents 3 specific insights backed by the charts.

## Contents

- `week2_eda.ipynb` — the full analysis notebook (data cleaning recap → correlation heatmap → 2 scatter plots → categorical bar chart → 3 written insights)

## How to run it

1. Clone this repo and open the notebook:
   ```bash
   git clone <your-repo-url>
   cd vortextech-datasci-week2
   ```
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn jupyter
   ```
3. Launch Jupyter and run all cells:
   ```bash
   jupyter notebook vortextech_week2_eda.ipynb
   ```
   (The notebook loads the `tips` dataset directly via `seaborn.load_dataset("tips")`, so no separate data file is needed.)

## Key insights (see notebook for full detail)

1. `total_bill` and `tip` are strongly positively correlated (r ≈ 0.68) — tips scale roughly proportionally with the bill.
2. `total_bill` and `size` correlate at r ≈ 0.60, but per-person spend drops as party size grows past 4–5 people.
3. Average bill on Sunday (~$21.4) is about 25% higher than on Friday (~$17.2), likely reflecting longer weekend group meals vs. quick weekday visits.
