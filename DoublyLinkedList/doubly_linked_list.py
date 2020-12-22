# A complete linked list implementation

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Linked List Class
class DoublyLinkedList:
    def __init__(self, initial_data=None):
        self.head = None
        self.tail = None
        self.size = 0
        if isinstance(initial_data, int):
            self.insert_first(initial_data)
        elif isinstance(initial_data, list):
            for num in initial_data:
                self.insert_last(num)

    # Empty the linked list
    def clear(self):
        trav = self.head
        while trav:
            next = trav.next
            trav.next = None
            trav.prev = None
            trav = next
        self.head = self.tail = trav = None
        self.size = 0

    # Checks if the linked list is empty
    def is_empty(self):
        return self.size == 0

    # Inserts at the begining
    def insert_first(self, new_node):
        new_node = Node(new_node)
        if self.is_empty():
            self.head = self.tail = new_node
            self.size += 1
            return

        new_node.next = self.head
        new_node.prev = None
        self.head = new_node
        self.head.next.prev = new_node
        self.size += 1

    # Inserts at the end
    def insert_last(self, new_node):
        new_node = Node(new_node)

        if self.is_empty():
            self.head = self.tail = new_node
            self.size += 1
            return

        new_node.next = None
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    # Inserts at a given position
    def insert_at(self, at, new_elem):
        if at < 0 or at > self.size:
            raise Exception('Overflow: The given "at" postion is invalid')

        if at == 0:
            self.insert_first(new_elem)
            return
        if at == self.size:
            self.insert_last(new_elem)
            return

        index = 1
        new_node = Node(new_elem)
        curr_node = self.head
        next_node = self.head.next
        while index < at:
            curr_node = curr_node.next
            next_node = next_node.next
            index += 1

        new_node.next = next_node
        new_node.prev = curr_node
        curr_node.next = new_node
        next_node.prev = new_node
        self.size += 1

    # Gets the first element of the list
    def peek_first(self):
        if (self.is_empty()):
            raise Exception("No elements in the list")
        return self.head.data

    # Gets the last element of the list
    def peek_last(self):
        if (self.is_empty()):
            raise Exception("No elements in the list")
        return self.tail.data

    # Removes the first elem
    def remove_first(self):
        if self.is_empty():
            raise Exception("Nothing to remove")

        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.data

    # Removes the last element
    def remove_last(self):
        if self.is_empty():
            raise Exception("Nothing to remove")

        temp = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1

        if self.is_empty():
            self.head = None
        return temp.data

    # Removes the first ocurrences of a piece of data
    def remove(self, to_remove):
        if self.is_empty():
            raise Exception("Nothing to remove")

        if self.head.data == to_remove:
            return self.remove_first()
        if self.tail.data == to_remove:
            return self.remove_last()

        curr_node = self.head
        next_node = self.head.next

        # Traverse until the node is found
        while next_node:
            if next_node.data == to_remove:
                temp = next_node
                next_node.next.prev = curr_node
                curr_node.next = next_node.next
                self.size -= 1
                return temp.data
            curr_node = curr_node.next
            next_node = next_node.next
        raise Exception("The element to remove was not found")

    # Returns the index of a piece of data in the list, -1 otherwise
    def index_of(self, data):
        index = 0
        last = self.head
        while last:
            if last.data == data:
                return index
            last = last.next
            index += 1
        return -1

    # Returns whether a piece of data is contianed in the list
    def contains(self, data):
        return self.index_of(data) != -1

    # Reverse the given linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev

        # Set new head only if it was not empty
        if prev != None:
            self.head = prev.prev

    # Represetantion method
    def __repr__(self):
        head = self.head
        arr = [] * self.size
        while head:
            arr.append(head.data)
            head = head.next
        return "DoublyLinkedList({})".format(arr.__repr__())

    # Convert to string method
    def __str__(self):
        head = self.head
        res = ''
        while head:
            res += str(head.data)
            if head.next:
                res += '->'
            head = head.next
        return res

    # Len of linked list
    def __len__(self):
        return self.size
