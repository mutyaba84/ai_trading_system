from fastapi import APIRouter
from backend.services.account_service import get_account_info, get_open_positions

router = APIRouter()

@router.get("/")
def account_info():
    return get_account_info()

@router.get("/positions")
def positions():
    return get_open_positions()
