'''
1. 아이디어 :
2. 시간복잡도 :
3. 자료구조/알고리즘 : BFS
'''

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        while True:
            # 1. 빈 칸 없을 때까지 모든 영역 탐색
            seen = set()
            regions = [] # 바이러스 셀
            frontiers = [] # 내일 감염될 셀
            perimeters = [] # 격리에 필요한 벽의 수

            for r in range(m):
                for c in range(n):
                    # 미탐색구역이면서 바이러스 있는 경우
                    if isInfected[r][c] == 1 and (r, c) not in seen:
                        region = set()
                        frontier = set()
                        perimeter = 0

                        # BFS로 연결된 바이러스 영역 탐색
                        queue = [(r, c)]
                        seen.add((r, c))

                        while queue:
                            curr_r, curr_c = queue.pop(0)
                            region.add((curr_r, curr_c))

                            # 동서남북으로 탐색
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), ((0, 1))]:
                                nr, nc = curr_r + dr, curr_c + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 1 and (nr, nc) not in seen:
                                        seen.add((nr, nc))
                                        queue.append((nr, nc))
                                    elif isInfected[nr][nc] == 0:
                                        frontier.add((nr, nc))  # 위협받는 비감염 칸
                                        perimeter += 1          # 필요한 벽 개수
                        
                        if region:
                            regions.append(region)
                            frontiers.append(frontier)
                            perimeters.append(perimeter)
            
            # 더 이상 남아 있는 영역 없으면 종료
            if not regions:
                break
                
            # 2. 다음 날 칸의 개수가 가장 큰 바이러스 영역 찾기
            idx_to_target = max(range(len(frontiers)), key=lambda i: len(frontiers[i]))
            
            # 위협 받는 칸 0개라면 더 이상 바이러스 확산 안 됨
            if len(frontiers[idx_to_target]) == 0:
                break

            # 3. 가장 위험한 영역에 벽을 설치하여 격리함 (2: 완전 격리된 영역)
            ans += perimeters[idx_to_target]
            for r, c in regions[idx_to_target]:
                isInfected[r][c] = 2
                
            # 4. 나머지 바이러스 영역들은 인접 확산 (1로 변경)
            for i in range(len(regions)):
                if i != idx_to_target:
                    for r, c in frontiers[i]:
                        isInfected[r][c] = 1
                        
        return ans