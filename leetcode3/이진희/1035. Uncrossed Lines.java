/* 

1. 아이디어 : DP를 활용한다. 가장 많이 선을 그을 수 있는 경우를 구한다.
              각 단계의 경우는 이전단계에 영향을 받으므로 DP를 활용한다.

2. 시간복잡도 : ON*M) (nums1.length = N, nums2.length = M)

3. 자료구조/알고리즘 : DP

 */

class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int[][] dp = new int[nums1.length+1][nums2.length+1];

        for(int i=1; i<=nums1.length; i++) {
            for(int j=1; j<=nums2.length; j++) {
                // 연결 가능할 때
                if(nums1[i-1] == nums2[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
                // 연결할 수 없을 때
                else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }

        return dp[nums1.length][nums2.length];

    }
}