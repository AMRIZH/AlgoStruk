# problem 234 Palindrome Linked List
# given a singly linked list, determine if it is a palindrome.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
  # create a list called vals
  vals = []
  # create a variable called current_node and assign it to head
  current_node = head
  # iterate through the linked list
  while current_node is not None:
    # append the value of current_node to the vals list
    vals.append(current_node.val)
    # move the current_node to the next node
    current_node = current_node.next
  # check if the list is a palindrome
  return vals == vals[::-1]
  
  # description:
  # 1. create a list called vals
  # 2. create a variable called current_node and assign it to head
  # 3. create a while loop that will run as long as current_node is not None
  # 4. append the value of current_node to the vals list
  # 5. move the current_node to the next node
  # 6. return True if vals is equal to vals[::-1] else return False
  # 7. end
  
  # Time complexity: O(n)
  # space complexity: O(n)
  
# # testcases
# ln1 = ListNode(1)
# ln2 = ListNode(2)
# ln3 = ListNode(2)
# ln4 = ListNode(1)
# ln1.next = ln2
# ln2.next = ln3
# ln3.next = ln4
# print(isPalindrome(ln1)) # True

# ln5 = ListNode(1)
# ln6 = ListNode(2)
# ln5.next = ln6
# print(isPalindrome(ln5)) # False
# ========================================================================================================
# problem 104 Maximum Depth of Binary Tree
# given a binary tree, find its maximum depth.
# the maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepth(root: TreeNode) -> int:
  # check if the root is None
  if root is None:
    # return 0
    return 0
  # create a variable called left and assign it to maxDepth(root.left)
  left = maxDepth(root.left)
  # create a variable called right and assign it to maxDepth(root.right)
  right = maxDepth(root.right)
  # return the maximum of left and right plus 1
  return max(left, right) + 1

  # description:
  # 1. check if the root is None
  # 2. create a variable called left and assign it to maxDepth(root.left)
  # 3. create a variable called right and assign it to maxDepth(root.right)
  # 4. return the maximum of left and right plus 1
  # 5. end

  # Time complexity: O(n)
  # space complexity: O(n)
  
# testcases
tn1 = TreeNode(3)
tn2 = TreeNode(9)
tn3 = TreeNode(20)
tn4 = TreeNode(15)
tn5 = TreeNode(7)
tn1.left = tn2
tn1.right = tn3
tn3.left = tn4
tn3.right = tn5
print(maxDepth(tn1)) # 3

tn6 = TreeNode(1)
tn7 = TreeNode(2)
tn6.right = tn7
print(maxDepth(tn6)) # 2