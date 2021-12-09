# Find largest sum of any contiguous subarray
def maxSubarraySum(arr):
    curr_max, best_max = arr[0], arr[0]
    for i in arr[1:]:
        curr_max = max(curr_max + i, i)
        best_max = max(curr_max, best_max)
    return best_max

arr = [5,10,-5,14,-3,8,4,1,-2,-1]
print(maxSubarraySum(arr))
arr = [-2,-3,4,-1,-2,1,5,-3]
print(maxSubarraySum(arr))
