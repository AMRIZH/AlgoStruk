# problem 1365 - How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.

def smallerNumbersThanCurrent(nums):
    result = []
    for i in nums:
        count = 0
        for j in nums:
            if j < i:
                count += 1
        result.append(count)
    return result