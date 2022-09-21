# https://leetcode.com/problems/longest-increasing-subsequence/
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/#:~:text=The%20Longest%20Increasing%20Subsequence%20(LIS)%20problem%20is%20to%20find%20the,50%2C%2060%2C%2080%7D.
def longestIncreasingSubsequence(nums):
    n = len(nums)
    dp = [1] * n

    for l in range(n - 1):
        for r in range(l + 1, n):
            if nums[r] > nums[l]:
                dp[r] = max(dp[r], dp[l] + 1)
    return max(dp)


nums1 = [3, 10, 2, 1, 20]
nums2 = [3, 2]
nums3 = [50, 3, 10, 7, 40, 80]
nums4 = [4, 10, 4, 3, 8, 9]
nums5 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
nums6 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
nums7 = [10, 9, 2, 5, 3, 7, 101, 18]
nums8 = [0, 1, 0, 3, 2, 3]
nums9 = [7, 7, 7, 7, 7, 7, 7]
nums10 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
nums11 = [4, 10, 4, 3, 8, 9]
nums12 = [1, 2, 0, 4, 4, 7, 5]

print(longestIncreasingSubsequence(nums1))  # 3
print(longestIncreasingSubsequence(nums2))  # 1
print(longestIncreasingSubsequence(nums3))  # 4
print(longestIncreasingSubsequence(nums4))  # 3
print(longestIncreasingSubsequence(nums5))  # 6
print(longestIncreasingSubsequence(nums6))  # 6
print(longestIncreasingSubsequence(nums7))  # 4
print(longestIncreasingSubsequence(nums8))  # 4
print(longestIncreasingSubsequence(nums9))  # 1
print(longestIncreasingSubsequence(nums10))  # 6
print(longestIncreasingSubsequence(nums11))  # 3
print(longestIncreasingSubsequence(nums12))  # 4
