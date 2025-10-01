import matplotlib.pyplot as plt
import pandas as pd
import os
from src.utils.logger import get_logger


class Dashboard:
def __init__(self, portfolio, log_dir="logs"):
self.portfolio = portfolio
self.logger = get_logger("Dashboard")
self.log_dir = log_dir
self.pnl_history = []


def update(self):
self.pnl_history.append(self.portfolio.pnl)


def plot_pnl(self):
if not self.pnl_history:
self.logger.warning("No PnL data to plot")
return
plt.figure(figsize=(10,5))
plt.plot(self.pnl_history, label="PnL")
plt.title("Portfolio PnL Over Time")
plt.xlabel("Time Steps")
plt.ylabel("PnL")
plt.legend()
plt.grid(True)
os.makedirs(self.log_dir, exist_ok=True)
plt.savefig(f"{self.log_dir}/pnl_chart.png")
plt.close()
self.logger.info(f"PnL chart saved to {self.log_dir}/pnl_chart.png")


def export_report(self):
os.makedirs(self.log_dir, exist_ok=True)
df = pd.DataFrame({'PnL': self.pnl_history})
df.to_csv(f"{self.log_dir}/pnl_history.csv", index=False)
self.logger.info(f"PnL history exported to {self.log_dir}/pnl_history.csv")