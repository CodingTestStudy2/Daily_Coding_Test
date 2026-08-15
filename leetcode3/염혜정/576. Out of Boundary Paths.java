// bfs + dp

class Solution {
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        final int MOD = 1_000_000_007;
        long[][] dp = new long[m][n];
        dp[startRow][startColumn] = 1;
        int count = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int move = 0; move < maxMove; move++) {
            long[][] next = new long[m][n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (dp[i][j] == 0) continue;
                    for (int[] d : dirs) {
                        int ni = i + d[0];
                        int nj = j + d[1];
                        if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
                            count = (int) ((count + dp[i][j]) % MOD);
                        } else {
                            next[ni][nj] = (next[ni][nj] + dp[i][j]) % MOD;
                        }
                    }
                }
            }
            dp = next;
        }

        return count;
    }
}
