# A complete linked list implementation

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head to null
        self.size = 0

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

        # If the list is empty, just push the new node
        if self.head == None:
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
            print("The given at position is invalid")
            return

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
        curr_node.next = new_node
        self.size += 1

    # Gets the first element of the list
    def peek_first(self):
        if (self.is_empty()):
            print("No elements in the list")
            return
        return self.head.data

    # Gets the last element of the list
    def peek_last(self):
        if (self.is_empty()):
            print("No elements in the list")
            return

        last = self.head
        while last.next:
            last = last.next
        return last.data

    # Removes all ocurrences of a piece of data
    def remove(self, to_remove):
        curr_node = self.head
        next_node = self.head.next

        # If node is at first position, just skip it
        if curr_node.data == to_remove:
            temp = self.head  # Save data to be able to return it
            self.head = self.head.next
            self.size -= 1
            return temp.data

        # Traverse until the node is found
        while next_node:
            if next_node.data == to_remove:
                temp = next_node  # Save next_node to to be able to return
                curr_node.next = next_node.next
                self.size -= 1
                return temp.data

            curr_node = curr_node.next
            next_node = next_node.next
        print("The element to remove was not found")

    # Removes the last element
    def remove_last(self):
        # If the list is empty
        if self.is_empty():
            print("Nothing to remove")
            return

        curr_node = self.head
        next_node = self.head.next

        while next_node.next:
            curr_node = curr_node.next
            next_node = next_node.next

        temp = next_node
        next_node = None
        curr_node.next = None
        return temp.data

    # Removes the first elem
    def remove_first(self):
        if self.is_empty():
            print("Nothing to remove")
            return

        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.data

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
        return self.indexOf(data) != -1

        # Print all elements
    def print(self):
        temp = self.head
        print("[", end='')
        while temp:
            if temp.next:
                print('"' + str(temp.data) + '", ', end='')
            else:
                print('"' + str(temp.data) + '"', end='')
            temp = temp.next
        print("] (" + str(self.size) + ")")
