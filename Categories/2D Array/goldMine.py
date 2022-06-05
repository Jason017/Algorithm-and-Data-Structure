# https://www.geeksforgeeks.org/gold-mine-problem/?ref=lbp
def getMaxGold(gold):
    m, n = len(gold), len(gold[0])

    if m == 1:
        return sum(g for g in gold[0])
    if n == 1:
        return -1

    dp = [[0] * n for _ in range(m)]

    for row in range(m):
        for col in range(n-1, -1, -1):
            if col == n-1:
                right = 0
            else:
                right = dp[row][col+1]

            if row == 0 or col == n-1:
                right_up = 0
            else:
                right_up = dp[row-1][col+1]

            if row == m-1 or col == n-1:
                right_down = 0
            else:
                right_down = dp[row+1][col+1]

            dp[row][col] = gold[row][col] + max(right, right_up, right_down)

    return max(dp[i][j] for i in range(m) for j in range(n))


gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]


print(getMaxGold(gold))
