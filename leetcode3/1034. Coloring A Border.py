class Solution:
    def colorBorder(self, grid, row, col, color):
        m = len(grid)
        n = len(grid[0])

        target = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        border = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            visited[r][c] = True

            is_border = False

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # 배열의 가장자리
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    is_border = True
                    continue

                # 다른 색과 인접
                if grid[nr][nc] != target:
                    is_border = True
                    continue

                # 같은 색이고 아직 방문하지 않았다면 DFS
                if not visited[nr][nc]:
                    dfs(nr, nc)

            if is_border:
                border.append((r, c))

        dfs(row, col)

        # border만 색칠
        for r, c in border:
            grid[r][c] = color

        return grid
