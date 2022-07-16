import numpy as np
import pandas as pd
import talib


class Strategy:

    def __init__(self):
        pass

    def indicators(self):
        return [
            {"name": "SMA14", "fn": talib.SMA, "kwargs":{"timeperiod":14}},
            {"name": "SMA21", "fn": talib.SMA, "kwargs":{"timeperiod":21}}
        ]

    def precompute_indicators(self, data:np.array):
        for indicator in self.indicators():
            setattr(self, indicator["name"], indicator["fn"](data))

    def next(self, candle:pd.Series):
        pass
