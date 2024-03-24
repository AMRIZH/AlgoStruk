import timeit

def jumlahkanCara1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya
  
def jumlahkanCara2(n):
  return ( n*(n + 1) )/2


def insertionSort(A):
  n = len(A)
  for i in range(1, n):
      nilai = A[i]
      pos = i
      while pos > 0 and nilai < A[pos - 1]:  # Find the correct position
          A[pos] = A[pos - 1]
          pos = pos - 1  # Shift larger values to the right
      A[pos] = nilai  # Insert the value at the correct position
      
#===============================
# no 1a
stmt = "jumlahkanCara1(10000)"  # Statement to be timed
setup = "from __main__ import jumlahkanCara1"  # Setup code

for i in range(5):  # Repeat 5 times
    timer = timeit.timeit(stmt, setup, number=1)  # Time the statement
    h = jumlahkanCara1(10000)  # Calculate the sum
    print(f"Jumlah adalah {h}, memerlukan {timer:.8f} detik")
    
#===============================
# no 1b
stmt = "jumlahkanCara2(10000)"  # Statement to be timed
setup = "from __main__ import jumlahkanCara2"  # Setup code

for i in range(5):  # Repeat 5 times
    timer = timeit.timeit(stmt, setup, number=1)  # Time the statement
    h = jumlahkanCara2(10000)  # Calculate the sum
    print(f"Jumlah adalah {h}, memerlukan {timer:.8f} detik")
    
print("---------------------------\n")
#===============================
# no 1c
# Setup code for timeit
setup_code = """
import random
from __main__ import insertionSort

def generate_list(n):
    L = list(range(n))
    random.shuffle(L)
    return L

def generate_reversed_list(n):
    L = list(range(n))
    L.reverse()
    return L
"""

# Timing for randomly shuffled list
print("Timing for randomly shuffled list:")
stmt = "insertionSort(generate_list(3000))"
for _ in range(5):
    timer = timeit.timeit(stmt, setup_code, number=1)
    print(f"Sorting 3000 numbers, took {timer:.7f} seconds")

# Timing for reversed list
print("\nTiming for reversed list:")
stmt = "insertionSort(generate_reversed_list(3000))"
for _ in range(5):
    timer = timeit.timeit(stmt, setup_code, number=1)
    print(f"Sorting 3000 numbers, took {timer:.7f} seconds")
    
print("---------------------------\n")
#===============================================================
# no 2
# in
stmt = "sorted(generate_list(3000))"
setup_code = """import random
def generate_list(n):
  L = list(range(n))
  random.shuffle(L)
  return L"""
for _ in range(5):
  timer = timeit.timeit(stmt, setup_code, number=1)
  print(f"Sorting 3000 numbers, took {timer:.7f} seconds")