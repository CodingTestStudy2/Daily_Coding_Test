/*

1. 아이디어 : 왼쪽과 오른쪽을 각각 계산하여, 현재 값이 모든 왼쪽 값보다 큰지, 현재 값이 모든 오른쪽 값보다 큰지 체크
            boolean 배열에 표시해 뒀다가 마지막에 계산 

2. 시간복잡도 : O(3*N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public List<Integer> findValidElements(int[] nums) {

        List<Integer> ans = new ArrayList<>();
        boolean[] check = new boolean[nums.length];

        check[0] = true;
        check[nums.length-1] = true;
        
        int leftMax = nums[0];
        for(int i=1; i<nums.length; i++){
            if(nums[i] > leftMax) check[i] = true;
            leftMax = Math.max(leftMax, nums[i]);
        }

        int rightMax = nums[nums.length-1];
        for(int i=nums.length-2; i>=0; i--){
            if(nums[i] > rightMax) check[i] = true;
            rightMax = Math.max(rightMax, nums[i]);
        }

        for(int i=0; i<nums.length; i++){
            if(check[i]) ans.add(nums[i]);
        }

        return ans;
    }
}