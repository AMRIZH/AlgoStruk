# linked list, NO 5
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
  
  def binerSearch(self,data) :
    dataset = []
    printval = self.head
    while printval is not None:
      dataset.append(printval.data)
      printval = printval.pointer
    
    low = 0
    high = len(dataset) - 1
    while low <= high:
    # Temukan pertengahan runtut itu
      mid = (high + low) // 2
      # Apakah pertengahannya memuat target?
      if dataset[mid] == data:
          return mid # True
      # ataukah targetnya di sebelah kirinya?
      elif data < dataset[mid]:
          high = mid - 1
      # ataukah targetnya di sebelah kanannya?
      else:
          low = mid + 1
   # Jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return -1 # false
  
  
# make initial Nodes & their pointers
a = Node(1)
b = Node(2)
c = Node(6)
d = Node(9)
e = Node(12)
f = Node(15)
a.pointer = b
b.pointer = c
c.pointer = d
d.pointer = e
e.pointer = f

linlis = LinkList(a) #create a new linlist
print("Terdapat pada indeks ke", linlis.search(9))

# if linlis.binerSearch(4) : print("Data ada di linlis") 
# else : print("data tidak ditemukan")

print(linlis.binerSearch(9))

print(linlis.search(15))