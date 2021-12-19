# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
from collections import deque

def path_without_obstacle(grid):
    m,n = len(grid), len(grid[0])
    dirs = [[0,1], [1,0], [-1,0], [0,-1]]
    q = deque()
    q.append([0,0,0]) # row, column, distance
    visited = set()

    while len(q) > 0:
        r, c, dist = q.popleft()
        if (r, c) == (m-1, n-1):
            return dist
        
        if grid[r][c] == 1:
            continue

        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                q.append([nr, nc, dist + 1])
                visited.add((nr, nc))
    return -1

def path_with_obstacle(grid,k):
    m,n = len(grid), len(grid[0])
    dirs = [[0,1], [1,0], [-1,0], [0,-1]]
    lives = [[-1 for _ in range(n)] for _ in range(m)]
    q = deque()
    q.append([0,0,k,0])
    
    while len(q) > 0:
        r, c, rlives, dist = q.popleft()
        if (r, c) == (m-1, n-1):
            return dist
        
        if grid[r][c] == 1:
            rlives -= 1

        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < m and 0 <= nc < n and lives[nr][nc] < rlives:
                q.append([nr, nc, rlives, dist+1])
                lives[nr][nc] = rlives

    return -1



grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0],
    [0,1,1],
    [0,0,0]]
print(path_without_obstacle(grid))
print(path_with_obstacle(grid,2))



