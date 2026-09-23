// O(3n)

class Solution {
    public int tribonacci(int n) {
        if (n <= 1) return n;

        int[] num = new int[n+1];
        num[1] = 1; num[2] = 1;
        if (n == 2) return num[2];

        for (int i = 3; i<=n; i++) {
            for (int k = i-3; k<i; k++) num[i] += num[k];
        }
        return num[n];
    }
}
