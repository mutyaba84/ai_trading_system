from src.trading.auto_scaler import AutoScaler
from fastapi import FastAPI, WebSocket
from src.interfaces.portfolio import portfolio  # your portfolio instance

auto_scaler = AutoScaler(base_size=1, max_risk=0.02)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        # send current PnL, equity, and AI suggested size
        recommended_size = auto_scaler.compute_size(portfolio, portfolio.recent_pnl())
        await ws.send_json({
            "equity": portfolio.total_equity(),
            "cash": portfolio.cash,
            "positions": portfolio.positions,
            "recommended_size": recommended_size,
        })
        await asyncio.sleep(1)  # refresh every second
