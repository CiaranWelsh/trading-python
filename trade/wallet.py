from __future__ import annotations
import numpy as np


class Wallet:

    def __init__(self, initial_balance: float):
        self.balance = initial_balance

    def __str__(self):
        return f"Wallet({self.balance})"

    def _compute(self, fn:callable, other: int|float|Wallet):
        if isinstance(other, Wallet):
            self.balance = fn(self.balance, other.balance)
        else:
            self.balance = fn(self.balance, other)
        return self.balance

    def __add__(self, other: float | int| Wallet):
        return self._compute(np.add, other)

    def __sub__(self, other: float | int| Wallet):
        return self._compute(np.subtract, other)

    def __mul__(self, other: float | int | Wallet):
        return self._compute(np.multiply, other)

    def __truediv__(self, other: float | int | Wallet):
        return self._compute(np.divide, other)

    def __floordiv__(self, other: float | int | Wallet):
        return self._compute(np.floor, other)

    def __eq__(self, other: float | int | Wallet):
        return self._compute(np.equal, other)

    def __ne__(self, other: float | int | Wallet):
        return not self.__eq__(other)


















