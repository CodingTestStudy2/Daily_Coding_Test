/*

1. 아이디어 : 배열의 숫자를 반전한뒤 기록한다
            각 숫자의 위치가 고정되어 있으므로, O(N)으로 한번에 계산 가능

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 단순계산

 */

class Solution {
    public int[] concatWithReverse(int[] nums) {
        int[] ans = new int[nums.length*2];

        for(int i=0; i<nums.length; i++) {
            ans[i] = nums[i];
            ans[nums.length*2-1-i] = nums[i];
        }

        return ans;
    }
}