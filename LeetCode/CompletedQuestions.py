# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        r = 0
        temp = x
        
        while x > 0:
            r = x % 10 + 10 * r
            x = x // 10
            
        return r == temp or r / 10 == temp

# 322. Coin Change
class Solution:
    def coinChange(coins, amount):
        mx = float('inf')
        dp = [0] + [mx] * amount

        for i in range(1, amount+1):
            dp[i] = min(dp[i-c] if i-c >=0 else mx for c in coins)+1
        return [dp[amount], -1][dp[amount] == mx]

# 1332. Remove Palindromic Subsequences
class Solution:
	def removePalindromeSub(self, s: str) -> int:
		if not s: 
			return -1
		return 1 if s[::-1] == s else 2
