T = int(input())

def maxSubarray(arr):
    curr_sum, global_sum= arr[0], arr[0]
    for i in range(1,len(arr)):
        curr_sum = curr_sum + arr[i] if curr_sum + arr[i] > arr[i] else arr[i]
        if curr_sum > global_sum:
            global_sum = curr_sum
            end = i
    
    start = end
    while start >= 0:
        global_sum -= arr[start]
        if global_sum == 0:
            break
        start -= 1
    return [start, end+1]


for i in range(T):
    nk = input().split()
    N,K = int(nk[0]), int(nk[1])
    
    arr = [int(i) for i in input().split()]
    allindices = [[]] * K
    seen = [0] * N
    allindices[0] = maxSubarray(arr)
    
    ans = [] * K


     
