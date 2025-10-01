# Placeholder for backend/routers/monitoring.py
# backend/routers/monitoring.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"system": "healthy", "status": "running"}
