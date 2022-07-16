from __future__ import annotations

from os import stat
from abc import ABC, abstractmethod

import pandas as pd


class DataAcquisition:
    """
    
    """



    def __init__(self, symbol: str, timeframe: str, start_str: str, end_str: str) -> None:
        self._symbol: str = symbol
        self._timeframe: str = timeframe
        self._start = start_str
        self._end = end_str

        self.data = self._get_data()


    @staticmethod
    def from_json(json: dict) -> DataAcquisition:
        pass

    @abstractmethod
    def _get_data(self) -> pd.DataFrame:
        pass


        

















