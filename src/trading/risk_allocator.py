import numpy as np

class RiskAllocator:
    def __init__(self, max_risk_per_trade=0.02):
        self.max_risk = max_risk_per_trade

    def compute_weights(self, portfolio, price_history):
        """
        Compute allocation weights per asset
        - Use inverse volatility: lower volatility -> higher weight
        - Adjust for correlation: reduce weight for correlated assets
        """
        assets = portfolio.positions.keys()
        volatilities = {}
        for asset in assets:
            prices = price_history.get(asset, [])
            if len(prices) < 2:
                volatilities[asset] = 1.0  # default if not enough data
            else:
                volatilities[asset] = np.std(prices)

        # Inverse volatility allocation
        inv_vol = {a: 1.0 / v if v>0 else 1.0 for a,v in volatilities.items()}
        total = sum(inv_vol.values())
        weights = {a: iv/total for a,iv in inv_vol.items()}

        # Optional: correlation adjustment
        # Can implement correlation matrix here to reduce weights for correlated assets

        return weights

    def allocate_trade_size(self, portfolio, base_size, price_history):
        weights = self.compute_weights(portfolio, price_history)
        sizes = {}
        equity = portfolio.total_equity()
        for asset, w in weights.items():
            sizes[asset] = min(int(base_size * w), int(equity * self.max_risk / price_history.get(asset, [1])[-1]))
        return sizes
