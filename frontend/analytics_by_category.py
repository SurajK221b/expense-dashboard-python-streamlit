import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import altair as alt

API_URL = "http://localhost:8000"

def analytics_category_tab():
    st.markdown("## 📊 Expense Analytics by Category")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("📅 Start Date", datetime(2025, 1, 1))
    with col2:
        end_date = st.date_input("📅 End Date", datetime(2025, 1, 31))

    if st.button("🔍 Get Analytics"):
        if start_date > end_date:
            st.error("❌ Start date must be before end date.")
            return

        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        try:
            response = requests.post(f"{API_URL}/analytics/", json=payload)
            response.raise_for_status()
            result = response.json()

            if not result:
                st.warning("No expenses found in the selected date range.")
                return

            data = {
                "Category": list(result.keys()),
                "Total": [result[cat]["total"] for cat in result],
                "Percentage": [result[cat]["percentage"] for cat in result]
            }

            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by="Percentage", ascending=False)

            # --- Existing Bar Chart (Percentage) ---
            st.markdown("### 📊 Category-wise Expense Distribution — Bar Chart")
            st.bar_chart(df_sorted.set_index("Category")["Percentage"], use_container_width=True)

            # # --- Additional Pie Chart ---
            # st.markdown("### 🥧 Category-wise Expense Distribution — Pie Chart")
            # pie_chart = alt.Chart(df_sorted).mark_arc(innerRadius=50).encode(
            #     theta=alt.Theta(field="Percentage", type="quantitative"),
            #     color=alt.Color(field="Category", type="nominal", legend=alt.Legend(title="Category")),
            #     tooltip=[
            #         alt.Tooltip("Category", type="nominal"),
            #         alt.Tooltip("Total", type="quantitative", format="₹,.2f"),
            #         alt.Tooltip("Percentage", type="quantitative", format=".2f")
            #     ],
            # ).properties(width=400, height=400)
            # st.altair_chart(pie_chart, use_container_width=True)

            # Format totals and percentages for display in the table
            df_sorted["Total"] = df_sorted["Total"].map("₹{:,.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}%".format)

            st.markdown("### 📄 Detailed Expense Table")
            st.dataframe(df_sorted, use_container_width=True)

        except requests.exceptions.RequestException as e:
            st.error(f"🔴 Failed to fetch analytics: {e}")

# If you want to run this tab standalone for testing, you can call the function here:
if __name__ == "__main__":
    analytics_category_tab()
