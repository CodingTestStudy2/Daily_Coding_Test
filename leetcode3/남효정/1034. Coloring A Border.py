# 풀이 실패

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        target_color = grid[row][col]

        queue = deque([(row, col)])
        visited = {(row, col)}
        borders = []

        while queue:
            r, c = queue.popleft()
            is_border = False

            # 상하좌우 4방향으로
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # 격자 밖이면 테두리임
                if not (0 <= nr < m and 0 <= nc < n):
                    is_border = True

                # 다른 색상이어도 테두리
                elif grid[nr][nc] != target_color:
                    is_border = True

                # 아직 안 가본 색상 칸이라면 큐에 추가함
                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

            # 테두리로 결정되면 기록
            if is_border:
                borders.append((r, c))
        
        # 테두리 칸들만 색상 변경
        for r, c in borders:
            grid[r][c] = color
        
        return grid
        