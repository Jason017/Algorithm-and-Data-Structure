def wave(nums):
    nums.sort()
    for i in range(0, len(nums)-1, 2):
        nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

print(wave([1,5,2,10,8]))
