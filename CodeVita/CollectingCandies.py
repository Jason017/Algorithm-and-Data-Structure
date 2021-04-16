T =  int(input())
arr1 = []
for i in range(0, T):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    count = arr[0]
    for i in range(1, len(arr)):
        count = count + arr[i]
        arr1.append(count)
print(sum(arr1))