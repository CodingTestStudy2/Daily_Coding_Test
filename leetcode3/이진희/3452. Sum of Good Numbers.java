/*

1. 아이디어 : k만큼 떨어진 양 옆의 수보다 큰 원소의 합 구하기
              이때 배열 범위를 벗어낫다면 무조건 더 크다고 판별

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int sumOfGoodNumbers(int[] nums, int k) {
        int sum = 0;
        for(int i=0; i<nums.length; i++){
            int left = (i-k)<0 ? 0 : nums[i-k];
            int right = (i+k)>nums.length-1 ? 0 : nums[i+k];

            if(nums[i] > left && nums[i] > right) sum+=nums[i];
        }

        return sum;
    }
}