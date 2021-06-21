# PCS Offseason 2020: Greedy
N=int(input())
arr=[int(i) for i in input.split()]
arr.sort()

ans=0

for i in range(N):
    ans+=arr[i]*(N-i)

print(ans/N)

