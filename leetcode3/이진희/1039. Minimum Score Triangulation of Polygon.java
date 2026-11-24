/* 

1. 아이디어 : 삼각형을 i k j 로 만든다면 i~k, k~j 사이의 더 작은 삼각형으로 반복 -> 그 값을 메모제이션으로 풀이
            dp[i][j] => 점 i,j를 한 변으로 하는 모든 삼각형 k의 최소 비용
            bottom-up은 떠오르지 않아 top-down 방식으로 직관적으로 풀이

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : dp

 */

class Solution {
    private int[][] dp;
    private int n;
    private int[] values;
    
    public int minScoreTriangulation(int[] values) {
        this.values = values;
        n = values.length;
        dp = new int[n][n];

        return top_down(0, n-1);
    }

    private int top_down(int i, int j) {
        if(j-i<2) return 0;
        if(dp[i][j] != 0) return dp[i][j];

        int min = Integer.MAX_VALUE;
        for(int k = i+1; k<j; k++) {
            int cost = top_down(i,k) + top_down(k,j) + values[i]*values[j]*values[k];
            min = Math.min(min, cost);
        }

        return dp[i][j] = min;
    }
}