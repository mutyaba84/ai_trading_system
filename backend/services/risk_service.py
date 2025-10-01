from backend.services.broker_client import api
from utils.config import settings

MAX_RISK_PER_TRADE = settings.risk_per_trade
CONF_THRESHOLD = 0.65

def get_account_balance():
    account = api.get_account()
    return float(account.cash)

def apply_risk_rules(symbol: str, signal: str, confidence: float):
    if confidence < CONF_THRESHOLD:
        return 0

    balance = get_account_balance()
    risk_amount = balance * MAX_RISK_PER_TRADE
    price = float(api.get_last_trade(symbol).price)
    qty = int(risk_amount / price)
    return max(qty, 0)
