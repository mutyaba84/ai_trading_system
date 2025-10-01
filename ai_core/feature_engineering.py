# Placeholder for ai_core/feature_engineering.py
# ai_core/feature_engineering.py
import pandas as pd
import numpy as np

def generate_features(df: pd.DataFrame) -> pd.DataFrame:
    """Generate features like returns, moving averages, volatility."""
    df["return"] = df["close"].pct_change()
    df["ma_5"] = df["close"].rolling(5).mean()
    df["ma_20"] = df["close"].rolling(20).mean()
    df["volatility"] = df["return"].rolling(10).std()
    df = df.dropna()
    return df
