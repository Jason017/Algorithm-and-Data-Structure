# 9. Palindrome Number
Class Solution:
	def isPalindrome(self, x: int) -> bool:
		return str(x) == str(x)[::-1]
