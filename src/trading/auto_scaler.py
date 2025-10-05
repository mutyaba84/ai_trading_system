class AutoScaler:
    def __init__(self, base_size=1, max_risk=0.02, min_size=1):
        self.base_size = base_size
        self.max_risk = max_risk
        self.min_size = min_size

    def compute_size(self, portfolio, recent_pnl):
        """
        Adjust trade size based on recent performance.
        - Reduce size if recent losses
        - Increase if profitable
        """
        equity = portfolio.total_equity()

        # Simple formula: scale size by performance ratio
        if not recent_pnl:
            return self.base_size

        avg_pnl = sum(recent_pnl[-5:]) / min(len(recent_pnl), 5)  # last 5 steps
        scale = 1 + avg_pnl / equity  # positive pnl -> scale up, negative -> scale down
        size = max(self.min_size, int(self.base_size * scale))
        # limit to max_risk per trade
        size = min(size, int(equity * self.max_risk))
        return max(1, size)
