from src.trading.broker_interface import BrokerInterface
from src.utils.logger import get_logger


class OrderManager:
def __init__(self, live=False, broker_api_key=None, broker_secret=None):
self.live = live
self.logger = get_logger("OrderManager")
self.broker = BrokerInterface(broker_api_key, broker_secret) if live else None


def execute(self, signal, portfolio):
if self.live:
success = self.broker.execute_order(signal['asset'], signal['action'], signal['size'], signal['price'])
if success:
portfolio.add_position(signal['asset'], signal['size'], signal['price'])
else:
self.logger.info(f"[PAPER] Executing {signal['action']} {signal['asset']} size {signal['size']} at {signal['price']}")
portfolio.add_position(signal['asset'], signal['size'], signal['price'])