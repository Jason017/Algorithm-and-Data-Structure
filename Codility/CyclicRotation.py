class CyclicRotation:
    def solution(A,K):
        l = len(A)
        arr = [0]*l
        
        if K == 0 or l == 0:
            return A
        for i in range(l):
            ind = (i+K)%l
            arr[ind] = A[i]
        return arr

    A = [3,6,2,0,3,5,9]
    print(solution(A,3))