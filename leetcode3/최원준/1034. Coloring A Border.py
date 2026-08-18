#

'''
1. 아이디어 :
border인 애들을 구해야한다. border의 조건은 grid의 끝에 위치하거나, 인접한 4개가 모두 같은 숫자가 아닌 경우.
dfs를 통해 border인지 구분하여 candids에 넣는다.
candids을 하나씩 순회하며 grid를 업데이트한다.

2. 시간복잡도 :
    O(n * m * (4+4+1))

3. 자료구조/알고리즘 :
dfs

'''
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        base_num = grid[row][col]
        candids = []
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        visited = [[0] * m for _ in range(n)]

        def dfs(x, y):
            if visited[x][y]:
                return

            visited[x][y] = 1
            if grid[x][y] != base_num:
                return

            is_border = False
            adjacent = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m):
                    is_border = True
                    break
                if grid[nx][ny] == base_num:
                    adjacent += 1
            
            if is_border or adjacent < 4:
                candids.append([x,y])
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0<=nx<n and 0<=ny<m):
                    continue
                dfs(nx, ny)
        
        dfs(row, col)

        for x, y in candids:
            grid[x][y] = color
        
        return grid


                


        # [1,1] 0 0 3
        # [1,2]
        
        # [3,3]
        # [3,2]

        # [1,2,2] 0 1 3
        # [2,3,2]

        # [1,3,3]
        # [2,3,3]

        # [1,1,1] 1 1 2
        # [1,1,1]
        # [1,1,1]

        # [2,2,2]
        # [2,1,2]
        # [2,2,2]
