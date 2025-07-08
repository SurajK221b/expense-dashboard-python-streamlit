import streamlit as st
from datetime import datetime
import requests

# --- Backend API endpoint ---
API_URL = "http://localhost:8000"  # Update if hosted elsewhere


def add_update_tab():
    # --- Page layout ---
    st.set_page_config(page_title="Add / Update Expenses", layout="wide")

    # --- Title ---
    st.markdown("## ➕ Add / Update Expenses")
    st.markdown("Use this form to enter or modify your daily expenses. Maximum 5 entries allowed per day.")

    # --- Date selection ---
    selected_date = st.date_input("📅 Select Date", value=datetime(2025, 1, 1))

    # --- Fetch existing data ---
    try:
        response = requests.get(f"{API_URL}/expenses/{selected_date}")
        response.raise_for_status()
        existing_expenses = response.json()
    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
        existing_expenses = []

    # --- Categories ---
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    # --- Expense Entry Form ---
    with st.form("expense_form"):
        st.write("### Enter Expenses")

        expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i].get("amount", 0.0)
                category = existing_expenses[i].get("category", "Shopping")
                notes = existing_expenses[i].get("notes", "")
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns([1.5, 1.5, 3])

            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=amount,
                    key=f"amount_{i}"
                )

            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"category_{i}"
                )

            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"notes_{i}"
                )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        st.markdown("---")
        submit_button = st.form_submit_button("💾 Submit Expenses")

        if submit_button:
            filtered_expenses = [e for e in expenses if e["amount"] > 0]

            if not filtered_expenses:
                st.warning("⚠️ No valid expenses to submit.")
            else:
                try:
                    post_response = requests.post(
                        f"{API_URL}/expenses/{selected_date}",
                        json=filtered_expenses
                    )
                    post_response.raise_for_status()
                    st.success("✅ Expenses updated successfully.")
                except Exception as ex:
                    st.error(f"❌ Failed to update expenses: {ex}")
