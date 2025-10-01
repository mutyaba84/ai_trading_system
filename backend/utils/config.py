from pydantic import BaseSettings

class Settings(BaseSettings):
    alpaca_api_key: str
    alpaca_secret_key: str
    alpaca_base_url: str = "https://paper-api.alpaca.markets"
    database_url: str = "sqlite:///trades.db"
    max_drawdown: float = 0.05
    risk_per_trade: float = 0.01

    class Config:
        env_file = ".env"

settings = Settings()
