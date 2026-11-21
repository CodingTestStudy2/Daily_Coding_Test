class Solution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        long maxSum = 0;
        int count = 0;
        int minDiff = Integer.MAX_VALUE;

        for (int num : nums) {
            int xorVal = num ^ k;
            if (xorVal > num) {
                maxSum += xorVal;
                count++;
                minDiff = Math.min(minDiff, xorVal - num);
            } else {
                maxSum += num;
                minDiff = Math.min(minDiff, num - xorVal);
            }
        }

        if (count % 2 == 1) {
            maxSum -= minDiff;
        }

        return maxSum;
    }
}