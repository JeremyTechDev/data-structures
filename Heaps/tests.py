import unittest
from heap import MinHeap


class TestMinHeap(unittest.TestCase):
    def test_init(self):
        heap = MinHeap()
        self.assertEqual(heap.size(), 0)
        self.assertEqual(heap.data, [])

    def test_size(self):
        heap = MinHeap()
        self.assertEqual(heap.size(), 0)
        heap.add(4)
        heap.add(5)
        heap.add(2)
        self.assertEqual(heap.size(), 3)

    def test_add(self):
        heap = MinHeap()
        heap.add(0)
        self.assertEqual(heap.size(), 1)
        self.assertEqual(heap.data, [0])
        heap.add(1)
        self.assertEqual(heap.size(), 2)
        self.assertEqual(heap.data, [0, 1])
        heap.add(-1)
        self.assertEqual(heap.size(), 3)
        self.assertEqual(heap.data, [-1, 1, 0])

    def test_poll(self):
        heap = MinHeap()
        heap.add(0)
        self.assertEqual(heap.poll(), 0)
        self.assertTrue(heap.is_empty())
        heap.add(0)
        heap.add(5)
        heap.add(-1)
        self.assertEqual(heap.poll(), -1)
        self.assertEqual(heap.data, [0, 5])

    def test_remove(self):
        heap = MinHeap()
        self.assertRaises(Exception, heap.remove, 0)
        heap.add(0)
        self.assertRaises(Exception, heap.remove, 1)
        heap.add(1)
        heap.add(-1)
        heap.remove(0)
        self.assertEqual(heap.data, [-1, 1])
        heap.remove(-1)
        self.assertEqual(heap.data, [1])
        heap.remove(1)
        self.assertEqual(heap.data, [])

    def test_swim(self):
        heap = MinHeap()
        heap.data = [0, 1, -1]
        heap.swim(2)
        self.assertEqual(heap.data, [-1, 1, 0])

        heap.data = [-1, 1, 0, -5]
        heap.swim(3)
        self.assertEqual(heap.data, [-5, -1, 0, 1])

    def test_sink(self):
        heap = MinHeap()
        heap.data = [5, 0, 1, -1]
        heap.sink(0)
        self.assertEqual(heap.data, [0, -1, 1, 5])
        heap.data = [0, 10, 5, 2, 2]
        heap.sink(1)
        self.assertEqual(heap.data, [0, 2, 5, 10, 2])
        heap.sink(2)
        self.assertEqual(heap.data, [0, 2, 5, 10, 2])

    def test_swap(self):
        heap = MinHeap()
        heap.data = [5, 2]
        heap.swap(0, 1)
        self.assertEqual(heap.data, [2, 5])

    def test_is_empty(self):
        heap = MinHeap()
        self.assertTrue(heap.is_empty())
        heap.add(0)
        self.assertFalse(heap.is_empty())

    def test_peek(self):
        heap = MinHeap()
        self.assertEqual(heap.peek(), None)
        heap.add(0)
        self.assertEqual(heap.peek(), 0)
        heap.add(-1)
        self.assertEqual(heap.peek(), -1)

    def test_index(self):
        heap = MinHeap()
        self.assertEqual(heap.index(0), -1)
        heap.add(0)
        self.assertEqual(heap.index(0), 0)
        heap.add(-1)
        heap.add(1)
        self.assertEqual(heap.index(-1), 0)

    def test_contains(self):
        heap = MinHeap()
        self.assertFalse(heap.contains(0))
        heap.add(0)
        self.assertTrue(heap.contains(0))
        self.assertFalse(heap.contains(1))


if __name__ == '__main__':
    unittest.main()
