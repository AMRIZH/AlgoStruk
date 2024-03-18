

# import numpy as np
string = "I love to learn python"
def longest(string):
  k = 0 # data holder to store len of longest string
  long = "" # data holder to store the lonest string
  pisah = string.split() # split the string into list of string
  for i in pisah : # check every string
    if len(i) > k : # if string is longer than the previous string
      k = len(i) # store the len of the string
      long = i # store the longer the string
  print ("the longest word is",long) #print the longest string

longest(string)

angka = [1,2,3,4,5,6,8,9,10]
# def missing(angka):
#   sepuluh = (1,2,3,4,5,6,7,8,9,10)
#   for i in angka :
#     if i not in sepuluh :
#       return i
      
# print(missing(angka))

# def missing2(angka):
#   sepuluh = [1,2,3,4,5,6,7,8,9,10]
#   for i in angka :
#     sepuluh.remove(i)
#     return sepuluh
  
# print(missing2(angka))

def missing3(angka): 
  return 55 - sum(angka) 
print(missing3(angka))

def longest2(string):
    print(max(string.split(" "), key=len))
longest2(string)