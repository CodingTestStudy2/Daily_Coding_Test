/*

1. 아이디어 : 각 인덱스 기준 i+1부터 배열끝까지 합을 누적합으로 계산
              누적된 값의 평균이 배열 i보다 더 작다면 값 증가

2. 시간복잡도 : O(2N)

3. 자료구조/알고리즘 : 누적합

 */

class Solution {
    public int dominantIndices(int[] nums) {
        int[] cnt = new int[nums.length];
        int ans = 0;

        // len-2 ~ 0까지
        for(int i=nums.length-2; i>=0; i--) cnt[i]= cnt[i+1] + nums[i+1];

        for(int i=0; i<nums.length-1; i++) {
            double avg = (double)cnt[i]/(nums.length-1-i);
            if(nums[i]>avg) ans++;
        }

        return ans;
    }
}