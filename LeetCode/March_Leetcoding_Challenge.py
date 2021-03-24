### March 1st: Distribute Candies
class Solution:
   def distributeCandies(self, candyType: List[int]) -> int:
      return min(len(candyType) //2, len(set(candyType)))


### March 2nd: Set Mismatch
# Approach 1:
class Solution:
   def findErrorNums(self, nums: List[int]) -> List[int]:
      ln, dup = len(nums), 0
      seen, aSum = [0]*(ln+1), ln*(ln+1)//2
      for num in nums:
         aSum -= num
         if seen[num]:
            dup = num
         seen[num] = 1
      return [dup, dup + aSum]
# Approach 2:
class Solution:
   def findErrorNums(self, nums):
      n = len(nums)
      A = -sum(nums) + n*(n+1)//2
      B = -sum(i*i for i in nums) + n*(n+1)*(2*n+1)//6
      return [(B-A*A)//2//A, (B+A*A)//2//A]


### March 3rd: Missing Number
# Approach 1:
class Solution:
   def missingNumber(self, nums: List[int]) -> int:
      for i in range(1,len(nums)+1):
         if i not in nums:
            return i
# Approach 2:
class Solution:
   def missingNumber(self, nums: List[int]) -> int:
      return sum(range(1,len(nums)+1)) - sum(nums)


### March 4th: Intersection of Two Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      currA, currB = headA, headB
      while currA != currB:
         if currA == None:
            currA = headB
         else:
            currA = currA.next
            
         if currB == None:
            currB = headA
         else:
            currB = currB.next
      return currA

### March 5th: Single-row Keyboard
# class Solution:




