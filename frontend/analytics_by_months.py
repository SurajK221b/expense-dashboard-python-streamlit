import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    st.markdown("## 📅 Expense Analytics by Month")

    try:
        response = requests.get(f"{API_URL}/monthly_summary/")
        response.raise_for_status()
        monthly_summary = response.json()

        if not monthly_summary:
            st.warning("No monthly expense data available.")
            return

        df = pd.DataFrame(monthly_summary)

        df.rename(columns={
            "expense_month": "Month Number",
            "month_name": "Month Name",
            "total": "Total"
        }, inplace=True)

        # Sort descending by Month Number (latest first)
        df_sorted = df.sort_values(by="Month Number", ascending=False).reset_index(drop=True)

        # Use raw numeric Total for plotting
        chart_data = df_sorted.set_index("Month Name")["Total"]

        st.markdown("### 📊 Monthly Expense Summary")
        st.bar_chart(chart_data, use_container_width=True)

        # Format Total for display only
        df_sorted_display = df_sorted.copy()
        df_sorted_display["Total"] = df_sorted_display["Total"].map("₹{:,.2f}".format)

        st.markdown("### 📋 Detailed Monthly Expense Table")
        st.dataframe(df_sorted_display.set_index("Month Number"), use_container_width=True)

    except requests.exceptions.RequestException as e:
        st.error(f"🔴 Unable to fetch monthly summary data: {e}")
