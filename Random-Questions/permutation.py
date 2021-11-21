# Solution 1
def swap(string, i, j):
    string[i], string[j] = string[j], string[i]

def permutations(string, curr=0):
    if curr == len(string)-1:
        res.append("".join(string))
    for i in range(curr, len(string)):
        swap(string, curr, i)
        permutations(string, curr+1)
        swap(string, curr, i)

res = []
permutations(list('abc'))
print(res)


# Solution 2
def permutations(remaining, candidate=''):
    if len(remaining) == 0:
        res.append(candidate)
    for i in range(len(remaining)):
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[:i] + remaining[i+1:]
        permutations(newRemaining, newCandidate)

res = []
permutations('abc')
print(res)


# Solution 3: iterative
def permutations(s):
    if not s:
        return []
    res = []
    res.append(s[0])
    for i in range(1, len(s)):
        for j in reversed(range(len(res))):
            curr = res.pop(j)
            for k in range(len(curr) + 1):
                res.append(curr[:k] + s[i] + curr[k:])
 
    return res

print(permutations('abc'))
 


