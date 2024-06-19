from binSerchTre import Node, preorderTrav, inorderTrav, postorderTrav, leaves, internal_nodes, nodes_at_level, depth

# initiate nodes
A = Node(14)
B = Node(78)
C = Node(39)
D = Node(52)
E = Node(83)
F = Node(41)
G = Node(17)
H = Node(9)
I = Node(2)
J = Node(60)
K = Node(23)
L = Node(4)
M = Node(19)

# connecting Nodes
A.left = B; A.right = I
B.left = C; B.right = D
D.left = E; D.right = F
E.left = G; E.right = H
I.left = J; I.right = K
K.left = L; K.right = M

# print(preorderTrav(A))
# print(inorderTrav(A))
# print(postorderTrav(A))

# print(leaves(A))
# print(internal_nodes(A))
# print(nodes_at_level(A, 4))

print(depth(A,78))
print(depth(A,41))
print(depth(A,60))
print(depth(A,19))
