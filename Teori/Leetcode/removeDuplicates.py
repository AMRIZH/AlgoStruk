# problem 26
def removeDuplicates(nums):
    """
    menghitung jumlah elemen unik dalam list nums
    :type nums: List[int]
    :rtype: int
    """
    if not nums: # jika nums kosong
        return 0 # return 0
    
    unique_index = 0 # inisialisasi unique_index
    
    for i in range(1, len(nums)): # iterate through the list nums starting from the second element (index 1)
        if nums[i] != nums[unique_index]: # if nums[i] is different from the last unique element (nums[unique_index])
            unique_index += 1 # increment unique_index
            nums[unique_index] = nums[i] # place nums[i] at the new unique index position (nums[unique_index] = nums[i])
    
    return unique_index + 1 # return the number of unique elements in nums
  
"""Here's how the code works:

    First, we check if the input list nums is empty. If it is, we return 0 because there are no unique elements.
    We initialize a variable unique_index to 0. This variable will keep track of the index where the next unique element should be placed.
    We iterate through the list nums starting from the second element (index 1). This is because the first element is always unique, so we can use nums[0] as the first unique element.
    For each element nums[i], we check if it is different from the last unique element (nums[unique_index]).
    If nums[i] is different from nums[unique_index], it means we have found a new unique element. We increment unique_index and place nums[i] at the new unique index position (nums[unique_index] = nums[i]).
    After the loop finishes, unique_index will be pointing to the index of the last unique element in the modified nums list.
    We return unique_index + 1 as the number of unique elements in nums.

This algorithm has a time complexity of O(n), where n is the length of the input list nums. We iterate through the list once to identify and place unique elements. The space complexity is O(1) because we only use a constant amount of extra space to store the unique_index variable.
"""
# TEST CASE
print(removeDuplicates([1, 1, 2]))  # Output: 2, nums = [1, 2, _]
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
print(removeDuplicates([]))  # Output: 0
print(removeDuplicates([1, 2, 3, 4]))  # Output: 4, nums = [1, 2, 3, 4]