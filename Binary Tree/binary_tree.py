# Binary Tree Implementation
from typing import List


# Node class for Binary Tree
class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insert a new node to the tree
    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = BinaryTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = BinaryTree(data)
            else:
                self.right.insert(data)

    # Returns whether the tree contains a given value
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
    def print_in_order(self):
        if self.left != None:
            self.left.print_in_order()
        print(self.data)
        if self.right != None:
            self.right.print_in_order()

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

    # Counts the number of unival nodes given a tree
    def count_univals(self):
        count = 0
        if self.is_node_unival():
            count += 1
        if self.left:
            count += self.left.count_univals()
        if self.right:
            count += self.right.count_univals()
        return count

    # Returns the depth of the furthest node to the root
    def max_depth(self):
        left = right = 0
        if self.left:
            left = self.left.max_depth()
        if self.right:
            right = self.right.max_depth()
        return max(left, right) + 1

    # Returns the depth of the closest children to the root
    def min_depth(self):
        left = right = 0
        if self.left:
            left = self.left.min_depth()
        if self.right:
            right = self.right.min_depth()

        if left == 0 or right == 0:
            return (left if right == 0 else right) + 1
        return min(left, right) + 1

    # Returns whether one path of the tree has a path sum equal to @param {sum}
    def has_path_sum(self, sum):
        if self.left == None and self.right == None:
            return sum - self.data == 0
        return (self.left and self.left.has_path_sum(sum - self.data)) or (self.right and self.right.has_path_sum(sum - self.data))

    # Returns a sorted array version of the given tree
    def convert_to_array(self):
        arr = []
        if self.left:
            arr.extend(self.left.convert_to_array())
        arr.append(self.data)
        if self.right:
            arr.extend(self.right.convert_to_array())
        return arr

    # Builds a balances BST from a sorted array
    def build_balanced_tree(self, sorted_arr: List[int], start: int, end: int):
        if start > end:
            return None

        mid = (start + end) // 2
        root = BinaryTree(sorted_arr[mid])

        root.left = self.build_balanced_tree(sorted_arr, start, mid - 1)
        root.right = self.build_balanced_tree(sorted_arr, mid + 1, end)
        return root

    # Balances the height of the given tree
    def balance(self):
        arr = self.convert_to_array()
        return self.build_balanced_tree(arr, 0, len(arr) - 1)

    # Inverts a binary tree
    def invert(self):
        left = self.left
        right = self.right
        self.left = right.invert() if right else None
        self.right = left.invert() if left else None
        return self

    # Finds the height of a tree
    def find_height(self):
        left_height = right_height = 0
        if self.left:
            left_height = self.left.find_height()
        if self.right:
            right_height = self.right.find_height()
        return max(left_height, right_height) + 1

    # Returns whether a tree is balanced
    def is_balanced(self):
        if self.left == None and self.right == None:
            return True
        left_height = right_height = 0
        if self.left:
            left_height = self.left.find_height()
        if self.right:
            right_height = self.right.find_height()
        return abs(left_height - right_height) <= 1
