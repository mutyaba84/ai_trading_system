# backend/models/trade.py
from pydantic import BaseModel
from datetime import datetime

class Trade(BaseModel):
    id: int
    symbol: str
    side: str
    qty: int
    price: float
    timestamp: datetime
    status: str
