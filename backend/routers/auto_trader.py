from fastapi import APIRouter
from backend.services.trade_service import execute_trade
from backend.services.broker_client import get_historical_data
from ai_core.ensemble import ensemble_predict

router = APIRouter()

@router.post("/")
def auto_trade(symbol: str):
    data = get_historical_data(symbol, timeframe="1Day", limit=50)
    result = ensemble_predict(data)
    trade_result = execute_trade(symbol, result["signal"], result["confidence"])
    return {
        "symbol": symbol,
        "ai_signal": result,
        "trade_result": trade_result
    }
