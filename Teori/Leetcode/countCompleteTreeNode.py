# problem 222 : Count Complete Tree Nodes
# Given the root of a complete binary tree, return the number of the nodes in the tree.

# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def countNodes(root):
    """
    Counts the number of nodes in a complete binary tree.
    """
    # Base case: empty tree
    if not root:
        return 0
    
    # Calculate the height of the left and right subtrees
    left_height = 0
    right_height = 0
    left_node = root
    right_node = root
    while left_node:
        left_height += 1
        left_node = left_node.left
    while right_node:
        right_height += 1
        right_node = right_node.right
    
    # If the height of the left and right subtrees is the same, the tree is full
    if left_height == right_height:
        return 2 ** left_height - 1
    
    # Otherwise, recursively count the nodes in the left and right subtrees
    return 1 + countNodes(root.left) + countNodes(root.right)
  
"""Here's how the algorithm works:

    If the tree is empty (root is None), we return 0.
    We calculate the height of the left and right subtrees by traversing the left and right child nodes.
    If the height of the left and right subtrees is the same, the tree is full, and we return the total number of nodes using the formula 2^height - 1.
    If the tree is not full, we recursively count the nodes in the left and right subtrees and add 1 for the current node.
    
The time complexity of this algorithm is O(log n * log n), where n is the number of nodes in the tree. The space complexity is O(log n), where log n is the height of the tree, due to the recursive calls on the left and right subtrees.
"""

# Test cases
# Test case 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
assert countNodes(root1) == 6

# Test case 2
root2 = TreeNode(1)
assert countNodes(root2) == 1

# Test case 3
root3 = None
assert countNodes(root3) == 0

# The first test case creates a complete binary tree with 6 nodes, and the expected output is 6.

# The second test case creates a complete binary tree with 1 node, and the expected output is 1.

# The third test case creates an empty tree, and the expected output is 0.