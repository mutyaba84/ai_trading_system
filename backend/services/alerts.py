# backend/services/alerts.py
import requests
import os

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

def send_slack_alert(message: str):
    if not SLACK_WEBHOOK:
        return
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK, json=payload)

def trade_alert(trade):
    message = f"Trade executed: {trade['symbol']} {trade['side']} {trade['qty']} shares, status: {trade['status']}"
    send_slack_alert(message)
