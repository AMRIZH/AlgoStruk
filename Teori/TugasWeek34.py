
def longest(string):
  k = 0 # data holder for longest length string
  long = "" # string with longest length
  pisah = string.split() # split the string into list of strings
  for i in pisah : 
    if len(i) > k : # choose the longest length string
      k = len(i) # the longest length string stored in the data holder
      long = i
  print ("the longest word is",long) # print the longest length string
  
string = "I love to learn python"
# longest(string)

#===============================

def missing(angka):
  return 55 - sum(angka) # the sum of 1,2,...,10 is 55.

angka = [1,2,3,4,5,6,8,9,10]
# print(missing(angka)) # result is 55 - sum of the miising list

#=================================
# linked list

class Node(object):
  """This is a node object"""
  def __init__(self, data=None):
    self.data = data
    self.pointer = None
    
class LinkList(object):
  def __init__(self,head) : # define head of new linlis
    self.head = head 
    
  def PrintLinkedList(self): # print all members of linked list
    printval = self.head
    while printval is not None:
      print (printval.data)
      printval = printval.pointer
      
  def AtBegining(self,newdata): # insert new node atBegining
    NewNode = Node(newdata)
    NewNode.pointer = self.head
    self.head = NewNode
    
  def AtEnd(self, newdata): # insert new node atEnd
    NewNode = Node(newdata)
    laste = self.head
    while(laste.pointer != None):
      laste = laste.pointer
    laste.pointer=NewNode
      
  def Inbetween(self,middle_node,newdata): # insert new node in middle
    NewNode = Node(newdata)
    NewNode.pointer = middle_node.pointer
    middle_node.pointer = NewNode
    
  def RemoveNode(self, Removekey): # remove node
    HeadVal = self.head
    if (HeadVal is not None):
      if (HeadVal.data == Removekey):
        self.head = HeadVal.pointer
        HeadVal = None
        return
    while (HeadVal is not None):
      if HeadVal.data == Removekey:
        break
      prev = HeadVal
      HeadVal = HeadVal.pointer
    if (HeadVal == None):
      return
    prev.pointer = HeadVal.pointer
    HeadVal = None
  
  def sumList(self): # sum all members of linked list
    k = 0
    printval = self.head
    while printval is not None:
      k+= printval.data
      printval = printval.pointer
    print(k)

# make initial Nodes & their pointers
a = Node(5)
b = Node(2)
c = Node(6)
d = Node(9)
a.pointer = b
b.pointer = c
c.pointer = d

linlis = LinkList(a) #create a new linlist
linlis.PrintLinkedList() #print the linlist traversing
print("===========================")
linlis.AtBegining(3) #insert at beginning
linlis.PrintLinkedList()
print("===========================")
linlis.AtEnd(7) #insert at end of list
linlis.PrintLinkedList()
print("===========================")
linlis.Inbetween(b,50) # insert Node after b node
linlis.PrintLinkedList()
print("===========================")
linlis.RemoveNode(50) # remove node with data 50
linlis.PrintLinkedList()
print("==========================")
linlis.sumList() # sum of all nodes in list 3+5+2+6+9+7 = 32


