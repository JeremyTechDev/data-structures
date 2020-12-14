import unittest
from doubly_linked_list import DoublyLinkedList, Node


class TestDoublyLinkedList(unittest.TestCase):

    def test_node(self):
        node = Node(0)
        self.assertEqual(node.data, 0)
        self.assertEqual(node.next, None)
        self.assertEqual(node.prev, None)

    def test_init(self):
        llist = DoublyLinkedList()
        self.assertEqual(llist.size, 0)
        self.assertEqual(llist.head, None)
        self.assertEqual(llist.tail, None)

    def test_clear(self):
        llist = DoublyLinkedList()
        llist.insert_first(0)
        llist.clear()

        self.assertEqual(llist.size, 0)
        self.assertEqual(llist.head, None)
        self.assertEqual(llist.tail, None)

    def test_is_empty(self):
        llist = DoublyLinkedList()
        self.assertTrue(llist.is_empty())

        llist.insert_first(0)
        self.assertFalse(llist.is_empty())

    def test_insert_first(self):
        llist = DoublyLinkedList()
        llist.insert_first(0)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 0)
        self.assertEqual(llist.tail.data, 0)

        llist.insert_first(1)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, 1)
        self.assertEqual(llist.tail.data, 0)

        llist.insert_first(2)
        self.assertEqual(llist.size, 3)
        self.assertEqual(llist.head.data, 2)
        self.assertEqual(llist.head.next.data, 1)
        self.assertEqual(llist.tail.data, 0)

    def test_insert_last(self):
        llist = DoublyLinkedList()
        llist.insert_last(0)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 0)
        self.assertEqual(llist.tail.data, 0)

        llist.insert_last(1)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, 0)
        self.assertEqual(llist.tail.data, 1)

        llist.insert_last(2)
        self.assertEqual(llist.size, 3)
        self.assertEqual(llist.head.data, 0)
        self.assertEqual(llist.head.next.data, 1)
        self.assertEqual(llist.tail.data, 2)

    def test_insert_at(self):
        llist = DoublyLinkedList()
        self.assertRaises(Exception, llist.insert_at, 1, 0)

        llist.insert_at(0, 0)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 0)
        self.assertEqual(llist.tail.data, 0)

        llist.insert_at(0, -1)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, -1)
        self.assertEqual(llist.tail.data, 0)

        llist.insert_at(2, 1)
        self.assertEqual(llist.size, 3)
        self.assertEqual(llist.head.data, -1)
        self.assertEqual(llist.head.next.data, 0)
        self.assertEqual(llist.tail.data, 1)

    def test_peek_first(self):
        llist = DoublyLinkedList()
        self.assertRaises(Exception, llist.peek_first)

        llist.insert_first(0)
        self.assertEqual(llist.peek_first(), 0)

    def test_peek_last(self):
        llist = DoublyLinkedList()
        self.assertRaises(Exception, llist.peek_last)

        llist.insert_first(0)
        self.assertEqual(llist.peek_last(), 0)

    def test_remove_first(self):
        llist = DoublyLinkedList()
        self.assertRaises(Exception, llist.remove_first)

        llist.insert_first(0)
        self.assertEqual(llist.remove_first(), 0)
        self.assertEqual(llist.size, 0)

        llist.insert_first(0)
        llist.insert_last(1)
        self.assertEqual(llist.remove_first(), 0)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.remove_first(), 1)
        self.assertEqual(llist.size, 0)

    def test_remove_last(self):
        llist = DoublyLinkedList()
        self.assertRaises(Exception, llist.remove_last)

        llist.insert_first(0)
        self.assertEqual(llist.remove_last(), 0)
        self.assertEqual(llist.size, 0)

        llist.insert_first(0)
        llist.insert_last(1)
        self.assertEqual(llist.remove_last(), 1)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.remove_last(), 0)
        self.assertEqual(llist.size, 0)

    def test_remove(self):
        llist = DoublyLinkedList()
        self.assertRaises(Exception, llist.remove, 0)

        llist.insert_first(0)
        llist.insert_first(1)
        llist.insert_first(2)

        self.assertEqual(llist.remove(1), 1)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, 2)
        self.assertEqual(llist.tail.data, 0)

    def test_index_of(self):
        llist = DoublyLinkedList()
        llist.insert_last(0)
        llist.insert_last(1)

        self.assertEqual(llist.index_of(0), 0)
        self.assertEqual(llist.index_of(1), 1)
        self.assertEqual(llist.index_of(2), -1)

    def test_contains(self):
        llist = DoublyLinkedList()
        llist.insert_last(1)
        self.assertTrue(llist.contains(1))
        self.assertFalse(llist.contains(0))

    def test_reverse(self):
        llist = DoublyLinkedList()
        llist.insert_last(1)
        llist.insert_last(2)
        llist.insert_last(3)
        llist.reverse()
        self.assertEqual(llist.head.data, 3)
        self.assertEqual(llist.head.prev, None)
        self.assertEqual(llist.head.next.data, 2)
        self.assertEqual(llist.head.next.prev.data, 3)
        self.assertEqual(llist.head.next.next.data, 1)
        self.assertEqual(llist.head.next.next.prev.data, 2)
        self.assertEqual(llist.head.next.next.next, None)


if __name__ == '__main__':
    unittest.main()
