class Vehicle (object) :
  """This is Vehicla class"""
  def __init__(self,merk,year,milleage,type) : #initialize vehicle object
    self.name = merk
    self.year = year
    self.capacity = 0 # initial capacity is zero, must be defined later
    self.milleage = milleage
    self.type = type
    
  def setCapacity(self,capacity) : # change the vehicle capacity
    self.capacity = capacity
    
  def printInfo(self): # print information about the vehicle
    print("Type :", self.type,"\nName :", self.name,"\nYear :", self.year,"\nCapacity :", self.capacity,"Person\nMilleage :",self.milleage,"Km")
    
class Truck(Vehicle): # trcuk is inheritance from Vehicle
  """Truck is a Big Loader Vehicle"""
  def __init__(self,merk,year,milleage) : # initialize truck object
    self.name = merk
    self.year = year
    self.capacity = 0
    self.milleage = milleage
    self.type = "Truck" # type of vehicle is already defined
  # truck class inherit all vehicle attributes & methods

    
# a = Truck("Hino", 2004, 2000) # initialize new truk
# a.setCapacity(3) # set capacity of the vehicle
# a.printInfo() # show all information

# b = Truck("Carry", 2005,1000) # initialize new truk
# b.setCapacity(4)
# b.printInfo()

#=================================================
from math import sqrt
class position(object):
  def __init__(self,X,Y): # initiating new position with certain X and Y
    self.X = X 
    self.Y = Y
    
  def setLocation(self,X,Y): # change the position coordinate
    self.X = X
    self.Y = Y
    
  def distanceFromOrigin(self):
        return sqrt(self.X**2 + self.Y**2) # using pytagoras to calculate distance from origin

  def distance(self, position1, position2):
      dx = position1.X - position2.X # define selish jarak antar X
      dy = position1.Y - position2.Y #define selish jarak antar Y
      return sqrt(dx**2 + dy**2) # define the distance using pytagoras

bendera = position(4,3)
print(bendera.distanceFromOrigin()) # 3,4,5 is one of fast pytagoras rule
mimbar = position(10,3)
print(mimbar.distance(mimbar,bendera)) # compare the distance between bendera and mimbar
# (10,3) - (4,3) = 10 -4 = 6 --> the distance is 6



