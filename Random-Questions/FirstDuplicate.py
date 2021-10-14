# O(1) Solution
def firstDuplicate(nums):
    for i in nums:
        if nums[abs(i)-1] < 0:
            return abs(i)
        nums[abs(i)-1] *= -1


nums1=[1,0,3,6,5,1,6,7,8,9,5]
nums2=[2,3,1,3,6,6]

# Only when nums[i] >= 0

print(firstDuplicate(nums1))
print(firstDuplicate(nums2))


