# Placeholder for backend/routers/risk.py
# backend/routers/risk.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def risk_status():
    return {"status": "Risk management active", "max_drawdown": "5%", "risk_per_trade": "1%"}
