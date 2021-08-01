# Floyd's tortoise and hare
# Solve findDuplicate in linear time and constant space
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr2


# Using HashMap
def findDuplicate1(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True


def findDuplicate2(nums):
    for i in range(len(nums)):
        if nums[abs(nums[i])-1] < 0:
            return nums[abs(nums[i])]
        nums[abs(nums[i])-1] *= -1

print(findDuplicate2([3,1,4,4,2]))