# https://github.com/Jason017/Algorithm-and-Data-Structure/blob/main/Random-Questions/findTotalWays.py
# https://www.geeksforgeeks.org/tabulation-vs-memoization/
# https://www.techiedelight.com/find-total-ways-reach-nth-stair-with-atmost-m-steps/

''' 
Find total ways to reach the n'th stair from the bottom
at most m steps at a time
'''

class Solution:
    ### Solution 1: recursion
    def totalWays(self, n, m):
        if n < 0:
            return 0

        if n == 0:
            return 1

        count = 0
        for i in range(1, m + 1):
            count += self.totalWays(n - i, m)

        return count

    ### Solution 2: memorization (Top-Down DP Approach)
    def totalWays(self, n, m):
        dp = [0] * (n+1)
        res = self.helper(n,m,dp)
        return res
    
    def helper(self, n, m, dp):
        # base case: invalid input
        if n < 0:
            return 0
    
        # base case: 1 way (with no steps)
        if n == 0:
            return 1
        
        # if the subproblem is not seen before
        if dp[n] == 0:
            for i in range(1, m+1):
                dp[n] += self.helper(n-i, m, dp)
        return dp[n]
    

    ### Solution 3: tabluation (Bottom-Up DP Approach)
    def totalWays(self, n, m):
        if n == 1 or m == 1:
            return 1

        dp = [0] * (n+1)
        # base case: 1 way (with no steps)
        dp[0] = 1
        # 1 way to reach the 1st stair
        dp[1] = 1
        # 2 ways to reach the 2nd stair
        dp[2] = 2

        for i in range(3, n+1):
            j = 1
            while j <= m and i>=j:
                dp[i] += dp[i-j]
                j+=1
        return dp[n]


sol = Solution()
n1 = 3; m1 = 2
n2 = 4; m2 = 3

print(sol.totalWays(n1, m1))
print(sol.totalWays(n2, m2))