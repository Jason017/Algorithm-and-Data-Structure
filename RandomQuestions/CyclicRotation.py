class RotationArray:
    def solution(arr,k):
        if len(arr) == 0:
            return arr
        return arr[-k:] + arr[:-k]

    def solution1(arr,k):
        l = len(arr)
        rotated = [None] * l
        for i in range(l):
            idx = (i+k) % l
            rotated[idx] = arr[i]
        return rotated


    # [1, 2, 3, 3, 6, 7, 7] # 3
    # [6, 7, 7, 1, 2, 3, 3]

    arr = [1,2,3,3,6,7,7]
    print(solution1(arr,3))



