import unittest
from hash_table import Entry, HashTable


class TestHashTable(unittest.TestCase):

    def test_entry_init(self):
        entry = Entry('key', 0, 0)
        self.assertEqual(entry.key, 'key')
        self.assertEqual(entry.value, 0)
        self.assertEqual(entry.hash, 0)

    def test_entry_eq(self):
        entry1 = Entry('key', 0, 0)
        entry2 = Entry('key', 0, 0)
        entry3 = Entry('key', 0, 1)
        self.assertTrue(entry1 == entry2)
        self.assertFalse(entry1 == entry3)

    def test_init(self):
        self.assertRaises(Exception, HashTable, -1)
        self.assertRaises(Exception, HashTable, 3, -1)

        table = HashTable()
        self.assertEqual(table.capacity, 3)
        self.assertEqual(table.max_load_factor, 0.75)
        self.assertEqual(table.table, [None] * table.capacity)
        self.assertEqual(len(table), 0)
        self.assertEqual(table.threshold, table.capacity *
                         table.max_load_factor)

        table = HashTable(5, 0.5)
        self.assertEqual(table.capacity, 5)
        self.assertEqual(table.max_load_factor, 0.5)
        self.assertEqual(table.table, [None] * table.capacity)
        self.assertEqual(len(table), 0)
        self.assertEqual(table.threshold, table.capacity *
                         table.max_load_factor)

    def test_hash(self):
        table = HashTable(10)
        hash1 = table.hash('key')
        hash2 = table.hash('not-the-same-key')
        self.assertGreaterEqual(hash1, 0)
        self.assertLessEqual(hash1, table.capacity)
        self.assertNotEqual(hash1, hash2)

    def test_contains(self):
        table = HashTable()
        table.insert('key', 'value')
        self.assertTrue(table.contains('key'))
        self.assertFalse(table.contains('key1'))

    def test_is_empty(self):
        table = HashTable()
        self.assertTrue(table.is_empty())
        table.insert('key', 0)
        self.assertFalse(table.is_empty())

    def test_clear(self):
        table = HashTable()
        table.insert('key1', 1)
        table.insert('key2', 2)
        table.insert('key3', 3)
        self.assertEqual(len(table), 3)
        table.clear()
        self.assertEqual(len(table), 0)
        self.assertEqual(table.table, [None] * table.capacity)

    def test_insert(self):
        table = HashTable()
        self.assertRaises(Exception, table.insert, None, 0)

        new_entry = table.insert('key', 'value')
        self.assertEqual(new_entry, None)
        self.assertTrue(table.contains('key'))
        self.assertEqual(len(table), 1)
        new_entry = table.insert('key', 'new_value')
        self.assertEqual(new_entry, 'value')
        self.assertTrue(table.contains('key'))
        self.assertEqual(len(table), 1)

    def test_get(self):
        table = HashTable()
        self.assertRaises(Exception, table.get, None)

        new_entry = table.insert('key', 'value')
        self.assertEqual(new_entry, None)
        self.assertTrue(table.get('key'), 'value')
        new_entry = table.insert('key', 'new_value')
        self.assertEqual(new_entry, 'value')
        self.assertTrue(table.get('key'), 'new_value')

    def test_remove(self):
        table = HashTable()
        self.assertRaises(Exception, table.remove, None)

        table.insert('key', 'value')
        self.assertEqual(table.remove('key'), 'value')
        self.assertEqual(table.remove('key'), None)
        self.assertEqual(len(table), 0)

    def test_len(self):
        table = HashTable()
        self.assertEqual(len(table), 0)
        table.insert('key1', 1)
        table.insert('key2', 2)
        table.insert('key3', 3)
        self.assertEqual(len(table), 3)
        table.remove('key1')
        self.assertEqual(len(table), 2)

    def test_keys(self):
        table = HashTable()
        table.insert('key1', 1)
        table.insert('key2', 2)
        table.insert('key3', 3)
        self.assertEqual(table.keys(), ['key1', 'key2', 'key3'])

    def test_values(self):
        table = HashTable()
        table.insert('key1', 1)
        table.insert('key2', 2)
        table.insert('key3', 3)
        self.assertEqual(table.values(), [1, 2, 3])

    def test_items(self):
        table = HashTable()
        table.insert('key1', 1)
        table.insert('key2', 2)
        table.insert('key3', 3)
        self.assertEqual(
            table.items(), [('key1', 1), ('key2', 2), ('key3', 3)])


if __name__ == '__main__':
    unittest.main()
