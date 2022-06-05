from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

#      B - E
#    / \  /
#   /  \ /
#   A  D
#   \  /
#    \/
#    C


def bfs(graph, vertex):
    dq = deque([vertex])
    level = {vertex: 0}
    parent = {vertex: None}
    while dq:
        v = dq.popleft()
        for n in graph[v]:
            if n not in level:
                dq.append(n)
                level[n] = level[v] + 1
                parent[n] = v
    return level, parent


print(bfs(graph, 'A'))

# {'A': 0, 'B': 1, 'C', 1, 'D': 2, 'E', 2},  # level
# {'A': None, 'B': 'A', 'C': 'A', 'D', 'B', 'E', 'B'}  # parent
