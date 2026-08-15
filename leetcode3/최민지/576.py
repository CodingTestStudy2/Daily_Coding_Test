class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def dfs(r, c, moves):
            # 경계 밖으로 나간 경우 -> 성공 경로 1개 반환
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            # 이동 횟수를 다 썼는데 여전히 경계 안인 경우 -> 실패 0개 반환
            if moves == 0:
                return 0
            # 이미 계산한 결과가 있는 경우
            if (r, c, moves) in memo:
                return memo[(r, c, moves)]

            # 상, 하, 좌, 우 4방향으로 탐색
            paths = (
                dfs(r - 1, c, moves - 1) +
                dfs(r + 1, c, moves - 1) +
                dfs(r, c - 1, moves - 1) +
                dfs(r, c + 1, moves - 1)
            ) % MOD

            memo[(r, c, moves)] = paths
            return memo[(r, c, moves)]

        return dfs(startRow, startColumn, maxMove)
        