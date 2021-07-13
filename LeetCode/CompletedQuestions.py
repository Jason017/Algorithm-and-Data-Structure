# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        
        if x < 0:
            negative = True
            x = -x
            
        r = 0
        while x > 0:
            r = x%10 + r*10
            x //= 10
        
        if r == 0 or r > (2**31) - 1 or r < -(2**31):
            return 0
        
        if negative:
            return -r
        return r

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
