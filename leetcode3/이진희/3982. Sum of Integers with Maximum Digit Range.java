/*

1. 아이디어 : 각 nums 배열 숫자의 원소의 최대 최소의 차중 가장 큰 값의 합을 구하기
              완전탐색으로 모든 숫자 속 원소의 최대 최소 차를 구한 후, 가장 큰 값만 더해줌
              
              maxLen 변수를 선언해, 그 변수보다 큰 차가 나올경우 지금까지 계산한 값을 0으로 초기화

2. 시간복잡도 : O(100*5)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int maxDigitRange(int[] nums) {

        int len = nums.length;
        int maxLen = -1;
        int ans = 0;

        for(int i=0; i<len; i++) {
            int n = nums[i];

            int max = 0;
            int min = 100001;

            while(n>0) {
                int tmp = n%10;
                max = Math.max(tmp, max);
                min = Math.min(tmp, min);

                n/=10;
            }

            int diff = max-min;
            if(diff<maxLen) continue;
            else if(diff>maxLen) {
                ans = 0;
                maxLen = diff;
            }

            ans+=nums[i];
        }

        return ans;
    }
}