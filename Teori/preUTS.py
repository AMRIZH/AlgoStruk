class nsabah(object):
  """Class Nasabah Bank"""
  def __init__(self, nama, saldo, alamat):
    self.nama = nama
    self.saldo = saldo
    self.alamat = alamat
  
  def cekSaldo(self):
    print(self.saldo)
  
  def debit(self, nominal):
    self.saldo += nominal
    
  def kredit(self, nominal):
    self.saldo -= nominal
    
  def transfer(self, nominal, nasabah):
    self.kredit(nominal)
    nasabah.debit(nominal)
  
  def pindahAlamat(self, alamat):
    self.alamat = alamat
    
  def cekAlamat(self):
    print(self.alamat)
    
  def tutupRekening(self):
    self.saldo = 0
    self.alamat = None
    self.nama = None
    
    
def fibonacci(index):
  if index == 1: # base case
    return 0
  elif index == 2:
    return 1
  else:
    return fibonacci(index-1) + fibonacci(index-2) # recursion case
  
def factorial(index):
  if index == 1: # base case
    return 1
  else:
    return index * factorial(index-1) # recursion case