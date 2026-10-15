// O(n)

class Solution {
    public int findClosestNumber(int[] nums) {
        int min = Integer.MAX_VALUE;
        for (int num : nums) {
            if (Math.abs(min) > Math.abs(num)) min = num;
            else if (Math.abs(min) == Math.abs(num)) {
                if (min < num) min = num; 
            }
        }
        return min;
    }
}
