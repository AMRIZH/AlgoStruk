# no 1a
def swap(lis,a,b) :
  temp = lis[a]
  lis[a] = lis[b]
  lis[b] = temp

def bubbleSort(A):
  n = len(A)-1
  for i in range(n):
      for j in range(n-i): 
          if A[j] > A[j+1]:
              swap(A,j,j+1) 
              
def findMedian(L):
  bubbleSort(L) # bisa diganti sorting lainnya
  n = len(L)
  mid = n//2
  if n % 2 == 0:
    return (L[mid]+L[mid-1])/2
  return L[mid]
A = [4,5,7,2,6]
print(findMedian(A))

# =============================================
# no 1b
def string_sort(A): # based on buble sort
  n = len(A)-1
  for i in range(n):
      for j in range(n-i): 
          if len(A[j]) > len(A[j+1]): # beda disini
              swap(A,j,j+1) 

B = ['apple','kiwi','mango','banana','pear','avocado']
string_sort(B)
print(B)

# ============================================
from math import inf
class minStack(object):
  def __init__(self):  
      self.items = []  # List untuk menyimpan stack.

  def isEmpty(self):  # Mengembalikan True kalau kosong,
      return len(self) == 0  
  
  def __len__(self):  # Mengembalikan banyaknya item di stack.
      return len(self.items)

  def pop(self):  # Mengembalikan nilai posisi atas lalu menghapus.
      assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
      return self.items.pop()

  def push(self, item):  # Mendorong item baru ke stack.
      self.items.append(item)
  
  def get_min(self):
    if len(self) == 0: # stack kososng
      return None
    return min(self.items)
  
  def get_min2(self):
    if len(self) == 0: # stack kososng
      return None
    minim = inf # infinity
    for i in self.items :
      if i < minim :
        minim = i
    return minim
  
  def get_min3(self) :
    if len(self) == 0: # stack kososng
      return None
    lis = []
    for i in self.items:
      lis.append(i)
    return min(lis)
  
  def get_min4(self): # tanpa iterasi langsung ke stack
    if len(self) == 0: # stack kososng
      return None
    lis = []
    for i in range(len(self)): # keluarin isi stack
      a = self.pop()
      lis.append(a) # catat data keluar
    for j in lis[::-1]: # masukin lagi ke stack
      self.push(j)
    return min(lis)
      
M = minStack()
M.push(5)
M.push(3)
print(M.get_min()) # output 3
M.push(2)
M.push(1)
print(M.get_min2()) # output 1
M.pop()
print(M.get_min3()) # output 2
M.pop()
print(M.get_min4()) # output 3