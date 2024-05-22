# problem 27 Remove Element
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0  # k will store the number of elements not equal to val
    
    for i in range(len(nums)): # iterate through the list nums
        if nums[i] != val: # if nums[i] is not equal to val
            nums[k] = nums[i] # place nums[i] at index k
            k += 1 # increment k
    
    return k # return the number of elements not equal to val

"""Here's how the code works:

    We initialize a variable k to 0. This variable will keep track of the number of elements in nums that are not equal to val.
    We iterate through the list nums using a for loop.
    For each element nums[i], we check if it is not equal to val.
    If nums[i] is not equal to val, we assign it to nums[k] and increment k by 1.
    After the loop finishes, k will be the number of elements in nums that are not equal to val.
    We return k.

This algorithm has a time complexity of O(n), where n is the length of the input list nums. We iterate through the list once to identify and place elements not equal to val. The space complexity is O(1) because we only use a constant amount of extra space to store the variable k.
"""

# TEST CASE
print(removeElement([3, 2, 2, 3], 3))  # Output: 2, nums = [2, 2, _, _]
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # Output: 5, nums = [0, 1, 4, 0, 3, _, _, _]
print(removeElement([1, 2, 3, 4, 5], 6))  # Output: 5, nums = [1, 2, 3, 4, 5]
print(removeElement([], 0))  # Output: 0