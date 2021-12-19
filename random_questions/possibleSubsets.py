def allContinuousSubsets(arr):
    n = len(arr)
    subsets = []

    for i in range(n):
        for j in range(i, n):
            subsets.append(arr[i:j+1])
    return subsets

arr = ["a", "b", "c"]
print(allContinuousSubsets(arr))