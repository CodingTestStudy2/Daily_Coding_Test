
/*

1. 아이디어 : 정렬 상태에서 인접한 원소의 최대 차이를 구하면 된다

2. 시간복잡도 : O(NlogN) + O(N) => O(NlogN)

3. 자료구조/알고리즘 : 정렬 + 완전탐색

 */

class Solution {
    public int maximumGap(int[] nums) {
        //최대 10만
        return solve(nums);
    }

    private int solve(int[] nums) {
        if(nums.length<2) return 0;
        Arrays.sort(nums);
        int maxDiff = -1;

        for(int i=0; i<nums.length-1; i++) {
            maxDiff = Math.max(maxDiff, nums[i+1]-nums[i]);
        }

        return maxDiff;
    }
}