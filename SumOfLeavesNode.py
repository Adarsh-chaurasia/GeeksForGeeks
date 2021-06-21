#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
def countLeaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
         return 1
    return countLeaves(root.left)+countLeaves(root.right)    
    
