/*

1. 아이디어 : 모든 k구간을 완전탐색으로 돌며 등장하는 구간 안 중복되지 않은 숫자를 각각 카운트, 가장 큰 수 반환 
              슬라이딩 윈도우 기법으로 풀려고 했지만, 중복된 숫자가 등장하는 경우를 처리하기가 까다로워 완전탐색으로 품

2. 시간복잡도 : O(N*K+50)

3. 자료구조/알고리즘 : 완전탐색, Set

 */

class Solution {
    public int largestInteger(int[] nums, int k) {
        int[] cnt = new int[51];
        for(int i=0; i<=nums.length-k; i++) {
            Set<Integer> set = new HashSet<>();
            for(int j=i; j<i+k; j++) {
                if(set.contains(nums[j])) continue;
                set.add(nums[j]);
                cnt[nums[j]]++;
            }
        }

        for(int i=50; i>=0; i--) {
            if(cnt[i] == 1) return i;
        }

        return -1;
    }
}