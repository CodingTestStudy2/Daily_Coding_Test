/*

1. 아이디어 : k개의 큰수의합와 k개의 작은수의 합을 구해 차이값을 구하기
              정렬 후, K번만큼 for문을 돌려 큰수와 작은수의 합을 구하고 빼준다
               

2. 시간복잡도 : O(NlogN + K)

3. 자료구조/알고리즘 : 계산

 */

class Solution {
    public int absDifference(int[] nums, int k) {
        // k개의 가장 크고 작은 수 

        Arrays.sort(nums);
        int maxSum = 0;
        int minSum = 0;

        for(int i=0; i<k; i++) {
            maxSum+=nums[nums.length-1-i];
            minSum+=nums[i];
        }

        return maxSum-minSum;

    }
}