from collections import deque

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        queue = deque()
        
        m, n = len(grid), len(grid[0])
        
        visited = [[0] * n for _ in range(m)]
        tmp = [[0] * n for _ in range(m)]
        
        queue.append((col,row))
        c = grid[row][col]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        
        while True:
            if len(queue) == 0:
                break
            
            x,y = queue.popleft()
            visited[y][x] = 1
            
            if x == 0 or x == n-1 or y == 0 or y == m-1:
                tmp[y][x] = 1
            elif not (grid[y+1][x] == c and grid[y-1][x] == c and grid[y][x+1] == c and grid[y][x-1] == c):
                tmp[y][x] = 1

            for dx,dy in dirs:
                if 0 <= x + dx < n and 0 <= y + dy < m and visited[y+dy][x+dx] == 0 and grid[y+dy][x+dx] == c:
                    queue.append((x+dx,y+dy))

        for y in range(m):
            for x in range(n):
                if tmp[y][x] == 1:
                    grid[y][x] = color

        return grid
        