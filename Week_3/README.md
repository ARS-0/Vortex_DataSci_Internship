# VortexTech Data Science & Analytics Internship - Week 3: **Build an Interactive Dashboard**.

## What this is

An interactive Streamlit dashboard built on the `tips` dataset (243 restaurant bills, with details on tip amount, party size, day, meal time, and smoker status). It lets you filter the data and see the visualizations and data table update live.

## Filters

- **Day of week** (multi-select) — choose any combination of Thur/Fri/Sat/Sun
- **Meal time** (dropdown) — All / Lunch / Dinner
- **Total bill range** (slider) — restrict to bills within a $ range
- **Party size** (slider) — restrict to parties within a size range

## Visualizations (all update live based on the filters above)

1. **Average total bill by day** — bar chart
2. **Total bill vs. tip** — scatter plot, colored by meal time
3. **Distribution of tip percentage** — histogram with density curve
4. **Average tip by party size** — line chart (bonus 4th visualization)

Plus 3 KPI metrics at the top (average bill, average tip, average tip %) and a full **filtered raw data table** at the bottom.

## Contents

- `dashboard.py` — the Streamlit app
- `tips.csv` — the dataset (kept in the same folder as the script, as required)
- `requirements.txt` — Python dependencies

## How to run it

1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd vortextech-datasci-week3
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run dashboard.py
   ```
4. It will open automatically in your browser at `http://localhost:8501`.
