from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.validation import check_is_fitted
from sklearn.exceptions import NotFittedError
import numpy as np
from src.strategies.base_strategy import BaseStrategy
from src.utils.logger import get_logger

class MLStrategy(BaseStrategy):
    def __init__(self, model=None, min_fit_samples=10):
        self.model = model or RandomForestClassifier()
        self.logger = get_logger("MLStrategy")
        self.features = []
        self.labels = []
        self.min_fit_samples = min_fit_samples  # minimum data to fit

    def generate_signals(self, tick_data):
        """
        Generate trading signals for each asset in tick_data.
        Returns a list of signals:
        [{'asset': asset, 'action': 'BUY'/'SELL', 'size': 1, 'price': price, 'confidence': confidence}]
        """
        signals = []
        for asset, price in tick_data.items():
            # Build feature vector for this tick
            feature_vector = self._build_features(asset, price)
            
            # Predict signal safely
            pred, confidence = self._predict(feature_vector)

            action = 'BUY' if pred > 0.5 else 'SELL'
            signals.append({
                'asset': asset,
                'action': action,
                'size': 1,
                'price': price,
                'confidence': confidence
            })
        return signals

    def _build_features(self, asset, price):
        """
        For now, simple placeholder feature: just the price.
        Replace with more complex features (moving averages, RSI, etc.) as needed.
        """
        return [price]

    def _predict(self, feature_vector):
        X = np.array([feature_vector])

        # Fallback: not enough data to fit
        if len(self.features) < self.min_fit_samples:
            return np.random.rand(), 0.5

        # Fit the model if not already fitted
        try:
            check_is_fitted(self.model)
        except NotFittedError:
            X_fit = np.array(self.features)
            y_fit = np.array(self.labels)
            if len(X_fit) >= self.min_fit_samples:
                self.model.fit(X_fit, y_fit)
                self.logger.info(f"MLStrategy model trained on {len(X_fit)} samples")
            else:
                # Not enough data even for fit, return random
                return np.random.rand(), 0.5

        # Predict probability of class 1 (BUY)
        y_pred = self.model.predict_proba(X)[0, 1]
        return y_pred, y_pred

    def learn(self, new_features, new_labels):
        """
        Feed new training data to the strategy.
        """
        self.features.extend(new_features)
        self.labels.extend(new_labels)

        # Optional: retrain every 50 samples
        if len(self.features) >= 50:
            try:
                self.model.fit(np.array(self.features), np.array(self.labels))
                self.logger.info("MLStrategy retrained with latest data")
            except Exception as e:
                self.logger.error(f"Failed to retrain MLStrategy: {e}")
            finally:
                self.features, self.labels = [], []
