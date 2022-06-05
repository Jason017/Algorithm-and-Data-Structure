class FrogJmp:
    def solution(X, Y, D):
        return (Y-X)//D if (Y-X) % D == 0 else (Y-X)//D+1
