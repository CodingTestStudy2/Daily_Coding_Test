// O(n)

class Solution {
    public int maxDigitRange(int[] nums) {
        int n = nums.length;
        int[] range = new int[n];
        int maxRange = -1;

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            int maxDigit = -1, minDigit = -1;
            if (num == 0) {
                maxDigit = minDigit = 0;
            }
            while (num > 0) {
                int digit = num % 10;
                num /= 10;
                if (maxDigit == -1 || digit > maxDigit) maxDigit = digit;
                if (minDigit == -1 || digit < minDigit) minDigit = digit;
            }
            range[i] = maxDigit - minDigit;
            maxRange = Math.max(maxRange, range[i]);
        }

        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (range[i] == maxRange) sum += nums[i];
        }
        return sum;
    }
}
