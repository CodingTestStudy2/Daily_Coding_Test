/*
1. 아이디어:
   - 2차원 DP 테이블 dp[i][diff]를 활용하여 i번째 원소로 끝나고 공차가 diff인 등차수열의 최대 길이를 기록
   - 이전 상태 dp[j][diff]가 존재하면 +1을 하고, 없으면 기본 길이 2로 초기화하며 최대 길이를 갱신

2. 시간복잡도: O(N^2)

3. 자료구조/알고리즘: DP
*/

class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        int maxLen = 2;
        
        int OFFSET = 500;
        int[][] dp = new int[n][1001];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = nums[i] - nums[j] + OFFSET;
                
                if (dp[j][diff] > 0) dp[i][diff] = dp[j][diff] + 1;
                else dp[i][diff] = 2;
                
                maxLen = Math.max(maxLen, dp[i][diff]);
            }
        }

        return maxLen;
    }
}