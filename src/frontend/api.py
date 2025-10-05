from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

trade_settings = {
    "trade_size": 1,
    "stop_loss": 0.02,
    "take_profit": 0.05,
    "trailing_stop": 0.03
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SettingsUpdate(BaseModel):
    trade_size: float
    stop_loss: float
    take_profit: float
    trailing_stop: float

@app.get("/settings")
def get_settings():
    return trade_settings

@app.post("/settings")
def update_settings(update: SettingsUpdate):
    trade_settings.update(update.dict())
    return {"status": "success", "updated_settings": trade_settings}
