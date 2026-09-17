'''
1. 아이디어:
bfs로 섬을 탐색하면서, 섬의 가장자리를 만나면 perimeter를 1씩 증가시킨다.
2. 시간복잡도:
o(n)
3. 알고리즘:
bfs
'''
from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x_len = len(grid[0])
        y_len = len(grid)

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = [[False] * x_len for _ in range(y_len)]
        queue = deque()

        for y in range(y_len):
            breaker = False
            for x in range(x_len):
                if grid[y][x] == 1:
                    queue.append((x,y))
                    visited[y][x] = True
                    breaker = True
                    break
            
            if breaker:
                break
        
        ans = 0
        while queue:
            x,y = queue.pop()
            
            if x == 0:
                ans += 1
            if x == x_len - 1:
                ans += 1
            if y == 0:
                ans += 1
            if y == y_len - 1:
                ans += 1
            
            for dx,dy in directions:
                if 0 <= dx + x < x_len and grid[y][dx+x] == 0:
                    ans += 1
                if 0 <= dy + y < y_len and grid[y+dy][x] == 0:
                    ans += 1
                
                if 0 <= dx + x < x_len and 0 <= dy+ y < y_len and grid[y+dy][x+dx] == 1 and not visited[y+dy][x+dx]:
                    queue.append((x+dx,y+dy))
                    visited[y+dy][x+dx] = True

        return ans
            
            