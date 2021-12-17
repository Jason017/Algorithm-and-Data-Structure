from collections import deque
from typing import List

class DAG:
    '''
    Directed Acyclic Graph (DAG). There's no cycle in this case, but it can have disconnected parts
    '''
    def __init__(self, path: List[int]) -> None:
        if not path: print("Invalid Input"); return 
        self.size = len(path)
        self.graph = {i:path[i] for i in range(self.size)}


    # BFS + Stack
    def allPathsSrcDestBFS(self, src: int, dst: int) -> List[int]: 
        stack = [[src]]
        output = []

        while stack:
            path = stack.pop()
            for neighbor in self.graph[path[-1]]:
                if neighbor == dst:
                    output.append(path+[neighbor])
                else:
                    stack.append(path+[neighbor])

        return output


    # DFS + Backtrack
    def allPathsSrcDestDFS(self, src: int, dst: int) -> List[int]: 
        output = []
        
        def backtrack(curr, path):
            if curr == dst:
                output.append(path)
            for nei in self.graph[curr]:
                backtrack(nei, path + [nei])

        backtrack(src, [0])
        return output


    # BFS + Queue
    def allConnectedNodesBFS(self, node):
        visited = set()
        q = deque([node])
        output = []

        while q:
            n = q.popleft()
            output.append(n)
            for nei in self.graph[n]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

        return output 
    

    # DFS + Backtrack
    def allConnectedNodesDFS(self, node):
        output = []

        def backtrack(curr):
            output.append(curr)
            for nei in self.graph[curr]:
                if nei not in output:
                    backtrack(nei)

        backtrack(node)
        return output


dag = DAG([[4,3,1],[3,2,4],[3],[4],[]])
print("Graph:", dag.graph)
print("Size:", dag.size)
print("All possible paths from src to dest (BFS):", dag.allPathsSrcDestBFS(0,4))
print("All possible paths from src to dest (DFS):", dag.allPathsSrcDestDFS(0,4))
print("All connected nodes from src (BFS):", dag.allConnectedNodesBFS(0))
print("All connected nodes from src (DFS):", dag.allConnectedNodesDFS(0))



class DG(DAG):
    '''
    Directed Graph (DG).
    '''
    # BFS + Queue
    def hasCycle(self):
        degrees = [0] * self.size
        for node in range(self.size):
            for nei in self.graph[node]:
                degrees[nei] += 1

        q = deque()
        for node in range(len(degrees)):
            if degrees[node] == 0:
                q.append(node)
        
        cnt = 0
        while q:
            n = q.popleft()
            for node in self.graph[n]:
                degrees[node] -= 1
                if degrees[node] == 0:
                    q.append(node)
            cnt += 1
        return cnt != self.size


g = DG([[1],[2],[3,4],[0],[2]]) 
print(g.hasCycle()) # True

g = DG([[1,2],[3],[3],[]])
print(g.hasCycle()) # False

g = DG([[1,2],[2],[0,3],[3]]) 
print(g.hasCycle()) # True

