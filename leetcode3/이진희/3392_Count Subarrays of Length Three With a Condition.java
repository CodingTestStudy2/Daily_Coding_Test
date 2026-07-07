/*

1. 아이디어 : 3개 크기의 부분 배열을 잘라 [a,b,c] -> b = (a*c)*2를 확인
              슬라이딩 윈도우 방법 사용

2. 시간복잡도 : O(N-2)

3. 자료구조/알고리즘 : 슬라이딩 윈도우

 */

class Solution {
    public int countSubarrays(int[] nums) {
        int ans = 0;
        for(int i=0; i<nums.length-2; i++) {
            int a = nums[i];
            int b = nums[i+1];
            int c = nums[i+2];

            if(b == 2*(a+c)) ans++;
        }

        return ans;
    }
}