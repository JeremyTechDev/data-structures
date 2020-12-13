import unittest
from _queues import Queue


class TestQueues(unittest.TestCase):

    def test_init(self):
        queue = Queue()
        self.assertEqual(queue.data, [])

    def test_push(self):
        queue = Queue()
        queue.push(5)
        self.assertEqual(queue.data, [5])
        self.assertEqual(queue.size(), 1)
        queue.push(5)
        self.assertEqual(queue.data, [5, 5])
        self.assertEqual(queue.size(), 2)

    def test_pop(self):
        queue = Queue()
        self.assertRaises(Exception, queue.pop)

        queue.push(5)
        queue.push(4)
        self.assertEqual(queue.pop(), 5)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.pop(), 4)
        self.assertEqual(queue.size(), 0)
        self.assertRaises(Exception, queue.pop)

    def test_peek(self):
        queue = Queue()
        self.assertRaises(Exception, queue.peek)

        queue.push(5)
        queue.push(4)
        self.assertEqual(queue.peek(), 5)
        self.assertEqual(queue.size(), 2)
        queue.pop()
        self.assertEqual(queue.peek(), 4)
        self.assertEqual(queue.size(), 1)

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)
        queue.push(1)
        self.assertEqual(queue.size(), 1)
        queue.push(2)
        self.assertEqual(queue.size(), 2)

    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.push(1)
        self.assertFalse(queue.is_empty())


if __name__ == "__main__":
    unittest.main()
