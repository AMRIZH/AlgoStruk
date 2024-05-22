from math import sqrt
import random
#==================================
def cetakSiku(x) :
  for i in range(1,x+1) :
    print("*"*i) 

# testcase
cetakSiku(5)
cetakSiku(3)

#=======================
def segi4(y,x) :
  print("@"*x)
  for i in range(y-2) :
    print("@"+ " "*(x-2) +"@")
  print("@"*x)

#testcase
segi4(5,5)

#=======================
def jumlahVokal(kata) :
  vocal = ("a","i","u","e","o")
  v = 0
  for i in kata :
    if i.lower() in vocal :
      v +=1
  return len(kata),v

#testcase
print("huruf/vokal =",jumlahVokal("Surakarta"))

def jumlahKonsonan(kata) :
  konsonan = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
  k = 0
  for i in kata :
    if i.lower() in konsonan :
      k +=1
  return len(kata), k

#testcase
print("huruf/konsonan =",jumlahKonsonan("Surakarta"))

#=========================================
def rerata(lis) :
  return sum(lis)/len(lis)

#testcase
l1 = [1,2,3,4,5]
l2 = [3,4,5,4,3,4,5,2,2,10,11,23]
print("mean =",rerata(l1))
print("mean =",rerata(l2))

#=====
def variance(lis) :
  n = len(lis)
  if n < 2:
    raise ValueError("Variance requires at least two data points")
  mean = rerata(lis)
  variance = sum((xi - mean) ** 2 for xi in lis) / (n - 1)
  return variance

def stdev(lis):
    import math
    return math.sqrt(variance(lis))

#testcase
print("variance =", variance(l1))
print("variance =",variance(l2))
print("standar deviasi =",stdev(l1))
print("standar deviasi =",stdev(l2))

#=============================================

def isPrime(x):
    if x < 2: # 1 , zero , negative number is not prime 
        # print("Not prime")
        return False
    elif x == 2: # 2 is prime number
        # print("Prime")
        return True
    elif x % 2 == 0: # even number is not prime 
        # print("Not prime")
        return False
    # checks all even numbers from 3 to the root of x, with rounding.
    else:
        for i in range(3, int(sqrt(x)) +1 , 2): 
            if x % i == 0:
                return False
                # print("Not prime")
                # break
        else:
            # print("Prime")
            return True

# testcases
# isPrime(-5)
# isPrime(0)
# isPrime(1)
# isPrime(45)
# isPrime(17)

#============
def faktorPrima(x) :
  faktor_prima = []
  faktor = 2
  while faktor <= x:
      if x % faktor == 0:
          faktor_prima.append(faktor)
          x = x // faktor
      else:
          faktor += 1
  return faktor_prima

# testcases
print("faktor prima =",faktorPrima(21))
print("faktor prima =",faktorPrima(143))
#===========================================
def apakahTerkandung(cari, kalimat) :
  if cari in kalimat :
    print("benar")
  else :
    print("salah")

apakahTerkandung("do", "Indonesia tanah air beta") #benar
apakahTerkandung("amri", "Indonesia tanah air beta") #salah
#==========================================
def tigaLima(x) :
  for i in range(1,x+1) :
    if i % 3 == 0 and i % 5 == 0 :
      print("python UMS")
    elif i % 3 == 0 :
      print("python")
    elif i % 5 == 0 :
      print("UMS")
    else :
      print(i)

# testcases
tigaLima(10)

#=========================================
def selesaikanABC(a,b,c) :
  a = float(a)
  b = float(b)
  c = float(c)
  D = b**2 - 4*a*c
  if D < 0 :
    print("Determinant is negative, function have no root")
  else :
    x1 = (-b + sqrt(D))/(2*a)
    x2 = (-b - sqrt(D))/(2*a)
    hasil = (x1,x2)
    print(hasil)
  
#testcases
selesaikanABC(1,2,3)

#========================================
def apakahKabisat(tahun) :
  if tahun % 400 == 0 :
    print(tahun, "merupakan tahun kabisat")
  elif tahun % 100 == 0 :
    print(tahun, "bukan tahun kabisat")
  elif tahun % 4 == 0 :
    print(tahun, "merupakan tahun kabisat")
  else :
    print(tahun, "bukan tahun kabisat")

#testcases
apakahKabisat(2000)

#==========================================
def tebakAngka() :
  angka = random.randint(1,5)
  k = 0 # menebak attempted
  print("Coba Tebak angka 1-100")
  while k < 5 :
    k +=1
    jawab = input("Masukkan tebakan ke "+str(k)+" :>")
    if int(jawab) < angka :
      print("Itu terlalu kecil")
    elif int(jawab) > angka :
      print("Itu terlalu besar")
    else : 
      print("Selamat Kamu benar!!")
      break
  if k == 5 :
    print("Kamu telah 5x menebak, jwaban yg benar adalah",angka)
    
#testcases
# tebakAngka()
    
#========================================
def katakan(bilangan):
    if bilangan == 0:
        return "Nol"
    elif bilangan > 999999999999 :
      return "Angka terlalu besar"
    
    satuan = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"]
    belasan = ["", "Sebelas", "Dua Belas", "Tiga Belas", "Empat Belas", "Lima Belas", "Enam Belas", "Tujuh Belas", "Delapan Belas", "Sembilan Belas"]
    puluhan = [" ", "Sepuluh ", "Dua Puluh ", "Tiga Puluh ", "Empat Puluh ", "Lima Puluh ", "Enam Puluh ", "Tujuh Puluh ", "Delapan Puluh ", "Sembilan Puluh "]

    def konversi_triple(angka):
        result = ""

        if angka // 100 > 0:
            result += satuan[angka // 100] + " Ratus "

        angka %= 100

        if angka // 10 == 1:
            result += belasan[angka % 10]
        else:
            result += puluhan[angka // 10] + satuan[angka % 10]

        return result

    miliar = bilangan // 1000000000
    juta = (bilangan % 1000000000) // 1000000
    ribu = (bilangan % 1000000) // 1000
    sisa = bilangan % 1000

    result = ""

    if miliar > 0:
        result += konversi_triple(miliar) + " Miliar "

    if juta > 0:
        result += konversi_triple(juta) + " Juta "

    if ribu > 0:
        result += konversi_triple(ribu) + " Ribu "

    result += konversi_triple(sisa)
    
    result = result.replace("Satu Ratus","Seratus")

    return result.strip()

print(katakan(3125150))
print(katakan(9999999999999))

#=================================================
def formatRupiah(n):
    # Mengonversi bilangan bulat menjadi string dan membalikkan urutannya
    reversedNominal = str(n)[::-1]

    # Membuat string dalam format rupiah dengan menambahkan titik setiap tiga digit
    formatTitik = '.'.join([reversedNominal[i:i+3] for i in range(0, len(reversedNominal), 3)])

    # Memutar kembali string dan menambahkan 'Rp ' di depannya
    return 'Rp ' + formatTitik[::-1]

# testcases
print(formatRupiah(1500))      # Output: Rp 1.500
print(formatRupiah(2560000))    # Output: Rp 2.560.000

#=================================================

