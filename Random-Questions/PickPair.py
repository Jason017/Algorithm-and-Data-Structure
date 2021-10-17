# https://www.geeksforgeeks.org/python-program-to-find-all-possible-pairs-with-given-sum/

class Solution:
    def findPairs(self,nums,target):
        nums.sort()
        cnt = 0
        low, high = 0, len(nums)-1
        while low < high:
            if nums[low] + nums[high] == target:
                cnt += 1
                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1
        return cnt

sol = Solution()
nums = [1,3,4,7,2,-1,7,4,3,0]; target=5
print(sol.findPairs(nums,target))