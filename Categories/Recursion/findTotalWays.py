def findTotalWays(arr, i, k): 
    '''
    Given an integer array, find number of ways 
    to calculate a target number using only array 
    elements and addition or subtraction operator.
    '''
    if k == 0 and i == len(arr): 
        return 1
    if i >= len(arr):
        return 0
    return (findTotalWays(arr, i + 1, k) + 
            findTotalWays(arr, i + 1, k - arr[i]) + 
            findTotalWays(arr, i + 1, k + arr[i])) 

arr = [-3, 1, 3, 5, 7]
k = 6
print(findTotalWays(arr, 0, k))

arr = [2, 3, -4, 4]
k = 5
print(findTotalWays(arr, 0, k))