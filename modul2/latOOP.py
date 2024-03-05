class Pesan(object):
  """Sebuah class bernama pesan"""

  def __init__(self, sebuahString):
    self.teks = sebuahString
  def cetakIni(self):
    print(self.teks)
  def cetakKapital(self):
    print(str.upper(self.teks))
  def cetakKecil(self):
    print(str.lower(self.teks))
  def jumlahKar(self):
    return len(self.teks)
  def cetakJumlahKar(self):
    print("kalimat ini memiliki",len(self.teks),"karakter")
  def perbarui(self, stringBaru):
    self.teks = stringBaru

class Manusia(object):
  """ Class 'Manusia' dengan inisiasi 'nama' """
  def __init__(self,nama):
    self.nama = nama
  def ucapkanSalam(self):
    print("Salaam, namaku", self.nama)
  def makan(self, s):
    print("Saya baru saja makan", s)
    self.keadaan = 'kenyang'
  def olahraga(self,k):
    print("Saya baru saja latihan", k)
    self.keadaan = 'lapar'
  def mengalikanDenganDua(self,n):
    return n*2
  
## Kali ini melarikannya lewat file yang sama.
## Lewat python shell juga bisa.
p1 = Manusia('Fatimah')
p1.ucapkanSalam()

class Mahasiswa(object):
  def __init__(self, nama, NIM, kota, us):
    """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
    self.nama = nama
    self.NIM = NIM
    self.kotaTinggal = kota
    self.uangSaku = us
    
  def __str__(self):
    s = self.nama + ', NIM ' + str(self.NIM) \
          + '. Tinggal di ' + self.kotaTinggal \
          + '. Uang saku Rp ' + str(self.uangSaku) \
          + ' tiap bulannya.'
    return s
    
  def ambilNama(self):
    return self.nama
    
  def ambilNIM(self):
    return self.NIM
    
  def ambilUangSaku(self):
    return self.uangSaku
    
  def makan(self, s):
    """Metode ini menutupi metode ’makan’-nya class Manusia. Mahasiswa kalau makan sambil belajar."""
    print("Saya baru saja makan", s, "sambil belajar.")
    self.keadaan = 'kenyang'

#========================
class MhsTIF(Mahasiswa): # perhatikan class induknya: Mahasiswa
  """Class MhsTIF yang dibangun dari class Mahasiswa"""
  def katakanPy(self):
    print('Python is cool.')

#=======================================
class kelasKosongan(object):
  pass
## Sekarang kita coba
k = kelasKosongan()
k.x = 23
k.y = 47
print(k.x + k.y)
k.mystr = 'Indonesia'
print(k.mystr)

#========================================
