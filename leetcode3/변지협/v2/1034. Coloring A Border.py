from collections import deque

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        queue = deque()
        
        m, n = len(grid), len(grid[0])
        
        visited = [[0] * n] * m
        print(visited)
        
        queue.append((col,row))
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while True:
            if len(queue) == 0:
                break
            
            x,y = queue.pop()
            visited[y][x] = 1
            
            if x == 0 or x == n or y == 0 or y == m :
                grid[y][x] = color

            for dx,dy in dirs:
                if  
            
            
            
        return grid
        