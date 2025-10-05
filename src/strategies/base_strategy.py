print('Base Strategy Placeholder')# /app/src/strategies/base_strategy.py

class BaseStrategy:
    """
    Abstract base class for trading strategies.
    All strategies should inherit from this class and implement required methods.
    """

    def __init__(self, name="BaseStrategy"):
        self.name = name

    def generate_signals(self, market_data):
        """
        Generate buy/sell/hold signals based on market_data.
        Must be implemented in subclasses.
        """
        raise NotImplementedError("Subclasses must implement generate_signals()")

    def backtest(self, historical_data):
        """
        Run a backtest on historical_data.
        Should be overridden by child strategies.
        """
        raise NotImplementedError("Subclasses must implement backtest()")

    def __repr__(self):
        return f"<Strategy {self.name}>"
