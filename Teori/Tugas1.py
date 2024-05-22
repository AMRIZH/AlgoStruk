def isPrime(x):
    if x < 2: # 1 , zero , negative number is not prime 
        print("Not prime")
    elif x == 2: # 2 is prime number
        print("Prime")
    elif x % 2 == 0: # even number is not prime 
        print("Not prime")
    # checks all even numbers from 3 to the root of x, with rounding.
    else:
        for i in range(3, int(x ** 0.5) +1 , 2): 
            if x % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")

# testcases 1
isPrime(-15) # negative number
isPrime(-1) # negative number
isPrime(0) # zero
isPrime(2) # prime
isPrime(3) # prime
isPrime(4)
isPrime(5) # prime
isPrime(7) # prime
isPrime(11) # prime
isPrime(15) 
isPrime(21)
isPrime(41) # prime
isPrime(49) 
isPrime(100)

#============================================================          
def removeRepetition(x):
  data = [] # creating new empty list
  for i in x :
    if i not in data : # check if the elements is repeated
      data.append(i) # if not repeated , then put the element into the new list
  print(data) # print the new list

# testcases 2
removeRepetition([1,2,3,4,5,6,7,8]) # unrepeated list
removeRepetition([2,2,3,4,4,5,5,5,6,7,7]) # list with repetition
removeRepetition(["a", "b", "c", "c", "d", "d" ,"e", "f"]) # list with repetition
removeRepetition([1,2,2,4,4,"a","a","b","",[2,3]]) # list with repetition and mixed data type
removeRepetition([]) # empty list

#===========================================================
def sumInt(x) :
  if x > 1 : 
    return x + sumInt(x-1) #if x is higher than 1, then the recursive is gradually down until 1
  elif x < 1 :
    return x + sumInt(x+1) #if x is lower than 1, then the recursive is gradually rise until 1
  else :
    return 1 # if x is 1, return 1

print(sumInt(-5)) # (-5)+(-4)+(-3)+(-2)+(-1)+(0)+(1) = -14
print(sumInt(-1)) # (-1)+(0)+(1) = 0
print(sumInt(0)) # (0)+(1) = 1
print(sumInt(1)) # (1) = 1
print(sumInt(5)) # (5)+(4)+(3)+(2)+(1) = 15
print(sumInt(10)) # (10)+(9)+(8)+(7)+(6)+(5)+(4)+(3)+(2)+(1) = 55