/*

1. 아이디어 : dp 활용
              박스가 2개 이상일때 합치며 가장 큰 포인트를 구해야한다.
              이때 구간 [a,b]에서도 서로 다른 경우의 수가 존재한다.
              
              dp[a][b][k]를 선언하여 - 구간 [a,b]에서 이미 박스[b]와 같은 색깔의 박스가 k개 존재한다고 가정.
              dfs를 통해 0, length-1으로 들어가고, 더 작은 구간을 재귀적으로 계산하는 top-down 방식으로 dp를 채운다.

2. 시간복잡도 : O(N^4) - 최대 N^3의 상태가 존재하고, 각 상태마다 같은 색 후보를 찾기 위해 최대 N개의 위치를 탐색

3. 자료구조/알고리즘 : DP, DFS

 */

class Solution {
    private int[][][] dp;
    public int removeBoxes(int[] boxes) {

        // 전부 없엤을때 가장 높은 포인트
        dp = new int[boxes.length][boxes.length][boxes.length];
        int ans = dfs(0,boxes.length-1,0,boxes);

        return ans;
    }

    private int dfs(int a, int b, int k, int[] boxes) {
        
        if(a>b) return 0;

        if(dp[a][b][k] != 0) return dp[a][b][k];
        
        dp[a][b][k] = dfs(a,b-1,0,boxes) + (k+1)*(k+1);

        for(int i=a; i<b; i++) {
            if(boxes[i] == boxes[b]) {
                int score = dfs(a, i, k+1, boxes) + dfs(i+1, b-1, 0, boxes);
                dp[a][b][k] = Math.max(dp[a][b][k], score);
            }
        }

        return dp[a][b][k];
    }
}