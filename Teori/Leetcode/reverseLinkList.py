# problem 206 : Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize the previous node to None
        prev = None
        
        # Set the current node to the head of the linked list
        curr = head
        
        # Reverse the linked list
        while curr:
            # Store the next node
            next_node = curr.next
            
            # Reverse the current node
            curr.next = prev
            
            # Move the pointers one position ahead
            prev = curr
            curr = next_node
        
        # Return the new head of the reversed linked list
        return prev
      
"""Here's how the algorithm works:

    We initialize two pointers, prev and curr, to keep track of the previous and current nodes in the linked list.
    We reverse the linked list by iterating through the nodes and updating the next pointers.
    For each node, we store the next node, reverse the current node by updating its next pointer to the previous node, and move the pointers one position ahead.
    After processing all nodes, the prev pointer will be pointing to the new head of the reversed linked list.
    
The time complexity of this algorithm is O(n), where n is the number of nodes in the linked list. The space complexity is O(1), as we are using a constant amount of extra space.
"""

# Test cases
# Test case 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
result1 = Solution().reverseList(head1)
while result1:
    print(result1.val, end=" ")
    result1 = result1.next
print()  # Output: 5 4 3 2 1

# Test case 2
head2 = ListNode(1)
result2 = Solution().reverseList(head2)
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
print()  # Output: 1

# Test case 3
head3 = None
result3 = Solution().reverseList(head3)
print(result3)  # Output: None
