# Min Heap Implementation

class MinHeap():
    def __init__(self):
        self.data = []

    # Returns the number of element in the heap
    def size(self):
        return len(self.data)

    # Add an element to the min heap
    def add(self, elem):
        self.data.append(elem)
        self.swim(len(self.data) - 1)

    # Removes and return the element with the highest priority (first element)
    def poll(self):
        if self.is_empty():
            raise Exception("Min heap is empty")

        polled = self.data[0]
        self.remove(polled)
        return polled

    # Removes an element form the heap
    def remove(self, elem):
        if self.is_empty():
            raise Exception("Min heap is empty")

        index = self.index(elem)
        if index == -1:
            raise Exception(f"Heap does not contain the element <{elem}>")

        self.swap(index, self.size() - 1)
        self.data.pop()

        # If the element was the last one, do nothing else
        if index == self.size():
            return

        if not self.is_empty():
            self.sink(index)
            self.swim(index)

    # Bubble up an element at a k position
    def swim(self, k):
        parent = (k - 1) // 2
        # Keep swimming while we have not reached the
        # root and while we're less than our parent.
        while k > 0 and self.data[k] < self.data[parent]:
            self.swap(k, parent)
            k = parent
            parent = (k - 1) // 2

    # Bubble down an element at a k position
    def sink(self, k):
        while True:
            left = 2 * k + 1
            right = 2 * k + 2
            smallest = left

            # Take the left children as smallest by default
            # Change only if right children is less than left children
            if right < self.size() and self.data[right] < self.data[left]:
                smallest = right

            # Keep swaping while k is less than parent and
            # we are not at the last position of the heap
            if left >= self.size() or self.data[k] < self.data[smallest]:
                break

            self.swap(k, smallest)
            k = smallest

    # Swaps the positions of two elements given their indexes
    def swap(self, i1, i2):
        elem1 = self.data[i1]
        elem2 = self.data[i2]
        self.data[i1] = elem2
        self.data[i2] = elem1

    # Returns whether the heap is empty
    def is_empty(self):
        return self.size() == 0

    # Returns the first element (smallest) of the heap
    def peek(self):
        return self.data[0] if not self.is_empty() else None

    # Returns the index of an element in the heap, -1 if it is not contained
    def index(self, elem):
        for index, value in enumerate(self.data):
            if value == elem:
                return index
        return -1

    # Whether an element in contained in the heap
    def contains(self, elem):
        return self.index(elem) != -1
