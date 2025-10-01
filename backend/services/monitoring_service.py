# Placeholder for backend/services/monitoring_service.py
# backend/services/monitoring_service.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("trading_system")

class Monitor:
    def log_trade(self, trade):
        logger.info(f"TRADE EXECUTED: {trade}")

    def log_error(self, error):
        logger.error(f"ERROR: {error}")

    def send_alert(self, message):
        # Placeholder → integrate with Slack/Telegram later
        logger.warning(f"ALERT: {message}")
