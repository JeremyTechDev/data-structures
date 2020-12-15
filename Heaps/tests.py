import unittest
from heap import MinHeap


class TestMinHeap(unittest.TestCase):
    def test_init(self):
        heap = MinHeap()
        self.assertEqual(heap.size, 0)
        self.assertEqual(heap.data, [])

    def test_add(self):
        heap = MinHeap()
        heap.add(0)
        self.assertEqual(heap.size, 1)
        self.assertEqual(heap.data, [0])
        heap.add(1)
        self.assertEqual(heap.size, 2)
        self.assertEqual(heap.data, [0, 1])
        heap.add(-1)
        self.assertEqual(heap.size, 3)
        self.assertEqual(heap.data, [-1, 1, 0])


if __name__ == '__main__':
    unittest.main()
