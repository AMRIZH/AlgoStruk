class Stack(object):
  def __init__(self):  # Membuat stack kosong.
      self.items = []  # List untuk menyimpan stack.

  def isEmpty(self):  # Mengembalikan True kalau kosong,
      return len(self) == 0  # selain itu False

  def __len__(self):  # Mengembalikan banyaknya item di stack.
      return len(self.items)

  def peek(self):  # Mengembalikan nilai posisi atas tanpa menghapus.
      assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
      return self.items[-1]

  def pop(self):  # Mengembalikan nilai posisi atas lalu menghapus.
      assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
      return self.items.pop()

  def push(self, item):  # Mendorong item baru ke stack.
      self.items.append(item)
      
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
    
    def getFrontMost(self): # Peek : Mengembalikan item yang paling depan tanpa menghapusnya.
        if self.isEmpty():
            return None
        return self.qlist[0]

    def getRearMost(self): #Mengembalikan item yang paling belakang tanpa menghapusnya.
        if self.isEmpty():
            return None
        return self.qlist[-1]
      
    def cetak(self):
        print(self.qlist)

