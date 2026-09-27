# vortextech-datasci-week4

Week 4 (Advanced/Capstone) submission for the VortexTech Data Science & Analytics Internship Track: **End-to-End Analysis Report**.

## What this is

A full end-to-end analysis of the **Telco Customer Churn** dataset (7,043 customers), built around one business question: *why are customers churning, and what could reduce it?* It goes from raw data through cleaning, exploratory analysis, and a polished stakeholder-ready report with 6 findings and 4 recommendations.

## Contents

- `capstone_report.ipynb` — the full notebook, organized as: Executive Summary → Methodology → Key Findings (with visuals) → Recommendations → Appendix (full cleaning & EDA code, for technical readers)
- `capstone_report_stakeholder.pdf` / `.html` — a **polished, code-free export** of the same report, suitable for a non-technical business audience (all code is hidden except in the notebook's Appendix)
- `Telco-Customer-Churn.csv` — the dataset (7,043 rows, IBM's public sample Telco churn data)

## Key findings (see report for full detail and charts)

1. Month-to-month customers churn at **42.7%**, vs. **11.3%** (one-year) and **2.8%** (two-year contracts) — contract length is the strongest churn driver.
2. New customers are highest-risk: **47.4%** churn in their first year, falling to **6.6%** after 5+ years.
3. Fiber optic customers churn at **41.9%**, more than double DSL customers (**19.0%**).
4. Customers without Tech Support or Online Security churn at **~42%**, roughly 3x the rate of those with these add-ons (**~15%**).
5. Electronic check payers churn at **45.3%**, far above automatic payment methods (**15–19%**).
6. Churned customers pay more on average (**$74.44/mo**) than retained customers (**$61.27/mo**).

## Recommendations

1. Incentivize longer contracts, especially at sign-up and within the first year.
2. Investigate and improve the fiber optic pricing/reliability experience.
3. Offer a free trial of Tech Support and Online Security to new customers.
4. Nudge electronic-check payers toward automatic payment methods.

## How to run it

1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd vortextech-datasci-week4
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. Open and run the notebook:
   ```bash
   jupyter notebook capstone_report.ipynb
   ```
   (It loads `Telco-Customer-Churn.csv` from the same folder — no other setup needed.)
4. To view the stakeholder-facing version without opening Jupyter, just open `capstone_report_stakeholder.pdf` or `.html` directly.
