def cetakSiku(x) :
  for i in range(x+1) :
    print("*"*i)

# testcase
cetakSiku(5)

#=======================
def segi4(y,x) :
  print("@"*x)
  for i in range(y-2) :
    print("@"+ " "*(x-2) +"@")
  print("@"*x)

#testcase
segi4(4,5)

#=======================
def jumlahVokal(kata) :
  vocal = ("a","i","u","e","o")
  v = 0
  for i in kata :
    if i.lower() in vocal :
      v +=1
  return len(kata),v

#testcase
print("huruf/vokal =",jumlahVokal("Surakarta"))

def jumlahKonsonan(kata) :
  konsonan = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
  k = 0
  for i in kata :
    if i.lower() in konsonan :
      k +=1
  return len(kata), k

#testcase
print("huruf/konsonan =",jumlahKonsonan("Surakarta"))

#=========================================
def rerata(lis) :
  k = sum(lis)
  return k/len(lis)

#testcase
l1 = [1,2,3,4,5]
l2 = [3,4,5,4,3,4,5,2,2,10,11,23]
print("mean =",rerata(l1))
print("mean =",rerata(l2))

#=====
def variance(lis) :
  n = len(lis)
  if n < 2:
    raise ValueError("Variance requires at least two data points")
  mean = rerata(lis)
  variance = sum((xi - mean) ** 2 for xi in lis) / (n - 1)
  return variance

def stdev(lis):
    import math
    return math.sqrt(variance(lis))

#testcase
print("variance =", variance(l1))
print("variance =",variance(l2))
print("standar deviasi =",stdev(l1))
print("standar deviasi =",stdev(l2))

#=============================================
