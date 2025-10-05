from src.utils.logger import get_logger

class HyperparameterTuner:
    def __init__(self):
        self.logger = get_logger("HyperparameterTuner")

    def tune_ml_strategy(self, ml_strategy, pnl_history=None):
        # Example: dynamically adjust n_estimators
        if pnl_history and len(pnl_history) > 0:
            if pnl_history[-1] < 0:  # reduce complexity if losing
                ml_strategy.model.n_estimators = max(10, ml_strategy.model.n_estimators - 10)
            else:
                ml_strategy.model.n_estimators += 10
            self.logger.info(f"MLStrategy tuned, n_estimators={ml_strategy.model.n_estimators}")

    def tune_rl_strategy(self, rl_strategy, pnl_history=None):
        # Example: adjust learning rate based on PnL
        if pnl_history and len(pnl_history) > 0:
            if pnl_history[-1] < 0:
                rl_strategy.learning_rate = max(0.01, getattr(rl_strategy, 'learning_rate', 0.1) * 0.9)
            else:
                rl_strategy.learning_rate = getattr(rl_strategy, 'learning_rate', 0.1) * 1.05
            self.logger.info(f"RLStrategy tuned, learning_rate={rl_strategy.learning_rate}")
