def missingNumber(nums):
    return sum(range(1,len(nums)+1)) - sum(nums)

nums = [1,3,5,7,2,4,6,8,0]
print(missingNumber(nums))