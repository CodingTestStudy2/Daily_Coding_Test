// 자릿수들 중에 최대값을 구한 뒤 자릿수 만큼 1로 이루어진 값과 곱한 뒤 합
// O(N)

class Solution {
    public int sumOfEncryptedInt(int[] nums) {
        int result = 0;
        for (int num : nums) {
            int max = 0;
            int ones = 0;
            while (num > 0) {
                int digit = num % 10;
                max = Math.max(max, digit);
                ones = ones * 10 + 1;
                num /= 10;
            }
            result += max * ones;
        }
        return result;
    }
}
