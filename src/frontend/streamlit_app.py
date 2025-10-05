import streamlit as st
import requests
import time

st.set_page_config(page_title="AI Trading Dashboard", layout="wide")

st.sidebar.title("Trading Controls")

# Risk parameters
risk_per_trade = st.sidebar.slider("Risk % per trade", 0.1, 5.0, 1.0, 0.1)
stop_loss_atr = st.sidebar.slider("Stop Loss (ATR multiples)", 0.5, 5.0, 2.0, 0.1)

# Refresh interval for live preview
refresh_rate = st.sidebar.slider("Auto-refresh interval (sec)", 5, 60, 15)

st.sidebar.markdown("---")
st.sidebar.subheader("Trade Size Preview (Live)")

# Assets to monitor
symbols = ["BTC-USD", "ETH-USD", "AAPL", "EURUSD"]

preview_container = st.empty()

while True:
    sizes = {}
    for symbol in symbols:
        try:
            response = requests.get(
                f"http://localhost:5000/preview_trade_size/{symbol}",
                params={"risk": risk_per_trade, "stop_loss": stop_loss_atr}
            )
            result = response.json()
            sizes[symbol] = round(result["recommended_size"], 4)
        except:
            sizes[symbol] = "N/A"

    with preview_container.container():
        st.subheader("📊 Risk-Adjusted Trade Sizes")
        for sym, size in sizes.items():
            st.write(f"{sym}: {size} units")

    time.sleep(refresh_rate)
