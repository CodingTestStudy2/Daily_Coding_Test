/*

1. 아이디어 : 투포인터, 정렬 후 for문을 통해 숫자 고정, 이후 투포인터로 값찾기

2. 시간복잡도 : O(NlogN)*O(N) -> O(N^2)

3. 자료구조/알고리즘 : 투포인터

 */

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);

        for(int i=0; i<nums.length-2; i++) {
            if(i>0 && nums[i] == nums[i-1]) continue;

            int left = i+1;
            int right = nums.length-1;

            while(left<right) {
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0) {
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    left++;
                    right--;
                }
                else if(sum < 0) left++;
                else right--;
            }
        }
        return ans;
    }
}