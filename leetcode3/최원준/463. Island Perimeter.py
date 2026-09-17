class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        def bfs(row, col):
            ans = 0
            grid[row][col] = 2
            queue = Deque()
            queue.append([row,col])

            while queue:
                x, y = queue.popleft()
                perimeter = 4
                for dirs in range(4):
                    nx = x + dx[dirs]
                    ny = y + dy[dirs]

                    if nx < 0 or n <= nx or ny < 0 or m <= ny:
                        continue
                    elif 0<=nx<n and 0<=ny<m:
                        if grid[nx][ny] == 1:
                            queue.append([nx,ny])
                            grid[nx][ny] = 2
                            perimeter-=1
                        elif grid[nx][ny] == 2:
                            perimeter-=1
                ans += perimeter
            return ans
                        

        
        for i in range(n):
            for j in range(m):
              if grid[i][j] == 1:
                return bfs(i, j)  

        return 0
