# problem 367: Valid Perfect Square
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.

def isPerfectSquare(num):
    if num == 1:
        return True
    left, right = 1, num
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False