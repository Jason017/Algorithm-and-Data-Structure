# March 1st: Distribute Candies
# March 2nd: Set Mismatch

# March 3rd: Missing Number
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
