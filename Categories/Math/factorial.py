from math import factorial as f


n = 23
print(f'The factorial of {n} is {f(n):e}')


def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


print(f'The factorial of {n} is {fact(n):e}')
