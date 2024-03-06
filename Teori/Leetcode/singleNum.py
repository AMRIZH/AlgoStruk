#gagal
def singleNumber(nums) :
    long = len(nums)
    for i in range(long+1) :
        if nums[i] not in nums[i:long-1] :
            return nums[i]

#sukses  
def singleNumber(nums):
    hasil = 0
    for num in nums:
        hasil ^= num 
    return hasil

# opertaor ^ merupakan implementasi gerbang XOR 
# dimana ^ akan membagi bilangan tersebut bila divisible
# bilangan akan dikali jika un-divisible