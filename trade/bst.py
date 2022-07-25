from __future__ import annotations
from abc import abstractmethod
from typing import *

Comparable = TypeVar('Comparible')


class BSTOperator(Generic[Comparable]):

    @abstractmethod
    def compare(self, x: Comparable, y: Comparable):
        raise NotImplementedError


class Less(BSTOperator):

    def compare(self, x: Comparable, y: Comparable):
        return x < y


class BST:
    class bst_node:
        def __init__(self, val):
            self.left: Optional[BST.bst_node] = None
            self.right: Optional[BST.bst_node] = None
            self.data: Comparable = val
            self.count = 1

        def __str__(self):
            return self.data.__str__()

    def __init__(self, root=None):
        self._root: Optional[BST.bst_node] = root

    def __str__(self):
        return self.to_list_inorder()

    def find_min(self, t:Optional[BST.bst_node]):
        if not t:
            t = self._root
        return self._find_min(t)

    def find_max(self, t:Optional[BST.bst_node]):
        if not t:
            t = self._root
        return self._find_min(t)

    def contains(self, x: Comparable):
        return self._contains(x, self._root)

    def is_empty(self):
        return self._is_empty(self._root)

    def printTree(self):
        s = ""
        return self._printTree(self._root, s)

    def make_empty(self):
        return self._make_empty(self._root)

    def insert(self, x: Comparable):
        self._root = self._insert(x, self._root)

    def remove(self, x: Comparable):
        return self._remove(x, self._root)

    def inorder(self, fn: Callable):
        results = []
        self._inorder(self._root, fn, results)
        return results

    def to_list_inorder(self):
        res = []
        self._inorder(self._root, lambda x: x, res)
        return res

    def _inorder(self, t: BST.bst_node, fn: Callable, results: List):
        if not t:
            return
        else:
            self._inorder(t.left, fn, results)
            # print(root.value, end=" -> ")
            results.append(fn(t.data))
            self._inorder(t.right, fn, results)

    def _find_min(self, t: BST.bst_node):
        if not t:
            return
        if t.left is None:
            return t
        return self._find_min(t.left)

    def _find_max(self, t: BST.bst_node):
        if not t:
            return
        if t.right is None:
            return t
        return self._find_max(t.right)

    def _contains(self, x: Comparable, t: BST.bst_node):
        if t is None:
            return False
        elif t.data < x:
            self._contains(x, t.left)
        elif x < t.data:
            self._contains(x, t.right)
        else:
            return True

    def _is_empty(self, t: BST.bst_node):
        return t is None

    def _printTree(self, t: BST.bst_node, s: str):
        if not t:
            return None
        self._printTree(t.left, s)
        print(t.data)
        self._printTree(t.right, s)

    def _make_empty(self, t: BST.bst_node):
        pass

    def _insert(self, x: Comparable, t: BST.bst_node):
        if t is None:
            t = self.bst_node(x)
        elif x < t.data:
            t.left = self._insert(x, t.left)
        elif t.data < x:
            t.right = self._insert(x, t.right)
        else:
            t.count += 1
        return t

    def _remove(self, x: Comparable, t: BST.bst_node):
        if not t:
            return
        if x < t.data:
            self._remove(x, t.left)
        elif t.data < x:
            self._remove(x, t.right)
        elif t.left and t.right:
            t.data = self.find_min(t.right).data
