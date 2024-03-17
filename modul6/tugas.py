def swap(lis,a,b) :
  temp = lis[a]
  lis[a] = lis[b]
  lis[b] = temp

class MhsTIF(object):
  def __init__(self,name, NIM, alamat, uangsaku) :
    self.name = name
    self.NIM = NIM
    self.alamat = alamat
    self.uangsaku = uangsaku

#================================================================
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
                i = i + 1                        
            else:                                
                A[k] = separuhKanan[j]           
                j = j + 1                       
            k = k + 1                            

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]    
            i = i + 1                
            k = k + 1                

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]   
            j = j + 1                
            k = k + 1                
        

#================================================================
def partisi(A, awal, akhir):
    nilaiPivot = A[awal]  
    penandaKiri = awal + 1  
    penandaKanan = akhir  
    selesai = False
    
    while not selesai:  
        while penandaKiri <= penandaKanan and \
                A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1            
        while A[penandaKanan] >= nilaiPivot and \
                penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1  
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            swap(A, A[penandaKiri], A[penandaKanan])
            
    swap(A, A[penandaKiri], A[penandaKanan]) 
    return penandaKanan  
  
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1 )  

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)  
        quickSortBantu(A, awal, titikBelah - 1)  
        quickSortBantu(A, titikBelah + 1, akhir)  
        
#================================================================
c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chandra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 245000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 230000)
# Lalu kita membuat daftar mahasiswa dalam bentuk list seperti ini:
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]