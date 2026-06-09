/*

1. 아이디어 : 증가 -> 감소 -> 증가 순으로 반드시 배열이 유지되어야 함
              idx를 증가시키며 각각의 구간을 만족하는지 확인한다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public boolean isTrionic(int[] nums) {
        
        int idx = 0;

        while(idx < nums.length-1 && nums[idx]<nums[idx+1]) idx++;

        if(idx == 0) return false;

        while(idx < nums.length-1 && nums[idx]>nums[idx+1]) idx++;

        if(idx == nums.length-1) return false;

        while(idx < nums.length-1 && nums[idx]<nums[idx+1]) idx++;

        if(idx == nums.length-1) return true;
        else return false;
    }
}