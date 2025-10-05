import streamlit as st
import requests

API_URL = "http://localhost:5000"  # your Flask API for trading engine (or direct state link later)

st.set_page_config(page_title="Trading Control Panel", layout="wide")
st.title("⚡ Trading Control Panel")

# Default trade size
default_size = st.slider("Default Trade Size", 0.1, 10.0, 1.0, 0.1)

# Per-asset trade sizes
btc_size = st.number_input("BTC-USD Size", value=1.0, step=0.1)
eth_size = st.number_input("ETH-USD Size", value=1.0, step=0.1)
aapl_size = st.number_input("AAPL Size", value=10.0, step=1.0)
eurusd_size = st.number_input("EURUSD Size", value=1000.0, step=100.0)

if st.button("Update Settings"):
    settings = {
        "default_size": default_size,
        "BTC-USD": btc_size,
        "ETH-USD": eth_size,
        "AAPL": aapl_size,
        "EURUSD": eurusd_size,
    }
    try:
        res = requests.post(f"{API_URL}/set_settings", json=settings)
        if res.status_code == 200:
            st.success("✅ Trading settings updated successfully!")
        else:
            st.error(f"❌ Failed to update settings: {res.text}")
    except Exception as e:
        st.error(f"Connection error: {e}")

if st.button("View Current Settings"):
    try:
        res = requests.get(f"{API_URL}/get_settings")
        st.json(res.json())
    except Exception as e:
        st.error(f"Connection error: {e}")
