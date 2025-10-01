from src.utils.logger import get_logger


class SignalAggregator:
def __init__(self, strategies, weights=None):
self.strategies = strategies
self.weights = weights or {}
self.logger = get_logger("SignalAggregator")


def aggregate_signals(self, tick_data):
asset_scores = {}
for strategy in self.strategies:
name = type(strategy).__name__
weight = self.weights.get(name,1.0)
signals = strategy.generate_signals(tick_data)
for s in signals:
asset = s['asset']
action = s['action']
confidence = s.get('confidence',1.0)
if asset not in asset_scores:
asset_scores[asset] = {'BUY':0.0,'SELL':0.0}
asset_scores[asset][action] += weight * confidence
final_signals = []
for asset, scores in asset_scores.items():
if scores['BUY']>scores['SELL']:
final_signals.append({'asset':asset,'action':'BUY','size':1,'price':tick_data[asset]})
elif scores['SELL']>scores['BUY']:
final_signals.append({'asset':asset,'action':'SELL','size':1,'price':tick_data[asset]})
return final_signals


def update_weights(self, performance_metrics):
self.weights.update(performance_metrics)
self.logger.info(f"Updated strategy weights: {self.weights}")