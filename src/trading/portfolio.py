class Portfolio:
    def __init__(self):
        self.positions = {}
        self.cash = 100000
        self.pnl = 100000

    def add_position(self, asset, size, price):
        if asset not in self.positions:
            self.positions[asset] = []
        self.positions[asset].append({'size':size,'price':price})

    def update(self, tick_data):
        total_value = self.cash
        for asset, pos_list in self.positions.items():
            current_price = tick_data.get(asset, pos_list[-1]['price'])
            for pos in pos_list:
                total_value += pos['size'] * current_price
        self.pnl = total_value
