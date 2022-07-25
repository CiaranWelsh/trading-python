import unittest

import pandas as pd
import pytest 
from trade.binance_data_acquisition import BinanceDataAcquisition
import configparser
from test.test_config import BTC_TEST_DATA_FILE
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")

config = configparser.ConfigParser()
config.read("credentials.ini")
api_key = config.get('binance', 'api_key')
secret_key = config.get('binance', 'secret_key')

class BinanceDataAcquisitionTest(unittest.TestCase):
    
    def test_data_collected(self):
        da = BinanceDataAcquisition(api_key, secret_key, "BTCBUSD", "1h", "1 June, 2022", "1 July, 2022")
        self.assertIsInstance(da.data, pd.DataFrame)
        self.assertFalse(da.data.shape == (0, 0))


    def test_x(self):
        da = BinanceDataAcquisition(api_key, secret_key, "BONDBUSD", "15m", "16 July, 2022", "25 July, 2022")
        print(da.data.columns)
        data = da.data
        # print(data["High"] - data["Low"])
        data["range"] = data["High"] - data["Low"]
        # data["Bearish"] = data["Open"] < data["Close"]
        # data["Bullish"] = data["Open"] > data["Close"]
        # data["direction"] = "bull" if data["Open"] < data["Close"] else "bear"
        direction = []
        for i in range(data.shape[0]):
            if data.iloc[i]["Close"] > data.iloc[i]["Open"]:
                direction.append("Bull")
            elif data.iloc[i]["Close"] < data.iloc[i]["Open"]:
                direction.append("Bear")
            else:
                direction.append("neutral")
        direction

        x = data.drop(["Open time", "Close time", "Ignore"], axis=1)

        # sns.scatterplot()
        from sklearn.decomposition import PCA
        pca = PCA(n_components=2)
        principalComponents = pd.DataFrame(pca.fit_transform(x))
        # principalComponents["direction"] = data["direction"]
        # principalComponents["Bearish"] = data["Bearish"]

        print(principalComponents)

        print(data.head())

        # sns.scatterplot(principalComponents.iloc[:,0], principalComponents.iloc[:,1], hue=direction)
        #
        # # sns.displot(data["range"])
        # plt.show()












