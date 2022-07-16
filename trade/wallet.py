from __future__ import annotations
import numpy as np
from math import isclose

class Wallet:

    def __init__(self, initial_balance: float, currency:str = "BUSD"):
        self.balance : float = initial_balance
        self.currency : str = currency

    def __str__(self):
        return f"Wallet({self.balance} {self.currency})"

    def __repr__(self):
        return self.__str__()

    def _compute(self, fn:callable, other: int|float|Wallet):
        if isinstance(other, Wallet):
            self.balance = fn(self.balance, other.balance)
        else:
            self.balance = fn(self.balance, other)
        return self.balance

    def __add__(self, other: float | int| Wallet):
        return self._compute(np.add, other)

    def __iadd__(self, other: float|int|Wallet):
        return self._compute(np.add, other)

    def __sub__(self, other: float | int| Wallet):
        return self._compute(np.subtract, other)

    def __isub__(self, other: float | int| Wallet):
        return self._compute(np.subtract, other)

    def __mul__(self, other: float | int | Wallet):
        return self._compute(np.multiply, other)

    def __imul__(self, other: float | int | Wallet):
        return self._compute(np.multiply, other)

    def __truediv__(self, other: float | int | Wallet):
        return self._compute(np.divide, other)

    def __itruediv__(self, other: float | int | Wallet):
        return self._compute(np.divide, other)

    def __floordiv__(self, other: float | int | Wallet):
        return self._compute(np.floor, other)

    def __ifloordiv__(self, other: float | int | Wallet):
        return self._compute(np.floor, other)

    def __eq__(self, other: float | int | Wallet):
        if isinstance(other, Wallet):
            return self.balance == other.balance
        else:
            return self.balance == other

    def __ne__(self, other: float | int | Wallet):
        return not self.__eq__(other)

    def almost_equal(self, other: float|int|Wallet, precision=1e-7):
        if isinstance(other, Wallet):
            return isclose(self.balance, other.balance, rel_tol=precision)
        else:
            return isclose(self.balance, other, rel_tol=precision)



















