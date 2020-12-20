# Stack Implementation

# Stack Class (LIFO)
class Stack():
    def __init__(self, initial_data=[]):
        if isinstance(initial_data, int):
            self.data = [initial_data]
            return
        self.data = list(initial_data)

    # Inserts a element at the top of the stack
    def push(self, element):
        self.data.append(element)

    # Removes and returns the first element in the stack (last in the list)
    def pop(self):
        if self.is_empty():
            raise Exception("Attempt to pop from an empty stack")
        return self.data.pop()

    # Returns the first element in the stack (last in the list)
    def peek(self):
        if self.is_empty():
            raise Exception("Attempt to peek from an empty stack")
        return self.data[len(self.data) - 1]

    # Returns the size of the stack
    def size(self):
        return len(self.data)

    # Returns whether the stack is empty
    def is_empty(self):
        return self.size() == 0

    # Represetantion method
    def __repr__(self):
        return f"Stack({repr(self.data)})"

    # Convert to string method
    def __str__(self):
        return str(self.data)

    # Len of linked list
    def __len__(self):
        return len(self.data)
