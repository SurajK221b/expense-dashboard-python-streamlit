import streamlit as st
import requests
import pandas as pd
import datetime

API_URL = "http://localhost:8000"

def custom_reports_tab():
    st.markdown("## 📝 Custom Expense Reports")

    # Filters
    today = datetime.date.today()
    start_of_year = datetime.date(today.year, 1, 1)
    end_of_year = datetime.date(today.year, 12, 31)
    start_date = st.date_input("Start Date", value=start_of_year)
    end_date = st.date_input("End Date", value=end_of_year)
    categories = st.multiselect("Categories", options=["Rent", "Food", "Shopping", "Entertainment", "Other"])

    if "custom_report_data" not in st.session_state:
        st.session_state.custom_report_data = None

    if st.button("Search"):
        if not start_date or not end_date:
            st.error("Both Start Date and End Date are required.")
            return

        payload = {
            "date_range": {
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d")
            }
        }
        if categories:
            payload["categories"] = categories

        try:
            response = requests.post(f"{API_URL}/reports", json=payload)
            response.raise_for_status()
            data = response.json()

            if not data:
                st.warning("No expenses found for the selected criteria.")
                st.session_state.custom_report_data = None
                return

            st.session_state.custom_report_data = pd.DataFrame(data)

        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch reports: {e}")
            st.session_state.custom_report_data = None

    df = st.session_state.custom_report_data
    if df is not None:
        # Sorting widgets outside the button block
        sort_column = st.selectbox("Sort By", options=df.columns.tolist(), index=df.columns.get_loc("expense_date"))
        ascending = st.checkbox("Ascending", value=True)
        df_sorted = df.sort_values(by=sort_column, ascending=ascending)

        st.dataframe(df_sorted, use_container_width=True)

        # Export option
        csv = df_sorted.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="custom_expense_report.csv",
            mime="text/csv"
        )
