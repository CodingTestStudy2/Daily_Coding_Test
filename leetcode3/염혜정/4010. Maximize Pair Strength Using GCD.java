// O(n^2)

class Solution {
    public long maxPairStrength(int[] nums) {
        long max = 0;
        for (int i = 0; i<nums.length-1; i++) {
            for (int k = i+1; k<nums.length; k++) {
                long gcd = gcd(nums[i], nums[k]);
                long cal = ((long) nums[i] * nums[k]) / (gcd * gcd);
                max = Math.max(max, cal);
            }
        }
        return max;
    }

    public long gcd(long a, long b) {
        while (b>0) {
            long temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }
}
