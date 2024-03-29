# Two Pointers
# https://www.geeksforgeeks.org/longest-subsegment-1s-formed-changing-k-0s/

def flipZeros(nums, k):
    cnt0 = mx = left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            cnt0 += 1
        while cnt0 > k:
            if nums[left] == 0:
                cnt0 -= 1
            left += 1
        mx = max(mx, right - left + 1)
    return mx

nums = [1, 0, 0, 1, 1, 0, 1]
k = 1
print(flipZeros(nums, k))


# https://www.geeksforgeeks.org/maximum-length-of-consecutive-1s-or-0s-after-flipping-at-most-k-characters/
def flipAny(nums, k):
    def getMax(toFlip):
        ans = -1
        cnt = left = 0
    
        for right in range(len(nums)):
            if nums[right] == toFlip:
                cnt += 1
            while cnt > k:
                if nums[left] == toFlip:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    return max(getMax(0), getMax(1))


nums = [1, 0, 0, 1]
k = 1
print(flipAny(nums, k))
