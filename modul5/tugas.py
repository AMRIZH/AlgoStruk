def swap(lis,a,b) :
  temp = lis[a]
  lis[a] = lis[b]
  lis[b] = temp

#=======================================================
class MhsTIF(object):
  def __init__(self,name, NIM, alamat, uangsaku) :
    self.name = name
    self.NIM = NIM
    self.alamat = alamat
    self.uangsaku = uangsaku
   
#=======================================================
def bubleSortNim(Daftar) :
  n = len(Daftar)
  for i in range(n-1):
      for j in range(n-i-1):
          if Daftar[j].NIM > Daftar[j+1].NIM : 
              swap(Daftar,j,j+1)
 

def cariPosisiYangTerkecil(Daftar, dariSini, sampaiSini):
  posisiYangTerkecil = dariSini
  for i in range(dariSini+1, sampaiSini): 
      if Daftar[i].NIM < Daftar[posisiYangTerkecil].NIM: 
          posisiYangTerkecil = i
  return posisiYangTerkecil
             
def selectionOrderNim(Daftar) :
  n = len(Daftar)
  for i in range(n - 1):
      indexKecil = cariPosisiYangTerkecil(Daftar, i, n)
      if indexKecil != i :
          swap(Daftar, i, indexKecil)
  
def insertionSortNim(Daftar):
  n = len(Daftar)
  for i in range(1, n):
      nilai = Daftar[i].NIM
      pos = i
      while pos > 0 and nilai < Daftar[pos - 1].NIM: # -> Cari posisi yang tepat
          Daftar[pos].NIM = Daftar[pos - 1].NIM
          pos = pos - 1 # # dan geser ke kanan terusnilai-nilai yang lebih besar
      Daftar[pos].NIM = nilai # -> Pada posisi ini tempatkan nilai elemen ke i.

def showUrurtan(Daftar) :
  for i in Daftar :
    print("Mahasiswa",i.name,"Memiliki NIM",i.NIM)
  print("---------------------------------")
#================================
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
bubleSortNim(Daftar)
showUrurtan(Daftar)

# mengembalikan urutan seperti semula
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

# selectionOrder Algorithm
selectionOrderNim(Daftar)
showUrurtan(Daftar)

# mengembalikan urutan seperti semula
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

# insertion odrder algorithm
insertionSortNim(Daftar)
showUrurtan(Daftar)


