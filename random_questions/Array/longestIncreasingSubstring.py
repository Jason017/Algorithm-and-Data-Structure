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

# Find all increasing substring
def findIncreasingSubstring(nums):
    output = [[nums[0]]]
    idx = 0
    for i in range(1, len(nums)):
        if nums[i-1] <= nums[i]:
            output[idx].append(nums[i])
        else:
            idx += 1
            output.append([nums[i]])
    return output

nums = [5, 6, 3, 5, 7, 8, 9, 1, 2]
print(findIncreasingSubstring(nums))