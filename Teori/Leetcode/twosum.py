# problem 1
# latihan leetcode

nums = [2,7,11,15]
def twosum(nums, target) :
    for i in nums :
        for j in nums :
            if i + j == target :
                return i , j
    pass

def twosums(nums,target) :
    for i in range(len(nums)) :
        for j in range(len(nums)-1) :
            if nums[i]+nums[j+1] == target :
                return [i,j+1]
    pass

def twopsums(nums,target) :
    for i in range(len(nums)) :
        for j in range(i+1,len(nums)) :
            if nums[i]+nums[j] == target :
                return [i,j]
            
def twoSum(nums, target): # misal nums = [2,7,11,15], target = 9
    complement_map = {} # menyimpan nilai complement
    for i, num in enumerate(nums): # (0, 2), (1, 7), (2, 11), (3, 15)
        complement = target - num # 9-2=7, 9-7=2, 9-11=-2, 9-15=-6
        if complement in complement_map: # jika 7 ada di dalam complement_map
            return [complement_map[complement], i] # return [1, 0]
        complement_map[num] = i # complement_map[2] = 0, complement_map[7] = 1, complement_map[11] = 2, complement_map[15] = 3
    return [] # jika tidak ada pasangan yang ditemukan

# complement_map = {0:2, 1:7, 2:11, 3:15}

"""Here's how the code works:

    We create an empty dictionary complement_map to store the complement of each number and its index.
    We iterate through the list of numbers nums using enumerate() to get both the index i and value num.
    For each number num, we calculate its complement complement = target - num.
    We check if the complement exists as a key in the complement_map dictionary.
    If the complement exists, it means we have found the two numbers that add up to the target. We return their indices as a list: [complement_map[complement], i].
    If the complement does not exist, we store the current number num and its index i in the complement_map dictionary.
    If we iterate through the entire list without finding a solution, we return an empty list [].

This algorithm has a time complexity of O(n), where n is the length of the input list nums, because we iterate through the list once. The space complexity is also O(n) because we store at most n elements in the dictionary complement_map."""

# TEST CASE\
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(twoSum([3, 3], 6))          # Output: [0, 1]