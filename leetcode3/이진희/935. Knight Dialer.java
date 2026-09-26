import java.util.Arrays;

class Solution {
    private static final int MOD = 1_000_000_007;
    private final int[][] moves = {
        {4, 6}, {6, 8}, {7, 9}, {4, 8}, {0, 3, 9},
        {}, {0, 1, 7}, {2, 6}, {1, 3}, {2, 4}
    };
    
    private int[][] memo;

    public int knightDialer(int n) {
        if (n == 1) return 10;

        memo = new int[n + 1][10];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        int totalWays = 0;
     
        for (int i = 0; i < 10; i++) {
            totalWays = (totalWays + backtrack(n - 1, i)) % MOD;
        }

        return totalWays;
    }

    private int backtrack(int remain, int digit) {
      
        if (remain == 0) {
            return 1;
        }

      
        if (memo[remain][digit] != -1) {
            return memo[remain][digit];
        }

        int count = 0;
        for (int nextDigit : moves[digit]) {
            count = (count + backtrack(remain - 1, nextDigit)) % MOD;
        }

        return memo[remain][digit] = count;
    }
}