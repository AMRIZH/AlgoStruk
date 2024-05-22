from Tugas import Mahasiswa
import random

print("Pendaftaran mahsiswa Baru !!")
nama = input("Nama mahasiswa baru ? >")
NIM = random.randint(100,999)
kota = input("Kota Asal? >")
uangSaku = int(input("Masukkan uang saku? >"))
mahs = Mahasiswa(nama,NIM,kota,uangSaku)
mahs.infoMHS()
