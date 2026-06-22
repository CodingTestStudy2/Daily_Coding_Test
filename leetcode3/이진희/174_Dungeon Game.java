/*

1. 아이디어 : dp 활용
              오른쪽, 아래 방향으로만 이동 가능
              이동 도중 0 이하가 되면 안됨
              도착지부터 출발지까지 역방향으로 이동하며, 최소 Stat를 찾는다

              포인트: 원래 던전 크기보다 +1씩 배열값을 초기화
                      도착지 [m-1][n-1]근처는 1로 초기화 하여 계산 (경계값 처리 줄이기)

2. 시간복잡도 : O(M * N)

3. 자료구조/알고리즘 : 이차원  DP

 */

class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;

        int[][] dp = new int[m+1][n+1];
        for(int i = 0; i <= m; i++) {
            for(int j = 0; j <= n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }

        dp[m][n-1] = 1;
        dp[m-1][n] = 1;

        for(int i=m-1; i>=0; i--) {
            for(int j=n-1; j>=0; j--) {
                int a = dp[i][j+1];
                int b = dp[i+1][j];
                int status = dungeon[i][j];

                dp[i][j] = Math.max(1, Math.min(a, b) - status);
            }
        }

        return dp[0][0];
    }
}