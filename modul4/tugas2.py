# linked list
class Node(object):
  """This is a node object"""
  def __init__(self, data=None):
    self.data = data
    self.pointer = None

class LinkList(object):
  def __init__(self,head) : # define head of new linlis
    self.head = head
    
  def search(self,data):
    position = 0
    current_node = self.head
    while current_node is not None:
        if current_node.data == data:
            return position
        current_node = current_node.pointer
        position += 1
    return -1  # data not found in the linked list
  
# make initial Nodes & their pointers
a = Node(5)
b = Node(2)
c = Node(6)
d = Node(9)
a.pointer = b
b.pointer = c
c.pointer = d

linlis = LinkList(a) #create a new linlist