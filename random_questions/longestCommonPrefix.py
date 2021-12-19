# https://afteracademy.com/blog/longest-common-prefix


# Divide and Conquer
def commonPrefix(left_str, right_str):
    n = min(len(left_str), len(right_str))
    for i in range(n):
        if left_str[i] != right_str[i]:
            return left_str[:i]
    return left_str[:n]

def longestCommonPrefix(arr, left, right):
    if (left == right):
        return arr[left]
    else:
        mid = (left + right)//2
        left_lcp = longestCommonPrefix(arr, left , mid)
        right_lcp = longestCommonPrefix(arr, mid + 1, right)
        return commonPrefix(left_lcp, right_lcp)

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
print("LCP:",longestCommonPrefix(arr, 0, len(arr)-1))



# Binary Search
def allContainsPrefix(arr, str, start, end):
    for i in range(0, len(arr)):
        word = arr[i]
        for j in range(start, end + 1):
            if word[j] != str[j]:
                return False
    return True
  
def longestCommonPrefix(arr):
    index = len(min(arr, key = len))
    prefix = ""   
    low, high = 0, index - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if allContainsPrefix(arr, arr[0], low, mid):
            prefix = prefix + arr[0][low:mid + 1]
            low = mid + 1
        else: 
            high = mid - 1
    return prefix

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
print("LCP:",longestCommonPrefix(arr))

