# merge sort baru libih efektif
def mergeSort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(A, low, mid)
        mergeSort(A, mid + 1, high)
        merge(A, low, mid, high)

def merge(A, low, mid, high):
    left_half = A[low:mid + 1]
    right_half = A[mid + 1:high + 1]
    
    i = 0
    j = 0
    k = low
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            A[k] = left_half[i]
            i += 1
        else:
            A[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        A[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        A[k] = right_half[j]
        j += 1
        k += 1

L = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
print("Sebelum merge sort:", L)
mergeSort(L, 0, len(L) - 1)
print("Setelah merge sort:", L)

#======================================================================

def median_of_three(A, awal, akhir):
    mid = (awal + akhir) // 2
    a = A[awal]
    b = A[mid]
    c = A[akhir]
    if a <= b <= c or c <= b <= a:
        return mid
    elif b <= a <= c or c <= a <= b:
        return awal
    else:
        return akhir

def partisi(A, awal, akhir):
    pivot_index = median_of_three(A, awal, akhir)
    nilaiPivot = A[pivot_index]
    A[awal], A[pivot_index] = A[pivot_index], A[awal]  # Pindahkan pivot ke awal
    penandaKiri = awal + 1
    penandaKanan = akhir
    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri += 1
        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan -= 1
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            A[penandaKanan], A[penandaKiri] = A[penandaKiri], A[penandaKanan]
    A[awal], A[penandaKanan] = A[penandaKanan], A[awal]  # Pindahkan pivot ke posisi akhirnya
    return penandaKanan

# Sisanya tetap sama
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1 )  

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)  
        quickSortBantu(A, awal, titikBelah - 1)  
        quickSortBantu(A, titikBelah + 1, akhir)
        
L = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
print(L)
quickSort(L)
print(L)

#========================================================
from time import time as detak
from random import shuffle as kocok
import time
k = list(range(6000))
kocok(k) 
u_mrg = k[:] 
u_qck = k[:] 

aw=detak();mergeSort(u_mrg,0,len(u_mrg)-1);ak=detak();print('merge: %g detik' %(ak-aw) );
aw=detak();quickSort(u_qck);ak=detak();print('quick: %g detik' %(ak-aw) );