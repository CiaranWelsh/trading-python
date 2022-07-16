import pandas as pd
import talib
from enum import Enum, auto

from trade.strategy import Strategy
from trade.wallet import Wallet
from trade.order import Order, Buy, Sell
from queue import Queue

class Simulator:

    class TREND(Enum):
        UP = auto()
        DOWN = auto()
        NONE = auto()

    def __init__(self, data:pd.DataFrame, initial_balance: float = 1000):
        self._data = data
        self._initial_balance = initial_balance
        self._wallet = Wallet(initial_balance)
        self._previous_trend_direction = self.TREND.NONE
        self._current_trend_direction = self.TREND.NONE

        self._orders = Queue()

    def apply_strategy(self, strategy: Strategy):
        strategy.precompute_indicators(self._data["Close"])
        print(self._data.shape)
        for candle_idx in range(self._data.shape[0]):
            print(candle_idx)
            if candle_idx >= 21 :
                input_data = self._data["Close"].iloc[candle_idx-21: candle_idx]
                sma21 = talib.SMA(input_data.values, timeperiod=21)[-1]
            if candle_idx >= 50:
                input_data = self._data["Close"].iloc[candle_idx-50: candle_idx]
                sma50 = talib.SMA(input_data.values, timeperiod=50)[-1]

                self._previous_trend_direction = self._current_trend_direction
                if sma21 < sma50:
                    self._current_trend_direction = self.TREND.DOWN
                elif sma50 < sma21:
                    self._current_trend_direction = self.TREND.UP
                else:
                    self._current_trend_direction = self.TREND.NONE

                if self._previous_trend_direction is self.TREND.UP and self._current_trend_direction is self.TREND.DOWN:
                    # we have crossed over to downtrend, place sell order, risk 1%, reward 2%
                    price = self._data["Close"].iloc[candle_idx]
                    stop_loss = max(self._data["Close"][candle_idx - 2], self._data["Close"][candle_idx - 1])
                    take_profit = price - 2 * (stop_loss - price)
                    position_size = Order.position_size(self._initial_balance, price, stop_loss, risk=0.01)
                    self._wallet -= position_size


                elif self._previous_trend_direction is self.TREND.DOWN and self._current_trend_direction is self.TREND.UP:
                    # cross over to up trend, buy order
                    price = self._data["Close"].iloc[candle_idx]
                    stop_loss = min(self._data["Close"][candle_idx - 2], self._data["Close"][candle_idx - 1])
                    take_profit = price + 2 * (price - stop_loss)
                    position_size = Order.position_size(self._initial_balance, price, stop_loss, risk=0.01)


                # if the 21 is lower than 50, we are in a a downtrend
                # if the 50 is lower then the 21 we are in an uptrend.



            # candle = self._data.iloc[candle_idx]
            # strategy.next(candle)
