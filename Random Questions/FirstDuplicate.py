def firstDuplicate(nums):
    for i in range(len(nums)):
        if nums[abs(nums[i])-1] < 0:
            return nums[abs(nums[i])]
        nums[abs(nums[i])-1] *= -1
    return -1