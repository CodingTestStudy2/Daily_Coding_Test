/* 

1. 아이디어 : 1개만 존재하는 짝수중 가장 앞쪽의 수 반환. 완전탐색을 통해 미리 각 짝수의 개수를 구하고, 다시 사전식으로 돌려 판단

2. 시간복잡도 : O(2*N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int firstUniqueEven(int[] nums) {
        // 정확히 한번 등장하는 사전순으로 가장 빠른 짝수 idx 
        // 없다면 -1

        int[] cnt = new int[101];

        for(int i=0; i<nums.length; i++) {
            if(nums[i]%2==1) continue;
            cnt[nums[i]]++;
        }

        for(int i=0; i<nums.length; i++) {
            if(cnt[nums[i]] == 1) return nums[i];
        }

        return -1;
    }
}