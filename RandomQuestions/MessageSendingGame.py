class MessageSendingGame:
    def solution(S, A):
        answer = ""
        k = 0
        l = len(S)

        for i in range(l):
            answer += S[k]
            k = A[k]
            if k == 0:
                break
        return answer