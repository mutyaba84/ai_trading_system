import numpy as np

class SmartRiskEngine:
    def __init__(self, max_drawdown=0.2, base_trade_size=1000, vol_window=20, vol_threshold=0.03):
        """
        max_drawdown: maximum allowed loss (20% default)
        base_trade_size: starting trade size in USD
        vol_window: number of lookback prices for volatility calculation
        vol_threshold: threshold for high volatility adjustment
        """
        self.max_drawdown = max_drawdown
        self.base_trade_size = base_trade_size
        self.vol_window = vol_window
        self.vol_threshold = vol_threshold

    def compute_volatility(self, prices):
        if len(prices) < self.vol_window:
            return 0.0
        returns = np.diff(prices[-self.vol_window:]) / prices[-self.vol_window:-1]
        return np.std(returns)

    def compute_trade_size(self, pnl_history, price_history, asset="default"):
        """
        Combines risk allocation, auto-scaling, and volatility adjustment.
        """
        # 1. Stop trading if drawdown too high
        total_pnl = sum(pnl_history)
        if total_pnl < -self.max_drawdown * self.base_trade_size:
            return 0  

        # 2. Base trade size
        trade_size = self.base_trade_size

        # 3. Auto-scale with performance
        if total_pnl > 0:
            trade_size *= 1 + min(total_pnl / 10000, 0.5)  # cap scaling at +50%
        elif total_pnl < 0:
            trade_size *= 0.5  # reduce size when losing

        # 4. Volatility adjustment
        vol = self.compute_volatility(price_history)
        if vol > self.vol_threshold:
            trade_size *= 0.5  # cut size in volatile conditions
        else:
            trade_size *= 1.2  # increase size slightly in stable conditions

        return max(trade_size, 10)  # never trade below $10

    def adjust_trade_frequency(self, price_history, base_frequency=1.0):
        """
        Adjust how often we trade based on volatility.
        """
        vol = self.compute_volatility(price_history)
        if vol > self.vol_threshold:
            return base_frequency * 0.5
        return base_frequency * 1.5
