# Hash Table implementation
# Hash Table Entry Class Definition


from typing import List


class Entry:
    def __init__(self, key, value, hash):
        self.key = key
        self.value = value
        self.hash = hash

    # Representation of Entry
    def __repr__(self) -> str:
        return f'Entry("{self.key}", {self.value})'

    # Convertion to string method
    def __str__(self) -> str:
        return f'{self.key}: {self.value}'

    # Custom equality operator
    def __eq__(self, other) -> bool:
        if isinstance(other, Entry):
            if hash != other.hash:
                return False
            return self == other

        return NotImplemented


# Hash Table Class definition
class HashTable:
    default_capacity = 3
    default_load_factor = 0.75

    max_load_factor = 0
    capacity, threshold, size = 0, 0, 0
    table = []

    def __init__(self, capacity: int, max_load_factor: int) -> None:
        if capacity < 0:
            raise Exception("Invalid capacity")
        if max_load_factor <= 0 or not isinstance(max_load_factor, int):
            raise Exception("Invalid max load factor")

        self.capacity = max(self.default_capacity, capacity)
        self.max_load_factor = max_load_factor
        self.threshold = self.capacity * self.max_load_factor
        self.table = [None] * self.capacity

    # Calculate the hash for a key
    def hash(self, key: str):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    # Wether the table contains a key or not
    def contains(self, key: str):
        bucket_index = self.hash(key)
        return self.bucket_get_key(bucket_index, key) != None

    # Insert or update an entry in the table
    def insert(self, key: str, value: int):
        if key == None:
            raise Exception("Invalid null key")

        entry = Entry(key, value, self.hash(key))
        return self.bucket_insert_entry(entry.hash, entry)

    # Gets a the value of a key in the table
    def get(self, key: str):
        if key == None:
            raise Exception("Invalid null key")

        bucket_index = self.hash(key)
        entry = self.bucket_get_entry(bucket_index, key)
        if entry == None:
            return None
        return entry.value

    # Removes the entry with the given key
    def remove(self, key: str):
        if key == None:
            raise Exception("Invalid null key")

        bucket_index = self.hash(key)
        return self.bucket_remove_entry(bucket_index, key)

    # Removes an entry from its corresponding bucket in the table
    def bucket_remove_entry(self, bucket_index: int, key: str):
        entry = self.bucket_get_entry(bucket_index, key)
        if entry == None:
            return None

        bucket = self.table[bucket_index]
        bucket.remove(entry)
        self.size -= 1
        return entry.value

    # Inserts an entry in its corresponding bucket in the table
    # Returns the old value is the entry was just updates, None if its a new one
    def bucket_insert_entry(self, bucket_index: int, entry: Entry):
        bucket = self.table[bucket_index]

        # If the bucket was empty, create a new list in it
        if bucket == None:
            self.table[bucket_index] = bucket = []

        entry_exists = self.bucket_get_entry(bucket_index, entry.key)
        if entry_exists:
            old_value = entry_exists.value
            entry_exists.value = entry.value
            return old_value
        else:
            bucket.append(entry)
            self.size += 1
            return None

    # Returns an entry given its bucket and key
    def bucket_get_entry(self, bucket_index: int, key: str):
        if key == None:
            return None

        bucket = self.table[bucket_index]
        if bucket == None:
            return None

        for entry in bucket:
            if entry.key == key:
                return entry
        return None

    # Convert to string method
    def __str__(self):
        res = "{\n"
        for bucket in self.table:
            if isinstance(bucket, List):
                for entry in bucket:
                    res += (f'  "{entry.key}": {entry.value}\n')
        res += "}"
        return res

    # Returns the number of entries in the table
    def __len__(self):
        return self.size
