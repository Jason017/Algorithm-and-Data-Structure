def totalWays(n, m):
    ''' 
    Find total ways to reach the n'th stair from the bottom
    when a person is allowed to take at most m steps at a time
    '''
    if n <= 1:
        return 1

    count = 0
    for i in range(1, m + 1):
        count += totalWays(n - i, m)

    return count

print(totalWays(0,1))