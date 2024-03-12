A = [ [2,3], [5,7] ]
print(A[0][1])
print(A[1][1])

B = [ [0 for j in range(3)] for i in range(3) ]
print(B)

# Membuat list kuadrat bilangan dari 0 sampai 6
C =  [x**2 for x in range(0,7)] #[0, 1, 4, 9, 16, 25, 36]

# Membuat list yang berisi tuple pasangan bilangan dan kuadratnya, dari 0 sampai 6
D =  [(x,x**2) for x in range(7)] #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]

def cariLurus( wadah, target ):
  n = len( wadah )
  for i in range( n ):
    if wadah[i] == target:
      return True
  return False

