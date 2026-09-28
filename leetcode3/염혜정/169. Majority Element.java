// O(n)

class Solution {
    public int majorityElement(int[] nums) {
        int now = nums[0];
        int cnt = 1;
        for (int i = 1; i<nums.length; i++) {
            if (nums[i] != now) {
                if (cnt > 0) cnt--;
                else {
                    now = nums[i];
                    cnt++;
                }
            } else {
                cnt++;
            }
        }
        return now;
    }
}
