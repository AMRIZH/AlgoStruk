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

#=============================================================

class StackLL(object):
  def __init__(self):
      self.top = None
      self.size = 0

  def isEmpty(self):
      return self.top is None

  def __len__(self):
      return self.size

  def peek(self):
      assert not self.isEmpty(), "Tidak bisa diintip. Stack kosong."
      return self.top.item

  def pop(self):
      assert not self.isEmpty(), "Tidak bisa pop dari stack kosong."
      node = self.top
      self.top = self.top.next
      self.size -= 1
      return node.item

  def push(self, data):
      self.top = _StackNode(data, self.top)
      self.size += 1


class _StackNode(object):  # Ini adalah kelas privat
  def __init__(self, data, link):  # untuk menyimpan data. Dia
      self.item = data  # dipanggil oleh class StackLL

#========================================================
def cetakBiner(d):
  f = Stack()  # Atau: f = StackLL()
  if d == 0:
      f.push(0)
  while d != 0:
      sisa = d % 2
      d = d // 2
      f.push(sisa)
  st = ""
  for i in range(len(f)):
      st = st + str(f.pop())
  return st

#========================================================
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

