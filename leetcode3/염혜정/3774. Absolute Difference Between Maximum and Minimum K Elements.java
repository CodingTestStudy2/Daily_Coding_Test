// 오름차순 정렬 후 0 ~ k / nums.length - k
// O(n)

class Solution {
    public int absDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int large = 0;
        int small = 0;

        for (int i = 0; i< k; i++) large += nums[i];
        for (int i = nums.length-1; i>=nums.length-k; i--) small += nums[i];

        return (int) Math.abs(large - small);
    }
}
