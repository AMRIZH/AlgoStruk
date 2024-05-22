# problem 160 : Intersection of Two Linked Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # If either list is empty, there is no intersection
        if not headA or not headB:
            return None

        # Initialize pointers for both lists
        ptrA, ptrB = headA, headB

        # Find the lengths of both lists
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next

        # Move the pointer of the longer list ahead by the difference
        if lenA > lenB:
            for _ in range(lenA - lenB):
                ptrA = ptrA.next
        else:
            for _ in range(lenB - lenA):
                ptrB = ptrB.next

        # Move both pointers simultaneously until they meet or reach the end
        while ptrA and ptrB:
            if ptrA == ptrB:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next

        # If the pointers meet, they will be at the intersection node
        # If they reach the end, they will be None
        return None
      
"""Here's how the algorithm works:

    If either of the input linked lists is empty, there is no intersection, so we return None.
    We initialize two pointers, ptrA and ptrB, to the heads of the input linked lists.
    We find the lengths of both linked lists by traversing them.
    We move the pointer of the longer linked list ahead by the difference in lengths.
    We move both pointers simultaneously until they meet or reach the end of the linked lists.
    If the pointers meet, they are at the intersection node, so we return the node.
    If the pointers reach the end of the linked lists, there is no intersection, so we return None.
    
The time complexity of this algorithm is O(m + n), where m and n are the lengths of the input linked lists. The space complexity is O(1), as we are only using a constant amount of extra space.
"""

# Test case 1: No intersection
headA1 = ListNode(4)
headA1.next = ListNode(1)
headA1.next.next = ListNode(8)
headA1.next.next.next = ListNode(4)
headA1.next.next.next.next = ListNode(5)

headB1 = ListNode(5)
headB1.next = ListNode(6)
headB1.next.next = ListNode(1)
headB1.next.next.next = ListNode(8)
headB1.next.next.next.next = ListNode(4)
headB1.next.next.next.next.next = ListNode(5)

assert Solution().getIntersectionNode(headA1, headB1) == None

# Test case 2: Intersection at the first node
headA2 = ListNode(1)
headA2.next = ListNode(9)
headA2.next.next = ListNode(1)
headA2.next.next.next = ListNode(2)
headA2.next.next.next.next = ListNode(4)

headB2 = ListNode(3)
headB2.next = headA2.next.next

assert Solution().getIntersectionNode(headA2, headB2) == headA2.next.next

# Test case 3: Intersection at the last node
headA3 = ListNode(2)
headA3.next = ListNode(6)
headA3.next.next = ListNode(4)

headB3 = ListNode(1)
headB3.next = ListNode(5)

headB3.next.next = headA3.next  # Intersection at the last node

assert Solution().getIntersectionNode(headA3, headB3) == headA3.next

# Test case 4: Intersection at a middle node
headA4 = ListNode(1)
headA4.next = ListNode(2)
headA4.next.next = ListNode(3)
headA4.next.next.next = ListNode(4)
headA4.next.next.next.next = ListNode(5)

headB4 = ListNode(6)
headB4.next = ListNode(7)
headB4.next.next = headA4.next.next  # Intersection at a middle node

assert Solution().getIntersectionNode(headA4, headB4) == headA4.next.next

