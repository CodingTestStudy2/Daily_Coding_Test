class Solution {
    public boolean isMiddleElementUnique(int[] nums) {
        int middle = (nums.length - 1) / 2;
        int cnt = 0;
        for (int num : nums) {
            if (num == nums[middle]) cnt++;
            if (cnt == 2) break;
        }
        return cnt == 1;
    }
}
