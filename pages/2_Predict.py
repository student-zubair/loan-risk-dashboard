import streamlit as st
import pandas as pd
from joblib import load

st.set_page_config(layout="wide")

st.title("🤖 Loan Risk Prediction")
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()
# =========================
# LOAD MODEL + FEATURES
# =========================
model = load("RFC.pkl")
features = load("features.pkl")

input_data = {}

# =========================
# CUSTOMER PROFILE
# =========================
st.subheader("👤 Customer Profile")

col1, col2 = st.columns(2)

with col1:
    input_data["AGE"] = st.slider("Age", 18, 80, 30)
    input_data["NETMONTHLYINCOME"] = st.number_input("Monthly Income", value=20000)
    input_data["Time_With_Curr_Empr"] = st.number_input("Months with Current Employer", value=24)

with col2:
    input_data["Credit_Score"] = st.slider("Credit Score", 300, 900, 650)

    # EDUCATION ENCODING
    education_map = {
        'OTHERS': 0,
        'SSC': 1,
        '12TH': 2,
        'UNDER GRADUATE': 3,
        'GRADUATE': 4,
        'POST-GRADUATE': 5,
        'PROFESSIONAL': 6
    }

    edu = st.selectbox("Education Level", list(education_map.keys()))
    input_data["EDUCATION"] = education_map[edu]

# =========================
# CREDIT BEHAVIOUR
# =========================
st.subheader("💳 Credit Behaviour")

col1, col2 = st.columns(2)

with col1:
    input_data["time_since_recent_payment"] = st.number_input("Days Since Last Payment", value=30)
    input_data["num_std"] = st.number_input("Total Standard Accounts", value=1)
    input_data["num_std_6mts"] = st.number_input("Standard Accounts (Last 6 Months)", value=0)

with col2:
    input_data["time_since_recent_enq"] = st.number_input("Days Since Last Enquiry", value=10)
    input_data["tot_enq"] = st.number_input("Total Enquiries", value=2)
    input_data["enq_L3m"] = st.number_input("Enquiries (Last 3 Months)", value=1)

# =========================
# LOAN BEHAVIOUR
# =========================
st.subheader("📊 Loan Behaviour")

col1, col2 = st.columns(2)

with col1:
    input_data["Total_TL"] = st.number_input("Total Loan Accounts", value=5)
    input_data["pct_of_active_TLs_ever"] = st.slider("% Active Loans", 0.0, 1.0, 0.5)
    input_data["pct_currentBal_all_TL"] = st.slider("% Current Balance", 0.0, 2.0, 0.5)

with col2:
    input_data["pct_tl_open_L12M"] = st.slider("% Loans Opened (12 Months)", 0.0, 1.0, 0.3)
    input_data["pct_tl_closed_L12M"] = st.slider("% Loans Closed (12 Months)", 0.0, 1.0, 0.2)
    input_data["pct_tl_closed_L6M"] = st.slider("% Loans Closed (6 Months)", 0.0, 1.0, 0.1)

# =========================
# RISK EXPOSURE
# =========================
st.subheader("💰 Risk Exposure")

col1, col2 = st.columns(2)

with col1:
    input_data["max_unsec_exposure_inPct"] = st.number_input("Max Unsecured Exposure (%)", value=20.0)

with col2:
    input_data["pct_opened_TLs_L6m_of_L12m"] = st.slider("% Loans Opened (6M vs 12M)", 0.0, 1.0, 0.5)

# =========================
# AUTO-FILL REMAINING FEATURES
# =========================
for col in features:
    if col not in input_data:
        input_data[col] = 0

# =========================
# PREDICTION
# =========================
if st.button("Predict"):

    input_df = pd.DataFrame([input_data])

    # Ensure correct feature order
    input_df = input_df[features]

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("📊 Prediction Result")

    if prediction[0] == 0:
        st.success(f"✅ Low Risk Customer (Approved)\n\nRisk Score: {probability:.2f}")
    else:
        st.error(f"⚠️ High Risk Customer (Rejected)\n\nRisk Score: {probability:.2f}")