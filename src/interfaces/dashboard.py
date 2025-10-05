from src.utils.logger import get_logger
import matplotlib.pyplot as plt  # For future plot_pnl implementation

class Dashboard:
    def __init__(self, portfolio, log_dir="logs"):
        self.portfolio = portfolio
        self.logger = get_logger("Dashboard")
        self.pnl_history = []

    def update(self, prices=None):
        if prices is None:
            prices = {}
        summary = self.show_portfolio(prices)
        pnl = summary["total_pnl"]
        self.pnl_history.append(pnl)
        self.logger.info(f"Step update: Current PnL: {pnl:.2f}")
    def show_portfolio(self, prices):
        total_pnl = 0
        positions_summary = {}
        if not hasattr(self.portfolio, "positions"):
            self.logger.error("Portfolio object missing 'positions' attribute.")
            return {"positions": {}, "total_pnl": 0}
        for asset, pos in self.portfolio.positions.items():
            current_price = prices.get(asset, pos.get("avg_price", 0))
            pos_pnl = (current_price - pos.get("avg_price", 0)) * pos.get("size", 0)
            positions_summary[asset] = {
                "size": pos.get("size", 0),
                "avg_price": pos.get("avg_price", 0),
                "pnl": pos_pnl
            }
            total_pnl += pos_pnl
        return {"positions": positions_summary, "total_pnl": total_pnl}
        return {"positions": positions_summary, "total_pnl": total_pnl}

    def plot_pnl(self):
        pass

    def export_report(self):
        pass
