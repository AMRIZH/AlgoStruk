# problem 342: Power of Four
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

def isPowerOfFour(num):
    if num == 0:
        return False
    while num % 4 == 0:
        num /= 4
    return num == 1