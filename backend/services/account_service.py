from backend.services.broker_client import api

def get_account_info():
    account = api.get_account()
    return {
        "cash": float(account.cash),
        "buying_power": float(account.buying_power),
        "equity": float(account.equity),
        "portfolio_value": float(account.portfolio_value),
        "status": account.status
    }

def get_open_positions():
    positions = api.list_positions()
    return [
        {
            "symbol": p.symbol,
            "qty": float(p.qty),
            "side": "long" if float(p.qty) > 0 else "short",
            "avg_entry_price": float(p.avg_entry_price),
            "market_value": float(p.market_value),
            "unrealized_pl": float(p.unrealized_pl)
        }
        for p in positions
    ]
