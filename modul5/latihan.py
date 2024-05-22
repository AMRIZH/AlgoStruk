def swap(lis,a,b) :
  temp = lis[a]
  lis[a] = lis[b]
  lis[b] = temp
  
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
  posisiYangTerkecil = dariSini #-> anggap ini yang terkecil
  for i in range(dariSini+1, sampaiSini): #-> cari di sisa list
      if A[i] < A[posisiYangTerkecil]: 
          posisiYangTerkecil = i
  return posisiYangTerkecil#-> #-> kalau menemukan yang lebih kecil,anggapan dirubah
  
def bubbleSort(A):
  n = len(A)-1
  for i in range(n): #-> Lakukan operasi gelembung sebanyak n-1
      for j in range(n-i): #-> Dorong elemen terbesar ke ujung kanan
          if A[j] > A[j+1]: #Jika di kiri lebih besar dari di kanannya,
              swap(A,j,j+1) #tukar posisi elemen ke j dengan ke j+1

def selectionSort(A):
  n = len(A)
  for i in range(n - 1):
      indexKecil = cariPosisiYangTerkecil(A, i, n)
      if indexKecil != i :
          swap(A, i, indexKecil)
          
def selectionsort2(A) :
  n = len(A)
  for i in range(n-1) :
    indexKecil = i
    for j in range(i+1,n) :
      if A[j] < A[indexKecil] :
        indexKecil = j
    if indexKecil != i :
      swap(A,i,indexKecil)
            
def insertionSort(A):
  n = len(A)
  for i in range(1, n):
    nilai = A[i]
    pos = i-1
    while pos > 0 and nilai < A[pos]: # -> Cari posisi yang tepat
      A[pos+1] = A[pos]
      pos = pos - 1 # # dan geser ke kanan terusnilai-nilai yang lebih besar
    A[pos] = nilai # -> Pada posisi ini tempatkan nilai elemen ke i.

A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

# buil-in sort method
def sortingPY(lis) :
  lis.sorted()
  print(lis)
  

#==================================================
# program test runtime
from time import time as waktu
from random import shuffle
from testcase import k

# k = list(range(1,6001))
# shuffle(k)
u_bub = k[:] ## \\\\
u_sel = k[:] ## -- Jangan lupa simbol [:]-nya!.
u_ins = k[:] ## //

aw=waktu();bubbleSort(u_bub);ak=waktu();print('bubble: %g detik' %(ak-aw) );
aw=waktu();selectionSort(u_sel);ak=waktu();print('selection: %g detik' %(ak-aw) );
aw=waktu();insertionSort(u_ins);ak=waktu();print('insertion: %g detik' % (ak-aw) );