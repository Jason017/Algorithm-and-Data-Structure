from collections import deque

def path_without_obstacle(grid):
    n, m = len(grid), len(grid[0])
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    q = deque()
    q.append([0,0,0]) # row, column, distance
    visited = set()

    while len(q) > 0:
        cr, cc, cdist = q.popleft()
        if cr == n-1 and cc == m-1:
            return cdist
        
        if grid[cr][cc] == 1:
            continue

        for direction in directions:
            nr, nc = cr + direction[0], cc + direction[1]
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                q.append([nr, nc, cdist + 1])
                visited.add((nr, nc))
    return -1

grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0],
    [0,1,1],
    [0,0,0]]
print(path_without_obstacle(grid))



