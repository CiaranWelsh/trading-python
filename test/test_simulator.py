import pandas as pd

from trade.simulator import Simulator
from trade.strategy import Strategy
import pytest

from test.test_config import BTC_TEST_DATA_FILE

def test_():
    data = pd.read_csv(BTC_TEST_DATA_FILE)
    strategy = Strategy()
    simulator = Simulator(data)
    # simulator.apply_strategy(strategy)
    simulator.apply_strategy(strategy)
    print(strategy.SMA14)


