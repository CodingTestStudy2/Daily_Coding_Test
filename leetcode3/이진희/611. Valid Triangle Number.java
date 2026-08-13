/*

1. 아이디어 : 삼각형을 만드는 조건은 a+b>c 이므로, 먼저 숫자를 정렬 뒤, 가장 큰 수 기준 투포인터를 활용하여 구한다.

2. 시간복잡도 : o(N^2)

3. 자료구조/알고리즘 : 투포인터, 정렬

*/

class Solution {
    public int triangleNumber(int[] nums) {
        // 삼각형을 만들 수 있는 모든 경우의 수 
        // idx 기준

        // a+b > c
        Arrays.sort(nums);
        int ans = 0;

        // 2, 2, 3, 4
        for(int i=nums.length-1; i>1; i--) {
            int c = nums[i];

            int l = 0;
            int r = i-1;
            
            while(l<r) {
                if(nums[l] + nums[r] <= c) l++;
                else {
                    ans+=r-l;
                    r--;
                }
            }
        }
        
        return ans;

    }
}