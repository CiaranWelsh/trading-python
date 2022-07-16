import unittest

import pandas as pd
import pytest 
from trade.binance_data_acquisition import BinanceDataAcquisition
import configparser
from test.test_config import BTC_TEST_DATA_FILE

config = configparser.ConfigParser()
config.read("credentials.ini")
api_key = config.get('binance', 'api_key')
secret_key = config.get('binance', 'secret_key')

class BinanceDataAcquisitionTest(unittest.TestCase):
    
    def test_data_collected(self):
        da = BinanceDataAcquisition(api_key, secret_key, "BTCBUSD", "1h", "1 June, 2022", "1 July, 2022")
        self.assertIsInstance(da.data, pd.DataFrame)
        self.assertFalse(da.data.shape == (0, 0))












