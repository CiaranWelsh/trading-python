from binance.client import Client
from trade.data_acquisition import DataAcquisition
import pandas as pd
import numpy as np


class BinanceDataAcquisition(DataAcquisition):

    _labels = [
        "Open time", "Open", "High",
        "Low", "Close", "Volume", "Close time", "Quote asset volume",
        "Number of trades", "Taker buy base,"
        "asset volume", "Taker buy quote asset volume", "Ignore"
    ]
    def __init__(self, api_key, api_secret, symbol: str, timeframe: str, start_str: str, end_str: str, ):
        self.client = Client(api_key, api_secret)
        super().__init__(symbol, timeframe, start_str, end_str)

    def _get_data(self) -> pd.DataFrame:
        candles = self.client.get_historical_klines(
            symbol=self._symbol, interval=self.client.KLINE_INTERVAL_1HOUR,
            start_str=self._start, end_str=self._end
        )
        df = pd.DataFrame(candles, columns=self._labels)
        df = df.astype(np.float)
        return df









