/*

1. 아이디어 : 100이하의 정렬되지 않은 수에서 빠진 수를 찾는다
              이때 최대값과, 최소값은 빠지지 않는다

              boolean배열로 미리 크기를 선언 후, 완전탐색으로 존재하는 수를 체크한다
              이후, boolean배열을 탐색해, 빠진 수를 찾는다

2. 시간복잡도 : O(N) + O(N) => O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        boolean[] check = new boolean[101];

        int start = 200;
        int end = 0;
        for(int i=0; i<nums.length; i++) {
            check[nums[i]] = true;
            start = Math.min(start, nums[i]);
            end = Math.max(end, nums[i]);
        }

        List<Integer> ans = new ArrayList<>();
        for(int idx=start; idx<=end; idx++) {
            if(!check[idx]) ans.add(idx);
        }

        return ans;
    }
}