# Placeholder for backend/database/models.py
# backend/database/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, func
from database.db import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    side = Column(String)
    qty = Column(Integer)
    price = Column(Float)
    status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
