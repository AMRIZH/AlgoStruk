
def consistent(matrik) :
  for i in matrik :
    if len(i) != len(matrik[1]) : # check if all inner array have similar length
      return False
  return True
  
def getMatrixSize(matrik) :
  if consistent(matrik) : 
    return (len(matrik), len(matrik[0])) # tinggi x lebar
  else :
    print("Not consistent matrik")
    return None

def sumMatrix2(matrik1 ,matrik2):
  if consistent(matrik1) and consistent(matrik2):
    size1 = getMatrixSize(matrik1)
    size2 = getMatrixSize(matrik2)
    if size1 != size2 :
      print("Matrix dimensions must be the same for addition.")
      return None
    result = [[0 for j in range(size1[1])] for i in range(size1[0])] # create zero matrik with result size
    for i in range(size1[1]):
      for j in range(size1[0]):
        result[i][j] = matrik1[i][j] + matrik2[i][j]
    return result
  else :
    print("either or both matrix is not consistent")
    return None

def sumMatrix(matrik1 ,matrik2):
  if consistent(matrik1) and consistent(matrik2): # check matrix consstency
    size1 = getMatrixSize(matrik1) # determine size of matrix
    size2 = getMatrixSize(matrik2) 
    if size1 != size2 : # addition must same size
      print("Matrix dimensions must be the same for addition.")
      return None
    result = [] # new list to store result
    for i in range(size1[0]):
        row = [] # row of new list , reset to empty list every iteration
        for j in range(size1[1]):
            row.append(matrik1[i][j] + matrik2[i][j])
        result.append(row)
  else :
    print("either or both matrix are not consistent")
    return None
  
def multiplyMatrices(matrix1, matrix2):
    # Check if the matrices are consistent
    if not consistent(matrix1) or not consistent(matrix2):
        print("One or both matrices are not consistent.")
        return None

    # Check if the dimensions are compatible for multiplication
    size1 = getMatrixSize(matrix1)
    size2 = getMatrixSize(matrix2)
    if size1[1] != size2[0]:
        print("Matrix dimensions are incompatible for multiplication.")
        return None

    # Create a new matrix with the correct dimensions
    result = [[0 for j in range(size2[1])] for i in range(size1[0])]

    # Perform matrix multiplication
    for i in range(size1[0]):
        for j in range(size2[1]):
            for k in range(size1[1]):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def multiplyMatrices2(matrix1, matrix2):
    # Check if the matrices are consistent
    if not consistent(matrix1) or not consistent(matrix2):
        print("One or both matrices are not consistent.")
        return None

    # Check if the dimensions are compatible for multiplication
    size1 = getMatrixSize(matrix1)
    size2 = getMatrixSize(matrix2)
    if size1[1] != size2[0]:
        print("Matrix dimensions are incompatible for multiplication.")
        return None

    result = []  # Initialize an empty list to store the result

    # Perform matrix multiplication
    for i in range(size1[0]):
        row = []  # Initialize an empty row
        for j in range(size2[1]):
            element = 0
            for k in range(size1[1]):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)

    return result

def determinant(matrik) :
  if not consistent(matrik) : # matrix must consistent/valid
    return None
  size = getMatrixSize(matrik)
  if size[0] != size[1] : # matrix must n*n in size
    return None
  if size[0] == 1: # single element matrix, the determinant is the only element
    return matrik[0][0]
  if size[0] == 2: # 2*2 size matrix, the determinant is a*d-b*c
      return matrik[0][0] * matrik[1][1] - matrik[0][1] * matrik[1][0]
  det = 0
  for i in range(size[0]): # more than 2*2 size matrix
      submatrix = [row[:i] + row[i+1:] for row in (matrik[:i] + matrik[i+1:])]
      det += ((-1) ** i) * matrik[0][i] * determinant(submatrix)
  return det

#=================================================
# testcases
matrik1 = [[1, 2, 3], [1, 1, 2], [2, 1 , 2]]
matrik2 = [[1, 3, 1], [0, 1, 0], [2, 0 , 2]]

# consistency and validation CHECK
if consistent(matrik1) :
  print(matrik1, "konsisten")

# check matrix size
print(getMatrixSize(matrik1))

# add 2 matrices
tambah = sumMatrix(matrik1,matrik2)
print(tambah)
tambah2 = sumMatrix2(matrik1,matrik2)
print(tambah2)

#multiply 2 matrix
print(multiplyMatrices(matrik1,matrik2))
print(multiplyMatrices2(matrik1,matrik2))


# check matrix determinant size 
print(determinant(matrik1))
print(determinant(matrik2))
