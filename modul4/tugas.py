class MhsTIF(object):
  def __init__(self,name, NIM, alamat, uangsaku) :
    self.name = name
    self.NIM = NIM
    self.alamat = alamat
    self.uangsaku = uangsaku
    
# target = 'Klaten'
def cariKota(Daftar, target) :
  for i in Daftar:
      if i.alamat == target:
          print(i.name + ' tinggal di ' + target)
          
def cariSemuaKota(Daftar,target) :
  absen = []
  for i in range(len(Daftar)):
    if Daftar[i].alamat == target:
      absen.append(i)
  return absen

def uangSakuMin(Daftar) :
  return min(mhs.uangsaku for mhs in Daftar)

def uangSakuMinAll(Daftar) :
  uangMinim = uangSakuMin(Daftar)
  return [mhs.name for mhs in Daftar if mhs.uangsaku == uangMinim]

def siapaUangSaku(Daftar , uang):
  return [mhs.name for mhs in Daftar if mhs.uangsaku < uang]

#======================================================
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

# print nama mhs yang tinggal di surakarts
cariKota(Daftar, "Surakarta")
cariKota(Daftar, "Negara Api")

# ABSEN mahasiswa yang tinggal di surakarta
print(cariSemuaKota(Daftar,"Surakarta"))

# mencari uang saku terkecil
print(uangSakuMin(Daftar))

# siapa saja yang memiliki uang saku terkecil
print(uangSakuMinAll(Daftar))

# mencari mhs yang sangu nya dibawah 250000
print(siapaUangSaku(Daftar,250000))



#========================================================
# junk code

# method berikut memiliki fungsi yang sama dengan yang diatas
# from math import inf as infinity
# def uangSakuMin(Daftar) :
#   uang = infinity
#   for i in Daftar:
#     if i.uangsaku < uang :
#       uang = i.uangsaku
#   return uang
  
# def uangSakuMinAll2(Daftar) :
#   uang = infinity
#   k =[]
#   for i in Daftar:
#     if i.uangsaku < uang :
#       uang = i.uangsaku
#   for j in range(len(Daftar)):
#     if Daftar[j].uangsaku == uang :
#       k.append(Daftar[j].name)
#   return k
