import pytest

from trade.order import MarketOrder
from trade.order import Wallet
from trade.orderbook import OrderBook


def test_place_order_empty():
    base_currency_wallet = Wallet(1000, currency="EUR")
    quote_currency_wallet = Wallet(0, currency="GBP")

    orderbook = OrderBook(1)

    order = MarketOrder(MarketOrder.TYPE.BUY, base_currency_wallet, quote_currency_wallet)
    orderbook.place(order)

    print(orderbook)





