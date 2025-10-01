from backend.services.broker_client import api
from backend.services.risk_service import apply_risk_rules
from backend.database.db import get_db
from datetime import datetime

def log_trade(symbol, side, qty, price, status):
    conn = get_db()
    conn.execute(
        "INSERT INTO trades (symbol, side, qty, price, timestamp, status) VALUES (?, ?, ?, ?, ?, ?)",
        (symbol, side, qty, price, datetime.utcnow().isoformat(), status)
    )
    conn.commit()

def place_order(symbol: str, qty: int, side: str):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side.lower(),
            type="market",
            time_in_force="gtc"
        )
        log_trade(symbol, side, qty, float(api.get_last_trade(symbol).price), "success")
        return {"status": "success", "order_id": order.id}
    except Exception as e:
        log_trade(symbol, side, qty, 0.0, f"error: {str(e)}")
        return {"status": "error", "message": str(e)}

def execute_trade(symbol: str, signal: str, confidence: float):
    qty = apply_risk_rules(symbol, signal, confidence)
    if qty > 0:
        return place_order(symbol, qty, signal)
    return {"status": "skipped", "reason": "did not pass risk rules"}
