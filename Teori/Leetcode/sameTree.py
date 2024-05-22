class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # If both trees are empty, they are considered the same
    if not p and not q:
        return True
    
    # If only one tree is empty, they are not the same
    if not p or not q:
        return False
    
    # If the values of the current nodes are different, they are not the same
    if p.val != q.val:
        return False
    
    # Recursively check the left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
  # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  
"""Here's how the code works:

    We define a TreeNode class to represent each node in the binary tree.
    The isSameTree function takes two root nodes p and q as input.
    We first handle the base cases:
        If both p and q are None, it means both trees are empty, so we return True.
        If only one of p or q is None, it means the trees have different structures, so we return False.
    If the values of the current nodes p and q are different, we return False because the trees are not the same.
    If the values of the current nodes p and q are the same, we recursively check if their left and right subtrees are the same by calling isSameTree(p.left, q.left) and isSameTree(p.right, q.right).
    If both the left and right subtrees are the same, we return True. Otherwise, we return False.
    
    The time complexity of this code is O(n), where n is the number of nodes in the tree, as we visit each node once."""
    
    