/*

1. 아이디어 : 배열을 순회하며, 현재 값 개수가 k 이상이면 continue, 이하면 붙인다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int[] limitOccurrences(int[] nums, int k) {

        int[] ans = new int[nums.length];

        int prev = nums[0];
        ans[0] = prev;

        int cnt = 1;
        int idx = 1;
        int len = 0;

        for(int i=1; i<nums.length; i++) {
            if(prev == nums[i] && cnt == k) continue;
            else if(prev != nums[i]) {
                prev = nums[i];
                cnt = 1;
                ans[idx++] = nums[i]; 
            }
            else {
                ans[idx++] = nums[i];
                cnt++;
            }
            len++;
        }

        return Arrays.copyOfRange(ans, 0, len+1);
    }
}