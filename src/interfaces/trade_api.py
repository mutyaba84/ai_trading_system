from flask import Flask, request, jsonify

app = Flask(__name__)

# Shared trade settings (default values)
trade_settings = {
    "default_size": 1.0,
    "BTC-USD": 1.0,
    "ETH-USD": 1.0,
    "AAPL": 10.0,
    "EURUSD": 1000.0,
    "account_balance": 100000.0,   # starting capital
    "max_risk_pct": 2.0,          # risk per trade (percentage of balance)
}

@app.route("/set_settings", methods=["POST"])
def set_settings():
    new_settings = request.get_json()
    for key, val in new_settings.items():
        trade_settings[key] = val
    return jsonify({"message": "Updated settings", "settings": trade_settings})

@app.route("/get_settings", methods=["GET"])
def get_settings():
    return jsonify(trade_settings)

# Helper for trading engine
def get_trade_size(symbol: str, stop_loss_distance: float = None):
    """
    Returns trade size based on settings.
    If stop_loss_distance is given, use risk-based sizing.
    """
    account_balance = trade_settings["account_balance"]
    risk_pct = trade_settings["max_risk_pct"]

    # If risk-based sizing is possible
    if stop_loss_distance and stop_loss_distance > 0:
        risk_amount = (risk_pct / 100.0) * account_balance
        # Position size = max risk allowed / stop distance
        size = risk_amount / stop_loss_distance
        return max(1, round(size, 4))

    # Otherwise fallback to fixed trade size
    return trade_settings.get(symbol, trade_settings["default_size"])
