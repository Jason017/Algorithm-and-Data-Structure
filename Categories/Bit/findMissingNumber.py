def findMissingNumber(nums, n):
    ans = 0
    for i in range(1, n + 1):
        ans ^= i

    for num in nums:
        ans ^= num

    return ans


def find_missing(nums, n):
    ans = 0

    for num in range(1, n + 1):
        ans += num

    for num in nums:
        ans -= num

    return ans
