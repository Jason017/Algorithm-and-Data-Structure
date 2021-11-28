# Similar question: LeetCode 300.

def longestIncreasingSubstring(nums):
    curr = ans = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            curr += 1
        else:
            curr = 1
        ans = max(ans, curr)
    return ans
nums = [5, 6, 3, 5, 7, 8, 9, 1, 2]
print(longestIncreasingSubstring(nums))