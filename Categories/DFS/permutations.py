'''
Core: Backtrack/DFS

1. Base Case
2. For each possibility p
    a. memorize current state
    b. backtrack(next state)
    c. restore the state
'''

# Solution 1
# O(n*n!) O(n!)


def dfs(arr, level, output):
    if level == len(arr):
        output.append(arr[:])
    for i in range(level, len(arr)):
        arr[i], arr[level] = arr[level], arr[i]
        # print("before", level, i, arr)
        dfs(arr, level+1, output)
        # print("after", level, i, arr)
        arr[i], arr[level] = arr[level], arr[i]


def permute(arr):
    output = []
    dfs(arr, 0, output)
    return output


print(permute([1, 2, 3]))


# Solution 2
# O(n*n!) O(n!)
def permute(arr):
    output = []
    if len(arr) == 1:
        output.append(arr[:])

    for _ in range(len(arr)):
        ele = arr.pop(0)
        perms = permute(arr)
        # print("before",perms)
        for perm in perms:
            perm.append(ele)
        # print("after",perms)
        output.extend(perms)
        arr.append(ele)

    return output


print(permute([1, 2, 3]))


# Solution 3
# O(n*n!) O(n!)
def backtrack(output, arr, visited, curr):
    if len(curr) == len(arr):
        output.append(curr)
    for ele in arr:
        if ele not in visited:
            visited.add(ele)
            backtrack(output, arr, visited, curr+[ele])
            visited.remove(ele)


def permute(arr):
    visited = set()
    output = []
    backtrack(output, arr, visited, [])
    return output


print(permute([1, 2, 3]))


# Solution 4
# O(n*n!) O(n!)
def dfs(output, arr, curr=[]):
    if not arr:
        output.append(curr)
    for i in range(len(arr)):
        dfs(output, arr[:i]+arr[i+1:], curr+[arr[i]])


def permute(arr):
    output = []
    dfs(output, arr)
    return output


# Solution 5: Iterative Approach
def permute(arr):
    output = []
    n = len(arr)
    i = 0
    while i < n:
        if not output:
            output.append([arr[i]])
        else:
            tmp = []
            for ele in output:
                for j in range(i+1):
                    e = ele[:]
                    e.insert(j, arr[i])
                    tmp.append(e)
            output = tmp
        i += 1
    return output


print(permute([1, 2, 3]))
