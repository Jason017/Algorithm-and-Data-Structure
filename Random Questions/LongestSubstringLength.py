def longestSubstringLength(X, Y):
    m, n = len(X), len(Y)
    grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                grid[i][j] = 0
            elif X[i-1] == Y[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
                result = max(result, grid[i][j])
            else:
                grid[i][j] = 0
    return result
 
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
 
print('Length of Longest Common Substring is', longestSubstringLength(X, Y))
