class Vehicle (object) :
  """This is Vehicla class"""
  def __init__(self,merk,year,milleage,type) :
    self.name = merk
    self.year = year
    self.capacity = 0
    self.milleage = milleage
    self.type = type
    
  def setCapacity(self,capacity) :
    self.capacity = capacity
    
  def printInfo(self):
    print("Type :", self.type,"\nName :", self.name,"\nYear :", self.year,"\nCapacity :", self.capacity,"Person\nMilleage :",self.milleage,"Km")
    
class Truck(Vehicle):
  """Truck is a Big Loader Vehicle"""
  def __init__(self,merk,year,milleage) :
    self.name = merk
    self.year = year
    self.capacity = 0
    self.milleage = milleage
    self.type = "Truck"

    
a = Truck("Hino", 2004, 2000)
a.setCapacity(3)
a.printInfo()

b = Truck("Carry", 2005,1000)
b.setCapacity(4)
b.printInfo()
