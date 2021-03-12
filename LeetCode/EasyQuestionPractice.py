# 9. Palindrome Number
class Solution:
	def isPalindrome(self, x: int) -> bool:
		return str(x) == str(x)[::-1]

# 1332. Remove Palindromic Subsequences
class Solution:
	def removePalindromeSub(self, s: str) -> int:
		if not s: 
			return -1
		return 1 if s[::-1] == s else 2
