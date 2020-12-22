import unittest
from singly_linked_list import SinglyLinkedList, Node


class TestSinglyLinkedList(unittest.TestCase):

    def test_node(self):
        node = Node(0)
        self.assertEqual(node.data, 0)
        self.assertEqual(node.next, None)

    def test_inti(self):
        llist = SinglyLinkedList()
        self.assertEqual(llist.size, 0)
        self.assertEqual(llist.head, None)
        llist = SinglyLinkedList(5)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 5)
        llist = SinglyLinkedList([1, 2, 3])
        self.assertEqual(llist.size, 3)
        self.assertEqual(llist.head.data, 1)
        self.assertEqual(llist.head.next.data, 2)
        self.assertEqual(llist.head.next.next.data, 3)

    def test_clear(self):
        llist = SinglyLinkedList()
        llist.insert_first(0)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 0)

        llist.clear()
        self.assertEqual(llist.size, 0)
        self.assertEqual(llist.head, None)

    def test_is_empty(self):
        llist = SinglyLinkedList()
        self.assertTrue(llist.is_empty())
        llist.insert_first(0)
        self.assertFalse(llist.is_empty())

    def test_insert_first(self):
        llist = SinglyLinkedList()
        llist.insert_first(1)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 1)

        llist.insert_first(0)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, 0)
        self.assertEqual(llist.head.next.data, 1)

    def test_insert_last(self):
        llist = SinglyLinkedList()
        llist.insert_last(0)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 0)

        llist.insert_last(1)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, 0)
        self.assertEqual(llist.head.next.data, 1)

    def test_insert_at(self):
        llist = SinglyLinkedList()
        self.assertRaises(Exception, llist.insert_at, 1, 0)

        llist.insert_at(0, 0)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 0)

        llist.insert_at(0, -1)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, -1)
        self.assertEqual(llist.head.next.data, 0)

        llist.insert_at(2, 1)
        self.assertEqual(llist.size, 3)
        self.assertEqual(llist.head.data, -1)
        self.assertEqual(llist.head.next.data, 0)
        self.assertEqual(llist.head.next.next.data, 1)

    def test_peek_first(self):
        llist = SinglyLinkedList()
        self.assertRaises(Exception, llist.peek_first)

        llist.insert_first(0)
        self.assertEqual(llist.peek_first(), 0)
        llist.insert_first(-1)
        self.assertEqual(llist.peek_first(), -1)

    def test_peek_last(self):
        llist = SinglyLinkedList()
        self.assertRaises(Exception, llist.peek_last)

        llist.insert_first(0)
        self.assertEqual(llist.peek_last(), 0)
        llist.insert_first(-1)
        self.assertEqual(llist.peek_last(), 0)

    def test_remove_first(self):
        llist = SinglyLinkedList()
        self.assertRaises(Exception, llist.remove_first)

        llist.insert_last(0)
        llist.insert_last(1)
        llist.insert_last(2)
        self.assertEqual(llist.remove_first(), 0)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, 1)
        self.assertEqual(llist.remove_first(), 1)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 2)
        self.assertEqual(llist.remove_first(), 2)
        self.assertEqual(llist.size, 0)
        self.assertEqual(llist.head, None)

    def test_remove_last(self):
        llist = SinglyLinkedList()
        self.assertRaises(Exception, llist.remove_last)

        llist.insert_last(0)
        llist.insert_last(1)
        llist.insert_last(2)
        self.assertEqual(llist.remove_last(), 2)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.next.next, None)
        self.assertEqual(llist.remove_last(), 1)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.next, None)
        self.assertEqual(llist.remove_last(), 0)
        self.assertEqual(llist.size, 0)
        self.assertEqual(llist.head, None)

    def test_remove(self):
        llist = SinglyLinkedList()
        self.assertRaises(Exception, llist.remove)

        llist.insert_last(0)
        llist.insert_last(1)
        llist.insert_last(2)
        llist.insert_last(3)
        self.assertEqual(llist.remove(0), 0)
        self.assertEqual(llist.size, 3)
        self.assertEqual(llist.head.data, 1)
        self.assertEqual(llist.remove(2), 2)
        self.assertEqual(llist.size, 2)
        self.assertEqual(llist.head.data, 1)
        self.assertEqual(llist.head.next.data, 3)
        self.assertEqual(llist.remove(3), 3)
        self.assertEqual(llist.size, 1)
        self.assertEqual(llist.head.data, 1)
        self.assertEqual(llist.head.next, None)
        self.assertEqual(llist.remove(1), 1)
        self.assertEqual(llist.size, 0)
        self.assertEqual(llist.head, None)

    def test_index_of(self):
        llist = SinglyLinkedList()

        llist.insert_last(0)
        llist.insert_last(1)
        llist.insert_last(2)

        self.assertEqual(llist.index_of(0), 0)
        self.assertEqual(llist.index_of(1), 1)
        self.assertEqual(llist.index_of(2), 2)
        self.assertEqual(llist.index_of(3), -1)

    def test_contains(self):
        llist = SinglyLinkedList()
        llist.insert_first(0)
        self.assertTrue(llist.contains(0))
        self.assertFalse(llist.contains(1))

    def test_contains(self):
        llist = SinglyLinkedList()
        llist.insert_last(1)
        llist.insert_last(2)
        llist.insert_last(3)
        llist.reverse()
        self.assertEqual(llist.head.data, 3)
        self.assertEqual(llist.head.next.data, 2)
        self.assertEqual(llist.head.next.next.data, 1)


if __name__ == '__main__':
    unittest.main()
