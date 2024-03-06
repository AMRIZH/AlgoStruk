# problem 1009
def findComplement(angka) :
  binary = bin(angka)[2:]
  complement = ""
  for i in binary :
    if i == "0" : 
      complement += "1"
    else : 
      complement += "0"
  return int(complement,2)

print(findComplement(10))