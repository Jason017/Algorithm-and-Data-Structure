# https://www.techiedelight.com/count-strictly-increasing-sub-arrays/
def countIncreasingSubarrays(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j - 1] >= nums[j]:
                break
            count = count + 1
    return count

nums = [1,2,4,4,5]
# [1, 2], [1, 2, 4], [2, 4], [4, 5]
print(countIncreasingSubarrays(nums)) # 4
