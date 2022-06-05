# Similar questions: Leetcode 1143. Longest Common Subsequence
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for row in range(m-1, -1, -1):
        for col in range(n-1, -1, -1):
            if text1[row] == text2[col]:
                dp[row][col] = dp[row+1][col+1]+1
            else:
                dp[row][col] = max(dp[row+1][col], dp[row][col+1])
    return dp[0][0]


def longestCommonSubstring(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n+1) for _ in range(m+1)]
    ans = 0
    for row in range(1, m+1):
        for col in range(1, n+1):
            if a[row-1] == b[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
                ans = max(ans, dp[row][col])
    return ans


a1 = 'OldSite:GeeksforGeeks.org'
b1 = 'NewSite:GeeksQuiz.com'
a2 = 'adsfesffdr'
b2 = 'adsjgowadsfeqsfdr'
a3 = "daceb"
b3 = "ace"

print('Length of longest common substring is',
      longestCommonSubstring(a1, b1))  # 10
print('Length of longest common substring is',
      longestCommonSubstring(a2, b2))  # 5
print('Length of longest common substring is',
      longestCommonSubstring(a3, b3))  # 3


def findLongestCommonSubstring(a, b):
    m, n = len(a), len(b)
    grid = [[0] * (n+1) for _ in range(m+1)]
    ans, temp = "", ""
    max_len = 0
    for row in range(1, m+1):
        for col in range(1, n+1):
            if a[row-1] == b[col-1]:
                grid[row][col] = grid[row-1][col-1] + 1
                if grid[row][col] > max_len:
                    max_len = grid[row][col]
                    temp += a[row-1]
                    ans = temp
    return ans


print('The longest common substring is',
      findLongestCommonSubstring(a1, b1))  # Site:Geeks
print('The longest common substring is',
      findLongestCommonSubstring(a2, b2))  # adsfe
print('The longest common substring is',
      findLongestCommonSubstring(a3, b3))  # ace
