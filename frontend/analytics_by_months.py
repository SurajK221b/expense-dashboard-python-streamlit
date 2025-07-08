import streamlit as st
import requests
import pandas as pd
import numpy as np
import altair as alt

API_URL = "http://localhost:8000"

def analytics_months_tab():
    st.markdown("## 📅 Expense Analytics Dashboard")

    # Fetch monthly summary (total per month)
    try:
        response = requests.get(f"{API_URL}/monthly_summary/")
        response.raise_for_status()
        monthly_summary = response.json()

        if not monthly_summary:
            st.warning("No monthly expense data available.")
            return

        df_monthly = pd.DataFrame(monthly_summary)
        df_monthly.rename(columns={
            "expense_month": "Month Number",
            "month_name": "Month Name",
            "total": "Total"
        }, inplace=True)

        # Sort ascending chronologically
        df_monthly = df_monthly.sort_values("Month Number").reset_index(drop=True)

    except requests.exceptions.RequestException as e:
        st.error(f"🔴 Unable to fetch monthly summary data: {e}")
        return

    # --- Bar Chart: Monthly Expense ---
    st.markdown("### 📊 Monthly Expense — Bar Chart")
    bar_chart_data = df_monthly.set_index("Month Name")["Total"]
    st.bar_chart(bar_chart_data, use_container_width=True)

    # --- Line Chart: Expense Trend ---
    st.markdown("### 📈 Monthly Expense Trend — Line Chart")
    st.line_chart(bar_chart_data, use_container_width=True)

    # --- Area Chart: Cumulative Expense ---
    st.markdown("### 📉 Cumulative Expense Over Time — Area Chart")
    df_monthly["Cumulative Total"] = df_monthly["Total"].cumsum()
    area_chart_data = df_monthly.set_index("Month Name")[["Cumulative Total"]]
    st.area_chart(area_chart_data, use_container_width=True)

    
    # --- Data Table: Monthly Totals ---
    st.markdown("### 📋 Detailed Monthly Expense Table")
    df_display = df_monthly.copy()
    df_display["Total"] = df_display["Total"].map("₹{:,.2f}".format)
    df_display["Cumulative Total"] = df_display["Cumulative Total"].map("₹{:,.2f}".format)
    st.dataframe(df_display.set_index("Month Number"), use_container_width=True)
