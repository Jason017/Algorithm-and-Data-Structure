def coinChanges(coins, amount):
    # Not going to work
    coins.sort()
    count = 0
    for i in range(len(coins)-1,-1,-1):
        coin_val = coins[i]
        count += amount//coin_val
        amount %= coin_val
    if amount != 0:
        return -1
    return count

def coinChanges1(coins, amount):

    memo = [float("inf")]*(amount+1)
    memo[0] = 0

    for i in range(1,amount+1):
        for coin in coins:
            
            if i-coin >= 0 and memo[i] > memo[i-coin]+1:
                memo[i] = memo[i-coin]+1

    if memo[amount] == float("inf"):
        return -1

def coinChanges2(coins, amount):
    coins.sort()
    changes=[amount+1]*(amount+1)
    changes[0]=0
    for i in range(1,amount+1):
        for coin in coins:
            if coin>i:
                break
            else:
                changes[i] = min(changes[i],changes[i-coin]+1)
    return changes[-1] if changes[-1]!=(amount+1) else -1

def coinChanges3(coins, amount):
    max = float('inf')
    dp = [0] + [max] * amount

    for i in range(1, amount+1):
        dp[i] = min(dp[i-c] if i-c >=0 else max for c in coins)+1
    return [dp[amount], -1][dp[amount] == max]

coins1 = [1,2,5]
amount1 = 11
coins2 = [186,419,83,408]
amount2 = 6249

print(coinChanges3(coins2, amount2))