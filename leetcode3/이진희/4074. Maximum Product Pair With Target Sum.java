/*

1. 아이디어 : 조건을 만족하는 원소쌍중 가장 큰 값 구하기
             i,j의 순서는 더 큰 원소 idx가 먼저와야함을 명심

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : 완전탐색

 */


class Solution {
    public int[] maxProductPair(int[] nums, int target) {
        // 조건을 만족하는 모든 pair중 nums[i] * nums[j]이 가장 큰 값
        // 없으면 [-1, -1]

        int[] ans = {-1, -1};
        int maxVal = Integer.MIN_VALUE;

        for(int i=0; i<nums.length-1; i++) {
            for(int j=i+1; j<nums.length; j++) {
                int iVal = nums[i];
                int jVal = nums[j];

                if((iVal + jVal) != target || iVal == jVal) continue;
                if(jVal*iVal > maxVal) {
                    maxVal = jVal*iVal;
                    
                    if(jVal>iVal) {
                        ans[0] = j;
                        ans[1] = i;
                    }
                    else {
                        ans[0] = i;
                        ans[1] = j;
                    }
                }
            }
        }

        return ans;
    }
}