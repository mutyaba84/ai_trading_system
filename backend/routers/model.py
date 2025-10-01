from fastapi import APIRouter
import pandas as pd
from ai_core.ensemble import ensemble_predict
from backend.services.broker_client import get_historical_data

router = APIRouter()

@router.get("/predict")
def predict(symbol: str):
    data = get_historical_data(symbol, timeframe="1Day", limit=50)
    result = ensemble_predict(data)
    return {
        "symbol": symbol,
        "prediction": result["signal"],
        "confidence": result["confidence"]
    }
