from src.data_pipeline.data_fetcher import DataFetcher
from src.trading.portfolio import Portfolio
from src.trading.risk_manager import RiskManager
from src.trading.order_manager import OrderManager
from src.strategies.ml_strategy import MLStrategy
from src.strategies.rl_strategy import RLStrategy
from src.strategies.signal_aggregator import SignalAggregator
from src.interfaces.dashboard import Dashboard
from src.utils.logger import get_logger
from src.utils.hyperparameter_tuner import HyperparameterTuner
from src.utils.config_loader import load_config

logger = get_logger("Main")

def main():
    config = load_config("configs/config.yaml")
    data_fetcher = DataFetcher(config['assets'], config)
    portfolio = Portfolio()
    risk_manager = RiskManager(config['risk'])
    order_manager = OrderManager(live=False)  # start with paper trading

    ml_strategy = MLStrategy()
    rl_strategy = RLStrategy()
    aggregator = SignalAggregator([ml_strategy, rl_strategy], weights={'MLStrategy':0.7,'RLStrategy':0.3})

    dashboard = Dashboard(portfolio)
    tuner = HyperparameterTuner()

    for step, tick in enumerate(data_fetcher.stream_data()):
        signals = aggregator.aggregate_signals(tick)
        for signal in signals:
            if risk_manager.validate(signal, portfolio):
                order_manager.execute(signal, portfolio)

        portfolio.update(tick)
        dashboard.update()
        logger.info(f"Step {step}: Current PnL: {portfolio.pnl:.2f}")

        # Self-learning
        reward = portfolio.pnl - 100000
        ml_strategy.learn([list(tick.values())], [reward>0])
        rl_strategy.learn(reward, list(tick.values()), 0)  # placeholder action
        aggregator.update_weights({'MLStrategy':0.6,'RLStrategy':0.4})

        if step % 50 == 0 and step > 0:
            tuner.tune_ml_strategy(ml_strategy, dashboard.pnl_history)
            tuner.tune_rl_strategy(rl_strategy, dashboard.pnl_history)

    dashboard.plot_pnl()
    dashboard.export_report()

if __name__ == "__main__":
    main()
