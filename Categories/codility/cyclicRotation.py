class CyclicRotation:
    def solution(A, K):
        n = len(A)
        arr = [0]*n

        if K == 0 or n == 0:
            return A
        for i in range(n):
            ind = (i+K) % n
            arr[ind] = A[i]
        return arr

    A = [3, 6, 2, 0, 3, 5, 9]
    print(solution(A, 3))
