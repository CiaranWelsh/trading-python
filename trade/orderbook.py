
from trade.order import Order
from typing import *
from queue import PriorityQueue
import binarytree as bt
from binarytree import Node

# use (price - closest

# Make order book a binary search tree

class OrderBook:

    def __init__(self, current_price):
        self._current_price = current_price
        self._orders : Optional[Node] = None

    def update_price(self, new_price):
        self._current_price = new_price

    def place(self, order:Order):
        node = Node(value=order)
        if self._orders is None:
            self._orders = node
        else:
            if self._orders.value < node.value:
                if self._orders.right is None:
                    self._orders.right = node
                else:
                    self.place( order)
            else:
                if self._orders.left is None:
                    self._orders.left = node
                else:
                    self.place( order)

    def __str__(self):
        return self._orders.__str__()
