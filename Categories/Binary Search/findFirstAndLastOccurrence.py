# https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-numsay/
# Find first and last positions of an element in a sorted numsay


# Solution 1: Recursive Implementation of Binary Search Solution
# O(log(n)) O(log(n))
def first(nums, l, r, target):
    if l <= r:
        m = (l + r) // 2
        if target > nums[m - 1] or m == 0 and nums[m] == target:
            return m
        elif target > nums[m]:
            return first(nums, m+1, r, target)
        else:
            return first(nums, l, m-1, target)
    return -1


def last(nums, l, r, target):
    if l <= r:
        m = (l + r) // 2
        if target < nums[m + 1] or m == len(nums)-1 and nums[m] == target:
            return m
        elif target < nums[m]:
            return last(nums, l, m-1, target)
        else:
            return last(nums, m+1, r, target)
    return -1


nums = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(first(nums, 0, len(nums)-1, target))
print(last(nums, 0, len(nums)-1, target))


# Solution 2: Iterative Implementation of Binary Search Solution
# O(log(n)) O(1)
def first(nums, target):
    l, r = 0, len(nums)-1
    res = -1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            res = m
            r = m - 1
    return res


def last(nums, target):
    l, r = 0, len(nums)-1
    res = -1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            res = m
            l = m + 1
    return res


nums = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(first(nums, target))
print(last(nums, target))
