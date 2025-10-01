import pandas as pd
import os

class DataFetcher:
    def __init__(self, assets, config):
        self.assets = assets
        self.config = config
        self.data = self.load_data()
        self.index = 0

    def load_data(self):
        data = {}
        for asset in self.assets:
            path = f"data/raw/{asset.replace('-','_')}.csv"
            if os.path.exists(path):
                data[asset] = pd.read_csv(path).to_dict('records')
            else:
                data[asset] = []
        return data

    def stream_data(self):
        length = max(len(v) for v in self.data.values())
        for i in range(length):
            tick = {}
            for asset, records in self.data.items():
                tick[asset] = records[i]['close'] if i < len(records) else records[-1]['close']
            yield tick
