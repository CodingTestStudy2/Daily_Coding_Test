// nums[0] ~ nums[length -1] 합으로 평균을 구함
// O(n)

class Solution {
    public int dominantIndices(int[] nums) {
        if (nums.length == 1) return 0;

        int sum = 0;
        for (int i = 0; i<nums.length; i++) sum += nums[i];

        int cnt = 0;
        for (int i = 0; i<nums.length-1; i++) {
            sum -= nums[i];
            float avg = sum / (nums.length - i - 1);
            if (nums[i] > avg) cnt++;
        }
        return cnt;
    }
}
