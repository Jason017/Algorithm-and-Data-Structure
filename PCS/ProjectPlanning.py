# PCS Offseason 2020: Greedy
N=int(input())
project,late_project=[],[]

for i in range(N):
    info=input().split()
    project.append([info[0],int(info[1]),int(info[2])])

for i in range(N):
    for j in range(N-1-i):
        if project[j][2] > project[j+1][2]:
            project[j],project[j+1]=project[j+1],project[j]

temp=0
for i in range(N):
    temp+=project[i][2]
    if temp>project[i][1]:
        late_project.append(project[i][0])

lateness=temp-project[N-1][1]
print(lateness)

sorted(late_project, key=str.lower)
for i in late_project:
    print(i)

# 2
# btree 8 4
# assembler 9 6

# 4
# physics 8 1
# paper 12 9
# chem 4 
# bio 9 1