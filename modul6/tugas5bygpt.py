class Node(object):
    """This is a node object"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    mid_next = mid.next
    mid.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(mid_next)

    return merge(left, right)

def get_middle(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data < right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result

def quicksort_linked_list(head):
    if not head or not head.next:
        return head

    pivot = head.data
    less_than_pivot = Node()
    equal_to_pivot = Node()
    greater_than_pivot = Node()

    current = head
    while current:
        if current.data < pivot:
            less_than_pivot.append(current.data)
        elif current.data == pivot:
            equal_to_pivot.append(current.data)
        else:
            greater_than_pivot.append(current.data)
        current = current.next

    sorted_less = quicksort_linked_list(less_than_pivot.next)
    sorted_greater = quicksort_linked_list(greater_than_pivot.next)

    return concatenate(sorted_less, equal_to_pivot, sorted_greater)

def concatenate(less, equal, greater):
    result = less
    while less and less.next:
        less = less.next
    less.next = equal
    while equal and equal.next:
        equal = equal.next
    equal.next = greater
    return result


    def swap(self, node1_data, node2_data):
        if not self.head or not self.head.next:
            return

        prev_node1 = None
        prev_node2 = None
        current = self.head

        # Find previous nodes of node1 and node2
        while current:
            if current.next and current.next.data == node1_data:
                prev_node1 = current
            if current.next and current.next.data == node2_data:
                prev_node2 = current
            current = current.next

        # Check if either node1 or node2 is not found
        if not prev_node1 or not prev_node2:
            print("One or both of the nodes not found.")
            return

        node1 = prev_node1.next
        node2 = prev_node2.next

        # If node2 comes before node1, swap the assignments
        if prev_node1.next.data > prev_node2.next.data:
            node1, node2 = node2, node1
            prev_node1, prev_node2 = prev_node2, prev_node1

        # Perform the swap
        prev_node1.next = node2
        prev_node2.next = node1
        temp = node2.next
        node2.next = node1.next
        node1.next = temp

# Test merge sort for linked list
print("Merge sort for linked list:")
a = Node(5)
b = Node(2)
c = Node(6)
d = Node(9)
a.next = b
b.next = c
c.next = d
ll = LinkedList(a)
print("Before sorting:")
ll.display()
ll.head = merge_sort_linked_list(ll.head)
print("After sorting:")
ll.display()

# Test quicksort for linked list
print("\nQuicksort for linked list:")
a = Node(5)
b = Node(2)
c = Node(6)
d = Node(9)
a.next = b
b.next = c
c.next = d
ll = LinkedList(a)
print("Before sorting:")
ll.display()
ll.head = quicksort_linked_list(ll.head)
print("After sorting:")
ll.display()
