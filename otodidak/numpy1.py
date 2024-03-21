import numpy as np
import sys

# a = np.array([1,2,3], dtype="int8")
# b = np.array([[1,0,2,0,3,0], [4,0,5,0,6,0]])

# print(a)

a = np.array([1,2,3])
b = np.array([3,4,5])
print(a)
print(a*b)

c = np.array([[1,2,3],[4,5,6]])
print(c)

#get dimension
print(c.ndim)
#get shape
print(c.shape)
#get data type
print(c.dtype)
d = np.array([1,4,6],dtype='int32') # we can specify which data type we want
e = np.array([4,5,6,7,8,9],dtype='int8')

# get data size (bytes)
print(d.itemsize)
print(e.itemsize)

#get  size (number of elements)
print(d.size)
print(e.size)

# get total size = itemsize * size
print(d.nbytes)
print(e.nbytes)

# slicing in numpy
# get specific element with certain index
print(c[1,2]) # matrix c index ke 1, lalu index 2
#get specific row
print(c[0,:]) # return whole 1st row
# get specific column
print(c[:,1])

f = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# array[row , startindex:endindex:stepsize]
print(f[0,1:6:2])
print(f[2,::3])

#change value
f[0,0] = 5  # 1 swapped with 5
print(f[0]) 

f[0,:] = 23 # mengubah baris ke 0, menjadi 23 semuanya
print(f[0])

# 3D array
g = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # 2x2x3
print(g)

# get specific element
print(g[0,1,1]) # lebar 0, row 1, column 1

# replace
g[:,1,1] = 9
print(g)

#======================================
# All zero matrix
zero = np.zeros((2,3,4)) # leabr 2, baris 3, kolom 4
print(zero)

zero2 = np.zeros((3,4)) # baris 3, kolom 4
print(zero2)

# All 1 matrices
one = np.ones((2,3,4))
print(one)
one2 = np.ones((3,4), dtype='int16')
print(one2)

# All (any number) matrices np.full((size),parameter,dtype='float32')
full = np.full((2,2),99)
print(full)

# full 2 and 3 will return exactly same matrix
full2 = np.full(a.shape,65)
full3 = np.full_like(a,65)
print(full2)
print(full3)

# full random decimal numbers
h = np.random.rand(2,4)
print(h)
i = np.random.random_sample(a.shape)
print(i)

# matrix full random integer values
j = np.random.randint(7)
print(j)
j = np.random.randint(5,size=(3,3))
print(j)
j = np.random.randint(-10,10,size=(3,4)) # random int -10 until 10, size 3x4
print(j)
#=====================================
# identity matrix
print(np.identity(5))

#=========================
# repeating array
arr = np.array([1,2,3])
repeat1 = np.repeat(arr,3) # repeatin array 3times
print(repeat1)


#================================
a = np.array([1,2,3,4])
print(a)

