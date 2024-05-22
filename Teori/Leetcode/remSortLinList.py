#problem 83 : remove duplicates from sorted list
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def removeDuplicates(head: ListNode) -> ListNode:
    current = head # set the current node to the head of the list
    while current is not None and current.next is not None: # iterate through the list
        if current.val == current.next.val: # if the current node has the same value as the next node
            current.next = current.next.next # remove the next node
        else:
            current = current.next # move to the next node
    return head # return the head of the modified list
  
"""
Explanation:

    We start by setting the current node to the head of the list.
    We iterate through the list as long as the current node and the next node are not None.
    If the value of the current node is equal to the value of the next node, we remove the next node by setting the next pointer of the current node to the node after the next node.
    If the values are not equal, we move to the next node.
    Finally, we return the head of the modified list.
"""

# test the function
# create a linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

# improved code
def deleteDuplicates(self, head) -> ListNode:
    curr = head # set the current node to the head of the list
    while curr and curr.next: # iterate through the list
        if curr.val == curr.next.val: # if the current node has the same value as the next node
            curr.next = curr.next.next # remove the next node
        else: # move to the next node
            curr = curr.next 
    return head # return the head of the modified list
