/*

1. 아이디어 : 
   n을 1부터 4까지 직접 경우의 수를 구한 후, 수학적 규칙을 찾아 계산

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : DP

 */

class Solution {
    public int climbStairs(int n) {

        // 1 2 3 5
        // 22 1111 211 -> 5
        
        if(n == 1) return 1;
        if(n == 2) return 2;
        
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;

        for(int i=3; i<=n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];

    }
}