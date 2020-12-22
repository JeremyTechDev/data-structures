# A complete linked list implementation

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class SinglyLinkedList:
    def __init__(self, initial_data=None):
        self.head = None
        self.size = 0
        if isinstance(initial_data, int):
            self.head = Node(initial_data)
            self.size = 1
        elif isinstance(initial_data, list):
            for num in initial_data:
                self.insert_last(num)

    # Empty the linked list
    def clear(self):
        trav = self.head
        while trav:
            next = trav.next
            trav.next = None
            trav = next
        self.head = trav = None
        self.size = 0

    # Checks if the linked list is empty
    def is_empty(self):
        return self.size == 0

    # Inserts at the begining
    def insert_first(self, new_node):
        new_node = Node(new_node)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # Inserts at the end
    def insert_last(self, new_node):
        new_node = Node(new_node)

        if self.is_empty():
            self.head = new_node
            self.size += 1
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.size += 1

    # Inserts at a given position
    def insert_at(self, at, new_elem):
        if at < 0 or at > self.size:
            raise Exception("Overflow: The given at position is invalid")

        if at == 0:
            return self.insert_first(new_elem)
        if at == self.size:
            return self.insert_last(new_elem)

        index = 1
        new_node = Node(new_elem)
        curr_node = self.head
        next_node = self.head.next
        while index < at:
            curr_node = curr_node.next
            next_node = next_node.next
            index += 1
        new_node.next = next_node
        curr_node.next = new_node
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

        last = self.head
        while last.next:
            last = last.next
        return last.data

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

        if not self.head.next:
            temp = self.head
            self.head = None
            self.size -= 1
            return temp.data

        curr_node = self.head
        next_node = self.head.next

        while next_node.next:
            curr_node = curr_node.next
            next_node = next_node.next

        temp = next_node
        next_node = None
        curr_node.next = None
        self.size -= 1
        return temp.data

    # Removes the first ocurrences of a piece of data
    def remove(self, to_remove):
        if self.is_empty():
            raise Exception("Nothing to remove")

        if self.head.data == to_remove:
            return self.remove_first()

        curr_node = self.head
        next_node = self.head.next

        # Traverse until the node is found
        while next_node:
            if next_node.data == to_remove:
                temp = next_node  # Save next_node to to be able to return
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

    # Reverses the given linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Set new head only if it was not empty
        if prev != None:
            self.head = prev

    # Represetantion method
    def __repr__(self):
        head = self.head
        arr = [] * self.size
        while head:
            arr.append(head.data)
            head = head.next
        return "SinglyLinkedList({})".format(arr.__repr__())

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
