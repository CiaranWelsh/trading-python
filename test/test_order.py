import pytest

from trade.order import *
from trade.wallet import Wallet


def test_buy_market_order():
    base_currency_wallet = Wallet(0, currency="EUR")
    quote_currency_wallet = Wallet(1000, currency="GBP")
    total = 1
    price = 1
    market_buy_order = MarketOrder(
        Order.TYPE.BUY, base_currency_wallet, quote_currency_wallet,
    )
    market_buy_order.place(total, price)
    assert quote_currency_wallet == 999
    assert base_currency_wallet == 1

def test_buy_market_order2():
    base_currency_wallet = Wallet(0, currency="EUR")
    quote_currency_wallet = Wallet(1000, currency="GBP")
    total = 1
    price = 100
    market_buy_order = MarketOrder(
        Order.TYPE.BUY, base_currency_wallet, quote_currency_wallet,
    )
    market_buy_order.place(total, price)
    # we have bought 0.01 EUR for 1 GBP
    assert base_currency_wallet == 0.01
    # the cost of 0.01 EUR was 1 GBP, we have 999 left
    assert quote_currency_wallet == 999

def test_buy_market_order3():
    base_currency_wallet = Wallet(0, currency="BTC")
    quote_currency_wallet = Wallet(1000, currency="BUSD")
    total = 100
    price = 20823.18
    market_buy_order = MarketOrder(
        Order.TYPE.BUY, base_currency_wallet, quote_currency_wallet,
    )
    market_buy_order.place(total, price)
    # we have bought 0.01 EUR for 1 GBP
    assert base_currency_wallet.almost_equal(0.00480, 4)
    # the cost of 0.01 EUR was 1 GBP, we have 999 left
    assert quote_currency_wallet == 900

def test_sell_market_order():
    # Sell 1 EUR for GBP at price of 10 GBP to 1 EUR
    base_currency_wallet = Wallet(1000, currency="EUR")
    quote_currency_wallet = Wallet(0, currency="GBP")
    total = 1
    price = 10
    market_sell_order = MarketOrder(
        Order.TYPE.SELL, base_currency_wallet, quote_currency_wallet,
    )
    market_sell_order.place(total, price)
    assert quote_currency_wallet == 1
    assert base_currency_wallet == 999.9

def test_sell_market_order2():
    # Sell 1 EUR for GBP at price of 10 GBP to 1 EUR
    base_currency_wallet = Wallet(1000, currency="BTC")
    quote_currency_wallet = Wallet(0, currency="BUSD")
    total = 100
    price = 20823.18
    market_sell_order = MarketOrder(
        Order.TYPE.SELL, base_currency_wallet, quote_currency_wallet,
    )
    market_sell_order.place(total, price)
    assert base_currency_wallet.almost_equal(100 - 0.00480, 6)
    # the cost of 0.01 EUR was 1 GBP, we have 999 left
    assert quote_currency_wallet == 100
