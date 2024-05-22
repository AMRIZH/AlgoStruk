# from modul1.tugas1 import isPrime

A = [ [2,3], [5,7] ]
print(A[0][1])
print(A[1][1])

B = [ [0 for j in range(3)] for i in range(3) ]
print(B)

# Membuat list kuadrat bilangan dari 0 sampai 6
C =  [x**2 for x in range(0,7)] #[0, 1, 4, 9, 16, 25, 36]

# Membuat list yang berisi tuple pasangan bilangan dan kuadratnya, dari 0 sampai 6
D =  [(x,x**2) for x in range(7)] #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]

# Membuat list kuadrat bilangan genap antara 0 dan 15
E = [x**2 for x in range(15) if x%2==0] #[0, 4, 16, 36, 64, 100, 144, 196]

# Membuat list sepanjang 5 elemen yang berisi bilangan 3
F =[3 for i in range(5)] #[3, 3, 3, 3, 3]

# Membuat list sepanjang tiga elemen yang berisi list sepanjang 3 elemen angka 0
G =[ [0 for j in range(3)] for i in range(3) ] #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Membuat matrix identitas 3 × 3
H =[ [ 1 if j==i else 0 for j in range(3) ] for i in range(3) ] #[[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Membuat list yang berisi huruf vokal suatu string
d = "Yogyakarta dan Surakarta."
I = [x for x in d if x in "aiueoAIUEO"]  #['o', 'a', 'a', 'a', 'a', 'u', 'a', 'a', 'a']

# Membuat list bilangan primaa dari 20 sampai 50
# J = [x for x in range(20,50) if isPrime(x)]  #[23, 29, 31, 37, 41, 43, 47]


def cariLurus( wadah, target ):
  n = len( wadah )
  for i in range( n ):
    if wadah[i] == target:
      return True
  return False

class Node(object):
  """Sebuah simpul di linked list"""
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

a = Node(11)
b = Node(52)
c = Node(18)
a.next = b
b.next = c
print(a.data) #11
print(a.next.data) #52
print(a.next.next.data) #18

def kunjungi( head ):
  curNode = head
  while curNode is not None :
    print(curNode.data)
    curNode = curNode.next

class DNode(object) :
  def __init__( self, data ):
    self.data = data
    self.next = None
    self.prev = None
    