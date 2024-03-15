# import numpy as np
string = "I love to learn python"
def longest(string):
  k = 0
  long = ""
  pisah = string.split()
  for i in pisah :
    if len(i) > k :
      k = len(i)
      long = i
  print ("the longest word is",long)
  
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