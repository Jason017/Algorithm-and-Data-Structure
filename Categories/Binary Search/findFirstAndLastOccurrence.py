# https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/
# Find first and last positions of an element in a sorted array


# Solution 1: Recursive Implementation of Binary Search Solution
# O(log(n)) O(log(n))
def first(arr, low, high, target):
    if low <= high:
        mid = (high+low)//2
        if mid == 0 or target > arr[mid-1] and arr[mid] == target:
            return mid
        elif target > arr[mid]:
            return first(arr, mid+1, high, target)
        else:
            return first(arr, low, mid-1, target)
    return -1


def last(arr, low, high, target):
    if low <= high:
        mid = (low+high)//2
        if mid == len(arr)-1 or target < arr[mid+1] and arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return last(arr, low, mid-1, target)
        else:
            return last(arr, mid+1, high, target)
    return -1


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(first(arr, 0, len(arr)-1, target))
print(last(arr, 0, len(arr)-1, target))


# Solution 2: Iterative Implementation of Binary Search Solution
# O(log(n)) O(1)
def first(arr, target):
    low, high = 0, len(arr)-1
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            res = mid
            high = mid - 1
    return res


def last(arr, target):
    low, high = 0, len(arr)-1
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(first(arr, target))
print(last(arr, target))
