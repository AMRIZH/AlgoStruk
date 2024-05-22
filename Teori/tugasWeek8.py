# how many smaller numbers of the current number
def smallerNumbersThanCurrent(nums):
  newList = [] #store the number of smaller number list
  for i in nums : # iterate through numbers in nums
    k = 0 # the smaller number count
    # count how much smaller number than the current number
    for j in nums : 
      if j < i :
        k+=1
    newList.append(k) # add the counting into the list
  return newList

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))
nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))
nums = [7,7,7,7]
print(smallerNumbersThanCurrent(nums))

print("=====================================")

# problem 1051 height checker

def heightChecker(heights):
  sortedHeights = sorted(heights) # sort the heights
  count = 0 # count the number of different height
  for i in range(len(heights)) : # iterate through the heights
    if heights[i] != sortedHeights[i] : # check if the height is different
      count+=1
  return count

# test case
heights = [1,1,4,2,1,3]
print(heightChecker(heights)) # 3
heights = [5,1,2,3,4]
print(heightChecker(heights)) # 5
heights = [1,2,3,4,5]
print(heightChecker(heights)) # 0

