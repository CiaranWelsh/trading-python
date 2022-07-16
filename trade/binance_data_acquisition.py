from binance.client import Client
from trade.data_acquisition import DataAcquisition
import pandas as pd

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
            symbol='SOLBUSD', interval=self.client.KLINE_INTERVAL_1HOUR,
            start_str="1 June, 2022", end_str="1 July, 2022"
        )
        df = pd.DataFrame(candles, columns=self._labels)
        return df









