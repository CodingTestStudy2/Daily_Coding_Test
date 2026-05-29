/*

1. 아이디어 : 완전탐색으로 조건을 만족하는 최소 인덱스를 구한다

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int minAbsoluteDifference(int[] nums) {
        // 조건을 만족하는 최소 절댓값
        // i == 1, j == 2
        // 순서 상관 없음

        return findMinDiff(nums);
    }

    private int findMinDiff(int[] nums) {
        // 0, 1, 2만 존재
        int ans = 1000;
        for(int i=0; i<nums.length-1; i++) {
            for(int j=i+1; j<nums.length; j++) {
                if((nums[i] == 1 && nums[j] == 2) || (nums[i] == 2 && nums[j] == 1)) {
                    ans = Math.min(ans, Math.abs(i-j));
                }
            }
        }

        if(ans == 1000) return -1;
        else return ans;
    }
}