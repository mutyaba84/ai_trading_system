import numpy as np

class VolatilityManager:
    def __init__(self, vol_window=20, vol_threshold=0.03):
        """
        vol_window: lookback window for volatility calculation
        vol_threshold: threshold for high volatility (as % of price)
        """
        self.vol_window = vol_window
        self.vol_threshold = vol_threshold

    def compute_volatility(self, prices):
        if len(prices) < self.vol_window:
            return 0.0
        returns = np.diff(prices[-self.vol_window:]) / prices[-self.vol_window:-1]
        return np.std(returns)

    def adjust_trade_frequency(self, prices, base_frequency=1.0):
        """
        Adjust trading frequency dynamically:
        - If volatility > threshold → reduce frequency
        - If volatility < threshold → increase frequency
        """
        vol = self.compute_volatility(prices)
        if vol > self.vol_threshold:
            return base_frequency * 0.5   # trade less
        else:
            return base_frequency * 1.5   # trade more
