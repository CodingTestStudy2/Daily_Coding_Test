/*

1. 아이디어 : 절댓값이 제일작은 값 구하기
            절댓값이 같으면 양수가 답

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int findClosestNumber(int[] nums) {
        // 0과 가장 가까운수 
        // 절댓값이 같다면 더 큰 수 

        int ans = 0;
        int diff = 1000000;

        for(int i : nums) {
            int abs = Math.abs(i);

            if(abs < diff) {
                diff = abs;
                ans = i;
            }
            else if(diff == abs) {
                if(i>ans) ans = i;
            }
        }

        return ans;
    }
}