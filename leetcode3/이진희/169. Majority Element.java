/*

1. 아이디어 : 공간복잡도를 O(1)로 유지하기 위해, 배열을 미리 정렬 후 완전탐색
             9ms, 37.40%가 나왔으므로, 좋은 풀이는 아닌것같음..

2. 시간복잡도 : O(NlogN)

3. 자료구조/알고리즘 : 완전탐색, 정렬

 */

class Solution {
    public int majorityElement(int[] nums) {
        int idx = 0;
        double base = (double)nums.length/2; 
        int cnt = 1;

        for(int i=1; i<nums.length; i++) {
            int num = nums[idx];
            
            if(cnt > base) return second;
            if( != second) {
                idx = i;
            }
            else cnt++; 
        }

        return nums[idx];
    }
}