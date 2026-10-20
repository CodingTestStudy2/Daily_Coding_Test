/* 

1. 아이디어 : 피보나치 배열을 실제로 구해서 계산

2. 시간복잡도 : O(250쯤..) - 10억

3. 자료구조/알고리즘 : 배열, 누적합

 */

class Solution {
    public boolean threeFibonacciSum(int n) {
        // 10억
        // 연속된 3개의 원소 합

        int[] dp = new int[250];

        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 1;

        for(int i=2; i<250; i++) {
            dp[i] = dp[i-1] + dp[i-2];
            
            int sum = dp[i] + dp[i-1] + dp[i-2];
            if(sum > n) break;
            if(sum == n) return true;
        }
        return false;
    }
}