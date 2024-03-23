def swap(lis,a,b) :
  temp = lis[a]
  lis[a] = lis[b]
  lis[b] = temp

#===========================================================================

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
                print(A) ##!!!
                i = i + 1                        
            else:                                
                A[k] = separuhKanan[j]
                print(A) ##!!!         
                j = j + 1                       
                k = k + 1                           
        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            print(A) ##!!!
            i = i + 1                
            k = k + 1                
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            print(A) ##!!!
            j = j + 1                
            k = k + 1                

#============================================================================
def partisi(A, awal, akhir):
    nilaiPivot = A[awal]  
    penandaKiri = awal + 1  
    penandaKanan = akhir  
    selesai = False
    while not selesai:  
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1
        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1 
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            swap(A, penandaKanan,penandaKiri)
            print(A) ##!!!
    swap(A, awal,penandaKanan)
    print(A) ##!!!!
    return penandaKanan  
  
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1 )  

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)  
        quickSortBantu(A, awal, titikBelah - 1)  
        quickSortBantu(A, titikBelah + 1, akhir)  

L = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
print(L)
mergeSort(L)
print(L)
print("-----------------------------------------")
L = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
print(L)
quickSort(L)
print(L)
