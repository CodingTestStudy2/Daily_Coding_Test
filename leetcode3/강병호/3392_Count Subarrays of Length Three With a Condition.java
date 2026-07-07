import java.util.Arrays;

class Solution {
    public int countSubarrays(int[] nums) {
        // the sum of the first and third numbers == second number
        // Sliding window

        int ans = 0;
        
        for (int i = 1; i < nums.length-1; i++) {
            if ((nums[i-1] + nums[i+1]) * 2 == nums[i]) ans++;
        }

        return ans;
        
    }
}