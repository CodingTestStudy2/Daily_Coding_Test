/*

1. 아이디어 : 1차는 left=0, right=1로두고 양 벽을 찾으려고 생각, 하지만 맨 마지막에 벽이 없을경우 조건이 복잡해짐
            2차는 left=0, right=len-1로 두고, 좌우 벽중 더 좁은 쪽으로 좁혀들어가며 계산.

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 투포인터

 */
class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length-1;

        int maxLeftH = height[left];
        int maxRightH = height[right];

        int sum = 0;
        int diff = 0;
        while(left < right) {
            if(maxLeftH<maxRightH) {
                left++;
                diff = maxLeftH-height[left];
                
                if(diff>0) sum+=diff;
                maxLeftH = Math.max(maxLeftH, height[left]);
            }
            else {
                right--;
                diff = maxRightH - height[right];
                
                if(diff>0) sum+=diff;
                maxRightH = Math.max(maxRightH, height[right]);
            }
        }
        return sum;
    }
}