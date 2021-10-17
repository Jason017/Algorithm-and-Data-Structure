# SImilar questions: Leetcode 1143. Longest Common Subsequence

def longestSubstringLength(a, b):
    m, n = len(a), len(b)
    grid = [[0] * (n+1) for _ in range(m+1)]
    ans = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
                ans = max(ans, grid[i][j])

    return ans
 
a = 'OldSite:GeeksforGeeks.org'; b = 'NewSite:GeeksQuiz.com'
a1 = 'adsfesf'; b1 = 'adsjgowadsfeqsfdr'
 
print('Length of longest common substring is', longestSubstringLength(a, b))
print('Length of longest common substring is', longestSubstringLength(a1, b1))

def findLongestCommonSubstring(a, b):
    m, n = len(a), len(b)
    grid = [[0] * (n+1) for _ in range(m+1)]
    ans,temp = "", ""
    mx = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
                if grid[i][j] == 0:
                    temp = ""
                elif grid[i][j] > mx:
                    mx = grid[i][j]
                    temp += a[i-1]
                    ans = temp
    return ans

print('The longest common substring is', findLongestCommonSubstring(a1, b1)) # adsfe
print('The longest common substring is', findLongestCommonSubstring(a, b))