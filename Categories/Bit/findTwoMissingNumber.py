def findTwoMissingNumber(nums, n):
    ans = fir = sec = 0
    i, j = 1, 0

    while i < n + 1 and j < len(nums) - 1:
        ans ^= nums[j] ^ i
        if ans != 0:
            if fir == 0:
                fir = i
                i = nums[j]
                ans = 0
            else:
                sec = i
                return (fir, sec)
        else:
            j += 1
            i += 1
    return (-1, -1)


print(findTwoMissingNumber([1, 3, 5, 6], 6))  # 2 4
print(findTwoMissingNumber([1, 2, 3, 4, 5], 5))  # -1 -1
