import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab
from custom_report import custom_reports_tab

# --- Page Configuration ---
st.set_page_config(
    page_title="Expense Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Title Section ---
st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>💼 Expense Management Dashboard</h1>
    <h5 style='text-align: center; color: #5D6D7E;'>Track, manage, and analyze your personal or business expenses with precision</h5>
    <hr style='margin-top: 0;'>
""", unsafe_allow_html=True)

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "➕ Add / Update Expenses", 
    "📊 Analytics by Category", 
    "📅 Analytics by Month",
    "📄 Custom Report"
])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()

with tab4:
    custom_reports_tab()