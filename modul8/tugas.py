def cetakHexa(decimal) :
  return hex(decimal)

def cetakHexa2(decimal) :
  hex_chars = "0123456789ABCDEF"
  if decimal == 0:
      return "0"
  hexadecimal = ""
  while decimal > 0:
      remainder = decimal % 16
      hexadecimal = hex_chars[remainder] + hexadecimal
      decimal = decimal // 16
  return hexadecimal

#==========================================================
from latihan import Stack
def no2():
  nilai = Stack()
  for i in range(16):
      if i % 3 == 0:
          nilai.push(i)
#======
def no3():
  nilai = Stack()
  for i in range(16):
      if i % 3 == 0:
          nilai.push(i)
      elif i % 4 == 0:
          nilai.pop()
          
#=======================================================
from latihan import Queue, PriorityQueue, PriorityQEntry

