import heapq

# Dijkstra = Greedy + BFS
# 
# Time Complexity: O((V + E) log V), V represents the number of vertices and E represents the number of edges in the graph
# Space Complexity: O(V)
def dijkstra(graph, src):
    dist = {vertex: float('inf') for vertex in graph}
    dist[src] = 0

    minHeap = [(0, src)]
    while minHeap:
        currWeight, currVertex = heapq.heappop(minHeap)

        if currWeight > dist[currVertex]:
            continue

        for neighborVertex, neighborWeight in graph[currVertex].items():
            if dist[neighborVertex] > currWeight + neighborWeight:
                dist[neighborVertex] = currWeight + neighborWeight
                heapq.heappush(minHeap, (dist[neighborVertex], neighborVertex))

    return dist

graph1 = {
    'U': {'W': 5, 'V': 2, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'Z': 5, 'V': 3, 'U': 5, 'X': 3, 'Y': 1},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

graph2 = {
    '0': {'1': 4, '7': 8},
    '1': {'0': 4, '7': 11, '2': 8},
    '2': {'1': 8, '3': 7, '8': 2},
    '3': {'2': 7, '5': 14, '4': 9},
    '4': {'3': 9, '5': 10},
    '5': {'6': 2, '2': 4, '3': 14, '4': 10},
    '6': {'7': 1, '8': 6, '5': 2},
    '7': {'0': 8, '1': 11, '8': 7, '6': 1},
    '8': {'2': 2, '7': 7, '6': 1},
}

print(dijkstra(graph1, "X"))
print(dijkstra(graph2, "2"))

def dijkstra(n, edges, src):
    graph = {}
    for i in range(n):
        graph[i] = []

    for s, d, w in edges:
        graph[s].append([d, w])
    
    dist = {}
    minHeap = [[0, src]]

    while minHeap:
        currWeight, currVertex = heapq.heappop(minHeap)
        if currVertex in dist:
            continue

        dist[currVertex] = currWeight
        for neighborVertex, neighborWeight in graph[currVertex]:
            if neighborVertex not in dist:
                heapq.heappush(minHeap, [currWeight + neighborWeight, neighborVertex])

    for i in range(n):
        if i not in dist:
            dist[i] = float('inf')

    return {i: dist[i] for i in range(n)}

n = 5
edges = [
    [0, 1, 10],
    [0, 2, 3],
    [1, 3, 2],
    [2, 1, 4],
    [2, 3, 8],
    [2, 4, 2],
    [3, 4, 5],
]
print(dijkstra(n, edges, 0)) # {0: 0, 1: 7, 2: 3, 3: 9, 4: 5}

def dijkstra_shortest_distance(n, edges, src):
    graph = {}
    for i in range(n):
        graph[i] = []

    for s, d, w in edges:
        graph[s].append([d, w])
    
    dist = {vertex: float('inf') for vertex in range(n)}
    dist[src] = 0
    minHeap = [(0, src)]

    while minHeap:
        currWeight, currVertex = heapq.heappop(minHeap)

        if currWeight > dist[currVertex]:
            continue

        for neighborVertex, neighborWeight in graph[currVertex]:
            if dist[neighborVertex] > currWeight + neighborWeight:
                dist[neighborVertex] = currWeight + neighborWeight
                heapq.heappush(minHeap, (dist[neighborVertex], neighborVertex))

    return {i: dist[i] for i in range(n)}

n = 5
edges = [
    [0, 1, 10],
    [0, 2, 3],
    [1, 3, 2],
    [2, 1, 4],
    [2, 3, 8],
    [2, 4, 2],
    [3, 4, 5],
]
print(dijkstra_shortest_distance(n, edges, 0)) # {0: 0, 1: 7, 2: 3, 3: 9, 4: 5}