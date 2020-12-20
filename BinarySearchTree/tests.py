import unittest
from binary_search_tree import BinarySearchTree


class TestBinaryTree(unittest.TestCase):

    def test_init(self):
        btree = BinarySearchTree()
        self.assertEqual(btree.data, None)
        self.assertEqual(btree.left, None)
        self.assertEqual(btree.right, None)
        btree = BinarySearchTree(0)
        self.assertEqual(btree.data, 0)
        self.assertEqual(btree.left, None)
        self.assertEqual(btree.right, None)
        btree = BinarySearchTree([2, 1, 3])
        self.assertEqual(btree.data, 2)
        self.assertEqual(btree.left.data, 1)
        self.assertEqual(btree.right.data, 3)

    def test_insert(self):
        btree = BinarySearchTree(2)
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
        btree = BinarySearchTree(2)
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
        btree = BinarySearchTree(2)
        self.assertEqual(btree.sum(), 2)
        btree.insert(1)
        btree.insert(3)
        btree.insert(0)
        btree.insert(4)
        self.assertEqual(btree.sum(), 10)

    def test_is_unival(self):
        btree = BinarySearchTree(0)
        self.assertTrue(btree.is_unival())

        btree = BinarySearchTree(5)
        btree.insert(5)
        btree.insert(5)
        btree.insert(5)
        self.assertTrue(btree.is_unival())

        btree = BinarySearchTree(5)
        btree.insert(5)
        btree.insert(5)
        btree.insert(1)
        self.assertFalse(btree.is_unival())

        btree = BinarySearchTree(1)
        btree.insert(5)
        btree.insert(5)
        self.assertFalse(btree.is_unival())

    def test_is_node_unival(self):
        btree = BinarySearchTree(1)
        self.assertTrue(btree.is_node_unival())
        btree.insert(1)
        self.assertTrue(btree.is_node_unival())
        btree.insert(1)
        self.assertTrue(btree.is_node_unival())
        btree = BinarySearchTree(1)
        btree.insert(2)
        self.assertFalse(btree.is_node_unival())

    def test_count_univals(self):
        btree = BinarySearchTree(5)
        btree.insert(5)
        self.assertEqual(btree.count_univals(), 2)
        btree.insert(3)
        btree.insert(5)
        btree.insert(5)
        btree.insert(3)
        self.assertEqual(btree.count_univals(), 5)

    def test_max_depth(self):
        btree = BinarySearchTree(2)
        self.assertEqual(btree.max_depth(), 1)
        btree.insert(3)
        btree.insert(1)
        self.assertEqual(btree.max_depth(), 2)
        btree.insert(4)
        btree.insert(4)
        self.assertEqual(btree.max_depth(), 4)

    def test_min_depth(self):
        btree = BinarySearchTree(2)
        self.assertEqual(btree.min_depth(), 1)
        btree.insert(3)
        btree.insert(1)
        self.assertEqual(btree.min_depth(), 2)
        btree.insert(4)
        btree.insert(4)
        self.assertEqual(btree.min_depth(), 2)
        btree.insert(0)
        self.assertEqual(btree.min_depth(), 3)

    def test_has_path_sum(self):
        btree = BinarySearchTree(2)
        self.assertTrue(btree.has_path_sum(2))
        self.assertFalse(btree.has_path_sum(5))
        btree.insert(5)
        self.assertFalse(btree.has_path_sum(2))
        self.assertTrue(btree.has_path_sum(7))
        btree.insert(1)
        self.assertTrue(btree.has_path_sum(3))
        self.assertTrue(btree.has_path_sum(7))
        btree.insert(7)
        self.assertTrue(btree.has_path_sum(14))
        self.assertTrue(btree.has_path_sum(3))
        self.assertFalse(btree.has_path_sum(5))

    def test_convert_to_array(self):
        btree = BinarySearchTree(2)
        self.assertEqual(btree.convert_to_array(), [2])
        btree.insert(1)
        btree.insert(3)
        self.assertEqual(btree.convert_to_array(), [1, 2, 3])
        btree.insert(4)
        btree.insert(0)
        btree.insert(5)
        self.assertEqual(btree.convert_to_array(), [0, 1, 2, 3, 4, 5])

    def test_balance(self):
        btree = BinarySearchTree(3)
        btree.insert(2)
        btree.insert(1)
        btree.insert(0)
        btree.insert(4)
        btree.insert(5)
        btree = btree.balance()
        self.assertEqual(btree.data, 2)
        self.assertEqual(btree.left.data, 0)
        self.assertEqual(btree.right.data, 4)
        self.assertEqual(btree.left.right.data, 1)
        self.assertEqual(btree.right.left.data, 3)
        self.assertEqual(btree.right.right.data, 5)

    def test_build_balanced_tree(self):
        btree = BinarySearchTree(0)
        btree = btree.build_balanced_tree([0, 1, 2, 3, 4, 5], 0, 5)
        self.assertEqual(btree.data, 2)
        self.assertEqual(btree.left.data, 0)
        self.assertEqual(btree.right.data, 4)
        self.assertEqual(btree.left.right.data, 1)
        self.assertEqual(btree.right.left.data, 3)
        self.assertEqual(btree.right.right.data, 5)

    def test_invert(self):
        btree = BinarySearchTree(2)
        btree.insert(1)
        btree.insert(3)
        btree.insert(0)
        btree = btree.invert()
        self.assertEqual(btree.left.data, 3)
        self.assertEqual(btree.left.left, None)
        self.assertEqual(btree.left.right, None)
        self.assertEqual(btree.right.data, 1)
        self.assertEqual(btree.right.right.data, 0)
        self.assertEqual(btree.right.left, None)

    def test_find_height(self):
        btree = BinarySearchTree(2)
        self.assertEqual(btree.find_height(), 1)
        btree.insert(3)
        btree.insert(4)
        self.assertEqual(btree.find_height(), 3)
        btree.insert(1)
        self.assertEqual(btree.find_height(), 3)

    def test_is_balanced(self):
        btree = BinarySearchTree(2)
        self.assertTrue(btree.is_balanced())
        btree.insert(3)
        self.assertTrue(btree.is_balanced())
        btree.insert(4)
        self.assertFalse(btree.is_balanced())
        btree.insert(1)
        self.assertTrue(btree.is_balanced())


if __name__ == '__main__':
    unittest.main()
