# problem 1080 Insufficient Nodes in Root to Leaf Paths
# given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf. a leaf is a node with no children.
# a node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
  # check if the root is None
  if root is None:
    # return None
    return None
  # check if the root is a leaf
  if root.left is None and root.right is None:
    # return None if the value of root is less than limit else return root
    return None if root.val < limit else root
  # create a variable called left and assign it to sufficientSubset(root.left, limit - root.val)
  left = self.sufficientSubset(root.left, limit - root.val)
  # create a variable called right and assign it to sufficientSubset(root.right, limit - root.val)
  right = self.sufficientSubset(root.right, limit - root.val)
  # check if left is None and right is None
  if left is None and right is None:
    # return None
    return None
  # set the left child of root to left
  root.left = left
  # set the right child of root to right
  root.right = right
  # return root
  return root

  # description:
  # 1. check if the root is None
  # 2. check if the root is a leaf
  # 3. create a variable called left and assign it to sufficientSubset(root.left, limit - root.val)
  # 4. create a variable called right and assign it to sufficientSubset(root.right, limit - root.val)
  # 5. check if left is None and right is None
  # 6. set the left child of root to left
  # 7. set the right child of root to right
  # 8. return root
  # 9. end

  # Time complexity: O(n)
  # space complexity: O(n)