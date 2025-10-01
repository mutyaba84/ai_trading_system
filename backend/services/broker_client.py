import os
import alpaca_trade_api as tradeapi
import pandas as pd

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")
BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)

def get_historical_data(symbol: str, timeframe="1Day", limit=100):
    bars = api.get_bars(symbol, timeframe, limit=limit).df
    return bars[["close"]].reset_index(drop=True)

def get_last_price(symbol: str):
    return float(api.get_last_trade(symbol).price)
