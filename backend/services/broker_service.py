# backend/services/broker_client.py
import os
import alpaca_trade_api as tradeapi
import pandas as pd

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")
BASE_URL = "https://paper-api.alpaca.markets"  # Switch to live when ready

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)

def get_historical_data(symbol: str, timeframe="1Day", limit=100):
    """Fetch OHLCV data from Alpaca."""
    bars = api.get_bars(symbol, timeframe, limit=limit).df
    return bars[["close"]].reset_index(drop=True)
