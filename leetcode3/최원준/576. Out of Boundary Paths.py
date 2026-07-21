#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(maxMove * n * m * 4)

3. 자료구조/알고리즘 :
dp

'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1_000_000_009
        
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        ans = 0
        dir = [0,1],[0,-1],[-1,0],[1,0]

        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]

            for row in range(m):
                for col in range(n):
                    if dp[row][col] == 0:
                        continue

                    for dx, dy in dir:
                        next_row = row + dx
                        next_col = col + dy

                        if 0<=next_row<m and 0<=next_col<n:
                            next_dp[next_row][next_col] += dp[row][col]
                            next_dp[next_row][next_col] %= MOD
                        else:
                            ans += dp[row][col]
                            ans %= MOD
            dp = next_dp
        
        return ans
