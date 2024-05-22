# problem 111 : Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode) -> int:
    if not root: # base case
        return 0
    
    if not root.left: # if the left child is None
        return minDepth(root.right) + 1 # return the minimum depth of the right subtree plus 1
    
    if not root.right: # if the right child is None
        return minDepth(root.left) + 1 # return the minimum depth of the left subtree plus 1
    
    return min(minDepth(root.left), minDepth(root.right)) + 1 # return the minimum of the depths of the left and right subtrees, plus 1
  
"""Here's how the code works:

    We define a TreeNode class to represent each node in the binary tree.
    The minDepth function takes the root node of the binary tree as input.
    We handle the base case first: if the root is None (empty tree), we return 0.
    If the root node has no left child, we recursively calculate the minimum depth of the right subtree and return minDepth(root.right) + 1.
    If the root node has no right child, we recursively calculate the minimum depth of the left subtree and return minDepth(root.left) + 1.
    If the root node has both left and right children, we recursively calculate the minimum depth of both subtrees and return the minimum of the two, plus 1 (for the root node itself).
    
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
print(minDepth(root))  # Output: 2

# Example 2
root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print(minDepth(root))  # Output: 5



