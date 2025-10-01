class RiskManager:
    def __init__(self, risk_config):
        self.max_position = risk_config.get('max_position', 100)
        self.max_drawdown = risk_config.get('max_drawdown', 0.1)
        self.max_exposure = risk_config.get('max_exposure', 5000)

    def validate(self, signal, portfolio):
        if signal['size'] > self.max_position:
            return False
        # additional exposure & drawdown checks can be added
        return True
