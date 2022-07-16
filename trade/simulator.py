import pandas as pd

from trade.strategy import Strategy

class Simulator:

    def __init__(self, data:pd.DataFrame):
        self._data = data

    def apply_strategy(self, strategy: Strategy):
        pass
