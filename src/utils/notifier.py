# --- src/utils/notifier.py ---
from src.utils.logger import get_logger


class Notifier:
def __init__(self):
self.logger = get_logger("Notifier")


def send_alert(self, message):
self.logger.info(f"[ALERT] {message}")