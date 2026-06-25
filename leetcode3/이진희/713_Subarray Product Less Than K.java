/*

1. 아이디어 : 주어진 배열에서 모든 원소의 곱이 k를 넘지 않는 연속된 부분배열의 개수를 구한다.
              1. 완전탐색으로 배열의 오른쪽 숫자를 순차적으로 곱함
              2. 곱이 k개 이상이면 왼쪽 숫자를 뺌
              3. 최종적으로 right-left+1를 하여 현재 만들수있는 연속 부분배열을 찾아서 더함

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 슬라이딩 윈도우

 */

class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        // 곱이 k보다 작은 nums의 연속 부분집합
        // 전부 양수 

        if(k <= 1) return 0;

        int ans = 0;
        int l = 0;
        int sum = 1;
        
        for(int r=0; r<nums.length; r++) {
            sum*=nums[r];

            while(sum >= k) {
                sum/=nums[l];
                l++;
            }

            int cnt = r-l+1;
            ans+=cnt;
        }

        return ans;
    }
}