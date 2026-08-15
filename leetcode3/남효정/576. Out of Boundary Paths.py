# 풀이 실패
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        MOD = 10**9 + 7

        def dp(r, c, moves):
            # 밖으로 탈출한 경우
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1

            # 이동 횟수 전부 사용한 경우
            if moves == 0:
                return 0

            # 이미 계산된 위치거나 남은 이동 횟수라면 저장된 값으로 사용
            if (r, c, moves) in memo:
                return memo[(r, c, moves)]

            # 상, 하, 좌, 우 이동 경로 합산
            res = (
                dp(r + 1, c, moves - 1)
                + dp(r - 1, c, moves - 1)
                + dp(r, c + 1, moves - 1)
                + dp(r, c - 1, moves - 1)
            ) % MOD

            # 결과 기록 후 반환
            memo[(r, c, moves)] = res
            return res

        return dp(startRow, startColumn, maxMove)