def allPossibleSublist(arr):
    n = len(arr)
    sublists = [[]]

    for i in range(n-1):
        for j in range(i+1, n+1):
            sublists.append(arr[i:j])
    return sublists

print(allPossibleSublist(["a", "b", "c"]))


def allContinuousSublist(arr):
    n = len(arr)
    sublists = []

    for i in range(n):
        for j in range(1, n+1):
            if i+j <= n:
                sublists.append(arr[i:i+j])
    return sublists

print(allContinuousSublist(["a", "b", "c"]))
