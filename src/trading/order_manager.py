from src.utils.logger import get_logger
from alpaca_trade_api.rest import REST

class OrderManager:
    def __init__(self, live=False, broker_api_key=None, broker_secret=None):
        self.live = live
        self.logger = get_logger("OrderManager")
        base_url = "https://api.alpaca.markets" if live else "https://paper-api.alpaca.markets"
        self.api = REST(broker_api_key, broker_secret, base_url=base_url)
        self.stop_loss_pct = 0.02
        self.take_profit_pct = 0.05
        self.trailing_stop_pct = 0.01

    def set_risk_params(self, stop_loss=None, take_profit=None, trailing_stop=None):
        if stop_loss is not None:
            self.stop_loss_pct = stop_loss
        if take_profit is not None:
            self.take_profit_pct = take_profit
        if trailing_stop is not None:
            self.trailing_stop_pct = trailing_stop
        self.logger.info(f"Updated risk params: stop_loss={self.stop_loss_pct}, take_profit={self.take_profit_pct}, trailing_stop={self.trailing_stop_pct}")

    def execute(self, signal, portfolio):
        asset = signal['asset']
        action = signal['action'].lower()
        size = signal['size']
        price = signal['price']

        # Validate action and size
        if action not in ['buy', 'sell']:
            self.logger.error(f"Invalid action '{action}' for asset {asset}. Must be 'buy' or 'sell'.")
            return
        if not isinstance(size, int) or size <= 0:
            self.logger.error(f"Invalid order size '{size}' for asset {asset}. Must be a positive integer.")
            return

        # Send order to broker
        try:
            self.api.submit_order(
                symbol=asset,
                qty=size,
                side=action,
                type="market",
                time_in_force="gtc"
            )
            self.logger.info(f"Executed {action.upper()} {size} {asset} @ {price}")
            # Update portfolio only after successful order
            if action == 'buy':
                portfolio.add_position(asset, size, price)
            elif action == 'sell':
                portfolio.add_position(asset, -size, price)
        except Exception as e:
            self.logger.error(f"Order execution failed for {asset}: {e}")
