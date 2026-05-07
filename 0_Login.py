import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

USERNAME = "admin"
PASSWORD = "1234"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.session_state.logged_in = True
        st.success("Login Successful")
        st.rerun()
    else:
        st.error("Invalid credentials")

if st.session_state.logged_in:
    st.sidebar.success("Logged in ✅")
    st.write("Go to Dashboard or Prediction from sidebar")