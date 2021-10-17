def allPossibleSublist(arr):
    n = len(arr)
    sublists = [[]]

    for i in range(n-1):
        for j in range(i+1, n+1):
            sublists.append(arr[i:j])
    return sublists

arr = ["a", "b", "c"]
print(allPossibleSublist(arr))


def allContinuousSublist(arr):
    n = len(arr)
    sublists = []

    for i in range(n):
        for j in range(i, n):
            sublists.append(arr[i:j+1])
    return sublists

arr = ["a", "b", "c"]
print(allContinuousSublist(arr))
print(arr[2:3])
