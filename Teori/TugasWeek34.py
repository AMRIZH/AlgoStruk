string = "I love to learn python"
def longest(string):
  k = 0
  long = ""
  pisah = string.split()
  for i in pisah :
    if len(i) > k :
      k = len(i)
      long = i
  print ("the longest word is",long)
  
longest(string)

#===============================
angka = [1,2,3,4,5,6,8,9,10]
def missing3(angka):
  return 55 - sum(angka) 
print(missing3(angka))

#=================================
# linked list

class Node(object):
  """This is a node"""
  def __init__(self, data=None):
    self.data = data
    self.pointer = None
    
class LinkList(object):
  def __init__(self) :
    self.head = None

a = Node()
b = Node()
c = Node()
a.pointer = b
b.pointer = c