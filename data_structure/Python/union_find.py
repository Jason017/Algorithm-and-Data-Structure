# https://jojozhuang.github.io/algorithm/algorithm-union-find/
## Disjoint Set/Union Find
class DSU:
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, i):
        if self.parents[i] == i:
            return self.parents[i]
        return self.find(self.parents[i])

    def union(self, i, j):
        p1 = self.find(i)
        p2 = self.find(j)
        self.parents[p1] = p2

dsu = DSU(5) # parents = [0,1,2,3,4]

# Set 2 as a parent of 0
dsu.union(0,2) # parents = [2,1,2,3,4]

# Set 2 as a parent of 4
dsu.union(4,2) # parents = [2,1,2,3,2]

# Set 1 as a parent of 3
dsu.union(3,1) # parents = [2,1,2,1,2]

# Group 1 = {0,2,4}
# Group 2 = {1,3}
if dsu.find(0) == dsu.find(4):
    print("0 and 4 share a parent.")

if dsu.find(1) != dsu.find(0):
    print("0 and 1 don't share a parent")



## Optimization

class DSU:
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
        self.rank = [0] * n
    
    # Path Compression by Recursion
    def find(self, i):
        if self.parents[i] == i:
            return self.parents[i]
        self.parents[i] = self.find(self.parents[i])
    # Path Compression by Iteration
    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return self.parents[i]
    
    # Union by rank
    def union(self, i, j):
        p1 = self.find(i)
        p2 = self.find(j)
        if p1 == p2:
            return 
        
        if self.rank[p1] < self.rank[p2]:
            self.parents[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2
            self.rank[p2]+=1

