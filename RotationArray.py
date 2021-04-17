class RotationArray:
    def solution(arr,k):
        if len(arr) == 0:
            return arr
        return arr[-k:] + arr[:-k]

    # def solution1(arr,k):
    #     for i in range(k):


    arr = [1,2,3,3,6,7,7]
    print(solution(arr,3))