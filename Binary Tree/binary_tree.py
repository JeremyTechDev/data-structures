# Binary Tree Implementation

# Node class for Binary Tree
class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insert a new node to the tree
    def insert(self, data):
        if data <= self.data:
            if self.left == None:
                self.left = BinaryTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = BinaryTree(data)
            else:
                self.right.insert(data)

    def contains(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left != None:
                if self.left.data == value:
                    return True
                else:
                    return self.left.contains(value)
        else:
            if self.right != None:
                if self.right.data == value:
                    return True
                else:
                    return self.right.contains(value)

    # Print all element is order
    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()
        print(self.data)
        if self.right != None:
            self.right.printInOrder()

    # Returns the sum of all the values in the tree
    def sum(self):
        curr_sum = self.data
        if self.left:
            curr_sum += self.left.sum()
        if self.right:
            curr_sum += self.right.sum()
        return curr_sum

    # Checks whether a tree is unival (all element are equal)
    def is_unival(self):
        if self.left and self.data != self.left.data:
            return False
        if self.right and self.data != self.right.data:
            return False
        if self.left and self.left.is_unival() == False:
            return False
        if self.right and self.right.is_unival() == False:
            return False
        return True

    # Checks only if the given node is unival
    def is_node_unival(self):
        if self.left == None and self.right == None:
            return True
        if self.left and self.left.data != self.data:
            return False
        if self.right and self.right.data != self.data:
            return False
        return True

    def count_univals(self):
        count = 0
        if self.is_node_unival():
            count += 1
        if self.left:
            count += self.left.count_univals()
        if self.right:
            count +=  self.right.count_univals()
        return count