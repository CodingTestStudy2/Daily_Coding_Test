class Solution {
    public int sumOfEncryptedInt(int[] nums) {
        int sum = 0;

        for (int num : nums) sum += encrypt(num);
        
        return sum;
    }

    private int encrypt(int x) {
        int maxNum = 0;
        int len = 0;
        
        int tmp = x;
        while (tmp > 0) {
            int digit = tmp % 10;
            if (digit > maxNum) {
                maxNum = digit;
            }
            len++;
            tmp /= 10;
        }
        
        int ans = 0;
        for (int i = 0; i < len; i++) {
            ans = ans * 10 + maxNum;
        }
        
        return ans;
    }
}