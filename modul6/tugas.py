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
def mergeSort(daftar):
    if len(daftar) > 1:
        mid = len(daftar) // 2
        separuhKiri = daftar[:mid]
        separuhKanan = daftar[mid:]
        
        mergeSort(separuhKiri)  
        mergeSort(separuhKanan)  
        
        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i].NIM < separuhKanan[j].NIM:  
                daftar[k] = separuhKiri[i]         
                i = i + 1                        
            else:                                
                daftar[k] = separuhKanan[j]           
                j = j + 1                       
            k = k + 1                            

        while i < len(separuhKiri):
            daftar[k] = separuhKiri[i]    
            i = i + 1                
            k = k + 1                

        while j < len(separuhKanan):
            daftar[k] = separuhKanan[j]   
            j = j + 1                
            k = k + 1                

#================================================================
def partisi(daftar, awal, akhir):
    nilaiPivot = daftar[awal]
    penandaKiri = awal + 1  
    penandaKanan = akhir  
    selesai = False
    
    while not selesai:  
        while penandaKiri <= penandaKanan and daftar[penandaKiri].NIM <= nilaiPivot.NIM:
            penandaKiri += 1            
        while daftar[penandaKanan].NIM >= nilaiPivot.NIM and penandaKanan >= penandaKiri:
            penandaKanan -= 1  
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            swap(daftar,penandaKiri,penandaKanan)
            
    swap(daftar,awal,penandaKanan) 
    return penandaKanan  
  
def quickSort(daftar):
    quickSortBantu(daftar, 0, len(daftar) - 1 )  

def quickSortBantu(daftar, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(daftar, awal, akhir) 
        quickSortBantu(daftar, awal, titikBelah - 1)  
        quickSortBantu(daftar, titikBelah + 1, akhir)  

def showUrurtan(Daftar) :
  for i in Daftar :
    print("Mahasiswa",i.name,"Memiliki NIM",i.NIM)
  print("---------------------------------")
  

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

# pengurutan nama mahasiswa berdasar NIM

# buble sort algorithm
mergeSort(Daftar)
showUrurtan(Daftar)

# mengembalikan urutan seperti semula
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

# selectionOrder Algorithm
quickSort(Daftar)
showUrurtan(Daftar)

