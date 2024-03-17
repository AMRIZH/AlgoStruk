
def cariLurus( wadah, target ):
  n = len( wadah )
  for i in range( n ):
    if wadah[i] == target:
      return True
  return False

def cariTerkecil(kumpulan):
  n = len(kumpulan)
  # Anggap item pertama adalah yang terkecil
  terkecil = kumpulan[0]
  # tentukan apakah item lain lebih kecil
  for i in range(1,n):
    if kumpulan[i] < terkecil:
      terkecil = kumpulan[i]
  return terkecil #kembalikan yang terkecil

def binSe(kumpulan, target):
   # Mulai dari seluruh runtutan elemen
   low = 0
   high = len(kumpulan) - 1

   # Secara berulang belah runtutan itu menjadi separuhnya
   # sampai targetnya ditemukan
   while low <= high:
       # Temukan pertengahan runtut itu
       mid = (high + low) // 2
       # Apakah pertengahannya memuat target?
       if kumpulan[mid] == target:
           return True
       # ataukah targetnya di sebelah kirinya?
       elif target < kumpulan[mid]:
           high = mid - 1
       # ataukah targetnya di sebelah kanannya?
       else:
           low = mid + 1
   # Jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
   return False
 
#=======================================================
