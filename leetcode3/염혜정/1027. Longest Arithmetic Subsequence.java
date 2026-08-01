// 시간복잡도 O(N^2)

import java.util.Arrays;

class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;

        // dp[i][diff + 500]: i번째 원소로 끝나고 공차가 diff인 등차수열의 최대 길이
        // 공차 범위: -500 ~ 500 -> offset 500을 더해 0 ~ 1000 범위로 변환
        int[][] dp = new int[n][1001];
        
        // 최소 등차수열의 길이는 2 (원소 2개만 모여도 공차가 형성됨)
        int maxLength = 2;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // 두 원소의 차이 계산 후 offset 처리
                int diff = nums[i] - nums[j] + 500;

                // j번째에서 이전 길이를 가져오고, 없었다면 기본 길이 1에서 시작하여 + 1
                int previousLength = dp[j][diff] > 0 ? dp[j][diff] : 1;
                
                dp[i][diff] = previousLength + 1;
                
                // 최대 길이 갱신
                maxLength = Math.max(maxLength, dp[i][diff]);
            }
        }

        return maxLength;
    }
}