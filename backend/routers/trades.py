from fastapi import APIRouter
from backend.database.db import get_db

router = APIRouter()

@router.get("/")
def get_trades():
    conn = get_db()
    rows = conn.execute("SELECT * FROM trades ORDER BY timestamp DESC").fetchall()
    return [dict(row) for row in rows]
