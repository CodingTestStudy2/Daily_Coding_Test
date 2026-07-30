/* 

1. 아이디어 : 0과 1로 이루어진 배열에서 최대 k만큼 0을 1로 만들었을때 가장 연속된 1의 길이를 구한다. 
              최대 10만의 길이므로 O(N)안에서 해결해야 하며, 슬라이딩 윈도우 방식을 사용해 
              left, right idx를 선언후, 구간 안의 0의 개수에 따라 left값을 조정하여 구할 수 있다.

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 슬라이딩 윈도우

 */

class Solution {
    public int longestOnes(int[] nums, int k) {
        // 0을 뒤집었을때 최대 연속된 1이 나오도록
        // 0은 최대 k만큼 뒤집기 가능

        // nums, k 최대 10만

        int cnt = 0;
        int l = 0;
        int ans = 0;

        for(int r=0; r<nums.length; r++) {
            if(nums[r] == 0) cnt++;

            if(cnt>k) {
                if(nums[l] == 0) cnt--;
                l++;
            }

            ans = Math.max(ans, r-l+1);
        }

        return ans;
    }
}