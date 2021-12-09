def cyclicRotation(arr,k):
    if len(arr) == 0:
        return arr
    return arr[-k:] + arr[:-k]

def cyclicRotation(arr,k):
    n = len(arr)
    rotated = [None] * n
    for i in range(n):
        idx = (i+k) % n
        rotated[idx] = arr[i]
    return rotated

# [1, 2, 3, 3, 6, 7, 7] => [6, 7, 7, 1, 2, 3, 3]

arr = [1,2,3,3,6,7,7]
print(cyclicRotation(arr,3))



