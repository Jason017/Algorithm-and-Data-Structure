def findContinuousNum(nums):
    r = []
    right = left = 0
    for i in nums + [float('inf')]:
        if i-1 == right:
            right += 1
        else:
            if right:
                if left < right:
                    # r.append('%s-%s' % (left, right))
                    r.append(list(range(left, right+1)))
                else:
                    # r.append(str(right))
                    r.append([right])
            left = right = i
    # return '(%s)' % ', '.join(r)
    return len(r)

nums1 = [2, 3, 4, 5, 20, 13, 14, 15, 16, 17, 20]
nums2 = [-4,-3,-1,3,4,7,8]
nums3 = [17,20,34,45,46]
nums4 = [4,6]
print(findContinuousNum(nums1))
print(findContinuousNum(nums2))
print(findContinuousNum(nums3))
print(findContinuousNum(nums4))


def consecutiveSegments(nums):
    n = len(nums)
    if n <= 1:
        return n

    x = nums[0]
    ans = 1
    for i in range(1, n):
        if nums[i] != x+1:
            ans += 1
        x = nums[i]
    return ans

nums1 = [2, 3, 4, 5, 20, 13, 14, 15, 16, 17, 20]
nums2 = [-4,-3,-1,3,4,7,8]
nums3 = [17,20,34,45,46]
nums4 = [4,6]

print(consecutiveSegments(nums1))
print(consecutiveSegments(nums2))
print(consecutiveSegments(nums3))
print(consecutiveSegments(nums4))


