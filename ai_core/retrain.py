# ai_core/retrain.py
import pandas as pd
from backend.services.broker_client import get_historical_data
from ai_core.train import train_model

def retrain(symbol: str = "AAPL", limit: int = 200):
    data = get_historical_data(symbol, limit=limit)
    train_model(data)

if __name__ == "__main__":
    retrain("AAPL")
    print("✅ Retraining complete")
