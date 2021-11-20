def missingNumber(nums):
    return len(nums)*(len(nums)+1)//2 - sum(nums)

nums = [1,3,5,7,2,4,6,8,0]
print(missingNumber(nums))