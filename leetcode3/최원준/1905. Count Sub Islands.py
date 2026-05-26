#

'''
1. 아이디어 :
bfs로 풀 수 있습니다.
sub_island는 grid2에 있는 island가 grid1에 있는 island와 같거나 안에 들어가면 카운트가 됩니다.
grid2를 순회하며, 땅인 경우, bfs를 수행.
bfs는 grid2를 순회하며 인접한 땅들을 검사합니다.
  grid1, 2 모두 1이어야하고, 만약 grid1이 0인 경우 sub_island가 될 수 없기에 아니라고 표시만하고 인접한 땅들을 순회합니다.
  - 조건에 만족하지 않았을때, 인접한 땅들을 순회하지 않고 바로 리턴하는 경우 오답.
  - 조건에 만족하지 않았을때, 인접한 땅들을 순회하지 않고, 방문했던 곳들을 다시 되돌리고 리턴하는 경우 메모리 초과.
  sub_island 조건에 만족할 경우 sub_island이므로 1을 리턴, 아니면 0을 리턴

2. 시간복잡도 :
    O(n * m)

3. 자료구조/알고리즘 :
bfs

'''

from collections import deque

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        ans = 0
        
        def bfs(x: int, y: int) -> int:
            queue = deque()
            queue.append((x,y))
            grid2[x][y]  = 0

            is_sub = 1
            
            while queue:
                x, y = queue.popleft()

                if grid1[x][y] == 0:
                    is_sub = 0
                
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<m and grid2[nx][ny]==1:
                        grid2[nx][ny] = 0
                        queue.append((nx, ny))

            return is_sub

        
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    ans += bfs(i,j)
        
        
        return ans
