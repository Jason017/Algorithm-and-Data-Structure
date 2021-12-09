from collections import deque, defaultdict
class Graph:
    def __init__(self, path):
        if not path:
            print("Invalid Input")
            return 
        self.graph = defaultdict(list)
        for i in range(len(path)):
            self.graph[i] = path[i]

    def allPathsSrcDest(self, src, dst):
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
    
g = Graph([[4,3,1],[3,2,4],[3],[4],[]])
print(g.graph)
print(g.allPathsSrcDest(0,4))


