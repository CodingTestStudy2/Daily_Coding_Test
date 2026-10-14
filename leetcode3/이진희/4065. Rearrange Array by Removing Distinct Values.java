class Solution {
    public int[] rearrangeArray(int[] nums) {
        // 오름차 순이어야함
        // 연속 같은 수 금지

        // 숫자 범위 1 ~ 100
        int[] cnt = new int[101];
        int[] ans = new int[nums.length];

        for(int i=0; i<nums.length; i++) cnt[nums[i]]++;

        int pos = 0;

        for(int i=0; i<101; i++) {
            for(int j=0; j<101; j++) {
                if(cnt[j]>0) {
                    ans[pos++] = j;
                    cnt[j]--;
                } 
                if(pos == nums.length) break;
            }
        } 

        return ans;
    }
}