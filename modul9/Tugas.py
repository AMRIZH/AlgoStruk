import math

# maksimum level pohon biner
def maxLevel(treeSize):
  if treeSize <= 0:
      return 0
  return treeSize - 1
  
# minimum level pohon biner
def minLevel(treeSize):
  if treeSize <= 0:
      return 0
  return math.floor(math.log2(treeSize))

# maksimum dan minimum jumlah simpul pada pohon biner dengan level tertentu
def maxNodes(height):
  if height < 0:
    return 0
  return (2 ** (height + 1)) - 1

def minNodes(height):
  if height < 0:
    return 0
  return height + 1

# Contoh penggunaan
print([minLevel(10),maxLevel(10)])
print([minLevel(35),maxLevel(35)])
print([minLevel(76),maxLevel(76)])  
print([minLevel(345),maxLevel(345)])  
print([minLevel(1),maxLevel(1)])
print([minLevel(2),maxLevel(2)])
print([minLevel(3),maxLevel(3)])
print([minLevel(4),maxLevel(4)])
print([minLevel(5),maxLevel(5)])
#=================================================================

def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient C(n, k), which is the number of ways to choose k elements from a set of n elements.
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

def count_binary_tree_shapes(n):
    """
    Determine the number of distinct binary tree shapes that can be formed with n nodes.
    """
    if n < 0:
        return 0
    catalan_number = binomial_coefficient(2 * n, n) // (n + 1)
    return catalan_number

# Example usage
n = 5
print("Number of distinct binary tree shapes with", n, "nodes:", count_binary_tree_shapes(n))

