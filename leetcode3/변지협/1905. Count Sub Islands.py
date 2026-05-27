'''
1. 아이디어 :
    grid2 bfs를 2중 for문 돌고, 
    각 bfs 돌면서 grid2 (인접한 곳) 을 visited 에 저장한다.
    visited에 저장된 곳들을 grid1과 비교해서 sub island인지 판단하고, 모두 0으로 초기화한다.
2. 시간복잡도 :
    O(n*m)
3. 자료구조/알고리즘 :
    bfs
'''


class Solution:
    def countSubIslands(self, grid1, grid2):
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        answer = 0

        y_len = len(grid2)
        x_len = len(grid2[0])
        
        for y in range(y_len):
            for x in range(x_len):
                queue = deque()
                visited = set()
                if grid2[y][x] == 1:
                    queue.append((x,y))
                    visited.add((x,y))
                
                while True:
                    if len(queue) == 0:
                        break
                    
                    _x,_y = queue.popleft()
                    
                    for dx,dy in directions:
                        if 0 <= dx + _x < x_len and 0 <= dy + _y < y_len and \
                         grid2[_y+dy][_x+dx] == 1 and (_x+dx, _y+dy) not in visited:
                            queue.append((_x+dx,_y+dy))
                            visited.add((_x+dx,_y+dy))
                
                sub = True
                for _x,_y in visited:
                    if grid1[_y][_x] == 0:
                        sub = False
                    grid2[_y][_x] = 0
                
                if visited and sub:
                    answer +=1
        
        return answer
                # print(visited)
                        
                