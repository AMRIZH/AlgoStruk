class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# Membuat simpul-simpul dan mengisi data
A = Node(56)
B = Node(37)
C = Node(78)
D = Node(22)
E = Node(43)
F = Node(60)
G = Node(83)
H = Node(40)
I = Node(85)

# Menghubungkan simpul ortu-anak
A.left = B; A.right = C
B.left = D; B.right = E
C.left = F; C.right = G
E.left = H
G.right = I

# preorder traversal
def preorderTrav(root):
  result = []
  if root is not None:
    result.append(root.data)
    result.extend(preorderTrav(root.left))
    result.extend(preorderTrav(root.right))
  return result

# inorder traversal
def inorderTrav(root):
  result = []
  if root is not None:
    result.extend(inorderTrav(root.left))
    result.append(root.data)
    result.extend(inorderTrav(root.right))
  return result

# postorder traversal
def postorderTrav(root):
  result = []
  if root is not None:
    result.extend(postorderTrav(root.left))
    result.extend(postorderTrav(root.right))
    result.append(root.data)
  return result

# # testcases
# print(preorderTrav(A))  # output [56, 37, 22, 43, 40, 78, 60, 83, 85]
# print(inorderTrav(A))   # output [22, 37, 40, 43, 56, 60, 78, 83, 85]
# print(postorderTrav(A)) # output [22, 40, 43, 37, 60, 85, 83, 78, 56]


# Inserting a new node
def insert(root, data): # insert a new node into a binary tree
  if root is None:
    return Node(data)
  if data < root.data:
    root.left = insert(root.left, data)
  else:
    root.right = insert(root.right, data)
  return root

# Deleting an existing node
def delete(root, data): # delete a node from a binary tree
  if root is None:
    return root
  if data < root.data:
    root.left = delete(root.left, data)
  elif data > root.data:
    root.right = delete(root.right, data)
  else:
    if root.left is None:
      return root.right
    elif root.right is None:
      return root.left
    temp = min_value_node(root.right)
    root.data = temp.data
    root.right = delete(root.right, temp.data)
  return root

# minimum value node
def min_value_node(node): # find the node with the minimum value in a binary tree
  current = node
  while current.left is not None:
    current = current.left
  return current

# maximum value node
def max_value_node(node): # find the node with the maximum value in a binary tree
  current = node
  while current.right is not None:
    current = current.right
  return current

# Tree size
def size(node): # determine the number of nodes in a binary tree
  if node is None:
    return 0
  return 1 + size(node.left) + size(node.right)

# Tree height
def height(node): # determine the height of a binary tree
  if node is None:
    return -1
  return 1 + max(height(node.left), height(node.right))

# Tree width
def width(root): # determine the maximum width of a binary tree
  if root is None:
    return 0
  max_width = 0
  q = [root]
  while q:
    count = len(q)
    max_width = max(max_width, count)
    for _ in range(count):
      node = q.pop(0)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
  return max_width

# Leaf nodes
def leaves(node): # determine which nodes are leaves
  leaf_nodes = []
  if node is not None:
    if node.left is None and node.right is None:
      leaf_nodes.append(node.data)
    else:
      leaf_nodes.extend(leaves(node.left))
      leaf_nodes.extend(leaves(node.right))
  return leaf_nodes

# Internal nodes
def internal_nodes(node): # determine which nodes are internal nodes
  internals = []
  if node is not None:
    if node.left is not None or node.right is not None:
      internals.append(node.data)
      internals.extend(internal_nodes(node.left))
      internals.extend(internal_nodes(node.right))
  return internals

# Node depth
def depth(root, node_data, current_depth=0): # determine the depth of a specific node
  if root is None:
    return -1
  if root.data == node_data:
    return current_depth
  if node_data < root.data:
    return depth(root.left, node_data, current_depth + 1)
  else:
    return depth(root.right, node_data, current_depth + 1)

# Nodes at specific level
def nodes_at_level(root, level): # determine which nodes are at a specific level
  result = []
  nodes_at_level_helper(root, level, 0, result)
  return result

def nodes_at_level_helper(node, level, current_level, result):
  """Helper function to find nodes at a specific level in a binary tree."""
  if node is None:
    return
  if current_level == level:
    result.append(node.data)
  else:
    nodes_at_level_helper(node.left, level, current_level + 1, result)
    nodes_at_level_helper(node.right, level, current_level + 1, result)

# # Example usage
# root = A
# # Inserting nodes
# root = insert(root, 56)
# root = insert(root, 37)
# root = insert(root, 78)
# root = insert(root, 22)
# root = insert(root, 43)
# root = insert(root, 60)
# root = insert(root, 83)
# root = insert(root, 40)
# root = insert(root, 85)

# # Define the tree size
# print("Tree size:", size(root))

# # Define the tree height
# print("Tree height:", height(root))

# # Define the tree width
# print("Tree width:", width(root))

# # Define which nodes are leaves
# print("Leaf nodes:", leaves(root))

# # Define which nodes are internal nodes
# print("Internal nodes:", internal_nodes(root))

# # Define the depth of a specific node
# print("Depth of node 43:", depth(root, 43))

# # Define which nodes are in a specific level
# print("Nodes at level 2:", nodes_at_level(root, 2))

# # Insert a new node
# root = insert(root, 50)
# print("Tree size after inserting 50:", size(root))

# # Delete an existing node
# root = delete(root, 37)
# print("Tree size after deleting 37:", size(root))

# # check all nodes
# print(preorderTrav(A))  # output [56, 37, 22, 22, 43, 40, 40, 43, 50, 78, 60, 56, 60, 83, 78, 85, 83, 85]