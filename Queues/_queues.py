# Queue Implementation

# Queue Class (FIFO)
class Queue():
    def __init__(self):
        self.data = []

    # Inserts a new element the the queue
    def push(self, element):
        self.data.append(element)

    # Removes and returns the first element of the queue
    def pop(self):
        if self.is_empty():
            raise Exception("Attempt to pop from an empty queue")
        element = self.data[0]
        self.data = self.data[1:]
        return element

    # Returns the first element of the queue
    def peek(self):
        if self.is_empty():
            raise Exception("Attempt to pop from an empty queue")
        return self.data[0]

    # Returns the number of elements in the queue
    def size(self):
        return len(self.data)

    # Returns whether the queue is empty or not
    def is_empty(self):
        return len(self.data) == 0
