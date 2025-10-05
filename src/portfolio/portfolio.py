class Portfolio:
    def __init__(self, initial_cash=100000, max_drawdown=-15000):
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.positions = {}
        self.pnl = 0.0
        self.history = []
        self.max_drawdown = max_drawdown
        self.trading_halted = False

    def update(self, tick):
        if self.trading_halted:
            return self.pnl
        total_value = self.cash
        for asset, pos in self.positions.items():
            if asset in tick:
                total_value += pos["size"] * tick[asset]
        self.pnl = total_value - self.initial_cash
        self.history.append(self.pnl)
        if self.pnl <= self.max_drawdown:
            self.trading_halted = True
            print("🚨 Max drawdown reached! Trading halted.")
        return self.pnl

    def get_market_data(self):
        tick_data = {}
        try:
            for symbol in self.positions.keys():
                tick_data[symbol] = 100.0
            if not tick_data:
                tick_data = {"AAPL": 175.2, "MSFT": 334.8}
        except Exception as e:
            print(f"⚠️ Error fetching market data: {e}")
        return tick_data

    def add_position(self, asset, size, price):
        if self.trading_halted:
            print(f"⚠️ Trade ignored: trading is halted.")
            return
        cost = size * price
        self.cash -= cost
        if asset not in self.positions:
            self.positions[asset] = {"size": size, "avg_price": price}
            print(f"📈 Added new position: {asset} | size={size} | price={price}")
        else:
            pos = self.positions[asset]
            new_size = pos["size"] + size
            if new_size != 0:
                new_avg_price = (pos["avg_price"] * pos["size"] + price * size) / new_size
                pos["avg_price"] = new_avg_price
            pos["size"] = new_size
            if new_size == 0:
                del self.positions[asset]
                print(f"💼 Closed position: {asset}")
            else:
                print(f"🔁 Updated position: {asset} | size={new_size} | avg_price={pos['avg_price']}")

    def remove_position(self, asset):
        if asset in self.positions:
            del self.positions[asset]
            print(f"❌ Position closed: {asset}")
        else:
            print(f"⚠️ No position found for {asset}")

    def close_all_positions(self):
        self.positions.clear()
        print("🧹 All positions closed.")

    def risk_adjustment(self, order_manager):
        if self.trading_halted:
            return
        if self.pnl <= -5000:
            order_manager.stop_loss_pct = 0.01
            order_manager.take_profit_pct = 0.02
            order_manager.trailing_stop_pct = 0.008
            order_manager.logger.info("⚠️ Auto risk tightened (losses > -5%)")
        elif self.pnl >= 10000:
            order_manager.stop_loss_pct = 0.03
            order_manager.take_profit_pct = 0.06
            order_manager.trailing_stop_pct = 0.02
            order_manager.logger.info("✅ Risk relaxed (gains > +10%)")

    def reset_trading(self):
        self.trading_halted = False
        self.history.clear()
        print("✅ Trading reset by user")

    def set_max_drawdown(self, amount):
        self.max_drawdown = amount
        print(f"⚙️ Max drawdown updated to {amount}")
