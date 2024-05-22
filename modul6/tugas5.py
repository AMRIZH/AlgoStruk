class Node:
    """This is a node object"""
    def __init__(self, data=None):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traversal(self):
        """Obtain a list of node data"""
        printval = self.head
        result = []
        while printval:
            result.append(printval.data)
            printval = printval.pointer
        return result[:]  # Return a copy of the list

    def reconstruct(self, sorted_list):
        """Update the data of existing nodes with the sorted list"""
        current = self.head
        for data in sorted_list:
            current.data = data
            current = current.pointer

    def printLinkedList(self):
        """Print all members of the linked list"""
        printval = self.head
        result = []
        while printval:
            result.append(printval.data)
            printval = printval.pointer
        print(result)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left_half = A[:mid]
    right_half = A[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def mrgSort(linklist):
    A = linklist.traversal()[:]
    sorted_list = merge_sort(A)
    linklist.reconstruct(sorted_list)

# Make initial Nodes & their pointers
a = Node(5)
b = Node(2)
c = Node(6)
d = Node(9)
e = Node(7)
f = Node(18)
g = Node(14)

a.pointer = b
b.pointer = c
c.pointer = d
d.pointer = e
e.pointer = f
f.pointer = g

linklist = LinkedList(a)  # Create a new linked list
mrgSort(linklist)
linklist.printLinkedList()