class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

# BST: Add
# Create an add(val) method on the BST object to add new value to the tree. 
# This entails creating a BTNode with this value and connecting it at the appropriate place in the tree. 
# Unless specified otherwise, BSTs can contain duplicate values.

    def add(self, val):
        if not self.root:
            new_node = Node(val)
            self.root = new_node
            return self
        runner = self.root
        new_node = Node(val)
        while runner != None:
            if val < runner.value:
                if runner.left == None:
                    runner.left = new_node
                    return self
                else:
                    runner = runner.left
            else:
                if runner.right == None:
                    runner.right = new_node
                    return self
                else:
                    runner = runner.right

# BST: Contains
# Create a contains(val) method on BST that returns whether the tree contains a given value. 
# Take advantage of the BST structure to make this a much more rapid operation than SList.contains() 
# would be.

    def contains(self, val):
        if self.root == None:
            return "There is no root"
        runner = self.root
        while runner != None:
            if runner.value == val:
                return "I found it"
            if val > runner.value:
                runner = runner.right
            else:
                runner = runner.left
        return "Did not find value in our tree"

# BST: Min
# Create a min() method on the BST class that returns the smallest value found in the BST.

    def min(self):
        runner = self.root
        min = self.root.value
        while runner.left:
            if runner.left.value < min:
                min = runner.left.value
            runner = runner.left
        return min

# BST: Max
# Create a max() BST method that returns the largest value contained in the binary search tree.

    def max(self):
        runner = self.root
        max = self.root.value
        while runner.right:
            if runner.right.value > max:
                max = runner.right.value
            runner = runner.right
        return max

# BONUS: BST: Size 
# Write a size() method that returns the number of nodes (values) contained in the tree.

    def size(self):
        if self.root == None:
            return 0
        def sizeHelp(runner):
            if (not runner):
                return 0
            return 1 + sizeHelp(runner.left) + sizeHelp(runner.right)
        return sizeHelp(self.root)

# BONUS: BST: Is Empty
# Create an isEmpty() method to return whether the BST is empty (whether it contains no values).

    def empty(self):
        if self.root == None:
            return "This tree is empty"
        else:
            return "This tree is not empty"




first_bst = BST()
first_bst.add(30).add(15).add(10).add(40).add(32).add(13)
print(first_bst.root.value)
print(first_bst.root.left.value)
print(first_bst.root.left.left.value)
print(first_bst.root.left.left.right.value)
print(first_bst.root.right.left.value)
print(first_bst.contains(13))
print(first_bst.contains(7))
print(first_bst.min())
print(first_bst.max())
print(first_bst.size())
print(first_bst.empty())
second_bst = BST()
print(second_bst.empty())