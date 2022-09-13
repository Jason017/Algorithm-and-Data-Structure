# https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6
from collections import deque


# find the first element smaller than current either in the left
# (from pushing in) or in the right (from popping out);


def monotonic_increasing_queue(nums):
    q = deque()

    for i, v in enumerate(nums):
        while q and nums[q[-1]] >= v:
            q.pop()
        q.append(i)
    return list(q)


def monotonic_decreasing_queue(nums):
    q = deque()

    for i, v in enumerate(nums):
        while q and nums[q[-1]] <= v:
            q.pop()
        q.append(i)
    return list(q)


nums = [5, 3, 1, 2, 4]
print("monotonic increasing queue:", monotonic_increasing_queue(nums))
print("monotonic decreasing queue:", monotonic_decreasing_queue(nums))


# monotonic increasing
def firstSmallerElement(nums):
    q = deque()
    firstSmallerToLeft = [-1]*len(nums)
    firstSmallerToRight = [-1]*len(nums)
    for i, v in enumerate(nums):
        while q and nums[q[-1]] >= v:  # right is from the popping out
            firstSmallerToRight[q.pop()] = v
        if q:  # left is from the pushing in
            firstSmallerToLeft[i] = nums[q[-1]]
        q.append(i)
    print(q)
    return firstSmallerToLeft, firstSmallerToRight


nums = [5, 3, 1, 2, 4]
# nums = [2, 5, 3, 4, 3, 4, 5, 1, 1, 2]
res = firstSmallerElement(nums)
print("firstSmallerToLeft:", res[0])  # [-1, -1, -1, 1, 2]
print("firstSmallerToRight:", res[1])  # [3, 1, -1, -1, -1]


# monotonic decreasing
def firstLargerElement(nums):
    q = deque()
    firstLargerToLeft = [-1]*len(nums)
    firstLargerToRight = [-1]*len(nums)
    for i, v in enumerate(nums):
        while q and nums[q[-1]] <= v:
            firstLargerToRight[q.pop()] = v
        if q:
            firstLargerToLeft[i] = nums[q[-1]]
        q.append(i)
    print(q)
    return firstLargerToLeft, firstLargerToRight


nums = [5, 3, 1, 2, 4]
# nums = [2, 5, 3, 4, 3, 4, 5, 1, 1, 2]
res = firstLargerElement(nums)
print("firstLargerToLeft:", res[0])  # [-1, 5, 3, 3, 5]
print("firstLargerToRight:", res[1])  # [-1, 4, 2, 4, -1]
