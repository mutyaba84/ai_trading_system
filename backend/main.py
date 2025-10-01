from fastapi import FastAPI
from routers import trades, risk, model, auto_trader, account

app = FastAPI(title="AI Trading System", version="0.1.0")

app.include_router(trades.router, prefix="/trades", tags=["Trades"])
app.include_router(risk.router, prefix="/risk", tags=["Risk"])
app.include_router(model.router, prefix="/model", tags=["AI Model"])
app.include_router(auto_trader.router, prefix="/auto_trade", tags=["Auto Trader"])
app.include_router(account.router, prefix="/account", tags=["Account"])

@app.get("/")
def root():
    return {"message": "AI Trading System Backend is running 🚀"}
