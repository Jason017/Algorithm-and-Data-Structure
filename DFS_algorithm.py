#  1st approach
def dfs(graph, start, visited=None):
    if visited is None:
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
         '4': set(['2', '3'])}
print('1st approach')
print(graph)
dfs(graph,'0')
print()

# 2nd approach
g = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

#      A
#     / \
#    B  C
#   / \  \
#  D  E - F

def dfs1(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs1(graph,neighbour,visited)

print('2nd approach')
dfs1(g, 'A')

# 3rd approach

