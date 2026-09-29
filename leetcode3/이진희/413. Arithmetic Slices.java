/* 

1. 아이디어 : 등차수열의 모든 부분배열을 구하므로, 각 원소를 차례대로 완전탐색하며 3개 이상의 원소가 차이가 같은지 확인
            같을 경우, 미리 구해둔 경우의 수로 계산해준다.

2. 시간복잡도 : O(2N)

3. 자료구조/알고리즘 : 누적합, 완전탐색

 */

class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        // 모든 등차수열 구하기
        // 최소 3개의 원소 

        // 1 2 3 5 7 10 13 17 21 25

        if(nums.length < 3) return 0;

        int ans = 0;
        int cnt = 2;
        int diff = nums[1] - nums[0];

        int[] sum = new int[nums.length+1];
        for(int i=3; i<=nums.length; i++) {
            sum[i] = sum[i-1] + (i-2); 
        }

        for(int i=2; i<nums.length; i++) {
            if((nums[i] - nums[i-1]) != diff) {
                ans+=sum[cnt];
                cnt = 2;
                diff = nums[i] - nums[i-1];
            }
            else cnt++;
        }

        if(cnt > 2) {
            ans+=sum[cnt];
        }

        return ans;
    }
}