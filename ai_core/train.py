# ai_core/train.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from feature_engineering import generate_features

def train_model(data: pd.DataFrame):
    df = generate_features(data)
    df["target"] = (df["return"].shift(-1) > 0).astype(int)  # 1 if price goes up

    X = df[["ma_5", "ma_20", "volatility"]]
    y = df["target"]

    model = LogisticRegression()
    model.fit(X, y)

    joblib.dump(model, "ai_core/model_store/latest_model.pkl")
    print("✅ Model trained and saved.")
