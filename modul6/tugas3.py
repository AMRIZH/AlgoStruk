def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
        mergeSort(separuhKiri)  
        mergeSort(separuhKanan)
        
        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:  
                A[k] = separuhKiri[i]            
                i = i + 1                        
            else:                                
                A[k] = separuhKanan[j]           
                j = j + 1                       
            k = k + 1                            

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]    
            i = i + 1                
            k = k + 1                

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]   
            j = j + 1                
            k = k + 1                

#==========================================================    
def partisi(A, awal, akhir):
    nilaiPivot = A[awal]  

    penandaKiri = awal + 1  
    penandaKanan = akhir  

    selesai = False
    while not selesai:  
        while penandaKiri <= penandaKanan and \
                A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1  

        while A[penandaKanan] >= nilaiPivot and \
                penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1  

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            swap(A, penandaKiri, penandaKanan)
    swap(A, awal, penandaKanan)
    return penandaKanan  
  
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1 )  

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)  
        quickSortBantu(A, awal, titikBelah - 1)  
        quickSortBantu(A, titikBelah + 1, akhir)  

#=================================================
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