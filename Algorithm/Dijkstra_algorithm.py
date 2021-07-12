import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        curr_distance, curr_vertex = heapq.heappop(pq)

        if curr_distance > distances[curr_vertex]:
            continue

        for neighbor, weight in graph[curr_vertex].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


example_graph = {
    'U': {'W': 5, 'V': 2, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'Z': 5, 'V': 3, 'U': 5, 'X': 3, 'Y': 1},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(calculate_distances(example_graph, 'X'))