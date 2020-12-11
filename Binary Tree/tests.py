import unittest
from unittest.signals import installHandler
from binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def test_init(self):
        btree = BinaryTree(0)
        self.assertEqual(btree.data, 0)
        self.assertEqual(btree.left, None)
        self.assertEqual(btree.right, None)

    def test_insert(self):
        btree = BinaryTree(2)
        btree.insert(1)
        self.assertEqual(btree.left.data, 1)
        self.assertEqual(btree.right, None)
        btree.insert(3)
        self.assertEqual(btree.left.data, 1)
        self.assertEqual(btree.right.data, 3)
        btree.insert(0)
        self.assertEqual(btree.left.data, 1)
        self.assertEqual(btree.left.left.data, 0)
        btree.insert(4)
        self.assertEqual(btree.right.data, 3)
        self.assertEqual(btree.right.right.data, 4)

    def test_contains(self):
        btree = BinaryTree(2)
        btree.insert(1)
        btree.insert(3)
        btree.insert(0)
        btree.insert(4)

        self.assertTrue(btree.contains(0))
        self.assertTrue(btree.contains(1))
        self.assertTrue(btree.contains(2))
        self.assertTrue(btree.contains(3))
        self.assertTrue(btree.contains(4))
        self.assertFalse(btree.contains(-1))

    def test_sum(self):
        btree = BinaryTree(2)
        self.assertEqual(btree.sum(), 2)
        btree.insert(1)
        btree.insert(3)
        btree.insert(0)
        btree.insert(4)
        self.assertEqual(btree.sum(), 10)

    def test_is_unival(self):
        btree = BinaryTree(0)
        self.assertTrue(btree.is_unival())

        btree = BinaryTree(5)
        btree.insert(5)
        btree.insert(5)
        btree.insert(5)
        self.assertTrue(btree.is_unival())

        btree = BinaryTree(5)
        btree.insert(5)
        btree.insert(5)
        btree.insert(1)
        self.assertFalse(btree.is_unival())

        btree = BinaryTree(1)
        btree.insert(5)
        btree.insert(5)
        self.assertFalse(btree.is_unival())

    def test_is_node_unival(self):
        btree = BinaryTree(1)
        self.assertTrue(btree.is_node_unival())
        btree.insert(1)
        self.assertTrue(btree.is_node_unival())
        btree.insert(1)
        self.assertTrue(btree.is_node_unival())
        btree = BinaryTree(1)
        btree.insert(2)
        self.assertFalse(btree.is_node_unival())

    def test_count_univals(self):
        btree = BinaryTree(5)
        btree.insert(5)
        self.assertEqual(btree.count_univals(), 2)
        btree.insert(3)
        btree.insert(5)
        btree.insert(5)
        btree.insert(3)
        self.assertEqual(btree.count_univals(), 5)

    def test_max_depth(self):
        btree = BinaryTree(2)
        self.assertEqual(btree.max_depth(), 1)
        btree.insert(3)
        btree.insert(1)
        self.assertEqual(btree.max_depth(), 2)
        btree.insert(4)
        btree.insert(4)
        self.assertEqual(btree.max_depth(), 4)

    def test_min_depth(self):
        btree = BinaryTree(2)
        self.assertEqual(btree.min_depth(), 1)
        btree.insert(3)
        btree.insert(1)
        self.assertEqual(btree.min_depth(), 2)
        btree.insert(4)
        btree.insert(4)
        self.assertEqual(btree.min_depth(), 2)
        btree.insert(0)
        self.assertEqual(btree.min_depth(), 3)


if __name__ == '__main__':
    unittest.main()
