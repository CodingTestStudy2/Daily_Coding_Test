// 짝수는 더하고 홀수는 빼기
// o(n)

class Solution {
    public int alternatingSum(int[] nums) {
        int sum = 0;
        for (int i = 0; i<nums.length; i++) {
            if (i%2 == 0) sum += nums[i];
            else sum -= nums[i];
        }
        return sum;
    }
}
