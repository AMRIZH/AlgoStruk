# problem 203 : Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all nodes of the linked list that have Node.val == val, and return the new head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(head, val):
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize pointers for the current and previous nodes
    prev, curr = dummy, head
    
    # Traverse the linked list
    while curr:
        # If the current node's value matches val, remove it
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        
        # Move to the next node
        curr = curr.next
    
    return dummy.next
  
"""Here's how the algorithm works:

    We create a dummy node to handle edge cases where the head of the linked list needs to be removed.
    We initialize two pointers, prev and curr, to keep track of the current and previous nodes in the linked list.
    We traverse the linked list using the curr pointer.
    If the current node's value matches val, we remove it by updating the next pointer of the previous node.
    If the current node's value does not match val, we update the prev pointer to the current node.
    After processing all nodes, we return the next node of the dummy node, which is the new head of the linked list.
    
The time complexity of this algorithm is O(n), where n is the number of nodes in the linked list. The space complexity is O(1), as we are using a constant amount of extra space.
"""

# Test cases
# Test case 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(6)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(5)
head1.next.next.next.next.next.next = ListNode(6)
val1 = 6
result1 = removeElements(head1, val1)
while result1:
    print(result1.val, end=" ")
    result1 = result1.next
print()  # Output: 1 2 3 4 5

# Test case 2
head2 = ListNode(7)
head2.next = ListNode(7)
head2.next.next = ListNode(7)
val2 = 7
result2 = removeElements(head2, val2)
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
print()  # Output: None

# Test case 3
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(4)
head3.next.next.next.next = ListNode(5)
val3 = 6
result3 = removeElements(head3, val3)
while result3:
    print(result3.val, end=" ")
    result3 = result3.next
print()  # Output: 1 2 3 4 5
