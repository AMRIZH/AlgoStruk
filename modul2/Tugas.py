from latOOP import Manusia, MhsTIF

class Pesan(object):
  """Sebuah class bernama pesan"""
  def __init__(self, sebuahString):
    self.teks = sebuahString
  def apakahTerkandung(self, strKandungan) :
    return strKandungan in self.teks
  def hitungKonsonan(self) :
    k = 0
    konson = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    for i in self.teks :
      if i.lower() in konson :
        k +=1
    return k
  def hitungVokal(self) :
    v = 0
    vokal = ('a', 'e', 'i', 'o', 'u')
    for i in self.teks :
      if i.lower() in vokal :
        v +=1
    return v


# p9 = Pesan("Indonesia Negeri yang indah")
# p9.apakahTerkandung('ege')
# p9.apakahTerkandung('eka')

# p10 = Pesan('Surakarta')
# p10.hitungKonsonan()
# p10.hitungVokal()

#===================================================
class Mahasiswa(Manusia):
  def __init__(self, nama, NIM, kota, us):
    """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
    self.nama = nama
    self.NIM = NIM
    self.kotaTinggal = kota
    self.uangSaku = us
    self.kuliah = []
  def infoMHS(self):
    s = self.nama + ', NIM ' + str(self.NIM) \
          + '. Tinggal di ' + self.kotaTinggal \
          + '. Uang saku Rp ' + str(self.uangSaku) \
          + ' tiap bulannya.'
    print(s)
  def perbaruiKotaTinggal(self, kota):
    self.kotaTinggal = kota
  def ambilKotaTinggal(self) :
    print(self.kotaTinggal)
  def ambilUangSaku(self):
    return self.uangSaku
  def tambahUangSaku(self, uang):
    self.uangSaku += uang
  def listKuliah(self) :
    return self.kuliah
  def ambilKuliah(self, matkul) :
    self.kuliah.append(matkul)
  def hapusKuliah(self, matkul) :
    self.kuliah.remove(matkul)
  

# m9 = Mahasiswa("Maraym", 123, "Jakarta", 5000)
# m7 = Mahasiswa("Penelope" ,234 , "Semarang", 10000)
# m9.perbaruiKotaTinggal('Sleman')
# m9.ambilKotaTinggal()
# m7.ambilUangSaku()
# m7.tambahUangSaku(50000)
# m7.ambilUangSaku()
  
#=======================================================
# m234 = Mahasiswa("Anastasia", 456, "Colomadu", 20000)
# m234.listKuliah()
# m234.ambilKuliah('Matematika Diskrit')
# m234.listKuliah()
# m234.ambilKuliah('Algoritma dan Struktur Data')
# m234.listKuliah()
# m234.hapusKuliah('Algoritma dan Struktur Data')
# m234.listKuliah()

#==================================================
class siswaSMA(Manusia):
  """Kami siswa siswi SMA"""
  def __init__(self, nama):
    self.nama = nama
    self.kelas = 10
  def naikKelas(self):
    self.kelas += 1
  def turunKelas(self):
    self.kelas -= 1
  def infoKelas(self):
    print(self.kelas)

# sma1 = siswaSMA("Maybeline")
# sma1.infoKelas()
# sma1.naikKelas()
# sma1.infoKelas()
# sma1.turunKelas()

#================================================
mTIF = MhsTIF("Abdul", 121, "Boyolali", 4000)

# ambilKotaTinggal = dari mahasiswa
# ambilKuliah = dari mahasiswa
# ambilNIm = dari mahasiswa
# ambilNama = dari mahasiswa
# ambilUangSaku = dari mahasiswa
# hapusKuliah = dari mahasiswa
# katakanPy = dari MhsTIF
# listKuliah = dari mahasiswa
# makan = dari manusia
# mengalikanDengandua = dari manusia
# olahraga = dari manusia
# perbaruiKotaTinggal  = dari mahasiswa
# tambahUangSaku = dari mahasiswa
# ucapkanSalam = dari manusia
