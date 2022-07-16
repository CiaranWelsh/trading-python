from __future__ import annotations

from os import stat
from abc import ABC, abstractmethod

import pandas as pd


class DataAcquisition:
    """
    
    """



    def __init__(self, api_key, api_secret, **kwargs) -> None:
        self.kwargs = kwargs
        self._pair: str 
        self._timeframe: str
        self._start = None 
        self._end = None

        self.data = self._get_data()


    @staticmethod
    def from_json(json: dict) -> DataAcquisition:
        pass

    @abstractmethod
    def _get_data(self) -> pd.DataFrame:
        pass


        

















