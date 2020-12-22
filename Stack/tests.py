import unittest
from _stacks import Stack


class TestStack(unittest.TestCase):

    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.data, [])
        stack = Stack(5)
        self.assertEqual(stack.data, [5])
        stack = Stack([1, 2, 3])
        self.assertEqual(stack.data, [1, 2, 3])

    def test_push(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.data, [5])
        self.assertEqual(stack.size(), 1)
        stack.push(5)
        self.assertEqual(stack.data, [5, 5])
        self.assertEqual(stack.size(), 2)

    def test_pop(self):
        stack = Stack()
        self.assertRaises(Exception, stack.pop)

        stack.push(5)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.size(), 0)
        self.assertRaises(Exception, stack.pop)

    def test_peek(self):
        stack = Stack()
        self.assertRaises(Exception, stack.peek)

        stack.push(5)
        stack.push(4)
        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.size(), 1)

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())


if __name__ == "__main__":
    unittest.main()
