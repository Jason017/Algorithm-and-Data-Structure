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
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

print(findDuplicate1([3,7,4,1,2,0,7,6]))