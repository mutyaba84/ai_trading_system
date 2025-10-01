from sklearn.ensemble import RandomForestClassifier
import numpy as np
from src.strategies.base_strategy import BaseStrategy
from src.utils.logger import get_logger

class MLStrategy(BaseStrategy):
    def __init__(self, model=None):
        self.model = model or RandomForestClassifier()
        self.logger = get_logger("MLStrategy")
        self.features = []
        self.labels = []

    def generate_signals(self, tick_data):
        signals = []
        for asset, price in tick_data.items():
            pred, confidence = self._predict(asset, price)
            action = 'BUY' if pred > 0.5 else 'SELL'
            signals.append({'asset': asset, 'action': action, 'size': 1, 'price': price, 'confidence': confidence})
        return signals

    def _predict(self, asset, price):
        if not self.features:
            return np.random.rand(), 0.5
        X = np.array(self.features)
        y_pred = self.model.predict_proba(X)[:,1][-1]
        return y_pred, y_pred

    def learn(self, new_features, new_labels):
        self.features.extend(new_features)
        self.labels.extend(new_labels)
        if len(self.features) > 50:
            self.model.fit(self.features, self.labels)
            self.features, self.labels = [], []
            self.logger.info("MLStrategy retrained with latest data")
