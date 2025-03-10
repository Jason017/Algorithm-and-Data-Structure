def binary_search(nums, target):
    l, r = 0, len(nums)-1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

def leftmost_bound_binary_search(nums, target):
    l, r = 0, len(nums)-1

    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    if l <= len(nums) - 1 and nums[l] == target:
        return l
    else:
        return -1

def rightmost_bound_binary_search(nums, target):
    l, r = 0, len(nums)-1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1

    if r >= 0 and nums[r] == target:
        return r
    else:
        return -1

print(binary_search([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 8)) # 3
print(leftmost_bound_binary_search([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2)) # 1
print(rightmost_bound_binary_search([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2)) # 4