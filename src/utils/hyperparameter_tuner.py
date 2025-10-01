

# --- src/utils/hyperparameter_tuner.py ---
import numpy as np
from src.utils.logger import get_logger


class HyperparameterTuner:
def __init__(self):
self.logger = get_logger("HyperparameterTuner")


def tune_ml_strategy(self, ml_strategy, performance_history):
new_n_estimators = np.random.choice([50, 100, 150])
if hasattr(ml_strategy.model, 'n_estimators'):
ml_strategy.model.n_estimators = new_n_estimators
self.logger.info(f"Tuned MLStrategy n_estimators to {new_n_estimators}")


def tune_rl_strategy(self, rl_strategy, performance_history):
new_exploration_rate = np.random.uniform(0.1, 0.3)
rl_strategy.exploration_rate = new_exploration_rate
self.logger.info(f"Tuned RLStrategy exploration_rate to {new_exploration_rate}")