import numpy as np
from src.strategies.base_strategy import BaseStrategy
from src.utils.logger import get_logger

class RLStrategy(BaseStrategy):
    def __init__(self, agent=None, memory_limit=50):
        self.agent = agent
        self.logger = get_logger("RLStrategy")
        self.memory = []
        self.memory_limit = memory_limit

    def generate_signals(self, tick_data):
        signals = []
        for asset, price in tick_data.items():
            action_idx = self._predict(asset, price)
            action = ['BUY','SELL','HOLD'][action_idx]
            if action != 'HOLD':
                confidence = np.random.rand()
                signals.append({'asset': asset, 'action': action, 'size': 1, 'price': price, 'confidence': confidence})
        return signals

    def _predict(self, asset, price):
        """
        Simple placeholder: random action. Replace with real RL agent prediction.
        """
        return np.random.randint(0,3)

    def learn(self, reward, state, action):
        self.memory.append((state, action, reward))
        if len(self.memory) >= self.memory_limit:
            # Optionally update agent here
            self.memory = []
            self.logger.info("RLStrategy updated from recent experience")
