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
      
#====================================================
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


class PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority
        