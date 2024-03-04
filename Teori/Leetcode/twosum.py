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
