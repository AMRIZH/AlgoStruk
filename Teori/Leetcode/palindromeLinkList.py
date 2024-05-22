# problem 234 : Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def isPalindrome(head):
    # Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    
    # Compare the first and second halves of the linked list
    while prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    
    return True

"""Here's how the algorithm works:

    We find the middle of the linked list using the slow and fast pointers.
    We reverse the second half of the linked list.
    We compare the first and second halves of the linked list to check if it is a palindrome.
    
    The time complexity of this algorithm is O(n), where n is the number of nodes in the linked list. The space complexity is O(1), as we are using a constant amount of extra space."""
    
# Test cases
# Test case 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)
assert isPalindrome(head1)

# Test case 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
assert not isPalindrome(head2)
# Output: True
# Output: False
# The first test case is a palindrome, as the linked list is [1, 2, 2, 1]. The second test case is not a palindrome, as the linked list is [1, 2, 3].
