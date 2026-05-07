import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("📊 Loan Risk Dashboard")

# =========================
# 🔐 AUTH CHECK
# =========================
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()
    
st.cache_data.clear()  # Clear cache on page load to ensure fresh data
# =========================
# ✅ LOAD DATA (CACHED)
# =========================
@st.cache_data
def load_data():

    df = pd.read_csv("dashboard_data.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert numeric columns safely
    numeric_cols = [
        "AGE",
        "NETMONTHLYINCOME",
        "Credit_Score",
        "num_times_delinquent"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove invalid rows
    df = df.dropna(subset=numeric_cols)

    return df

df = load_data()

# =========================
# ✅ SIDEBAR FILTERS
# =========================
st.sidebar.header("🔍 Filters")

# -------------------------
# Gender Filter
# -------------------------
gender = st.sidebar.multiselect(
    "Gender",
    df["GENDER"].dropna().unique(),
    default=df["GENDER"].dropna().unique()
)

# -------------------------
# Age Filter
# -------------------------
age_data = df["AGE"].dropna()

age_range = st.sidebar.slider(
    "Age",
    int(age_data.min()),
    int(age_data.max()),
    (
        int(age_data.quantile(0.10)),
        int(age_data.quantile(0.90))
    )
)

# -------------------------
# Income Filter
# -------------------------
income_data = df["NETMONTHLYINCOME"]

income_range = st.sidebar.slider(
    "Income",
    int(income_data.min()),
    int(income_data.max()),
    (
        int(income_data.quantile(0.10)),
        int(income_data.quantile(0.90))
    )
)

# -------------------------
# Credit Score Filter
# -------------------------
credit_data = df["Credit_Score"]

credit_range = st.sidebar.slider(
    "Credit Score",
    int(credit_data.min()),
    int(credit_data.max()),
    (
        int(credit_data.quantile(0.10)),
        int(credit_data.quantile(0.90))
    )
)
# -------------------------
# Delinquency Filter
# -------------------------
delinq_data = df["num_times_delinquent"]

delinq_range = st.sidebar.slider(
    "Delinquencies",
    int(delinq_data.min()),
    int(delinq_data.max()),
    (
        int(delinq_data.min()),
        int(delinq_data.max())
    )
)

# -------------------------
# Reset Button
# -------------------------
if st.sidebar.button("Reset Filters"):
    st.cache_data.clear()
    st.rerun()

# =========================
# ✅ APPLY FILTERS
# =========================
filtered_df = df[
    (df["GENDER"].isin(gender)) &
    (df["AGE"].between(age_range[0], age_range[1])) &
    (df["NETMONTHLYINCOME"].between(income_range[0], income_range[1])) &
    (df["Credit_Score"].between(credit_range[0], credit_range[1])) &
    (df["num_times_delinquent"].between(delinq_range[0], delinq_range[1]))
].copy()

# =========================
# ✅ HANDLE EMPTY DATA
# =========================
if filtered_df.empty:
    st.warning("No data available for selected filters")
    st.stop()

# =========================
# ✅ CREATE SAFE RISK CATEGORY
# =========================
filtered_df["Risk_Category"] = filtered_df[
    "num_times_delinquent"
].apply(
    lambda x: "High Risk" if x > 2 else "Low Risk"
)

# =========================
# ✅ SAFE KPI FUNCTION
# =========================
def safe_metric(series):
    return 0 if series.empty else round(series.mean(), 2)

# =========================
# ✅ KPI CARDS
# =========================
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Filtered Customers",
    len(filtered_df)
)

col2.metric(
    "Total Customers",
    len(df)
)

col3.metric(
    "Avg Income",
    safe_metric(filtered_df["NETMONTHLYINCOME"])
)

col4.metric(
    "Avg Credit Score",
    safe_metric(filtered_df["Credit_Score"])
)

col5.metric(
    "Avg Delinquency",
    safe_metric(filtered_df["num_times_delinquent"])
)
# =========================
# ✅ FAST CHART DATA
# =========================
@st.cache_data
def compute_stats(df):

    credit_dist = df["Credit_Score"].value_counts().sort_index()

    income_distribution = (
        df["NETMONTHLYINCOME"]
        .value_counts(bins=20)
        .sort_index()
    )

    scatter_sample = df.sample(
        min(3000, len(df)),
        random_state=42
    )

    risk_counts = df["Risk_Category"].value_counts()

    gender_counts = df["GENDER"].value_counts()

    return (
        credit_dist,
        income_distribution,
        scatter_sample,
        risk_counts,
        gender_counts
    )

(
    credit_dist,
    income_distribution,
    scatter_sample,
    risk_counts,
    gender_counts
) = compute_stats(filtered_df)

# =========================
# ✅ VISUALS
# =========================

# -------------------------
# Credit Score Distribution
# -------------------------
st.subheader("📈 Credit Score Distribution")
st.bar_chart(credit_dist)

# -------------------------
# Income + Delinquency
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Income Distribution")
    st.bar_chart(income_distribution)

with col2:
    st.subheader("📉 Delinquency vs Credit Score")

    st.scatter_chart(
        scatter_sample[
            ["Credit_Score", "num_times_delinquent"]
        ]
    )

# -------------------------
# Risk Distribution
# -------------------------
st.subheader("⚠️ Risk Distribution")
st.bar_chart(risk_counts)

# -------------------------
# Gender Distribution
# -------------------------
st.subheader("👥 Gender Distribution")
st.bar_chart(gender_counts)

# =========================
# ✅ FILTERED DATA TABLE
# =========================
st.subheader("📋 Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)