# problem 141 : Linked List Cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head) -> bool:
        # If the linked list is empty or has only one node, there is no cycle
        if not head or not head.next: 
            return False
        
        # Initialize the slow and fast pointers
        slow = head
        fast = head.next
        
        # Move the pointers until they meet or the fast pointer reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If the pointers meet, there is a cycle
            if slow == fast:
                return True
        
        # If the loop terminates, there is no cycle
        return False
      
"""Here's how the algorithm works:

    If the linked list is empty or has only one node, there is no cycle, so we return False.
    We initialize two pointers, slow and fast, both pointing to the head of the linked list.
    We move the slow pointer one step at a time, and the fast pointer two steps at a time.
    If there is a cycle in the linked list, the slow and fast pointers will eventually meet at some node in the cycle.
    If the fast pointer reaches the end of the linked list (i.e., fast or fast.next becomes None), there is no cycle, and we return False.

The time complexity of this algorithm is O(n), where n is the number of nodes in the linked list, because in the worst case (when there is no cycle), the fast pointer will traverse the entire linked list once. The space complexity is O(1), as we are only using two pointer variables, slow and fast.
"""

# test case
# Test case 1: Linked list with no cycle
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
assert not Solution().hasCycle(head1)

# Test case 2: Linked list with cycle at position 0
head2 = ListNode(1)
head2.next = head2
assert Solution().hasCycle(head2)

# Test case 3: Linked list with cycle at position 1
head3 = ListNode(3)
head3.next = ListNode(2)
head3.next.next = ListNode(0)
head3.next.next.next = ListNode(-4)
head3.next.next.next.next = head3.next
assert Solution().hasCycle(head3)

# Test case 4: Linked list with cycle at the last node
head4 = ListNode(1)
head4.next = ListNode(2)
head4.next.next = ListNode(3)
head4.next.next.next = ListNode(4)
head4.next.next.next.next = ListNode(5)
head4.next.next.next.next.next = head4.next.next
assert Solution().hasCycle(head4)

# Test case 5: Empty linked list
head5 = None
assert not Solution().hasCycle(head5)

# Test case 6: Linked list with a single node (no cycle)
head6 = ListNode(1)
assert not Solution().hasCycle(head6)