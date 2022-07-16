import unittest
import pandas as pd
from test.test_config import BTC_TEST_DATA_FILE



class IndicatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data : pd.DataFrame = pd.read_csv(BTC_TEST_DATA_FILE, index_col=None)

    def tearDown(self) -> None:
        pass

    def test(self):
        close = self.test_data.Close
        import talib
        print(talib.SMA(close))

















