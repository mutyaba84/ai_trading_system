from src.utils.logger import get_logger


class BrokerInterface:
def __init__(self, broker_api_key=None, broker_secret=None):
self.logger = get_logger("BrokerInterface")
self.api_key = broker_api_key
self.secret = broker_secret


def execute_order(self, asset, action, size, price):
self.logger.info(f"[LIVE] {action} {size} {asset} at {price}")
return True