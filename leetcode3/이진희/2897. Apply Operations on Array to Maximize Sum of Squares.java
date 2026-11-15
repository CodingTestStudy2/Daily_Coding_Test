/*  
    시간 초과로 실패, 다시 풀어볼 예정...
 */


class Solution {
    private static final int MOD = 1_000_000_007;
    private static final int BITS = 30;

    public int maxSum(List<Integer> nums, int k) {
        int[] bitCount = new int[BITS];

        for (int num : nums) {
            for (int b = 0; b < BITS; b++) {
                if ((num & (1 << b)) != 0) {
                    bitCount[b]++;
                }
            }
        }

        long ans = 0;
        for (int i = 0; i < k; i++) {
            long current = 0;
            for (int b = 0; b < BITS; b++) {
                if (bitCount[b] > 0) {
                    current |= (1L << b);
                    bitCount[b]--;
                }
            }
            long sq = (current % MOD) * (current % MOD) % MOD;
            ans = (ans + sq) % MOD;
        }

        return (int) ans;
    }
}