class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode()
    curr = dummy
    # Traverse both lists and merge them
    while list1 and list2: # selama list1 dan list2 tidak kosong
        if list1.val <= list2.val: # jika list1 <= list2
            curr.next = list1 # append list1 to the merged list
            list1 = list1.next # move to the next node in list1
        else: # jika list2 < list1
            curr.next = list2 # append list2 to the merged list
            list2 = list2.next # move to the next node in list2
        curr = curr.next # move the curr pointer to the next node
    # Append the remaining nodes of the non-empty list
    if list1: # jika list1 tidak kosong
        curr.next = list1 # append the remaining nodes of list1
    else: # jika list2 tidak kosong
        curr.next = list2 # append the remaining nodes of list2
    # Return the head of the merged list
    return dummy.next # return the head of the merged list
  
  
"""Here's how the code works:

    We define a ListNode class to represent each node in the linked list.
    The mergeTwoLists function takes two linked lists list1 and list2 as input.
    We create a dummy node dummy to serve as the head of the merged list. This is a common technique to simplify the merging process.
    We initialize a pointer curr to the dummy node.
    We use a while loop to traverse both list1 and list2 simultaneously.
        In each iteration, we compare the values of the current nodes in list1 and list2.
        If the value in list1 is smaller or equal, we append the node from list1 to the merged list by setting curr.next = list1, and we move to the next node in list1 by updating list1 = list1.next.
        If the value in list2 is smaller, we append the node from list2 to the merged list by setting curr.next = list2, and we move to the next node in list2 by updating list2 = list2.next.
        We then move the curr pointer to the next node in the merged list by updating curr = curr.next.
    After the while loop, one of the input lists may have remaining nodes. We append these remaining nodes to the end of the merged list by setting curr.next to the head of the non-empty list.
    Finally, we return the head of the merged list by returning dummy.next (since dummy itself is not part of the merged list).
    
This algorithm has a time complexity of O(n + m), where n and m are the lengths of list1 and list2, respectively. We traverse both lists once to merge them. The space complexity is O(1) because we only use a constant amount of extra space for the dummy node and pointers.
"""

# test case
# Example 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged = mergeTwoLists(list1, list2)
# Output: [1, 1, 2, 3, 4, 4]

# Example 2
list1 = None
list2 = None
merged = mergeTwoLists(list1, list2)
# Output: []

# Example 3
list1 = None
list2 = ListNode(0)
merged = mergeTwoLists(list1, list2)
# Output: [0]