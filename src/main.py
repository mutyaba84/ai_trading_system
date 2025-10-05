import time
from src.utils.config_loader import load_config
from src.trading.order_manager import OrderManager
from src.strategies.signal_aggregator import SignalAggregator
from src.strategies.ml_strategy import MLStrategy
from src.strategies.rl_strategy import RLStrategy
from src.interfaces.dashboard import Dashboard
from src.utils.hyperparameter_tuner import HyperparameterTuner
from src.portfolio.portfolio import Portfolio
from src.utils.logger import get_logger

logger = get_logger("Main")

def main():
    config = load_config("configs/config.yaml")
    mode = config.get("mode", "paper")
    live = mode == "live"

    # Initialize portfolio
    portfolio = Portfolio(initial_cash=100000)

    # Initialize strategies
    ml_strategy = MLStrategy()
    rl_strategy = RLStrategy()
    aggregator = SignalAggregator(strategies=[ml_strategy, rl_strategy])

    # Initialize OrderManager
    order_manager = OrderManager(
        live=live,
        broker_api_key=config["paper_trading"]["api_key"],
        broker_secret=config["paper_trading"]["api_secret"]
    )

    # Initialize dashboard
    dashboard = Dashboard(portfolio)

    # Hyperparameter tuner
    tuner = HyperparameterTuner()

    # Main loop
    for step in range(10):  # example test steps
        tick = portfolio.get_market_data()  # fetch prices
        signals = aggregator.aggregate_signals(tick)
        for signal in signals:
            order_manager.execute(signal, portfolio)

        # Update portfolio PnL
        portfolio.update(tick)

        # Update dashboard (pass prices!)
        dashboard.update(tick)

        # Tune strategies
        tuner.tune_ml_strategy(ml_strategy, dashboard.pnl_history)
        tuner.tune_rl_strategy(rl_strategy, dashboard.pnl_history)

        # Auto-adjust risk if needed
        order_manager.set_risk_params(
            stop_loss=config.get("stop_loss", 0.02),
            take_profit=config.get("take_profit", 0.05),
            trailing_stop=config.get("trailing_stop", 0.01)
        )

        time.sleep(1)

if __name__ == "__main__":
    main()
                new_avg_price = (pos["avg_price"] * pos["size"] + price * size) / new_size
                self.positions[asset] = {"size": new_size, "avg_price": new_avg_price}
                print(f"🔄 Updated position: {asset} | new size={new_size} | new avg price={new_avg_price}")
            else:
                del self.positions[asset]
                print(f"❌ Closed position: {asset}")