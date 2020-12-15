# Min Heap Implementation

class MinHeap():
    def __init__(self):
        self.data = []

    # Add an element to the min heap
    def add(self, elem):
        self.data.append(elem)
        self.swim(len(self.data) - 1)

    # Returns the number of element in the heap
    def size(self):
        return len(self.data)

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
