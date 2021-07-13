from collections import deque

def path_without_obstacle(grid):
    n, m = len(grid), len(grid[0])
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    q = deque()
    q.append([0,0,0]) # row, column, distance
    visited = set()

    while len(q) > 0:
        row_idx, col_idx, dist = q.popleft()
        if row_idx == n-1 and col_idx == m-1:
            return dist
        
        if grid[row_idx][col_idx] == 1:
            continue

        for direction in directions:
            nr_idx, nc_idx = row_idx + direction[0], col_idx + direction[1]
            if 0 <= nr_idx < n and 0 <= nc_idx < m and (nr_idx, nc_idx) not in visited:
                q.append([nr_idx, nc_idx, dist + 1])
                visited.add((nr_idx, nc_idx))
    return -1

def path_with_obstacle(grid,k):
    n,m = len(grid), len(grid[0])
    directions = [[0,1], [1,0], [-1,0], [0,-1]]
    lives = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0,k,0])
    visited = set()

    while len(q) > 0:
        row_idx, col_idx, rlives, dist = q.popleft()
        if row_idx == n-1 and col_idx == m-1:
            return dist
        
        if grid[row_idx][col_idx] == 1:
            rlives -= 1

        for direction in directions:
            nr_idx, nc_idx = row_idx + direction[0], col_idx + direction[1]
            if 0 <= nr_idx < n and 0 <= nc_idx < m and lives[nr_idx][nc_idx] < rlives:
                q.append([nr_idx, nc_idx, rlives, dist+1])
                lives[nr_idx][nc_idx] = rlives

    return -1



grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0],
    [0,1,1],
    [0,0,0]]
print(path_without_obstacle(grid))
print(path_with_obstacle(grid,2))



