from math import log
import bisect

def findKLargest(nums, k):
    arr = []
    for _ in range(k): 
        mx = float('-inf')
        for j in range(len(nums)):
            if nums[j] > mx:
                mx = nums[j]
        nums.remove(mx)
        arr.append(mx)
          
    return arr[-1]

nums = [1000,298,3579,100,200,-45,900]
k = 2
print(findKLargest(nums, k))


def find_k_largest_sort(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k-1]

def find_k_largest_remove_max(nums, k):
    for _ in range(k-1):
        nums.remove(max(nums))
    return max(nums)

def find_k_largest_element(nums, k):
    window = nums[:k]
    for element in nums[k:]:
        if element > window[0]:
            # Remove minimum from window
            window = window[1:]
            # Sorted insert of new element
            bisect.insort(window, element)
    return window[0]

print(find_k_largest_sort(nums, k))
print(find_k_largest_remove_max(nums, k))
print(find_k_largest_element(nums, k))
