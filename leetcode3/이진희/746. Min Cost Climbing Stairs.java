/* 

1. 아이디어 : 계단 1칸 or 2칸 오르고, 최소비용 구하기

            dp로 직전위치까지의 최소 비용 계산후 값 반환

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : DP

 */

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // 1개 or 2개

        int[] dp = new int[cost.length+1];

        dp[1] = cost[0];
        dp[2] = cost[1];

        for(int i=3; i<cost.length+1; i++) {
            dp[i] = cost[i-1] + Math.min(dp[i-1], dp[i-2]);
        }

        int ans = Math.min(dp[cost.length], dp[cost.length-1]);

        return ans;
    }
}