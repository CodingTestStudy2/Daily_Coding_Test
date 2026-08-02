from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])

        answer = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while True:

            visited = [[False] * n for _ in range(m)]

            regions = []        # 감염 영역
            frontiers = []      # 각 영역이 감염시킬 수 있는 칸(set)
            walls = []          # 필요한 벽 개수

            def dfs(x, y):

                visited[x][y] = True
                region.append((x, y))

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if isInfected[nx][ny] == 1:
                        if not visited[nx][ny]:
                            dfs(nx, ny)

                    elif isInfected[nx][ny] == 0:
                        frontier.add((nx, ny))
                        wall[0] += 1

            # 모든 감염 영역 찾기
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:

                        region = []
                        frontier = set()
                        wall = [0]

                        dfs(i, j)

                        regions.append(region)
                        frontiers.append(frontier)
                        walls.append(wall[0])

            # 더 이상 퍼질 곳이 없음
            if not frontiers:
                break

            idx = max(range(len(frontiers)),
                      key=lambda i: len(frontiers[i]))

            if len(frontiers[idx]) == 0:
                break

            answer += walls[idx]

            # 선택된 영역 봉쇄
            for x, y in regions[idx]:
                isInfected[x][y] = -1

            # 나머지 영역 확산
            for i in range(len(regions)):
                if i == idx:
                    continue

                for x, y in frontiers[i]:
                    isInfected[x][y] = 1

        return answer
