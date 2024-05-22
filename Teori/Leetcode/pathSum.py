# problem 112 : Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    def dfs(node, curr_sum): # helper function
        if not node: # base case
            return False

        curr_sum += node.val # add the value of the current node to the current sum

        # If the current node is a leaf and the current sum equals the target sum,
        # there is a root-to-leaf path with the target sum
        if not node.left and not node.right: 
            return curr_sum == targetSum 

        # Recursively check the left and right subtrees
        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    # Call the helper function with the root node and an initial sum of 0
    return dfs(root, 0)
  
"""Here's how the code works:

    We define a TreeNode class to represent each node in the binary tree.
    The hasPathSum function takes the root node of the binary tree and the targetSum as input.
    Inside hasPathSum, we define a helper function dfs that performs the depth-first search.
    The dfs function takes a node and the current sum (curr_sum) as input.
    In the dfs function, we first check if the current node is None. If it is, we return False because there is no path.
    We add the value of the current node to the curr_sum.
    If the current node is a leaf (i.e., both node.left and node.right are None), we check if the curr_sum equals the targetSum. If it does, we return True because we have found a root-to-leaf path with the target sum.
    If the current node is not a leaf, we recursively call dfs on the left and right subtrees with the updated curr_sum. If either of the recursive calls returns True, we return True because we have found a root-to-leaf path with the target sum.
    If none of the recursive calls returns True, we return False because no root-to-leaf path with the target sum exists.
    In the hasPathSum function, we call the dfs helper function with the root node and an initial sum of 0.
    We return the result of the dfs function, which indicates whether a root-to-leaf path with the target sum exists.
    
The time complexity of this solution is O(n), where n is the number of nodes in the binary tree. This is because we visit each node exactly once in the worst case.

The space complexity is O(h), where h is the height of the binary tree. This is because the recursion stack can potentially grow up to the height of the tree in the worst case (when the tree is skewed)."""

# test the function
# Example 1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
targetSum = 22
print(hasPathSum(root, targetSum))  # Output: True  (5 -> 4 -> 11 -> 2) 

# Example 2
root = TreeNode(1)
root.left = TreeNode(2)
targetSum = 1
print(hasPathSum(root, targetSum))  # Output: False

# Example 3
root = None
targetSum = 0
print(hasPathSum(root, targetSum))  # Output: False