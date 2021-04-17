def sumOfTwoArr(a,b,v):
    diff = set()
    for i in range(len(a)):
        d = v-a[i]
        diff.add(d)
    for i in range(len(b)):
        if b[i] in diff:
            return True
    return False

# Brute Force:
# 
# def sumOfTwoArr(a,b,v):
#     for i in range(len(a)):
#         diff_value = v-a[i]
#         for j in range(len(b)):
#             if b[j] == diff_value:
#                 return True
#     return False

a = [0,0,-5,3203]
b = [-10,40,-3,9]
v = -8
print(sumOfTwoArr(a,b,v))

# Kadane's Algorithm
# Find largest sum of any contiguous subarray
def maxSubarraySum(arr):
    curr_max, best_max = arr[0], arr[0]
    for i in arr[1:]:
        curr_max = max(i, curr_max+i)
        best_max = max(curr_max, best_max)
    return best_max

arr = [5,10,-5,14,-3,8,4,1,-2,-1]
a = [-2,-3,4,-1,-2,1,5,-3]
print(maxSubarraySum(arr))
