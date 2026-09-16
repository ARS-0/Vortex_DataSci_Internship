"""
VortexTech Week 3 — Interactive Restaurant Tips Dashboard
Run with: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# Page setup
# ---------------------------------------------------------
st.set_page_config(page_title="Restaurant Tips Dashboard", layout="wide")
st.title("🍽️ Restaurant Tips Dashboard")
st.write(
    "Explore how bill amount, tips, and party size vary across days, "
    "meal times, and customer groups. Use the filters in the sidebar to drill in."
)

# ---------------------------------------------------------
# Load data
# ---------------------------------------------------------
df = pd.read_csv("tips.csv")

# ---------------------------------------------------------
# Sidebar filters
# ---------------------------------------------------------
st.sidebar.header("Filters")

# Filter 1: dropdown (multi-select) for day of week
days = sorted(df["day"].unique().tolist())
selected_days = st.sidebar.multiselect("Day of week", options=days, default=days)

# Filter 2: dropdown for meal time
times = sorted(df["time"].unique().tolist())
selected_time = st.sidebar.selectbox("Meal time", options=["All"] + times)

# Filter 3: slider for total bill range
min_bill, max_bill = float(df["total_bill"].min()), float(df["total_bill"].max())
bill_range = st.sidebar.slider(
    "Total bill range ($)",
    min_value=min_bill,
    max_value=max_bill,
    value=(min_bill, max_bill),
)

# Filter 4: slider for party size
min_size, max_size = int(df["size"].min()), int(df["size"].max())
size_range = st.sidebar.slider(
    "Party size",
    min_value=min_size,
    max_value=max_size,
    value=(min_size, max_size),
)

# ---------------------------------------------------------
# Apply filters
# ---------------------------------------------------------
filtered_df = df[df["day"].isin(selected_days)]

if selected_time != "All":
    filtered_df = filtered_df[filtered_df["time"] == selected_time]

filtered_df = filtered_df[
    (filtered_df["total_bill"] >= bill_range[0])
    & (filtered_df["total_bill"] <= bill_range[1])
    & (filtered_df["size"] >= size_range[0])
    & (filtered_df["size"] <= size_range[1])
]

st.markdown(f"**{len(filtered_df)} of {len(df)} records match your filters.**")

if filtered_df.empty:
    st.warning("No records match the current filters — try widening your selection.")
    st.stop()

# ---------------------------------------------------------
# KPI row
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Average bill", f"${filtered_df['total_bill'].mean():.2f}")
col2.metric("Average tip", f"${filtered_df['tip'].mean():.2f}")
col3.metric("Average tip %", f"{(filtered_df['tip'] / filtered_df['total_bill'] * 100).mean():.1f}%")

st.divider()

# ---------------------------------------------------------
# Visualization 1: Average total bill by day (bar chart)
# ---------------------------------------------------------
st.subheader("Average Total Bill by Day")
avg_bill_by_day = filtered_df.groupby("day", observed=True)["total_bill"].mean().sort_values(ascending=False)
st.bar_chart(avg_bill_by_day)

# ---------------------------------------------------------
# Visualization 2: Total bill vs. tip (scatter plot)
# ---------------------------------------------------------
st.subheader("Total Bill vs. Tip")
fig1, ax1 = plt.subplots(figsize=(7, 4))
sns.scatterplot(data=filtered_df, x="total_bill", y="tip", hue="time", alpha=0.8, ax=ax1)
ax1.set_xlabel("Total Bill ($)")
ax1.set_ylabel("Tip ($)")
ax1.set_title("Total Bill vs. Tip (filtered data)")
st.pyplot(fig1)

# ---------------------------------------------------------
# Visualization 3: Distribution of tip percentage (histogram)
# ---------------------------------------------------------
st.subheader("Distribution of Tip Percentage")
filtered_df = filtered_df.copy()
filtered_df["tip_pct"] = filtered_df["tip"] / filtered_df["total_bill"] * 100
fig2, ax2 = plt.subplots(figsize=(7, 4))
sns.histplot(filtered_df["tip_pct"], bins=20, kde=True, ax=ax2, color="teal")
ax2.set_xlabel("Tip (% of bill)")
ax2.set_ylabel("Count")
ax2.set_title("Tip Percentage Distribution (filtered data)")
st.pyplot(fig2)

# ---------------------------------------------------------
# Visualization 4 (bonus): Average tip by party size (line chart)
# ---------------------------------------------------------
st.subheader("Average Tip by Party Size")
avg_tip_by_size = filtered_df.groupby("size", observed=True)["tip"].mean()
st.line_chart(avg_tip_by_size)

st.divider()

# ---------------------------------------------------------
# Filtered raw data table
# ---------------------------------------------------------
st.subheader("Filtered Raw Data")
st.dataframe(filtered_df, width="stretch")
