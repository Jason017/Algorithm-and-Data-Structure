#  1st approach
def dfs(graph, start, visited=None):
    if not visited:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['3'])}
#       0
#      / \
#     1  2
#    /\ /
#   3  4
print('1st approach')
dfs(graph, '0')
print()


# 2nd approach
def dfs(graph, node, visited=None):
    if not visited:
        visited = set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
#      A
#     / \
#    B  C
#   / \  \
#  D  E - F
print('2nd approach')
dfs(graph, 'A')


# 3rd approach
from collections import deque

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)
    
    while stack:
        curr = stack.pop()
        print(curr)

        for next in reversed(graph[curr]):
            if next not in visited:
                visited.append(next)
                stack.append(next)

print('3rd approach')
dfs(graph, 'A')