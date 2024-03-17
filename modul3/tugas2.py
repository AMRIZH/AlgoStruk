# matriks nol

def matrixZero(n ,m = None) :
  if m is None :
    m = n
  result = [[0 for j in range(m)] for i in range(n)] # create zero matrik with result size
  return result

# matrix identity

def identityMatrix(n) :
  result = [[0 for j in range(n)] for i in range(n)] # create zero matrik with result size
  for i in range(n) :
    result[i][i] = 1
  return result

print(matrixZero(5,4))
print(identityMatrix(5))