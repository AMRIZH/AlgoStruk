import re
# cocok = re.findall(pola, string)

s = 'sebuah contoh kata:batagor!!'
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
if cocok:
  print('menemukan', cocok ) ## 'menemukan [kata:teh]'
else:
  print('tidak menemukan')
  

cocok = re.findall(r'ehs', 'teeeh') #=> cocok == []
if cocok:
  print('menemukan', cocok ) ## 'menemukan [kata:teh]'
else:
  print('tidak menemukan')
  
## . = semua karakter kecuali \\n
cocok = re.findall(r'..h', 'te%eh') #=> cocok == ['eeh']
if cocok:
  print('menemukan', cocok ) ## 'menemukan [kata:teh]'
else:
  print('tidak menemukan')
## \d = karakter angka, \w = karakter huruf atau angka
cocok = re.findall(r'\d\d\d', 't123h di 2019 bulan 02') #=> cocok == ['123', '201']
if cocok:
  print('menemukan', cocok ) ## 'menemukan [kata:teh]'
else:
  print('tidak menemukan')
  
cocok = re.findall(r'\w\w\w', '@@a*bc#def*tghh!!') #=> cocok == ['def', 'tgh']
if cocok:
  print('menemukan', cocok ) ## 'menemukan [kata:teh]'
else:
  print('tidak menemukan')
  
#================================
file_path="C:\Amri\KULIAH_UMS\Semester4\labASD\modul7\indonesia.txt"

# Open the file and read its contents
with open(file_path, 'r', encoding='UTF-8') as file:
  text = file.read()
  
# \b = word boundary, \w = word character, * = zero or more
pattern = r'\bme\w*' 
me_words = re.findall(pattern, text)
me_words_tuple = tuple(me_words)
print(me_words_tuple)