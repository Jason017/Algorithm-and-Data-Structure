# PCS Offseason 2020: Greedy
N=int(input())
arr=[int(i) for i in input().split()]

ans,curr_max=0,0
for i in arr:
    curr_max+=i
    ans = max(ans,curr_max)

print(ans)