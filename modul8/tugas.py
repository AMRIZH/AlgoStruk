def cetakHexa(decimal) :
  return hex(decimal)[2:].upper()

def cetakHexa2(decimal) :
  hex_chars = "0123456789ABCDEF"
  if decimal == 0:
      return "0"
  hexadecimal = "" # menyipan hasil konversi dari LSB ke MSB
  while decimal > 0:
      remainder = decimal % 16
      hexadecimal = hex_chars[remainder] + hexadecimal
      decimal = decimal // 16
  return hexadecimal

# def cetakHexa3(decimal):
#     hex_chars = "0123456789ABCDEF"
#     if decimal == 0:
#         return "0"
#     hexadecimal = ""
#     while decimal > 0:
#         remainder = decimal % 16
#         hexadecimal = hex_chars[remainder] + hexadecimal
#         decimal = decimal // 16
#     return hexadecimal
    
#==========================================================
from latihan import Stack
def no2():
  nilai = Stack()
  for i in range(16):
      if i % 3 == 0:
          nilai.push(i)
      print(nilai.items,f" -> mencoba memasukkan: {i}")

#======
def no3():
  nilai = Stack()
  for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
        print(f"mencoba memasukkan: {i}")
    elif i % 4 == 0:
        print(f"pop item teratas {nilai.peek()}")
        nilai.pop()
    else:
        print(f"memeriksa {i}")
    print(nilai.items)

#=======================================================
class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)
    
    def getFrontMost(self):
        """
        Mengembalikan item yang paling depan tanpa menghapusnya.
        """
        if self.isEmpty():
            return None
        return self.qlist[0]

    def getRearMost(self):
        """
        Mengembalikan item yang paling belakang tanpa menghapusnya.
        """
        if self.isEmpty():
            return None
        return self.qlist[-1]
      
#=======================================================
class PriorityQueue(object):
  def __init__(self):
      self.qlist = []

  def __len__(self):
      return len(self.qlist)

  def isEmpty(self):
      return len(self) == 0

  def enqueue(self, data, priority):
      entry = PriorityQEntry(data, priority)  # Memanggil object _PriorityQEntry
      self.qlist.append(entry)

  def dequeue(self):
    """
      Menghapus dan mengembalikan item dengan prioritas tertinggi dari antrian.
      Jika terdapat beberapa item dengan prioritas tertinggi yang sama,
      item yang lebih dulu masuk akan diambil terlebih dahulu (FIFO).
      """
    if self.isEmpty():
        return None
    else:
        # Mencari item dengan prioritas tertinggi
        highest_priority = min(self.qlist, key=lambda entry: entry.priority)
        index = self.qlist.index(highest_priority)

        # Jika terdapat beberapa item dengan prioritas tertinggi yang sama,
        # ambil item yang lebih dulu masuk (FIFO)
        same_priority_items = [entry for entry in self.qlist if entry.priority == highest_priority.priority]
        dequeued_item = same_priority_items.pop(0)

        self.qlist.pop(index)
        return dequeued_item.item
    
  def getFrontMost(self):
    """
    Mengembalikan item dengan prioritas tertinggi (paling depan) tanpa menghapusnya dari antrian.
    """
    if self.isEmpty():
        return None
    else:
        # Mencari item dengan prioritas tertinggi
        highest_priority = min(self.qlist, key=lambda entry: entry.priority)
        return highest_priority.item

  def getRearMost(self):
    """
    Mengembalikan item dengan prioritas terendah (paling belakang) tanpa menghapusnya dari antrian.
    """
    if self.isEmpty():
        return None
    else:
        # Mencari item dengan prioritas terendah
        lowest_priority = max(self.qlist, key=lambda entry: entry.priority)
        return lowest_priority.item

class PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority
        
#=======================================================

# testcases

print(cetakHexa(12))
print(cetakHexa(31))
print(cetakHexa(229))
print(cetakHexa(255))
print(cetakHexa(31519))
print("---------")
print(cetakHexa2(12))
print(cetakHexa2(31))
print(cetakHexa2(229))
print(cetakHexa2(255))
print(cetakHexa2(31519))
print("---------")

#------------------------
no2()
print("---------")
no3()
#------------------------

