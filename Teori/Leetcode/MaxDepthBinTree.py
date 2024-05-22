# problem 104 : Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root: # base case
        return 0
    
    left_depth = maxDepth(root.left) # calculate the maximum depth of the left subtree
    right_depth = maxDepth(root.right) # calculate the maximum depth of the right subtree
    
    return max(left_depth, right_depth) + 1 # return the maximum depth of the current tree
  
"""Here's how the code works:

    We define a TreeNode class to represent each node in the binary tree.
    The maxDepth function takes the root node of the binary tree as input.
    We handle the base case first: if the root is None (empty tree), we return 0.
    We recursively calculate the maximum depth of the left and right subtrees by calling maxDepth on root.left and root.right, respectively.
    The maximum depth of the current tree is the maximum of the depths of the left and right subtrees, plus 1 (for the root node itself).
    We return the calculated maximum depth.

The time complexity of this solution is O(n), where n is the number of nodes in the binary tree. This is because we visit each node exactly once in the worst case.

The space complexity is O(h), where h is the height of the binary tree. This is because the recursion stack can potentially grow up to the height of the tree in the worst case (when the tree is skewed).
"""
# test the function
# Example 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxDepth(root))  # Output: 3

# Example 2
root = TreeNode(1)
root.right = TreeNode(2)
print(maxDepth(root))  # Output: 2