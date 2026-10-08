/*

1. 아이디어 : 
   문자열에서 중복된 원소를 빼고 재배치, 고유한 원소 크기 반환

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int removeDuplicates(int[] nums) {
        int prev = -200;
        int idx = 0;

        // 오름차순
        for(int i : nums) {
            if(i == prev) continue;
            nums[idx++] = i;
            prev = i;
        }

        return idx;
    }
}