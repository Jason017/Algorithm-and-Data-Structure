class OddOccurrenceInArray:
    def solution(A):
        result = 0
        for n in A:
            result ^= n
        return result
    
    def solution2(A):
        A.sort()
        if len(A) == 1:
            return A[0]
        
        for i in range(0, len(A), 2):
            if i+1==len(A):
                return A[i]
            if A[i] != A[i+1]:
                return A[i]
            