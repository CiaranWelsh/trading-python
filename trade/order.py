from abc import abstractmethod, ABC
from enum import Enum
from trade.wallet import Wallet


class Order(ABC):
    class TYPE(Enum):
        BUY = 0
        SELL = 1

    def __init__(self, type, base_wallet: Wallet, quote_wallet: Wallet):
        self._type = type
        # the BTC in BTC/BUSD
        self._base_wallet = base_wallet
        # the BUSD in BTC/BUSD
        self._quote_wallet = quote_wallet
        # total amount of base currency to purchase, in units in the quote currency
        # i.e 10 dollars worth of BTC, total is 10

    @staticmethod
    def position_size(total_capital, entry_price, stop_loss_price, risk=0.01):
        return (risk * total_capital) / (entry_price - stop_loss_price)

    @abstractmethod
    def place(self, total, base_currency_price):
        pass


class MarketOrder(Order):

    def __init__(self, type: Order.TYPE, base_wallet: Wallet, quote_wallet: Wallet):
        super().__init__(type, base_wallet, quote_wallet)

    def place(self, total, base_currency_price):
        amount = total / base_currency_price
        if self._type == self.TYPE.BUY:
            self._base_wallet += amount
            self._quote_wallet -= total
        elif self._type == self.TYPE.SELL:
            self._base_wallet -= amount
            self._quote_wallet += total


class LimitOrder(Order):

    def __init__(self, type: Order.TYPE, base_wallet: Wallet, quote_wallet: Wallet, target_price: float):
        self._target_price = target_price
        super().__init__(type, base_wallet, quote_wallet)

    def place(self, total, base_currency_price):
        if self._type == self.TYPE.BUY and self._target_price >= base_currency_price :
            MarketOrder(self.TYPE.BUY, self._base_wallet, self._quote_wallet).place(total, base_currency_price)
        else:
            MarketOrder(self.TYPE.SELL, self._base_wallet, self._quote_wallet).place(total, base_currency_price)



class Buy:

    def __init__(self, price, stop, take_profit, risk=0.01):
        super().__init__(price, stop, take_profit)


class Sell:

    def __init__(self, price, stop, take_profit, risk=0.01):
        super().__init__(price, stop, take_profit)
