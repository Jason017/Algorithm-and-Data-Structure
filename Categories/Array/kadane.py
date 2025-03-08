# Find largest sum of any contiguous subarray
def maxSubarraySum(nums):
    curr_max, best_max = nums[0], nums[0]
    for num in nums[1:]:
        curr_max = max(curr_max + num, num)
        best_max = max(curr_max, best_max)
    return best_max


nums = [5, 10, -5, 14, -3, 8, 4, 1, -2, -1]
print(maxSubarraySum(nums))
nums = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubarraySum(nums))
