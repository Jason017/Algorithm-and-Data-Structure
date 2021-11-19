# Algorithm-and-Data-Structure/Random-Questions/findTotalWays.py

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

m1 = 3; n1 = 2
m2 = 4; n2 = 3

print(totalWays(n1, m1))
print(totalWays(n2, m2))