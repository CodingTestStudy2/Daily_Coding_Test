/*

1. 아이디어 : 현재 숫자 기준 뒤의 홀수, 짝수 개수 파악
            뒤부터 탐색하여, 현재 숫자가 짝수면, 현재까지 홀수들의 개수를
            현재 숫자가 홀수면, 현재까지 짝수들의 개수를 저장한다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : DP

 */

class Solution {
    public int[] countOppositeParity(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        int oddCnt = 0;
        int evenCnt = 0;

        for(int i=n-1; i>=0; i--) {
            if(nums[i]%2==0) {
                ans[i] = oddCnt;
                evenCnt++;
            }
            else {
                ans[i] = evenCnt;
                oddCnt++;
            }
        }

        return ans;
    }
}