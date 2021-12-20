# https://stackoverflow.com/questions/43017251/solve-almostincreasingsequence-codefights/43017981
def almostIncreasingSequence(nums):
    def helper(nums):
        idx = -1
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return i
        return idx
    
    idx = helper(nums)
    if idx == -1:
        return True
    if helper(nums[:idx] + nums[idx+1:]) == -1:
        # Deleting an ealier element that goes down
        return True
    if helper(nums[:idx+1] + nums[idx+2:]) == -1:
        # Deleting a later element that goes down
        return True
    return False
    
nums = [10,1,2,3,4,5]
print(almostIncreasingSequence(nums)) # True
nums = [1,2,3,4,5,-10]
print(almostIncreasingSequence(nums)) # True
nums = [1,2,3,4,3,6]
print(almostIncreasingSequence(nums)) # True
nums = [1,2,3,4,99,5,6]
print(almostIncreasingSequence(nums)) # True
nums = [1,2,3]
print(almostIncreasingSequence(nums)) # True
nums = [1,3,2]
print(almostIncreasingSequence(nums)) # True
nums = [1,2,2,3]
print(almostIncreasingSequence(nums)) # True
nums = [1,3,2,1]
print(almostIncreasingSequence(nums)) # False
nums = [3,2,1]
print(almostIncreasingSequence(nums)) # False

