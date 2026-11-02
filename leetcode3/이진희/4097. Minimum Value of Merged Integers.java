class Solution {
    public int minMergedInteger(int[] nums) {
        int ans = Integer.MAX_VALUE;
        int num = 0;
        for(int i=0; i<nums.length; i+=2) {
            int tmp = nums[i+1];
            num = nums[i];
            while(tmp>0) {
                num*=10;
                tmp/=10;
            }   
            num += nums[i+1];
            ans = Math.min(ans, num);
        }

        return ans;
    }
}