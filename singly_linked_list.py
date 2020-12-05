# A complete linked list implementation

# Node Class
class Node:
    # Node initializer
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    # Linked List initializer
    def __init__(self):
        self.head = None  # Initialize head to null
        self.size = 0

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

    # To insert at the begining
    def shift(self, new_node):
        new_node = Node(new_node)  # Create the new node
        new_node.next = self.head  # Point new node next to the old head
        self.head = new_node  # Point head to the new node
        self.size += 1

    # To insert at the end
    def push(self, new_node):
        new_node = Node(new_node)  # Create the new node

        # If the list is empty, just push the new node
        if self.head == None:
            self.head = new_node
            self.size += 1
            return

        # Move to the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node  # Point the last element's next to the new node
        self.size += 1

    # To insert after a certain node
    def pushAfter(self, after, new_node):
        if after == None:
            print("The given after node is null")
            return

        new_node = Node(new_node)  # Create the new node
        new_node.next = after.next  # Point new node next to the after node next
        after.next = new_node  # Point after next to the new node
        self.size += 1

    # To remove a given node
    def remove(self, node_to_remove):
        trav1 = self.head  # Pointer to head
        trav2 = self.head.next  # Pointed to the head's next

        # If node is at first pos, just skip it
        if node_to_remove == trav1:
            temp = self.head  # Save head to to be able to return
            self.head = self.head.next
            self.size -= 1
            return temp

        # Traverse until the node is found
        while trav2:
            if node_to_remove == trav2:
                temp = trav2  # Save trav2 to to be able to return
                trav1.next = trav2.next  # Skip the node pointing the prev to the node's next
                self.size -= 1
                return temp
            trav1 = trav1.next
            trav2 = trav2.next
        print("The element to remove was not found")

    # To remove the last element
    def pop(self):
        last = self.head

        # If the list is empty
        if last == None:
            print("Nothing to pop")
            return

        # If the list has only one element
        if last.next == None:
            temp = self.head  # Save head to to be able to return
            self.head = None
            self.size -= 1
            return temp

        # Move to the last element and remove
        while last.next.next:
            last = last.next
            temp = last.next  # Save last to to be able to return
        last.next = None
        self.size -= 1
        return temp

    # To remove the first elem
    def unshift(self):
        if self.head == None:
            print("Nothing to unshift")
            return
        temp = self.head  # Save trav2 to to be able to return
        self.head = self.head.next  # skip the first element
        self.size -= 1
        return temp

    # Returns the index of a piece of data in the list, -1 otherwise
    def indexOf(self, data):
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
