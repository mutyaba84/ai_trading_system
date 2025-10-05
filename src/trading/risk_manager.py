class RiskManager:
    def __init__(self, max_risk_per_trade=0.02, max_drawdown=0.1):
        self.max_risk = max_risk_per_trade
        self.max_drawdown = max_drawdown

    def adjust_trade_size(self, portfolio, suggested_size, price):
        """
        Adjust size based on:
        - Max risk per trade
        - Drawdown limits
        """
        equity = portfolio.total_equity()
        risk_size = int(equity * self.max_risk / price)
        size = min(suggested_size, risk_size)

        # Check drawdown
        if portfolio.max_equity() - portfolio.total_equity() > equity * self.max_drawdown:
            size = 0  # freeze trading if drawdown exceeded
        return max(size, 0)
