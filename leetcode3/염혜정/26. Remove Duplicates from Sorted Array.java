// 투포인터
// O(n)

class Solution {
    public int removeDuplicates(int[] nums) {
        int now = 1;
        for (int next = 1; next<nums.length; next++) {
            if (nums[next] != nums[now-1]) {
                nums[now] = nums[next];
                now++;
            }
        }
        return now;
    }
}
