import collections

N=int(input())
for i in range(N):
    G=input()
    nums=[int(j) for j in input().split(' ')]
    invitations=collections.Counter(nums)
    print('Case #'+str(i+1)+': '+str(invitations.most_common()[len(invitations)-1][0]))
