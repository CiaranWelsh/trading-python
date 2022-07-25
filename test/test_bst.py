import unittest

import pytest

from trade.bst import BST


class BSTTest(unittest.TestCase):


    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass

    def test_inorder_trversal(self):
        bst = BST()
        bst.insert(5)
        bst.insert(9)
        bst.insert(3)
        bst.insert(14)
        res = bst.to_list_inorder()
        expected = [3, 5, 9, 14]
        self.assertEqual(expected, res)

    def test_contains_when_true(self):
        bst = BST()
        bst.insert(5)
        bst.insert(9)
        bst.insert(3)
        bst.insert(14)
        self.assertTrue(bst.contains(5))

    def test_contains_when_false(self):
        bst = BST()
        bst.insert(5)
        bst.insert(9)
        bst.insert(3)
        bst.insert(14)
        self.assertFalse(bst.contains(6))

    def test_find_min(self):
        bst = BST()
        bst.insert(5)
        bst.insert(9)
        bst.insert(3)
        bst.insert(14)
        self.assertEqual(3, bst.find_min().data)

    def test_find_max(self):
        bst = BST()
        bst.insert(5)
        bst.insert(9)
        bst.insert(3)
        bst.insert(14)
        self.assertEqual(14, bst.find_max().data)











