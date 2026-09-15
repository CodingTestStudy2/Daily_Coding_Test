// O(n)

class Solution {
    public int climbStairs(int n) {
        int[] cnt = new int[n+1];
        cnt[1] = 1;
        if (n >= 2) cnt[2] = 2;

        for (int i = 3; i<=n; i++) {
            cnt[i] = cnt[i-1] + cnt[i-2];
        }
        return cnt[n];
    }
}
