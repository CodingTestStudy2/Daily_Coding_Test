/*

1. 아이디어 : 왼쪽부터 탐색하며 가장 큰 수, 오른쪽부터 탐색하며 가장 작은수를 구하고,
            각 배열의 인덱스 i기준 가장 큰 수 와, 작은 수를 미리 저장,
            저장 된 값 기반 다시 탐색하며 조건을 만족하는 가장 작은 인덱스 i 구하기

2. 시간복잡도 : O(N) + O(N) => O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int firstStableIndex(int[] nums, int k) {
       
        return findSmallestStableIndex(nums, k);
    }

    static int findSmallestStableIndex(int[] nums, int k) {
        
        int smallestNum = -1;
        int[] leftMax = new int[nums.length];
        int[] rightMin = new int[nums.length];
        int currMaxNum = -1;
        int currMinNum = Integer.MAX_VALUE;

        for(int i=0; i<nums.length; i++) {
            if(currMaxNum<nums[i]) {
                currMaxNum = nums[i];
            }
            leftMax[i] = currMaxNum;

            if(currMinNum>nums[nums.length-1-i]) {
                currMinNum = nums[nums.length-1-i];
            }
            rightMin[nums.length-1-i] = currMinNum;
        }

        for(int i=0; i<nums.length; i++) {
            if(leftMax[i] - rightMin[i] <= k) {
                smallestNum = i;
                break;
            }
        }

        return smallestNum;
    }
}