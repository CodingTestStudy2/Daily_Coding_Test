/*

1. 아이디어 : 정렬후, Set을 사용해 파악

2. 시간복잡도 : O(NlogN) + O(N) = O(NlogN)

3. 자료구조/알고리즘 : 정렬, Set

 */

class Solution {
    public int[] maxKDistinct(int[] nums, int k) {
        //내림차 순 반환
        //중복 선택 안됨

        int[] ans = new int[k];
        int idx = 0;
        Set<Integer>set = new HashSet<>();

        Arrays.sort(nums);
        for(int i=nums.length-1; i>=0; i--) {
            if(set.size()==k) break;
            if(set.contains(nums[i])) continue;
            set.add(nums[i]);
            ans[idx++] = nums[i];
        }

        return Arrays.copyOfRange(ans,0,idx);
    }
}