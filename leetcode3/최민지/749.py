from collections import deque
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        answer = 0

        while True:
            visited = [[False] * n for _ in range(m)]
            regions = [] # 각 감염 구역의 좌표 목록
            frontiers = [] # 각 구역이 감염시킬 수 있는 0들의 집합
            walls = [] # 각 구역을 막는 데 필요한 벽 개수 

            # 1. 모든 감염 구역 선택  
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        q = deque([(i,j)])
                        visited[i][j] = True

                        region = []
                        frontier = set()
                        wall = 0

                        while q:
                            x, y = q.popleft()
                            region.append((x,y))

                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy

                                if 0 <= nx < m and 0 <= ny < n:

                                    # 같은 감염 구역
                                    if isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        q.append((nx, ny))

                                    # 앞으로 감염될 수 있는 칸 
                                    elif isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        wall += 1
                        regions.append(region)
                        frontiers.append(frontier)
                        walls.append(wall)

            # 더 이상 퍼질 곳이 없으면 종료
            if not frontiers:
                break
            # 2. 가장 많이 퍼질 수 있는 구역 선택
            idx = 0
            for i in range(1, len(frontiers)):
                if len(frontiers[i]) > len(frontiers[idx]):
                    idx = i
            
            # 퍼질 수 있는 칸이 0개면 종료
            if len(frontiers[idx]) == 0:
                break

            # 3. 선택한 구역 격리
            answer += walls[idx]

            for x, y in regions[idx]:
                isInfected[x][y] = -1  # 격리 표시

            # 4. 나머지 구역 확산
            for i in range(len(regions)):            
                if i == idx:
                    continue
                
                for x, y in frontiers[i]:
                    isInfected[x][y] = 1
                    
        return answer

        
        