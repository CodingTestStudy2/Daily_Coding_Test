/*

1. 아이디어 : 조건에 맞춰 or 연산

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 조건문

 */

class Solution {
    public int evenNumberBitwiseORs(int[] nums) {
        int sum = 0;

        for(int i : nums) {
            if(i%2==0) sum |= i;
        }   

        return sum;
    }
}