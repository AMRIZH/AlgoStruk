# problem 66. Plus One
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    n = len(digits) # length of the digits list
    
    # Start from the least significant digit
    for i in range(n - 1, -1, -1): # iterate through the digits list in reverse order
        # If the current digit is less than 9, we can increment it and return
        if digits[i] < 9: # if the current digit is less than 9
            digits[i] += 1 # increment the current digit by 1
            return digits # return the modified digits list
        
        # Otherwise, set the current digit to 0 and move to the next digit
        digits[i] = 0  # set the current digit to 0
    
    # If we reach here, it means all digits were 9
    # We need to create a new list with an extra digit at the beginning
    result = [1] + [0] * n  # create a new list with an extra digit 1 at the beginning
    return result # return the new list

"""Here's how the code works:

    We start by iterating over the digits list from the least significant digit to the most significant digit (right to left).
    For each digit, we check if it is less than 9. If it is, we increment that digit by 1 and return the modified digits list.
    If the digit is 9, we set it to 0 and move to the next digit (more significant digit).
    If we reach the end of the loop and all digits were 9 (e.g., [9, 9, 9]), we create a new list with an extra digit 1 at the beginning (e.g., [1, 0, 0, 0]) and return it.

This algorithm has a time complexity of O(n), where n is the number of digits in the input list. We iterate through the list once to increment the number. The space complexity is O(n) because we create a new list of size n+1 in the worst case.
"""
# TEST CASE
print(plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(plusOne([9]))  # Output: [1, 0]
print(plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]


# improved code
def plusOne(digits) :
    carry, result = 1, []
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits