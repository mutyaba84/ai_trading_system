# ai_core/inference.py
import pandas as pd
import joblib
from feature_engineering import generate_features

def load_model():
    return joblib.load("ai_core/model_store/latest_model.pkl")

def predict_signal(data: pd.DataFrame):
    model = load_model()
    df = generate_features(data)
    X = df[["ma_5", "ma_20", "volatility"]].iloc[-1:].values
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][pred]
    signal = "BUY" if pred == 1 else "SELL"
    return {"signal": signal, "confidence": float(prob)}
