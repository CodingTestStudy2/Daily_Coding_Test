/*

1. 아이디어 : 완탐으로 배열 안의 0의 개수 세기, 배열 뒤부터 0의 개수 만큼 0이 존재하는지 파악 -> 0이 없다면, 교환해야하므로 +1 

2. 시간복잡도 : O(100 + 100) => O(200)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int minimumSwaps(int[] nums) {
        //0을 배열 끝으로 이동
        //최소한의 이동
        int cnt = 0;
        int ans = 0;

        for(int i : nums) {
            if(i == 0) cnt++;
        }

        for(int i=nums.length-cnt; i<nums.length; i++) {
            if(nums[i] != 0) ans++;
        }

        return ans;
    }
}