import re
# cocok = re.findall(pola, string)

s = 'sebuah contoh kata:teh!!'
cocok = re.findall(r'kata:\w\w\w', s)
# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil:

if cocok:
  print('menemukan', cocok ) ## 'menemukan [kata:teh]'
else:
  print('tidak menemukan')
  
  
## Dua baris ini mencari pola 'eee' di string 'teeeh'. 
## Seluruh pola harus cocok, tapi itu bisa muncul di mana saja.
## Jika berhasil, \\texttt{cocok} adalah daftar semua teks yang cocok.
cocok = re.findall(r'eee', 'teeeh') #=> cocok == ['eee']
cocok = re.findall(r'ehs', 'teeeh') #=> cocok == []

## . = semua karakter kecuali \\n
cocok = re.findall(r'..h', 'teeeh') #=> cocok == ['eeh']

## \\d = karakter angka, \\w = karakter huruf atau angka
cocok = re.findall(r'\\d\\d\\d', 't123h di 2019 bulan 02') #=> cocok == ['123', '201']
cocok = re.findall(r'\\w\\w\\w', '@@a\*bc#def\*tghh!!') #=> cocok == ['def', 'tgh']

#================================================================

## e+ = satu atau lebih e, sebanyak-banyaknya.
cocok = re.findall(r'te+', 'ghdteeeh') #=> cocok == ['teee']

## Menemukan solusi yang paling kiri, dan dari situ mendorong si tanda '+'
## sejauh-jauhnya (ingat 'paling kiri dan paling besar').  
## Pada contoh ini, perhatikan bahwa pencarian menemukan dua pola yang tepat.
cocok = re.findall(r'e+', 'teeheeee') #=> cocok == ['ee', 'eeee']

## \\s\\* = nol atau lebih karakter putih (spasi, tab, dsb.)
## Di sini mencari 3 angka, kemungkinan dipisahkan oleh spasi/tab.
polanya = r'\\d\\s\\*\\d\\s\\*\\d'

cocok = re.findall(polanya, 'xx1 2 3xx') #=> cocok == ['1 2 3']
cocok = re.findall(polanya, 'xx12 3xx') #=> cocok == ['12 3']
cocok = re.findall(polanya, 'xx123xx') #=> cocok == ['123']

## ^ -> cocok dengan awal string, jadi ini tidak akan menemukan:
cocok = re.findall(r'^k\\w+', 'mejakursi') #=> tidak ketemu, cocok == []
## tapi tanpa ^ dia berhasil:
cocok = re.findall(r'k[\w\s]+', 'mejakursi tamu saya')#=> cocok == ['kursi tamu saya']

#=================================
s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'\w+@\w+', s)
print(cocok[0]) ## => 'b@google'

cocok = re.findall(r'[\w.-]+@[\w.-]+', s)
print(cocok[0]) ## => 'dita-b@google.com'

pola = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

#================================================

s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'([\w.-]+)@([\w.-]+)', s) ## perhatikan posisi () di polanya

cocok ## adalah [('dita-b', 'google.com')]
## Bisa kita pilah satu per satu seperti ini:
cocok[0][0] ## 'dita-b'
cocok[0][1] ## 'google.com'

#==============================================
## Kita punya banyak alamat email
s = 'Alamatku sri@google.com serta joko@abc.com ok bro. atau don@email.com'

## Di sini re.findall() mengembalikan sebuah list beranggotakan string alamat
pola = r'[\w\.-]+@[\w\.-]+'
e = re.findall(pola, s)
print(e)
##=> e akan berisi ['sri@google.com', 'joko@abc.com', 'don@email.com']

pola = r'([\w\.-]+)@([\w\.-]+)'
e = re.findall(pola, s)
print(e) ##==> sekarang bagaimanakah hasilnya?

## Atau kita cetak satu per satu:
for tup in e:
    print('user', tup[0], 'dengan host:', tup[1])
    
# contoh hasil :
# [('sri', 'google.com'), ('joko', 'abc.com'), ('don', 'email.com')]
# user sri dengan host: google.com
# user joko dengan host: abc.com 
# user don dengan host: email.com

#==================================================
