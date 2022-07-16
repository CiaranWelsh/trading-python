import unittest

import pandas as pd
import pytest 
from trade.binance_data_acquisition import BinanceDataAcquisition
import configparser

config = configparser.ConfigParser()
config.read("credentials.ini")
api_key = config.get('binance', 'api_key')
secret_key = config.get('binance', 'secret_key')

class BinanceDataAcquisitionTest(unittest.TestCase):
    
    def test_data_collected(self):
        da = BinanceDataAcquisition(api_key, secret_key)
        self.assertIsInstance(da.data, pd.DataFrame)
        self.assertFalse(da.data.shape == (0, 0))












