def findDuplicateNumber(nums):
    ans, prev = nums[0], nums[0]

    for num in nums[1:]:
        ans ^= num
        if ans == prev:
            return num
        prev = ans
    return -1
